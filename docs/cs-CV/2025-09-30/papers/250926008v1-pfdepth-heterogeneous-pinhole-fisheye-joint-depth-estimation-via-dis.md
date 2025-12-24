---
layout: default
title: "PFDepth: Heterogeneous Pinhole-Fisheye Joint Depth Estimation via Distortion-aware Gaussian-Splatted Volumetric Fusion"
---

# PFDepth: Heterogeneous Pinhole-Fisheye Joint Depth Estimation via Distortion-aware Gaussian-Splatted Volumetric Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26008" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26008v1</a>
  <a href="https://arxiv.org/pdf/2509.26008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26008v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26008v1', 'PFDepth: Heterogeneous Pinhole-Fisheye Joint Depth Estimation via Distortion-aware Gaussian-Splatted Volumetric Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiwei Zhang, Ruikai Xu, Weijian Zhang, Zhizhong Zhang, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma

**分类**: cs.CV, cs.AI, cs.CG

**发布日期**: 2025-09-30

**备注**: Accepted by ACM MM 2025 Conference

**DOI**: [10.1145/3746027.3755159](https://doi.org/10.1145/3746027.3755159)

---

## 💡 一句话要点

**PFDepth：提出一种基于畸变感知高斯溅射体素融合的异构针孔-鱼眼联合深度估计框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `深度估计` `多视角几何` `针孔相机` `鱼眼相机` `异构传感器融合` `三维重建` `高斯溅射`

## 📋 核心要点

1. 现有深度估计方法难以有效融合针孔相机和小视场鱼眼相机的互补信息，导致深度估计精度受限。
2. PFDepth通过显式地将异构视角的2D特征提升到3D体素空间，并设计异构空间融合模块，实现跨视角特征的有效融合。
3. 实验结果表明，PFDepth在KITTI-360和RealHet数据集上优于主流深度网络，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种用于异构多视角深度估计的针孔-鱼眼框架PFDepth。核心思想是利用针孔和鱼眼图像的互补特性（无畸变vs.有畸变，小vs.大视场，远场vs.近场）进行联合优化。PFDepth采用统一的架构，能够处理任意组合的具有不同内外参数的针孔和鱼眼相机。在PFDepth中，首先将来自每个异构视角的2D特征显式地提升到规范的3D体素空间中。然后，设计了一个名为异构空间融合的核心模块来处理和融合跨重叠和非重叠区域的畸变感知体素特征。此外，巧妙地将传统的体素融合重新表述为一种新的3D高斯表示，其中可学习的潜在高斯球动态地适应局部图像纹理，以实现更精细的3D聚合。最后，将融合的体素特征渲染成多视角深度图。通过大量的实验，证明PFDepth在KITTI-360和RealHet数据集上实现了最先进的性能，优于当前主流的深度网络。据我们所知，这是对异构针孔-鱼眼深度估计的首次系统研究，提供了技术创新和有价值的经验见解。

## 🔬 方法详解

**问题定义**：论文旨在解决异构多视角深度估计问题，特别是如何有效地融合针孔相机和鱼眼相机的数据。现有方法通常难以处理鱼眼相机的畸变，或者无法充分利用两种相机视场大小和景深范围的互补优势，导致深度估计精度不高。

**核心思路**：论文的核心思路是利用针孔相机和鱼眼相机的互补特性进行联合优化。具体来说，针孔相机图像无畸变，适合远距离深度估计；鱼眼相机视场大，适合近距离深度估计。通过将两种相机的数据融合，可以提高深度估计的精度和鲁棒性。

**技术框架**：PFDepth的整体架构包含以下几个主要模块：1) 特征提取：从每个视角的图像中提取2D特征。2) 空间提升：将2D特征提升到3D体素空间。3) 异构空间融合：融合来自不同视角的体素特征。4) 深度渲染：将融合后的体素特征渲染成多视角深度图。

**关键创新**：论文的关键创新点在于提出了异构空间融合模块和基于高斯溅射的体素表示。异构空间融合模块能够有效地处理和融合来自针孔相机和鱼眼相机的特征，考虑到鱼眼相机的畸变。基于高斯溅射的体素表示能够更精细地表示3D空间，从而提高深度估计的精度。

**关键设计**：在异构空间融合模块中，使用了可学习的权重来控制不同视角特征的贡献。在基于高斯溅射的体素表示中，高斯球的参数（如中心位置、方差）是可学习的，可以动态地适应局部图像纹理。损失函数包括深度损失和几何一致性损失，用于约束深度图的准确性和一致性。

## 📊 实验亮点

PFDepth在KITTI-360和RealHet数据集上取得了state-of-the-art的性能。相较于现有主流深度网络，PFDepth在深度估计精度上有显著提升。实验结果表明，PFDepth能够有效地融合针孔相机和鱼眼相机的数据，从而提高深度估计的精度和鲁棒性。具体提升幅度在论文中有详细数据。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、三维重建等领域。通过融合多种类型的相机数据，可以提高环境感知的准确性和鲁棒性，从而提升相关系统的性能。例如，在自动驾驶中，可以利用该方法生成高精度的深度图，辅助车辆进行障碍物检测和路径规划。

## 📄 摘要（原文）

> In this paper, we present the first pinhole-fisheye framework for heterogeneous multi-view depth estimation, PFDepth. Our key insight is to exploit the complementary characteristics of pinhole and fisheye imagery (undistorted vs. distorted, small vs. large FOV, far vs. near field) for joint optimization. PFDepth employs a unified architecture capable of processing arbitrary combinations of pinhole and fisheye cameras with varied intrinsics and extrinsics. Within PFDepth, we first explicitly lift 2D features from each heterogeneous view into a canonical 3D volumetric space. Then, a core module termed Heterogeneous Spatial Fusion is designed to process and fuse distortion-aware volumetric features across overlapping and non-overlapping regions. Additionally, we subtly reformulate the conventional voxel fusion into a novel 3D Gaussian representation, in which learnable latent Gaussian spheres dynamically adapt to local image textures for finer 3D aggregation. Finally, fused volume features are rendered into multi-view depth maps. Through extensive experiments, we demonstrate that PFDepth sets a state-of-the-art performance on KITTI-360 and RealHet datasets over current mainstream depth networks. To the best of our knowledge, this is the first systematic study of heterogeneous pinhole-fisheye depth estimation, offering both technical novelty and valuable empirical insights.

