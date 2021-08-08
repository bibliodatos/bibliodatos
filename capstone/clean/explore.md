---
title: Mike Maynard | Google Data Analytics Capstone - Data exploration
---
## [Acme Auto Case Study](/capstone/)

### Some additional data exploration


#### Mean vehicle price by condition in Oregon

Excluding 'new' condition

  | Mean | Condition |
  | --- | ------ |
  |	25792.0	|	like new	|
  |	16795.0	|	excellent	|
  |	11511.0	|	good	|
  |	10774.0	|	fair	|
  |	2700.0	|	salvage	|

SQL Query

```sql
    SELECT  
     ROUND(AVG(price)) AS Mean,
     condition AS Condition
    FROM or_vehicles
    WHERE condition !=  'new'
    GROUP BY condition
    ORDER BY mean DESC
```

___


#### Online postings by manufacturer

  | Manufacturer | Num |
  | --- | ------ |
  |	ford	|	1507	|
  |	toyota	|	819	|
  |	chevrolet	|	708	|
  |	honda	|	430	|
  |	ram	|	336	|
  |	subaru	|	332	|
  |	nissan	|	307	|
  |	jeep	|	283	|
  |	hyundai	|	262	|
  |	gmc	|	231	|
  |	dodge	|	228	|
  |	bmw	|	220	|

SQL Query saved as or_manufacturer_postings in database

```sql
     SELECT Manufacturer, Num
     FROM
     (SELECT  
        manufacturer, COUNT(*) AS num
        FROM or_vehicles
        WHERE manufacturer IS NOT NULL
        GROUP BY manufacturer
        ORDER BY num DESC
    ) AS x

    ORDER BY num DESC
    LIMIT 12
```


#### Number of vehicle postings matching our target conditions

  | Count |
  | ----- |
  | 1133  |

SQL Query

```sql
    SELECT COUNT(*) AS Count
    FROM  or_targeted_manufacturer
    WHERE
        (condition = 'excellent' AND odometer < 110000 AND year > 2010)
        OR
        (condition = 'like new' AND odometer < 60000 AND year > 2014)
```

[Acme Project Home](../) | [Appendix](../appendix.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-08**
