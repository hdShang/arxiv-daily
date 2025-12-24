---
layout: default
title: "i2Nav-Robot: A Large-Scale Indoor-Outdoor Robot Dataset for Multi-Sensor Fusion Navigation and Mapping"
---

# i2Nav-Robot: A Large-Scale Indoor-Outdoor Robot Dataset for Multi-Sensor Fusion Navigation and Mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11485" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11485v2</a>
  <a href="https://arxiv.org/pdf/2508.11485.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11485v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11485v2', 'i2Nav-Robot: A Large-Scale Indoor-Outdoor Robot Dataset for Multi-Sensor Fusion Navigation and Mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hailiang Tang, Tisheng Zhang, Liqiang Wang, Xin Ding, Man Yuan, Zhiyu Xiang, Jujin Chen, Yuhan Bian, Shuangyan Liu, Yuqing Wang, Guan Wang, Xiaoji Niu

**分类**: cs.RO

**发布日期**: 2025-08-15 (更新: 2025-08-27)

**备注**: 10 pages, 12 figures

---

## 💡 一句话要点

**提出i2Nav-Robot数据集以解决UGV导航与映射的多传感器融合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多传感器融合` `无人驾驶` `数据集` `导航与映射` `激光雷达` `室内外环境` `高精度定位`

## 📋 核心要点

1. 现有UGV数据集在传感器配置和场景多样性方面存在不足，限制了导航和映射技术的进步。
2. 本文提出i2Nav-Robot数据集，集成多种传感器并实现高精度时间同步，以支持多传感器融合导航。
3. i2Nav-Robot数据集经过多个系统评估，显示出优越的数据质量，能够有效提升导航精度和可靠性。

## 📝 摘要（中文）

准确可靠的导航对于自主无人地面车辆（UGV）至关重要。然而，现有UGV数据集在传感器配置、时间同步、真实值和场景多样性等方面存在不足。为了解决这些挑战，本文提出了i2Nav-Robot，这是一个为室内外环境中的多传感器融合导航和映射而设计的大规模数据集。该数据集整合了最新的前视和360度固态激光雷达、四维雷达、立体相机、里程计、全球导航卫星系统（GNSS）接收器和惯性测量单元（IMU）。通过在线硬件同步和离线校准获得准确的时间戳，数据集包含十个大规模序列，覆盖多样的UGV操作场景，总长度约为17060米。高频真实值通过后处理集成导航方法获得，位置精度达到厘米级。i2Nav-Robot数据集经过十多个开源多传感器融合系统的评估，证明其数据质量优越。

## 🔬 方法详解

**问题定义**：本文旨在解决现有UGV数据集在传感器配置、时间同步和场景多样性等方面的不足，以满足多传感器融合导航和映射的需求。

**核心思路**：通过构建一个集成多种传感器的大规模数据集，提供高频、准确的时间戳和真实值，支持更为精确的导航和映射技术。

**技术框架**：数据集由多个模块组成，包括前视和360度激光雷达、四维雷达、立体相机、里程计、GNSS接收器和IMU，所有传感器通过在线同步和离线校准确保时间一致性。

**关键创新**：i2Nav-Robot数据集的创新在于其多模态传感器的集成和高精度的时间同步，显著提升了数据的准确性和可靠性，与现有数据集相比具有明显优势。

**关键设计**：数据集的设计包括高频采样和厘米级位置精度的真实值生成，采用导航级IMU进行后处理集成导航，确保数据的高质量和适用性。

## 📊 实验亮点

实验结果显示，i2Nav-Robot数据集在超过十个开源多传感器融合系统中表现出色，数据质量显著优于现有数据集，尤其在导航精度上实现了厘米级的提升，验证了其在实际应用中的有效性。

## 🎯 应用场景

i2Nav-Robot数据集具有广泛的应用潜力，特别是在自主驾驶、机器人导航和智能交通系统等领域。其高质量的数据支持研究人员和工程师开发更为先进的导航算法和系统，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Accurate and reliable navigation is crucial for autonomous unmanned ground vehicle (UGV). However, current UGV datasets fall short in meeting the demands for advancing navigation and mapping techniques due to limitations in sensor configuration, time synchronization, ground truth, and scenario diversity. To address these challenges, we present i2Nav-Robot, a large-scale dataset designed for multi-sensor fusion navigation and mapping in indoor-outdoor environments. We integrate multi-modal sensors, including the newest front-view and 360-degree solid-state LiDARs, 4-dimensional (4D) radar, stereo cameras, odometer, global navigation satellite system (GNSS) receiver, and inertial measurement units (IMU) on an omnidirectional wheeled robot. Accurate timestamps are obtained through both online hardware synchronization and offline calibration for all sensors. The dataset includes ten larger-scale sequences covering diverse UGV operating scenarios, such as outdoor streets, and indoor parking lots, with a total length of about 17060 meters. High-frequency ground truth, with centimeter-level accuracy for position, is derived from post-processing integrated navigation methods using a navigation-grade IMU. The proposed i2Nav-Robot dataset is evaluated by more than ten open-sourced multi-sensor fusion systems, and it has proven to have superior data quality.

