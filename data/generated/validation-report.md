# Student count batch validation

- Academic year: 114
- University source: https://stats.moe.gov.tw/files/opendata/students.csv (2883507 bytes, utf-8-sig)
- High-school source: https://stats.moe.gov.tw/files/opendata/base2.csv (6503868 bytes, utf-8-sig)

## University
- Target windows: 212
- AUTO_MATCHED: 195
- FINAL_ZERO_NO_114_RECORD: 1
- N/A_NON_ENROLLMENT: 7
- VERIFIED_ALIAS: 5
- VERIFIED_OFFICIAL_OVERRIDE: 3
- VERIFIED_UDB_WEB_ADJUSTMENT: 1
- Cross-window duplicate official rows: 0

### University rows requiring review


## High school
- Target schools: 176
- AUTO_MATCHED: 167
- MATCHED_WITH_114_ABSENCES: 6
- NOT_OPEN_114: 1
- NO_114_TARGET_DEPT: 2
- Existing-count corrections: 2

### High-school existing-count corrections

- 臺中市大明高中 (061310)｜主檔既有值342；114教育部正式科別資料為352，應採114官方值
- 國立嘉義高商 (200406)｜主檔既有值196；114教育部正式科別資料為186，應採114官方值

### High-school rows requiring review


## Source schemas

### University headers

學年度 | 學校代碼 | 學校名稱 | 科系代碼 | 科系名稱 | 日間∕進修別 | 等級別 | 總計 | 男生計 | 女生計 | 華語先修生男生 | 華語先修生女生 | 一年級男生 | 一年級女生 | 二年級男生 | 二年級女生 | 三年級男生 | 三年級女生 | 四年級男生 | 四年級女生 | 五年級男生 | 五年級女生 | 六年級男生 | 六年級女生 | 七年級男生 | 七年級女生 | 延修生男生 | 延修生女生 | 縣市名稱 | 體系別

### High-school headers

學年度 | 縣市代碼 | 縣市名稱 | 學校代碼 | 學校名稱 | 等級別 | 等級名稱 | 日夜別 | 日夜別名稱 | 群別代碼 | 群別名稱 | 科系代碼 | 科系名稱 | 一年級班級數 | 二年級班級數 | 三年級班級數 | 四年級班級數 | 一年級男學生數 | 一年級女學生數 | 二年級男學生數 | 二年級女學生數 | 三年級男學生數 | 三年級女學生數 | 四年級男學生數 | 四年級女學生數 | 延修生男學生數 | 延修生女學生數 | 上學年畢業生數男 | 上學年畢業生數女
