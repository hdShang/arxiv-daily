---
layout: default
title: "MapAnything: Universal Feed-Forward Metric 3D Reconstruction"
---

# MapAnything: Universal Feed-Forward Metric 3D Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13414" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13414v2</a>
  <a href="https://arxiv.org/pdf/2509.13414.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13414v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13414v2', 'MapAnything: Universal Feed-Forward Metric 3D Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikhil Keetha, Norman Müller, Johannes Schönberger, Lorenzo Porzi, Yuchen Zhang, Tobias Fischer, Arno Knapitsch, Duncan Zauss, Ethan Weber, Nelson Antunes, Jonathon Luiten, Manuel Lopez-Antequera, Samuel Rota Bulò, Christian Richardt, Deva Ramanan, Sebastian Scherer, Peter Kontschieder

**分类**: cs.CV, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-09-16 (更新: 2025-09-18)

**备注**: Project Page: https://map-anything.github.io/

---

## 💡 一句话要点

**MapAnything：通用前馈式度量3D重建模型**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D重建` `Transformer网络` `多视图几何` `深度估计` `相机定位`

## 📋 核心要点

1. 现有3D重建方法通常针对特定任务设计，缺乏通用性和联合训练能力。
2. MapAnything采用基于Transformer的前馈网络，统一处理多种几何输入，直接回归度量3D场景。
3. 实验表明，MapAnything在多个3D视觉任务上表现优异，并支持更高效的联合训练。

## 📝 摘要（中文）

本文提出MapAnything，一个统一的基于Transformer的前馈模型，它接收单张或多张图像以及可选的几何输入（如相机内参、位姿、深度或部分重建），然后直接回归度量3D场景几何和相机。MapAnything利用多视图场景几何的分解表示，即深度图、局部光线图、相机位姿和度量比例因子集合，有效地将局部重建升级为全局一致的度量框架。通过标准化跨不同数据集的监督和训练，以及灵活的输入增强，MapAnything能够通过单个前馈过程解决广泛的3D视觉任务，包括未校准的运动结构恢复、校准的多视图立体、单目深度估计、相机定位、深度补全等。我们提供了广泛的实验分析和模型消融研究，表明MapAnything优于或匹配专门的前馈模型，同时提供更有效的联合训练行为，从而为通用3D重建骨干网络铺平了道路。

## 🔬 方法详解

**问题定义**：现有3D重建方法通常是针对特定任务设计的，例如，运动结构恢复、多视图立体、单目深度估计等，每种方法都有其特定的输入和输出格式，以及特定的损失函数。这导致了缺乏通用性，难以在不同任务之间共享知识和模型。此外，联合训练多种任务也变得困难，因为需要针对每种任务单独设计训练流程。

**核心思路**：MapAnything的核心思路是将各种3D重建任务统一到一个通用的前馈框架中。它通过使用一个基于Transformer的网络，能够处理多种类型的输入，包括图像、相机内参、位姿、深度等。同时，它采用一种分解的场景表示，将场景几何分解为深度图、局部光线图、相机位姿和度量比例因子，从而能够有效地将局部重建升级为全局一致的度量框架。

**技术框架**：MapAnything的整体架构包括一个输入编码器、一个Transformer网络和一个输出解码器。输入编码器负责将各种类型的输入转换为统一的特征表示。Transformer网络负责处理这些特征，并学习场景的几何结构。输出解码器负责将Transformer的输出解码为深度图、相机位姿等。整个流程是一个端到端的前馈过程。

**关键创新**：MapAnything最重要的技术创新在于其通用性和统一性。它能够处理多种类型的输入，并解决多种3D重建任务，而无需针对每种任务单独设计模型。这使得它能够更有效地利用数据，并学习更通用的场景表示。此外，它还采用了一种分解的场景表示，能够有效地将局部重建升级为全局一致的度量框架。

**关键设计**：MapAnything的关键设计包括：1) 使用Transformer网络来处理各种类型的输入；2) 采用分解的场景表示，将场景几何分解为深度图、局部光线图、相机位姿和度量比例因子；3) 设计合适的损失函数，以监督模型的训练。具体的网络结构和参数设置需要根据具体的任务进行调整。论文中对不同的任务使用了标准化的监督和训练方法，以及灵活的输入增强。

## 📊 实验亮点

实验结果表明，MapAnything在多个3D视觉任务上表现优异，包括未校准的运动结构恢复、校准的多视图立体、单目深度估计、相机定位、深度补全等。在某些任务上，MapAnything甚至超过了专门针对该任务设计的模型。此外，MapAnything还能够更有效地进行联合训练，从而进一步提高性能。

## 🎯 应用场景

MapAnything具有广泛的应用前景，例如，它可以用于自动驾驶、机器人导航、增强现实等领域。在自动驾驶中，它可以用于构建高精度的3D地图，从而提高车辆的感知能力。在机器人导航中，它可以用于估计机器人的位姿，并构建周围环境的3D模型。在增强现实中，它可以用于将虚拟物体与真实场景进行融合。

## 📄 摘要（原文）

> We introduce MapAnything, a unified transformer-based feed-forward model that ingests one or more images along with optional geometric inputs such as camera intrinsics, poses, depth, or partial reconstructions, and then directly regresses the metric 3D scene geometry and cameras. MapAnything leverages a factored representation of multi-view scene geometry, i.e., a collection of depth maps, local ray maps, camera poses, and a metric scale factor that effectively upgrades local reconstructions into a globally consistent metric frame. Standardizing the supervision and training across diverse datasets, along with flexible input augmentation, enables MapAnything to address a broad range of 3D vision tasks in a single feed-forward pass, including uncalibrated structure-from-motion, calibrated multi-view stereo, monocular depth estimation, camera localization, depth completion, and more. We provide extensive experimental analyses and model ablations demonstrating that MapAnything outperforms or matches specialist feed-forward models while offering more efficient joint training behavior, thus paving the way toward a universal 3D reconstruction backbone.

