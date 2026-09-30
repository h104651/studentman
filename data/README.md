# StudentMan data

本目錄以 **114 學年度正式在學學生數** 為唯一人數口徑。

## Canonical results

### 大專院校
- `generated/university-window-counts-114.csv`
- 統計單位：同一邀請／行政窗口
- 學士、進修、碩士、碩專、博士、國際專班、技優、產學、五專/二專等，只要屬同一窗口即合併
- 最終窗口數：**212**
- 跨窗口重複官方學生列：**0**
- 非獨立招生研究中心／實驗室：**7（N/A）**
- 114 官方學生原始檔無在學紀錄：**1（亞洲大學創意設計學院不分系國際設計學士班，114計0）**

### 高中職
- `generated/highschool-relevant-counts-114.csv`
- 統計單位：學校
- 同校所有本案相關科別合併
- 最終學校數：**176**
- 114 明確為 0 的項目會輸出數字 **0**，不留空白

## Validation
- `generated/validation-report.md`
- 大專待人工判讀：**0**
- 高中職待人工判讀：**0**
- 大專跨窗口重複：**0**

## Source mapping
- `university-targets.csv`：由格式統一版 Excel 匯出的 243 個原始大專列，依實際窗口合併為 212 個結果
- `highschool-targets.csv`：176 校及其相關科別目標

## Official sources
- 大專：教育部統計處 `https://stats.moe.gov.tw/files/opendata/students.csv`
- 高中職：教育部統計處 `https://stats.moe.gov.tw/files/opendata/base2.csv`
- 北科車輛工程另以教育部 UDB 114「學1-1」頁補入 OpenData 缺少的附設進院 1 人，因此最終為 474。

## Important corrections against the previous workbook
- 臺中市大明高中：342 → **352**
- 國立嘉義高商：196 → **186**
- 國立彰化師範大學車輛科技研究所：33 → **27**
- 國立彰化師範大學智慧車輛工程學系：30 → **19**
- 逢甲大學室內設計窗口：286 → **268**
- 北科車輛工程窗口：**474**（含附設進院 1）
- 吳鳳機械與智慧製造工程系：**368**（納入改名前「機械工程系」仍在學的專班）

## File status
`student-count-findings-2026-09-30.csv` 已改為最終大專結果的同步副本，不再保留早期手動最低值，避免同一 repo 出現兩套數字。
