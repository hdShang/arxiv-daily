---
layout: default
title: Efficient Model-Based Reinforcement Learning for Robot Control via Online Learning
---

# Efficient Model-Based Reinforcement Learning for Robot Control via Online Learning

**arXiv**: [2510.18518v1](https://arxiv.org/abs/2510.18518) | [PDF](https://arxiv.org/pdf/2510.18518.pdf)

**作者**: Fang Nan, Hao Ma, Qinghua Guan, Josie Hughes, Michael Muehlebach, Marco Hutter

---

## 💡 一句话要点

**提出在线模型强化学习算法，用于机器人控制，提升样本效率与适应性。**

**关键词**: `模型强化学习` `机器人控制` `在线学习` `样本效率` `动态适应`

## 📋 核心要点

1. 核心问题：传统机器人控制依赖离线仿真，样本效率低且易受模拟偏差影响。
2. 方法要点：从实时交互数据构建动态模型，指导策略更新，减少样本需求。
3. 实验效果：在液压挖掘臂和软体机器人上验证，样本效率高，适应动态变化。

## 📄 摘要（原文）

> We present an online model-based reinforcement learning algorithm suitable
> for controlling complex robotic systems directly in the real world. Unlike
> prevailing sim-to-real pipelines that rely on extensive offline simulation and
> model-free policy optimization, our method builds a dynamics model from
> real-time interaction data and performs policy updates guided by the learned
> dynamics model. This efficient model-based reinforcement learning scheme
> significantly reduces the number of samples to train control policies, enabling
> direct training on real-world rollout data. This significantly reduces the
> influence of bias in the simulated data, and facilitates the search for
> high-performance control policies. We adopt online learning analysis to derive
> sublinear regret bounds under standard stochastic online optimization
> assumptions, providing formal guarantees on performance improvement as more
> interaction data are collected. Experimental evaluations were performed on a
> hydraulic excavator arm and a soft robot arm, where the algorithm demonstrates
> strong sample efficiency compared to model-free reinforcement learning methods,
> reaching comparable performance within hours. Robust adaptation to shifting
> dynamics was also observed when the payload condition was randomized. Our
> approach paves the way toward efficient and reliable on-robot learning for a
> broad class of challenging control tasks.

