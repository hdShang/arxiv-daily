---
layout: default
title: Curriculum Guided Massive Multi Agent System Solving For Robust Long Horizon Tasks
---

# Curriculum Guided Massive Multi Agent System Solving For Robust Long Horizon Tasks

**arXiv**: [2512.08545v1](https://arxiv.org/abs/2512.08545) | [PDF](https://arxiv.org/pdf/2512.08545.pdf)

**作者**: Indrajit Kar, Kalathur Chenchu Kishore Kumar

---

## 💡 一句话要点

**提出基于空间课程的分层多智能体系统，以解决长时程推理任务中的计算成本与稳定性问题。**

**关键词**: `分层多智能体系统` `空间课程学习` `长时程推理` `负对数似然置信度` `Thompson Sampling` `分布式协作`

## 📋 核心要点

1. 核心问题：大语言模型与多智能体系统在长时程推理任务中面临计算成本高和稳定性不足的挑战。
2. 方法要点：采用64*64网格的轻量级智能体分层架构，结合空间课程和负对数似然置信度度量，通过Thompson Sampling自适应管理训练区域。
3. 实验或效果：在空间化汉诺塔基准测试中，系统表现出稳定性提升、预言机使用减少和分布式协作增强的长程推理能力。

## 📄 摘要（原文）

> Large Language Models and multi-agent systems have shown promise in decomposing complex tasks, yet they struggle with long-horizon reasoning tasks and escalating computation cost. This work introduces a hierarchical multi-agent architecture that distributes reasoning across a 64*64 grid of lightweight agents, supported by a selective oracle. A spatial curriculum progressively expands the operational region of the grid, ensuring that agents master easier central tasks before tackling harder peripheral ones. To improve reliability, the system integrates Negative Log-Likelihood as a measure of confidence, allowing the curriculum to prioritize regions where agents are both accurate and well calibrated. A Thompson Sampling curriculum manager adaptively chooses training zones based on competence and NLL-driven reward signals. We evaluate the approach on a spatially grounded Tower of Hanoi benchmark, which mirrors the long-horizon structure of many robotic manipulation and planning tasks. Results demonstrate improved stability, reduced oracle usage, and stronger long-range reasoning from distributed agent cooperation.

