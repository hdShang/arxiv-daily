---
layout: default
title: SyncHuman: Synchronizing 2D and 3D Generative Models for Single-view Human Reconstruction
---

# SyncHuman: Synchronizing 2D and 3D Generative Models for Single-view Human Reconstruction

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07723" target="_blank" class="toolbar-btn">arXiv: 2510.07723v2</a>
    <a href="https://arxiv.org/pdf/2510.07723.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07723v2" 
            onclick="toggleFavorite(this, '2510.07723v2', 'SyncHuman: Synchronizing 2D and 3D Generative Models for Single-view Human Reconstruction')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Wenyue Chen, Peng Li, Wangguandong Zheng, Chengfeng Zhao, Mengfei Li, Yaolong Zhu, Zhiyang Dou, Ronggang Wang, Yuan Liu

**分类**: cs.CV

**发布日期**: 2025-10-09 (更新: 2025-10-13)

**备注**: NeurIPS 2025 https://xishuxishu.github.io/SyncHuman.github.io/

---

## 💡 一句话要点

**SyncHuman：同步2D和3D生成模型，实现单视角人体重建**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `单视角重建` `3D人体建模` `生成模型` `多视角学习` `几何对齐`

## 📋 核心要点

1. 现有单视角人体重建方法依赖SMPL模型，但SMPL先验不准确，难以处理复杂姿势和精细细节。
2. SyncHuman结合2D多视角和3D原生生成模型，利用各自优势，实现几何对齐和细节增强。
3. 实验表明，SyncHuman在复杂姿势下实现了鲁棒且逼真的3D人体重建，优于现有方法。

## 📝 摘要（中文）

从单张图像进行逼真的3D全身人体重建是一项关键但具有挑战性的任务，由于固有的歧义性和严重的自遮挡，该技术在电影和视频游戏等应用中至关重要。现有方法利用SMPL估计和SMPL条件图像生成模型来生成新视角，但它们受到SMPL网格估计的不准确3D先验的限制，并且难以处理复杂的人体姿势和重建精细的细节。本文提出了一种新颖的框架SyncHuman，它首次结合了2D多视角生成模型和3D原生生成模型，即使在具有挑战性的人体姿势下，也能从单视角图像中实现高质量的服装人体网格重建。多视角生成模型擅长捕捉精细的2D细节，但在结构一致性方面存在困难，而3D原生生成模型生成粗糙但结构一致的3D形状。通过整合这两种方法的互补优势，我们开发了一个更有效的生成框架。具体来说，我们首先使用提出的像素对齐的2D-3D同步注意力联合微调多视角生成模型和3D原生生成模型，以生成几何对齐的3D形状和2D多视角图像。为了进一步提高细节，我们引入了一种特征注入机制，将精细的细节从2D多视角图像提升到对齐的3D形状上，从而实现准确和高保真的重建。大量的实验表明，SyncHuman实现了鲁棒和逼真的3D人体重建，即使对于具有挑战性姿势的图像也是如此。我们的方法在几何精度和视觉保真度方面优于基线方法，为未来的3D生成模型展示了一个有希望的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像中高质量、高逼真度地重建3D人体的问题。现有方法，特别是基于SMPL模型的方法，在处理复杂姿势、自遮挡以及捕捉精细细节方面存在局限性。SMPL模型提供的3D先验不够准确，导致重建结果在几何结构和视觉效果上都存在不足。

**核心思路**：论文的核心思路是结合2D多视角生成模型和3D原生生成模型的优势。2D多视角生成模型擅长捕捉图像的精细纹理和细节，但缺乏结构一致性；而3D原生生成模型能够生成结构一致的3D形状，但细节较为粗糙。通过将两者结合，可以实现优势互补，从而生成既具有精细细节又具有良好结构一致性的3D人体模型。

**技术框架**：SyncHuman框架主要包含两个阶段：联合微调阶段和特征注入阶段。在联合微调阶段，多视角生成模型和3D原生生成模型通过像素对齐的2D-3D同步注意力机制进行联合训练，以确保生成的3D形状和2D多视角图像在几何上对齐。在特征注入阶段，从2D多视角图像中提取的精细细节特征被注入到对齐的3D形状中，以增强重建结果的细节表现。

**关键创新**：该论文的关键创新在于首次将2D多视角生成模型和3D原生生成模型结合用于单视角人体重建。提出的像素对齐的2D-3D同步注意力机制是另一个创新点，它能够有效地将2D图像信息和3D形状信息对齐，从而实现更好的重建效果。此外，特征注入机制也能够有效地将2D图像的细节信息传递到3D模型中。

**关键设计**：像素对齐的2D-3D同步注意力机制是关键设计之一，它通过注意力机制学习2D图像像素和3D形状顶点之间的对应关系，从而实现几何对齐。特征注入机制的具体实现方式（例如，使用哪种类型的神经网络层进行特征融合）也是一个关键设计。损失函数的设计也至关重要，需要平衡几何精度、视觉保真度和结构一致性。

## 📊 实验亮点

实验结果表明，SyncHuman在几何精度和视觉保真度方面均优于现有方法。具体而言，SyncHuman在具有挑战性姿势的图像上也能实现鲁棒的重建效果，并且能够生成更精细的3D人体模型。论文中提供了与多个基线方法的定量和定性比较，展示了SyncHuman的优越性。

## 🎯 应用场景

SyncHuman技术在电影、视频游戏、虚拟现实、增强现实等领域具有广泛的应用前景。它可以用于创建逼真的3D虚拟角色，实现虚拟试衣、远程协作等功能。该技术还可以应用于人体姿态估计、动作捕捉等领域，为相关应用提供更准确的3D人体模型。

## 📄 摘要（原文）

> Photorealistic 3D full-body human reconstruction from a single image is a critical yet challenging task for applications in films and video games due to inherent ambiguities and severe self-occlusions. While recent approaches leverage SMPL estimation and SMPL-conditioned image generative models to hallucinate novel views, they suffer from inaccurate 3D priors estimated from SMPL meshes and have difficulty in handling difficult human poses and reconstructing fine details. In this paper, we propose SyncHuman, a novel framework that combines 2D multiview generative model and 3D native generative model for the first time, enabling high-quality clothed human mesh reconstruction from single-view images even under challenging human poses. Multiview generative model excels at capturing fine 2D details but struggles with structural consistency, whereas 3D native generative model generates coarse yet structurally consistent 3D shapes. By integrating the complementary strengths of these two approaches, we develop a more effective generation framework. Specifically, we first jointly fine-tune the multiview generative model and the 3D native generative model with proposed pixel-aligned 2D-3D synchronization attention to produce geometrically aligned 3D shapes and 2D multiview images. To further improve details, we introduce a feature injection mechanism that lifts fine details from 2D multiview images onto the aligned 3D shapes, enabling accurate and high-fidelity reconstruction. Extensive experiments demonstrate that SyncHuman achieves robust and photo-realistic 3D human reconstruction, even for images with challenging poses. Our method outperforms baseline methods in geometric accuracy and visual fidelity, demonstrating a promising direction for future 3D generation models.

