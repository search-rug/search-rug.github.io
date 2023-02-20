---
title: "Is Design Pattern Grime Related to Technical Debt?"
category: "Software & Architecture Analytics Projects"
keywords:
  - mining software repositories
  - empirical studies
  - technical debt
  - design patterns
is_group: true
available: true
types:
  - BSc
  - MSc
posted: 2023-02-10
supervisors:
  - name: "Daniel Feitosa"
    email: "d.feitosa@rug.nl"
---

The GoF (Gang-of-Four) design patterns (e.g., observer, command) are widely adopted in the industry as best practices and have well-investigated effects on software quality. However, not all instances of the same pattern are implemented equally. Deviations from the intended pattern structure (i.e., a buildup of elements such as classes unrelated to the pattern structure) are called pattern grime (or pollution). Among other side-effects, there is a correlation between the accumulation of grime and decreased levels of performance, security, and correctness of source code [1].

Another form of 'deviation from best practices' is Technical Debt (TD). TD refers to sub-optimal decisions (e.g., use a workaround) that can provide short-term benefits (e.g., meet a deadline) [2].

As you may have guessed by now, the main goal of this project is to find to what extent Technical Debt is correlated with Pattern Grime. For that, you will work on an empirical study where you will mine pattern grime and TD items from open-source software (OSS) projects and correlate the presence of TD items in pattern instances with higher levels of pattern grime.

This project is offered as a group BSc thesis or a single MSc thesis.

[1] Daniel Feitosa, Apostolos Ampatzoglou, Paris Avgeriou, and Elisa Y Nakagawa. 2018. Correlating Pattern Grime and Quality Attributes. In IEEE Access, vol. 6, pp. 23065-23078. https://doi.org/10.1109/ACCESS.2018.2829895.

[2] Paris Avgeriou, Philippe Kruchten, Ipek Ozkaya, and Carolyn Seaman. 2016. Managing Technical Debt in Software Engineering (Dagstuhl Seminar 16162). Dagstuhl Reports 6, 4 (2016), 110–138. https://doi.org/10.4230/DagRep.6.4.110