---
layout: default
title: AgriLiRa4D: A Multi-Sensor UAV Dataset for Robust SLAM in Challenging Agricultural Fields
---

# AgriLiRa4D: A Multi-Sensor UAV Dataset for Robust SLAM in Challenging Agricultural Fields

**arXiv**: [2512.01753v1](https://arxiv.org/abs/2512.01753) | [PDF](https://arxiv.org/pdf/2512.01753.pdf)

**作者**: Zhihao Zhan, Yuhang Ming, Shaobin Li, Jie Yuan

---

## 💡 一句话要点

**提出AgriLiRa4D多模态无人机数据集，以支持农业环境中鲁棒SLAM研究。**

**关键词**: `农业SLAM` `多模态数据集` `无人机导航` `鲁棒定位` `传感器融合` `真实环境评估`

## 📋 核心要点

1. 核心问题：农业无人机SLAM缺乏真实多模态数据集，难以应对低纹理、重复模式等挑战。
2. 方法要点：提供包含3D LiDAR、4D雷达、IMU和FINS_RTK高精度轨迹的同步数据，覆盖平坦、丘陵和梯田三种农田类型。
3. 实验或效果：基准测试四种多传感器SLAM算法，验证数据集对鲁棒性评估的实用性，促进农业无人机自主导航技术发展。

## 📄 摘要（原文）

> Multi-sensor Simultaneous Localization and Mapping (SLAM) is essential for Unmanned Aerial Vehicles (UAVs) performing agricultural tasks such as spraying, surveying, and inspection. However, real-world, multi-modal agricultural UAV datasets that enable research on robust operation remain scarce. To address this gap, we present AgriLiRa4D, a multi-modal UAV dataset designed for challenging outdoor agricultural environments. AgriLiRa4D spans three representative farmland types-flat, hilly, and terraced-and includes both boundary and coverage operation modes, resulting in six flight sequence groups. The dataset provides high-accuracy ground-truth trajectories from a Fiber Optic Inertial Navigation System with Real-Time Kinematic capability (FINS_RTK), along with synchronized measurements from a 3D LiDAR, a 4D Radar, and an Inertial Measurement Unit (IMU), accompanied by complete intrinsic and extrinsic calibrations. Leveraging its comprehensive sensor suite and diverse real-world scenarios, AgriLiRa4D supports diverse SLAM and localization studies and enables rigorous robustness evaluation against low-texture crops, repetitive patterns, dynamic vegetation, and other challenges of real agricultural environments. To further demonstrate its utility, we benchmark four state-of-the-art multi-sensor SLAM algorithms across different sensor combinations, highlighting the difficulty of the proposed sequences and the necessity of multi-modal approaches for reliable UAV localization. By filling a critical gap in agricultural SLAM datasets, AgriLiRa4D provides a valuable benchmark for the research community and contributes to advancing autonomous navigation technologies for agricultural UAVs. The dataset can be downloaded from: https://zhan994.github.io/AgriLiRa4D.

