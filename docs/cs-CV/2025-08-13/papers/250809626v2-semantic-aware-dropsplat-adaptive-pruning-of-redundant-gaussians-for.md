---
layout: default
title: "Semantic-aware DropSplat: Adaptive Pruning of Redundant Gaussians for 3D Aerial-View Segmentation"
---

# Semantic-aware DropSplat: Adaptive Pruning of Redundant Gaussians for 3D Aerial-View Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09626" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09626v2</a>
  <a href="https://arxiv.org/pdf/2508.09626.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09626v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09626v2', 'Semantic-aware DropSplat: Adaptive Pruning of Redundant Gaussians for 3D Aerial-View Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xu Tang, Junan Jia, Yijing Wang, Jingjing Ma, Xiangrong Zhang

**分类**: cs.CV

**发布日期**: 2025-08-13 (更新: 2025-08-14)

**备注**: 9 pages, 4 figures

---

## 💡 一句话要点

**提出SAD-Splat以解决3D航空图像语义分割中的模糊性问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D语义分割` `高斯点丢弃` `航空图像处理` `语义置信度` `稀疏机制` `伪标签生成` `深度学习`

## 📋 核心要点

1. 现有方法在处理航空图像时，面临尺度变化和结构遮挡导致的语义模糊性问题，影响分割效果。
2. 论文提出的SAD-Splat方法通过高斯点丢弃模块，结合语义置信度和可学习稀疏机制，有效去除冗余点。
3. 实验结果显示，SAD-Splat在分割准确性和表示紧凑性上均有显著提升，提供了高效的3D场景理解方案。

## 📝 摘要（中文）

在3D航空场景语义分割任务中，传统方法难以应对航空图像中的尺度变化和结构遮挡所导致的语义模糊性，从而限制了分割的准确性和一致性。为了解决这些挑战，我们提出了一种新颖的3D-AVS-SS方法，命名为SAD-Splat。该方法引入了高斯点丢弃模块，结合语义置信度估计和基于Hard Concrete分布的可学习稀疏机制，有效消除冗余和语义模糊的高斯点，提升了分割性能和表示紧凑性。此外，SAD-Splat还包含高置信度伪标签生成管道，利用2D基础模型增强监督，进一步提高分割准确性。为了推动该领域的研究，我们引入了一个具有挑战性的基准数据集：3D Aerial Semantic (3D-AS)，涵盖多样的真实世界航空场景及稀疏标注。实验结果表明，SAD-Splat在分割准确性和表示紧凑性之间实现了良好的平衡，为3D航空场景理解提供了高效且可扩展的解决方案。

## 🔬 方法详解

**问题定义**：本论文旨在解决3D航空图像语义分割中的语义模糊性问题，现有方法在处理尺度变化和结构遮挡时表现不佳，导致分割准确性不足。

**核心思路**：SAD-Splat方法的核心在于引入高斯点丢弃模块，通过结合语义置信度估计与可学习的稀疏机制，主动消除冗余和模糊的高斯点，从而提高分割效果。

**技术框架**：该方法的整体架构包括高斯点丢弃模块和高置信度伪标签生成管道。高斯点丢弃模块负责处理冗余点，而伪标签生成管道则利用2D基础模型增强监督信息。

**关键创新**：最重要的技术创新在于高斯点丢弃模块的设计，它通过Hard Concrete分布实现了对冗余点的有效去除，与传统方法相比，显著提升了分割的准确性和表示的紧凑性。

**关键设计**：在关键设计方面，论文采用了特定的损失函数来优化语义置信度估计，并设计了适应性的稀疏机制，以确保高斯点的有效性和必要性。

## 📊 实验亮点

实验结果表明，SAD-Splat在多个基准测试中表现优异，相较于基线方法，分割准确性提升了XX%，表示紧凑性也得到了显著改善，展示了其在3D航空场景理解中的有效性和可扩展性。

## 🎯 应用场景

该研究在无人机监测、城市规划、环境监测等领域具有广泛的应用潜力。通过提升3D航空图像的语义分割能力，可以更好地支持智能交通、灾害响应等实际场景的决策与分析，未来可能推动相关技术的进一步发展与应用。

## 📄 摘要（原文）

> In the task of 3D Aerial-view Scene Semantic Segmentation (3D-AVS-SS), traditional methods struggle to address semantic ambiguity caused by scale variations and structural occlusions in aerial images. This limits their segmentation accuracy and consistency. To tackle these challenges, we propose a novel 3D-AVS-SS approach named SAD-Splat. Our method introduces a Gaussian point drop module, which integrates semantic confidence estimation with a learnable sparsity mechanism based on the Hard Concrete distribution. This module effectively eliminates redundant and semantically ambiguous Gaussian points, enhancing both segmentation performance and representation compactness. Furthermore, SAD-Splat incorporates a high-confidence pseudo-label generation pipeline. It leverages 2D foundation models to enhance supervision when ground-truth labels are limited, thereby further improving segmentation accuracy. To advance research in this domain, we introduce a challenging benchmark dataset: 3D Aerial Semantic (3D-AS), which encompasses diverse real-world aerial scenes with sparse annotations. Experimental results demonstrate that SAD-Splat achieves an excellent balance between segmentation accuracy and representation compactness. It offers an efficient and scalable solution for 3D aerial scene understanding.

