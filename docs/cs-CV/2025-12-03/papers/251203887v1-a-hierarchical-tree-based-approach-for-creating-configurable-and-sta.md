---
layout: default
title: A Hierarchical Tree-based approach for creating Configurable and Static Deep Research Agent (Static-DRA)
---

# A Hierarchical Tree-based approach for creating Configurable and Static Deep Research Agent (Static-DRA)

**arXiv**: [2512.03887v1](https://arxiv.org/abs/2512.03887) | [PDF](https://arxiv.org/pdf/2512.03887.pdf)

**作者**: Saurav Prateek

---

## 💡 一句话要点

**提出基于分层树结构的可配置静态深度研究代理，以解决复杂多轮研究任务中静态RAG管道的局限性。**

**关键词**: `深度研究代理` `分层树结构` `可配置参数` `多跳检索` `并行研究` `RACE评估`

## 📋 核心要点

1. 核心问题：静态RAG管道在处理复杂多轮研究任务时存在局限性，需要更灵活的代理系统。
2. 方法要点：引入可配置的深度和广度参数，通过分层树结构实现多跳信息检索和并行子主题研究。
3. 实验或效果：在DeepResearch Bench上评估，配置深度2和广度5时获得34.72分，验证参数增加可提升研究深度和评分。

## 📄 摘要（原文）

> The advancement in Large Language Models has driven the creation of complex agentic systems, such as Deep Research Agents (DRAs), to overcome the limitations of static Retrieval Augmented Generation (RAG) pipelines in handling complex, multi-turn research tasks. This paper introduces the Static Deep Research Agent (Static-DRA), a novel solution built upon a configurable and hierarchical Tree-based static workflow.
>   The core contribution is the integration of two user-tunable parameters, Depth and Breadth, which provide granular control over the research intensity. This design allows end-users to consciously balance the desired quality and comprehensiveness of the research report against the associated computational cost of Large Language Model (LLM) interactions. The agent's architecture, comprising Supervisor, Independent, and Worker agents, facilitates effective multi-hop information retrieval and parallel sub-topic investigation.
>   We evaluate the Static-DRA against the established DeepResearch Bench using the RACE (Reference-based Adaptive Criteria-driven Evaluation) framework. Configured with a depth of 2 and a breadth of 5, and powered by the gemini-2.5-pro model, the agent achieved an overall score of 34.72. Our experiments validate that increasing the configured Depth and Breadth parameters results in a more in-depth research process and a correspondingly higher evaluation score. The Static-DRA offers a pragmatic and resource-aware solution, empowering users with transparent control over the deep research process. The entire source code, outputs and benchmark results are open-sourced at https://github.com/SauravP97/Static-Deep-Research/

