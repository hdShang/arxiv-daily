---
layout: default
title: Approximating Signed Distance Fields of Implicit Surfaces with Sparse Ellipsoidal Radial Basis Function Networks
---

# Approximating Signed Distance Fields of Implicit Surfaces with Sparse Ellipsoidal Radial Basis Function Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02350" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02350v3</a>
  <a href="https://arxiv.org/pdf/2505.02350.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02350v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02350v3', 'Approximating Signed Distance Fields of Implicit Surfaces with Sparse Ellipsoidal Radial Basis Function Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bobo Lian, Dandan Wang, Chenjian Wu, Minxin Chen

**分类**: cs.GR, cs.CV, cs.LG

**发布日期**: 2025-05-05 (更新: 2025-10-24)

**🔗 代码/项目**: [GITHUB](https://github.com/lianbobo/SE-RBFNet.git)

---

## 💡 一句话要点

**提出稀疏椭球径向基函数网络以近似隐式表面的有符号距离场**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `有符号距离场` `隐式表面` `稀疏表示` `椭球径向基函数` `多目标优化` `计算机图形学` `3D几何`

## 📋 核心要点

1. 现有方法在隐式表面的有符号距离函数表示上存在参数冗余和计算效率低下的问题。
2. 本文提出通过稀疏椭球径向基函数网络来近似隐式表面的SDF，优化参数数量和计算效率。
3. 实验结果显示，该方法在多个基准数据集上以更少的参数实现了更高的准确性和计算效率。

## 📝 摘要（中文）

准确且紧凑地表示隐式表面的有符号距离函数（SDF）对于3D几何的高效存储、计算和后续处理至关重要。本文提出了一种通用学习方法，通过相对较少的椭球径向基函数（ERBFs）来近似预计算的隐式表面SDF场。该方法能够从多种来源（如点云、三角网格、解析表达式、预训练神经网络等）计算SDF值，并在空间网格点上以尽可能少的ERBFs来近似SDF，保持几何形状的同时实现紧凑表示。为平衡稀疏性和近似精度，本文引入了一种动态多目标优化策略，适应性地结合正则化以强制稀疏性，并联合优化ERBFs的权重、中心、形状和方向。实验表明，该方法在多个基准数据集上以显著更少的参数表示SDF场，且在准确性、鲁棒性和计算效率上均优于现有稀疏隐式表示方法。

## 🔬 方法详解

**问题定义**：本文旨在解决隐式表面的有符号距离函数（SDF）表示中存在的参数冗余和计算效率低下的问题。现有方法通常需要大量参数来表示SDF，导致存储和计算开销增加。

**核心思路**：论文提出了一种基于稀疏椭球径向基函数（ERBFs）的学习方法，通过优化ERBFs的数量和配置来实现紧凑的SDF表示。该方法能够从多种数据源中提取SDF值，并在保持几何形状的同时减少参数数量。

**技术框架**：整体框架包括数据输入、SDF值计算、ERBFs的优化和表示。首先，从点云或网格等数据源计算SDF值，然后通过动态多目标优化策略调整ERBFs的权重、中心、形状和方向，最后生成紧凑的SDF表示。

**关键创新**：最重要的创新在于引入动态多目标优化策略，该策略通过正则化来平衡稀疏性和近似精度，显著减少了所需的ERBFs数量。与现有方法相比，本文方法在保持表示精度的同时，显著降低了参数数量。

**关键设计**：在参数设置上，采用了基于最近邻的数据结构来限制计算范围，并利用CUDA并行化加速优化过程。此外，采用分层细化策略，从粗到细逐步引入样本进行参数初始化和优化，提高了收敛速度和训练效率。

## 📊 实验亮点

实验结果表明，本文方法在多个基准数据集上以显著更少的参数表示SDF场，相较于现有稀疏隐式表示方法，准确性提高了XX%，计算效率提升了YY%。具体而言，使用的ERBF数量减少了ZZ%，同时保持了良好的几何形状表示。

## 🎯 应用场景

该研究的潜在应用领域包括计算机图形学、虚拟现实、游戏开发和机器人导航等。通过提供高效的SDF表示，能够显著提升3D模型的处理速度和存储效率，进而推动相关技术的发展和应用。未来，该方法可能在实时渲染和复杂场景建模中发挥重要作用。

## 📄 摘要（原文）

> Accurate and compact representation of signed distance functions (SDFs) of implicit surfaces is crucial for efficient storage, computation, and downstream processing of 3D geometry. In this work, we propose a general learning method for approximating precomputed SDF fields of implicit surfaces by a relatively small number of ellipsoidal radial basis functions (ERBFs). The SDF values could be computed from various sources, including point clouds, triangle meshes, analytical expressions, pretrained neural networks, etc. Given SDF values on spatial grid points, our method approximates the SDF using as few ERBFs as possible, achieving a compact representation while preserving the geometric shape of the corresponding implicit surface. To balance sparsity and approximation precision, we introduce a dynamic multi-objective optimization strategy, which adaptively incorporates regularization to enforce sparsity and jointly optimizes the weights, centers, shapes, and orientations of the ERBFs. For computational efficiency, a nearest-neighbor-based data structure restricts computations to points near each kernel center, and CUDA-based parallelism further accelerates the optimization. Furthermore, a hierarchical refinement strategy based on SDF spatial grid points progressively incorporates coarse-to-fine samples for parameter initialization and optimization, improving convergence and training efficiency. Extensive experiments on multiple benchmark datasets demonstrate that our method can represent SDF fields with significantly fewer parameters than existing sparse implicit representation approaches, achieving better accuracy, robustness, and computational efficiency. The corresponding executable program is publicly available at https://github.com/lianbobo/SE-RBFNet.git

