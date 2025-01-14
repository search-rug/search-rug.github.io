---
archived: false
status: "Available"
category: Software Analytics Projects 2023-24
is_group: false
keywords:
- software engineering
- empirical research
- industry collaboration
posted: 2023-12-04
description: This thesis will look into the unsupervised Anomaly Detection (AD) solutions in the DevOps CI/CD pipeline of SIG. 
contact:
  header: Supervisor(s)
  members:
  - a.rastogi@rug.nl
title: Anomaly Detection in DevOps (CI/CD)
types:
- MSc thesis
---
**Problem Statement**
The tools used in the DevOps CI/CID pipeline generate a significant amount of data. This data is usually manually reviewed as part of the development process to identify issues that
must be addressed. This process is time-consuming and error-prone.

This thesis will help identify anomaly detection solution(s) that can be used to identify issues before software is deployed. In other words, the focus is on the Development and Staging parts of the DevOps DSP model [1].

The data generated during DevOps's development and staging phase is unlabelled; therefore, we first want to look into the unsupervised Anomaly Detection (AD) solutions [2]. These solutions would utilize different data available, e.g., numbers of code lines added/removed
per commit, number of tests, number of failed tests, etc.
Research Questions
Q1. Which unsupervised anomaly detection algorithms and which code/development metrics should be used for anomaly detection?
Q2. What is the performance of the proposed solution?

**Tentative Approach**
The research will take three phases – during the first phase, exploration of anomaly detection,
different code metrics, repositories, etc. will take place. This would also include a (statistical)
modeling of the identified metrics. The outcomes of this phase would be used to set up the
experimental environment and refine the questions. During the second phase, experiments
will be developed and conducted. The performance of the applied AD algorithms and
solutions will be evaluated.

### Relevant Literature
[1] Bass, L., "The Software Architect and DevOps" in IEEE Software, 35 (01), pp. 8-10, 2018.

[2] Zhao, Y., Nasrullah, Z. and Li, Z., “PyOD: A Python Toolbox for Scalable Outlier Detection” in
Journal of machine learning research (JMLR), 20(96), pp.1-7.

