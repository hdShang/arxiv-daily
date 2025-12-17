---
layout: default
title: Fast Gaussian Process Approximations for Autocorrelated Data
---

# Fast Gaussian Process Approximations for Autocorrelated Data

**arXiv**: [2512.02925v1](https://arxiv.org/abs/2512.02925) | [PDF](https://arxiv.org/pdf/2512.02925.pdf)

**作者**: Ahmadreza Chokhachian, Matthias Katzfuss, Yu Ding

---

## 💡 一句话要点

**提出基于分块数据的快速高斯过程近似方法，以处理自相关数据并避免时间过拟合。**

**关键词**: `高斯过程回归` `自相关数据` `快速近似` `分块方法` `时间过拟合`

## 📋 核心要点

1. 核心问题：自相关数据导致标准高斯过程回归计算慢且易时间过拟合，需改进现有快速近似方法。
2. 方法要点：将自相关数据分块以去相关，使现有快速高斯过程近似适用于分块数据，加速计算。
3. 实验或效果：多数据集实验显示，方法显著加速自相关数据的高斯过程回归，且不损害预测性能。

## 📄 摘要（原文）

> This paper is concerned with the problem of how to speed up computation for Gaussian process models trained on autocorrelated data. The Gaussian process model is a powerful tool commonly used in nonlinear regression applications. Standard regression modeling assumes random samples and an independently, identically distributed noise. Various fast approximations that speed up Gaussian process regression work under this standard setting. But for autocorrelated data, failing to account for autocorrelation leads to a phenomenon known as temporal overfitting that deteriorates model performance on new test instances. To handle autocorrelated data, existing fast Gaussian process approximations have to be modified; one such approach is to segment the originally correlated data points into blocks in which the blocked data are de-correlated. This work explains how to make some of the existing Gaussian process approximations work with blocked data. Numerical experiments across diverse application datasets demonstrate that the proposed approaches can remarkably accelerate computation for Gaussian process regression on autocorrelated data without compromising model prediction performance.

