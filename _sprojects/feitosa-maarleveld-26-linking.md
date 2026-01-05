---
archived: false
status: "Available"
category: Software & Architecture Analytics Projects 2025-26
is_group: true
keywords:
- software engineering 
- empirical research
- machine learning 
posted: 2026-01-05
description: Develop a machine learning model to predict what files require changes to resolve specific issues. The objective is to develop a machine learning model that takes in issue text, source code, and other information, and ranks all source files according to their relevance for the given issue. The end goal is to reduce developer time spent on code comprehension, and enable automated large-scale backlog analysis based on issues.
contact:
  header: Supervisor(s)
  members:
  - d.feitosa@rug.nl
  - j.maarleveld@rug.nl
title: 'Towards Issue Impact Prediction: Predicting Files for Issues'
types:
- BSc
- MSc
---

Software developers typically coordinate their work by creating *issues* in a project management system (e.g. Jira). 
Issues are used to track bugs, feature requests, and other work items. 
They typically contain a problem description, or a description of work to be done.

In resolving the issues, a significant amount of software developers' time is spent on code comprehension,
including determining what files should be changed to solve the issue.
Code comprehension can be even more time-consuming for developers that are new to a given project.

The goal of this project is to develop a machine learning model that can predict the files involved in a given issue,
given the text of an issue, and the current codebase. The model should rank all source files according to their relevance for the given issue.

This project can accomodate multiple students (including groups), exploring different approaches to the problem:

- **Pure-NLP models**: Use NLP models such as bag of words, word embeddings, and transformer models to predict the files involved in a given issue.

- **Multi-modal models**: Use models that combine information from different modalities,
such as text and historical changes, to predict the files involved in a given issue. 
This approach is more technical from a machine learning perspective; The idea is to map issue text and graph-based embeddings of historical information into a common embedding space, similar to CLIP [1].

### References
[1] Radford, Alec, et al. "Learning transferable visual models from natural language supervision." International conference on machine learning. PmLR, 2021.
