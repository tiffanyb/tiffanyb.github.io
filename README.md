15/18-487 Introduction to Computer Security, Fall 2017
======================================================

An experiment of 15/18-487 site setup based on [Steve's No-Good-Very-Bad 
Jekyll Theme](https://github.com/svmiller/steve-ngvb-jekyll-template).

---

# 15/18487-f17 Lecture Post Markdown

The 15/18487-f17 website is based on the [steve-ngvb Jekyll template](https://github.com/svmiller/steve-ngvb-jekyll-template). Modifications were made to post entries to simplify formatting on the Lectures page.

Modifications made to the YAML FrontMatter (top of each post in between the `---`) allow for the easy construction of these lectures.

**Note:** Text in the body of the posts no longer is used, as the YAML FrontMatter is what's used to generate the lectures on the lecture page.

## Adding a Summary

```
title: Lecture Title
categories: category1
summary: >
  This is my summary. It can be pretty
  long if I wanted it to.
```

## Adding Slides

If slides are to be included, simply include the slides filename in the `slides` parameter. **The `slides/` directory is automatically prepended, so you only need the filename itself.**

```
title: Lecture Title
categories: category1
summary: >
  This is my summary. It can be pretty
  long if I wanted it to.
slides: slides_filename.pptx
```

## Adding Lecture Readings
Readings for lectures can be either required or optional. For styling purposes on the lectures page, we differentiate between the two.

### Required Readings
Required readings take a title and either a filename or URL. If we want to give a file we are hosting statically, we use the `file` parameter and give it the file located in the `reading/` directory. **The `reading` directory path is automatically prepended, so you only need the filename itself.**

```
title: Lecture Title
categories: category1
summary: >
  This is my summary. It can be pretty
  long if I wanted it to.
reading:
 - title: Reading Title
   file: filename_in_reading_directory.pdf
```

If the reading is a URL, use the `url` parameter, and add the URL as-is in there.

```
title: Lecture Title
categories: category1
summary: >
  This is my summary. It can be pretty
  long if I wanted it to.
reading:
 - title: Reading Title
   url: https://website.com/reading.html
```

### Optional Readings
The optional readings use the exact same parameters as the required readings but with `optional` instead of `reading`.

```
title: Lecture Title
categories: category1
summary: >
  This is my summary. It can be pretty
  long if I wanted it to.
optional:
 - title: Optional Reading Title
   file: optional_reading.pdf
```

```
title: Lecture Title
categories: category1
summary: >
  This is my summary. It can be pretty
  long if I wanted it to.
optional:
 - title: Optional Reading Title
   url: https://website.com/optional.html
```

## Example

Now here's an example post tying all of that together. This is currently found in _posts/2017-09-18-return-oriented-programming.md.

```
---
layout: post
title: Return Oriented Programming
date: 2017-09-18
categories: binary-exploitation
summary: >
  This lecture will cover Return Oriented Programming.
slides: 06-ROP.pptx
reading:
 - title: The Geometry of Innocent Flesh on the Bone Return-into-libc without Calls (on the x86)
   file: Shacham_2007_The Geometry of Innocent Flesh on the Bone Return-into-libc without Function Calls (on the x86).pdf
optional:
 - title: Return-Oriented Programming Systems, Languages, and Applications
   url: https://cseweb.ucsd.edu/~hovav/dist/rop.pdf
 - title: Q Exploit Hardening Made Easy
   url: http://dl.acm.org/citation.cfm?id=2028092
 - title: ropasaurusrex a primer on return-oriented
   url: https://blog.skullsecurity.org/2013/ropasaurusrex-a-primer-on-return-oriented-programming
---

Hi!

```