# Student count batch validation

- Academic year: 114
- University source: https://stats.moe.gov.tw/files/opendata/students.csv (2883507 bytes, utf-8-sig)
- High-school source: https://stats.moe.gov.tw/files/opendata/base2.csv (6503868 bytes, utf-8-sig)

## University
- Target windows: 213
- AUTO_MATCHED: 203
- N/A_NON_ENROLLMENT: 7
- NO_114_STUDENT_RECORD: 1
- VERIFIED_ALIAS: 2
- Cross-window duplicate official rows: 13

### University rows requiring review

- 亞洲大學｜創意設計學院不分系國際設計學士班｜NO_114_STUDENT_RECORD｜unmatched=創意設計學院不分系國際設計學士班｜official=人工智慧博士學位學程；人工智慧學系；健康產業管理學系；創意商品設計學系；創新產業博士學位學程；外國語文學系；學士後獸醫學系；學士後護理學系；室內設計學系；幼兒教育學系；心理學系；數位媒體設計學系；新興產業策略與發展博士學位學程；時尚設計學系；智慧健康先進管理技術博士學位學程；會計與資訊學系；物理治療學系；生物資訊與醫學工程學系；社會工作學系；管理學院進修學士學位學程；經營管理學系；經營管理學系企業經濟與策略博士班；職能治療學系；聽力暨語言治療學系；視光學系；護理學系；財務金融學系；財務金融學系114秋季班元大國際產業人才教育財務金融碩士專班；財務金融學系財務金融碩士專班；財經法律學系；資訊傳播學系；資訊工程學系；醫學檢驗暨生物技術學系；長期照護學系；食品營養與保健生技學系

### Cross-window duplicate official rows

- 僑光科技大學｜機械與電腦輔助工程系=179｜owners=[('eiwang@ocu.edu.tw', '機械與電腦輔助工程系（原電腦輔助工業設計系）'), ('mcae@ocu.edu.tw', '機械與電腦輔助工程系')]
- 僑光科技大學｜機械與電腦輔助工程系=329｜owners=[('eiwang@ocu.edu.tw', '機械與電腦輔助工程系（原電腦輔助工業設計系）'), ('mcae@ocu.edu.tw', '機械與電腦輔助工程系')]
- 勤益科技大學｜冷凍空調與能源系_機械工程專班=28｜owners=[('cnhsu@ncut.edu.tw', '冷凍空調與能源系'), ('cyhuang@ncut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程科=1｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程科=6｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程系=106｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程系=386｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程系=389｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程系=43｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程系機電整合碩士在職專班=77｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程系機電整合碩士班=230｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程系機電整合碩士班=31｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]
- 臺北科技大學｜機械工程系產學訓專班=6｜owners=[('jshuang@tpcu.edu.tw', '機械工程系'), ('tsf@ntut.edu.tw', '機械工程系')]

## High school
- Target schools: 176
- AUTO_MATCHED: 167
- MATCHED_WITH_114_ABSENCES: 6
- NOT_OPEN_114: 1
- NO_114_TARGET_DEPT: 2

### High-school rows requiring review


## Source schemas

### University headers

學年度 | 學校代碼 | 學校名稱 | 科系代碼 | 科系名稱 | 日間∕進修別 | 等級別 | 總計 | 男生計 | 女生計 | 華語先修生男生 | 華語先修生女生 | 一年級男生 | 一年級女生 | 二年級男生 | 二年級女生 | 三年級男生 | 三年級女生 | 四年級男生 | 四年級女生 | 五年級男生 | 五年級女生 | 六年級男生 | 六年級女生 | 七年級男生 | 七年級女生 | 延修生男生 | 延修生女生 | 縣市名稱 | 體系別

### High-school headers

學年度 | 縣市代碼 | 縣市名稱 | 學校代碼 | 學校名稱 | 等級別 | 等級名稱 | 日夜別 | 日夜別名稱 | 群別代碼 | 群別名稱 | 科系代碼 | 科系名稱 | 一年級班級數 | 二年級班級數 | 三年級班級數 | 四年級班級數 | 一年級男學生數 | 一年級女學生數 | 二年級男學生數 | 二年級女學生數 | 三年級男學生數 | 三年級女學生數 | 四年級男學生數 | 四年級女學生數 | 延修生男學生數 | 延修生女學生數 | 上學年畢業生數男 | 上學年畢業生數女
