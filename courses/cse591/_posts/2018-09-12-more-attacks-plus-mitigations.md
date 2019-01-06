---
layout: post
title: "Control-Flow Attacks and Defenses"
category: "Software Security"
prof: Vyas
summary: >
  In this lecture we will present additional control-flow-hijacking attacks that gain 
  control of the instruction pointer, e.g., format-string exploits, and integer overflows.

  We will then introduce control flow hijack defenses found in practice 
  today, including canaries, DEP, and randomization (ASLR). We will also 
  discuss methods for bypassing these defenses.

reading:
 - title: Exploiting Format String Vulnerabilities
   file: Scut_2001_Exploiting Format String Vulnerabilities(2).pdf
 - title: Smashing the Stack in 2011
   file: Makowski_2011_Smashing the Stack in 2011.pdf
 - title: Design of ASLR in PAX
   file: PAX_Unknown_Design of PAX ASLR on Linux.pdf
 - title: ASLR Smack and Laugh Reference
   file: Muller_2008_ASLR Smack & Laugh Reference Seminar on Advanced Exploitation Techniques.pdf
optional:
 - title: Effectiveness of ASLR
   file: Shacham_2004_ASLR_Effectiveness.pdf
---

