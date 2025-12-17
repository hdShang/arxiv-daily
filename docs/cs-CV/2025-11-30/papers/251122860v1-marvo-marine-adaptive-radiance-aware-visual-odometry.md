---
layout: default
title: MARVO: Marine-Adaptive Radiance-aware Visual Odometry
---

# MARVO: Marine-Adaptive Radiance-aware Visual Odometry

**arXiv**: [2511.22860v1](https://arxiv.org/abs/2511.22860) | [PDF](https://arxiv.org/pdf/2511.22860.pdf)

**作者**: Sacchin Sundar, Atman Kikani, Aaliya Alam, Sumukh Shrote, A. Nayeemulla Khan, A. Shahina

---

## 💡 一句话要点

**提出MARVO框架，融合物理建模与强化学习，解决水下视觉定位挑战。**

**关键词**: `水下视觉里程计` `物理感知建模` `强化学习优化` `多传感器融合` `因子图估计`

## 📋 核心要点

1. 核心问题：水下视觉定位受波长衰减、纹理差和非高斯噪声影响。
2. 方法要点：前端用物理感知适配器增强特征匹配，后端结合多传感器因子图优化。
3. 实验或效果：实时全状态估计，强化学习优化器提升全局轨迹精度。

## 📄 摘要（原文）

> Underwater visual localization remains challenging due to wavelength-dependent attenuation, poor texture, and non-Gaussian sensor noise. We introduce MARVO, a physics-aware, learning-integrated odometry framework that fuses underwater image formation modeling, differentiable matching, and reinforcement-learning optimization. At the front-end, we extend transformer-based feature matcher with a Physics Aware Radiance Adapter that compensates for color channel attenuation and contrast loss, yielding geometrically consistent feature correspondences under turbidity. These semi dense matches are combined with inertial and pressure measurements inside a factor-graph backend, where we formulate a keyframe-based visual-inertial-barometric estimator using GTSAM library. Each keyframe introduces (i) Pre-integrated IMU motion factors, (ii) MARVO-derived visual pose factors, and (iii) barometric depth priors, giving a full-state MAP estimate in real time. Lastly, we introduce a Reinforcement-Learningbased Pose-Graph Optimizer that refines global trajectories beyond local minima of classical least-squares solvers by learning optimal retraction actions on SE(2).

