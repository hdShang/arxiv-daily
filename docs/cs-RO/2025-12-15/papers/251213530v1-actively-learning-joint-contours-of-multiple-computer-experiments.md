---
layout: default
title: Actively Learning Joint Contours of Multiple Computer Experiments
---

# Actively Learning Joint Contours of Multiple Computer Experiments

**arXiv**: [2512.13530v1](https://arxiv.org/abs/2512.13530) | [PDF](https://arxiv.org/pdf/2512.13530.pdf)

**作者**: Shih-Ni Prim, Kevin R. Quinlan, Paul Hawkins, Jagadeesh Movva, Annie S. Booth

---

## 💡 一句话要点

**提出联合轮廓定位方案以解决多计算机实验联合轮廓识别问题**

**关键词**: `联合轮廓定位` `主动学习` `高斯过程` `计算机实验` `多响应优化`

## 📋 核心要点

1. 核心问题：识别多独立计算机实验同时返回预设值的输入配置，如飞行器零扭矩稳定条件
2. 方法要点：基于高斯过程代理模型，平衡探索响应曲面与利用轮廓交叉学习
3. 实验或效果：在飞行器扭矩实验中，显著优于单响应轮廓定位策略，高效定位联合轮廓

## 📄 摘要（原文）

> Contour location$\unicode{x2014}$the process of sequentially training a surrogate model to identify the design inputs that result in a pre-specified response value from a single computer experiment$\unicode{x2014}$is a well-studied active learning problem. Here, we tackle a related but distinct problem: identifying the input configuration that returns pre-specified values of multiple independent computer experiments simultaneously. Motivated by computer experiments of the rotational torques acting upon a vehicle in flight, we aim to identify stable flight conditions which result in zero torque forces. We propose a "joint contour location" (jCL) scheme that strikes a strategic balance between exploring the multiple response surfaces while exploiting learning of the intersecting contours. We employ both shallow and deep Gaussian process surrogates, but our jCL procedure is applicable to any surrogate that can provide posterior predictive distributions. Our jCL designs significantly outperform existing (single response) CL strategies, enabling us to efficiently locate the joint contour of our motivating computer experiments.

