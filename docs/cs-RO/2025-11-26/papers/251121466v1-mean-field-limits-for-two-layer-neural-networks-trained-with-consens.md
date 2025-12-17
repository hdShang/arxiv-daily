---
layout: default
title: Mean-Field Limits for Two-Layer Neural Networks Trained with Consensus-Based Optimization
---

# Mean-Field Limits for Two-Layer Neural Networks Trained with Consensus-Based Optimization

**arXiv**: [2511.21466v1](https://arxiv.org/abs/2511.21466) | [PDF](https://arxiv.org/pdf/2511.21466.pdf)

**作者**: William De Deyn, Michael Herty, Giovanni Samaey

---

## 💡 一句话要点

**提出结合CBO与Adam的混合方法，加速双层神经网络训练收敛。**

**关键词**: `双层神经网络` `共识优化` `均值场极限` `混合训练` `多任务学习`

## 📋 核心要点

1. 研究双层神经网络训练，使用基于粒子的共识优化方法。
2. 在均值场极限下，将CBO与神经网络耦合，方差单调递减。
3. 实验显示混合方法比纯CBO收敛更快，并减少内存开销。

## 📄 摘要（原文）

> We study two-layer neural networks and train these with a particle-based method called consensus-based optimization (CBO). We compare the performance of CBO against Adam on two test cases and demonstrate how a hybrid approach, combining CBO with Adam, provides faster convergence than CBO. In the context of multi-task learning, we recast CBO into a formulation that offers less memory overhead. The CBO method allows for a mean-field limit formulation, which we couple with the mean-field limit of the neural network. To this end, we first reformulate CBO within the optimal transport framework. Finally, in the limit of infinitely many particles, we define the corresponding dynamics on the Wasserstein-over-Wasserstein space and show that the variance decreases monotonically.

