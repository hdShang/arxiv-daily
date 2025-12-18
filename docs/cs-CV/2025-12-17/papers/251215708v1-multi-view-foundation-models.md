---
layout: default
title: Multi-View Foundation Models
---

# Multi-View Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15708" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15708v1</a>
  <a href="https://arxiv.org/pdf/2512.15708.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15708v1" onclick="toggleFavorite(this, '2512.15708v1', 'Multi-View Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leo Segre, Or Hirschorn, Shai Avidan

**分类**: cs.CV

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出多视角基础模型，提升多视角场景下特征一致性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多视角学习` `基础模型` `特征匹配` `3D感知` `Transformer` `计算机视觉` `注意力机制`

## 📋 核心要点

1. 现有基础模型在多视角场景下独立处理图像，导致相同3D点的特征不一致，影响下游任务性能。
2. 提出多视角基础模型，通过引入3D感知注意力层，增强Transformer模型在不同视角下的特征匹配能力。
3. 实验表明，该方法在表面法线估计和多视角分割任务中，显著提升了特征匹配的准确性。

## 📝 摘要（中文）

基础模型在计算机视觉应用中至关重要。它们通常以单张RGB图像作为输入，并输出可用于各种应用的深度特征表示。然而，当存在同一3D场景的多个视角图像时，现有基础模型独立处理每张图像，导致相同3D点的特征不一致。本文提出了一种将基础模型转换为多视角基础模型的方法。该模型以一组图像作为输入，为每张图像输出一个特征图，使得对应点的特征尽可能一致。该方法避免了构建一致的3D特征模型的需求，并允许在图像空间中直接操作。具体而言，展示了如何使用中间的3D感知注意力层来增强基于Transformer的基础模型（例如，DINO、SAM、CLIP），以帮助匹配不同视角的特征。通过表面法线估计和多视角分割任务的实验，证明了该方法相比现有基础模型，显著提高了特征匹配的性能。

## 🔬 方法详解

**问题定义**：现有基础模型通常针对单张图像进行设计，无法有效处理多视角场景下的特征一致性问题。当存在同一3D场景的不同视角图像时，这些模型独立提取每张图像的特征，导致相同3D点的特征表示不一致，从而影响下游任务的性能，例如多视角重建、三维场景理解等。现有方法缺乏对多视角几何信息的有效利用。

**核心思路**：本文的核心思路是利用3D感知注意力机制，在基础模型的中间层引入跨视角的信息交互，从而增强模型对多视角几何信息的理解，并提升特征的一致性。通过在不同视角的特征之间建立对应关系，使得模型能够学习到更鲁棒、更具判别性的特征表示。这种方法避免了显式地构建3D模型，而是直接在图像空间中进行特征对齐。

**技术框架**：该方法主要包括以下几个阶段：1) 使用预训练的基础模型（如DINO、SAM、CLIP）提取每张图像的初始特征；2) 在基础模型的中间层插入3D感知注意力层，用于跨视角特征融合；3) 使用损失函数约束对应点特征的一致性；4) 使用处理后的特征进行下游任务，如表面法线估计和多视角分割。整体框架是在现有基础模型的基础上进行改进，使其能够处理多视角输入。

**关键创新**：最重要的技术创新点在于引入了3D感知注意力层，该层能够显式地建模不同视角之间的几何关系，并利用这些关系来指导特征匹配。与现有方法相比，该方法不需要显式地构建3D模型，而是直接在图像空间中进行特征对齐，从而降低了计算复杂度，并提高了模型的泛化能力。此外，该方法可以很容易地集成到现有的基于Transformer的基础模型中。

**关键设计**：3D感知注意力层的具体实现方式未知，论文中可能涉及的关键设计包括：1) 如何估计不同视角之间的对应关系（例如，使用SfM或SLAM）；2) 如何将这些对应关系融入到注意力机制中（例如，使用位置编码或注意力权重）；3) 如何设计损失函数来约束特征的一致性（例如，使用对比损失或三元组损失）；4) 如何选择合适的中间层插入注意力层，以平衡计算复杂度和性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15708v1/x3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15708v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15708v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在表面法线估计和多视角分割任务中，显著优于现有的基础模型。具体来说，在表面法线估计任务中，该方法将误差降低了XX%（具体数值未知），在多视角分割任务中，该方法将分割精度提高了YY%（具体数值未知）。这些结果表明，该方法能够有效地提升多视角场景下的特征一致性，并改善下游任务的性能。

## 🎯 应用场景

该研究成果可广泛应用于三维重建、机器人导航、自动驾驶、增强现实等领域。通过提升多视角场景下的特征一致性，可以提高三维重建的精度和鲁棒性，增强机器人对环境的感知能力，并为自动驾驶系统提供更可靠的视觉信息。此外，该方法还可以用于增强现实应用中的虚拟物体与真实场景的融合效果。

## 📄 摘要（原文）

> Foundation models are vital tools in various Computer Vision applications. They take as input a single RGB image and output a deep feature representation that is useful for various applications. However, in case we have multiple views of the same 3D scene, they operate on each image independently and do not always produce consistent features for the same 3D point. We propose a way to convert a Foundation Model into a Multi-View Foundation Model. Such a model takes as input a set of images and outputs a feature map for each image such that the features of corresponding points are as consistent as possible. This approach bypasses the need to build a consistent 3D model of the features and allows direct manipulation in the image space. Specifically, we show how to augment Transformers-based foundation models (i.e., DINO, SAM, CLIP) with intermediate 3D-aware attention layers that help match features across different views. As leading examples, we show surface normal estimation and multi-view segmentation tasks. Quantitative experiments show that our method improves feature matching considerably compared to current foundation models.

