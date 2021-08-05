---
title: Mike Maynard | Google Data Analysis Capstone Project - Analysis Summary
---
## [Acme Auto Case Study](/capstone/)

| County | Precip |
| --- | ---- |
|	MORROW	|	12	|
|	CROOK	|	13	|
|	HARNEY	|	13	|
|	JEFFERSON	|	13	|
|	MALHEUR	|	13	|
|	GILLIAM	|	14	|
|	SHERMAN	|	14	|
|	WHEELER	|	15	|
|	LAKE	|	16	|
|	DESCHUTES	|	17	|
|	UMATILLA	|	17	|
|	GRANT	|	18	|
|	WASCO	|	18	|
|	UNION	|	20	|
|	WALLOWA	|	21	|
|	BAKER	|	22	|
|	KLAMATH	|	24	|
|	JACKSON	|	26	|
|	JOSEPHINE	|	36	|
|	HOOD RIVER	|	42	|
|	YAMHILL	|	43	|
|	DOUGLAS	|	44	|
|	WASHINGTON	|	44	|
|	MULTNOMAH	|	45	|
|	MARION	|	49	|
|	POLK	|	50	|
|	COLUMBIA	|	52	|
|	CLACKAMAS	|	53	|
|	LINN	|	53	|
|	LANE	|	55	|
|	BENTON	|	58	|
|	COOS	|	65	|
|	LINCOLN	|	80	|
|	CURRY	|	81	|
|	CLATSOP	|	87	|
|	TILLAMOOK	|	89	|


SQL saved as or_precip_table view in database:

```sql
  SELECT
  '|',  county AS County,
  '|', precip AS Precip,
  '|'
  FROM or_climate
  ORDER BY precip ASC
```








---
[Capstone Project Home](./) | [Key Insights](insights.html) | [Table of Contents](index.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-03**
