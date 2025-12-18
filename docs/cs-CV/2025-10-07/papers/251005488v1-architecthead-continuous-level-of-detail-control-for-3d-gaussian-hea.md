---
layout: default
title: ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head Avatars
---

# ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head Avatars

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05488" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05488v1</a>
  <a href="https://arxiv.org/pdf/2510.05488.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05488v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.05488v1', 'ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head Avatars')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du

**分类**: cs.CV

**发布日期**: 2025-10-07

---

## 💡 一句话要点

**ArchitectHead：提出首个支持连续细节层次控制的3D高斯头部头像框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `头部头像` `细节层次控制` `UV特征场` `神经渲染`

## 📋 核心要点

1. 现有基于3D高斯溅射的头像通常依赖数万个高斯点，训练后数量固定，无法根据需求调整细节层次。
2. ArchitectHead将高斯参数化到UV特征空间，通过UV特征场和轻量级解码器实现高斯属性的动态生成和LOD控制。
3. 实验表明，该方法在最高LOD下达到SOTA质量，在较低LOD下保持接近SOTA性能，并显著提升渲染速度。

## 📝 摘要（中文）

本文提出名为“ArchitectHead”的框架，用于创建支持连续细节层次（LOD）控制的3D高斯头部头像，这是首个此类框架。核心思想是将高斯参数化到2D UV特征空间中，并提出由多层可学习特征图组成的UV特征场来编码其潜在特征。轻量级的神经网络解码器将这些潜在特征转换为用于渲染的3D高斯属性。ArchitectHead通过动态重采样UV特征场中所需分辨率的特征图来控制高斯数量，从而实现高效且连续的LOD控制，无需重新训练。实验结果表明，ArchitectHead在最高LOD下实现了自重演和跨身份重演任务中最先进的（SOTA）质量，并在较低LOD下保持接近SOTA的性能。在最低LOD下，我们的方法仅使用6.2％的高斯，质量适度下降（L1 Loss +7.9％，PSNR --0.97％，SSIM --0.6％，LPIPS Loss +24.1％），而渲染速度几乎翻倍。

## 🔬 方法详解

**问题定义**：现有基于3D高斯溅射（3DGS）的头部头像方法，其高斯数量在训练后是固定的，无法根据实际应用需求调整细节层次（LOD），难以在渲染效率和视觉质量之间取得平衡。这限制了它们在需要不同LOD的应用场景中的使用。

**核心思路**：论文的核心思路是将3D高斯参数化到2D UV特征空间中，并使用一个可学习的UV特征场来编码高斯的潜在特征。通过在不同分辨率下对UV特征场进行重采样，可以动态地控制高斯点的数量，从而实现连续的LOD控制。这种设计避免了重新训练模型的需求，并允许在运行时调整LOD。

**技术框架**：ArchitectHead框架主要包含以下几个模块：1) UV特征场：由多层可学习的特征图组成，用于编码高斯的潜在特征。2) 解码器：一个轻量级的神经网络，将UV特征场中提取的特征解码为3D高斯属性（如位置、旋转、缩放、颜色等）。3) 渲染器：使用解码后的3D高斯属性进行渲染，生成最终的头部头像图像。整个流程是：首先，将头部姿态和表情作为输入；然后，在UV特征场中采样特征；接着，使用解码器将特征转换为高斯属性；最后，使用渲染器生成图像。

**关键创新**：该论文的关键创新在于提出了基于UV特征场的LOD控制方法。与现有方法相比，ArchitectHead能够实现连续的LOD控制，而无需重新训练模型。此外，通过将高斯参数化到UV空间，可以更有效地利用2D图像处理技术，例如特征图的重采样。

**关键设计**：UV特征场由多层特征图组成，每一层对应不同的分辨率。解码器是一个轻量级的MLP网络，输入是UV特征场中采样得到的特征向量，输出是3D高斯属性。损失函数包括L1损失、PSNR、SSIM和LPIPS损失，用于优化UV特征场和解码器的参数。在训练过程中，使用自重演和跨身份重演任务来评估模型的性能。

## 📊 实验亮点

实验结果表明，ArchitectHead在最高LOD下实现了自重演和跨身份重演任务中最先进的（SOTA）质量。在最低LOD下，该方法仅使用6.2％的高斯，质量适度下降（L1 Loss +7.9％，PSNR --0.97％，SSIM --0.6％，LPIPS Loss +24.1％），但渲染速度几乎翻倍。这表明ArchitectHead能够在视觉质量和渲染效率之间取得良好的平衡。

## 🎯 应用场景

ArchitectHead在虚拟会议、游戏、虚拟现实和增强现实等领域具有广泛的应用前景。它可以根据用户的设备性能和网络带宽动态调整头部头像的细节层次，从而在保证视觉质量的同时，提高渲染效率和用户体验。此外，该方法还可以用于创建高度逼真的数字替身，用于社交互动和内容创作。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has enabled photorealistic and real-time rendering of 3D head avatars. Existing 3DGS-based avatars typically rely on tens of thousands of 3D Gaussian points (Gaussians), with the number of Gaussians fixed after training. However, many practical applications require adjustable levels of detail (LOD) to balance rendering efficiency and visual quality. In this work, we propose "ArchitectHead", the first framework for creating 3D Gaussian head avatars that support continuous control over LOD. Our key idea is to parameterize the Gaussians in a 2D UV feature space and propose a UV feature field composed of multi-level learnable feature maps to encode their latent features. A lightweight neural network-based decoder then transforms these latent features into 3D Gaussian attributes for rendering. ArchitectHead controls the number of Gaussians by dynamically resampling feature maps from the UV feature field at the desired resolutions. This method enables efficient and continuous control of LOD without retraining. Experimental results show that ArchitectHead achieves state-of-the-art (SOTA) quality in self and cross-identity reenactment tasks at the highest LOD, while maintaining near SOTA performance at lower LODs. At the lowest LOD, our method uses only 6.2\% of the Gaussians while the quality degrades moderately (L1 Loss +7.9\%, PSNR --0.97\%, SSIM --0.6\%, LPIPS Loss +24.1\%), and the rendering speed nearly doubles.

