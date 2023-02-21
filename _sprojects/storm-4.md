---
title: "Hybrid Partial Evaluation for Javascript"
category: "Language Engineering Projects"
keywords:
  - language engineering
  - partial evaluation
  - compilation
  - interpreters
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
Partial evaluation is a technique for optimizing interpreters of programming languages. It works by fixing one of the arguments to the intepreter (i.e., the program), but leaving other parameters open (i.e., the dynamic input). A partial evaluator then "executes" the program, evaluating as much as possible. Partial evaluation is a well-research topic, both theoretically, and practically. A recent technique that claims to solve one of the problems of partial evaluation (e.g., code explosion) is Hybrid Partial Evaluation (see reference below). This original work is based on class-based OO languages (i.e., Java). The goal of this project is to transfer the idea of Hybrid partial evaluation to Javascript.