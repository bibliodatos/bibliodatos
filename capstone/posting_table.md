---
title: Mike Maynard | Google Data Analysis Capstone Project
---
## [Acme Auto Case Study](/capstone/)

#### Oregon County Online Car Postings

| County | Posts |
| --- | ---- |
|	LANE	|	1693	|
|	DESCHUTES	|	1104	|
|	CLACKAMAS	|	1001	|
|	MARION	|	741	|
|	MULTNOMAH	|	678	|
|	JACKSON	|	639	|
|	WASHINGTON	|	361	|
|	LINN	|	201	|
|	JOSEPHINE	|	179	|
|	POLK	|	147	|
|	BENTON	|	143	|
|	DOUGLAS	|	107	|
|	KLAMATH	|	70	|
|	COOS	|	65	|
|	UMATILLA	|	62	|
|	CROOK	|	43	|
|	MALHEUR	|	30	|
|	YAMHILL	|	28	|
|	UNION	|	20	|
|	LINCOLN	|	14	|
|	JEFFERSON	|	8	|
|	CURRY	|	8	|
|	BAKER	|	6	|
|	COLUMBIA	|	5	|
|	TILLAMOOK	|	3	|
|	LAKE	|	3	|
|	GRANT	|	3	|
|	CLATSOP	|	3	|
|	HOOD RIVER	|	2	|
|	WHEELER	|	1	|
|	WASCO	|	1	|
|	WALLOWA	|	1	|
|	MORROW	|	1	|





SQL saved as or_precip_table view in database:

```sql
SELECT
  county AS County,
  COUNT(*) AS Posts
FROM or_vehicles
GROUP BY county
ORDER BY Posts DESC
```








---
[Capstone Project Home](./) | [Key Insights](insights.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-03**
