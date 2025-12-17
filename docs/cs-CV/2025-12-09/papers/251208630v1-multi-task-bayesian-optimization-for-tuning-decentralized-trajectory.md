---
layout: default
title: Multi-Task Bayesian Optimization for Tuning Decentralized Trajectory Generation in Multi-UAV Systems
---

# Multi-Task Bayesian Optimization for Tuning Decentralized Trajectory Generation in Multi-UAV Systems

**arXiv**: [2512.08630v1](https://arxiv.org/abs/2512.08630) | [PDF](https://arxiv.org/pdf/2512.08630.pdf)

**作者**: Marta Manzoni, Alessandro Nazzari, Roberto Rubinacci, Marco Lovera

---

## 💡 一句话要点

**提出多任务贝叶斯优化以调优多无人机系统中的分散轨迹生成算法**

**关键词**: `多任务贝叶斯优化` `分散轨迹生成` `多无人机系统` `高斯过程` `参数调优` `仿真评估`

## 📋 核心要点

1. 核心问题：多无人机系统中分散轨迹生成算法的参数调优，涉及不同无人机交互场景。
2. 方法要点：采用多任务高斯过程建模任务间关系，实现优化过程中的信息共享。
3. 实验或效果：通过仿真比较，单任务优化随群规模增大任务时间缩短，但优化时间显著高于平均任务方法。

## 📄 摘要（原文）

> This paper investigates the use of Multi-Task Bayesian Optimization for tuning decentralized trajectory generation algorithms in multi-drone systems. We treat each task as a trajectory generation scenario defined by a specific number of drone-to-drone interactions. To model relationships across scenarios, we employ Multi-Task Gaussian Processes, which capture shared structure across tasks and enable efficient information transfer during optimization. We compare two strategies: optimizing the average mission time across all tasks and optimizing each task individually. Through a comprehensive simulation campaign, we show that single-task optimization leads to progressively shorter mission times as swarm size grows, but requires significantly more optimization time than the average-task approach.

