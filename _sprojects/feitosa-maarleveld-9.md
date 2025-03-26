---
archived: false
status: "Available"
category: Software & Architecture Analytics Projects 2024-25
is_group: true
keywords:
- empirical research
- technical debt
posted: 2025-02-25
description: The goal of this project is to create a machine learning based system which can help determining whether a given fix for an SATD issue is actually correct. The project will involve creating an extended dataset of SATD items reported in issue tracking systems, together with the commits fixing the reported SATD items. This dataset will then be used to develop a machine learning model. The created model will enable more extensive collection of correct SATD fixes for use in future research.
contact:
  header: Supervisor(s)
  members:
  - d.feitosa@rug.nl
  - j.maarleveld@rug.nl
title: 'Creating a Dataset of SATD Fixes and Developing Semi-Automated Tooling to Detect Them'
types:
- BSc
- MSc
---

Developers sometimes document shortcomings in their code. A common example would be the insertion of "TODO" comments. In case such remarks refer to technical debt, we call this "Self-Admitted Technical Debt" (SATD).

The goal of this project is to create an extended dataset of SATD items reported in issue tracking systems, together with the commits fixing the reported SATD items, in a similar fashion as done in [2]. Moreover, the goal is to develop a machine learning model enabling more efficient searching.

This project will involve the use of existing methods to detect likely SATD candidates in issue tracking systems, and manual confirmation of the presence of SATD and corresponding fixes in the commits associated with the identified issues. This way, an initial dataset of SATD items with fixes is created, which can be used to develop a machine learning model to find likely correct SATD fixes for manual identification. The second step is development and evaluation of the machine learning model, which will involve natural lanuage proceessing and machine learning models, including language models such as BERT.

### References

[1] Li, Y., Soliman, M., & Avgeriou, P. (2020). Identification and Remediation of Self-Admitted Technical Debt in Issue Trackers. 2020 46th Euromicro Conference on Software Engineering and Advanced Applications (SEAA), 495–503. [https://doi.org/10.1109/SEAA51224.2020.00083](https://doi.org/10.1109/SEAA51224.2020.00083)

[2] Tan, J., Feitosa, D., & Avgeriou, P. (2022). Does it matter who pays back Technical Debt? An empirical study of self-fixed TD. Information and Software Technology, 143, 106738. [https://doi.org/10.1016/j.infsof.2021.106738](https://doi.org/10.1016/j.infsof.2021.106738)

[3] Tan, J., Feitosa, D., & Avgeriou, P. (2023). The lifecycle of Technical Debt that manifests in both source code and issue trackers. Information and Software Technology, 159, 107216. [https://doi.org/10.1016/j.infsof.2023.107216](https://doi.org/10.1016/j.infsof.2023.107216)
