---
layout: default
title: "SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation"
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

**提出SegGraph，利用SAM分割图进行少样本3D部件分割**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少样本学习` `3D部件分割` `图神经网络` `SAM分割` `几何特征学习`

## 📋 核心要点

1. 现有少样本3D部件分割方法在聚合2D基础模型知识到3D时，忽略了几何结构或SAM分组线索，导致分割不足和标签不一致。
2. SegGraph通过构建SAM分割图，显式学习分割掩码中的几何特征，并利用图神经网络进行特征传播，从而实现更精确的部件分割。
3. 在PartNet-E数据集上的实验表明，SegGraph显著优于现有方法，尤其在小组件和部件边界上表现出色，证明了其几何理解能力。

## 📝 摘要（中文）

本文提出了一种用于少样本3D部件分割的新框架。最近的研究表明，2D基础模型在低样本3D部件分割方面具有巨大的潜力。然而，如何有效地将2D知识从基础模型聚合到3D仍然是一个开放的问题。现有方法要么忽略3D特征学习的几何结构，要么忽略SAM提供的高质量分组线索，导致分割不足和部件标签不一致。我们设计了一种新颖的基于SAM分割图的传播方法，名为SegGraph，以显式地学习SAM分割掩码中编码的几何特征。我们的方法通过对分割之间的相互重叠和邻接关系进行建模来编码几何特征，同时保持分割内的语义一致性。我们构建了一个分割图，在概念上类似于地图集，其中节点表示分割，边表示它们之间的空间关系（重叠/邻接）。每个节点自适应地调节2D基础模型特征，然后通过图神经网络传播以学习全局几何结构。为了加强分割内的语义一致性，我们使用一种新颖的视角方向加权融合将分割特征映射到3D点，从而衰减低质量分割的贡献。在PartNet-E上的大量实验表明，我们的方法优于所有竞争基线至少6.9个百分点的mIoU。进一步的分析表明，SegGraph在小组件和部件边界上实现了特别强大的性能，证明了其卓越的几何理解能力。

## 🔬 方法详解

**问题定义**：论文旨在解决少样本3D部件分割问题。现有方法在利用2D基础模型（如SAM）的知识时，要么忽略了3D几何结构的学习，要么未能充分利用SAM分割结果中蕴含的高质量分组信息，导致分割结果不准确，部件标签不一致。这些方法无法有效区分细小的部件，并且在部件边界处的分割效果较差。

**核心思路**：论文的核心思路是构建一个基于SAM分割结果的图结构（SegGraph），显式地对分割区域之间的几何关系（重叠和邻接）进行建模，并利用图神经网络学习全局几何结构。通过这种方式，模型可以更好地理解3D形状的结构信息，从而提高分割的准确性。同时，论文还考虑了分割区域内部的语义一致性，避免低质量分割区域对最终结果产生负面影响。

**技术框架**：SegGraph框架主要包含以下几个阶段：1) 利用SAM对3D形状进行分割，得到一系列2D分割掩码；2) 构建分割图，其中节点表示分割区域，边表示分割区域之间的空间关系（重叠和邻接）；3) 使用图神经网络在分割图上进行特征传播，学习全局几何结构；4) 将分割特征映射回3D点，并使用视角方向加权融合来增强分割区域内部的语义一致性。

**关键创新**：论文的关键创新在于：1) 提出了SegGraph，一种显式地对分割区域之间的几何关系进行建模的图结构；2) 使用图神经网络在SegGraph上进行特征传播，从而学习全局几何结构；3) 提出了视角方向加权融合方法，用于增强分割区域内部的语义一致性。与现有方法相比，SegGraph能够更好地利用SAM分割结果中的几何信息，从而提高分割的准确性。

**关键设计**：在构建SegGraph时，节点特征由2D基础模型提取的特征表示，边的权重根据分割区域之间的重叠和邻接程度计算。图神经网络采用GCN结构，损失函数包括分割损失和一致性损失。视角方向加权融合根据视角方向与分割区域法向量的夹角来确定权重，从而降低低质量分割区域的贡献。

## 📊 实验亮点

实验结果表明，SegGraph在PartNet-E数据集上优于所有竞争基线至少6.9个百分点的mIoU。尤其在小组件和部件边界上，SegGraph表现出更强的性能，证明了其卓越的几何理解能力。消融实验验证了SegGraph中各个模块的有效性，例如，分割图结构和视角方向加权融合都对最终性能有显著贡献。

## 🎯 应用场景

该研究成果可应用于机器人感知、三维场景理解、CAD模型分析等领域。例如，机器人可以利用该技术更准确地识别和操作物体部件，从而实现更复杂的任务。在CAD模型分析中，该技术可以帮助用户快速理解模型的结构和功能，提高设计效率。未来，该技术有望扩展到更多领域，如医疗影像分析、文物修复等。

## 📄 摘要（原文）

> This work presents a novel framework for few-shot 3D part segmentation. Recent advances have demonstrated the significant potential of 2D foundation models for low-shot 3D part segmentation. However, it is still an open problem that how to effectively aggregate 2D knowledge from foundation models to 3D. Existing methods either ignore geometric structures for 3D feature learning or neglects the high-quality grouping clues from SAM, leading to under-segmentation and inconsistent part labels. We devise a novel SAM segment graph-based propagation method, named SegGraph, to explicitly learn geometric features encoded within SAM's segmentation masks. Our method encodes geometric features by modeling mutual overlap and adjacency between segments while preserving intra-segment semantic consistency. We construct a segment graph, conceptually similar to an atlas, where nodes represent segments and edges capture their spatial relationships (overlap/adjacency). Each node adaptively modulates 2D foundation model features, which are then propagated via a graph neural network to learn global geometric structures. To enforce intra-segment semantic consistency, we map segment features to 3D points with a novel view-direction-weighted fusion attenuating contributions from low-quality segments. Extensive experiments on PartNet-E demonstrate that our method outperforms all competing baselines by at least 6.9 percent mIoU. Further analysis reveals that SegGraph achieves particularly strong performance on small components and part boundaries, demonstrating its superior geometric understanding. The code is available at: https://github.com/YueyangHu2000/SegGraph.

