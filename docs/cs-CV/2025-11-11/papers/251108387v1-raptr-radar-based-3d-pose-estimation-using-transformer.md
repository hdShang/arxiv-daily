---
layout: default
title: "RAPTR: Radar-based 3D Pose Estimation using Transformer"
---

# RAPTR: Radar-based 3D Pose Estimation using Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08387" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08387v1</a>
  <a href="https://arxiv.org/pdf/2511.08387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08387v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.08387v1', 'RAPTR: Radar-based 3D Pose Estimation using Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sorachi Kato, Ryoma Yataka, Pu Perry Wang, Pedro Miraldo, Takuya Fujihashi, Petros Boufounos

**分类**: cs.CV, cs.AI, eess.SP

**发布日期**: 2025-11-11

**备注**: 26 pages, Accepted to NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/merlresearch/radar-pose-transformer)

---

## 💡 一句话要点

**RAPTR：利用Transformer的雷达3D人体姿态估计，使用弱监督学习。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `雷达` `3D人体姿态估计` `Transformer` `弱监督学习` `室内场景` `可变形注意力` `深度学习`

## 📋 核心要点

1. 现有基于雷达的3D人体姿态估计依赖于昂贵的3D关键点标注，难以在复杂室内环境中获取。
2. RAPTR通过两阶段Transformer解码器，利用易于获取的3D BBox和2D关键点标签进行弱监督学习。
3. 实验结果表明，RAPTR在HIBER和MMVR数据集上显著优于现有方法，关节位置误差分别降低34.3%和76.9%。

## 📝 摘要（中文）

本文提出了一种基于雷达的室内3D人体姿态估计方法RAPTR，该方法使用Transformer，并在弱监督下进行训练。与需要精细3D关键点标签的传统方法不同，RAPTR仅使用3D BBox和2D关键点标签，这些标签更容易且更具可扩展性。RAPTR的特点是采用两阶段姿态解码器架构，并使用伪3D可变形注意力来增强多视角雷达特征的姿态/关节查询。姿态解码器使用3D模板损失估计初始3D姿态，以利用3D BBox标签并减轻深度模糊；关节解码器使用2D关键点标签和3D重力损失来细化初始姿态。在两个室内雷达数据集上的评估表明，RAPTR优于现有方法，在HIBER上将关节位置误差降低了34.3％，在MMVR上降低了76.9％。

## 🔬 方法详解

**问题定义**：现有基于雷达的3D人体姿态估计方法需要大量的精细3D关键点标注，这在复杂的室内环境中，尤其是在存在遮挡或多人场景下，标注成本非常高昂。因此，如何利用更容易获取的弱监督信息（如3D BBox和2D关键点）来实现精确的3D人体姿态估计是一个关键问题。

**核心思路**：RAPTR的核心思路是利用Transformer架构，通过两阶段解码器，结合3D BBox和2D关键点标签进行弱监督学习。第一阶段利用3D BBox信息估计初始姿态，第二阶段利用2D关键点信息细化姿态。这种设计旨在利用不同类型标签的优势，同时减轻深度模糊问题。

**技术框架**：RAPTR包含以下主要模块：1) 雷达特征提取模块（具体实现未知）；2) 姿态解码器：利用3D BBox标签和3D模板损失估计初始3D姿态；3) 关节解码器：利用2D关键点标签和3D重力损失细化初始姿态。姿态解码器和关节解码器都基于Transformer架构，并使用伪3D可变形注意力机制来增强特征表示。

**关键创新**：RAPTR的关键创新在于其弱监督学习框架和两阶段解码器架构。与现有方法相比，RAPTR不需要昂贵的3D关键点标注，而是利用更容易获取的3D BBox和2D关键点标签进行训练。此外，两阶段解码器能够有效地利用不同类型标签的信息，并减轻深度模糊问题。伪3D可变形注意力机制也是一个创新点，它能够有效地融合多视角雷达特征。

**关键设计**：RAPTR的关键设计包括：1) 3D模板损失：用于利用3D BBox标签，鼓励预测的3D姿态与BBox对齐；2) 3D重力损失：用于利用2D关键点标签，鼓励预测的3D姿态符合重力方向；3) 伪3D可变形注意力：用于融合多视角雷达特征，增强特征表示。具体的网络结构和参数设置在论文中应该有详细描述（未知）。

## 📊 实验亮点

RAPTR在HIBER和MMVR两个室内雷达数据集上进行了评估，实验结果表明，RAPTR显著优于现有方法。在HIBER数据集上，RAPTR将关节位置误差降低了34.3％，在MMVR数据集上，关节位置误差降低了76.9％。这些结果表明，RAPTR在基于雷达的3D人体姿态估计方面具有显著的优势。

## 🎯 应用场景

RAPTR在室内环境中的人体姿态估计具有广泛的应用前景，例如智能家居、老人看护、人机交互、安防监控等。该方法能够利用低成本的雷达传感器，在光线不足或存在遮挡的情况下，准确地估计人体姿态，从而实现更智能、更安全的应用。

## 📄 摘要（原文）

> Radar-based indoor 3D human pose estimation typically relied on fine-grained 3D keypoint labels, which are costly to obtain especially in complex indoor settings involving clutter, occlusions, or multiple people. In this paper, we propose \textbf{RAPTR} (RAdar Pose esTimation using tRansformer) under weak supervision, using only 3D BBox and 2D keypoint labels which are considerably easier and more scalable to collect. Our RAPTR is characterized by a two-stage pose decoder architecture with a pseudo-3D deformable attention to enhance (pose/joint) queries with multi-view radar features: a pose decoder estimates initial 3D poses with a 3D template loss designed to utilize the 3D BBox labels and mitigate depth ambiguities; and a joint decoder refines the initial poses with 2D keypoint labels and a 3D gravity loss. Evaluated on two indoor radar datasets, RAPTR outperforms existing methods, reducing joint position error by $34.3\%$ on HIBER and $76.9\%$ on MMVR. Our implementation is available at https://github.com/merlresearch/radar-pose-transformer.

