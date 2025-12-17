---
layout: default
title: Safe and Optimal Learning from Preferences via Weighted Temporal Logic with Applications in Robotics and Formula 1
---

# Safe and Optimal Learning from Preferences via Weighted Temporal Logic with Applications in Robotics and Formula 1

**arXiv**: [2511.08502v1](https://arxiv.org/abs/2511.08502) | [PDF](https://arxiv.org/pdf/2511.08502.pdf)

**作者**: Ruya Karagulle, Cristian-Ioan Vasile, Necmiye Ozay

---

## 💡 一句话要点

**提出基于加权信号时序逻辑的方法，以安全学习偏好并应用于机器人和F1赛车**

**关键词**: `加权信号时序逻辑` `偏好学习` `安全保证` `混合整数线性规划` `机器人导航` `F1赛车数据`

## 📋 核心要点

1. 现有方法在安全关键领域学习人类偏好时，常无法保证安全性。
2. 引入结构剪枝和对数变换，将问题转化为混合整数线性规划，确保安全。
3. 在机器人导航和F1数据实验中，有效捕捉复杂偏好和任务目标。

## 📄 摘要（原文）

> Autonomous systems increasingly rely on human feedback to align their behavior, expressed as pairwise comparisons, rankings, or demonstrations. While existing methods can adapt behaviors, they often fail to guarantee safety in safety-critical domains. We propose a safety-guaranteed, optimal, and efficient approach to solve the learning problem from preferences, rankings, or demonstrations using Weighted Signal Temporal Logic (WSTL). WSTL learning problems, when implemented naively, lead to multi-linear constraints in the weights to be learned. By introducing structural pruning and log-transform procedures, we reduce the problem size and recast the problem as a Mixed-Integer Linear Program while preserving safety guarantees. Experiments on robotic navigation and real-world Formula 1 data demonstrate that the method effectively captures nuanced preferences and models complex task objectives.

