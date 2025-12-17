---
layout: default
title: HEADER: Hierarchical Robot Exploration via Attention-Based Deep Reinforcement Learning with Expert-Guided Reward
---

# HEADER: Hierarchical Robot Exploration via Attention-Based Deep Reinforcement Learning with Expert-Guided Reward

**arXiv**: [2510.15679v1](https://arxiv.org/abs/2510.15679) | [PDF](https://arxiv.org/pdf/2510.15679.pdf)

**作者**: Yuhong Cao, Yizhuo Wang, Jingsong Liang, Shuhao Liao, Yifeng Zhang, Peizhuo Li, Guillaume Sartoretti

---

## 💡 一句话要点

**提出HEADER方法以解决大规模环境中机器人自主探索效率问题**

**关键词**: `机器人探索` `分层强化学习` `注意力机制` `全局图构建` `探索效率优化`

## 📋 核心要点

1. 核心问题：大规模环境下的机器人自主探索效率与可扩展性不足
2. 方法要点：使用基于注意力的分层强化学习，结合社区算法构建全局图
3. 实验或效果：在模拟和真实场景中，探索效率提升达20%，优于现有方法

## 📄 摘要（原文）

> This work pushes the boundaries of learning-based methods in autonomous robot
> exploration in terms of environmental scale and exploration efficiency. We
> present HEADER, an attention-based reinforcement learning approach with
> hierarchical graphs for efficient exploration in large-scale environments.
> HEADER follows existing conventional methods to construct hierarchical
> representations for the robot belief/map, but further designs a novel
> community-based algorithm to construct and update a global graph, which remains
> fully incremental, shape-adaptive, and operates with linear complexity.
> Building upon attention-based networks, our planner finely reasons about the
> nearby belief within the local range while coarsely leveraging distant
> information at the global scale, enabling next-best-viewpoint decisions that
> consider multi-scale spatial dependencies. Beyond novel map representation, we
> introduce a parameter-free privileged reward that significantly improves model
> performance and produces near-optimal exploration behaviors, by avoiding
> training objective bias caused by handcrafted reward shaping. In simulated
> challenging, large-scale exploration scenarios, HEADER demonstrates better
> scalability than most existing learning and non-learning methods, while
> achieving a significant improvement in exploration efficiency (up to 20%) over
> state-of-the-art baselines. We also deploy HEADER on hardware and validate it
> in complex, large-scale real-life scenarios, including a 300m*230m campus
> environment.

