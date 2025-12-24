---
layout: default
title: "GMF-Drive: Gated Mamba Fusion with Spatial-Aware BEV Representation for End-to-End Autonomous Driving"
---

# GMF-Drive: Gated Mamba Fusion with Spatial-Aware BEV Representation for End-to-End Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06113" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06113v2</a>
  <a href="https://arxiv.org/pdf/2508.06113.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06113v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06113v2', 'GMF-Drive: Gated Mamba Fusion with Spatial-Aware BEV Representation for End-to-End Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Wang, Chaokang Jiang, Haitao Xu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-08 (更新: 2025-08-12)

**备注**: 7 pages, 4 figures

---

## 💡 一句话要点

**提出GMF-Drive以解决现有自动驾驶模型的融合效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动驾驶` `空间感知` `状态空间模型` `几何增强` `信息融合` `鸟瞰图表示` `高效计算` `深度学习`

## 📋 核心要点

1. 现有的基于变压器的自动驾驶模型在高分辨率特征处理上存在计算复杂度高的问题，限制了其性能。
2. GMF-Drive通过几何增强的柱状格式和空间感知的状态空间模型，提升了信息表示和融合效率。
3. 在NAVSIM基准测试中，GMF-Drive显著超越了DiffusionDrive，展示了其在性能和效率上的优势。

## 📝 摘要（中文）

基于扩散模型的自动驾驶技术正在重新定义该领域的前沿，但其性能受到依赖于变压器融合的限制。现有架构面临计算复杂度高和缺乏空间先验的挑战，无法有效建模鸟瞰图（BEV）表示。本文提出GMF-Drive（Gated Mamba Fusion for Driving），通过两项创新克服这些挑战。首先，采用几何增强的柱状格式替代信息有限的直方图激光雷达表示，保留关键的3D几何细节。其次，提出了一种新型的分层门控曼巴融合（GM-Fusion）架构，用高效的空间感知状态空间模型（SSM）替代昂贵的变压器。实验结果表明，GMF-Drive在NAVSIM基准测试中实现了新的最优性能，显著超越DiffusionDrive。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动驾驶模型在高分辨率特征处理中的计算复杂度和空间建模能力不足的问题。现有的变压器架构在处理鸟瞰图表示时，无法有效捕捉空间信息，导致性能受限。

**核心思路**：GMF-Drive的核心思路是通过几何增强的柱状格式和高效的空间感知状态空间模型（SSM）来替代传统的变压器架构，从而降低计算复杂度并提高信息融合的有效性。

**技术框架**：GMF-Drive的整体架构包括两个主要模块：几何增强的柱状格式用于表示激光雷达数据，和分层门控曼巴融合架构（GM-Fusion）用于信息融合。BEV-SSM模块通过方向序列和自适应融合机制捕捉长距离依赖关系。

**关键创新**：最重要的技术创新在于引入了几何增强的柱状格式和空间感知的状态空间模型（SSM），这使得GMF-Drive在处理复杂场景时能够保持线性复杂度，显著提升了性能和效率。

**关键设计**：在设计中，GMF-Drive采用了方向序列和自适应融合机制，以确保模型能够有效捕捉空间特性。此外，损失函数和网络结构经过精心设计，以优化任务特定的性能。

## 📊 实验亮点

在NAVSIM基准测试中，GMF-Drive实现了新的最优性能，显著超越了DiffusionDrive，展示了在性能和效率上的提升。具体而言，GMF-Drive在处理高分辨率特征时，计算复杂度保持在线性水平，极大地提高了模型的实用性和响应速度。

## 🎯 应用场景

GMF-Drive的研究成果具有广泛的应用潜力，特别是在自动驾驶、智能交通系统和机器人导航等领域。其高效的信息处理能力和空间建模能力能够提升自动驾驶系统的安全性和可靠性，推动智能交通技术的发展。未来，GMF-Drive可能会在更复杂的城市环境中得到应用，进一步提升自动驾驶的智能化水平。

## 📄 摘要（原文）

> Diffusion-based models are redefining the state-of-the-art in end-to-end autonomous driving, yet their performance is increasingly hampered by a reliance on transformer-based fusion. These architectures face fundamental limitations: quadratic computational complexity restricts the use of high-resolution features, and a lack of spatial priors prevents them from effectively modeling the inherent structure of Bird's Eye View (BEV) representations. This paper introduces GMF-Drive (Gated Mamba Fusion for Driving), an end-to-end framework that overcomes these challenges through two principled innovations. First, we supersede the information-limited histogram-based LiDAR representation with a geometrically-augmented pillar format encoding shape descriptors and statistical features, preserving critical 3D geometric details. Second, we propose a novel hierarchical gated mamba fusion (GM-Fusion) architecture that substitutes an expensive transformer with a highly efficient, spatially-aware state-space model (SSM). Our core BEV-SSM leverages directional sequencing and adaptive fusion mechanisms to capture long-range dependencies with linear complexity, while explicitly respecting the unique spatial properties of the driving scene. Extensive experiments on the challenging NAVSIM benchmark demonstrate that GMF-Drive achieves a new state-of-the-art performance, significantly outperforming DiffusionDrive. Comprehensive ablation studies validate the efficacy of each component, demonstrating that task-specific SSMs can surpass a general-purpose transformer in both performance and efficiency for autonomous driving.

