---
layout: default
title: Bounding Hallucinations: Information-Theoretic Guarantees for RAG Systems via Merlin-Arthur Protocols
---

# Bounding Hallucinations: Information-Theoretic Guarantees for RAG Systems via Merlin-Arthur Protocols

**arXiv**: [2512.11614v1](https://arxiv.org/abs/2512.11614) | [PDF](https://arxiv.org/pdf/2512.11614.pdf)

**作者**: Björn Deiseroth, Max Henning Höth, Kristian Kersting, Letitia Parcalabescu

---

## 💡 一句话要点

**提出基于Merlin-Arthur协议的训练框架，以提升检索增强生成系统的可验证性与可靠性。**

**关键词**: `检索增强生成` `交互证明系统` `可解释人工智能` `幻觉减少` `信息论保证` `自动监督`

## 📋 核心要点

1. 核心问题：当前RAG系统将检索视为启发式而非可验证证据，导致模型幻觉、依赖虚假证据。
2. 方法要点：将RAG管道建模为交互证明系统，通过Merlin提供证据、Morgana注入误导上下文，训练生成器基于证据回答、拒绝或依赖具体上下文。
3. 实验或效果：在多个数据集和模型上，M/A训练改善了模型的基础性、完整性和拒绝行为，减少了幻觉，并提升了检索器性能。

## 📄 摘要（原文）

> Retrieval-augmented generation (RAG) models rely on retrieved evidence to guide large language model (LLM) generators, yet current systems treat retrieval as a weak heuristic rather than verifiable evidence. As a result, LLMs answer without support, hallucinate under incomplete or misleading context, and rely on spurious evidence. We introduce a training framework that treats the entire RAG pipeline -- both the retriever and the generator -- as an interactive proof system via an adaptation of the Merlin-Arthur (M/A) protocol. Arthur (the generator LLM) trains on questions of unkown provenance: Merlin provides helpful evidence, while Morgana injects adversarial, misleading context. Both use a linear-time XAI method to identify and modify the evidence most influential to Arthur. Consequently, Arthur learns to (i) answer when the context support the answer, (ii) reject when evidence is insufficient, and (iii) rely on the specific context spans that truly ground the answer. We further introduce a rigorous evaluation framework to disentangle explanation fidelity from baseline predictive errors. This allows us to introduce and measure the Explained Information Fraction (EIF), which normalizes M/A certified mutual-information guarantees relative to model capacity and imperfect benchmarks. Across three RAG datasets and two model families of varying sizes, M/A-trained LLMs show improved groundedness, completeness, soundness, and reject behavior, as well as reduced hallucinations -- without needing manually annotated unanswerable questions. The retriever likewise improves recall and MRR through automatically generated M/A hard positives and negatives. Our results demonstrate that autonomous interactive-proof-style supervision provides a principled and practical path toward reliable RAG systems that treat retrieved documents not as suggestions, but as verifiable evidence.

