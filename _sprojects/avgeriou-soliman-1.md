---
title: "Develop a Web-Based Self-Admitted Technical Debt Visualization and Management System"
category: "Software & Architecture Analytics Projects"
keywords:
  - software engineering
  - empirical studies
  - self-admitted technical debt
is_group: false
available: true
types:
  - BSc
  - MSc
posted: 2023-01-01
supervisors:
  - name: "Paris Avgeriou"
    email: "p.avgeriou@rug.nl"
  - name: "Mohamed Soliman"
    email: "m.a.m.soliman@rug.nl"
  - name: "Yikun Li"
    email: "yikun.li@rug.nl"
---

Technical debt refers to taking shortcuts, either deliberately or inadvertently, to achieve short-term goals, which might negatively influence the maintenance and evolution of software on the long term [2]. If technical debt is incurred immoderately and left unresolved, the accumulated technical debt can turn into maintenance burdens.

A part of technical debt is declared by the developers themselves (i.e., self-admitted technical debt). For instance, a developer found low-quality code, which complicates debugging; thus, he created a new ticket in the issue tracker to resolve the found code debt (code debt is a type of technical debt that results from poorly-written code; other types of debt are defined in the work of Alves et al. [1]):

>   If the user doesn't setup the right camel context for the context component.
>   The exception we got is misleading, we need to throw more meaningful 
>   exception for it. - [Camel-5714]

In another case, during a code review in issues, a developer found that a shortcut was taken. Thus, he commented the technical debt on a patch:

>   The patch looks good to me... It would be better if we can add an upper limit
>   for the size of the GSet. - [Hadoop-9763]

Technical debt statement examples shown above are identified and reported by developers in the JIRA issue tracker. Some of them are repaid while some are not. In order to better manage technical debt, we need to design and develop a visualization and management system to help developers manage self-admitted technical debt.

If you are interested in this project, please contact us for project detail information. Contact: [Yikun Li](mailto:yikun.li@rug.nl), [Mohamed Soliman](mailto:m.a.m.soliman@rug.nl), or [Paris Avgeriou](mailto:p.avgeriou@rug.nl)

**References:**

[1] Nicolli SR Alves, Leilane F Ribeiro, Vivyane Caires, Thiago S Mendes, and Rodrigo O Spínola. 2014. Towards an ontology of terms on technical debt. In 2014 Sixth International Workshop on Managing Technical Debt. IEEE, 1–7.

[2] Paris Avgeriou, Philippe Kruchten, Ipek Ozkaya, and Carolyn Seaman. 2016. Managing Technical Debt in Software Engineering (Dagstuhl Seminar 16162). Dagstuhl Reports 6, 4 (2016), 110–138. https://doi.org/10.4230/DagRep.6.4.110