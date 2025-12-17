---
layout: default
title: Autonomous Vehicle Path Planning by Searching With Differentiable Simulation
---

# Autonomous Vehicle Path Planning by Searching With Differentiable Simulation

**arXiv**: [2511.11043v1](https://arxiv.org/abs/2511.11043) | [PDF](https://arxiv.org/pdf/2511.11043.pdf)

**作者**: Asen Nachkov, Jan-Nico Zaech, Danda Pani Paudel, Xi Wang, Luc Van Gool

---

## 💡 一句话要点

**提出可微分模拟搜索框架以提升自动驾驶路径规划精度**

**关键词**: `自动驾驶路径规划` `可微分模拟` `梯度优化` `动作序列搜索` `状态预测`

## 📋 核心要点

1. 核心问题：自动驾驶中需安全规划动作，避免碰撞，但学习策略、状态预测和评估器具挑战。
2. 方法要点：利用可微分模拟器Waymax作为状态预测器和评估器，通过梯度下降优化动作序列。
3. 实验或效果：相比序列预测、模仿学习等方法，显著提高跟踪和路径规划准确性。

## 📄 摘要（原文）

> Planning allows an agent to safely refine its actions before executing them in the real world. In autonomous driving, this is crucial to avoid collisions and navigate in complex, dense traffic scenarios. One way to plan is to search for the best action sequence. However, this is challenging when all necessary components - policy, next-state predictor, and critic - have to be learned. Here we propose Differentiable Simulation for Search (DSS), a framework that leverages the differentiable simulator Waymax as both a next state predictor and a critic. It relies on the simulator's hardcoded dynamics, making state predictions highly accurate, while utilizing the simulator's differentiability to effectively search across action sequences. Our DSS agent optimizes its actions using gradient descent over imagined future trajectories. We show experimentally that DSS - the combination of planning gradients and stochastic search - significantly improves tracking and path planning accuracy compared to sequence prediction, imitation learning, model-free RL, and other planning methods.

