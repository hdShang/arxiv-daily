---
layout: default
title: LVI-Q: Robust LiDAR-Visual-Inertial-Kinematic Odometry for Quadruped Robots Using Tightly-Coupled and Efficient Alternating Optimization
---

# LVI-Q: Robust LiDAR-Visual-Inertial-Kinematic Odometry for Quadruped Robots Using Tightly-Coupled and Efficient Alternating Optimization

**arXiv**: [2510.15220v1](https://arxiv.org/abs/2510.15220) | [PDF](https://arxiv.org/pdf/2510.15220.pdf)

**作者**: Kevin Christiansen Marsim, Minho Oh, Byeongho Yu, Seungjae Lee, I Made Aswin Nahrendra, Hyungtae Lim, Hyun Myung

---

## 💡 一句话要点

**提出LVI-Q系统以增强四足机器人在复杂环境中的鲁棒定位与建图**

**关键词**: `四足机器人` `传感器融合` `SLAM系统` `交替优化` `鲁棒定位`

## 📋 核心要点

1. 核心问题：现有传感器融合SLAM在挑战性环境中易产生估计漂移，依赖不合适的融合策略。
2. 方法要点：采用紧密耦合交替优化，结合视觉-惯性-运动学与LiDAR-惯性-运动学里程计。
3. 实验或效果：在公共和长期数据集上展示优于其他融合算法的鲁棒性能。

## 📄 摘要（原文）

> Autonomous navigation for legged robots in complex and dynamic environments
> relies on robust simultaneous localization and mapping (SLAM) systems to
> accurately map surroundings and localize the robot, ensuring safe and efficient
> operation. While prior sensor fusion-based SLAM approaches have integrated
> various sensor modalities to improve their robustness, these algorithms are
> still susceptible to estimation drift in challenging environments due to their
> reliance on unsuitable fusion strategies. Therefore, we propose a robust
> LiDAR-visual-inertial-kinematic odometry system that integrates information
> from multiple sensors, such as a camera, LiDAR, inertial measurement unit
> (IMU), and joint encoders, for visual and LiDAR-based odometry estimation. Our
> system employs a fusion-based pose estimation approach that runs
> optimization-based visual-inertial-kinematic odometry (VIKO) and filter-based
> LiDAR-inertial-kinematic odometry (LIKO) based on measurement availability. In
> VIKO, we utilize the footpreintegration technique and robust LiDAR-visual depth
> consistency using superpixel clusters in a sliding window optimization. In
> LIKO, we incorporate foot kinematics and employ a point-toplane residual in an
> error-state iterative Kalman filter (ESIKF). Compared with other sensor
> fusion-based SLAM algorithms, our approach shows robust performance across
> public and longterm datasets.

