---
layout: default
title: "SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse Satellite Images"
---

# SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse Satellite Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09479" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09479v1</a>
  <a href="https://arxiv.org/pdf/2508.09479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09479v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09479v1', 'SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse Satellite Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang

**分类**: cs.CV

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出SkySplat以解决多时相稀疏卫星图像的3D重建问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `三维重建` `卫星图像` `高斯点云` `自监督学习` `遥感技术` `几何线索` `跨数据集泛化`

## 📋 核心要点

1. 现有的3D重建方法在处理稀疏卫星图像时存在不兼容RPC模型和泛化能力不足的问题。
2. SkySplat通过将RPC模型整合进3DGS流程，利用稀疏几何线索进行自监督学习，提升重建效果。
3. SkySplat在DFC19数据集上将MAE显著降低至1.80米，并在多个数据集上展示了优越的泛化能力，速度提升达86倍。

## 📝 摘要（中文）

从稀疏视角卫星图像进行三维场景重建一直是一个长期且具有挑战性的任务。尽管三维高斯点云（3DGS）及其变体因其高效性受到关注，但现有方法由于与有理多项式系数（RPC）模型的不兼容性和有限的泛化能力，仍不适用于卫星图像。为了解决这些局限性，本文提出了SkySplat，一个新颖的自监督框架，将RPC模型集成到可泛化的3DGS流程中，从而更有效地利用稀疏几何线索以改善重建效果。SkySplat仅依赖RGB图像和辐射稳健的相对高度监督，消除了对真实高度图的需求。实验结果表明，SkySplat在DFC19数据集上将平均绝对误差（MAE）从13.18米显著降低至1.80米，并在MVS3D基准上展示了强大的跨数据集泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决从多时相稀疏卫星图像进行三维重建的挑战，现有方法由于与RPC模型的不兼容性和泛化能力不足，难以有效处理此类数据。

**核心思路**：SkySplat的核心思路是将RPC模型集成到可泛化的3DGS框架中，通过自监督学习方式，利用RGB图像和相对高度监督来改善重建效果，避免对真实高度图的依赖。

**技术框架**：SkySplat的整体架构包括多个模块，主要有Cross-Self Consistency Module（CSCM）用于减少瞬态物体干扰，以及多视图一致性聚合策略以精细化重建结果。

**关键创新**：SkySplat的创新在于引入RPC模型和自监督学习机制，使得稀疏几何线索的利用更加有效，显著提升了重建精度和速度，与传统的逐场景优化方法相比具有本质区别。

**关键设计**：SkySplat的关键设计包括使用一致性掩蔽来减轻瞬态物体的影响，采用辐射稳健的相对高度监督，并通过多视图一致性聚合策略来优化重建结果。

## 📊 实验亮点

SkySplat在DFC19数据集上将平均绝对误差（MAE）从13.18米降低至1.80米，显示出显著的性能提升。同时，相较于EOGS，SkySplat实现了86倍的速度提升，并在MVS3D基准上展现了强大的跨数据集泛化能力。

## 🎯 应用场景

该研究在遥感、环境监测和城市规划等领域具有广泛的应用潜力。通过提高稀疏卫星图像的三维重建精度，SkySplat能够为地理信息系统（GIS）提供更为准确的空间数据，进而支持决策制定和资源管理。

## 📄 摘要（原文）

> Three-dimensional scene reconstruction from sparse-view satellite images is a long-standing and challenging task. While 3D Gaussian Splatting (3DGS) and its variants have recently attracted attention for its high efficiency, existing methods remain unsuitable for satellite images due to incompatibility with rational polynomial coefficient (RPC) models and limited generalization capability. Recent advances in generalizable 3DGS approaches show potential, but they perform poorly on multi-temporal sparse satellite images due to limited geometric constraints, transient objects, and radiometric inconsistencies. To address these limitations, we propose SkySplat, a novel self-supervised framework that integrates the RPC model into the generalizable 3DGS pipeline, enabling more effective use of sparse geometric cues for improved reconstruction. SkySplat relies only on RGB images and radiometric-robust relative height supervision, thereby eliminating the need for ground-truth height maps. Key components include a Cross-Self Consistency Module (CSCM), which mitigates transient object interference via consistency-based masking, and a multi-view consistency aggregation strategy that refines reconstruction results. Compared to per-scene optimization methods, SkySplat achieves an 86 times speedup over EOGS with higher accuracy. It also outperforms generalizable 3DGS baselines, reducing MAE from 13.18 m to 1.80 m on the DFC19 dataset significantly, and demonstrates strong cross-dataset generalization on the MVS3D benchmark.

