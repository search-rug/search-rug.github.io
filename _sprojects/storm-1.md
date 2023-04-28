---
archived: false
available: true
category: Language Engineering Projects
is_group: false
keywords:
- language engineering
- spreadsheets
- end-user programming
posted: 2023-02-10
short: The goal of this project is to explore how Rascal can support the definition
  of domain-specific spreadsheet languages.
supervisors:
- storm@cwi.nl
title: Domain-specific Spreadsheet Languages and Tools
types:
- MSc
---

[Rascal](http://www.rascal-mpl.org/) is a meta programming language and language workbench for developing source code analysis and transformation tools. This includes compilers for programming languages and DSLs. Currently, Rascal can be considered a textual language workbench since it takes plain-text source code as input and produces various kinds of output.

Textual source code, however, is not always desired. For instance, business users generally prefer structured interfaces, like spreadsheets. The goal of this project is to explore how Rascal can support the definition of domain-specific spreadsheet languages. This means that the primary user interface for a DSL user is a grid of cells. The contents of each cell is defined by an ordinary textual grammar. Furthermore, there may be additional structural constraints on the shape of the grid, and how the grid can be modified.

Components of the work:

- Detailed literature study of spreadsheet-based languages or systems.
- Design of a "spreadsheet grammar" formalism which supports defining spreadsheet-based languages.
- Implementation of a prototype which shows feasibility and viability of putting spreadsheets in front of Rascal.
- Evaluation using a case-study DSL (for instance, the questionnaire language QL)

### Literature

- Markus Voelter's work on language-oriented business applications.
- Adam, Schultz. [Towards tool support for spreadsheet-based domain-specific languages](http://dl.acm.org/citation.cfm?id=2814215), GPCE'15.