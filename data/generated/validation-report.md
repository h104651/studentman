# Student count batch validation

- Academic year: 114
- University source: https://stats.moe.gov.tw/files/opendata/students.csv (2883507 bytes, utf-8-sig)
- High-school source: https://stats.moe.gov.tw/files/opendata/base2.csv (6503868 bytes, utf-8-sig)

## University
- Target windows: 213
- AUTO_MATCHED: 203
- N/A_NON_ENROLLMENT: 7
- NO_DEPT_MATCH: 1
- REVIEW_PARTIAL: 2

### University rows requiring review

- 南開科技大學｜國際產學合作車輛相關專班；車輛工程系；車輛與機電產業研究所；車輛與機電產業碩士專班；車輛零組件相關專班｜REVIEW_PARTIAL｜unmatched=國際產學合作車輛相關專班；車輛零組件相關專班
- 台南家專學校財團法人台南應用科技大學｜視覺傳達創新應用設計碩士班；視覺傳達設計系｜REVIEW_PARTIAL｜unmatched=視覺傳達創新應用設計碩士班
- 亞洲大學｜創意設計學院不分系國際設計學士班｜NO_DEPT_MATCH｜unmatched=創意設計學院不分系國際設計學士班

## High school
- Target schools: 176
- AUTO_MATCHED: 156
- NO_ACTIVE_TARGET: 3
- NO_DEPT_MATCH: 7
- NO_SCHOOL_MATCH: 1
- REVIEW_PARTIAL: 9

### High-school rows requiring review

- 私立大同高中 (341302)｜REVIEW_PARTIAL｜unmatched=機械；電子
- 私立大誠高中 (381303)｜NO_ACTIVE_TARGET｜unmatched=
- 市立光復高中 (014363)｜NO_DEPT_MATCH｜unmatched=多媒體設計學程
- 私立格致高中 (011316)｜NO_ACTIVE_TARGET｜unmatched=
- 私立淡江高中 (011301)｜NO_DEPT_MATCH｜unmatched=廣告設計學程
- 私立豫章工商 (011427)｜REVIEW_PARTIAL｜unmatched=多媒體設計
- 國立基隆商工 (170404)｜REVIEW_PARTIAL｜unmatched=美工；廣告設計學程
- 縣立自強高工 (044428)｜NO_SCHOOL_MATCH｜unmatched=資訊
- 市立大甲高中 (063303)｜NO_DEPT_MATCH｜unmatched=廣告設計學程
- 市立臺中家商 (193404)｜REVIEW_PARTIAL｜unmatched=服裝設計
- 國立員林崇實高工 (070409)｜REVIEW_PARTIAL｜unmatched=裝潢技術
- 私立大成商工 (091410)｜NO_DEPT_MATCH｜unmatched=多媒體設計；資訊
- 私立萬能工商 (101406)｜REVIEW_PARTIAL｜unmatched=多媒體設計
- 國立新豐高中 (110302)｜NO_DEPT_MATCH｜unmatched=廣告設計學程
- 私立陽明工商 (111419)｜NO_DEPT_MATCH｜unmatched=家具木工科(114仍有在學資料
- 國立旗山農工 (120401)｜REVIEW_PARTIAL｜unmatched=生物機電
- 市立三民家商 (533402)｜NO_DEPT_MATCH｜unmatched=多媒體設計
- 市立中正高工 (593401)｜REVIEW_PARTIAL｜unmatched=圖文傳播
- 私立海星高中 (151306)｜NO_ACTIVE_TARGET｜unmatched=
- 國立金門農工 (710401)｜REVIEW_PARTIAL｜unmatched=機工

## Source schemas

### University headers

學年度 | 學校代碼 | 學校名稱 | 科系代碼 | 科系名稱 | 日間∕進修別 | 等級別 | 總計 | 男生計 | 女生計 | 華語先修生男生 | 華語先修生女生 | 一年級男生 | 一年級女生 | 二年級男生 | 二年級女生 | 三年級男生 | 三年級女生 | 四年級男生 | 四年級女生 | 五年級男生 | 五年級女生 | 六年級男生 | 六年級女生 | 七年級男生 | 七年級女生 | 延修生男生 | 延修生女生 | 縣市名稱 | 體系別

### High-school headers

學年度 | 縣市代碼 | 縣市名稱 | 學校代碼 | 學校名稱 | 等級別 | 等級名稱 | 日夜別 | 日夜別名稱 | 群別代碼 | 群別名稱 | 科系代碼 | 科系名稱 | 一年級班級數 | 二年級班級數 | 三年級班級數 | 四年級班級數 | 一年級男學生數 | 一年級女學生數 | 二年級男學生數 | 二年級女學生數 | 三年級男學生數 | 三年級女學生數 | 四年級男學生數 | 四年級女學生數 | 延修生男學生數 | 延修生女學生數 | 上學年畢業生數男 | 上學年畢業生數女
