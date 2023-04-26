---
archived: false
available: true
category: Language Engineering Projects
is_group: false
keywords:
- language engineering
- grammarware
- Rascal
- Swift
- reverse engineering
posted: 2023-01-01
short: In this project the goal is to obtain a high quality Rascal grammar from the
  Swift language reference, in a (semi-)automatic, traceable way.
supervisors:
- storm@cwi.nl
title: Extracting a Rascal Grammar from the Swift Reference Manual
types:
- BSc
---

Grammars are an essential component of many meta programming scenarios, such as static analysis, mass maintenance, and refactoring. In this project the goal is to obtain a high quality [Rascal](http://www.rascal-mpl.org/) grammar from the Swift language reference, in a (semi-)automatic, traceable way. In particular, we're interested in the grammar transformation steps needed to go from a "documentation" grammar, to a grammar that can be used for parsing.

Deliverables

- A prototype tool to extract the Swift grammar
- An analysis of transformations needed for recovering disambiguation constructs
- Evaluation by parsing realistic Swift code.