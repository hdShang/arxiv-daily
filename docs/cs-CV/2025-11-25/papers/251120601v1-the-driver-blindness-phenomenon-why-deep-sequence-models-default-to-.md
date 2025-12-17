---
layout: default
title: The Driver-Blindness Phenomenon: Why Deep Sequence Models Default to Autocorrelation in Blood Glucose Forecasting
---

# The Driver-Blindness Phenomenon: Why Deep Sequence Models Default to Autocorrelation in Blood Glucose Forecasting

**arXiv**: [2511.20601v1](https://arxiv.org/abs/2511.20601) | [PDF](https://arxiv.org/pdf/2511.20601.pdf)

**作者**: Heman Shakeri

---

## 💡 一句话要点

**提出Driver-Blindness现象以解决血糖预测中深度序列模型忽略临床驱动因素的问题**

**关键词**: `血糖预测` `序列模型` `Driver-Blindness` `临床驱动因素` `模型评估`

## 📋 核心要点

1. 核心问题：深度序列模型在血糖预测中忽视胰岛素等临床驱动因素，性能增益Δ_drivers接近零
2. 方法要点：分析架构偏好自相关、数据保真度不足和生理异质性，提出特征编码和正则化策略
3. 实验或效果：建议报告Δ_drivers以评估模型，部分策略可缓解Driver-Blindness

## 📄 摘要（原文）

> Deep sequence models for blood glucose forecasting consistently fail to leverage clinically informative drivers--insulin, meals, and activity--despite well-understood physiological mechanisms. We term this Driver-Blindness and formalize it via $Δ_{\text{drivers}}$, the performance gain of multivariate models over matched univariate baselines. Across the literature, $Δ_{\text{drivers}}$ is typically near zero. We attribute this to three interacting factors: architectural biases favoring autocorrelation (C1), data fidelity gaps that render drivers noisy and confounded (C2), and physiological heterogeneity that undermines population-level models (C3). We synthesize strategies that partially mitigate Driver-Blindness--including physiological feature encoders, causal regularization, and personalization--and recommend that future work routinely report $Δ_{\text{drivers}}$ to prevent driver-blind models from being considered state-of-the-art.

