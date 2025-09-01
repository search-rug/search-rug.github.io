---
archived: false
status: "Available"
is_group: true
keywords:
- artificial intelligence
- generative ai
- java
- kotlin
posted: 2025-09-01
description: Develop core RAG back‑end modules in Java/Kotlin, covering document conversion, metadata enrichment, flexible chunking, advanced prompting, input guardrails, query transformation, multi‑source retrieval, result aggregation, and hallucination detection. Build a JUnit‑based testing framework to ensure deterministic, repeatable assessments and create comprehensive unit/integration tests. Collaborate with the UI team, mentor interns, and offer top performers a TA role for Block 2B 2026.
contact:
  header: Supervisor(s)
  members:
  - d.feitosa@rug.nl
title: "Development of RAG Modules for a Learning Assistant"
types:
- BSc int.
- MSc int.
---

The objective of this project is to build the back‑end engine that powers a conversational learning assistant for students. Interns will implement modules of a RAG pipeline using either Java or Kotlin. The work is organized in modular sub‑tasks, allowing participants to specialize in ingestion, processing, or evaluation while contributing to a cohesive system.

This project can accommodate multiple students, and each student will work on a set of responsibilities. Core responsibilities include:

- **Ingestion Layer** – Implement document conversion adapters, e.g., for PDFs, PowerPoint decks, plain‑text files, and Google Docs, followed by metadata enrichment (capturing content type, source URL, timestamps, and custom tags).
- **Chunking Strategies** – Design flexible splitting mechanisms (e.g., fixed‑size chunks, sentence‑level segmentation, and context‑aware sliding windows) that feed downstream vectorization.
- **Inference Enhancements** – Extend prompting capabilities with optional memory buffers, enforce input guardrails (privacy checks, profanity filters), and develop query transformers that can summarize or expand user intents before retrieval.
- **Retrieval & Aggregation** – Integrate multiple back‑ends (vector stores, SQL/text search, optional web‑search fallback) and devise ranking/aggregation logic that combines relevance scores, freshness, and confidence thresholds.
- **Output Guardrails** – Build hallucination detectors that compare generated answers against source excerpts, flagging inconsistencies for human review.
- **Testing Framework** – A dedicated testing framework will sit atop JUnit, providing utilities for deterministic re‑execution of flaky tests (e.g., retry policies, seed‑controlled randomness) and for generating synthetic workloads that stress‑test the end‑to‑end pipeline.

You will work closely with the Digital Lab team to iterate on prototypes, and incorporate feedback into successive sprints. Depending on your performance, you may be invited to serve as a Teaching Assistant for Block 2B 2026 to work on the first stable version of the system.
