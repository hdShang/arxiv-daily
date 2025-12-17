---
layout: default
title: Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms
---

# Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms

**arXiv**: [2512.02810v1](https://arxiv.org/abs/2512.02810) | [PDF](https://arxiv.org/pdf/2512.02810.pdf)

**作者**: Shyam prasad reddy Kaitha, Hongrui Yu

---

## 💡 一句话要点

**提出基于LangGraph的LLM框架LTAA，用于建筑机器人任务分配，通过多阶段验证提升效率。**

**关键词**: `建筑机器人任务分配` `LLM框架` `多阶段验证` `动态提示` `基准测试` `LangGraph`

## 📋 核心要点

1. 核心问题：传统优化方法在建筑自动化中缺乏LLM的严格验证与基准测试。
2. 方法要点：LTAA集成阶段自适应策略、多阶段验证和动态提示，减少令牌使用94.6%。
3. 实验或效果：在重型Excel设置中，LTAA任务完成率达77%，优于动态规划和强化学习基线。

## 📄 摘要（原文）

> Multi-robot task allocation in construction automation has traditionally relied on optimization methods such as Dynamic Programming and Reinforcement Learning. This research introduces the LangGraph-based Task Allocation Agent (LTAA), an LLM-driven framework that integrates phase-adaptive allocation strategies, multi-stage validation with hierarchical retries, and dynamic prompting for efficient robot coordination. Although recent LLM approaches show potential for construction robotics, they largely lack rigorous validation and benchmarking against established algorithms. This paper presents the first systematic comparison of LLM-based task allocation with traditional methods in construction scenarios.The study validates LLM feasibility through SMART-LLM replication and addresses implementation challenges using a Self-Corrective Agent Architecture. LTAA leverages natural-language reasoning combined with structured validation mechanisms, achieving major computational gains reducing token usage by 94.6% and allocation time by 86% through dynamic prompting. The framework adjusts its strategy across phases: emphasizing execution feasibility early and workload balance in later allocations.The authors evaluate LTAA against Dynamic Programming, Q-learning, and Deep Q-Network (DQN) baselines using construction operations from the TEACh human-robot collaboration dataset. In the Heavy Excels setting, where robots have strong task specializations, LTAA achieves 77% task completion with superior workload balance, outperforming all traditional methods. These findings show that LLM-based reasoning with structured validation can match established optimization algorithms while offering additional advantages such as interpretability, adaptability, and the ability to update task logic without retraining.

