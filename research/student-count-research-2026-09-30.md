# StudentMan｜114學年度學生人數查核完成報告

**Status: COMPLETE**  
查核完成日：2026-09-30

> 本報告只記錄人數研究結果；主 Excel 尚未回寫，依使用者要求等確認後再更新。

## 1. 最終統計規則

### 大專
以「同一邀請／行政窗口」為統計單位。同一窗口之：
學士、進修、碩士、碩士在職、博士、國際專班、技優專班、產學專班、二專／五專等 **全部合併**。

不同窗口才分列。研究中心／實驗室若非獨立招生單位不重複計學生數。

### 高中職
以學校為統計單位，把同校本案相關科別的 **114學年度實際在學人數** 加總。

### 人數來源
只採正式在學數，不使用招生名額或舊年度推估：
- 大專：教育部統計處 `students.csv`
- 高中職：教育部統計處 `base2.csv`
- 必要時再以教育部 UDB 114「學1-1」頁交叉確認

## 2. 完成度

### 大專
- 原 Excel：243 列
- 合併後邀請窗口：**212**
- AUTO_MATCHED：195
- VERIFIED_ALIAS：5
- VERIFIED_OFFICIAL_OVERRIDE：3
- VERIFIED_UDB_WEB_ADJUSTMENT：1
- FINAL_ZERO_NO_114_RECORD：1
- N/A_NON_ENROLLMENT：7
- 跨窗口重複官方學生列：**0**
- 待人工判讀：**0**

### 高中職
- 學校：**176**
- AUTO_MATCHED：167
- MATCHED_WITH_114_ABSENCES：6
- NOT_OPEN_114：1
- NO_114_TARGET_DEPT：2
- 待人工判讀：**0**

## 3. 特殊狀態說明

- **MATCHED_WITH_114_ABSENCES**：原邀請名單中有部分舊科名，但114官方資料已不存在；總數只計114仍正式存在的相關科別。
- **NOT_OPEN_114**：新竹縣自強高工115學年度首招，因此114人數為0。
- **NO_114_TARGET_DEPT**：學校在114存在，但原名單所列的目標科別在114正式資料為0／不存在。
- **FINAL_ZERO_NO_114_RECORD**：亞洲大學「創意設計學院不分系國際設計學士班」在114教育部學生原始檔無正式在學列，因此114計0；不沿用舊年度4人。
- **N/A_NON_ENROLLMENT**：研究中心／實驗室不是獨立招生單位，不另外計學生數。

## 4. 重要校正

- 北科車輛工程窗口：114 UDB = 日間200＋進修126＋附設進院1＋碩專57＋碩士90 = **474**
- 彰師車輛科技研究所：**27**（主檔舊值33）
- 彰師智慧車輛工程學系：**19**（主檔舊值30）
- 逢甲室內設計窗口：日間143＋進修125 = **268**（主檔舊值286）
- 吳鳳機械與智慧製造工程系：新名317＋改名前仍在學專班51 = **368**
- 臺中市大明高中：**352**（主檔舊值342）
- 嘉義高商廣告設計科：**186**（主檔舊值196）

## 5. Canonical files

- 大專最終結果：`data/generated/university-window-counts-114.csv`
- 高中職最終結果：`data/generated/highschool-relevant-counts-114.csv`
- 最終驗證：`data/generated/validation-report.md`
- 大專來源映射：`data/university-targets.csv`
- 高中職來源映射：`data/highschool-targets.csv`
- 自動計算程式：`scripts/refresh_student_counts.py`
- GitHub Actions：`.github/workflows/refresh-student-counts.yml`

## 6. 下一階段

人數研究已完成。下一階段若要執行，應直接以 canonical CSV 回寫「格式統一版 Excel」，同時依大專 212 個窗口重新合併原本重複列；不要再回到早期逐列人數口徑。
