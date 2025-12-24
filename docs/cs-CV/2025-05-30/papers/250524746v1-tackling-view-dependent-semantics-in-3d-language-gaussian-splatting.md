---
layout: default
title: Tackling View-Dependent Semantics in 3D Language Gaussian Splatting
---

# Tackling View-Dependent Semantics in 3D Language Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24746" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24746v1</a>
  <a href="https://arxiv.org/pdf/2505.24746.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24746v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24746v1', 'Tackling View-Dependent Semantics in 3D Language Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiazhong Cen, Xudong Zhou, Jiemin Fang, Changsong Wen, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian

**分类**: cs.CV

**发布日期**: 2025-05-30

**备注**: ICML 2025 camera ready. Project Page: https://jumpat.github.io/laga-page/

**🔗 代码/项目**: [GITHUB](https://github.com/SJTU-DeepVisionLab/LaGa)

---

## 💡 一句话要点

**提出LaGa以解决3D场景中的视角依赖语义问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景重建` `视角依赖语义` `高斯点云` `语言驱动` `开放词汇理解` `语义聚合` `多视角学习`

## 📋 核心要点

1. 现有方法在处理3D场景时，未能有效解决视角依赖语义的问题，导致语义理解不足。
2. 论文提出LaGa，通过将3D场景分解为物体，建立跨视角的语义连接，聚合视角信息以增强语义表示。
3. 实验结果显示，LaGa在LERF-OVS数据集上实现了18.7%的mIoU提升，显著优于现有最优方法。

## 📝 摘要（中文）

近年来，3D高斯点云技术（3D-GS）在从RGB图像重建高质量3D场景方面取得了显著进展。许多研究将这一范式扩展到语言驱动的开放词汇场景理解。然而，大多数研究仅将2D语义特征投影到3D高斯上，忽视了2D与3D理解之间的根本差距：3D物体从不同视角可能展现出不同的语义，这一现象被称为视角依赖语义。为了解决这一挑战，本文提出了LaGa（语言高斯），通过将3D场景分解为物体，建立跨视角的语义连接。然后，基于多视角语义聚类语义描述符并重新加权，从而构建视角聚合的语义表示。大量实验表明，LaGa有效捕捉视角依赖语义的关键信息，从而实现更全面的3D场景理解。在相同设置下，LaGa在LERF-OVS数据集上相较于之前的SOTA取得了显著提升，mIoU提高了18.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决3D场景理解中的视角依赖语义问题。现有方法通常将2D语义特征简单投影到3D高斯上，未能考虑3D物体在不同视角下的语义变化，导致理解效果不佳。

**核心思路**：LaGa通过将3D场景分解为多个物体，建立跨视角的语义连接，进而聚合来自不同视角的语义信息，以实现更全面的3D场景理解。这种设计考虑了视角变化对语义的影响，增强了语义表示的准确性。

**技术框架**：LaGa的整体架构包括三个主要模块：首先是3D场景的物体分解，其次是语义描述符的聚类，最后是基于多视角语义的加权重构。这一流程确保了不同视角下的语义信息能够有效整合。

**关键创新**：LaGa的主要创新在于其视角聚合的语义表示方法，通过对语义描述符的聚类与加权，建立了更为精确的视角依赖语义连接。这与传统方法的直接投影方式形成了鲜明对比。

**关键设计**：在设计中，LaGa采用了特定的聚类算法来处理语义描述符，并通过加权机制来调整不同视角的语义影响。此外，损失函数的设计也考虑了视角间的语义一致性，以提高模型的学习效果。

## 📊 实验亮点

实验结果表明，LaGa在LERF-OVS数据集上实现了18.7%的mIoU提升，显著超越了之前的最优方法，验证了其在视角依赖语义理解方面的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、虚拟现实和增强现实等场景理解任务。通过更准确的3D场景理解，LaGa能够提升机器人导航、环境建模和人机交互的智能化水平，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advancements in 3D Gaussian Splatting (3D-GS) enable high-quality 3D scene reconstruction from RGB images. Many studies extend this paradigm for language-driven open-vocabulary scene understanding. However, most of them simply project 2D semantic features onto 3D Gaussians and overlook a fundamental gap between 2D and 3D understanding: a 3D object may exhibit various semantics from different viewpoints--a phenomenon we term view-dependent semantics. To address this challenge, we propose LaGa (Language Gaussians), which establishes cross-view semantic connections by decomposing the 3D scene into objects. Then, it constructs view-aggregated semantic representations by clustering semantic descriptors and reweighting them based on multi-view semantics. Extensive experiments demonstrate that LaGa effectively captures key information from view-dependent semantics, enabling a more comprehensive understanding of 3D scenes. Notably, under the same settings, LaGa achieves a significant improvement of +18.7% mIoU over the previous SOTA on the LERF-OVS dataset. Our code is available at: https://github.com/SJTU-DeepVisionLab/LaGa.

