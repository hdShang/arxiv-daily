---
layout: default
title: "Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments"
---

# Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05965" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05965v1</a>
  <a href="https://arxiv.org/pdf/2506.05965.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05965v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05965v1', 'Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingrui Li, Yiming Zhou, Hongxing Zhou, Xinggang Hu, Florian Roemer, Hongyu Wang, Ahmad Osman

**分类**: cs.CV

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出Dy3DGS-SLAM以解决动态环境下单目SLAM问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态SLAM` `单目视觉` `3D高斯点云` `神经辐射场` `光流掩码` `姿态估计` `实时定位` `地图构建`

## 📋 核心要点

1. 现有SLAM方法在动态环境下的跟踪和重建能力不足，尤其是依赖RGB-D输入的方案较少适用于单目RGB输入。
2. Dy3DGS-SLAM通过融合光流和深度掩码，提出了一种新的动态掩码生成方法，并设计了运动损失以改进姿态估计。
3. 实验结果显示，Dy3DGS-SLAM在动态场景中的跟踪和渲染性能优于现有RGB-D方法，展现出显著的提升。

## 📝 摘要（中文）

当前基于神经辐射场（NeRF）或3D高斯点云的同时定位与地图构建（SLAM）方法在重建静态3D场景方面表现优异，但在动态环境中（如具有移动元素的真实场景）的跟踪和重建能力较弱。现有的NeRF基础SLAM方法通常依赖RGB-D输入，纯RGB输入的适应性较少。为克服这些限制，本文提出了Dy3DGS-SLAM，这是首个使用单目RGB输入的动态场景3D高斯点云SLAM方法。通过融合光流掩码和深度掩码，获得融合动态掩码，并设计了新的运动损失以约束姿态估计网络。实验结果表明，Dy3DGS-SLAM在动态环境中的跟踪和渲染性能达到了最先进水平，超越或匹配了现有的RGB-D方法。

## 🔬 方法详解

**问题定义**：本文旨在解决动态环境下单目SLAM的跟踪和重建问题，现有方法在处理动态元素时面临显著挑战，尤其是依赖RGB-D输入的方案。

**核心思路**：Dy3DGS-SLAM通过融合光流掩码和深度掩码，生成一个融合动态掩码，以此来约束跟踪尺度并优化渲染几何。

**技术框架**：该方法包括动态掩码生成、姿态估计网络和动态像素渲染等主要模块。首先生成动态掩码，然后通过运动损失约束姿态估计，最后进行动态像素的渲染。

**关键创新**：Dy3DGS-SLAM的核心创新在于首次将3D高斯点云SLAM应用于动态场景，并使用单目RGB输入，显著提升了动态环境下的SLAM性能。

**关键设计**：在设计中，采用了融合光流和深度掩码的概率模型，并引入了新的运动损失函数，以优化姿态估计网络的输出。

## 📊 实验亮点

实验结果表明，Dy3DGS-SLAM在动态环境中的跟踪和渲染性能达到了最先进水平，超越或匹配了现有RGB-D方法，具体性能提升幅度未知，显示出其在动态场景处理中的优越性。

## 🎯 应用场景

Dy3DGS-SLAM的潜在应用场景包括自动驾驶、机器人导航和增强现实等领域，能够在动态环境中实现高效的实时定位与地图构建。这一研究的实际价值在于提升了SLAM技术在复杂场景中的适应性和准确性，未来可能推动相关技术的广泛应用。

## 📄 摘要（原文）

> Current Simultaneous Localization and Mapping (SLAM) methods based on Neural Radiance Fields (NeRF) or 3D Gaussian Splatting excel in reconstructing static 3D scenes but struggle with tracking and reconstruction in dynamic environments, such as real-world scenes with moving elements. Existing NeRF-based SLAM approaches addressing dynamic challenges typically rely on RGB-D inputs, with few methods accommodating pure RGB input. To overcome these limitations, we propose Dy3DGS-SLAM, the first 3D Gaussian Splatting (3DGS) SLAM method for dynamic scenes using monocular RGB input. To address dynamic interference, we fuse optical flow masks and depth masks through a probabilistic model to obtain a fused dynamic mask. With only a single network iteration, this can constrain tracking scales and refine rendered geometry. Based on the fused dynamic mask, we designed a novel motion loss to constrain the pose estimation network for tracking. In mapping, we use the rendering loss of dynamic pixels, color, and depth to eliminate transient interference and occlusion caused by dynamic objects. Experimental results demonstrate that Dy3DGS-SLAM achieves state-of-the-art tracking and rendering in dynamic environments, outperforming or matching existing RGB-D methods.

