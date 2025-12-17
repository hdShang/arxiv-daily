---
layout: default
title: LORE: A Large Generative Model for Search Relevance
---

# LORE: A Large Generative Model for Search Relevance

**arXiv**: [2512.03025v1](https://arxiv.org/abs/2512.03025) | [PDF](https://arxiv.org/pdf/2512.03025.pdf)

**作者**: Chenji Lu, Zhuo Chen, Hui Zhao, Zhiyuan Zeng, Gang Zhao, Junjie Ren, Ruicong Xu, Haoran Li, Songyan Liu, Pengjie Wang, Jian Xu, Bo Zheng

---

## 💡 一句话要点

**提出LORE框架，通过能力分解与两阶段训练提升电商搜索相关性。**

**关键词**: `搜索相关性` `大语言模型` `两阶段训练` `能力分解` `电商搜索` `RAIR基准`

## 📋 核心要点

1. 核心问题：现有方法将相关性视为单一任务，导致性能瓶颈。
2. 方法要点：将相关性分解为知识推理、多模态匹配和规则遵循能力，采用SFT与RL两阶段训练。
3. 实验或效果：在线部署三年，累计提升GoodRate指标27%，并建立RAIR基准评估。

## 📄 摘要（原文）

> Achievement. We introduce LORE, a systematic framework for Large Generative Model-based relevance in e-commerce search. Deployed and iterated over three years, LORE achieves a cumulative +27\% improvement in online GoodRate metrics. This report shares the valuable experience gained throughout its development lifecycle, spanning data, features, training, evaluation, and deployment. Insight. While existing works apply Chain-of-Thought (CoT) to enhance relevance, they often hit a performance ceiling. We argue this stems from treating relevance as a monolithic task, lacking principled deconstruction. Our key insight is that relevance comprises distinct capabilities: knowledge and reasoning, multi-modal matching, and rule adherence. We contend that a qualitative-driven decomposition is essential for breaking through current performance bottlenecks. Contributions. LORE provides a complete blueprint for the LLM relevance lifecycle. Key contributions include: (1) A two-stage training paradigm combining progressive CoT synthesis via SFT with human preference alignment via RL. (2) A comprehensive benchmark, RAIR, designed to evaluate these core capabilities. (3) A query frequency-stratified deployment strategy that efficiently transfers offline LLM capabilities to the online system. LORE serves as both a practical solution and a methodological reference for other vertical domains.

