# Excel final backfill — 2026-09-30

## Result

主 Excel 已依 GitHub canonical student-count results 完成最終回填與整理。

Final workbook:
`台灣設計_汽車_引擎_機械電機航太_NVH_全台學校邀請名單_最終回填版_20260930.xlsx`

## University

- Source workbook rows: 243
- Final invitation / administrative windows: 212
- Same-window bachelor / continuing / master / executive master / doctoral / international / industry / technical / 2-year / 5-year programs merged
- Manual review remaining: 0
- Non-enrollment research centers / labs: 7 N/A
- Cross-window duplicate official student rows: 0
- Canonical source: `data/generated/university-window-counts-114.csv`

Verified special corrections retained:
- NTUT Vehicle Engineering window: 474, including UDB 附設進院 1
- NCUE Vehicle Technology Institute: 27
- NCUE Intelligent Vehicle Engineering: 19
- FCU Interior Design window: 268
- WFU Mechanical & Intelligent Manufacturing window: 368

## High school

- Final schools: 176
- FINAL_SCOPE_MATCHED: 174
- FINAL_NOT_OPEN_114: 1
- FINAL_ZERO_NO_RELEVANT_114_DEPT: 1
- Manual review remaining: 0
- Canonical source: `data/generated/highschool-scope-counts-114.csv`

The workbook now writes the official 114 scope total to the student-count column and writes official department/count detail to the department-detail column. It does not use admissions quota, older-year counts, or estimated values as 114 enrollment.

## Workbook changes

- Preserved the 3-sheet structure.
- University sheet physically consolidated from 243 source rows to 212 invitation windows; residual old rows blanked.
- High-school sheet kept one row per school (176) and filled all 114 official scope totals.
- Updated summary sheet to remove obsolete “still pending” statements.
- Preserved existing principal / department / office contact data and reconciled merged-window contact conflicts against canonical window identity.
- Formula/error scan: 0 matches for REF/DIV0/VALUE/NAME/N/A formula errors.
