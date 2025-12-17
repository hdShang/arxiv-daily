---
layout: default
title: Direct Data-Driven Predictive Control for a Three-dimensional Cable-Driven Soft Robotic Arm
---

# Direct Data-Driven Predictive Control for a Three-dimensional Cable-Driven Soft Robotic Arm

**arXiv**: [2510.08953v1](https://arxiv.org/abs/2510.08953) | [PDF](https://arxiv.org/pdf/2510.08953.pdf)

**作者**: Cheng Ouyang, Moeen Ul Islam, Dong Chen, Kaixiang Zhang, Zhaojian Li, Xiaobo Tan

---

## 💡 一句话要点

**提出数据驱动预测控制框架以解决三维软体机器人动态控制难题**

**关键词**: `软体机器人控制` `数据驱动预测控制` `三维运动控制` `模型自由控制` `轨迹跟踪`

## 📋 核心要点

1. 软体机器人因非线性动力学难以实现精确动态控制
2. 采用DeePC方法直接利用输入输出数据，避免显式系统辨识
3. 实验验证在三维软体臂上实现高精度轨迹跟踪和鲁棒性

## 📄 摘要（原文）

> Soft robots offer significant advantages in safety and adaptability, yet
> achieving precise and dynamic control remains a major challenge due to their
> inherently complex and nonlinear dynamics. Recently, Data-enabled Predictive
> Control (DeePC) has emerged as a promising model-free approach that bypasses
> explicit system identification by directly leveraging input-output data. While
> DeePC has shown success in other domains, its application to soft robots
> remains underexplored, particularly for three-dimensional (3D) soft robotic
> systems. This paper addresses this gap by developing and experimentally
> validating an effective DeePC framework on a 3D, cable-driven soft arm.
> Specifically, we design and fabricate a soft robotic arm with a thick tubing
> backbone for stability, a dense silicone body with large cavities for strength
> and flexibility, and rigid endcaps for secure termination. Using this platform,
> we implement DeePC with singular value decomposition (SVD)-based dimension
> reduction for two key control tasks: fixed-point regulation and trajectory
> tracking in 3D space. Comparative experiments with a baseline model-based
> controller demonstrate DeePC's superior accuracy, robustness, and adaptability,
> highlighting its potential as a practical solution for dynamic control of soft
> robots.

