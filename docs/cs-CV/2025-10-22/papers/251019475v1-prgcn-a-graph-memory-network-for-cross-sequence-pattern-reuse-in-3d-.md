---
layout: default
title: PRGCN: A Graph Memory Network for Cross-Sequence Pattern Reuse in 3D Human Pose Estimation
---

# PRGCN: A Graph Memory Network for Cross-Sequence Pattern Reuse in 3D Human Pose Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19475" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19475v1</a>
  <a href="https://arxiv.org/pdf/2510.19475.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19475v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.19475v1', 'PRGCN: A Graph Memory Network for Cross-Sequence Pattern Reuse in 3D Human Pose Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuoyang Xie, Yibo Zhao, Hui Huang, Riwei Wang, Zan Gao

**分类**: cs.CV

**发布日期**: 2025-10-22

**备注**: 29 pages, 6 figures, 6 tables

---

## 💡 一句话要点

**提出PRGCN，利用图记忆网络实现跨序列人体姿态模式复用，提升3D人体姿态估计精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `3D人体姿态估计` `图卷积网络` `模式复用` `记忆网络` `时空建模`

## 📋 核心要点

1. 现有基于视频的3D人体姿态估计方法孤立地处理每个序列，忽略了跨序列的结构规律和重复运动模式。
2. PRGCN通过图记忆网络学习和存储姿态原型，并利用注意力机制动态检索，为姿态估计提供结构化的先验知识。
3. 在Human3.6M和MPI-INF-3DHP数据集上，PRGCN取得了state-of-the-art的结果，MPJPE分别达到37.1mm和13.4mm。

## 📝 摘要（中文）

单目3D人体姿态估计是一个根本上不适定的逆问题，因为2D到3D的提升存在固有的深度模糊性。现有的基于视频的方法利用时间上下文来增强空间推理，但它们存在一个关键的范式限制：孤立地处理每个序列，从而无法利用贯穿于跨序列人体运动的强大结构规律和重复运动模式。本文提出了一种模式复用图卷积网络（PRGCN），该框架将姿态估计形式化为模式检索和适应的问题。PRGCN的核心是一个图记忆库，它学习并存储一组紧凑的姿态原型，编码为关系图，这些原型通过注意力机制动态检索以提供结构化的先验知识。这些先验知识通过记忆驱动的图卷积与硬编码的解剖约束自适应地融合，确保了几何合理性。为了用鲁棒的时空特征支持这种检索过程，我们设计了一个双流混合架构，该架构协同结合了基于Mamba的状态空间模型的线性复杂性、局部时间建模与自注意力的全局关系能力。在Human3.6M和MPI-INF-3DHP基准上的大量评估表明，PRGCN建立了一个新的最先进水平，分别实现了37.1mm和13.4mm的MPJPE，同时表现出增强的跨域泛化能力。我们的工作表明，长期被忽视的跨序列模式复用机制对于推动该领域的发展至关重要，将范式从每个序列的优化转向累积知识学习。

## 🔬 方法详解

**问题定义**：单目3D人体姿态估计由于2D到3D的深度模糊性，是一个不适定的逆问题。现有方法通常独立处理每个视频序列，忽略了不同序列之间人体运动模式的相似性和重复性，导致无法充分利用跨序列的结构信息，限制了模型的性能和泛化能力。

**核心思路**：PRGCN的核心思想是将姿态估计问题转化为模式检索和适应的问题。通过构建一个图记忆库，存储一系列代表性的姿态原型，并在估计过程中，根据输入序列的特征动态检索相关的姿态原型，作为先验知识指导姿态估计。这种跨序列的模式复用机制能够有效利用人体运动的结构规律，提高姿态估计的准确性和鲁棒性。

**技术框架**：PRGCN采用双流混合架构。首先，使用Mamba-based状态空间模型提取局部时序特征，并利用自注意力机制捕捉全局关系。然后，通过注意力机制从图记忆库中检索相关的姿态原型，这些原型被编码为关系图。检索到的姿态原型与硬编码的解剖约束一起，通过记忆驱动的图卷积网络进行融合，最终得到3D人体姿态估计结果。

**关键创新**：PRGCN的关键创新在于引入了跨序列的模式复用机制，通过图记忆网络学习和存储姿态原型，并利用注意力机制动态检索。这种方法打破了传统方法独立处理每个序列的限制，能够有效利用跨序列的结构信息，提高姿态估计的性能。此外，双流混合架构结合了Mamba和自注意力的优势，能够更好地捕捉时空特征。

**关键设计**：图记忆库中的每个姿态原型都被编码为一个关系图，节点表示人体关键点，边表示关键点之间的关系。注意力机制用于计算输入序列特征与每个姿态原型之间的相似度，并根据相似度加权融合姿态原型。记忆驱动的图卷积网络利用检索到的姿态原型和解剖约束，对姿态估计结果进行约束和优化。损失函数包括MPJPE损失和正则化损失，用于约束姿态估计的准确性和几何合理性。

## 📊 实验亮点

PRGCN在Human3.6M和MPI-INF-3DHP数据集上取得了显著的性能提升，MPJPE分别达到37.1mm和13.4mm，超越了现有的state-of-the-art方法。此外，PRGCN还表现出增强的跨域泛化能力，表明其能够更好地适应不同的场景和数据分布。这些结果验证了跨序列模式复用机制的有效性。

## 🎯 应用场景

PRGCN在单目3D人体姿态估计领域具有广泛的应用前景，可应用于人机交互、虚拟现实、运动分析、智能监控等领域。通过提高姿态估计的准确性和鲁棒性，可以为这些应用提供更可靠的基础，例如，在运动分析中，可以更准确地分析运动员的动作，提高训练效果；在智能监控中，可以更准确地识别异常行为，提高安全性。

## 📄 摘要（原文）

> Monocular 3D human pose estimation remains a fundamentally ill-posed inverse problem due to the inherent depth ambiguity in 2D-to-3D lifting. While contemporary video-based methods leverage temporal context to enhance spatial reasoning, they operate under a critical paradigm limitation: processing each sequence in isolation, thereby failing to exploit the strong structural regularities and repetitive motion patterns that pervade human movement across sequences. This work introduces the Pattern Reuse Graph Convolutional Network (PRGCN), a novel framework that formalizes pose estimation as a problem of pattern retrieval and adaptation. At its core, PRGCN features a graph memory bank that learns and stores a compact set of pose prototypes, encoded as relational graphs, which are dynamically retrieved via an attention mechanism to provide structured priors. These priors are adaptively fused with hard-coded anatomical constraints through a memory-driven graph convolution, ensuring geometrical plausibility. To underpin this retrieval process with robust spatiotemporal features, we design a dual-stream hybrid architecture that synergistically combines the linear-complexity, local temporal modeling of Mamba-based state-space models with the global relational capacity of self-attention. Extensive evaluations on Human3.6M and MPI-INF-3DHP benchmarks demonstrate that PRGCN establishes a new state-of-the-art, achieving an MPJPE of 37.1mm and 13.4mm, respectively, while exhibiting enhanced cross-domain generalization capability. Our work posits that the long-overlooked mechanism of cross-sequence pattern reuse is pivotal to advancing the field, shifting the paradigm from per-sequence optimization towards cumulative knowledge learning.

