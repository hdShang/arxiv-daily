---
layout: default
title: Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations
---

# Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations

**arXiv**: [2512.14428v1](https://arxiv.org/abs/2512.14428) | [PDF](https://arxiv.org/pdf/2512.14428.pdf)

**作者**: Aaron Kurda, Simon Steuernagel, Lukas Jung, Marcus Baum

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: 9 pages, 4 figures, submitted to International Journal of Robotics Research (IJRR)

---

## 💡 一句话要点

**提出Odyssey数据集，基于环形激光陀螺仪惯性导航系统，为GNSS信号缺失环境下的激光雷达-惯性里程计研究提供高精度地面真值。**

🎯 **匹配领域**: **自动驾驶** **视觉里程计** **强化学习**

**关键词**: `激光雷达-惯性里程计` `同时定位与建图` `惯性导航系统` `环形激光陀螺仪` `GNSS缺失环境` `自动驾驶数据集` `地点识别` `传感器融合`

## 📋 核心要点

1. 核心问题：现有数据集依赖GNSS作为地面真值，但在遮挡环境中信号不可靠，且常用IMU系统（如MEMS或FOG）偏置稳定性不足，无法支持GNSS缺失环境的长期研究。
2. 方法要点：提出Odyssey数据集，采用基于环形激光陀螺仪的导航级惯性导航系统提供高精度地面真值，专注于隧道、停车场等GNSS缺失场景。
3. 实验或效果：数据集首次公开基于RLG的INS数据，支持LIO、SLAM和地点识别等任务，通过重复轨迹和地理坐标增强实用性。

## 📝 摘要（中文）

激光雷达-惯性里程计（LIO）和同时定位与建图（SLAM）系统的开发与评估需要精确的地面真值。全球导航卫星系统（GNSS）常被用作基础，但其信号在遮挡环境中可能因多径效应或信号丢失而不可靠。现有数据集通过集成惯性测量单元（IMU）测量来补偿GNSS信号的偶发性丢失，但常用的微机电系统（MEMS）或光纤陀螺仪（FOG）系统无法支持对GNSS缺失环境的长期研究。为填补这一空白，我们提出了Odyssey，一个专注于GNSS缺失环境（如隧道和停车场）以及其他代表性不足但普遍存在场景（如启停交通、颠簸道路和开阔田野）的LIO数据集。我们的地面真值源自配备环形激光陀螺仪（RLG）的导航级惯性导航系统（INS），相比现有数据集使用的IMU，具有卓越的偏置稳定性特性，支持对GNSS缺失环境的长期准确研究。这使得Odyssey成为首个公开可用的基于RLG的INS数据集。除了为LIO提供数据外，我们还通过三次重复所有轨迹以及提供精确大地坐标集成外部地图数据，支持其他任务，如地点识别。所有数据、数据加载器和其他材料可在https://odyssey.uni-goettingen.de/在线获取。

## 🔬 方法详解

论文的核心方法是构建Odyssey数据集，其整体框架包括数据采集、处理和发布。关键技术创新点在于使用配备环形激光陀螺仪的导航级惯性导航系统作为地面真值源，相比现有数据集中的微机电系统或光纤陀螺仪，RLG具有更高的偏置稳定性，能提供更准确和长期的姿态估计。与现有方法的主要区别在于：Odyssey专注于GNSS缺失环境（如隧道、停车场），并覆盖启停交通、颠簸道路等代表性不足场景；通过三次重复轨迹和集成外部地图数据，支持地点识别等扩展任务；数据集公开可用，填补了长期GNSS缺失研究的数据空白。

## 📊 实验亮点

最重要的实验亮点是Odyssey数据集首次公开基于环形激光陀螺仪的惯性导航系统数据，相比现有数据集，其地面真值在偏置稳定性上显著提升，支持对GNSS缺失环境的长期准确研究。数据集覆盖多样场景，并通过重复轨迹增强实用性，为LIO和SLAM算法提供了更可靠的评估基准。

## 🎯 应用场景

该研究主要应用于自动驾驶和机器人领域，特别是在GNSS信号受限或缺失的环境（如城市隧道、地下停车场、山区道路）中，为激光雷达-惯性里程计和同时定位与建图系统的开发、测试和评估提供基准数据。此外，数据集支持地点识别、地图构建和传感器融合算法的研究，提升定位精度和鲁棒性。

## 📄 摘要（原文）

> The development and evaluation of Lidar-Inertial Odometry (LIO) and Simultaneous Localization and Mapping (SLAM) systems requires a precise ground truth. The Global Navigation Satellite System (GNSS) is often used as a foundation for this, but its signals can be unreliable in obstructed environments due to multi-path effects or loss-of-signal. While existing datasets compensate for the sporadic loss of GNSS signals by incorporating Inertial Measurement Unit (IMU) measurements, the commonly used Micro-Electro-Mechanical Systems (MEMS) or Fiber Optic Gyroscope (FOG)-based systems do not permit the prolonged study of GNSS-denied environments. To close this gap, we present Odyssey, a LIO dataset with a focus on GNSS-denied environments such as tunnels and parking garages as well as other underrepresented, yet ubiquitous situations such as stop-and-go-traffic, bumpy roads and wide open fields. Our ground truth is derived from a navigation-grade Inertial Navigation System (INS) equipped with a Ring Laser Gyroscope (RLG), offering exceptional bias stability characteristics compared to IMUs used in existing datasets and enabling the prolonged and accurate study of GNSS-denied environments. This makes Odyssey the first publicly available dataset featuring a RLG-based INS. Besides providing data for LIO, we also support other tasks, such as place recognition, through the threefold repetition of all trajectories as well as the integration of external mapping data by providing precise geodetic coordinates. All data, dataloader and other material is available online at https://odyssey.uni-goettingen.de/ .

