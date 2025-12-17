---
layout: default
title: SINRL: Socially Integrated Navigation with Reinforcement Learning using Spiking Neural Networks
---

# SINRL: Socially Integrated Navigation with Reinforcement Learning using Spiking Neural Networks

**arXiv**: [2512.07266v1](https://arxiv.org/abs/2512.07266) | [PDF](https://arxiv.org/pdf/2512.07266.pdf)

**作者**: Florian Tretter, Daniel Flögel, Alexandru Vasilache, Max Grobbel, Jürgen Becker, Sören Hohmann

---

## 💡 一句话要点

**提出混合社会集成DRL方法，结合SNN与ANN，以解决机器人导航中训练不稳定和能耗高的问题。**

**关键词**: `社会导航` `深度强化学习` `脉冲神经网络` `神经形态计算` `能耗优化` `人机交互`

## 📋 核心要点

1. 核心问题：自主移动机器人在人类环境中需类人决策和节能计算，但神经形态方法在DRL导航中因训练不稳定应用少。
2. 方法要点：采用混合DRL演员-评论家方法，演员用SNN，评论家用ANN，并集成神经形态特征提取器捕捉时空动态。
3. 实验或效果：提升社会导航性能，估计能耗降低约1.69个数量级。

## 📄 摘要（原文）

> Integrating autonomous mobile robots into human environments requires human-like decision-making and energy-efficient, event-based computation. Despite progress, neuromorphic methods are rarely applied to Deep Reinforcement Learning (DRL) navigation approaches due to unstable training. We address this gap with a hybrid socially integrated DRL actor-critic approach that combines Spiking Neural Networks (SNNs) in the actor with Artificial Neural Networks (ANNs) in the critic and a neuromorphic feature extractor to capture temporal crowd dynamics and human-robot interactions. Our approach enhances social navigation performance and reduces estimated energy consumption by approximately 1.69 orders of magnitude.

