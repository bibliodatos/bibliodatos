---
title: Mike Maynard | Google Data Analysis Capstone Project
---
## [Acme Auto Case Study](/capstone/)

#### Oregon County Online Car Postings

| County | Posts |
| --- | ---- |


SQL saved as or_precip_table view in database:

```sql
SELECT county, COUNT(*) AS Posts
FROM or_vehicles
GROUP BY county
ORDER BY Posts DESC
```








---
[Capstone Project Home](./) | [Key Insights](insights.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-03**
