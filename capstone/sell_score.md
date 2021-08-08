---
title: Data exploration
---
## [Acme Auto Case Study](/capstone/)

#### Sell Score

Composite metric for evaluating the best county market for Acme to sell used cars. Each component is a score from 0 to 100 with 100 being the highest rated county and 0 being the lowest rated county.  All components of the sell score are equally weighted when calculating the overall score.

Components:

  * **Competition Score**: passenger car registrations / number of used car dealers. Higher the better.

  * **Posting Score**: online car postings count / (passenger registrations / 10000). Higher the better

  * **Distance Score**: distance in km of county seat to the average location of online car postings in Oregon. Smaller the better.

  * **Climate Score**: annual average precipitation for the county.  Smaller the better

  * **Growth Score**: percentage growth of passenger car registrations between 2015 and 2019. Higher the better.

See [Data Sources](data.html) for underlying datasets.  

<HR>

Acme Project Home / Table of Contents](/capstone/) | [Appendix](../appendix.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQL, Tableau, Python, Google Sheets, Markdown**<BR>
Last updated:  **2021-08-08**
