---
layout: default
title: Independent policy gradient-based reinforcement learning for economic and reliable energy management of multi-microgrid systems
---

# Independent policy gradient-based reinforcement learning for economic and reliable energy management of multi-microgrid systems

**arXiv**: [2511.20977v1](https://arxiv.org/abs/2511.20977) | [PDF](https://arxiv.org/pdf/2511.20977.pdf)

**作者**: Junkai Hu, Li Xia

---

## 💡 一句话要点

**提出独立策略梯度强化学习以解决多微网系统经济可靠能源管理问题**

**关键词**: `多微网系统` `能源管理` `强化学习` `策略梯度` `均值-方差优化` `分布式算法`

## 📋 核心要点

1. 核心问题：多微网系统在分布式方案下经济与可靠能源管理，需优化长期性能
2. 方法要点：基于独立策略梯度的分布式算法，处理均值-方差团队随机博弈
3. 实验或效果：数值实验验证方法有效性，平衡经济性与可靠性

## 📄 摘要（原文）

> Efficiency and reliability are both crucial for energy management, especially in multi-microgrid systems (MMSs) integrating intermittent and distributed renewable energy sources. This study investigates an economic and reliable energy management problem in MMSs under a distributed scheme, where each microgrid independently updates its energy management policy in a decentralized manner to optimize the long-term system performance collaboratively. We introduce the mean and variance of the exchange power between the MMS and the main grid as indicators for the economic performance and reliability of the system. Accordingly, we formulate the energy management problem as a mean-variance team stochastic game (MV-TSG), where conventional methods based on the maximization of expected cumulative rewards are unsuitable for variance metrics. To solve MV-TSGs, we propose a fully distributed independent policy gradient algorithm, with rigorous convergence analysis, for scenarios with known model parameters. For large-scale scenarios with unknown model parameters, we further develop a deep reinforcement learning algorithm based on independent policy gradients, enabling data-driven policy optimization. Numerical experiments in two scenarios validate the effectiveness of the proposed methods. Our approaches fully leverage the distributed computational capabilities of MMSs and achieve a well-balanced trade-off between economic performance and operational reliability.

