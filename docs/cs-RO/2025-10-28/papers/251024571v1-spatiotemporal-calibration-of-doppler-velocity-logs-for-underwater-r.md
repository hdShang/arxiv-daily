---
layout: default
title: Spatiotemporal Calibration of Doppler Velocity Logs for Underwater Robots
---

# Spatiotemporal Calibration of Doppler Velocity Logs for Underwater Robots

**arXiv**: [2510.24571v1](https://arxiv.org/abs/2510.24571) | [PDF](https://arxiv.org/pdf/2510.24571.pdf)

**作者**: Hongxu Zhao, Guangyang Zeng, Yunling Shao, Tengfei Zhang, Junfeng Wu

---

## 💡 一句话要点

**提出统一迭代校准框架，解决水下机器人多传感器时空校准问题**

**关键词**: `水下机器人` `传感器校准` `最大后验估计` `高斯过程` `多模态融合` `开源工具`

## 📋 核心要点

1. 核心问题：水下SLAM中DVL传感器外参和时钟偏移校准不足，现有方法受限或假设简化
2. 方法要点：基于MAP估计和GP运动先验，交替更新运动状态与校准变量，提供统计一致初始化
3. 实验或效果：通过仿真和真实测试验证，并发布开源DVL-相机校准工具箱

## 📄 摘要（原文）

> The calibration of extrinsic parameters and clock offsets between sensors for
> high-accuracy performance in underwater SLAM systems remains insufficiently
> explored. Existing methods for Doppler Velocity Log (DVL) calibration are
> either constrained to specific sensor configurations or rely on oversimplified
> assumptions, and none jointly estimate translational extrinsics and time
> offsets. We propose a Unified Iterative Calibration (UIC) framework for general
> DVL sensor setups, formulated as a Maximum A Posteriori (MAP) estimation with a
> Gaussian Process (GP) motion prior for high-fidelity motion interpolation. UIC
> alternates between efficient GP-based motion state updates and gradient-based
> calibration variable updates, supported by a provably statistically consistent
> sequential initialization scheme. The proposed UIC can be applied to IMU,
> cameras and other modalities as co-sensors. We release an open-source
> DVL-camera calibration toolbox. Beyond underwater applications, several aspects
> of UIC-such as the integration of GP priors for MAP-based calibration and the
> design of provably reliable initialization procedures-are broadly applicable to
> other multi-sensor calibration problems. Finally, simulations and real-world
> tests validate our approach.

