---
layout: default
title: CoRL-MPPI: Enhancing MPPI With Learnable Behaviours For Efficient And Provably-Safe Multi-Robot Collision Avoidance
---

# CoRL-MPPI: Enhancing MPPI With Learnable Behaviours For Efficient And Provably-Safe Multi-Robot Collision Avoidance

**arXiv**: [2511.09331v1](https://arxiv.org/abs/2511.09331) | [PDF](https://arxiv.org/pdf/2511.09331.pdf)

**作者**: Stepan Dergachev, Artem Pshenitsyn, Aleksandr Panov, Alexey Skrynnik, Konstantin Yakovlev

---

## 💡 一句话要点

**提出CoRL-MPPI以增强MPPI，实现高效可证明安全的多机器人避碰**

**关键词**: `多机器人避碰` `模型预测路径积分` `合作强化学习` `可证明安全` `导航效率` `采样优化`

## 📋 核心要点

1. 核心问题：去中心化多机器人避碰依赖MPPI，但随机采样导致轨迹次优。
2. 方法要点：融合强化学习训练合作策略，嵌入MPPI引导采样分布。
3. 实验效果：在密集动态环境中，显著提升导航效率和安全性。

## 📄 摘要（原文）

> Decentralized collision avoidance remains a core challenge for scalable multi-robot systems. One of the promising approaches to tackle this problem is Model Predictive Path Integral (MPPI) -- a framework that is naturally suited to handle any robot motion model and provides strong theoretical guarantees. Still, in practice MPPI-based controller may provide suboptimal trajectories as its performance relies heavily on uninformed random sampling. In this work, we introduce CoRL-MPPI, a novel fusion of Cooperative Reinforcement Learning and MPPI to address this limitation. We train an action policy (approximated as deep neural network) in simulation that learns local cooperative collision avoidance behaviors. This learned policy is then embedded into the MPPI framework to guide its sampling distribution, biasing it towards more intelligent and cooperative actions. Notably, CoRL-MPPI preserves all the theoretical guarantees of regular MPPI. We evaluate our approach in dense, dynamic simulation environments against state-of-the-art baselines, including ORCA, BVC, and a multi-agent MPPI implementation. Our results demonstrate that CoRL-MPPI significantly improves navigation efficiency (measured by success rate and makespan) and safety, enabling agile and robust multi-robot navigation.

