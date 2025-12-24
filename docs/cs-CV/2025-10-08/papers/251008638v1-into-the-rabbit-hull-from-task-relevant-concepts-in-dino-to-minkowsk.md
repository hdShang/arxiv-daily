---
layout: default
title: "Into the Rabbit Hull: From Task-Relevant Concepts in DINO to Minkowski Geometry"
---

# Into the Rabbit Hull: From Task-Relevant Concepts in DINO to Minkowski Geometry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08638" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08638v1</a>
  <a href="https://arxiv.org/pdf/2510.08638.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08638v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08638v1', 'Into the Rabbit Hull: From Task-Relevant Concepts in DINO to Minkowski Geometry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thomas Fel, Binxu Wang, Michael A. Lepori, Matthew Kowal, Andrew Lee, Randall Balestriero, Sonia Joseph, Ekdeep S. Lubana, Talia Konkle, Demba Ba, Martin Wattenberg

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**通过SAE分析DINOv2，揭示其表征的功能专业化和Minkowski几何特性。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `DINOv2` `可解释性` `稀疏自编码器` `Minkowski几何` `视觉Transformer`

## 📋 核心要点

1. DINOv2在目标识别等任务中表现出色，但其内部表征机制尚不明确，面临可解释性挑战。
2. 论文提出Minkowski表征假设（MRH），认为DINOv2的表征是原型概念的凸组合，并用SAE进行验证。
3. 实验表明，DINOv2在不同任务中展现功能专业化，且其表征具有非线性稀疏性和Minkowski几何特性。

## 📝 摘要（中文）

本文旨在探究DINOv2的感知机制。研究基于线性表征假设（LRH），利用稀疏自编码器（SAE）构建了一个包含32000个单元的字典，作为可解释性分析的基础。研究分为三个部分：首先，分析不同下游任务如何利用字典中的概念，揭示了功能专业化现象：分类任务利用“Elsewhere”概念实现学习到的否定；分割任务依赖于形成连贯子空间的边界检测器；深度估计任务利用与视觉神经科学原理相符的单目深度线索。其次，分析SAE学习到的概念的几何和统计特性，发现表征是部分稠密的，字典向更大的连贯性演进，偏离了最大正交理想。图像内的tokens占据低维局部连接集合，且在移除位置信息后仍然存在。最后，提出了一种改进的观点：tokens由原型（例如，动物中的兔子，颜色中的棕色，纹理中的蓬松）的凸混合形成。这种结构基于Gardenfors的概念空间，并与模型的多头注意力机制相符，从而定义了由原型界定的区域。提出了Minkowski表征假设（MRH），并检验了其经验特征及其对解释视觉Transformer表征的意义。

## 🔬 方法详解

**问题定义**：DINOv2等视觉Transformer模型在各种视觉任务中表现出色，但其内部表征机制，即模型究竟“看到”了什么，仍然是一个黑盒。现有方法难以有效解释这些模型的表征，缺乏对模型内部概念和几何结构的理解。

**核心思路**：论文的核心思路是通过稀疏自编码器（SAE）学习DINOv2的中间层表征，构建一个可解释的字典，然后分析这个字典中的概念在不同任务中的激活模式，以及这些概念的几何和统计特性。通过这种方式，揭示DINOv2内部表征的功能专业化和Minkowski几何结构。

**技术框架**：整体框架包括以下几个主要步骤：1. 使用DINOv2提取图像特征。2. 使用SAE对DINOv2的特征进行训练，得到一个包含32000个单元的字典。3. 分析字典中的概念在不同下游任务（分类、分割、深度估计）中的激活模式。4. 分析字典中概念的几何和统计特性，例如稀疏性、连贯性、正交性等。5. 提出Minkowski表征假设（MRH），并验证其经验特征。

**关键创新**：最重要的技术创新点在于提出了Minkowski表征假设（MRH），认为DINOv2的表征是由原型概念的凸组合形成的，这是一种对视觉Transformer表征的新颖解释。与传统的线性稀疏表征假设不同，MRH考虑了概念之间的非线性关系和几何结构。

**关键设计**：SAE的训练目标是最小化重构误差，同时鼓励稀疏性。具体来说，使用了L1正则化来约束SAE的激活。此外，论文还分析了字典中概念的连贯性，通过计算概念之间的相关性来衡量。在验证MRH时，论文分析了DINOv2的多头注意力机制，发现其产生的输出可以解释为原型概念的凸组合。

## 📊 实验亮点

实验结果表明，DINOv2在不同任务中展现出功能专业化，例如，分类任务利用“Elsewhere”概念实现学习到的否定，分割任务依赖于边界检测器。此外，实验还发现DINOv2的表征具有非线性稀疏性和Minkowski几何特性，支持了Minkowski表征假设。

## 🎯 应用场景

该研究成果可应用于提升视觉Transformer模型的可解释性和可控性，例如，通过理解模型内部的概念，可以更好地进行模型调试和优化。此外，该研究还可以促进对视觉认知的理解，为开发更智能的视觉系统提供理论基础。

## 📄 摘要（原文）

> DINOv2 is routinely deployed to recognize objects, scenes, and actions; yet the nature of what it perceives remains unknown. As a working baseline, we adopt the Linear Representation Hypothesis (LRH) and operationalize it using SAEs, producing a 32,000-unit dictionary that serves as the interpretability backbone of our study, which unfolds in three parts.
>   In the first part, we analyze how different downstream tasks recruit concepts from our learned dictionary, revealing functional specialization: classification exploits "Elsewhere" concepts that fire everywhere except on target objects, implementing learned negations; segmentation relies on boundary detectors forming coherent subspaces; depth estimation draws on three distinct monocular depth cues matching visual neuroscience principles.
>   Following these functional results, we analyze the geometry and statistics of the concepts learned by the SAE. We found that representations are partly dense rather than strictly sparse. The dictionary evolves toward greater coherence and departs from maximally orthogonal ideals (Grassmannian frames). Within an image, tokens occupy a low dimensional, locally connected set persisting after removing position. These signs suggest representations are organized beyond linear sparsity alone.
>   Synthesizing these observations, we propose a refined view: tokens are formed by combining convex mixtures of archetypes (e.g., a rabbit among animals, brown among colors, fluffy among textures). This structure is grounded in Gardenfors' conceptual spaces and in the model's mechanism as multi-head attention produces sums of convex mixtures, defining regions bounded by archetypes. We introduce the Minkowski Representation Hypothesis (MRH) and examine its empirical signatures and implications for interpreting vision-transformer representations.

