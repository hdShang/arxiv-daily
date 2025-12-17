---
layout: default
title: HalluGraph: Auditable Hallucination Detection for Legal RAG Systems via Knowledge Graph Alignment
---

# HalluGraph: Auditable Hallucination Detection for Legal RAG Systems via Knowledge Graph Alignment

**arXiv**: [2512.01659v1](https://arxiv.org/abs/2512.01659) | [PDF](https://arxiv.org/pdf/2512.01659.pdf)

**作者**: Valentin Noël, Elimane Yassine Seidou, Charly Ken Capo-Chichi, Ghanem Amari

---

## 💡 一句话要点

**提出HalluGraph框架，通过知识图谱对齐检测法律RAG系统中的幻觉，以解决可审计性问题。**

**关键词**: `幻觉检测` `知识图谱对齐` `法律RAG系统` `可审计性` `图论框架` `实体接地`

## 📋 核心要点

1. 核心问题：法律AI系统在生成文本时可能产生幻觉，现有检测方法容忍实体替换，导致高风险错误。
2. 方法要点：基于图论框架，通过提取上下文、查询和响应的知识图谱进行结构对齐，量化幻觉为实体接地和关系保持指标。
3. 实验或效果：在结构化文档上AUC达0.979，在生成任务上AUC约0.89，优于语义相似性基线，提供透明审计追踪。

## 📄 摘要（原文）

> Legal AI systems powered by retrieval-augmented generation (RAG) face a critical accountability challenge: when an AI assistant cites case law, statutes, or contractual clauses, practitioners need verifiable guarantees that generated text faithfully represents source documents. Existing hallucination detectors rely on semantic similarity metrics that tolerate entity substitutions, a dangerous failure mode when confusing parties, dates, or legal provisions can have material consequences. We introduce HalluGraph, a graph-theoretic framework that quantifies hallucinations through structural alignment between knowledge graphs extracted from context, query, and response. Our approach produces bounded, interpretable metrics decomposed into \textit{Entity Grounding} (EG), measuring whether entities in the response appear in source documents, and \textit{Relation Preservation} (RP), verifying that asserted relationships are supported by context. On structured control documents, HalluGraph achieves near-perfect discrimination ($>$400 words, $>$20 entities), HalluGraph achieves $AUC = 0.979$, while maintaining robust performance ($AUC \approx 0.89$) on challenging generative legal task, consistently outperforming semantic similarity baselines. The framework provides the transparency and traceability required for high-stakes legal applications, enabling full audit trails from generated assertions back to source passages.

