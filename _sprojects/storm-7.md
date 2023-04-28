---
archived: false
available: true
category: Language Engineering Projects
is_group: false
keywords:
- language engineering
- pretty printing
- machine learning
posted: 2023-01-01
short: CodeBuff has been implemented in the context of the ANTLR parse generator,
  and uses its internal parse tree data structures for learning and formatting. We're
  interested in transferring CodeBuff to the context of the Rascal language workbench.
supervisors:
- storm@cwi.nl
title: CodeBuff in Rascal
types:
- BSc
---

Pretty printing is one aspect of language engineering that's often overlooked, but nevertheless important. Unfortunately, developing a (good) pretty printer is very hard. For instance, Bob Nystrom, of Google, called his Dart formatter, ["the hardest program I've ever written"](http://journal.stuffwithstuff.com/2015/09/08/the-hardest-program-ive-ever-written/).

Fortunately, Terence Parr (the ANTLR guy) and Jurgen Vinju recently developed CodeBuff: a universal formatter that learns formatting rules from samples of source code exhibiting the desired formatting. Their [paper](https://arxiv.org/abs/1606.08866) won the distinguished paper award at the International Conference on Software Language Engineering (SLE'16).

CodeBuff has been implemented in the context of the ANTLR parse generator, and uses its internal parse tree data structures for learning and formatting. We're interested in transferring CodeBuff to the context of the [Rascal](http://www.rascal-mpl.org/) language workbench. A key technical challenge, however, is that the way ANTLR and Rascal deal with layout nodes (i.e. nodes in the parse tree containing whitespace, comments etc.) is different. Thus, porting CodeBuff to Rascal, requires conceptual changes to the learning and formatting algorithms. Figuring out how, is exactly the goal of this project.

Deliverables:

- A precise description of the CodeBuff algorithm, including the required modifications for working with Rascal parse trees.
- (Re-)evaluation of the CodeBuff learning and formatting quality using the case studies of the paper.
- Evaluation in the context of other Rascal-defined languages (including Rascal itself).