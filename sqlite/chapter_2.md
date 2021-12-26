---
title: SQLite Cookbook Chapter 2
---
## SQLite Cookbook Chapter 2

### Sorting Query Results

| SQLite Query        | MySQL differences? | Run query on sqlime.org |
| ------------ | ------------ |
| 2.1 [Results in a specified order](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.1.sql)<BR>2.1.a  Results in a specified order - Ascending<BR>2.1.b  Results in a specified order - Descending<BR>2.1.c Results in a specified order - Descending by value in third column | No | [run 2.1.a](https://sqlime.org/#gist:d4c9c5d7fde993304b59fdb51059701f)<BR>[run 2.1.b](https://sqlime.org/#gist:6c6cc239ea780bd808948c2f6e8a02ed)<BR>[run 2.1.c](https://sqlime.org/#gist:e5943e9e3bb4d1304d850e3693b48272)<BR>[run 2.1.c](https://sqlime.org/#gist:e5943e9e3bb4d1304d850e3693b48272) |
| 2.2 [Results sorted by multiple fields](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.2.sql) | No | [run 2.2](https://sqlime.org/#gist:d0d5f1ff743bf98c628efc437c906102) |
| 2.3 [Sorting query by substrings](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.3.sql) | [Yes](len.html) | [run 2.3](https://sqlime.org/#gist:bdcd7b9f6ba74a4704ae9a2ef8f0aaeb) |
| 2.4 [Sorting mixed alphanumeric data](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.4.sql)| No 'Translate' function in SQLite or MySQL | |
| 2.5 [Dealing with NULLs when sorting](https://github.com/bibliodatos/SQLite_Cookbook/blob/main/chapter_2/2.5.sql)<BR>2.5.b Make NULLS sort last using DESC<BR>2.5.c NON-NULL commission sorted ascending and all NULLS last<BR>2.5.d NON-NULL commission sorted descending and all NULLS last<BR>2.5.e NON-NULL commission sorted ascending and all NULLS first<BR>2.4.f NON-NULL commission sorted descending and all NULLS first | No | [run 2.5.a](https://sqlime.org/#gist:537dc372b70fcf51f7192026d99c32c1) |

[SQLite Cookbook Home](./index.html)

Created by **Mike Maynard**<BR>
Project Implemented in **SQLite, DB Browser for SQLite, SQLime.org and Markdown**<BR>
Last updated: **2021-12-26**
