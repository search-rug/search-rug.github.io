---
archived: false
status: "Available"
category: Software & Architecture Analytics Projects 2024-25
is_group: true
keywords:
- technical debt
- empirical research
posted: 2025-02-25
description: The goal of this project is to analyse how developers document SATD in non-code artefacts such as emails or issue tracking systems. The objective is to answer questions like "Do developers know beforehand what changes have to be made" and "Do initially proposed changes align with the actual changes?".
contact:
  header: Supervisor(s)
  members:
  - d.feitosa@rug.nl
  - j.maarleveld@rug.nl
title: 'Do Developers Know Where and How to Resolve Self-Admitted Technical Debt?'
types:
- BSc
- MSc
---

Developers sometimes document shortcomings in their code. A common example would be the insertion of "TODO" comments. In case such remarks refer to technical debt, we call this "Self-Admitted Technical Debt" (SATD).

The goal of this project is to analyse how developers document SATD in non-code artefacts such as emails or issue tracking systems. Research has shown that sometimes, approximate (e.g. "In file X") or more exact ("File X, Line Y") links are mentioned in text [2]. However, existing research is limited in scope since it only considers a single company. The goal of this project is to analyse non-code artefacts in one or multiple open source projects, and investigate details like

- Do developers know where changes have to be made when reporting SATD?
- When resolving SATD, how do the actual changes differ from the initially reported required changes?
- Do resolved SATD issues actually fix the reported SATD?

This project will involve the use of existing SATD datasets and  tools to automatically identify likely SATD candidates in non-code artefacts, and then analysing the identified documents to answer questions like the ones outlined above.

### References

[1] Li, Y., Soliman, M., & Avgeriou, P. (2020). Identification and Remediation of Self-Admitted Technical Debt in Issue Trackers. 2020 46th Euromicro Conference on Software Engineering and Advanced Applications (SEAA), 495–503. [https://doi.org/10.1109/SEAA51224.2020.00083](https://doi.org/10.1109/SEAA51224.2020.00083)

[2] Li, Y., Soliman, M., Avgeriou, P., & Somers, L. (2023). Self-Admitted Technical Debt in the Embedded Systems Industry: An Exploratory Case Study. IEEE Transactions on Software Engineering, 49(4), 2545–2565. IEEE Transactions on Software Engineering. [https://doi.org/10.1109/TSE.2022.3224378](https://doi.org/10.1109/TSE.2022.3224378)

[3] Tan, J., Feitosa, D., & Avgeriou, P. (2023). The lifecycle of Technical Debt that manifests in both source code and issue trackers. Information and Software Technology, 159, 107216. [https://doi.org/10.1016/j.infsof.2023.107216](https://doi.org/10.1016/j.infsof.2023.107216)
