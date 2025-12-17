---
layout: default
title: Natural Language Summarization Enables Multi-Repository Bug Localization by LLMs in Microservice Architectures
---

# Natural Language Summarization Enables Multi-Repository Bug Localization by LLMs in Microservice Architectures

**arXiv**: [2512.05908v1](https://arxiv.org/abs/2512.05908) | [PDF](https://arxiv.org/pdf/2512.05908.pdf)

**作者**: Amirkia Rafiei Oskooei, S. Selcan Yukcu, Mehmet Cevheri Bozoglan, Mehmet S. Aktas

---

## 💡 一句话要点

**提出基于自然语言摘要的多仓库微服务架构缺陷定位方法，以解决语义鸿沟与LLM上下文限制问题。**

**关键词**: `缺陷定位` `微服务架构` `自然语言摘要` `多仓库搜索` `LLM应用` `代码理解`

## 📋 核心要点

1. 核心问题：多仓库微服务架构中，自然语言缺陷报告与代码间的语义鸿沟、LLM上下文限制及仓库识别困难。
2. 方法要点：将代码库转化为层次化自然语言摘要，通过自然语言到自然语言搜索进行两阶段缺陷定位。
3. 实验或效果：在工业系统DNext上评估，Pass@10达0.82，MRR达0.50，优于检索基线和GitHub Copilot等系统。

## 📄 摘要（原文）

> Bug localization in multi-repository microservice architectures is challenging due to the semantic gap between natural language bug reports and code, LLM context limitations, and the need to first identify the correct repository. We propose reframing this as a natural language reasoning task by transforming codebases into hierarchical NL summaries and performing NL-to-NL search instead of cross-modal retrieval. Our approach builds context-aware summaries at file, directory, and repository levels, then uses a two-phase search: first routing bug reports to relevant repositories, then performing top-down localization within those repositories. Evaluated on DNext, an industrial system with 46 repositories and 1.1M lines of code, our method achieves Pass@10 of 0.82 and MRR of 0.50, significantly outperforming retrieval baselines and agentic RAG systems like GitHub Copilot and Cursor. This work demonstrates that engineered natural language representations can be more effective than raw source code for scalable bug localization, providing an interpretable repository -> directory -> file search path, which is vital for building trust in enterprise AI tools by providing essential transparency.

