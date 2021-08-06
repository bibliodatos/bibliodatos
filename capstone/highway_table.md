---
title: Mike Maynard | Google Data Analysis Capstone Project
---
## [Acme Auto Case Study](/capstone/)

#### Oregon County Highway Miles


| County | miles_per_vehicle | score |
| ------ | ------ | ----- |
|	GILLIAM	|	73780	|	100	|
|	SHERMAN	|	53069	|	100	|
|	BAKER	|	17577	|	100	|
|	MORROW	|	16611	|	94	|
|	WASCO	|	13910	|	74	|
|	HOOD RIVER	|	13036	|	68	|
|	MALHEUR	|	12313	|	63	|
|	HARNEY	|	11802	|	59	|
|	WHEELER	|	11764	|	59	|
|	UNION	|	10185	|	47	|
|	DOUGLAS	|	10176	|	47	|
|	LINN	|	9700	|	44	|
|	UMATILLA	|	9564	|	43	|
|	CLATSOP	|	9259	|	41	|
|	TILLAMOOK	|	8822	|	38	|
|	JEFFERSON	|	8750	|	37	|
|	LAKE	|	8173	|	33	|
|	LINCOLN	|	7741	|	30	|
|	KLAMATH	|	7041	|	25	|
|	GRANT	|	6864	|	24	|
|	MARION	|	6226	|	19	|
|	POLK	|	5741	|	16	|
|	JOSEPHINE	|	5515	|	14	|
|	MULTNOMAH	|	5321	|	13	|
|	WALLOWA	|	5000	|	10	|
|	CLACKAMAS	|	4972	|	10	|
|	COOS	|	4965	|	10	|
|	COLUMBIA	|	4962	|	10	|
|	JACKSON	|	4941	|	10	|
|	CURRY	|	4849	|	9	|
|	LANE	|	4747	|	8	|
|	YAMHILL	|	4588	|	7	|
|	CROOK	|	4258	|	5	|
|	WASHINGTON	|	3785	|	1	|
|	DESCHUTES	|	3684	|	1	|
|	BENTON	|	3580	|	0	|

SQL query saved as *or_highway_miles_score* in database:

```sql
SELECT
	m.county AS county,
	m.miles_per_vehicle,
	CASE
		WHEN m.miles_per_vehicle > 17500 THEN 100
		ELSE
			CAST(ROUND(((m.miles_per_vehicle - 3580) / 13920.0) * 100) AS INTEGER)
		END
	AS score,
	'|'
FROM or_highway_miles m
```



Data sources: [Kaggle](https://www.kaggle.com/bibliodatos/oregon-vehicle-miles-travelled) |  [Oregon DOT](
Https://www.oregon.gov/odot/Data/documents/VMT_County.xls)


---
[Acme Project Home / Table of Contents](./) | [Key Insights](insights.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-03**
