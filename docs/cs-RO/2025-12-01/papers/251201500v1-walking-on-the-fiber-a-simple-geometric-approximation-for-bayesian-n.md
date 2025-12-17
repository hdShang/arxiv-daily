---
layout: default
title: Walking on the Fiber: A Simple Geometric Approximation for Bayesian Neural Networks
---

# Walking on the Fiber: A Simple Geometric Approximation for Bayesian Neural Networks

**arXiv**: [2512.01500v1](https://arxiv.org/abs/2512.01500) | [PDF](https://arxiv.org/pdf/2512.01500.pdf)

**作者**: Alfredo Reichlin, Miguel Vasco, Danica Kragic

---

## 💡 一句话要点

**提出基于参数空间变形的贝叶斯神经网络后验采样方法，以提升可扩展性和准确性。**

**关键词**: `贝叶斯神经网络` `后验采样` `参数空间变形` `不确定性量化` `深度学习推断`

## 📋 核心要点

1. 核心问题：贝叶斯神经网络后验推断计算困难，传统近似方法在深度网络中可扩展性和准确性不足。
2. 方法要点：利用损失最小值的低维结构，设计参数空间变形模型，实现快速后验采样，避免迭代方法。
3. 实验或效果：实证显示该方法在可扩展性上优于近期改进技术，提供竞争性后验近似。

## 📄 摘要（原文）

> Bayesian Neural Networks provide a principled framework for uncertainty quantification by modeling the posterior distribution of network parameters. However, exact posterior inference is computationally intractable, and widely used approximations like the Laplace method struggle with scalability and posterior accuracy in modern deep networks. In this work, we revisit sampling techniques for posterior exploration, proposing a simple variation tailored to efficiently sample from the posterior in over-parameterized networks by leveraging the low-dimensional structure of loss minima. Building on this, we introduce a model that learns a deformation of the parameter space, enabling rapid posterior sampling without requiring iterative methods. Empirical results demonstrate that our approach achieves competitive posterior approximations with improved scalability compared to recent refinement techniques. These contributions provide a practical alternative for Bayesian inference in deep learning.

