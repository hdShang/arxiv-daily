---
layout: default
title: Semi-distributed Cross-modal Air-Ground Relative Localization
---

# Semi-distributed Cross-modal Air-Ground Relative Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06749" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06749v1</a>
  <a href="https://arxiv.org/pdf/2511.06749.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06749v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06749v1', 'Semi-distributed Cross-modal Air-Ground Relative Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weining Lu, Deer Bin, Lian Ma, Ming Ma, Zhihao Ma, Xiangyang Chen, Longfei Wang, Yixiao Feng, Zhouxian Jiang, Yongliang Shi, Bin Liang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-11-10

**备注**: 7 pages, 3 figures. Accepted by IROS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Ascbpiac/cross-model-relative-localization.git)

---

## 💡 一句话要点

**提出半分布式跨模态空地相对定位框架，提升协同任务的灵活性和精度。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `空地协同` `相对定位` `半分布式系统` `跨模态融合` `深度学习` `Bundle Adjustment` `回环检测`

## 📋 核心要点

1. 现有机器人相对定位方法与所有机器人的状态估计紧密耦合，限制了灵活性和精度。
2. 利用UGV的高集成能力，提出半分布式跨模态空地相对定位框架，解耦相对定位与状态估计。
3. 实验结果表明，该方法在精度和效率方面表现出色，且通信带宽需求低。

## 📝 摘要（中文）

本文提出了一种高效、精确且灵活的相对定位框架，用于空地协同任务。现有机器人相对定位方法主要采用分布式多机器人SLAM系统，这些系统与所有机器人的状态估计紧密耦合，限制了灵活性和精度。本文充分利用无人地面车辆(UGV)的高集成能力，融合多种传感器，实现半分布式跨模态空地相对定位。UGV和无人机(UAV)独立执行SLAM，并提取基于深度学习的关键点和全局描述符，将相对定位与所有智能体的状态估计解耦。UGV采用包含激光雷达、相机和IMU的局部Bundle Adjustment(BA)，快速获得精确的相对位姿估计。BA过程采用稀疏关键点优化，分为两个阶段：首先优化从激光雷达惯性里程计(LIO)插值的相机位姿，然后估计UGV和UAV之间的相对相机位姿。此外，本文还实现了使用深度学习描述符的增量式回环检测算法，以高效地维护和检索关键帧。实验结果表明，该方法在精度和效率方面均表现出色。与传输图像或点云的传统多机器人SLAM方法不同，该方法仅传输关键点像素及其描述符，有效将通信带宽限制在0.3 Mbps以下。

## 🔬 方法详解

**问题定义**：论文旨在解决空地协同任务中，现有相对定位方法灵活性和精度不足的问题。传统的多机器人SLAM系统通常需要紧耦合所有机器人的状态估计，导致系统复杂且易受单个机器人误差的影响。此外，传输大量图像或点云数据对通信带宽提出了很高的要求。

**核心思路**：论文的核心思路是将相对定位与各个机器人的状态估计解耦，采用半分布式的架构。UGV和UAV分别独立进行SLAM，并通过提取和匹配跨模态的关键点和描述符来实现相对定位。这种解耦的设计提高了系统的灵活性和鲁棒性，降低了对通信带宽的需求。

**技术框架**：整体框架包含以下几个主要模块：1) UGV和UAV分别进行独立的SLAM，估计自身位姿；2) 使用深度学习方法提取图像中的关键点和全局描述符；3) UGV进行局部Bundle Adjustment(BA)，融合激光雷达、相机和IMU数据，优化位姿估计；4) 通过匹配UGV和UAV的关键点和描述符，估计它们之间的相对位姿；5) 使用增量式回环检测算法，维护和检索关键帧，提高定位精度。

**关键创新**：论文的关键创新在于半分布式的跨模态相对定位框架，以及将深度学习方法应用于关键点提取和描述符生成。通过解耦相对定位与状态估计，提高了系统的灵活性和鲁棒性。同时，利用深度学习提取的跨模态特征，实现了在不同传感器配置下的相对定位。

**关键设计**：在Bundle Adjustment(BA)过程中，采用了稀疏关键点优化，并分为两个阶段：首先，优化从激光雷达惯性里程计(LIO)插值的相机位姿；然后，估计UGV和UAV之间的相对相机位姿。此外，增量式回环检测算法使用深度学习描述符来高效地维护和检索关键帧。

## 📊 实验亮点

实验结果表明，该方法在精度和效率方面均表现出色。与传统的多机器人SLAM方法相比，该方法仅传输关键点像素及其描述符，有效将通信带宽限制在0.3 Mbps以下。这使得该方法更适用于带宽受限的环境。代码和数据已开源，方便其他研究者复现和改进。

## 🎯 应用场景

该研究成果可广泛应用于需要空地协同的场景，例如：灾害救援、环境监测、农业巡检、物流配送等。通过精确的相对定位，可以实现无人机和地面车辆之间的协同作业，提高任务效率和安全性。未来，该技术有望进一步发展，应用于更复杂的机器人协同系统。

## 📄 摘要（原文）

> Efficient, accurate, and flexible relative localization is crucial in air-ground collaborative tasks. However, current approaches for robot relative localization are primarily realized in the form of distributed multi-robot SLAM systems with the same sensor configuration, which are tightly coupled with the state estimation of all robots, limiting both flexibility and accuracy. To this end, we fully leverage the high capacity of Unmanned Ground Vehicle (UGV) to integrate multiple sensors, enabling a semi-distributed cross-modal air-ground relative localization framework. In this work, both the UGV and the Unmanned Aerial Vehicle (UAV) independently perform SLAM while extracting deep learning-based keypoints and global descriptors, which decouples the relative localization from the state estimation of all agents. The UGV employs a local Bundle Adjustment (BA) with LiDAR, camera, and an IMU to rapidly obtain accurate relative pose estimates. The BA process adopts sparse keypoint optimization and is divided into two stages: First, optimizing camera poses interpolated from LiDAR-Inertial Odometry (LIO), followed by estimating the relative camera poses between the UGV and UAV. Additionally, we implement an incremental loop closure detection algorithm using deep learning-based descriptors to maintain and retrieve keyframes efficiently. Experimental results demonstrate that our method achieves outstanding performance in both accuracy and efficiency. Unlike traditional multi-robot SLAM approaches that transmit images or point clouds, our method only transmits keypoint pixels and their descriptors, effectively constraining the communication bandwidth under 0.3 Mbps. Codes and data will be publicly available on https://github.com/Ascbpiac/cross-model-relative-localization.git.

