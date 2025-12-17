---
layout: default
title: Simultaneous Calibration of Noise Covariance and Kinematics for State Estimation of Legged Robots via Bi-level Optimization
---

# Simultaneous Calibration of Noise Covariance and Kinematics for State Estimation of Legged Robots via Bi-level Optimization

**arXiv**: [2510.11539v1](https://arxiv.org/abs/2510.11539) | [PDF](https://arxiv.org/pdf/2510.11539.pdf)

**作者**: Denglin Cheng, Jiarong Kang, Xiaobin Xiong

---

## 💡 一句话要点

**提出双级优化框架以联合校准噪声协方差和运动学参数，提升腿式机器人状态估计精度**

**关键词**: `状态估计` `噪声协方差校准` `双级优化` `腿式机器人` `运动学参数校准` `数据驱动框架`

## 📋 核心要点

1. 核心问题：腿式和空中机器人在动态环境中状态估计需准确噪声协方差，但通常未知或手动调整
2. 方法要点：采用双级优化，上层优化噪声协方差和模型参数，下层执行全信息估计器
3. 实验或效果：在四足和人形机器人上验证，估计精度和不确定性校准显著优于手动基线

## 📄 摘要（原文）

> Accurate state estimation is critical for legged and aerial robots operating
> in dynamic, uncertain environments. A key challenge lies in specifying process
> and measurement noise covariances, which are typically unknown or manually
> tuned. In this work, we introduce a bi-level optimization framework that
> jointly calibrates covariance matrices and kinematic parameters in an
> estimator-in-the-loop manner. The upper level treats noise covariances and
> model parameters as optimization variables, while the lower level executes a
> full-information estimator. Differentiating through the estimator allows direct
> optimization of trajectory-level objectives, resulting in accurate and
> consistent state estimates. We validate our approach on quadrupedal and
> humanoid robots, demonstrating significantly improved estimation accuracy and
> uncertainty calibration compared to hand-tuned baselines. Our method unifies
> state estimation, sensor, and kinematics calibration into a principled,
> data-driven framework applicable across diverse robotic platforms.

