---
title: Mike Maynard | Google Data Analysis Capstone Project
---
## [Acme Auto Case Study](/capstone/)

#### Oregon County Seat Used Car Dealers (Acme Auto markets only)


| County | Dealers |
| ------ | ------ |
|	MULTNOMAH	|	146	|
|	MARION	|	105	|
|	LANE	|	79	|
|	CLACKAMAS	|	64	|
|	JACKSON	|	64	|
|	WASHINGTON	|	55	|
|	DESCHUTES	|	38	|
|	JOSEPHINE	|	29	|
|	LINN	|	25	|
|	DOUGLAS	|	21	|
|	YAMHILL	|	21	|
|	KLAMATH	|	18	|
|	BENTON	|	14	|
|	UMATILLA	|	14	|
|	COOS	|	12	|
|	POLK	|	6	|


SQL query:

```sql
SELECT
  County,
  dealers AS Dealers
FROM or_competition
ORDER BY Dealers DESC
```


Note: For the 'Buy Score' calculations we used `dealers / car registrations`

Data source: [Google Maps](https://maps.google.com/)


---
[Acme Project Home / Table of Contents](./) | [Key Insights](insights.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-03**
