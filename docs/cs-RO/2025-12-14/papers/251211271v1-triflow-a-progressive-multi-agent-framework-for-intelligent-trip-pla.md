---
layout: default
title: TriFlow: A Progressive Multi-Agent Framework for Intelligent Trip Planning
---

# TriFlow: A Progressive Multi-Agent Framework for Intelligent Trip Planning

**arXiv**: [2512.11271v1](https://arxiv.org/abs/2512.11271) | [PDF](https://arxiv.org/pdf/2512.11271.pdf)

**作者**: Yuxing Chen, Basem Suleiman, Qifan Chen

---

## 💡 一句话要点

**提出TriFlow多智能体框架以解决旅行规划中约束满足和效率问题**

**关键词**: `旅行规划` `多智能体框架` `约束优化` `LLM协作` `渐进式推理`

## 📋 核心要点

1. 核心问题：现有LLM智能体在旅行规划中难以满足时空预算约束，导致计划不可行或低效
2. 方法要点：采用检索-规划-治理三阶段流水线，结合规则与LLM协作渐进优化行程
3. 实验或效果：在TravelPlanner和TripTailor基准上达到91.1%和97%通过率，运行效率提升超10倍

## 📄 摘要（原文）

> Real-world trip planning requires transforming open-ended user requests into executable itineraries under strict spatial, temporal, and budgetary constraints while aligning with user preferences. Existing LLM-based agents struggle with constraint satisfaction, tool coordination, and efficiency, often producing infeasible or costly plans. To address these limitations, we present TriFlow, a progressive multi-agent framework that unifies structured reasoning and language-based flexibility through a three-stage pipeline of retrieval, planning, and governance. By this design, TriFlow progressively narrows the search space, assembles constraint-consistent itineraries via rule-LLM collaboration, and performs bounded iterative refinement to ensure global feasibility and personalisation. Evaluations on TravelPlanner and TripTailor benchmarks demonstrated state-of-the-art results, achieving 91.1% and 97% final pass rates, respectively, with over 10x runtime efficiency improvement compared to current SOTA.

