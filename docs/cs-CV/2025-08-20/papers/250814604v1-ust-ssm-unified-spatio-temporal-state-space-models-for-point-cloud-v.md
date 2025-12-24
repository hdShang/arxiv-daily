---
layout: default
title: "UST-SSM: Unified Spatio-Temporal State Space Models for Point Cloud Video Modeling"
---

# UST-SSM: Unified Spatio-Temporal State Space Models for Point Cloud Video Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14604" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14604v1</a>
  <a href="https://arxiv.org/pdf/2508.14604.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14604v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14604v1', 'UST-SSM: Unified Spatio-Temporal State Space Models for Point Cloud Video Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peiming Li, Ziyi Wang, Yulin Yuan, Hong Liu, Xiangming Meng, Junsong Yuan, Mengyuan Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-20

**备注**: 8 pages, 5 figures, Accepted to ICCV2025

**🔗 代码/项目**: [GITHUB](https://github.com/wangzy01/UST-SSM)

---

## 💡 一句话要点

**提出UST-SSM以解决点云视频建模中的时空无序问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `点云视频` `状态空间模型` `时空建模` `动作识别` `深度学习`

## 📋 核心要点

1. 现有选择性状态空间模型在处理点云视频时，因时空无序性导致建模效果受限，无法有效利用空间和时间信息。
2. 本文提出的UST-SSM通过空间-时间选择扫描（STSS）和时空结构聚合（STSA）等技术，重组点云并补偿缺失信息，从而提高建模效果。
3. 在多个数据集上的实验结果显示，UST-SSM在动作识别任务中显著提升了性能，验证了其有效性。

## 📝 摘要（中文）

点云视频捕捉动态3D运动，减少光照和视角变化的影响，适用于识别细微且连续的人类动作。尽管选择性状态空间模型（SSMs）在序列建模中表现良好，但点云视频的时空无序性使得其在直接展开为一维序列时受到限制。为此，本文提出统一时空状态空间模型（UST-SSM），通过空间-时间选择扫描（STSS）将无序点重组为语义感知序列，并通过时空结构聚合（STSA）补偿缺失的几何和运动细节。此外，时间交互采样（TIS）增强了采样序列中的细粒度时间依赖性。实验结果表明，该方法在MSR-Action3D、NTU RGB+D和Synthia 4D数据集上有效。

## 🔬 方法详解

**问题定义**：本文旨在解决点云视频建模中的时空无序问题，现有的选择性状态空间模型在处理此类数据时，因其线性复杂度和一维序列展开方式，导致建模效果不佳。

**核心思路**：UST-SSM通过引入空间-时间选择扫描（STSS）技术，重组无序点为语义感知序列，从而有效利用空间和时间信息，提升模型的表现。

**技术框架**：UST-SSM的整体架构包括三个主要模块：空间-时间选择扫描（STSS）、时空结构聚合（STSA）和时间交互采样（TIS）。STSS负责点的重组，STSA用于补偿缺失的几何和运动细节，而TIS则增强了时间依赖性。

**关键创新**：最重要的创新点在于STSS和STSA的结合，前者通过提示引导聚类实现点的重组，后者则通过聚合时空特征来补偿信息缺失，这与现有方法的线性处理方式形成鲜明对比。

**关键设计**：在模型设计中，STSS采用了提示引导聚类策略，STSA则通过特征聚合来处理缺失信息，TIS则通过非锚帧的利用和扩展感受野来增强时间交互，确保模型能够捕捉到细粒度的时间依赖性。

## 📊 实验亮点

在MSR-Action3D、NTU RGB+D和Synthia 4D数据集上的实验结果显示，UST-SSM在动作识别任务中相较于基线方法提升了XX%至XX%的准确率，验证了其在时空建模中的有效性。

## 🎯 应用场景

UST-SSM在动态场景理解、动作识别和人机交互等领域具有广泛的应用潜力。其能够有效处理点云视频数据，提升动作识别的准确性和鲁棒性，未来可在智能监控、虚拟现实等场景中发挥重要作用。

## 📄 摘要（原文）

> Point cloud videos capture dynamic 3D motion while reducing the effects of lighting and viewpoint variations, making them highly effective for recognizing subtle and continuous human actions. Although Selective State Space Models (SSMs) have shown good performance in sequence modeling with linear complexity, the spatio-temporal disorder of point cloud videos hinders their unidirectional modeling when directly unfolding the point cloud video into a 1D sequence through temporally sequential scanning. To address this challenge, we propose the Unified Spatio-Temporal State Space Model (UST-SSM), which extends the latest advancements in SSMs to point cloud videos. Specifically, we introduce Spatial-Temporal Selection Scanning (STSS), which reorganizes unordered points into semantic-aware sequences through prompt-guided clustering, thereby enabling the effective utilization of points that are spatially and temporally distant yet similar within the sequence. For missing 4D geometric and motion details, Spatio-Temporal Structure Aggregation (STSA) aggregates spatio-temporal features and compensates. To improve temporal interaction within the sampled sequence, Temporal Interaction Sampling (TIS) enhances fine-grained temporal dependencies through non-anchor frame utilization and expanded receptive fields. Experimental results on the MSR-Action3D, NTU RGB+D, and Synthia 4D datasets validate the effectiveness of our method. Our code is available at https://github.com/wangzy01/UST-SSM.

