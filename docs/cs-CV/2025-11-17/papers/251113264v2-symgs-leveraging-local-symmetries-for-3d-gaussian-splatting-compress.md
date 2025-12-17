---
layout: default
title: SymGS : Leveraging Local Symmetries for 3D Gaussian Splatting Compression
---

# SymGS : Leveraging Local Symmetries for 3D Gaussian Splatting Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13264" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13264v2</a>
  <a href="https://arxiv.org/pdf/2511.13264.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13264v2" onclick="toggleFavorite(this, '2511.13264v2', 'SymGS : Leveraging Local Symmetries for 3D Gaussian Splatting Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keshav Gupta, Akshat Sanghvi, Shreyas Reddy Palley, Astitva Srivastava, Charu Sharma, Avinash Sharma

**分类**: cs.CV, cs.GR

**发布日期**: 2025-11-17 (更新: 2025-11-19)

**备注**: Project Page: https://symgs.github.io/

---

## 💡 一句话要点

**SymGS：利用局部对称性压缩3D高斯溅射模型**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `压缩算法` `对称性建模` `新视角合成` `可学习镜像`

## 📋 核心要点

1. 现有3D高斯溅射压缩方法在处理复杂场景时，内存占用依然巨大，限制了其应用。
2. SymGS通过引入可学习的镜像，显式地建模和消除场景中的局部和全局反射对称性，减少冗余图元。
3. 实验表明，SymGS作为现有压缩方法的插件，能显著提升压缩率，平均可达108倍，同时保持渲染质量。

## 📝 摘要（中文）

3D高斯溅射（3DGS）已成为新视角合成领域的一项变革性技术，这主要归功于其高渲染速度和照片级逼真度。然而，其内存占用随着场景复杂性的增加而迅速增长，通常达到数GB。现有方法通过相似性检测和量化来利用图元级别的冗余，从而解决这个问题，引入压缩策略。我们旨在通过结合对称感知技术，特别是针对镜像对称性来消除冗余图元，从而超越此类方法的压缩限制。我们提出了一个新的压缩框架SymGS，将可学习的镜像引入场景，从而消除局部和全局反射冗余以进行压缩。我们的框架可以作为最先进的压缩方法（例如HAC）的即插即用增强，以实现进一步的压缩。与HAC相比，我们在基准数据集上实现了1.66倍的压缩（在大型场景上高达3倍）。平均而言，SymGS能够将3DGS场景压缩108倍，同时保持渲染质量。项目页面和补充材料可在symgs.github.io找到。

## 🔬 方法详解

**问题定义**：3D高斯溅射（3DGS）虽然在高质量新视角合成方面表现出色，但其存储需求随着场景复杂度的增加而迅速增长。现有的压缩方法，如基于聚类和量化的方法，虽然能减少冗余，但未能充分利用场景中普遍存在的对称性，导致压缩效率受限。

**核心思路**：SymGS的核心思路是显式地建模场景中的对称性，特别是镜像对称性，并利用这些对称性来消除冗余的3D高斯图元。通过学习得到场景中的镜像平面，可以将对称的图元合并或删除，从而减少存储空间。

**技术框架**：SymGS作为一个即插即用的模块，可以集成到现有的3DGS压缩流程中。其主要流程包括：1) 使用现有方法（如HAC）进行初步压缩；2) 引入可学习的镜像平面，通过优化损失函数来学习最佳的镜像位置和方向；3) 根据学习到的镜像平面，识别并消除对称的3D高斯图元；4) 对剩余的图元进行进一步的压缩。

**关键创新**：SymGS的关键创新在于引入了可学习的镜像平面，并将其用于3DGS的压缩。与传统的基于相似性的压缩方法不同，SymGS显式地建模了场景的对称性，从而能够更有效地消除冗余。此外，SymGS的设计使其可以方便地集成到现有的压缩流程中，提高了其通用性和实用性。

**关键设计**：SymGS的关键设计包括：1) 使用可学习的参数来表示镜像平面，并通过优化损失函数来学习这些参数；2) 设计损失函数，鼓励镜像平面能够准确地反映场景中的对称性，并减少对称图元之间的差异；3) 使用阈值来判断两个图元是否对称，并根据判断结果进行合并或删除。

## 📊 实验亮点

SymGS在多个基准数据集上进行了评估，实验结果表明，SymGS能够显著提高3DGS模型的压缩率。与HAC相比，SymGS平均实现了1.66倍的压缩，在大型场景上甚至高达3倍。总体而言，SymGS能够将3DGS场景压缩108倍，同时保持渲染质量。

## 🎯 应用场景

SymGS在虚拟现实、增强现实、游戏开发等领域具有广泛的应用前景。通过显著降低3DGS模型的存储需求，SymGS使得在移动设备或资源受限的环境中部署高质量的3D场景成为可能。此外，SymGS还可以应用于三维重建、场景理解等任务，提高效率和精度。

## 📄 摘要（原文）

> 3D Gaussian Splatting has emerged as a transformative technique in novel view synthesis, primarily due to its high rendering speed and photorealistic fidelity. However, its memory footprint scales rapidly with scene complexity, often reaching several gigabytes. Existing methods address this issue by introducing compression strategies that exploit primitive-level redundancy through similarity detection and quantization. We aim to surpass the compression limits of such methods by incorporating symmetry-aware techniques, specifically targeting mirror symmetries to eliminate redundant primitives. We propose a novel compression framework, SymGS, introducing learnable mirrors into the scene, thereby eliminating local and global reflective redundancies for compression. Our framework functions as a plug-and-play enhancement to state-of-the-art compression methods, (e.g. HAC) to achieve further compression. Compared to HAC, we achieve $1.66 \times$ compression across benchmark datasets (upto $3\times$ on large-scale scenes). On an average, SymGS enables $\bf{108\times}$ compression of a 3DGS scene, while preserving rendering quality. The project page and supplementary can be found at symgs.github.io

