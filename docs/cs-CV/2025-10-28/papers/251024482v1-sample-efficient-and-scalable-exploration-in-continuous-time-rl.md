---
layout: default
title: Sample-efficient and Scalable Exploration in Continuous-Time RL
---

# Sample-efficient and Scalable Exploration in Continuous-Time RL

**arXiv**: [2510.24482v1](https://arxiv.org/abs/2510.24482) | [PDF](https://arxiv.org/pdf/2510.24482.pdf)

**作者**: Klemens Iten, Lenart Treven, Bhavya Sukhija, Florian Dörfler, Andreas Krause

---

## 💡 一句话要点

**提出COMBRL算法以解决连续时间强化学习的样本效率与可扩展性问题**

**关键词**: `连续时间强化学习` `概率模型` `样本效率` `可扩展性` `模型不确定性` `无监督强化学习`

## 📋 核心要点

1. 核心问题：强化学习算法通常针对离散时间设计，而真实控制系统多为连续时间
2. 方法要点：利用概率模型学习非线性ODE动态，贪婪最大化奖励与模型不确定性加权和
3. 实验或效果：在标准和无监督RL设置中，COMBRL样本效率更高、可扩展性更强，优于基线方法

## 📄 摘要（原文）

> Reinforcement learning algorithms are typically designed for discrete-time
> dynamics, even though the underlying real-world control systems are often
> continuous in time. In this paper, we study the problem of continuous-time
> reinforcement learning, where the unknown system dynamics are represented using
> nonlinear ordinary differential equations (ODEs). We leverage probabilistic
> models, such as Gaussian processes and Bayesian neural networks, to learn an
> uncertainty-aware model of the underlying ODE. Our algorithm, COMBRL, greedily
> maximizes a weighted sum of the extrinsic reward and model epistemic
> uncertainty. This yields a scalable and sample-efficient approach to
> continuous-time model-based RL. We show that COMBRL achieves sublinear regret
> in the reward-driven setting, and in the unsupervised RL setting (i.e., without
> extrinsic rewards), we provide a sample complexity bound. In our experiments,
> we evaluate COMBRL in both standard and unsupervised RL settings and
> demonstrate that it scales better, is more sample-efficient than prior methods,
> and outperforms baselines across several deep RL tasks.

