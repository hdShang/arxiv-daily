---
layout: default
title: Bayesian Physics-Informed Neural Networks for Inverse Problems (BPINN-IP): Application in Infrared Image Processing
---

# Bayesian Physics-Informed Neural Networks for Inverse Problems (BPINN-IP): Application in Infrared Image Processing

**arXiv**: [2512.02495v1](https://arxiv.org/abs/2512.02495) | [PDF](https://arxiv.org/pdf/2512.02495.pdf)

**作者**: Ali Mohammad-Djafari, Ning Chu, Li Wang

---

## 💡 一句话要点

**提出贝叶斯物理信息神经网络框架BPINN-IP，用于红外图像处理中的反问题求解**

**关键词**: `贝叶斯物理信息神经网络` `反问题求解` `红外图像处理` `不确定性量化` `去卷积` `超分辨率`

## 📋 核心要点

1. 核心问题：高维或复杂物理模型下的反问题求解，传统方法计算受限
2. 方法要点：扩展PINNs为贝叶斯框架，通过先验建模和后验推断整合物理约束与不确定性
3. 实验或效果：应用于红外图像去卷积和超分辨率，在模拟和真实工业数据上验证有效性

## 📄 摘要（原文）

> Inverse problems arise across scientific and engineering domains, where the goal is to infer hidden parameters or physical fields from indirect and noisy observations. Classical approaches, such as variational regularization and Bayesian inference, provide well established theoretical foundations for handling ill posedness. However, these methods often become computationally restrictive in high dimensional settings or when the forward model is governed by complex physics. Physics Informed Neural Networks (PINNs) have recently emerged as a promising framework for solving inverse problems by embedding physical laws directly into the training process of neural networks. In this paper, we introduce a new perspective on the Bayesian Physics Informed Neural Network (BPINN) framework, extending classical PINNs by explicitly incorporating training data generation, modeling and measurement uncertainties through Bayesian prior modeling and doing inference with the posterior laws. Also, as we focus on the inverse problems, we call this method BPINN-IP, and we show that the standard PINN formulation naturally appears as its special case corresponding to the Maximum A Posteriori (MAP) estimate. This unified formulation allows simultaneous exploitation of physical constraints, prior knowledge, and data-driven inference, while enabling uncertainty quantification through posterior distributions. To demonstrate the effectiveness of the proposed framework, we consider inverse problems arising in infrared image processing, including deconvolution and super-resolution, and present results on both simulated and real industrial data.

