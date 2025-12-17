---
layout: default
title: Transferable Deep Reinforcement Learning for Cross-Domain Navigation: from Farmland to the Moon
---

# Transferable Deep Reinforcement Learning for Cross-Domain Navigation: from Farmland to the Moon

**arXiv**: [2510.23329v1](https://arxiv.org/abs/2510.23329) | [PDF](https://arxiv.org/pdf/2510.23329.pdf)

**作者**: Shreya Santra, Thomas Robbins, Kazuya Yoshida

---

## 💡 一句话要点

**提出可迁移深度强化学习策略，实现从农田到月球的跨域自主导航。**

**关键词**: `深度强化学习` `跨域导航` `策略迁移` `自主机器人` `模拟验证`

## 📋 核心要点

1. 核心问题：传统导航方法需环境特定调优，难以适应新领域。
2. 方法要点：使用PPO算法训练DRL策略，在农田模拟中学习导航与避障。
3. 实验效果：零样本迁移至月球模拟，成功率近50%，无需额外训练。

## 📄 摘要（原文）

> Autonomous navigation in unstructured environments is essential for field and
> planetary robotics, where robots must efficiently reach goals while avoiding
> obstacles under uncertain conditions. Conventional algorithmic approaches often
> require extensive environment-specific tuning, limiting scalability to new
> domains. Deep Reinforcement Learning (DRL) provides a data-driven alternative,
> allowing robots to acquire navigation strategies through direct interactions
> with their environment. This work investigates the feasibility of DRL policy
> generalization across visually and topographically distinct simulated domains,
> where policies are trained in terrestrial settings and validated in a zero-shot
> manner in extraterrestrial environments. A 3D simulation of an agricultural
> rover is developed and trained using Proximal Policy Optimization (PPO) to
> achieve goal-directed navigation and obstacle avoidance in farmland settings.
> The learned policy is then evaluated in a lunar-like simulated environment to
> assess transfer performance. The results indicate that policies trained under
> terrestrial conditions retain a high level of effectiveness, achieving close to
> 50\% success in lunar simulations without the need for additional training and
> fine-tuning. This underscores the potential of cross-domain DRL-based policy
> transfer as a promising approach to developing adaptable and efficient
> autonomous navigation for future planetary exploration missions, with the added
> benefit of minimizing retraining costs.

