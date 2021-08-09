---
title: Mike Maynard | Google Data Analysis Capstone - database views
---
## [Acme Auto Case Study](../)

### Database views

#### Used for data exploration, creating more complex queries, and csv's for import into Tableau


```sql
CREATE VIEW "or_bend_distance_score" AS SELECT
	'|', county,
	'|', distance_to_bend AS km,
   	'|', CAST(ROUND(((353 - ROUND(distance_to_bend) ) / 353) * 100) AS INTEGER) AS score,
   '|'
FROM or_county_seats
ORDER BY score DESC

CREATE VIEW "or_buy" AS SELECT
	b.county,
	b.score AS distance_score,
	c.climate_score,
	p.score AS posting_score,
	ROUND(((b.score  * 5 ) + (c.climate_score * 2)  + (p.score * 3)) / 10.0)  AS weighted_score
FROM or_bend_distance_score AS b
JOIN or_climate_score AS c
	ON b.county = c.county
JOIN or_condition_score as p
	ON b.county = p.county
ORDER BY weighted_score DESC

CREATE VIEW "or_buy_view" AS SELECT
	'|', b.county AS County,
	'|', CAST(ROUND(((b.weighted_score - 8) / 85.0) * 100) AS INTEGER) AS buy_score,
    '|'
    FROM
       or_buy as b

CREATE VIEW "or_climate_score" AS SELECT
 	County AS county,
 	CAST(ROUND(((89 - precip) / 77.0) * 100) AS INTEGER) AS climate_score
  FROM or_climate
  ORDER BY precip ASC

CREATE VIEW "or_competition_score" AS SELECT
  	c.county,
  	c.dealers,
  	r.Passenger_Registrations,
  	CAST(ROUND((((r.Passenger_Registrations / c.dealers ) - 2895) / 9648.0) * 100) AS INTEGER) AS score
  FROM or_competition AS c
  JOIN or_registrations AS r
  	ON c.county = r.county
  	WHERE r.year = 2019
  ORDER BY score DESC

CREATE VIEW "or_condition_mean" AS SELECT  
	'|', ROUND(AVG(price)) AS mean,
	'|', condition,
	'|'
FROM or_vehicles
WHERE condition !=  'new'
GROUP BY condition
ORDER BY mean DESC

CREATE VIEW "or_condition_score" AS SELECT
        p.county,
        p.cnt,
        CAST(ROUND((p.cnt / 656.0)  * 100) AS INTEGER) AS score
    FROM
       or_target_condition_postings AS p

CREATE VIEW "or_distance_score" AS SELECT county,
  CAST((450.0 - ROUND(distance_to_avg)) / 4.0 AS INTEGER)  AS dist_score
	FROM or_county_seats
 	ORDER BY dist_score DESC

CREATE VIEW "or_growth_2015_2019" AS SELECT y.County, x.reg_2015, y.reg_2019,  CAST(ROUND(((y.reg_2019 - x.reg_2015) / CAST(x.reg_2015 AS REAL)) * 100) AS INTEGER) AS growth
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

  CREATE VIEW "or_growth_score" AS SELECT
  County,
  CAST(ROUND(((growth - 2) / 15.0) * 100) AS INTEGER) AS score
  FROM or_growth_2015_2019

  CREATE VIEW "or_growth_table" AS SELECT
  '|',  y.County,
   '|' , CAST(ROUND(((y.reg_2019 - x.reg_2015) / CAST(x.reg_2015 AS REAL)) * 100) AS INTEGER) AS growth,
   '|'
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

  CREATE VIEW "or_highway_miles" AS SELECT
  	m.county AS county,
  	m.Vehicle_Miles AS miles,
  	r.Passenger_Registrations AS vehicles,
  	m.Vehicle_Miles  / r.Passenger_Registrations AS miles_per_vehicle
  FROM or_vmt_highway AS m
  JOIN or_registrations AS r
  	ON m.county = r.county AND m.year = r.year
  WHERE m.Year = 2019
  ORDER BY miles_per_vehicle DESC

  CREATE VIEW "or_highway_miles_score" AS SELECT
	'|' ,  m.county AS county,
	'|' ,  m.miles_per_vehicle,
	'|' ,
	CASE
		WHEN m.miles_per_vehicle > 17500 THEN 100
		ELSE
			CAST(ROUND(((m.miles_per_vehicle - 3580) / 13920.0) * 100) AS INTEGER)
		END
	AS score,
	'|'
FROM or_highway_miles m

CREATE VIEW "or_joy_score" AS SELECT
	x.county AS 'county',
	(x.comp_score + x.posting_score + x.dist_score + x.climate_score + x.growth_score) AS joy_score,
	'Oregon' AS 'state',
	'USA' AS 'country'
FROM

(SELECT
	c.county,
	c.score AS comp_score,
	p.posting_score,
	d.dist_score,
	l.climate_score,
	g.score AS growth_score
FROM or_competition_score AS c
JOIN or_posting_score AS p
	ON (c.county = p.county)
JOIN or_distance_score as d
	ON (c.county = d.county)
JOIN or_climate_score as l
	ON (c.county = l.county)
JOIN or_growth_score as g
	ON (c.county = g.county)
	) x

ORDER BY joy_score DESC

CREATE VIEW "or_manufacturer_postings" AS SELECT Manufacturer, Num
     FROM
     (SELECT  
        manufacturer, COUNT(*) AS num
        FROM or_vehicles
        WHERE manufacturer IS NOT NULL
        GROUP BY manufacturer
        ORDER BY num DESC
    ) AS x

    ORDER BY num DESC

CREATE VIEW "or_odometer_price_condition" AS SELECT  DISTINCT(clean_vin),
        odometer,
        price,
    	condition
        FROM or_vehicles
        WHERE condition !=  'new'
    	AND (condition = 'like new'  OR condition = 'excellent')
    	AND odometer IS NOT NULL

      CREATE VIEW "or_population_growth" AS SELECT y.County, x.reg_2016, y.reg_2020,  CAST(ROUND(((y.reg_2020 - x.reg_2016) / CAST(x.reg_2016 AS REAL)) * 100) AS INTEGER) AS growth
      FROM

      (
      SELECT
      	County,  
      	Population_Estimate AS reg_2016
      FROM or_population
      WHERE year = 2016) AS x

      INNER JOIN

      (SELECT
      	County,
      	Population_Estimate AS reg_2020
      FROM or_population
      WHERE year = 2020) AS y

      ON x.County = y.County
      ORDER BY growth DESC;

CREATE VIEW "or_posting_score" AS SELECT x.County,
      x.posting_cnt,
       x.registration_cnt,
      CAST(  ((x.posting_rate / 55.0 ) * 100) AS INTEGER) AS posting_score,
      'OREGON' AS state,
      'USA' AS country
      FROM

      (SELECT reg.County, reg.Passenger_Registrations AS registration_cnt,
      	p.Cnt AS posting_cnt,
      	(p.Cnt / (reg.Passenger_Registrations / 10000)) AS posting_rate
      FROM or_registrations AS reg
      LEFT OUTER JOIN or_postings_per_county AS p ON (reg.county = p.County)
      WHERE  Year = 2019
      ORDER BY posting_rate DESC, posting_cnt DESC) x;

CREATE VIEW "or_postings_per_county" AS SELECT county, COUNT(*) AS Cnt
      FROM or_vehicles
      GROUP BY county
      ORDER BY Cnt DESC;

CREATE VIEW "or_precip_table" AS SELECT  
      county AS County,
      precip AS Precip
      FROM or_climate
      ORDER BY precip ASC;

CREATE VIEW "or_small_county" AS SELECT County, State, Country, '1'
      FROM or_population
      WHERE year = 2019 and Population_Estimate < 60000

      CREATE VIEW "or_target_condition_postings" AS SELECT county, COUNT(*) AS cnt
      FROM

      (SELECT DISTINCT(clean_vin), county
      FROM or_vehicles
      WHERE condition = 'like new' OR condition = 'excellent'
      ) AS x

      GROUP BY (county)
      ORDER BY cnt DESC;

CREATE VIEW "or_targeted_manufacturer" AS SELECT DISTINCT(clean_vin), *
      FROM
      or_vehicles
      WHERE manufacturer IN ('ford', 'lincoln', 'chevrolet', 'gmc', 'honda', 'acura', 'nissan', 'infiniti', 'toyota', 'lexus', 'chrysler', 'jeep', 'dodge', 'ram');

CREATE VIEW "posting_by_day_of_week" AS SELECT
      	CASE day_num
      		WHEN '0' THEN 'Sunday'
      		WHEN '1' THEN 'Monday'
      		WHEN '2' THEN 'Tuesday'
      		WHEN '3' THEN 'Wednesday'
      		WHEN '4' THEN 'Thursday'
      		WHEN '5' THEN 'Friday'
      		WHEN '6' THEN 'Saturday'
      		ELSE ''
      	END AS Day,
      	COUNT(*) AS Cnt

      FROM

      	(SELECT  strftime('%w', substr(posting_date, 1, 10)) AS day_num
      	FROM vehicles) x

      GROUP BY 1;

```


---
[Acme Project Home](../)  | [Appendix](../appendix.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-08**
