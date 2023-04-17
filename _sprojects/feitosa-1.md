---
title: "Upgrade Design Pattern Detector and Quality Assessment"
category: "ML, NLP and Refactoring Projects 2022-23"
archived: false
short: "This project entails the refactoring and upgrade (incl. dependencies' update and small bug fixes) of both SSAP and Spoon-PttGrime."
keywords:
  - refactoring
  - design patterns
  - software analytics
is_group: false
available: true
types:
  - BSc
  - MSc Int
posted: 2023-02-10
supervisors:
  - Dr. Daniel Feitosa
---

The GoF (Gang-of-Four) **design patterns** (e.g., observer, command) are widely adopted in the industry as best practices and have well-investigated effects on software quality. However, not all instances of the same pattern are implemented equally. Deviations from the intended pattern structure (i.e., a buildup of elements such as classes unrelated to the pattern structure) are called **pattern grime** (or pollution). Among other side-effects, there is a correlation between the accumulation of grime and decreased levels of performance, security, and correctness of source code [1].

The SEARCH group has built two tools to support the measurement of pattern grime: [SSAP](https://github.com/search-rug/ssap) and [Spoon-PttGrime](https://github.com/search-rug/spoon-pttgrime). SSAP is combined with the [Design Pattern Detector (DPD)](https://users.encs.concordia.ca/~nikolaos/pattern_detection.html) to extract pattern-participating classes (e.g., concrete commands of a command pattern); for more details, see Section III.C, step 2 in [1]. Spoon-PttGrime calculates six metrics for measuring class, modular and organizational grime; for more details, see Section III.C, step 3 in [1].

This project entails the **refactoring and upgrade** (incl. dependencies' update and small bug fixes) of both SSAP and Spoon-PttGrime. It can be taken as one or two Short Programming Projects (**SPP**) (depending on the level of refactoring), or a **master's intership**.

### References

- [1] Daniel Feitosa, Apostolos Ampatzoglou, Paris Avgeriou, and Elisa Y Nakagawa. 2018. Correlating Pattern Grime and Quality Attributes. In IEEE Access, vol. 6, pp. 23065-23078. <https://doi.org/10.1109/ACCESS.2018.2829895>.
