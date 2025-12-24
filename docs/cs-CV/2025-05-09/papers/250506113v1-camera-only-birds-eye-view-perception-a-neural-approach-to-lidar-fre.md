---
layout: default
title: "Camera-Only Bird's Eye View Perception: A Neural Approach to LiDAR-Free Environmental Mapping for Autonomous Vehicles"
---

# Camera-Only Bird's Eye View Perception: A Neural Approach to LiDAR-Free Environmental Mapping for Autonomous Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06113" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06113v1</a>
  <a href="https://arxiv.org/pdf/2505.06113.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06113v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06113v1', 'Camera-Only Bird\'s Eye View Perception: A Neural Approach to LiDAR-Free Environmental Mapping for Autonomous Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anupkumar Bochare

**分类**: cs.CV

**发布日期**: 2025-05-09

---

## 💡 一句话要点

**提出基于相机的鸟瞰视图感知框架以解决激光雷达依赖问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `自主驾驶` `鸟瞰视图` `深度学习` `目标检测` `环境感知` `多相机系统` `激光雷达替代`

## 📋 核心要点

1. 现有的自主车辆感知系统通常依赖昂贵的激光雷达传感器，导致成本高昂且难以普及。
2. 本文提出了一种基于相机的感知框架，结合YOLOv11目标检测和单目深度估计，实现鸟瞰视图地图生成。
3. 在OpenLane-V2和NuScenes数据集上，我们的方法在道路分割和车辆检测方面表现优异，验证了其有效性。

## 📝 摘要（中文）

自主车辆感知系统传统上依赖昂贵的激光雷达传感器来生成精确的环境表示。本文提出了一种仅基于相机的感知框架，通过扩展Lift-Splat-Shoot架构生成鸟瞰视图（BEV）地图。我们的方法结合了基于YOLOv11的目标检测和DepthAnythingV2单目深度估计，利用多相机输入实现全面的360度场景理解。在OpenLane-V2和NuScenes数据集上的评估结果显示，与激光雷达的真实数据相比，我们的方法在道路分割准确率上达到85%，车辆检测率在85-90%之间，平均位置误差限制在1.2米。这些结果突显了深度学习在仅使用相机输入提取丰富空间信息方面的潜力，从而实现了成本效益高的自主导航而不牺牲准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决自主车辆感知系统对激光雷达的依赖问题，现有方法在成本和普及性上存在明显不足。

**核心思路**：我们提出了一种仅依赖相机的感知框架，通过结合YOLOv11进行目标检测和DepthAnythingV2进行深度估计，来生成鸟瞰视图地图，从而实现全面的环境理解。

**技术框架**：整体架构包括多个模块，首先通过多相机输入获取图像数据，然后利用YOLOv11进行目标检测，接着应用DepthAnythingV2进行深度估计，最后将这些信息整合生成鸟瞰视图。

**关键创新**：最重要的创新在于将YOLOv11与单目深度估计相结合，突破了传统方法对激光雷达的依赖，实现了高效的环境感知。

**关键设计**：在网络结构上，我们优化了YOLOv11的参数设置，并设计了适应于多相机输入的损失函数，以提高目标检测和深度估计的准确性。通过这些设计，我们的模型在准确性和效率上均有显著提升。

## 📊 实验亮点

实验结果显示，我们的方法在OpenLane-V2和NuScenes数据集上达到了85%的道路分割准确率和85-90%的车辆检测率，平均位置误差仅为1.2米。这些结果表明，基于相机的感知框架在准确性上与激光雷达方法相当，具有较高的实用价值。

## 🎯 应用场景

该研究的潜在应用领域包括自主驾驶、智能交通系统和机器人导航等。通过降低对激光雷达的依赖，能够显著降低成本，提高系统的可普及性，推动自主车辆技术的广泛应用。未来，该方法可能在复杂环境下的实时感知中发挥重要作用。

## 📄 摘要（原文）

> Autonomous vehicle perception systems have traditionally relied on costly LiDAR sensors to generate precise environmental representations. In this paper, we propose a camera-only perception framework that produces Bird's Eye View (BEV) maps by extending the Lift-Splat-Shoot architecture. Our method combines YOLOv11-based object detection with DepthAnythingV2 monocular depth estimation across multi-camera inputs to achieve comprehensive 360-degree scene understanding. We evaluate our approach on the OpenLane-V2 and NuScenes datasets, achieving up to 85% road segmentation accuracy and 85-90% vehicle detection rates when compared against LiDAR ground truth, with average positional errors limited to 1.2 meters. These results highlight the potential of deep learning to extract rich spatial information using only camera inputs, enabling cost-efficient autonomous navigation without sacrificing accuracy.

