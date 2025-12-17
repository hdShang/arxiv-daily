---
layout: default
title: CM-LIUW-Odometry: Robust and High-Precision LiDAR-Inertial-UWB-Wheel Odometry for Extreme Degradation Coal Mine Tunnels
---

# CM-LIUW-Odometry: Robust and High-Precision LiDAR-Inertial-UWB-Wheel Odometry for Extreme Degradation Coal Mine Tunnels

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01379" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01379v1</a>
  <a href="https://arxiv.org/pdf/2511.01379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01379v1" onclick="toggleFavorite(this, '2511.01379v1', 'CM-LIUW-Odometry: Robust and High-Precision LiDAR-Inertial-UWB-Wheel Odometry for Extreme Degradation Coal Mine Tunnels')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kun Hu, Menggang Li, Zhiwen Jin, Chaoquan Tang, Eryi Hu, Gongbo Zhou

**分类**: cs.RO

**发布日期**: 2025-11-03

**备注**: Accepted by IROS 2025

---

## 💡 一句话要点

**CM-LIUW-Odometry：面向极端退化煤矿巷道的鲁棒高精度激光-惯性-UWB-轮速里程计**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `激光雷达` `惯性导航` `UWB定位` `轮速里程计` `多传感器融合` `煤矿环境` `同步定位与建图` `误差状态卡尔曼滤波`

## 📋 核心要点

1. 现有方法在煤矿隧道中面临GPS缺失、地形崎岖和特征匮乏等挑战，导致定位精度和鲁棒性下降。
2. CM-LIUW-Odometry通过紧耦合激光雷达、惯性测量单元、UWB和轮速计数据，提升在恶劣环境下的定位性能。
3. 实验结果验证了CM-LIUW-Odometry在真实煤矿场景中的优越性，显著提升了定位精度和鲁棒性。

## 📝 摘要（中文）

针对大规模、复杂且无GPS的地下煤矿环境中的同步定位与建图(SLAM)难题，本文提出了CoalMine-LiDAR-IMU-UWB-Wheel-Odometry (CM-LIUW-Odometry)。该方法基于迭代误差状态卡尔曼滤波器(IESKF)构建多模态SLAM框架。首先，激光雷达-惯性里程计与UWB绝对定位约束紧耦合，使SLAM系统与全局坐标对齐。其次，通过紧耦合集成轮速里程计，并结合非完整约束(NHC)和车辆杆臂补偿，解决UWB测量范围外性能退化问题。最后，自适应运动模式切换机制根据UWB测量范围和环境退化程度动态调整机器人运动模式。实验结果表明，该方法在真实地下煤矿场景中实现了优于现有方法的精度和鲁棒性。该工作的代码已在Github上开源。

## 🔬 方法详解

**问题定义**：在地下煤矿环境中，由于GPS信号缺失、地形崎岖不平以及长而特征匮乏的隧道，传统的SLAM方法面临着定位精度和鲁棒性下降的挑战。轮速计在不平坦或湿滑的地面上容易产生较大的误差，而激光雷达在特征稀疏的环境中也难以提供可靠的定位信息。因此，如何在极端退化的煤矿隧道环境中实现高精度和鲁棒的定位是本文要解决的关键问题。

**核心思路**：本文的核心思路是将激光雷达、惯性测量单元(IMU)、超宽带(UWB)和轮速计的数据进行紧耦合，利用各自的优势来弥补彼此的不足。UWB提供绝对位置约束，校正累积误差；轮速计提供短时间内的相对运动信息，提高定位频率；激光雷达和IMU提供环境几何信息和运动估计。通过多传感器融合，提高系统在恶劣环境下的鲁棒性和精度。

**技术框架**：CM-LIUW-Odometry采用基于迭代误差状态卡尔曼滤波器(IESKF)的多模态SLAM框架。该框架主要包括以下几个模块：1) 激光雷达-惯性里程计(LIO)：利用激光雷达点云和IMU数据进行初始的位姿估计。2) UWB定位：利用UWB基站提供的距离信息，计算机器人的绝对位置。3) 轮速里程计：利用轮速计数据估计机器人的运动。4) 紧耦合融合：将LIO、UWB和轮速计的数据通过IESKF进行紧耦合，实现全局一致的位姿估计。5) 自适应运动模式切换：根据UWB测量范围和环境退化程度，动态调整机器人的运动模式。

**关键创新**：本文最重要的技术创新点在于多传感器紧耦合框架和自适应运动模式切换机制。传统的多传感器融合方法通常采用松耦合方式，而本文采用紧耦合方式，能够更充分地利用传感器之间的互补信息，提高定位精度。自适应运动模式切换机制能够根据环境变化动态调整机器人的运动模式，提高系统的鲁棒性。

**关键设计**：在紧耦合融合中，本文采用了迭代误差状态卡尔曼滤波器(IESKF)，能够有效地处理非线性误差。同时，本文还考虑了车辆杆臂的补偿，提高了轮速里程计的精度。在自适应运动模式切换中，本文根据UWB测量范围和环境退化程度，动态调整LIO、UWB和轮速计的权重，以实现最佳的定位性能。

## 📊 实验亮点

实验结果表明，CM-LIUW-Odometry在真实地下煤矿场景中实现了优于现有方法的精度和鲁棒性。相较于其他state-of-the-art方法，该方法在定位精度方面有显著提升，尤其是在UWB信号较弱或缺失的区域，通过轮速计和非完整约束的紧耦合，有效抑制了漂移。

## 🎯 应用场景

该研究成果可广泛应用于地下矿井、隧道、地下停车场等GPS信号受限或环境恶劣的场景。高精度定位能力有助于提升矿井作业效率、保障矿工安全，并为自动化采矿设备的研发提供技术支持。此外，该技术还可应用于地下管网巡检、隧道施工监测等领域，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) in large-scale, complex, and GPS-denied underground coal mine environments presents significant challenges. Sensors must contend with abnormal operating conditions: GPS unavailability impedes scene reconstruction and absolute geographic referencing, uneven or slippery terrain degrades wheel odometer accuracy, and long, feature-poor tunnels reduce LiDAR effectiveness. To address these issues, we propose CoalMine-LiDAR-IMU-UWB-Wheel-Odometry (CM-LIUW-Odometry), a multimodal SLAM framework based on the Iterated Error-State Kalman Filter (IESKF). First, LiDAR-inertial odometry is tightly fused with UWB absolute positioning constraints to align the SLAM system with a global coordinate. Next, wheel odometer is integrated through tight coupling, enhanced by nonholonomic constraints (NHC) and vehicle lever arm compensation, to address performance degradation in areas beyond UWB measurement range. Finally, an adaptive motion mode switching mechanism dynamically adjusts the robot's motion mode based on UWB measurement range and environmental degradation levels. Experimental results validate that our method achieves superior accuracy and robustness in real-world underground coal mine scenarios, outperforming state-of-the-art approaches. We open source our code of this work on Github to benefit the robotics community.

