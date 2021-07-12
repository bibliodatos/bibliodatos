---
title: Mike Maynard | Marlow Indexing Project
---
## Marlow, New Hampshire book indexing project

### The Goal:
Create indexes for an unindexed book in order to help family history researchers and genealogists.

### The Indexes:

#### - [Surnames Index](Surname.txt)
#### - [Places Index](Places.txt)
#### - [Streets/Roads Index](Streets.txt)

### Why:

Many years ago I was researching my family history, and I determined that my 5th great-grandfather spent some years living in a small town named Marlow in Cheshire County, New Hampshire. At that time he was the farthest back I had been able to trace my direct paternal line.  This man, Benajah Maynard, was a bit of a brick wall in my research.

I learned of a local history of Marlow compiled by Elgin Jones prior to his death in 1934. I quickly ordered a copy of the book and eagerly waited the delivery.  The book, while a treasure trove of information for my research, did not contain an index. I considered the work it would take to carefully read each page looking for potential family names as I went. I decided to scan the pages and use OCR software to create my own personal electronic text version.  I scanned it and after a bit of manual editing to correct for OCR errors I was able to do a text search for my family names.  To my delight I found a note indicating that a certain Jabez Maynard was Benajah's father.  Just the breakthrough I needed for my research.

My copy of the History of Marlow, New Hampshire sat unused for years.  From time to time I thought about how much data might be hidden from other researchers in these kinds of histories.  These books and records were written as a labor of love to a local community.  I decided to create a surname index for the book that had unlocked my family line for me.  It would be just the right level of complexity to deepen by Python skills.

I wrote scripts to find all the proper nouns in the text and to wrangle them into a better format. Patterns that could be used to help identify people, surnames, and geographical places were apparent. The script did a good job of finding terms of interest, but the results are not perfect. For instance, is "Hill" a person or a geographical feature? Some of each are found in the text.  I was 90% of the way to having something to create my indexes from, but those last bits would be more difficult to accomplish programmatically.  The last 10% was done by old-fashioned editing. The process made me appreciate the work done by Python even more. 

These indexes are no doubt far from perfect. The text itself is not perfect. I hope the indexes help other researchers quickly gain access to the wealth of information in the book.  If the History of Marlow, New Hampshire is something of interest to you, I hope you will support the [Marlow Historical Society](http://www.marlownewhampshire.org/marlow-historical-society.php).  Copies of the book are available for sale from their website.  My indexes are for the 2002 version of the book. 

![History of Marlow cover picture](marlow_cover.png)

Created by **Mike Maynard**<BR>
Project Implemented in **Python**<BR>
Last updated:  **2021-07-12**

