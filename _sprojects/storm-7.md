---
title: "CodeBuff in Rascal"
category: "Language Engineering Projects"
short: ""
keywords:
  - language engineering
  - pretty printing
  - machine learning
is_group: false
available: true
types:
  - BSc
posted: 2023-01-01
supervisors:
  - name: "Tijs van der Storm"
    email: "storm@cwi.nl"
---

DESCRIPTION

Pretty printing is one aspect of language engineering that's often overlooked, but nevertheless important. Unfortunately, developing a (good) pretty printer is very hard. For instance, Bob Nystrom, of Google, called his Dart formatter, "the hardest program I've ever written".

Fortunately, Terence Parr (the ANTLR guy) and Jurgen Vinju recently developed CodeBuff: a universal formatter that learns formatting rules from samples of source code exhibiting the desired formatting. Their paper won the distinguished paper award at the International Conference on Software Language Engineering (SLE'16).

CodeBuff has been implemented in the context of the ANTLR parse generator, and uses its internal parse tree data structures for learning and formatting. We're interested in transferring CodeBuff to the context of the Rascal language workbench. A key technical challenge, however, is that the way ANTLR and Rascal deal with layout nodes (i.e. nodes in the parse tree containing whitespace, comments etc.) is different. Thus, porting CodeBuff to Rascal, requires conceptual changes to the learning and formatting algorithms. Figuring out how, is exactly the goal of this project.
