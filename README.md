# studentman

台灣設計／汽車／引擎／機械電機／航太／NVH 全台學校邀請名單資料研究。

## 目前狀態

**114 學年度學生人數查核已完成；主 Excel 已完成最終回填與整理。**

- 大專：**212 個合併邀請窗口**，待人工判讀 **0**
- 高中職：**176 校**，待人工判讀 **0**
  - 174 校有 114 現行相關科別
  - 1 校 114 尚未開辦（自強高工，115 首招）
  - 1 校 114 無符合範圍之相關科別（格致高中）
- 大專跨窗口重複官方學生列：**0**

## Canonical results

- 大專：`data/generated/university-window-counts-114.csv`
- 高中職：`data/generated/highschool-scope-counts-114.csv`
- 驗證報告：`data/generated/validation-report.md`

> `data/generated/highschool-relevant-counts-114.csv` 僅為舊 Excel 科別逐項比對紀錄，不是最終回填來源。

## 統計口徑

- 大專：同一邀請／行政窗口之學士、進修、碩士、碩專、博士、國際、技優、產學、二專／五專等全部合併。
- 高中職：一校一筆；直接以教育部 114 現行科別，彙總設計／汽車／機械／機電／電機／電子／資訊／控制／冷凍空調／飛機修護／航空電子等相關科別。
- 排除商管誤判：電子商務、商用資訊、資訊管理、商業資訊、商務資訊。
- 只採正式在學人數，不用招生名額或舊年度推估。

請從 [data/README.md](data/README.md) 與 [research/student-count-research-2026-09-30.md](research/student-count-research-2026-09-30.md) 開始閱讀。


## Excel 最終回填

- 完成日：**2026-09-30**
- 最終檔名：`台灣設計_汽車_引擎_機械電機航太_NVH_全台學校邀請名單_最終回填版_20260930.xlsx`
- 大專：原 243 列依同一邀請／行政窗口合併為 **212 個窗口**
  - 114 正式學生數待人工判讀：**0**
  - 非獨立招生研究中心／實驗室：**7 筆 N/A**
  - 跨窗口重複官方學生列：**0**
- 高中職：**176 校**
  - FINAL_SCOPE_MATCHED：**174**
  - 114 尚未開辦：**1**
  - 114 無符合本案範圍科別：**1**
  - 待人工判讀：**0**
- Excel 回填來源只採 canonical 結果：
  - `data/generated/university-window-counts-114.csv`
  - `data/generated/highschool-scope-counts-114.csv`
- Excel 二進位檔不作為 repo SSOT；repo 以 canonical CSV、validation report 與本回填紀錄作可追溯依據。
