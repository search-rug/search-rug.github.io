---
archived: false
available: true
category: Language Engineering Projects
is_group: false
keywords:
- language engineering
- graphical modeling
- Javascript
- Rascal
posted: 2023-02-10
short: The goal of this project is to investigate how to embed Web-based diagram editor
  frameworks into the Salix model for defining UIs.
supervisors:
- storm@cwi.nl
title: Embedding Diagram Editors into Salix
types:
- BSc
---

[Salix](https://github.com/cwi-swat/salix) is a framework in Rascal for defining immediate mode, web-based UIs. It follows the Elm model where an application is defined using a view function and an model update function.

Salix is an extensible framework, and currently features "embeddings" of "foreign" Javascript components, like CodeMirror, xterm.js, dagre-d3 and Google Charts. The goal of this project is to investigate how to embed Web-based diagram editor frameworks into the Salix model for defining UIs.

Deliverables:

- A survey of existing diagram editor components (for instance, [MxGraph](https://jgraph.github.io/mxgraph/)) and an assessment of their suitability for embedding in Salix.
- The implementation of an embedding of the chosen framework into Salix (i.e. using Rascal); the goal is to allow the definition of *custom* diagram editors using the framework, not just embed pre-existing editors (like UML editors).
- Evaluation using a case study (showing that and how it works).