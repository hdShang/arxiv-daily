---
layout: default
title: PALMS+: Modular Image-Based Floor Plan Localization Leveraging Depth Foundation Model
---

# PALMS+: Modular Image-Based Floor Plan Localization Leveraging Depth Foundation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09724" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09724v1</a>
  <a href="https://arxiv.org/pdf/2511.09724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09724v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.09724v1', 'PALMS+: Modular Image-Based Floor Plan Localization Leveraging Depth Foundation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunqian Cheng, Benjamin Princen, Roberto Manduchi

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-11-12

**备注**: Accepted to IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) 2026, Application Track. Main paper: 8 pages, 5 figures. Supplementary material included

**🔗 代码/项目**: [GITHUB](https://github.com/Head-inthe-Cloud/PALMS-Plane-based-Accessible-Indoor-Localization-Using-Mobile-Smartphones)

---

## 💡 一句话要点

**提出PALMS+以解决室内定位精度不足问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `室内定位` `深度估计` `图像处理` `模块化系统` `无基础设施导航` `机器人导航` `紧急响应`

## 📋 核心要点

1. 现有的室内定位方法在GPS缺失环境中面临短距离和布局模糊性等挑战，影响定位精度。
2. PALMS+通过重建3D点云并与平面图进行几何匹配，提供了一种新的模块化图像定位方案。
3. 在多个数据集上，PALMS+在静态定位精度上超越了现有方法，且在顺序定位中表现出更低的误差。

## 📝 摘要（中文）

在GPS信号缺失的环境中，室内定位对于紧急响应和辅助导航等应用至关重要。现有的基于视觉的方法如PALMS，虽然能够利用平面图和静态扫描实现基础定位，但受到智能手机LiDAR短距离和室内布局模糊性的限制。本文提出PALMS+，一个模块化的基于图像的系统，通过使用基础单目深度估计模型（Depth Pro）从姿态RGB图像重建尺度对齐的3D点云，随后通过与平面图的卷积进行几何布局匹配。PALMS+输出位置和方向的后验分布，适用于直接或顺序定位。在Structured3D和一个包含80个观测的自定义校园数据集上进行评估，PALMS+在静态定位精度上超越了PALMS和F3Loc，且无需任何训练。此外，当与粒子滤波器结合用于33条真实世界轨迹的顺序定位时，PALMS+实现了更低的定位误差，展示了其在无基础设施跟踪中的鲁棒性及潜在应用价值。

## 🔬 方法详解

**问题定义**：本文旨在解决在GPS信号缺失的室内环境中，现有视觉定位方法因短距离和布局模糊性导致的定位精度不足的问题。

**核心思路**：PALMS+通过利用基础单目深度估计模型，从RGB图像中重建尺度对齐的3D点云，并与平面图进行几何匹配，从而提高定位精度。

**技术框架**：PALMS+的整体架构包括两个主要模块：首先是使用Depth Pro模型从RGB图像生成3D点云，其次是通过卷积操作与平面图进行几何匹配，最终输出位置和方向的后验分布。

**关键创新**：PALMS+的核心创新在于其模块化设计和深度估计模型的应用，使得系统在无需训练的情况下，能够在多种环境中实现高精度定位。

**关键设计**：在技术细节上，PALMS+采用了特定的参数设置以优化点云重建过程，并设计了适合于室内环境的损失函数，以提高几何匹配的准确性。通过这些设计，系统能够有效应对复杂的室内布局。

## 📊 实验亮点

PALMS+在Structured3D和自定义校园数据集上表现出色，静态定位精度超越PALMS和F3Loc，且无需任何训练。在与粒子滤波器结合的顺序定位实验中，PALMS+在33条真实世界轨迹上实现了更低的定位误差，显示出其在实际应用中的鲁棒性。

## 🎯 应用场景

PALMS+的研究成果在紧急响应、辅助导航和智能建筑管理等领域具有广泛的应用潜力。其基础设施无关的特性使得在复杂环境中进行实时定位成为可能，未来可进一步拓展至无人驾驶、机器人导航等场景，提升操作效率和安全性。

## 📄 摘要（原文）

> Indoor localization in GPS-denied environments is crucial for applications like emergency response and assistive navigation. Vision-based methods such as PALMS enable infrastructure-free localization using only a floor plan and a stationary scan, but are limited by the short range of smartphone LiDAR and ambiguity in indoor layouts. We propose PALMS$+$, a modular, image-based system that addresses these challenges by reconstructing scale-aligned 3D point clouds from posed RGB images using a foundation monocular depth estimation model (Depth Pro), followed by geometric layout matching via convolution with the floor plan. PALMS$+$ outputs a posterior over the location and orientation, usable for direct or sequential localization. Evaluated on the Structured3D and a custom campus dataset consisting of 80 observations across four large campus buildings, PALMS$+$ outperforms PALMS and F3Loc in stationary localization accuracy -- without requiring any training. Furthermore, when integrated with a particle filter for sequential localization on 33 real-world trajectories, PALMS$+$ achieved lower localization errors compared to other methods, demonstrating robustness for camera-free tracking and its potential for infrastructure-free applications. Code and data are available at https://github.com/Head-inthe-Cloud/PALMS-Plane-based-Accessible-Indoor-Localization-Using-Mobile-Smartphones

