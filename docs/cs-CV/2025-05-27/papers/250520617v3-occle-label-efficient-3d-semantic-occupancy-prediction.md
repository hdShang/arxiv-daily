---
layout: default
title: "OccLE: Label-Efficient 3D Semantic Occupancy Prediction"
---

# OccLE: Label-Efficient 3D Semantic Occupancy Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20617" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20617v3</a>
  <a href="https://arxiv.org/pdf/2505.20617.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20617v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20617v3', 'OccLE: Label-Efficient 3D Semantic Occupancy Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Naiyu Fang, Zheyuan Zhou, Fayao Liu, Xulei Yang, Jiacheng Wei, Lemiao Qiu, Guosheng Lin

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-11-10)

**🔗 代码/项目**: [GITHUB](https://github.com/NerdFNY/OccLE)

---

## 💡 一句话要点

**提出OccLE以解决3D语义占用预测中的标注效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D语义占用预测` `标注效率` `自监督学习` `多模态融合` `图像与LiDAR` `深度学习` `自动驾驶`

## 📋 核心要点

1. 现有的3D语义占用预测方法要么依赖昂贵的全监督标注，要么在自监督学习中表现不佳，导致性能受限。
2. 本文提出的OccLE方法通过解耦语义和几何学习任务，利用图像和LiDAR输入进行特征融合，从而提高了标注效率。
3. 实验结果显示，OccLE在SemanticKITTI和Occ3D-nuScenes数据集上，仅使用10%的体素标注便实现了竞争性性能。

## 📝 摘要（中文）

3D语义占用预测为场景理解提供了直观且高效的方式，受到自动驾驶感知领域的广泛关注。现有方法要么依赖于全面监督，需昂贵的体素级标注，要么依赖自监督，提供的指导有限且性能欠佳。为了解决这些挑战，本文提出了OccLE，一种标注高效的3D语义占用预测方法，能够在仅有少量体素标注的情况下保持高性能。该方法通过解耦语义和几何学习任务，并融合两个任务学习的特征网格，最终实现语义占用预测。实验表明，OccLE在SemanticKITTI和Occ3D-nuScenes数据集上仅使用10%的体素标注便能取得竞争性性能。

## 🔬 方法详解

**问题定义**：本文旨在解决3D语义占用预测中的标注效率问题。现有方法通常需要大量的体素级标注，导致成本高昂，或依赖自监督学习，性能受到限制。

**核心思路**：OccLE的核心思路是解耦语义和几何学习任务，通过融合两个任务的特征网格来实现最终的语义占用预测。这种设计使得模型能够在有限的标注下仍然保持高性能。

**技术框架**：OccLE的整体架构包括两个主要分支：语义分支和几何分支。语义分支利用2D基础模型提取对齐的伪标签，而几何分支则结合图像和LiDAR输入，通过半监督学习增强几何学习。最终，两个分支的特征网格通过Dual Mamba进行融合，并采用散射累积投影来监督未标注的预测。

**关键创新**：OccLE的主要创新在于通过解耦语义和几何学习任务，利用图像和LiDAR的互补性来提高预测精度。这一方法与现有依赖全监督或自监督的技术有本质区别。

**关键设计**：在设计上，OccLE采用了散射累积投影技术来处理未标注数据，并在损失函数中引入了伪标签的对齐机制，以提升模型的学习效果。

## 📊 实验亮点

在实验中，OccLE在SemanticKITTI和Occ3D-nuScenes数据集上仅使用10%的体素标注，便实现了与全监督方法相当的性能，显示出其在标注效率和预测准确性上的显著提升。

## 🎯 应用场景

该研究在自动驾驶、机器人导航和智能城市等领域具有广泛的应用潜力。通过提高3D语义占用预测的标注效率，OccLE能够降低数据标注成本，促进更智能的环境感知和决策支持系统的发展。

## 📄 摘要（原文）

> 3D semantic occupancy prediction offers an intuitive and efficient scene understanding and has attracted significant interest in autonomous driving perception. Existing approaches either rely on full supervision, which demands costly voxel-level annotations, or on self-supervision, which provides limited guidance and yields suboptimal performance. To address these challenges, we propose OccLE, a Label-Efficient 3D Semantic Occupancy Prediction that takes images and LiDAR as inputs and maintains high performance with limited voxel annotations. Our intuition is to decouple the semantic and geometric learning tasks and then fuse the learned feature grids from both tasks for the final semantic occupancy prediction. Therefore, the semantic branch distills 2D foundation model to provide aligned pseudo labels for 2D and 3D semantic learning. The geometric branch integrates image and LiDAR inputs in cross-plane synergy based on their inherency, employing semi-supervision to enhance geometry learning. We fuse semantic-geometric feature grids through Dual Mamba and incorporate a scatter-accumulated projection to supervise unannotated prediction with aligned pseudo labels. Experiments show that OccLE achieves competitive performance with only 10\% of voxel annotations on the SemanticKITTI and Occ3D-nuScenes datasets. The code will be publicly released on https://github.com/NerdFNY/OccLE

