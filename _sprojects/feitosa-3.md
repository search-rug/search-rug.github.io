---
archived: false
available: true
category: Software & Architecture Analytics Projects 2022-23
is_group: false
keywords:
- mining software repositories
- software analytics
- cloud infrastructure
posted: 2023-02-10
short: This project aims at building an MSR data collection infrastructure that can
  evolve and scale with minimum interruption.
supervisors:
- d.feitosa@rug.nl
title: 'Software Mining Rig: Building a Scalable MSR Infrastructure for Research'
types:
- BSc
- MSc Int
---

Mining Software Repositories (MSR) is an established research approach to extract generalizable knowledge from code-hosting platforms (e.g., GitHub and GitLab) and associated tools (e.g., issue trackers such as Jira, and email lists). Due to the scale of MSR studies (e.g., investigating thousands of repositories), tooling is a central piece of any method to reduce an already very time-consuming set of tasks. However, reusing tools between studies is not trivial and seldom happens in practice.

This project aims at building an MSR data collection infrastructure that can evolve and scale with minimum interruption. Although not a requirement per se, this project originated with the idea to leverage recent technologies such as [GrimoreLab](https://github.com/chaoss/grimoirelab).

Ideally, some of the intended requirements for this infrastructure are:

- Facilitated and configurable deployment via Infrastructure-as-Code;
- Centralized database;
- Plug-in data analytics on the fly;
- Client for querying data (e.g., CLI or RESTful).