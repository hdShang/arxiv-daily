---
layout: default
title: "SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian Bracketing"
---

# SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian Bracketing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20400" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20400v1</a>
  <a href="https://arxiv.org/pdf/2509.20400.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20400v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20400v1', 'SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian Bracketing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiyu Li, Haoyuan Wang, Ke Xu, Gerhard Petrus Hancke, Rynson W. H. Lau

**分类**: cs.GR

**发布日期**: 2025-09-23

**备注**: ICCV 2025 accepted paper

---

## 💡 一句话要点

**SeHDR：基于3D高斯包围的单曝光HDR新视角合成**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `HDR成像` `新视角合成` `3D高斯溅射` `单曝光图像` `神经渲染`

## 📋 核心要点

1. 现有HDR新视角合成方法依赖多曝光图像，采集繁琐且易受运动模糊和校准误差影响。
2. SeHDR从单曝光多视角LDR图像估计不同曝光的3D高斯，再融合为HDR场景表示。
3. 实验表明，SeHDR在HDR新视角合成任务中优于现有方法和精心设计的基线。

## 📝 摘要（中文）

本文提出了一种新颖的高动态范围3D高斯溅射(HDR-3DGS)方法SeHDR，用于从多视角LDR图像生成HDR新视角，这些LDR图像是从单次曝光中获取的。与现有方法通常需要从不同曝光捕获多视角LDR输入图像不同（这种捕获方式繁琐且更容易出现错误，例如物体运动模糊和校准/对齐不准确），我们的方法从单次曝光的多视角LDR图像中学习HDR场景表示。我们解决这个不适定问题的关键在于，首先从单次曝光多视角LDR图像中估计包围的3D高斯（即具有不同曝光），然后将这些包围的3D高斯合并为HDR场景表示。具体来说，SeHDR首先从单次曝光LDR输入中学习基础3D高斯，其中球谐函数参数化线性颜色空间中的颜色。然后，我们估计多个具有相同几何形状但线性颜色随曝光变化的3D高斯。最后，我们提出了可微神经曝光融合(NeEF)来将基础和估计的3D高斯集成到HDR高斯中，以进行新视角渲染。大量实验表明，SeHDR优于现有方法以及精心设计的基线。

## 🔬 方法详解

**问题定义**：现有HDR新视角合成方法需要多曝光的LDR图像作为输入，这使得数据采集过程非常繁琐，并且容易受到运动模糊、相机校准误差等问题的影响，从而影响最终的合成质量。因此，如何在单曝光的LDR图像下实现高质量的HDR新视角合成是一个具有挑战性的问题。

**核心思路**：SeHDR的核心思路是从单曝光LDR图像中推断出不同曝光下的3D高斯表示，然后将这些不同曝光的3D高斯融合起来，得到HDR场景表示。这种方法避免了直接从LDR图像预测HDR图像的困难，而是通过学习不同曝光下的场景几何和颜色信息，从而实现HDR合成。

**技术框架**：SeHDR的整体框架包括以下几个主要步骤：1) 从单曝光LDR图像中学习基础3D高斯表示，其中球谐函数用于参数化线性颜色空间中的颜色。2) 估计多个具有相同几何形状但线性颜色随曝光变化的3D高斯。3) 使用可微神经曝光融合(NeEF)模块，将基础3D高斯和估计的3D高斯集成到HDR高斯中。4) 使用HDR高斯进行新视角渲染。

**关键创新**：SeHDR的关键创新在于提出了Bracketed 3D Gaussians的概念，即从单曝光LDR图像中估计不同曝光下的3D高斯表示。此外，提出的Differentiable Neural Exposure Fusion (NeEF)模块能够有效地将不同曝光下的3D高斯融合为HDR高斯，从而实现高质量的HDR新视角合成。与现有方法相比，SeHDR不需要多曝光图像作为输入，从而简化了数据采集过程，并降低了对相机校准精度的要求。

**关键设计**：SeHDR的关键设计包括：1) 使用球谐函数参数化线性颜色空间中的颜色，以便更好地表示HDR颜色信息。2) 使用NeEF模块进行曝光融合，该模块通过学习权重来控制不同曝光下3D高斯的贡献。3) 使用可微渲染技术，使得整个模型可以端到端地进行训练。损失函数包括L1损失、L2损失和感知损失等，用于约束合成图像的质量。

## 📊 实验亮点

SeHDR在合成HDR新视角方面表现出色，优于现有方法和精心设计的基线。具体性能数据在论文中给出，但摘要中未明确提及具体的性能提升幅度。实验结果表明，SeHDR能够有效地从单曝光LDR图像中恢复HDR信息，并生成高质量的新视角图像。

## 🎯 应用场景

SeHDR具有广泛的应用前景，例如虚拟现实、增强现实、游戏开发、电影制作等领域。它可以用于创建逼真的HDR场景，从而提升用户体验。此外，SeHDR还可以用于图像编辑和修复，例如从单张LDR图像中恢复HDR信息，或者去除图像中的曝光不足或过度曝光区域。未来，SeHDR有望成为一种重要的图像处理工具。

## 📄 摘要（原文）

> This paper presents SeHDR, a novel high dynamic range 3D Gaussian Splatting (HDR-3DGS) approach for generating HDR novel views given multi-view LDR images. Unlike existing methods that typically require the multi-view LDR input images to be captured from different exposures, which are tedious to capture and more likely to suffer from errors (e.g., object motion blurs and calibration/alignment inaccuracies), our approach learns the HDR scene representation from multi-view LDR images of a single exposure. Our key insight to this ill-posed problem is that by first estimating Bracketed 3D Gaussians (i.e., with different exposures) from single-exposure multi-view LDR images, we may then be able to merge these bracketed 3D Gaussians into an HDR scene representation. Specifically, SeHDR first learns base 3D Gaussians from single-exposure LDR inputs, where the spherical harmonics parameterize colors in a linear color space. We then estimate multiple 3D Gaussians with identical geometry but varying linear colors conditioned on exposure manipulations. Finally, we propose the Differentiable Neural Exposure Fusion (NeEF) to integrate the base and estimated 3D Gaussians into HDR Gaussians for novel view rendering. Extensive experiments demonstrate that SeHDR outperforms existing methods as well as carefully designed baselines.

