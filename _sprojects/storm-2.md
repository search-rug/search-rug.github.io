---
archived: false
available: true
category: Software & Architecture Analytics Projects
is_group: false
keywords:
- source code analysis
- M3
- Rascal
- smart contracts
posted: 2023-01-01
short: The goal of this project is provide an M3 bridge to the Ethereum Solidity language.
  This will enable analysis and reverse engineering of Smart Contracts running on
  the Ethereum blockchain.
supervisors:
- storm@cwi.nl
title: 'M3Solidity: M3 Source Code Model for Ethereum Solidity'
types:
- BSc
---

Rascal is a language workbench and environment for source code analysis and transformation. One library component of Rascal is *M3* a general model to represent facts about source code. It includes information on files, classes, ASTs, name binding, type relations, containment, and optionally inheritance, call graphs etc. Currently, the model has been instantiated for Java, Javascript, and CSharp. The goal of this project is provide an M3 bridge to the Ethereum Solidity language. This will enable analysis and reverse engineering of Smart Contracts running on the Ethereum blockchain.

Deliverables:

- A systematic exploration of which M3 features capture which Solidity language features.
- The development of a parsing front-end and/or Rascal grammar to parse Solidity into M3 ASTs.
- Development of basic M3 "databases" such as name resolution and containment.
- Evaluation by performing experiments analyzing actual Solidity code (for instance, computing metrics like SLOC or McCabe complexity).

### Resources

- [http://www.rascal-mpl.org](http://www.rascal-mpl.org)
- [https://solidity.readthedocs.io/en/develop/](https://solidity.readthedocs.io/en/develop/)
- M3: [http://www.cs.ecu.edu/hillsma/publications/swan-m3.pdf](http://www.cs.ecu.edu/hillsma/publications/swan-m3.pdf)