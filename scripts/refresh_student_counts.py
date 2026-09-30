#!/usr/bin/env python3
import csv
import io
import re
import unicodedata
import urllib.request
from collections import defaultdict, Counter
from pathlib import Path

YEAR = "114"
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = DATA / "generated"
OUT.mkdir(parents=True, exist_ok=True)
UNIV_URL = "https://stats.moe.gov.tw/files/opendata/students.csv"
HS_URL = "https://stats.moe.gov.tw/files/opendata/base2.csv"

def download_csv(url):
    req = urllib.request.Request(url, headers={"User-Agent": "studentman/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        raw = r.read()
    last = None
    for enc in ("utf-8-sig", "utf-8", "cp950", "big5"):
        try:
            rows = list(csv.DictReader(io.StringIO(raw.decode(enc))))
            if rows:
                return rows, list(rows[0].keys()), enc, len(raw)
        except Exception as e:
            last = e
    raise RuntimeError("Cannot decode %s: %s" % (url, last))

def clean(s):
    s = "" if s is None else str(s)
    s = unicodedata.normalize("NFKC", s).replace("台", "臺")
    s = re.sub(r"\s+", "", s)
    return s.replace("／", "/").replace("－", "-").replace("–", "-").replace("—", "-").strip()

def norm_school(s):
    x = clean(s)
    for phrase in ("學校財團法人", "財團法人", "學校法人", "台南家專", "臺南家專", "中信金"):
        x = x.replace(phrase, "")
    return x

def relaxed_school(s):
    x = norm_school(s)
    for prefix in ("國立", "市立", "縣立", "私立"):
        if x.startswith(prefix):
            x = x[len(prefix):]
    return x

def numeric(v):
    s = clean(v).replace(",", "")
    if not s or s in ("-", "—", "NA", "N/A"):
        return 0
    try:
        return int(float(s))
    except ValueError:
        return 0

def pick_field(headers, candidates, contains=()):
    by = {clean(h): h for h in headers}
    for c in candidates:
        if clean(c) in by:
            return by[clean(c)]
    for h in headers:
        ch = clean(h)
        if contains and all(clean(x) in ch for x in contains):
            return h
    return None

def strip_paren(s):
    return re.sub(r"[（(].*?[）)]", "", clean(s))

def dept_stem(s):
    x = strip_paren(s)
    x = re.sub(r"(附設進修學院)$", "", x)
    x = re.sub(r"-.*$", "", x)
    if x.endswith("組") and "系" in x:
        x = x[:x.find("系")+1]
    special = ("國際專班","國際產學專班","國際學生產學合作專班","多元培力專班","香港二技專班")
    if any(k in x for k in special) and "系" in x:
        x = x[:x.find("系")+1]
    x = re.sub(r"(學系|系|研究所|學士學位學程|碩士學位學程|學位學程|科)$", "", x)
    return x

def plausible_univ_dept(target, official):
    t = dept_stem(target)
    o = strip_paren(official)
    on = re.sub(r"(學系|系|研究所|學士學位學程|碩士學位學程|學位學程|科)$", "", o)
    if not t or len(t) < 2:
        return False
    # Only exact/prefix matches are safe. "contains" caused unrelated embedded program names
    # (e.g. 冷凍空調與能源系_機械工程專班) to be counted under 機械工程系.
    return on == t or o.startswith(t)

def parse_targets(s):
    out = []
    base = strip_paren(s)
    for raw in re.split(r"[;；]", base):
        if not raw:
            continue
        p = strip_paren(raw)
        if p.startswith(("114", "115")) and ("未" in p or "招生" in p or "現行" in p):
            continue
        p = re.sub(r"科$", "", p)
        if p:
            out.append(p)
    return out

def hs_dept_key(s):
    return re.sub(r"(科|學程)$", "", strip_paren(s))

univ_rows, univ_headers, univ_enc, univ_bytes = download_csv(UNIV_URL)
hs_rows, hs_headers, hs_enc, hs_bytes = download_csv(HS_URL)

uyear = pick_field(univ_headers, ["學年度"])
uschool = pick_field(univ_headers, ["學校名稱"])
udept = pick_field(univ_headers, ["科系名稱", "科系別"])
utotal = pick_field(univ_headers, ["總計"], contains=("總計",))
if not all((uyear, uschool, udept, utotal)):
    raise RuntimeError("University schema not recognized: %s" % univ_headers)

u114 = [r for r in univ_rows if clean(r.get(uyear)) == YEAR]
u_by_school = defaultdict(list)
for r in u114:
    u_by_school[relaxed_school(r.get(uschool))].append(r)

with open(DATA / "university-targets.csv", encoding="utf-8") as f:
    targets = list(csv.DictReader(f))

ugroups = defaultdict(list)
for t in targets:
    dept = clean(t["department"])
    non_enrollment = ("實驗室" in dept or "研究中心" in dept or "聲學智能與數據科學" in dept or "噪音振動研究" in dept)
    if non_enrollment:
        key = (relaxed_school(t["school"]), "N/A:" + t["row"])
    else:
        window = clean(t.get("window_email") or "").lower() or clean(t.get("window_name") or "") or dept
        key = (relaxed_school(t["school"]), window)
    ugroups[key].append(t)

uout = []
for (school_key, window), group in ugroups.items():
    school = group[0]["school"]
    if window.startswith("N/A:"):
        uout.append({
            "school": school, "window": group[0].get("window_name",""), "window_email": group[0].get("window_email",""),
            "target_rows": "|".join(x["row"] for x in group), "target_departments": "；".join(x["department"] for x in group),
            "official_total_114": "", "matched_official_departments": "", "official_school_departments": "", "status": "N/A_NON_ENROLLMENT",
            "unmatched_target_departments": ""
        })
        continue
    candidates = u_by_school.get(school_key, [])
    if not candidates:
        keys = [k for k in u_by_school if school_key in k or k in school_key]
        if len(keys) == 1:
            candidates = u_by_school[keys[0]]
    unique = {}
    unmatched = []
    for t in group:
        hits = [r for r in candidates if plausible_univ_dept(t["department"], r.get(udept,""))]
        if not hits:
            unmatched.append(t["department"])
        for r in hits:
            ident = tuple((h, clean(r.get(h))) for h in univ_headers)
            unique[ident] = r
    rows = list(unique.values())
    total = sum(numeric(r.get(utotal)) for r in rows)
    details = ["%s=%s" % (r.get(udept), numeric(r.get(utotal))) for r in sorted(rows, key=lambda z: clean(z.get(udept)))]
    if not candidates:
        status = "NO_SCHOOL_MATCH"
    elif not rows:
        status = "NO_DEPT_MATCH"
    elif unmatched:
        status = "REVIEW_PARTIAL"
    else:
        status = "AUTO_MATCHED"
    uout.append({
        "school": school, "window": group[0].get("window_name",""), "window_email": group[0].get("window_email",""),
        "target_rows": "|".join(x["row"] for x in group), "target_departments": "；".join(x["department"] for x in group),
        "official_total_114": total if rows else "", "matched_official_departments": "；".join(details),
        "official_school_departments": "；".join(sorted(set(str(r.get(udept,"")) for r in candidates))),
        "status": status, "unmatched_target_departments": "；".join(unmatched)
    })

for x in uout:
    if x["school"] == "南開科技大學" and x["window_email"] == "deshau@nkut.edu.tw":
        x["status"] = "VERIFIED_ALIAS"
        x["unmatched_target_departments"] = ""
    elif "台南應用科技大學" in x["school"] and x["window_email"] == "emvcda@mail.tut.edu.tw":
        x["status"] = "VERIFIED_ALIAS"
        x["unmatched_target_departments"] = ""
    elif x["school"] == "亞洲大學" and "創意設計學院不分系國際設計學士班" in x["target_departments"]:
        # Exact program exists in older/public metadata but has no row in official 114 student-count dataset.
        x["official_total_114"] = 0
        x["status"] = "NO_114_STUDENT_RECORD"

ufields = ["school","window","window_email","target_rows","target_departments","official_total_114","matched_official_departments","official_school_departments","status","unmatched_target_departments"]
with open(OUT / "university-window-counts-114.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ufields); w.writeheader(); w.writerows(uout)

hyear = pick_field(hs_headers, ["學年度"])
hcode = pick_field(hs_headers, ["學校代碼"])
hschool = pick_field(hs_headers, ["學校名稱"])
hdept = pick_field(hs_headers, ["科系名稱", "科別名稱", "科別"])
if not all((hyear, hschool, hdept)):
    raise RuntimeError("High-school schema not recognized: %s" % hs_headers)

htotal = pick_field(hs_headers, ["學生數總計", "學生數合計", "總計"])
grade_sex_cols = [h for h in hs_headers if ("學生數" in clean(h) and ("男" in clean(h) or "女" in clean(h)))]
if not htotal and not grade_sex_cols:
    raise RuntimeError("Cannot identify high-school count columns: %s" % hs_headers)

h114 = [r for r in hs_rows if clean(r.get(hyear)) == YEAR]
h_by_code = defaultdict(list)
h_by_school = defaultdict(list)
for r in h114:
    h_by_code[clean(r.get(hcode))].append(r)
    h_by_school[relaxed_school(r.get(hschool))].append(r)

def hs_row_total(r):
    if htotal:
        return numeric(r.get(htotal))
    return sum(numeric(r.get(c)) for c in grade_sex_cols)

with open(DATA / "highschool-targets.csv", encoding="utf-8") as f:
    htargets = list(csv.DictReader(f))

HS_ALIASES = {
    "193404": {"服裝設計": ["流行服飾"]},
    "120401": {"生物機電": ["生物產業機電"]},
    "710401": {"機工": ["機械"]},
    "091410": {"多媒體設計": ["多媒體技術"]},
    "101406": {"多媒體設計": ["多媒體技術"]},
}
# Historical 114 programs that the invitation sheet intentionally retained even if 115招生已停/改制.
HS_114_TARGET_OVERRIDE = {
    "381303": ["室內空間設計"],  # 私立大誠高中：114仍有8人
    "151306": ["多媒體設計", "室內設計", "廣告設計", "服裝設計"],  # 海星高中114仍有設計相關在學生
    "011316": [],  # 私立格致高中：114官方資料無設計群學生
}
HS_NOT_OPEN_114 = {"044428"}  # 新竹縣自強高工115學年度首招，114無在學生

hout = []
for t in htargets:
    code = clean(t["school_code"])
    candidates = h_by_code.get(code, []) or h_by_school.get(relaxed_school(t["school"]), [])
    wanted = parse_targets(t["relevant_departments"])
    if code in HS_114_TARGET_OVERRIDE:
        wanted = list(HS_114_TARGET_OVERRIDE[code])
    by_key = defaultdict(list)
    for r in candidates:
        by_key[hs_dept_key(r.get(hdept,""))].append(r)
    matched_rows = {}
    unmatched = []
    for target in wanted:
        key = hs_dept_key(target)
        hits = list(by_key.get(key, []))
        if not hits:
            synonyms = {
                "室內設計": ["室內空間設計"], "室內空間設計": ["室內設計"],
                "汽車": ["汽車"], "資訊": ["資訊"], "圖文傳播": ["圖文傳播"],
                "廣告設計": ["廣告設計"], "美工": ["美工"], "多媒體技術": ["多媒體技術"]
            }
            for alt in synonyms.get(key, []):
                hits.extend(by_key.get(alt, []))
            for alt in HS_ALIASES.get(code, {}).get(key, []):
                hits.extend(by_key.get(hs_dept_key(alt), []))
        if not hits:
            unmatched.append(target)
        for r in hits:
            ident = tuple((h, clean(r.get(h))) for h in hs_headers)
            matched_rows[ident] = r
    total = sum(hs_row_total(r) for r in matched_rows.values())
    details = ["%s=%s" % (r.get(hdept), hs_row_total(r)) for r in sorted(matched_rows.values(), key=lambda z: clean(z.get(hdept)))]
    if code in HS_NOT_OPEN_114 and not candidates:
        status = "NOT_OPEN_114"
        total = 0
    elif not candidates:
        status = "NO_SCHOOL_MATCH"
    elif code in HS_114_TARGET_OVERRIDE and not wanted:
        status = "NO_114_TARGET_DEPT"
        total = 0
    elif not wanted:
        status = "NO_ACTIVE_TARGET"
    elif not matched_rows:
        # School exists in the official 114 file but none of the requested target departments do.
        status = "NO_114_TARGET_DEPT"
        total = 0
    elif unmatched:
        # We have exact official counts for the present target departments; unmatched names are absent from 114 data.
        status = "MATCHED_WITH_114_ABSENCES"
    else:
        status = "AUTO_MATCHED"
    hout.append({
        "school": t["school"], "school_code": t["school_code"], "target_departments": t["relevant_departments"],
        "official_relevant_total_114": total if matched_rows else "", "matched_official_departments": "；".join(details),
        "official_school_departments": "；".join("%s=%s" % (r.get(hdept), hs_row_total(r)) for r in sorted(candidates, key=lambda z: clean(z.get(hdept)))),
        "status": status, "unmatched_target_departments": "；".join(unmatched),
        "review_note": (
            "114官方資料中部分原名科別已不存在；合計僅計現存正式列" if status == "MATCHED_WITH_114_ABSENCES"
            else "114官方資料有學校但無所列目標科別" if status == "NO_114_TARGET_DEPT"
            else "115學年度首招，114無在學生" if status == "NOT_OPEN_114"
            else ""
        )
    })

hfields = ["school","school_code","target_departments","official_relevant_total_114","matched_official_departments","official_school_departments","status","unmatched_target_departments","review_note"]
with open(OUT / "highschool-relevant-counts-114.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=hfields); w.writeheader(); w.writerows(hout)

# Cross-window duplicate audit: an exact official row should not be counted by two different invitation windows at the same school.
u_row_owners = defaultdict(set)
for x in uout:
    if not x.get("matched_official_departments"):
        continue
    for detail in x["matched_official_departments"].split("；"):
        if detail:
            u_row_owners[(relaxed_school(x["school"]), detail)].add((x["window_email"], x["target_departments"]))
u_duplicates = {k:v for k,v in u_row_owners.items() if len(v) > 1}

uc = Counter(x["status"] for x in uout)
hc = Counter(x["status"] for x in hout)
lines = [
    "# Student count batch validation", "",
    "- Academic year: %s" % YEAR,
    "- University source: %s (%s bytes, %s)" % (UNIV_URL, univ_bytes, univ_enc),
    "- High-school source: %s (%s bytes, %s)" % (HS_URL, hs_bytes, hs_enc),
    "", "## University", "- Target windows: %s" % len(uout)
]
for k,v in sorted(uc.items()):
    lines.append("- %s: %s" % (k,v))
lines.append("- Cross-window duplicate official rows: %s" % len(u_duplicates))
lines += ["", "### University rows requiring review", ""]
for x in uout:
    if x["status"] not in ("AUTO_MATCHED","N/A_NON_ENROLLMENT","VERIFIED_ALIAS"):
        lines.append("- %s｜%s｜%s｜unmatched=%s｜official=%s" % (x["school"], x["target_departments"], x["status"], x["unmatched_target_departments"], x.get("official_school_departments","")))
if u_duplicates:
    lines += ["", "### Cross-window duplicate official rows", ""]
    for (school_key, detail), owners in sorted(u_duplicates.items()):
        lines.append("- %s｜%s｜owners=%s" % (school_key, detail, sorted(owners)))
lines += ["", "## High school", "- Target schools: %s" % len(hout)]
for k,v in sorted(hc.items()):
    lines.append("- %s: %s" % (k,v))
lines += ["", "### High-school rows requiring review", ""]
for x in hout:
    if x["status"] not in ("AUTO_MATCHED","MATCHED_WITH_114_ABSENCES","NO_114_TARGET_DEPT","NOT_OPEN_114"):
        lines.append("- %s (%s)｜%s｜unmatched=%s｜official=%s" % (x["school"], x["school_code"], x["status"], x["unmatched_target_departments"], x.get("official_school_departments","")))
lines += ["", "## Source schemas", "", "### University headers", "", " | ".join(univ_headers), "", "### High-school headers", "", " | ".join(hs_headers), ""]
(OUT / "validation-report.md").write_text("\n".join(lines), encoding="utf-8")

print("University status:", dict(uc))
print("High-school status:", dict(hc))
