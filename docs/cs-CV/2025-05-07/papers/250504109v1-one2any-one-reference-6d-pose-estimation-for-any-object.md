---
layout: default
title: "One2Any: One-Reference 6D Pose Estimation for Any Object"
---

# One2Any: One-Reference 6D Pose Estimation for Any Object

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04109" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04109v1</a>
  <a href="https://arxiv.org/pdf/2505.04109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04109v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04109v1', 'One2Any: One-Reference 6D Pose Estimation for Any Object')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengya Liu, Siyuan Li, Ajad Chhatkuli, Prune Truong, Luc Van Gool, Federico Tombari

**分类**: cs.CV

**发布日期**: 2025-05-07

**备注**: accepted by CVPR 2025

**期刊**: CVPR 2025

---

## 💡 一句话要点

**提出One2Any以解决6D物体姿态估计的模型依赖问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `6D姿态估计` `物体识别` `深度学习` `计算机视觉` `机器人技术`

## 📋 核心要点

1. 现有的6D物体姿态估计方法依赖于完整的3D模型和多视角图像，限制了其在新物体上的应用。
2. 本文提出的One2Any方法通过单个RGB-D图像进行姿态估计，避免了对3D模型和多视角数据的依赖。
3. 实验结果显示，该方法在多个基准数据集上实现了最先进的性能，且计算效率显著提升。

## 📝 摘要（中文）

6D物体姿态估计在许多应用中仍然具有挑战性，主要由于对完整3D模型、多视角图像的依赖，以及训练限制于特定物体类别。这些要求使得对新颖物体的泛化变得困难。为了解决这一问题，本文提出了一种新方法One2Any，该方法仅使用单个参考-查询RGB-D图像来估计相对6自由度物体姿态，而无需先验的3D模型、多视角数据或类别约束。我们将物体姿态估计视为编码-解码过程，首先从单个参考视图中获取全面的参考物体姿态嵌入（ROPE），该嵌入编码了物体的形状、方向和纹理。利用这一嵌入，基于U-Net的姿态解码模块为新视图生成参考物体坐标（ROC），从而实现快速而准确的姿态估计。该简单的编码-解码框架使我们的模型能够在任意成对姿态数据上进行训练，展示了良好的可扩展性。实验结果表明，我们的模型在多个基准数据集上对新颖物体具有良好的泛化能力，达到了最先进的准确性和鲁棒性，甚至与需要多视角或CAD输入的方法相媲美，同时计算成本大幅降低。

## 🔬 方法详解

**问题定义**：本文旨在解决6D物体姿态估计中对完整3D模型和多视角图像的依赖问题。现有方法在处理新物体时面临泛化困难，限制了其应用范围。

**核心思路**：One2Any方法通过单个参考RGB-D图像进行姿态估计，将物体姿态估计视为编码-解码过程。通过提取参考物体姿态嵌入（ROPE），该方法能够在没有3D模型的情况下进行有效的姿态推断。

**技术框架**：该方法的整体架构包括两个主要模块：首先是参考物体姿态嵌入模块，通过单个视图提取物体的形状、方向和纹理信息；其次是基于U-Net的姿态解码模块，利用ROPE为新视图生成参考物体坐标（ROC）。

**关键创新**：One2Any的核心创新在于其能够在没有3D模型和多视角数据的情况下，仅依赖单个图像进行高效的6D姿态估计。这一方法显著提升了模型的泛化能力和计算效率。

**关键设计**：在模型设计中，采用了U-Net结构作为解码模块，损失函数设计为适应成对姿态数据的训练，确保了模型在大规模数据集上的训练效果。

## 📊 实验亮点

实验结果表明，One2Any在多个基准数据集上实现了最先进的准确性，尤其在处理新颖物体时表现出色。与传统方法相比，该方法在计算资源消耗上大幅降低，展现出良好的可扩展性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、增强现实和自动驾驶等场景，能够在缺乏3D模型的情况下实现高效的物体识别与定位。未来，该方法可能推动更多领域的智能化进程，提升物体交互的智能水平。

## 📄 摘要（原文）

> 6D object pose estimation remains challenging for many applications due to dependencies on complete 3D models, multi-view images, or training limited to specific object categories. These requirements make generalization to novel objects difficult for which neither 3D models nor multi-view images may be available. To address this, we propose a novel method One2Any that estimates the relative 6-degrees of freedom (DOF) object pose using only a single reference-single query RGB-D image, without prior knowledge of its 3D model, multi-view data, or category constraints. We treat object pose estimation as an encoding-decoding process, first, we obtain a comprehensive Reference Object Pose Embedding (ROPE) that encodes an object shape, orientation, and texture from a single reference view. Using this embedding, a U-Net-based pose decoding module produces Reference Object Coordinate (ROC) for new views, enabling fast and accurate pose estimation. This simple encoding-decoding framework allows our model to be trained on any pair-wise pose data, enabling large-scale training and demonstrating great scalability. Experiments on multiple benchmark datasets demonstrate that our model generalizes well to novel objects, achieving state-of-the-art accuracy and robustness even rivaling methods that require multi-view or CAD inputs, at a fraction of compute.

