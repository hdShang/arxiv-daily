---
layout: default
title: Worst-case generation via minimax optimization in Wasserstein space
---

# Worst-case generation via minimax optimization in Wasserstein space

**arXiv**: [2512.08176v1](https://arxiv.org/abs/2512.08176) | [PDF](https://arxiv.org/pdf/2512.08176.pdf)

**作者**: Xiuyuan Cheng, Yao Xie, Linglingzhi Zhu, Yunqin Zhu

---

## 💡 一句话要点

**提出基于Wasserstein空间极小极大优化的最坏情况生成框架，用于评估系统在分布偏移下的鲁棒性。**

**关键词**: `最坏情况生成` `Wasserstein空间` `极小极大优化` `分布鲁棒优化` `梯度下降上升` `神经网络参数化`

## 📋 核心要点

1. 核心问题：传统离散分布鲁棒优化方法存在可扩展性差、泛化有限和最坏情况推断成本高的问题。
2. 方法要点：利用Brenier定理将最坏分布表征为连续参考测度的推前映射，实现连续且表达性强的风险诱导生成。
3. 实验或效果：通过合成和图像数据实验验证了方法作为风险诱导最坏情况生成器的效率。

## 📄 摘要（原文）

> Worst-case generation plays a critical role in evaluating robustness and stress-testing systems under distribution shifts, in applications ranging from machine learning models to power grids and medical prediction systems. We develop a generative modeling framework for worst-case generation for a pre-specified risk, based on min-max optimization over continuous probability distributions, namely the Wasserstein space. Unlike traditional discrete distributionally robust optimization approaches, which often suffer from scalability issues, limited generalization, and costly worst-case inference, our framework exploits the Brenier theorem to characterize the least favorable (worst-case) distribution as the pushforward of a transport map from a continuous reference measure, enabling a continuous and expressive notion of risk-induced generation beyond classical discrete DRO formulations. Based on the min-max formulation, we propose a Gradient Descent Ascent (GDA)-type scheme that updates the decision model and the transport map in a single loop, establishing global convergence guarantees under mild regularity assumptions and possibly without convexity-concavity. We also propose to parameterize the transport map using a neural network that can be trained simultaneously with the GDA iterations by matching the transported training samples, thereby achieving a simulation-free approach. The efficiency of the proposed method as a risk-induced worst-case generator is validated by numerical experiments on synthetic and image data.

