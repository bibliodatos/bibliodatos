---
title: SQLite Cookbook Chapter 2
---
## SQLite Cookbook Chapter 2

### Sorting Query Results

| SQLite Query &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;      | MySQL<br>differences? | Run query on sqlime.org |
| ------------ | ------------ |
| **2.1** [Results in a specified order](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.1.sql)<br><font size="-1">  2.1.a  - Ascending<br>  2.1.b - Descending<br>  2.1.c - Descending by value in third column</font> | No | &nbsp; <br> [run 2.1.a](https://sqlime.org/#gist:d4c9c5d7fde993304b59fdb51059701f)<br>[run 2.1.b](https://sqlime.org/#gist:6c6cc239ea780bd808948c2f6e8a02ed)<br>[run 2.1.c](https://sqlime.org/#gist:e5943e9e3bb4d1304d850e3693b48272) |
| **2.2** [Results sorted by multiple fields](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.2.sql) | No | [run 2.2](https://sqlime.org/#gist:d0d5f1ff743bf98c628efc437c906102) |
| **2.3** [Sorting query by substrings](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.3.sql) | [Yes](len.html) | [run 2.3](https://sqlime.org/#gist:bdcd7b9f6ba74a4704ae9a2ef8f0aaeb) |
| **2.4** [Sorting mixed alphanumeric data](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.4.sql)| [No](translate.html) | |
| **2.5** [Dealing with NULLs when sorting](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.5.sql)<br><font size="-1"> 2.4.a NULLS sort first by default<br>2.5.b Make NULLS sort last using DESC<br>2.5.c NON-NULL commission sorted ascending and all NULLS last<br>2.5.d NON-NULL commission sorted descending and all NULLS last<br>2.5.e NON-NULL commission sorted ascending and all NULLS first<br>2.4.f NON-NULL commission sorted descending and all NULLS first</font> | No |&nbsp; <br> [run 2.5.a](https://sqlime.org/#gist:537dc372b70fcf51f7192026d99c32c1)<br>[run 2.5.b](https://sqlime.org/#gist:bf423fccfb569857aa1f41a016afeb42)<br>[run 2.5.c](https://sqlime.org/#gist:c68100f42a0a1bfc287110532709c13c)<br>[run 2.5.d](https://sqlime.org/#gist:2f501f93831e5c0167053f729ef5af04)<br>[run 2.5.e](https://sqlime.org/#gist:a2b938e47d56508a23292e56f98b259c)<br>[run 2.5.f](https://sqlime.org/#gist:60aab3298ea13305c87b4fa99b53b3f7) |

[← Chapter 1](chapter_1.html)  [SQLite Cookbook Home](./index.html)  [Chapter 3 →](chapter_3.html)


Created by **Mike Maynard**<br>
Project Implemented in **SQLite, DB Browser for SQLite, SQLime.org and Markdown**<br>
Last updated: **2021-12-31**
