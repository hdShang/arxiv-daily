---
layout: default
title: "LVI-Q: Robust LiDAR-Visual-Inertial-Kinematic Odometry for Quadruped Robots Using Tightly-Coupled and Efficient Alternating Optimization"
---

# LVI-Q: Robust LiDAR-Visual-Inertial-Kinematic Odometry for Quadruped Robots Using Tightly-Coupled and Efficient Alternating Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15220" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15220v1</a>
  <a href="https://arxiv.org/pdf/2510.15220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15220v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15220v1', 'LVI-Q: Robust LiDAR-Visual-Inertial-Kinematic Odometry for Quadruped Robots Using Tightly-Coupled and Efficient Alternating Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kevin Christiansen Marsim, Minho Oh, Byeongho Yu, Seungjae Lee, I Made Aswin Nahrendra, Hyungtae Lim, Hyun Myung

**分类**: cs.RO

**发布日期**: 2025-10-17

**备注**: 8 Pages, 9 Figures

**期刊**: IEEE Robotics and Automation Letters, vol. 10, no. 10, pp. 10050-10057, Oct. 2025

**DOI**: [10.1109/LRA.2025.3598661](https://doi.org/10.1109/LRA.2025.3598661)

---

## 💡 一句话要点

**提出LVI-Q：一种鲁棒的激光雷达-视觉-惯性-运动学里程计，用于四足机器人。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四足机器人` `激光雷达` `视觉惯性里程计` `传感器融合` `运动学里程计`

## 📋 核心要点

1. 现有基于传感器融合的SLAM算法在复杂环境中易受漂移影响，原因是融合策略不当。
2. LVI-Q系统融合相机、激光雷达、IMU和关节编码器信息，通过交替优化VIKO和LIKO实现鲁棒定位。
3. 实验表明，LVI-Q在公共和长期数据集上优于其他传感器融合SLAM算法，展现了更强的鲁棒性。

## 📝 摘要（中文）

本文提出了一种鲁棒的激光雷达-视觉-惯性-运动学里程计系统（LVI-Q），用于四足机器人在复杂动态环境中实现自主导航。该系统融合了相机、激光雷达、惯性测量单元（IMU）和关节编码器等多传感器信息，用于视觉和激光雷达里程计估计。系统采用基于融合的位姿估计方法，根据测量数据的可用性，运行基于优化的视觉-惯性-运动学里程计（VIKO）和基于滤波的激光雷达-惯性-运动学里程计（LIKO）。在VIKO中，利用足部预积分技术和基于超像素聚类的鲁棒激光雷达-视觉深度一致性，进行滑动窗口优化。在LIKO中，结合足部运动学，并在误差状态迭代卡尔曼滤波器（ESIKF）中使用点到面残差。实验结果表明，与其它基于传感器融合的SLAM算法相比，该方法在公共和长期数据集上表现出更强的鲁棒性。

## 🔬 方法详解

**问题定义**：四足机器人在复杂和动态环境中自主导航需要精确的定位和建图。现有的传感器融合SLAM方法在具有挑战性的环境中容易出现估计漂移，因为它们依赖于不合适的融合策略，无法充分利用多源信息的互补性。

**核心思路**：本文的核心思路是设计一种紧耦合的激光雷达-视觉-惯性-运动学里程计，通过交替优化视觉-惯性-运动学里程计（VIKO）和激光雷达-惯性-运动学里程计（LIKO），并根据传感器数据的可用性动态切换，从而提高系统在各种环境下的鲁棒性。

**技术框架**：LVI-Q系统包含两个主要模块：VIKO和LIKO。VIKO模块利用视觉和IMU数据，并结合足部运动学信息，通过滑动窗口优化进行位姿估计。LIKO模块则利用激光雷达和IMU数据，同样结合足部运动学信息，通过误差状态迭代卡尔曼滤波器（ESIKF）进行位姿估计。系统根据传感器数据的可用性，交替运行VIKO和LIKO，并将它们的结果进行融合，以获得最终的位姿估计。

**关键创新**：该方法的主要创新在于紧耦合了视觉、激光雷达、惯性和运动学信息，并采用交替优化的策略。VIKO模块中，利用超像素聚类实现鲁棒的激光雷达-视觉深度一致性。LIKO模块中，将足部运动学信息融入到ESIKF中，提高了滤波器的精度和鲁棒性。

**关键设计**：VIKO模块使用滑动窗口优化，窗口大小需要根据环境动态调整。LIKO模块使用点到面残差作为观测模型，需要仔细选择合适的点云特征。足部预积分技术用于减少计算量。超像素聚类算法的选择和参数设置会影响深度一致性的效果。交替优化策略的切换条件需要根据传感器数据的质量进行调整。

## 📊 实验亮点

实验结果表明，LVI-Q在公共数据集和长期数据集上均表现出优异的性能。与现有的传感器融合SLAM算法相比，LVI-Q在定位精度和鲁棒性方面均有显著提升。具体数据未在摘要中给出，但强调了其在各种数据集上的优越性。

## 🎯 应用场景

该研究成果可应用于各种需要四足机器人自主导航的场景，例如：复杂地形的搜索救援、工业巡检、农业勘测、以及物流配送等。通过提高四足机器人在复杂环境下的定位精度和鲁棒性，可以使其更好地适应各种实际应用需求，并为未来的机器人自主化发展奠定基础。

## 📄 摘要（原文）

> Autonomous navigation for legged robots in complex and dynamic environments relies on robust simultaneous localization and mapping (SLAM) systems to accurately map surroundings and localize the robot, ensuring safe and efficient operation. While prior sensor fusion-based SLAM approaches have integrated various sensor modalities to improve their robustness, these algorithms are still susceptible to estimation drift in challenging environments due to their reliance on unsuitable fusion strategies. Therefore, we propose a robust LiDAR-visual-inertial-kinematic odometry system that integrates information from multiple sensors, such as a camera, LiDAR, inertial measurement unit (IMU), and joint encoders, for visual and LiDAR-based odometry estimation. Our system employs a fusion-based pose estimation approach that runs optimization-based visual-inertial-kinematic odometry (VIKO) and filter-based LiDAR-inertial-kinematic odometry (LIKO) based on measurement availability. In VIKO, we utilize the footpreintegration technique and robust LiDAR-visual depth consistency using superpixel clusters in a sliding window optimization. In LIKO, we incorporate foot kinematics and employ a point-toplane residual in an error-state iterative Kalman filter (ESIKF). Compared with other sensor fusion-based SLAM algorithms, our approach shows robust performance across public and longterm datasets.

