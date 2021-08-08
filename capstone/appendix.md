---
title: Mike Maynard | Google Data Analysis Capstone Project - Appendix
---
## [Acme Auto Case Study](/capstone/)

### Appendix

#### Data Cleaning and Exploration

  * [Cleaning with SQL](clean/clean_vehicles_sql.html)
  * [More exploring in SQL](clean/explore.html)
  * Postings grouped by region in [Google Sheets](https://docs.google.com/spreadsheets/d/1LdlBaJk7wCdMmCah5XsSkEnTyDtc2ey_LguZ7qA5rvY/edit?usp=sharing)
  * Price quartiles & averages grouped by condition in [Google Sheets](https://docs.google.com/spreadsheets/d/1-iIShpd4WEcCGclM1-a4zczGqpQrGrHl2nYIzmkFQco/edit?usp=sharing)

#### Data Wrangling

  * Scripts
    * Populate **county** field in *or_vehicles* table with [python script](https://github.com/bibliodatos/bibliodatos.github.io/blob/main/capstone/python/clean_county.py)
    * Populate **distance_to_bend** field in *or_county_seats* table with [python script](https://github.com/bibliodatos/bibliodatos.github.io/blob/main/capstone/python/distance_to_bend.py)
    * Populate **distance_to_avg** field in *or_county_seats* table with [python script](https://github.com/bibliodatos/bibliodatos.github.io/blob/main/capstone/python/distance_to_avg.py)
  * Spreadsheets
    * Transform US Census county data from wide to long format [Google Sheets](https://docs.google.com/spreadsheets/d/1Lyp5Idy-g-xDi2-4vftaellIXRUWlzo_AgyPYbaLM7s/edit?usp=sharing)
    * Consolidate 5 years of Oregon car registration data [Google Sheets](https://docs.google.com/spreadsheets/d/1vvosiQDx0oBLaoxEYhDFrSDCbgjwpqUpzu3Y9fggNa0/edit?usp=sharing)
    * Oregon highway miles traveled data from wide to long format [Google Sheets](https://docs.google.com/spreadsheets/d/1pFLCwuB4Z9NW3xQgaUSOYZ0aU9WuPrMchXL30pibA9A/edit?usp=sharing)
  * [Database Views](clean/views.html)

#### Composite Metrics

  * [Sell Score](sell_score.html)
  * [Buy Score](buy_score.html)






---
[Acme Project Home / Table of Contents](./)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-05**
