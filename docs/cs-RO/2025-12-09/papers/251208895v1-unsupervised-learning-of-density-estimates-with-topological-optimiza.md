---
layout: default
title: Unsupervised Learning of Density Estimates with Topological Optimization
---

# Unsupervised Learning of Density Estimates with Topological Optimization

**arXiv**: [2512.08895v1](https://arxiv.org/abs/2512.08895) | [PDF](https://arxiv.org/pdf/2512.08895.pdf)

**作者**: Suina Tanweer, Firas A. Khasawneh

---

## 💡 一句话要点

**提出基于拓扑优化的无监督核密度估计方法，用于自动选择最优带宽**

**关键词**: `无监督学习` `核密度估计` `拓扑数据优化` `带宽选择` `高维数据分析`

## 📋 核心要点

1. 核心问题：核密度估计中带宽超参数的无监督选择，影响拓扑特征的平滑度
2. 方法要点：使用拓扑数据分析的损失函数，自动化优化带宽，无需人工调参
3. 实验或效果：在不同维度上基准测试，展示其优于经典技术的潜力

## 📄 摘要（原文）

> Kernel density estimation is a key component of a wide variety of algorithms in machine learning, Bayesian inference, stochastic dynamics and signal processing. However, the unsupervised density estimation technique requires tuning a crucial hyperparameter: the kernel bandwidth. The choice of bandwidth is critical as it controls the bias-variance trade-off by over- or under-smoothing the topological features. Topological data analysis provides methods to mathematically quantify topological characteristics, such as connected components, loops, voids et cetera, even in high dimensions where visualization of density estimates is impossible. In this paper, we propose an unsupervised learning approach using a topology-based loss function for the automated and unsupervised selection of the optimal bandwidth and benchmark it against classical techniques -- demonstrating its potential across different dimensions.

