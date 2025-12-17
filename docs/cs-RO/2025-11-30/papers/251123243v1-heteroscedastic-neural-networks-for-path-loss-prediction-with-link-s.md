---
layout: default
title: Heteroscedastic Neural Networks for Path Loss Prediction with Link-Specific Uncertainty
---

# Heteroscedastic Neural Networks for Path Loss Prediction with Link-Specific Uncertainty

**arXiv**: [2511.23243v1](https://arxiv.org/abs/2511.23243) | [PDF](https://arxiv.org/pdf/2511.23243.pdf)

**作者**: Jonathan Ethier

---

## 💡 一句话要点

**提出异方差神经网络，通过联合预测均值和链路特定方差，解决路径损耗预测中不确定性估计不足的问题。**

**关键词**: `路径损耗预测` `异方差神经网络` `不确定性估计` `RF规划` `链路特定方差` `模型校准`

## 📋 核心要点

1. 传统和现代机器学习路径损耗模型通常假设恒定预测方差，导致不确定性估计不准确。
2. 设计神经网络，通过最小化高斯负对数似然，联合预测均值和链路特定方差，实现异方差不确定性估计。
3. 在大型公共RF驱动测试数据集上，共享参数架构表现最佳，RMSE为7.4 dB，95%预测区间覆盖率达95.1%。

## 📄 摘要（原文）

> Traditional and modern machine learning-based path loss models typically assume a constant prediction variance. We propose a neural network that jointly predicts the mean and link-specific variance by minimizing a Gaussian negative log-likelihood, enabling heteroscedastic uncertainty estimates. We compare shared, partially shared, and independent-parameter architectures using accuracy, calibration, and sharpness metrics on blind test sets from large public RF drive-test datasets. The shared-parameter architecture performs best, achieving an RMSE of 7.4 dB, 95.1 percent coverage for 95 percent prediction intervals, and a mean interval width of 29.6 dB. These uncertainty estimates further support link-specific coverage margins, improve RF planning and interference analyses, and provide effective self-diagnostics of model weaknesses.

