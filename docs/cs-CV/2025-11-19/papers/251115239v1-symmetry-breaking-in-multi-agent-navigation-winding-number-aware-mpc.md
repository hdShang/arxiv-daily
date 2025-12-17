---
layout: default
title: Symmetry-Breaking in Multi-Agent Navigation: Winding Number-Aware MPC with a Learned Topological Strategy
---

# Symmetry-Breaking in Multi-Agent Navigation: Winding Number-Aware MPC with a Learned Topological Strategy

**arXiv**: [2511.15239v1](https://arxiv.org/abs/2511.15239) | [PDF](https://arxiv.org/pdf/2511.15239.pdf)

**作者**: Tomoki Nakao, Kazumi Kasaura, Tadashi Kozuno

---

## 💡 一句话要点

**提出基于缠绕数和强化学习的层次导航方法以解决多智能体对称死锁问题**

**关键词**: `多智能体导航` `对称性破缺` `缠绕数` `强化学习` `模型预测控制` `层次策略`

## 📋 核心要点

1. 核心问题：多智能体导航中对称性导致死锁，难以自主决策避让方式
2. 方法要点：层次策略结合学习型规划器和模型控制器，量化拓扑策略并动态优化权重
3. 实验或效果：仿真与真实实验显示在密集环境中优于基线，避免碰撞和死锁

## 📄 摘要（原文）

> We address the fundamental challenge of resolving symmetry-induced deadlocks in distributed multi-agent navigation by proposing a new hierarchical navigation method. When multiple agents interact, it is inherently difficult for them to autonomously break the symmetry of deciding how to pass each other. To tackle this problem, we introduce an approach that quantifies cooperative symmetry-breaking strategies using a topological invariant called the winding number, and learns the strategies themselves through reinforcement learning. Our method features a hierarchical policy consisting of a learning-based Planner, which plans topological cooperative strategies, and a model-based Controller, which executes them. Through reinforcement learning, the Planner learns to produce two types of parameters for the Controller: one is the topological cooperative strategy represented by winding numbers, and the other is a set of dynamic weights that determine which agent interaction to prioritize in dense scenarios where multiple agents cross simultaneously. The Controller then generates collision-free and efficient motions based on the strategy and weights provided by the Planner. This hierarchical structure combines the flexible decision-making ability of learning-based methods with the reliability of model-based approaches. Simulation and real-world robot experiments demonstrate that our method outperforms existing baselines, particularly in dense environments, by efficiently avoiding collisions and deadlocks while achieving superior navigation performance. The code for the experiments is available at https://github.com/omron-sinicx/WNumMPC.

