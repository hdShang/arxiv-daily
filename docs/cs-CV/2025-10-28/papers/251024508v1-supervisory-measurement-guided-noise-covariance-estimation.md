---
layout: default
title: Supervisory Measurement-Guided Noise Covariance Estimation
---

# Supervisory Measurement-Guided Noise Covariance Estimation

**arXiv**: [2510.24508v1](https://arxiv.org/abs/2510.24508) | [PDF](https://arxiv.org/pdf/2510.24508.pdf)

**作者**: Haoying Li, Yifan Peng, Junfeng Wu

---

## 💡 一句话要点

**提出双层优化方法以高效估计传感器噪声协方差**

**关键词**: `噪声协方差估计` `双层优化` `状态估计` `贝叶斯方法` `并行计算`

## 📋 核心要点

1. 核心问题：传感器噪声协方差难以准确指定，影响状态估计可靠性。
2. 方法要点：将噪声协方差估计建模为双层优化，分解联合似然，实现高效并行计算。
3. 实验效果：在合成和真实数据集上，方法比基线更高效。

## 📄 摘要（原文）

> Reliable state estimation hinges on accurate specification of sensor noise
> covariances, which weigh heterogeneous measurements. In practice, these
> covariances are difficult to identify due to environmental variability,
> front-end preprocessing, and other reasons. We address this by formulating
> noise covariance estimation as a bilevel optimization that, from a Bayesian
> perspective, factorizes the joint likelihood of so-called odometry and
> supervisory measurements, thereby balancing information utilization with
> computational efficiency. The factorization converts the nested Bayesian
> dependency into a chain structure, enabling efficient parallel computation: at
> the lower level, an invariant extended Kalman filter with state augmentation
> estimates trajectories, while a derivative filter computes analytical gradients
> in parallel for upper-level gradient updates. The upper level refines the
> covariance to guide the lower-level estimation. Experiments on synthetic and
> real-world datasets show that our method achieves higher efficiency over
> existing baselines.

