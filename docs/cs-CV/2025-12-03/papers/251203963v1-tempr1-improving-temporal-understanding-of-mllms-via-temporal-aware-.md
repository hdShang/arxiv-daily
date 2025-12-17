---
layout: default
title: TempR1: Improving Temporal Understanding of MLLMs via Temporal-Aware Multi-Task Reinforcement Learning
---

# TempR1: Improving Temporal Understanding of MLLMs via Temporal-Aware Multi-Task Reinforcement Learning

**arXiv**: [2512.03963v1](https://arxiv.org/abs/2512.03963) | [PDF](https://arxiv.org/pdf/2512.03963.pdf)

**作者**: Tao Wu, Li Yang, Gen Zhan, Yiting Liao, Junlin Li, Deliang Fu, Li Zhang, Limin Wang

---

## 💡 一句话要点

**提出TempR1框架，通过时态感知多任务强化学习增强多模态大语言模型的时序理解能力。**

**关键词**: `多模态大语言模型` `时序理解` `强化学习` `多任务学习` `长视频分析` `时序定位`

## 📋 核心要点

1. 核心问题：现有强化学习方法在时序理解中任务类型和数据有限，泛化能力不足。
2. 方法要点：构建多任务语料库，基于GRPO算法设计针对不同时序对应类型的定位奖励。
3. 实验或效果：在多个基准测试中达到最优性能，联合优化产生协同效应，提升泛化和单任务表现。

## 📄 摘要（原文）

> Enhancing the temporal understanding of Multimodal Large Language Models (MLLMs) is essential for advancing long-form video analysis, enabling tasks such as temporal localization, action detection, and time-sensitive question answering. While reinforcement learning (RL) has recently been explored for improving temporal reasoning, existing approaches are often confined to limited task types and data, restricting their generalization across diverse temporal understanding scenarios. To address this challenge, we present TempR1, a temporal-aware multi-task reinforcement learning framework that systematically strengthens MLLMs' temporal comprehension. We curate a multi-task corpus that exposes the model to diverse temporal structures and semantics, and build upon the Group Relative Policy Optimization (GRPO) algorithm to achieve stable and effective cross-task optimization. Specifically, we categorize temporal tasks into three correspondence types between predicted intervals and ground-truth instances, and design tailored localization rewards for each, enabling TempR1 to capture fine-grained temporal dependencies and adapt to different temporal patterns. Extensive experiments demonstrate that TempR1 attains state-of-the-art performance across multiple benchmarks. Moreover, its joint optimization over complementary tasks yields a strong synergistic effect, enhancing both generalization and single-task performance, establishing a scalable and principled paradigm for temporal reasoning in MLLMs.

