---
layout: default
title: Physics-Informed Learning of Flow Distribution and Receiver Heat Losses in Parabolic Trough Solar Fields
---

# Physics-Informed Learning of Flow Distribution and Receiver Heat Losses in Parabolic Trough Solar Fields

**arXiv**: [2512.10886v1](https://arxiv.org/abs/2512.10886) | [PDF](https://arxiv.org/pdf/2512.10886.pdf)

**作者**: Stefan Matthes, Markus Schramm

---

## 💡 一句话要点

**提出物理信息学习框架，从运行数据推断抛物槽太阳能场流量分布与接收器热损参数。**

**关键词**: `物理信息学习` `抛物槽太阳能场` `流量分布推断` `接收器热损估计` `可微优化` `运行数据分析`

## 📋 核心要点

1. 问题：抛物槽CSP场中，回路流量与接收器热损参数未知，导致无法诊断水力失衡或接收器退化。
2. 方法：利用夜间均质化周期，嵌入可微共轭传热模型，通过端到端学习从历史数据优化推断参数。
3. 效果：模型准确重建回路温度，识别高损接收器区域，与红外热成像结果一致。

## 📄 摘要（原文）

> Parabolic trough Concentrating Solar Power (CSP) plants operate large hydraulic networks of collector loops that must deliver a uniform outlet temperature despite spatially heterogeneous optical performance, heat losses, and pressure drops. While loop temperatures are measured, loop-level mass flows and receiver heat-loss parameters are unobserved, making it impossible to diagnose hydraulic imbalances or receiver degradation using standard monitoring tools.
>   We present a physics-informed learning framework that infers (i) loop-level mass-flow ratios and (ii) time-varying receiver heat-transfer coefficients directly from routine operational data. The method exploits nocturnal homogenization periods -- when hot oil is circulated through a non-irradiated field -- to isolate hydraulic and thermal-loss effects. A differentiable conjugate heat-transfer model is discretized and embedded into an end-to-end learning pipeline optimized using historical plant data from the 50 MW Andasol 3 solar field.
>   The model accurately reconstructs loop temperatures (RMSE $<2^\circ$C) and produces physically meaningful estimates of loop imbalances and receiver heat losses. Comparison against drone-based infrared thermography (QScan) shows strong correspondence, correctly identifying all areas with high-loss receivers. This demonstrates that noisy real-world CSP operational data contain enough information to recover latent physical parameters when combined with appropriate modeling and differentiable optimization.

