---
title: Mike Maynard | Google Data Analysis Capstone Project
---
## [Acme Auto Case Study](/capstone/)

#### Oregon County Car Registration Growth

| County | Growth |
| --- | ---- |
|	DESCHUTES	|	17	|
|	CROOK	|	16	|
|	JEFFERSON	|	13	|
|	POLK	|	13	|
|	CLATSOP	|	12	|
|	LINN	|	12	|
|	MARION	|	12	|
|	LANE	|	11	|
|	LINCOLN	|	11	|
|	TILLAMOOK	|	11	|
|	YAMHILL	|	11	|
|	COLUMBIA	|	10	|
|	CURRY	|	10	|
|	MORROW	|	10	|
|	HOOD RIVER	|	9	|
|	JACKSON	|	9	|
|	JOSEPHINE	|	9	|
|	WASHINGTON	|	9	|
|	CLACKAMAS	|	8	|
|	COOS	|	8	|
|	DOUGLAS	|	8	|
|	KLAMATH	|	8	|
|	MALHEUR	|	8	|
|	SHERMAN	|	8	|
|	WASCO	|	8	|
|	BENTON	|	7	|
|	MULTNOMAH	|	7	|
|	UMATILLA	|	7	|
|	GILLIAM	|	6	|
|	UNION	|	6	|
|	BAKER	|	5	|
|	WALLOWA	|	5	|
|	GRANT	|	4	|
|	HARNEY	|	3	|
|	WHEELER	|	3	|
|	LAKE	|	2	|

SQL saved as or_growth_table view in database:

```sql
SELECT
y.County,
CAST(ROUND(((y.reg_2019 - x.reg_2015) / CAST(x.reg_2015 AS REAL)) * 100) AS INTEGER) AS Growth
FROM

(
SELECT
	County,
	Passenger_Registrations AS reg_2015
FROM or_registrations
WHERE year = 2015) AS x

INNER JOIN

(SELECT
	County,
	Passenger_Registrations AS reg_2019
FROM or_registrations
WHERE year = 2019) AS y

ON x.County = y.County
ORDER BY growth DESC
```



Data Source: [Oregon DMV Registrations](https://www.oregon.gov/odot/dmv/pages/news/vehicle_stats.aspx)


---
[Capstone Project Home](./) | [Key Insights](insights.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-03**
