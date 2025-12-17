---
layout: default
title: Model-Based Learning of Whittle indices
---

# Model-Based Learning of Whittle indices

**arXiv**: [2511.20397v1](https://arxiv.org/abs/2511.20397) | [PDF](https://arxiv.org/pdf/2511.20397.pdf)

**作者**: Joël Charles-Rebuffé, Nicolas Gast, Bruno Gaujal

---

## 💡 一句话要点

**提出BLINQ算法以学习可索引通信单链MDP的Whittle指数**

**关键词**: `Whittle指数学习` `模型强化学习` `马尔可夫决策过程` `样本效率优化` `计算复杂度分析`

## 📋 核心要点

1. 核心问题：学习可索引通信单链马尔可夫决策过程的Whittle指数
2. 方法要点：基于经验MDP估计，扩展现有算法计算Whittle指数
3. 实验或效果：样本效率优于Q学习，计算成本更低

## 📄 摘要（原文）

> We present BLINQ, a new model-based algorithm that learns the Whittle indices of an indexable, communicating and unichain Markov Decision Process (MDP). Our approach relies on building an empirical estimate of the MDP and then computing its Whittle indices using an extended version of a state-of-the-art existing algorithm. We provide a proof of convergence to the Whittle indices we want to learn as well as a bound on the time needed to learn them with arbitrary precision. Moreover, we investigate its computational complexity. Our numerical experiments suggest that BLINQ significantly outperforms existing Q-learning approaches in terms of the number of samples needed to get an accurate approximation. In addition, it has a total computational cost even lower than Q-learning for any reasonably high number of samples. These observations persist even when the Q-learning algorithms are speeded up using pre-trained neural networks to predict Q-values.

