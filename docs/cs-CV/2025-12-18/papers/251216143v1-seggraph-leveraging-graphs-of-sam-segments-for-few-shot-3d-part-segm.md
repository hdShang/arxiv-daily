---
layout: default
title: SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation
---

# SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16143" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16143v1</a>
  <a href="https://arxiv.org/pdf/2512.16143.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16143v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16143v1', 'SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yueyang Hu, Haiyong Jiang, Haoxuan Song, Jun Xiao, Hao Pan

**分类**: cs.CV

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/YueyangHu2000/SegGraph)

---

## 💡 一句话要点

**SegGraph：利用SAM分割图进行少样本3D部件分割**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少样本学习` `3D部件分割` `图神经网络` `SAM分割` `几何特征学习`

## 📋 核心要点

1. 现有少样本3D部件分割方法未能有效聚合2D基础模型的知识到3D，忽略了几何结构或SAM分组线索。
2. SegGraph通过构建SAM分割图，显式学习分割掩码中的几何特征，并保持段内语义一致性。
3. 实验表明，SegGraph在PartNet-E数据集上显著优于现有方法，尤其在小组件和部件边界上表现出色。

## 📝 摘要（中文）

本文提出了一种新颖的少样本3D部件分割框架。最近的研究表明，2D基础模型在低样本3D部件分割方面具有巨大的潜力。然而，如何有效地将来自基础模型的2D知识聚合到3D仍然是一个开放的问题。现有方法要么忽略3D特征学习的几何结构，要么忽略来自SAM的高质量分组线索，导致分割不足和部件标签不一致。我们设计了一种新颖的基于SAM分割图的传播方法，名为SegGraph，以显式地学习SAM分割掩码中编码的几何特征。我们的方法通过建模段之间的相互重叠和邻接关系来编码几何特征，同时保持段内语义一致性。我们构建了一个分割图，在概念上类似于地图集，其中节点代表分割，边代表它们之间的空间关系（重叠/邻接）。每个节点自适应地调节2D基础模型特征，然后通过图神经网络传播以学习全局几何结构。为了加强段内语义一致性，我们使用一种新颖的视角方向加权融合将段特征映射到3D点，从而衰减来自低质量段的贡献。在PartNet-E上的大量实验表明，我们的方法优于所有竞争基线至少6.9个百分点的mIoU。进一步的分析表明，SegGraph在小组件和部件边界上实现了特别强大的性能，证明了其卓越的几何理解能力。

## 🔬 方法详解

**问题定义**：论文旨在解决少样本3D部件分割问题。现有方法在利用2D基础模型知识时，要么忽略了3D几何结构的学习，要么未能充分利用SAM分割提供的高质量分组信息，导致分割结果不完整，部件标签不一致。这些方法无法有效捕捉部件之间的空间关系，尤其是在小部件和部件边界处表现不佳。

**核心思路**：论文的核心思路是构建一个基于SAM分割的图结构（SegGraph），显式地学习和利用分割区域之间的几何关系。通过图神经网络进行信息传播，可以有效地聚合来自不同分割区域的特征，并增强对全局几何结构的理解。同时，通过视角方向加权融合，保证了段内语义一致性，减少了低质量分割的影响。

**技术框架**：SegGraph框架主要包含以下几个阶段：1) 利用SAM生成2D分割掩码；2) 构建分割图，节点代表分割区域，边表示分割区域之间的空间关系（重叠和邻接）；3) 使用图神经网络在分割图上进行特征传播，每个节点自适应地调节2D基础模型特征；4) 通过视角方向加权融合，将分割区域特征映射到3D点云，进行最终的部件分割。

**关键创新**：该方法的核心创新在于利用SAM分割图来显式地建模和学习3D几何特征。与以往方法相比，SegGraph能够更好地捕捉部件之间的空间关系，尤其是在小部件和部件边界处。此外，视角方向加权融合机制能够有效抑制低质量分割的影响，提高分割的鲁棒性。

**关键设计**：分割图的构建方式是关键。论文考虑了分割区域之间的重叠和邻接关系，使用不同的权重来表示这些关系。图神经网络的具体结构（例如，使用的图卷积算子）以及视角方向加权融合的权重计算方式也是重要的设计细节。损失函数的设计也需要考虑如何平衡分割精度和部件一致性。

## 📊 实验亮点

SegGraph在PartNet-E数据集上取得了显著的性能提升，mIoU指标超过所有基线方法至少6.9%。尤其在小组件和部件边界上的分割效果提升明显，证明了其对几何结构的卓越理解能力。消融实验验证了分割图结构和视角方向加权融合的有效性。

## 🎯 应用场景

该研究成果可应用于机器人感知、自动驾驶、三维场景理解等领域。例如，机器人可以利用该技术更准确地识别和分割物体部件，从而更好地进行操作和交互。在自动驾驶领域，可以用于精确识别车辆、行人等目标的不同部件，提高安全性。此外，该技术还可用于CAD模型分析、虚拟现实等领域。

## 📄 摘要（原文）

> This work presents a novel framework for few-shot 3D part segmentation. Recent advances have demonstrated the significant potential of 2D foundation models for low-shot 3D part segmentation. However, it is still an open problem that how to effectively aggregate 2D knowledge from foundation models to 3D. Existing methods either ignore geometric structures for 3D feature learning or neglects the high-quality grouping clues from SAM, leading to under-segmentation and inconsistent part labels. We devise a novel SAM segment graph-based propagation method, named SegGraph, to explicitly learn geometric features encoded within SAM's segmentation masks. Our method encodes geometric features by modeling mutual overlap and adjacency between segments while preserving intra-segment semantic consistency. We construct a segment graph, conceptually similar to an atlas, where nodes represent segments and edges capture their spatial relationships (overlap/adjacency). Each node adaptively modulates 2D foundation model features, which are then propagated via a graph neural network to learn global geometric structures. To enforce intra-segment semantic consistency, we map segment features to 3D points with a novel view-direction-weighted fusion attenuating contributions from low-quality segments. Extensive experiments on PartNet-E demonstrate that our method outperforms all competing baselines by at least 6.9 percent mIoU. Further analysis reveals that SegGraph achieves particularly strong performance on small components and part boundaries, demonstrating its superior geometric understanding. The code is available at: https://github.com/YueyangHu2000/SegGraph.

