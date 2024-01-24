---
archived: false
status: "Available"
category: Software & Architecture Analytics Projects 2023-24
is_group: true
keywords:
- technical debt
- software analytics
- machine learning
posted: 2024-01-15
description: The goal of this project is to select techniques previously used for vulnerability detection and check whether they are also successful in detecting technical debt in benchmark datasets.
contact:
  header: Supervisor(s)
  members:
  - d.feitosa@rug.nl
  - j.maarleveld@rug.nl
title: 'Applying Graph Learning For Technical Debt Detection'
types:
- BSc
- MSc
---

Technical debt refers to suboptimal decisions made by developers while writing software. Too much technical debt can cause the code to become difficult to maintain. As such, it is important to manage the amount of technical debt in a project. One of the steps involved in this process is actually identifying the technical debt.

In recent years, neural networks and deep learning have become popular. One particular development is the emergence of graph neural networks, which are neural networks which operate on graph data. Such neural networks have been applied on graph representations of code (e.g. ASTs) for vulnerability detection.

The goal of this project is to select techniques previously used for vulnerability detection from literature, apply them in the technical debt setting, and check whether these techniques are also successful in detecting technical debt in existing technical debt datasets.

### Relevant Literature

[1] T. Amanatidis, N. Mittas, A. Moschou, A. Chatzigeorgiou, A. Ampatzoglou, and L. Angelis, ‘Evaluating the agreement among technical debt measurement tools: building an empirical benchmark of technical debt liabilities’, Empirical Software Engineering vol. 25, no. 5, pp. 4161–4204, 2020.
doi: [10.1007/s10664-020-09869-w](https://doi.org/10.1007/s10664-020-09869-w).

[2] V. Lenarduzzi, N. Saarimäki, and D. Taibi. ‘The Technical Debt Dataset’. In Proceedings of the Fifteenth International Conference on Predictive Models and Data Analytics in Software Engineering, 2–11. PROMISE’19. New York, NY, USA: Association for Computing Machinery, 2019.
doi: [10.1145/3345629.3345630](https://doi.org/10.1145/3345629.3345630).

[3] L. Šikić, A. S. Kurdija, K. Vladimir, and M. Šilić, ‘Graph Neural Network for Source Code Defect Prediction’, IEEE Access, vol. 10, pp. 10402–10415, 2022.
doi: [10.1109/ACCESS.2022.3144598](https://doi.org/10.1109/ACCESS.2022.3144598).

[4] Y. Zhou, S. Liu, J. Siow, X. Du, and Y. Liu, ‘Devign: Effective Vulnerability Identification by Learning Comprehensive Program Semantics via Graph Neural Networks’, in Advances in Neural Information Processing Systems, Curran Associates, Inc., 2019.
url: [link](https://proceedings.neurips.cc/paper_files/paper/2019/hash/49265d2447bc3bbfe9e76306ce40a31f-Abstract.html)

[5] T. Sharma, and M. Kessentini. ‘QScored: A Large Dataset of Code Smells and Quality Metrics’. In 2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR), 590–94, 2021.
doi: [10.1109/MSR52588.2021.00080](https://doi.org/10.1109/MSR52588.2021.00080).

[6] S. Cao, X. Sun, L. Bo, Y. Wei, and B. Li. ‘BGNN4VD: Constructing Bidirectional Graph Neural-Network for Vulnerability Detection’. Information and Software Technology 136 (1 August 2021): 106576.
doi: [10.1016/j.infsof.2021.106576](https://doi.org/10.1016/j.infsof.2021.106576).

### Datasets

* Dataset from [1]: [link](https://zenodo.org/records/3979784)
* Dataset from [2]: [link](https://github.com/clowee/The-Technical-Debt-Dataset)
* Dataset from [6]: [link](https://zenodo.org/records/4468361)
