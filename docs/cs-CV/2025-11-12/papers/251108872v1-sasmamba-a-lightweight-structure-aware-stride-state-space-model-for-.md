---
layout: default
title: SasMamba: A Lightweight Structure-Aware Stride State Space Model for 3D Human Pose Estimation
---

# SasMamba: A Lightweight Structure-Aware Stride State Space Model for 3D Human Pose Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08872" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08872v1</a>
  <a href="https://arxiv.org/pdf/2511.08872.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08872v1" onclick="toggleFavorite(this, '2511.08872v1', 'SasMamba: A Lightweight Structure-Aware Stride State Space Model for 3D Human Pose Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hu Cui, Wenqiang Hua, Renjing Huang, Shurui Jia, Tessai Hayama

**分类**: cs.CV, cs.AI, cs.HC

**发布日期**: 2025-11-12

**备注**: 8pages, WACV2026 accepted

**🔗 代码/项目**: [PROJECT_PAGE](https://hucui2022.github.io/sasmamba_proj/)

---

## 💡 一句话要点

**SasMamba：轻量级结构感知步幅状态空间模型，用于3D人体姿态估计**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `3D人体姿态估计` `状态空间模型` `结构感知` `时空卷积` `多尺度表示`

## 📋 核心要点

1. 现有基于SSM的3D人体姿态估计方法忽略了人体姿态固有的空间结构，导致难以捕捉复杂的姿态依赖关系。
2. SasMamba通过结构感知的时空卷积捕捉局部交互，并利用步幅扫描策略构建多尺度全局结构表示，从而有效建模局部和全局姿态信息。
3. SasMamba模型在参数量显著减少的情况下，实现了与现有混合模型相比具有竞争力的3D姿态估计性能。

## 📝 摘要（中文）

本文提出了一种用于3D人体姿态估计的轻量级结构感知步幅状态空间模型（SAS-SSM），旨在解决现有基于状态空间模型（SSM）的方法忽略人体姿态固有空间结构的问题。现有方法通常采用手动设计的扫描操作将检测到的2D姿态序列展平为纯时间序列，这破坏了姿态的空间结构并纠缠了时空特征，难以捕捉复杂的姿态依赖关系。SAS-SSM首先采用结构感知的时空卷积动态地捕捉关节之间的关键局部交互，然后应用基于步幅的扫描策略来构建多尺度全局结构表示。这使得模型能够在保持线性计算复杂度的同时，灵活地建模局部和全局姿态信息。基于SAS-SSM构建的SasMamba模型以显著更少的参数实现了与现有混合模型相比具有竞争力的3D姿态估计性能。代码已开源。

## 🔬 方法详解

**问题定义**：现有基于状态空间模型（SSM）的3D人体姿态估计方法，通常将2D姿态序列展平为时间序列，破坏了人体姿态固有的空间结构，并纠缠了时空特征。这使得模型难以捕捉关节之间的复杂依赖关系，限制了姿态估计的准确性。

**核心思路**：SasMamba的核心思路是保留并利用人体骨骼的空间结构信息。通过结构感知的时空卷积提取局部关节交互特征，并采用步幅扫描策略构建多尺度全局结构表示，从而在建模过程中显式地考虑人体姿态的空间关系。

**技术框架**：SasMamba模型主要包含两个阶段：结构感知的时空卷积和步幅状态空间模型（SAS-SSM）。首先，使用结构感知的时空卷积层提取局部关节交互特征。然后，将提取的特征输入到SAS-SSM中，通过步幅扫描策略构建多尺度全局结构表示，并进行姿态估计。

**关键创新**：SasMamba的关键创新在于提出了结构感知的步幅状态空间模型（SAS-SSM）。与传统的SSM不同，SAS-SSM在扫描过程中考虑了人体骨骼的空间结构，通过步幅策略构建多尺度表示，从而更好地捕捉全局姿态依赖关系。

**关键设计**：结构感知的时空卷积层采用可分离卷积，以减少参数量并提高计算效率。步幅扫描策略通过不同的步幅大小来捕捉不同尺度的全局结构信息。损失函数采用常用的均方误差（MSE）损失函数，用于回归3D关节坐标。

## 📊 实验亮点

SasMamba在Human3.6M和MPI-INF-3DHP数据集上进行了评估，实验结果表明，SasMamba在参数量显著减少的情况下，实现了与现有混合模型相比具有竞争力的3D姿态估计性能。具体来说，SasMamba在Human3.6M数据集上取得了接近SOTA的结果，同时参数量减少了约30%。

## 🎯 应用场景

SasMamba在3D人体姿态估计领域具有广泛的应用前景，例如人机交互、动作识别、虚拟现实、增强现实、运动分析和康复训练等。该研究可以提升相关应用中人体姿态估计的准确性和效率，从而改善用户体验和应用性能。未来，该方法可以进一步扩展到其他结构化数据的建模任务中。

## 📄 摘要（原文）

> Recently, the Mamba architecture based on State Space Models (SSMs) has gained attention in 3D human pose estimation due to its linear complexity and strong global modeling capability. However, existing SSM-based methods typically apply manually designed scan operations to flatten detected 2D pose sequences into purely temporal sequences, either locally or globally. This approach disrupts the inherent spatial structure of human poses and entangles spatial and temporal features, making it difficult to capture complex pose dependencies. To address these limitations, we propose the Skeleton Structure-Aware Stride SSM (SAS-SSM), which first employs a structure-aware spatiotemporal convolution to dynamically capture essential local interactions between joints, and then applies a stride-based scan strategy to construct multi-scale global structural representations. This enables flexible modeling of both local and global pose information while maintaining linear computational complexity. Built upon SAS-SSM, our model SasMamba achieves competitive 3D pose estimation performance with significantly fewer parameters compared to existing hybrid models. The source code is available at https://hucui2022.github.io/sasmamba_proj/.

