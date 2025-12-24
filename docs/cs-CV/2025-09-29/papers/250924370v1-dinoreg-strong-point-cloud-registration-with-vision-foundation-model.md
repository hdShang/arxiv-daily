---
layout: default
title: "DINOReg: Strong Point Cloud Registration with Vision Foundation Model"
---

# DINOReg: Strong Point Cloud Registration with Vision Foundation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24370" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24370v1</a>
  <a href="https://arxiv.org/pdf/2509.24370.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24370v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24370v1', 'DINOReg: Strong Point Cloud Registration with Vision Foundation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Congjia Chen, Yufu Qu

**分类**: cs.CV

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/ccjccjccj/DINOReg)

---

## 💡 一句话要点

**DINOReg：利用视觉基础模型实现强大的点云配准**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `点云配准` `视觉基础模型` `DINOv2` `多模态融合` `RGB-D数据` `几何特征` `视觉特征`

## 📋 核心要点

1. 现有RGB-D点云配准方法未能充分利用图像的纹理和语义信息，且特征融合过程存在信息损失，限制了配准性能。
2. DINOReg利用DINOv2提取图像的视觉特征，并在patch级别与几何特征融合，从而结合了视觉语义信息和几何结构信息。
3. 实验表明，DINOReg在RGBD-3DMatch和RGBD-3DLoMatch数据集上显著优于现有方法，提升了配准精度和召回率。

## 📝 摘要（中文）

点云配准是三维计算机视觉中的一项基本任务。现有方法大多仅依赖几何信息进行特征提取和匹配。最近，一些研究将RGB-D数据中的颜色信息融入特征提取，虽然取得了显著改进，但它们没有充分利用图像中丰富的纹理和语义信息，并且特征融合以一种图像有损的方式进行，限制了性能。本文提出了DINOReg，一种充分利用视觉和几何信息来解决点云配准问题的网络。受视觉基础模型进展的启发，我们采用DINOv2从图像中提取信息丰富的视觉特征，并在patch级别融合视觉和几何特征。这种设计有效地结合了DINOv2提取的丰富纹理和全局语义信息，以及几何骨干网络捕获的详细几何结构信息。此外，提出了一种混合位置嵌入来编码来自图像空间和点云空间的位置信息，增强了模型感知patch之间空间关系的能力。在RGBD-3DMatch和RGBD-3DLoMatch数据集上的大量实验表明，我们的方法相对于最先进的纯几何方法和多模态配准方法，取得了显著的改进，patch内点比例提高了14.2%，配准召回率提高了15.7%。代码已公开。

## 🔬 方法详解

**问题定义**：论文旨在解决RGB-D点云配准问题。现有方法主要依赖几何信息，或虽引入RGB信息但未能充分利用图像的纹理和语义信息，且特征融合过程存在信息损失，导致配准精度受限。

**核心思路**：论文的核心思路是利用视觉基础模型DINOv2提取图像的视觉特征，并将其与几何特征在patch级别进行融合。通过这种方式，模型可以同时利用图像的全局语义信息和点云的局部几何结构信息，从而提高配准的准确性。

**技术框架**：DINOReg的整体框架包括以下几个主要模块：1) 几何特征提取模块：使用几何骨干网络提取点云的几何特征。2) 视觉特征提取模块：使用DINOv2提取图像的视觉特征。3) 特征融合模块：在patch级别融合几何特征和视觉特征。4) 混合位置编码模块：编码图像空间和点云空间的位置信息。5) 配准模块：利用融合后的特征进行点云配准。

**关键创新**：该论文的关键创新在于：1) 充分利用了视觉基础模型DINOv2提取的图像语义信息，克服了传统方法对图像信息利用不足的缺点。2) 提出了patch级别的特征融合方法，避免了图像信息的损失。3) 提出了混合位置编码方法，增强了模型对空间关系的感知能力。

**关键设计**：混合位置嵌入的设计是关键。它结合了图像空间和点云空间的位置信息，具体实现方式未知（论文未详细描述）。损失函数的设计也至关重要，但论文中没有明确说明使用了何种损失函数。DINOv2的参数设置和几何骨干网络的选择也会影响最终的性能。

## 📊 实验亮点

DINOReg在RGBD-3DMatch和RGBD-3DLoMatch数据集上取得了显著的性能提升。相较于最先进的几何方法和多模态方法，DINOReg的patch内点比例提高了14.2%，配准召回率提高了15.7%。这些结果表明，DINOReg能够有效地利用视觉信息，提高点云配准的精度和鲁棒性。

## 🎯 应用场景

DINOReg在机器人导航、三维重建、增强现实等领域具有广泛的应用前景。它可以用于提高机器人对环境的感知能力，实现更精确的三维场景重建，以及增强AR应用的真实感和交互性。该研究的成果有助于推动三维视觉技术的发展，并为相关应用带来更高的精度和鲁棒性。

## 📄 摘要（原文）

> Point cloud registration is a fundamental task in 3D computer vision. Most existing methods rely solely on geometric information for feature extraction and matching. Recently, several studies have incorporated color information from RGB-D data into feature extraction. Although these methods achieve remarkable improvements, they have not fully exploited the abundant texture and semantic information in images, and the feature fusion is performed in an image-lossy manner, which limit their performance. In this paper, we propose DINOReg, a registration network that sufficiently utilizes both visual and geometric information to solve the point cloud registration problem. Inspired by advances in vision foundation models, we employ DINOv2 to extract informative visual features from images, and fuse visual and geometric features at the patch level. This design effectively combines the rich texture and global semantic information extracted by DINOv2 with the detailed geometric structure information captured by the geometric backbone. Additionally, a mixed positional embedding is proposed to encode positional information from both image space and point cloud space, which enhances the model's ability to perceive spatial relationships between patches. Extensive experiments on the RGBD-3DMatch and RGBD-3DLoMatch datasets demonstrate that our method achieves significant improvements over state-of-the-art geometry-only and multi-modal registration methods, with a 14.2% increase in patch inlier ratio and a 15.7% increase in registration recall. The code is publicly available at https://github.com/ccjccjccj/DINOReg.

