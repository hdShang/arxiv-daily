---
layout: default
title: "MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction"
---

# MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04297" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04297v2</a>
  <a href="https://arxiv.org/pdf/2508.04297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04297v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04297v2', 'MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaopeng Lou, Liao Shen, Tianqi Liu, Jiaqi Li, Zihao Huang, Huiqiang Sun, Zhiguo Cao

**分类**: cs.CV

**发布日期**: 2025-08-06 (更新: 2025-10-23)

**备注**: This work is accepted by ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/EuclidLou/MuGS)

---

## 💡 一句话要点

**提出MuGS以解决多基线视图合成问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多基线合成` `高斯表示` `深度融合` `特征增强` `虚拟现实` `计算机图形学`

## 📋 核心要点

1. 现有方法在处理多基线视图合成时，往往对输入视图的稀疏性和基线差异敏感，导致重建效果不佳。
2. 论文提出了一种结合多视图立体和单目深度估计的特征增强方法，并引入投影与采样机制以优化深度融合过程。
3. MuGS在DTU、RealEstate10K等数据集上表现出色，且在LLFF和Mip-NeRF 360数据集上实现了零-shot性能，展示了其广泛的适用性。

## 📝 摘要（中文）

我们提出了多基线高斯点云重建（MuGS），这是一种通用的前馈方法，能够有效处理包括稀疏输入视图在内的多种基线设置。具体而言，我们结合了多视图立体（MVS）和单目深度估计（MDE）的特征，以增强可泛化重建的特征表示。接下来，我们提出了一种投影与采样机制，用于深度融合，构建精细的概率体积以指导特征图的回归。此外，我们引入了参考视图损失，以提高几何和优化效率。MuGS在多个基线设置和从简单物体到复杂室内外场景的多种场景中实现了最先进的性能，并在LLFF和Mip-NeRF 360数据集上展示了良好的零-shot性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决多基线视图合成中的重建质量问题，现有方法在处理稀疏输入视图和不同基线时效果不佳，难以实现高质量的重建。

**核心思路**：我们提出MuGS，通过结合多视图立体（MVS）和单目深度估计（MDE）来增强特征表示，并通过投影与采样机制优化深度融合，从而提高重建的泛化能力。

**技术框架**：MuGS的整体架构包括特征提取、深度融合和重建三个主要模块。特征提取模块负责从输入视图中提取特征，深度融合模块通过投影与采样机制构建概率体积，最后重建模块生成最终的视图。

**关键创新**：本研究的关键创新在于引入了参考视图损失，显著提高了几何重建的精度和优化效率，同时利用3D高斯表示加速了训练和推理过程。

**关键设计**：我们设计了特定的损失函数来优化几何重建，并在网络结构中采用了高斯表示，以提高渲染质量和训练速度。

## 📊 实验亮点

MuGS在DTU和RealEstate10K数据集上实现了最先进的性能，特别是在复杂场景中表现优异。此外，在LLFF和Mip-NeRF 360数据集上展示了良好的零-shot性能，证明了其广泛的适用性和强大的泛化能力。

## 🎯 应用场景

该研究在虚拟现实、增强现实和计算机图形学等领域具有广泛的应用潜力。MuGS能够在多种场景中实现高质量的视图合成，推动相关技术的发展，提升用户体验。

## 📄 摘要（原文）

> We present Multi-Baseline Gaussian Splatting (MuGS), a generalized feed-forward approach for novel view synthesis that effectively handles diverse baseline settings, including sparse input views with both small and large baselines. Specifically, we integrate features from Multi-View Stereo (MVS) and Monocular Depth Estimation (MDE) to enhance feature representations for generalizable reconstruction. Next, We propose a projection-and-sampling mechanism for deep depth fusion, which constructs a fine probability volume to guide the regression of the feature map. Furthermore, We introduce a reference-view loss to improve geometry and optimization efficiency. We leverage 3D Gaussian representations to accelerate training and inference time while enhancing rendering quality. MuGS achieves state-of-the-art performance across multiple baseline settings and diverse scenarios ranging from simple objects (DTU) to complex indoor and outdoor scenes (RealEstate10K). We also demonstrate promising zero-shot performance on the LLFF and Mip-NeRF 360 datasets. Code is available at https://github.com/EuclidLou/MuGS.

