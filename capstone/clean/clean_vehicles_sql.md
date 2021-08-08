---
title: Clean vehicles sql table
---
## [Acme Auto Case Study](/capstone/)

### SQL Data Cleaning and Exploration

#### Import CSV into SQL database
Data Source: [Used Cars Dataset - Kaggle](https://www.kaggle.com/austinreese/craigslist-carstrucks-data)

```sql
  CREATE TABLE "vehicles" (
	"id"	INTEGER,
	"url"	TEXT,
	"region"	TEXT,
	"region_url"	TEXT,
	"price"	INTEGER,
	"year"	TEXT,
	"manufacturer"	TEXT,
	"model"	TEXT,
	"condition"	TEXT,
	"cylinders"	TEXT,
	"fuel"	TEXT,
	"odometer"	INTEGER,
	"title_status"	TEXT,
	"transmission"	TEXT,
	"VIN"	TEXT,
	"drive"	TEXT,
	"size"	TEXT,
	"type"	TEXT,
	"paint_color"	TEXT,
	"image_url"	TEXT,
	"description"	TEXT,
	"county"	TEXT,
	"state"	TEXT,
	"lat"	REAL,
	"long"	REAL,
	"posting_date"	TEXT,
    "clean_model" TEXT,
    "clean_manufacturer" TEXT,
    "clean_vin" TEXT);
```

#### Save copy of table before any data cleaning

```sql
    CREATE TABLE vehicles_orig AS
    SELECT *
    FROM vehicles
```


#### Original number of rows in _vehicles_ table

```sql
    SELECT COUNT(*) AS Row_Count
    FROM vehicles
```

    Row_Count
    ---------
    426880

#### Original number of rows in _or_vehicles_ table

```sql
    SELECT COUNT(*) AS OR_Count
    FROM vehicles
    WHERE state = 'or'
```


    OR_Count
    --------
    17104

#### Most often we are going to be querying for Oregon data so create an Oregon only table

```sql
    CREATE TABLE or_vehicles AS
    SELECT *
    FROM vehicles
    WHERE state = 'or'
```

#### Is _county_ field is populated?

```sql
    SELECT COUNT(*) as County_Not_Null
    FROM or_vehicles
    WHERE county is not NULL
```

Answer:  all NULL

    County_Not_Null
    ---------------
    0

#### No county so do we have latitude and longitude?

```sql
    SELECT COUNT(*) as Lat_Long_Not_Null
    FROM
      or_vehicles
    WHERE
      lat is not NULL
      AND long IS NOT NULL
```

Answer:  Yes we have latitude and longitude

    Lat_Long_Not_Null
    17044

#### Sanity check latitude and clean up any non-Oregon data

Northernmost latitude in Oregon = 46.291719, southernmost latitude in Oregon = 42

```sql
    -- Too far North
    DELETE
    FROM  or_vehicles
    WHERE lat > 46.291719
```

    -- Result: 512 rows returned in 2875ms

```sql
    -- Too far South
    DELETE
    FROM   or_vehicles
    WHERE lat < 42.0
```

    -- Result: query executed successfully. Took 83ms, 486 rows affected

#### Clean up some NULL lat longs based on region value

```sql
    UPDATE   or_vehicles
    SET lat = 44.0581728,
	  long = -121.3153096,
	  county = 'DESCHUTES'
    WHERE lat IS NULL
      AND region = 'bend';

    UPDATE   or_vehicles
    SET lat = 45.5051064,
	  long = -122.6750261,
	  county = 'MULTNOMAH'
    WHERE lat  IS NULL
      AND region = 'portland';

    UPDATE   or_vehicles
    SET lat = 44.0520691,
	  long = -123.0867536,
	  county = 'LANE'
    WHERE lat  IS NULL
      AND region = 'eugene';

    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    16618

#### Delete the few rows left that are without lat or long

```sql
    DELETE
    FROM or_vehicles
    WHERE lat IS NULL
      OR long IS NULL

    -- Result: query executed successfully. Took 40ms, 6 rows affected

    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    16612

#### Westernmost point in Oregon is -124.565233, Easternmost point is -116.463761

```sql
    SELECT COUNT(*)
    FROM or_vehicles
	  WHERE long < -124.565233;
```

    COUNT(*)
    --------
    0

```sql
    DELETE
    FROM or_vehicles
	  WHERE long > -116.463761;

    -- Result: query executed successfully. Took 45ms, 122 rows affected

    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles;
```

    Row_Count
    ---------
    16490

#### Explore _title_status_ field and clean up

```sql
    SELECT DISTINCT(title_status) AS Status, COUNT(*) AS Cnt
    FROM or_vehicles
    GROUP BY title_status
    ORDER BY title_status
```

    title_status Cnt
    ------------ ---
    NULL  	     183
    clean	   15913
    lien	      29
    missing	      30
    parts only     3
    rebuilt	     216
    salvage	     116

#### We only want clean titles.  If value is NULL will include in analysis for now.

```sql
    DELETE
    FROM or_vehicles
    WHERE title_status IS NOT NULL
    AND title_status IS NOT 'clean'

    -- Result: query executed successfully. Took 36ms, 394 rows affected

    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    16096

Do the same for the larger **vehicles** table


```sql
    DELETE
    FROM vehicles
    WHERE title_status IS NOT NULL
    AND title_status IS NOT 'clean'

    -- Result: query executed successfully. Took 980ms, 13521 rows affected
```

## Explore _type_ and clean up

```sql
    SELECT DISTINCT(type), COUNT(*) AS Cnt
    FROM
	  or_vehicles
	  WHERE
	  type IS NOT NULL
    GROUP BY type
	  ORDER BY type
```

    type        Cnt
    ----------- ----
    SUV	    3593
    bus	      11
    convertible  207
    coupe	     450
    hatchback    457
    mini-van     142
    offroad	      19
    other	     173
    pickup	    1605
    sedan	    2930
    truck	    3156
    van          199

Not interested in _bus_, _offroad_, or _other_ vehicle types.

```sql
    DELETE
    FROM
	  or_vehicles
	  WHERE
	  type = 'other' OR type='bus' OR type='offroad';

    -- Result: query executed successfully. Took 54ms, 203 rows affected

    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    15893

Do the same for **vehicles** table

```sql
    DELETE
    FROM
	  vehicles
	  WHERE
	  type = 'other' OR type='bus' OR type='offroad';

    -- Result: query executed successfully. Took 1712ms, 23058 rows affected
```

## Explore _odometer_ field and clean up.

```sql
    DELETE
    FROM
      or_vehicles
    WHERE
      odometer IS NULL OR odometer = 0

    -- Result: query executed successfully. Took 53ms, 527 rows affected
```

Mileage above 300,000 will be considered outliers

```sql
    DELETE
    FROM  or_vehicles
    WHERE odometer > 3000000

    -- Result: query executed successfully. Took 16ms, 3 rows affected

    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    15363

Do the same for **vehicles** table

```sql
    DELETE
    FROM  vehicles
    WHERE odometer > 3000000;

    -- Result: query executed successfully. Took 3538ms, 174 rows affected
```

## Clean up _year_ field

Not interested in cars older than 1995

```sql
    DELETE
    FROM  or_vehicles
    WHERE year < 1995

    -- Result: query executed successfully. Took 48ms, 504 rows affected

    DELETE
    FROM  vehicles
    WHERE year < 1995

    -- Result: query executed successfully. Took 1249ms, 14335 rows affected
```

Look for NULLS in year field

```sql
    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
    WHERE year IS NULL
```

    Row_Count
    ---------
    0

```sql
    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    14859

```sql
    DELETE
    FROM vehicles
    WHERE year IS NULL

    -- Result: query executed successfully. Took 393ms, 1095 rows affected
```

## Explore the condition field and clean it up

```sql
    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
    WHERE condition IS NULL
```

    Row_Count
    ---------
    10387

We have an issue. Over 2/3 of our listings don't have a condition value. Let's see if we can use mileage as a proxy for condition.

```sql
    SELECT DISTINCT(condition), COUNT(*) AS Row_Count, ROUND(AVG(odometer)) AS Mileage
    FROM or_vehicles
    WHERE condition !=  'new' AND condition != 'salvage'
	  GROUP BY condition
	  ORDER BY Mileage ASC
```

    condition   Row_Count      Mileage
    ---------   ---------      -------
    like new     337 	   63279.0
    excellent   2769	  112857.0
    good	    1229	  148738.0
    fair	     116	  196823.0

Set condition based on 40,000 mile buckets

```sql
    UPDATE   or_vehicles
    SET condition = 'new'
    WHERE condition IS NULL
	  AND odometer < 40000

    -- Result: query executed successfully. Took 238ms, 2243 rows affected

    UPDATE   or_vehicles
    SET condition = 'like new'
    WHERE condition IS NULL
	  AND odometer < 80000

    -- Result: query executed successfully. Took 270ms, 2653 rows affected

    UPDATE   or_vehicles
    SET condition = 'excellent'
    WHERE condition IS NULL
	  AND odometer < 120000

    -- Result: query executed successfully. Took 241ms, 2577 rows affected

    UPDATE   or_vehicles
    SET condition = 'good'
    WHERE condition IS NULL
	  AND odometer < 160000

    -- Result: query executed successfully. Took 113ms, 1740 rows affected

    UPDATE   or_vehicles
    SET condition = 'fair'
    WHERE condition IS NULL

    -- Result: query executed successfully. Took 163ms, 1174 rows affected

```

## Explore and clean the manufacturer field using clean_manufacturer field

```sql
    UPDATE or_vehicles
    SET clean_manufacturer = manufacturer

    UPDATE vehicles
    SET clean_manufacturer = manufacturer

    DELETE
    FROM or_vehicles
    WHERE clean_manufacturer = 'harley-davidson'


    SELECT DISTINCT(clean_manufacturer), COUNT(*) AS Cnt
    FROM or_vehicles
    GROUP BY clean_manufacturer
    ORDER BY clean_manufacturer  

    UPDATE or_vehicles
    SET clean_manufacturer = 'scion'
    WHERE model LIKE '%Scion%' OR model LIKE '%scion%'
    AND clean_manufacturer IS NULL

    -- Result: query executed successfully. Took 22ms, 57 rows affected

    UPDATE or_vehicles
    SET clean_manufacturer = 'genesis'
    WHERE model LIKE '%genesis%' OR model LIKE '%Genesis%'
    AND clean_manufacturer IS NULL

    -- Result: query executed successfully. Took 21ms, 24 rows affected

    UPDATE or_vehicles
    SET clean_manufacturer = 'suzuki'
    WHERE model LIKE '%suzuki%' OR model LIKE '%Suzuki%' OR model LIKE '%SUZUKI%'
    AND clean_manufacturer IS NULL

    -- Result: query executed successfully. Took 21ms, 15 rows affected

    UPDATE or_vehicles
    SET clean_manufacturer = 'hummer'
    WHERE model LIKE '%hummer%' OR model LIKE '%Hummer%' OR model LIKE '%HUMMER%'
    AND clean_manufacturer IS NULL

    -- Result: query executed successfully. Took 20ms, 15 rows affected

    UPDATE or_vehicles
    SET clean_manufacturer = 'bentley'
    WHERE model LIKE '%bentley%' OR model LIKE '%Bentley%' OR model LIKE '%BENTLEY%'
    AND clean_manufacturer IS NULL

    -- Result: query executed successfully. Took 23ms, 10 rows affected

    UPDATE or_vehicles
    SET clean_manufacturer = 'saab'
    WHERE model LIKE '%saab%' OR model LIKE '%Saab%' OR model LIKE '%SAAB%'
    AND clean_manufacturer IS NULL

    -- The rest aren't worth looking at.  Outliers
    DELETE
    FROM or_vehicles
    WHERE clean_manufacturer IS NULL

    -- Result: query executed successfully. Took 45ms, 62 rows affected

    UPDATE or_vehicles
    SET clean_manufacturer = 'ram'
    WHERE clean_model = '1500' AND clean_manufacturer = 'dodge'

    UPDATE or_vehicles
    SET clean_manufacturer = 'ram'
    WHERE clean_model = '2500' AND clean_manufacturer = 'dodge'
```

## Clean up some NULL values in _model_ field

```sql
    UPDATE   or_vehicles
    SET  model = '2500 laramie'
    WHERE model is NULL
        AND description LIKE '%2500 Laramie%'

    UPDATE   or_vehicles
    SET  model = '2500 laramie'
    WHERE model is NULL
        AND description LIKE '%2500 SLT Laramie%'

    UPDATE   or_vehicles
    SET  model = '3500 laramie'
    WHERE model is NULL
        AND description LIKE '%3500 Laramie%'

    UPDATE   or_vehicles
    SET  model = '3500'
    WHERE model is NULL
        AND description LIKE '%Ram 3500%'

    UPDATE   or_vehicles
    SET  model = '2500'
    WHERE model is NULL
            AND description LIKE '%Dodge Ram 2500%'

    UPDATE   or_vehicles
    SET  model = '1500'
    WHERE model is NULL
            AND description LIKE '%Dodge Ram 1500%'

    UPDATE   or_vehicles
    SET  model = '1500'
    WHERE model is NULL
        AND description LIKE '%1500%'
            AND manufacturer = 'ram'

    UPDATE   or_vehicles
    SET  clean_model = model

    --everything lower case
    UPDATE or_vehicles
    SET clean_model = LOWER(clean_model)

    UPDATE or_vehicles
    SET clean_model = 'suburban 1500'
    WHERE clean_model LIKE '%suburban 1500%' OR clean_model LIKE '%Suburban 1500%'

    UPDATE or_vehicles
    SET clean_model = 'silverado 1500'
    WHERE clean_model LIKE '%silverado 1500%' OR clean_model LIKE '%Silverado 1500%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'supercrew cab',  'supercrew')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'crew cab', 'crewcab')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'off road', 'offroad')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, '4wd', '4x4')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'quad cab' , 'quadcab')
    WHERE clean_model LIKE '%quad cab%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'mega cab', 'megacab')
	  WHERE clean_model LIKE '%mega cab%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'cummins diesel ', 'cummins')
	  WHERE clean_model LIKE '%cummins diesel%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, '-', ' ')
	  WHERE clean_model LIKE '%-%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, '*', ' ')
	  WHERE clean_model LIKE '%*%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'v6', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'v8', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'truck', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'loaded', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'lifted', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'local', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'suv', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'clean', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'carfax', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'owner', '')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, '4 door', '4dr')
	  WHERE clean_model LIKE '%4 door%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, '2 door', '2dr')
	  WHERE clean_model LIKE '%2 door%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, '5 door', '5dr')
	  WHERE clean_model LIKE '%5 door%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'vehicle', '')
	  WHERE clean_model LIKE '%vehicle%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model, 'pickup', '')
    WHERE clean_model LIKE '%pickup%'

    UPDATE or_vehicles
    SET clean_model = model
    WHERE clean_model LIKE '%cross country%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'automatic' ,  '' )

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'low miles' ,  '' )

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  ' auto ' ,  ' ' )

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'f 150' ,  'f150' )

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'f 250' ,  'f250' )

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'f 350' ,  'f350' )

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'super duty', 'superduty')
    WHERE clean_model LIKE '%super duty%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  ' manual ', ' ')
    WHERE clean_model LIKE '%manual%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  ' manual', '')
    WHERE clean_model LIKE '%manual'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'super cab', 'supercab')
    WHERE clean_model LIKE '%super cab%'

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'double cab', 'doublecab')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  ' 4d ' , ' 4dr ')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'crew max' , 'crewmax')

    UPDATE vehicles
    SET clean_model = REPLACE(clean_model,  'king cab' , 'kingcab')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'off road' , 'offroad')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  'ext cab' , 'extcab')

    UPDATE or_vehicles
    SET clean_model = REPLACE(clean_model,  '  ' , ' ')
    WHERE clean_model LIKE '%  %'

    UPDATE or_vehicles
    SET clean_model = TRIM(clean_model)



    SELECT substr(clean_model, 1, pos-1) AS first_name,
       substr(clean_model, pos+1) AS last_name
    FROM
    (SELECT *,
          instr(clean_model,' ') AS pos
    FROM or_vehicles)
    ORDER BY first_name,
         last_name;

```

#### Just delete the stragglers with no _model_ value

```sql
    DELETE
    FROM or_vehicles
    WHERE model IS NULL

    -- Result: query executed successfully. Took 21ms, 28 rows affected

    -- Copy model into clean_model field. We will update clean_model values
    UPDATE or_vehicles
    SET clean_model = model

```

#### Explore and clean _vin_ field

```sql
    -- we have a lot of NULL vins but we need a unique ID for each car
    -- so we can get the latest posting for each individual car later.
    -- Populate clean_vin with id if vin is NULL
    UPDATE or_vehicles
    SET clean_vin = id
    WHERE vin IS NULL

    -- Result: query executed successfully. Took 111ms, 2562 rows affected

    -- Now put the existing real VINs into clean_vin
    UPDATE or_vehicles
    SET clean_vin = vin
    WHERE vin IS NOT NULL

    -- Result: query executed successfully. Took 951ms, 12199 rows affected

    SELECT COUNT(*) AS Cnt
    FROM or_vehicles
    WHERE clean_vin IS NULL
```

    Cnt
    ---
    0

```sql
    SELECT COUNT(DISTINCT(clean_vin)) AS Cnt
    FROM or_vehicles
```

    Cnt
    ----
    9367

```sql
    -- See which cars in Oregon have been posted the most times
    SELECT clean_vin, COUNT(*) AS Cnt
    FROM or_vehicles
    GROUP BY clean_vin
    ORDER BY Cnt DESC
    LIMIT 10
```

    clean_vin              Cnt
    -----------------      ---
    3C6UR4CL1HG615370	25
    1GC4K1E85FF601426	24
    1FD8W3FT2FEA90621	24
    3D7MX48C86G224937	23
    JTEBU5JR6D5128822	20
    1GT42VCY5KF147716	20
    1GC1KWE85GF195827	19
    1FTFW1ETXEKE03772	19
    3C6UR5DL3JG242522	18
    1GCHK23133F150618	18

```sql
    -- Lets look at the most posted car
    SELECT manufacturer, clean_model, price, posting_date
    FROM or_vehicles
    WHERE clean_vin = '3C6UR4CL1HG615370'
    ORDER BY posting_date DESC
    LIMIT 10
```

    ram	2500 6 speed diesel	0	2021-05-03T16:52:52-0700
    ram	2500 6 speed diesel	0	2021-05-03T16:50:46-0700
    ram	2500 6 speed diesel	0	2021-05-03T16:50:36-0700
    ram	2500 6 speed diesel	0	2021-05-03T16:34:30-0700
    ram	2500 6 speed diesel	0	2021-05-03T16:34:21-0700
    ram	2500 6 speed diesel	0	2021-05-01T14:16:13-0700
    ram	2500 6 speed diesel	0	2021-05-01T14:14:08-0700
    ram	2500 6 speed diesel	0	2021-05-01T14:13:59-0700
    ram	2500 6 speed diesel	0	2021-05-01T12:50:12-0700
    ram	2500 6 speed diesel	0	2021-04-25T13:05:34-0700

#### Price clean up

```sql
    DELETE
    FROM or_vehicles
    WHERE price = 0 OR price IS NULL

    -- Result: query executed successfully. Took 150ms, 2519 rows affected

    DELETE
    FROM or_vehicles
    WHERE price > 165000

    -- Result: query executed successfully. Took 13ms, 1 rows affected

    DELETE
    FROM vehicles
    WHERE price > 165000

    -- Result: query executed successfully. Took 281ms, 87 rows affected

    DELETE
    FROM or_vehicles
    WHERE price < 1000

    -- Result: query executed successfully. Took 94ms, 1697 rows affected

    DELETE
    FROM vehicles
    WHERE price < 1000

    -- Result: query executed successfully. Took 962ms, 11119 rows affected
```

```sql
    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    10544

```sql
    SELECT COUNT(*) AS Row_Count
    FROM vehicles
```

    Row_Count
    ---------
    323388

## clean_county.py has now populated _county_ field based on pull from US census API for lat, long

```sql
    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
    WHERE county IS NULL
```

    Row_Count
    ---------
    0

## Some counties have cross postings in other regions that don't make sense for the county's location.
#### Example:  HOOD RIVER county

```sql
    SELECT County, Region, COUNT(*) AS Cnt
    FROM or_vehicles
    WHERE county = 'HOOD RIVER'
    GROUP BY county, region
    ORDER BY County ASC, Cnt DESC
```

    county          region          Cnt
    ------          ------          ---
    HOOD RIVER	portland	1
    HOOD RIVER	medford-ashland	1
    HOOD RIVER	east oregon	1

## Delete cross postings in non-contigous regions for that county

```sql
    DELETE FROM or_vehicles WHERE  county = 'CANYON' -- Idaho
    DELETE FROM or_vehicles WHERE  county = 'FRANKLIN'  -- Washington
    DELETE FROM or_vehicles WHERE  county = 'SNOHOMISH' -- Washington
    DELETE FROM or_vehicles WHERE  county = 'BENTON' AND 	region = 'portland'
    DELETE FROM or_vehicles WHERE  county = 'CLACKAMAS' AND 	region = 'eugene'
    DELETE FROM or_vehicles WHERE  county = 'CLACKAMAS' AND 	region = 'oregon coast'
    DELETE FROM or_vehicles WHERE  county = 'CLACKAMAS' AND 	region = 'corvallis/albany'
    DELETE FROM or_vehicles WHERE  county = 'CLACKAMAS' AND 	region = 'medford-ashland'
    DELETE FROM or_vehicles WHERE  county = 'CLATSOP' AND 	region = 'portland'
    DELETE FROM or_vehicles WHERE  county = 'CURRY' AND 	region = 'portland'
    DELETE FROM or_vehicles WHERE  county = 'DESCHUTES' AND 	region = 'medford-ashland'
    DELETE FROM or_vehicles WHERE  county = 'DESCHUTES' AND 	region = 'portland'
    DELETE FROM or_vehicles WHERE  county = 'DESCHUTES' AND 	region = 'eugene'
    DELETE FROM or_vehicles WHERE  county = 'DESCHUTES' AND 	region = 'corvallis/albany'
    DELETE FROM or_vehicles WHERE  county = 'HOOD RIVER'  AND 	region = 'medford-ashland'
    DELETE FROM or_vehicles WHERE  county = 'JACKSON'  AND 	region = 'eugene'
    DELETE FROM or_vehicles WHERE  county = 'JACKSON'  AND 	region = 'oregon coast'
    DELETE FROM or_vehicles WHERE  county = 'JACKSON'  AND 	region = 'bend'
    DELETE FROM or_vehicles WHERE  county = 'JOSEPHINE'  AND 	region = 'klamath falls'
    DELETE FROM or_vehicles WHERE  county = 'JOSEPHINE'  AND 	region = 'eugene'
    DELETE FROM or_vehicles WHERE  county = 'LANE'  AND 	region = 'medford-ashland'
    DELETE FROM or_vehicles WHERE  county = 'LANE'  AND 	region = 'portland'
    DELETE FROM or_vehicles WHERE  county = 'LINN'  AND 	region = 'medford-ashland'
    DELETE FROM or_vehicles WHERE  county = 'MARION'  AND 	region = 'eugene'
    DELETE FROM or_vehicles WHERE  county = 'MARION'  AND 	region = 'roseburg'
    DELETE FROM or_vehicles WHERE  county = 'MARION'  AND 	region = 'medford-ashland'
    DELETE FROM or_vehicles WHERE  county = 'MARION'  AND 	region = 'corvallis/albany'
    DELETE FROM or_vehicles WHERE  county = 'MULTNOMAH'  AND 	region != 'portland'
    DELETE FROM or_vehicles WHERE  county = 'POLK'  AND 	region = 'portland'
    DELETE FROM or_vehicles WHERE  county = 'UMATILLA'   AND 	region = 'portland'
    DELETE FROM or_vehicles WHERE  county = 'WASHINGTON'   AND 	region != 'portland'
```

```sql
    SELECT COUNT(*) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    7371

## How many unique vehicles to we have now after cleaning up region cross postings?

```sql
    SELECT COUNT(DISTINCT(clean_vin)) AS Row_Count
    FROM or_vehicles
```

    Row_Count
    ---------
    5696

---
[Acme Project Home](./) | [Appendix](../appendix.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-08**
