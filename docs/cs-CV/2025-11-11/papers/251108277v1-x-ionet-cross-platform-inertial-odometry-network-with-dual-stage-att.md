---
layout: default
title: X-IONet: Cross-Platform Inertial Odometry Network with Dual-Stage Attention
---

# X-IONet: Cross-Platform Inertial Odometry Network with Dual-Stage Attention

**arXiv**: [2511.08277v1](https://arxiv.org/abs/2511.08277) | [PDF](https://arxiv.org/pdf/2511.08277.pdf)

**作者**: Dehan Shen, Changhao Chen

---

## 💡 一句话要点

**提出X-IONet以解决跨平台惯性里程计在行人和四足机器人上的性能退化问题**

**关键词**: `惯性里程计` `跨平台学习` `双阶段注意力` `专家网络` `状态估计`

## 📋 核心要点

1. 核心问题：基于学习的惯性里程计在四足机器人上性能显著下降，因运动模式差异大
2. 方法要点：采用基于规则的专家选择模块和双阶段注意力网络，结合EKF进行状态估计
3. 实验或效果：在公开和自收集数据集上，ATE和RTE在行人和四足机器人数据上均显著降低

## 📄 摘要（原文）

> Learning-based inertial odometry has achieved remarkable progress in pedestrian navigation. However, extending these methods to quadruped robots remains challenging due to their distinct and highly dynamic motion patterns. Models that perform well on pedestrian data often experience severe degradation when deployed on legged platforms. To tackle this challenge, we introduce X-IONet, a cross-platform inertial odometry framework that operates solely using a single Inertial Measurement Unit (IMU). X-IONet incorporates a rule-based expert selection module to classify motion platforms and route IMU sequences to platform-specific expert networks. The displacement prediction network features a dual-stage attention architecture that jointly models long-range temporal dependencies and inter-axis correlations, enabling accurate motion representation. It outputs both displacement and associated uncertainty, which are further fused through an Extended Kalman Filter (EKF) for robust state estimation. Extensive experiments on public pedestrian datasets and a self-collected quadruped robot dataset demonstrate that X-IONet achieves state-of-the-art performance, reducing Absolute Trajectory Error (ATE) by 14.3% and Relative Trajectory Error (RTE) by 11.4% on pedestrian data, and by 52.8% and 41.3% on quadruped robot data. These results highlight the effectiveness of X-IONet in advancing accurate and robust inertial navigation across both human and legged robot platforms.

