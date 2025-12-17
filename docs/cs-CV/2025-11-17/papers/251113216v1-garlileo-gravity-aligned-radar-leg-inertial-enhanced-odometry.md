---
layout: default
title: GaRLILEO: Gravity-aligned Radar-Leg-Inertial Enhanced Odometry
---

# GaRLILEO: Gravity-aligned Radar-Leg-Inertial Enhanced Odometry

**arXiv**: [2511.13216v1](https://arxiv.org/abs/2511.13216) | [PDF](https://arxiv.org/pdf/2511.13216.pdf)

**作者**: Chiyun Noh, Sangwoo Jung, Hanjun Kim, Yafei Hu, Laura Herlant, Ayoung Kim

---

## 💡 一句话要点

**提出GaRLILEO以解决腿式机器人在复杂地形中的垂直里程计漂移问题**

**关键词**: `腿式机器人里程计` `雷达-腿-惯性融合` `重力对齐估计` `连续时间优化` `垂直姿态精度`

## 📋 核心要点

1. 核心问题：腿式机器人里程计在垂直方向易漂移，源于接触冲击和姿态估计不准
2. 方法要点：结合雷达多普勒和腿运动学构建连续时间速度样条，并引入软S2约束重力因子
3. 实验或效果：在室内外数据集上验证，垂直里程计精度领先，尤其在楼梯和斜坡场景

## 📄 摘要（原文）

> Deployment of legged robots for navigating challenging terrains (e.g., stairs, slopes, and unstructured environments) has gained increasing preference over wheel-based platforms. In such scenarios, accurate odometry estimation is a preliminary requirement for stable locomotion, localization, and mapping. Traditional proprioceptive approaches, which rely on leg kinematics sensor modalities and inertial sensing, suffer from irrepressible vertical drift caused by frequent contact impacts, foot slippage, and vibrations, particularly affected by inaccurate roll and pitch estimation. Existing methods incorporate exteroceptive sensors such as LiDAR or cameras. Further enhancement has been introduced by leveraging gravity vector estimation to add additional observations on roll and pitch, thereby increasing the accuracy of vertical pose estimation. However, these approaches tend to degrade in feature-sparse or repetitive scenes and are prone to errors from double-integrated IMU acceleration. To address these challenges, we propose GaRLILEO, a novel gravity-aligned continuous-time radar-leg-inertial odometry framework. GaRLILEO decouples velocity from the IMU by building a continuous-time ego-velocity spline from SoC radar Doppler and leg kinematics information, enabling seamless sensor fusion which mitigates odometry distortion. In addition, GaRLILEO can reliably capture accurate gravity vectors leveraging a novel soft S2-constrained gravity factor, improving vertical pose accuracy without relying on LiDAR or cameras. Evaluated on a self-collected real-world dataset with diverse indoor-outdoor trajectories, GaRLILEO demonstrates state-of-the-art accuracy, particularly in vertical odometry estimation on stairs and slopes. We open-source both our dataset and algorithm to foster further research in legged robot odometry and SLAM. https://garlileo.github.io/GaRLILEO

