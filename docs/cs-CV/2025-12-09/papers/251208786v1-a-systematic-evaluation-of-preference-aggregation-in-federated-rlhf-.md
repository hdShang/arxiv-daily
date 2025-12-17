---
layout: default
title: A Systematic Evaluation of Preference Aggregation in Federated RLHF for Pluralistic Alignment of LLMs
---

# A Systematic Evaluation of Preference Aggregation in Federated RLHF for Pluralistic Alignment of LLMs

**arXiv**: [2512.08786v1](https://arxiv.org/abs/2512.08786) | [PDF](https://arxiv.org/pdf/2512.08786.pdf)

**作者**: Mahmoud Srewa, Tianyu Zhao, Salma Elmalaki

---

## 💡 一句话要点

**提出自适应聚合策略以解决联邦RLHF中LLM与多元人类偏好对齐的公平性问题**

**关键词**: `联邦学习` `强化学习人类反馈` `偏好聚合` `公平性评估` `大语言模型对齐`

## 📋 核心要点

1. 核心问题：联邦学习中标准方法难以充分代表多元人类偏好，导致对齐质量与公平性失衡
2. 方法要点：评估标准聚合技术并引入自适应方案，基于历史性能动态调整偏好权重
3. 实验或效果：在Q/A任务中，自适应方法在保持对齐得分的同时显著提升公平性

## 📄 摘要（原文）

> This paper addresses the challenge of aligning large language models (LLMs) with diverse human preferences within federated learning (FL) environments, where standard methods often fail to adequately represent diverse viewpoints. We introduce a comprehensive evaluation framework that systematically assesses the trade-off between alignment quality and fairness when using different aggregation strategies for human preferences. In our federated setting, each group locally evaluates rollouts and produces reward signals, and the server aggregates these group-level rewards without accessing any raw data. Specifically, we evaluate standard reward aggregation techniques (min, max, and average) and introduce a novel adaptive scheme that dynamically adjusts preference weights based on a group's historical alignment performance. Our experiments on question-answering (Q/A) tasks using a PPO-based RLHF pipeline demonstrate that our adaptive approach consistently achieves superior fairness while maintaining competitive alignment scores. This work offers a robust methodology for evaluating LLM behavior across diverse populations and provides a practical solution for developing truly pluralistic and fairly aligned models.

