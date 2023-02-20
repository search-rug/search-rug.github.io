---
title: "Domain-specific Spreadsheet Languages and Tools"
category: "Language Engineering Projects"
keywords:
  - language engineering
  - spreadsheets
  - end-user programming
is_group: false
available: true
types:
  - MSc
posted: 2023-02-10
supervisors:
  - name: "Tijs van der Storm"
    email: "storm@cwi.nl"
---
DESCRIPTION
Rascal is a meta programming language and language workbench for developing source code analysis and transformation tools. This includes compilers for programming languages and DSLs. Currently, Rascal can be considered a textual language workbench since it takes plain-text source code as input and produces various kinds of output.

Textual source code, however, is not always desired. For instance, business users generally prefer structured interfaces, like spreadsheets. The goal of this project is to explore how Rascal can support the definition of domain-specific spreadsheet languages. This means that the primary user interface for a DSL user is a grid of cells. The contents of each cell is defined by an ordinary textual grammar. Furthermore, there may be additional structural constraints on the shape of the grid, and how the grid can be modified.