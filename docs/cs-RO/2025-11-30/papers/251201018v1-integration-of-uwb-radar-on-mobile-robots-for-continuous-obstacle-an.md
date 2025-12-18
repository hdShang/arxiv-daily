---
layout: default
title: Integration of UWB Radar on Mobile Robots for Continuous Obstacle and Environment Mapping
---

# Integration of UWB Radar on Mobile Robots for Continuous Obstacle and Environment Mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.01018" class="toolbar-btn" target="_blank">📄 arXiv: 2512.01018v1</a>
  <a href="https://arxiv.org/pdf/2512.01018.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.01018v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.01018v1', 'Integration of UWB Radar on Mobile Robots for Continuous Obstacle and Environment Mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adelina Giurea, Stijn Luchie, Dieter Coppens, Jeroen Hoebeke, Eli De Poorter

**分类**: cs.RO

**发布日期**: 2025-11-30

**备注**: This paper has been submitted to IEEE Access Journal and is currently undergoing review

---

## 💡 一句话要点

**提出一种基于移动机器人UWB雷达的连续障碍物与环境地图构建方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `UWB雷达` `移动机器人` `障碍物检测` `环境地图构建` `信道脉冲响应` `信号处理`

## 📋 核心要点

1. 传统视觉和激光雷达在低能见度环境下失效，限制了移动机器人的应用。
2. 利用UWB雷达，提出一种无需基础设施的障碍物检测和环境地图构建方法。
3. 实验表明，该方法能有效降低噪声和多径效应，实现较高的障碍物检测精度和召回率。

## 📝 摘要（中文）

本文提出了一种无需基础设施的障碍物检测和环境地图构建方法，该方法使用安装在移动机器人平台上的超宽带（UWB）雷达。传统的视觉相机和激光雷达（LiDAR）等传感方式在黑暗、烟雾或反射表面等能见度差的环境中失效。在这些视觉受损的条件下，UWB雷达提供了一种有前景的替代方案。为此，本研究探讨了机器人搭载的UWB雷达在动态、无锚点场景中进行环境地图构建的适用性。该研究调查了不同材料（金属、混凝土和胶合板）和UWB无线电信道（5和9）如何影响信道脉冲响应（CIR）。此外，提出了一种处理流程，以实现对检测到的障碍物的可靠映射，该流程包括3个步骤：（i）目标识别（基于CIR峰值检测），（ii）滤波（基于峰值属性、信噪比和到达相位差），以及（iii）聚类（基于距离估计和到达角估计）。所提出的方法成功地降低了噪声和多径效应，即使在检测像胶合板这样的低反射材料时，在信道9上的障碍物检测精度也至少达到82.36%，召回率达到89.46%。这项工作为进一步开发不依赖视觉特征的基于UWB的定位和地图构建（SLAM）系统奠定了基础，并且与传统的UWB定位系统不同，它不需要固定的锚节点进行三角测量。

## 🔬 方法详解

**问题定义**：论文旨在解决移动机器人在视觉受限环境下进行障碍物检测和环境地图构建的问题。现有方法，如视觉相机和激光雷达，在黑暗、烟雾或反射表面等环境中表现不佳，无法提供可靠的环境感知信息。这限制了移动机器人在这些场景中的应用，例如灾难救援、矿井勘探等。

**核心思路**：论文的核心思路是利用UWB雷达在恶劣环境下的鲁棒性，通过分析UWB信号的信道脉冲响应（CIR）来检测障碍物并构建环境地图。UWB雷达不受光照条件和烟雾的影响，能够穿透某些材料，提供可靠的距离和角度信息。通过设计合适的信号处理流程，可以有效降低噪声和多径效应，提高障碍物检测的准确性。

**技术框架**：该方法包含三个主要步骤：(1) 目标识别：基于CIR峰值检测识别潜在的障碍物目标。(2) 滤波：利用峰值属性（如幅度、宽度）、信噪比和到达相位差等信息，对检测到的目标进行滤波，去除噪声和多径干扰。(3) 聚类：基于距离估计和到达角估计，将滤波后的目标进行聚类，形成障碍物的空间分布。

**关键创新**：该方法的关键创新在于提出了一种针对移动机器人UWB雷达的信号处理流程，该流程能够有效降低噪声和多径效应，提高障碍物检测的精度和召回率。此外，该方法无需预先部署的锚节点，可以在动态、无基础设施的环境中进行环境地图构建，这与传统的UWB定位系统不同。

**关键设计**：在滤波阶段，论文使用了多种特征来区分真实目标和噪声/多径干扰，包括峰值幅度、峰值宽度、信噪比和到达相位差。聚类阶段使用了基于距离和角度的聚类算法，将空间上相邻的目标聚为一类。论文还研究了不同材料（金属、混凝土和胶合板）和UWB无线电信道（5和9）对CIR的影响，为参数选择提供了依据。

## 📊 实验亮点

实验结果表明，该方法在信道9上对包括低反射材料（如胶合板）在内的障碍物检测精度达到至少82.36%，召回率达到89.46%。这表明该方法能够有效降低噪声和多径效应，实现较高的障碍物检测性能。该方法无需预先部署的锚节点，可以在动态、无基础设施的环境中进行环境地图构建。

## 🎯 应用场景

该研究成果可应用于灾难救援、矿井勘探、智能仓储等视觉受限环境下的移动机器人导航与避障。通过UWB雷达构建的环境地图可以帮助机器人在复杂环境中安全可靠地移动，完成各种任务。未来，该技术有望与SLAM算法结合，实现更精确的定位和地图构建。

## 📄 摘要（原文）

> This paper presents an infrastructure-free approach for obstacle detection and environmental mapping using ultra-wideband (UWB) radar mounted on a mobile robotic platform. Traditional sensing modalities such as visual cameras and Light Detection and Ranging (LiDAR) fail in environments with poor visibility due to darkness, smoke, or reflective surfaces. In these visioned-impaired conditions, UWB radar offers a promising alternative. To this end, this work explores the suitability of robot-mounted UWB radar for environmental mapping in dynamic, anchor-free scenarios. The study investigates how different materials (metal, concrete and plywood) and UWB radio channels (5 and 9) influence the Channel Impulse Response (CIR). Furthermore, a processing pipeline is proposed to achieve reliable mapping of detected obstacles, consisting of 3 steps: (i) target identification (based on CIR peak detection), (ii) filtering (based on peak properties, signal-to-noise score, and phase-difference of arrival), and (iii) clustering (based on distance estimation and angle-of-arrival estimation). The proposed approach successfully reduces noise and multipath effects, resulting in an obstacle detection precision of at least 82.36% and a recall of 89.46% on channel 9 even when detecting low-reflective materials such as plywood. This work offers a foundation for further development of UWB-based localisation and mapping (SLAM) systems that do not rely on visual features and, unlike conventional UWB localisation systems, do not require on fixed anchor nodes for triangulation.

