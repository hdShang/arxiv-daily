---
layout: default
title: Platform-Agnostic Reinforcement Learning Framework for Safe Exploration of Cluttered Environments with Graph Attention
---

# Platform-Agnostic Reinforcement Learning Framework for Safe Exploration of Cluttered Environments with Graph Attention

**arXiv**: [2511.15358v1](https://arxiv.org/abs/2511.15358) | [PDF](https://arxiv.org/pdf/2511.15358.pdf)

**作者**: Gabriele Calzolari, Vidya Sumathy, Christoforos Kanellakis, George Nikolakopoulos

---

## 💡 一句话要点

**提出平台无关强化学习框架，结合图注意力和安全过滤器，实现杂乱环境中的安全高效探索。**

**关键词**: `强化学习` `图神经网络` `安全探索` `平台无关框架` `PPO算法` `潜在场奖励`

## 📋 核心要点

1. 核心问题：自主探索障碍密集空间需平衡效率与安全，避免碰撞。
2. 方法要点：使用PPO算法训练图神经网络策略，集成安全过滤器修正不可行动作。
3. 实验或效果：在仿真和实验室环境中验证，实现高效安全探索。

## 📄 摘要（原文）

> Autonomous exploration of obstacle-rich spaces requires strategies that ensure efficiency while guaranteeing safety against collisions with obstacles. This paper investigates a novel platform-agnostic reinforcement learning framework that integrates a graph neural network-based policy for next-waypoint selection, with a safety filter ensuring safe mobility. Specifically, the neural network is trained using reinforcement learning through the Proximal Policy Optimization (PPO) algorithm to maximize exploration efficiency while minimizing safety filter interventions. Henceforth, when the policy proposes an infeasible action, the safety filter overrides it with the closest feasible alternative, ensuring consistent system behavior. In addition, this paper introduces a reward function shaped by a potential field that accounts for both the agent's proximity to unexplored regions and the expected information gain from reaching them. The proposed framework combines the adaptability of reinforcement learning-based exploration policies with the reliability provided by explicit safety mechanisms. This feature plays a key role in enabling the deployment of learning-based policies on robotic platforms operating in real-world environments. Extensive evaluations in both simulations and experiments performed in a lab environment demonstrate that the approach achieves efficient and safe exploration in cluttered spaces.

