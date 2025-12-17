---
layout: default
title: Breaking the Passive Learning Trap: An Active Perception Strategy for Human Motion Prediction
---

# Breaking the Passive Learning Trap: An Active Perception Strategy for Human Motion Prediction

**arXiv**: [2511.14237v1](https://arxiv.org/abs/2511.14237) | [PDF](https://arxiv.org/pdf/2511.14237.pdf)

**作者**: Juncheng Hu, Zijian Zhang, Zeyu Wang, Guoyu Wang, Yingji Li, Kedi Lyu

---

## 💡 一句话要点

**提出主动感知策略以解决3D人体运动预测中的被动学习问题**

**关键词**: `3D人体运动预测` `主动感知策略` `商空间表示` `辅助学习` `时空建模`

## 📋 核心要点

1. 核心问题：现有方法依赖隐式网络建模，导致冗余坐标获取和单调学习
2. 方法要点：使用商空间表示和辅助学习目标，增强运动属性和时空建模
3. 实验或效果：在多个数据集上实现SOTA，性能提升超过10%

## 📄 摘要（原文）

> Forecasting 3D human motion is an important embodiment of fine-grained understanding and cognition of human behavior by artificial agents. Current approaches excessively rely on implicit network modeling of spatiotemporal relationships and motion characteristics, falling into the passive learning trap that results in redundant and monotonous 3D coordinate information acquisition while lacking actively guided explicit learning mechanisms. To overcome these issues, we propose an Active Perceptual Strategy (APS) for human motion prediction, leveraging quotient space representations to explicitly encode motion properties while introducing auxiliary learning objectives to strengthen spatio-temporal modeling. Specifically, we first design a data perception module that projects poses into the quotient space, decoupling motion geometry from coordinate redundancy. By jointly encoding tangent vectors and Grassmann projections, this module simultaneously achieves geometric dimension reduction, semantic decoupling, and dynamic constraint enforcement for effective motion pose characterization. Furthermore, we introduce a network perception module that actively learns spatio-temporal dependencies through restorative learning. This module deliberately masks specific joints or injects noise to construct auxiliary supervision signals. A dedicated auxiliary learning network is designed to actively adapt and learn from perturbed information. Notably, APS is model agnostic and can be integrated with different prediction models to enhance active perceptual. The experimental results demonstrate that our method achieves the new state-of-the-art, outperforming existing methods by large margins: 16.3% on H3.6M, 13.9% on CMU Mocap, and 10.1% on 3DPW.

