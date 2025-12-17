---
layout: default
title: InternSVG: Towards Unified SVG Tasks with Multimodal Large Language Models
---

# InternSVG: Towards Unified SVG Tasks with Multimodal Large Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11341" target="_blank" class="toolbar-btn">arXiv: 2510.11341v2</a>
    <a href="https://arxiv.org/pdf/2510.11341.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11341v2" 
            onclick="toggleFavorite(this, '2510.11341v2', 'InternSVG: Towards Unified SVG Tasks with Multimodal Large Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Haomin Wang, Jinhui Yin, Qi Wei, Wenguang Zeng, Lixin Gu, Shenglong Ye, Zhangwei Gao, Yaohui Wang, Yanting Zhang, Yuanqi Li, Yanwen Guo, Wenhai Wang, Kai Chen, Yu Qiao, Hongjie Zhang

**分类**: cs.CV

**发布日期**: 2025-10-13 (更新: 2025-11-04)

---

## 💡 一句话要点

**InternSVG：利用多模态大语言模型实现统一的SVG任务处理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `SVG建模` `统一建模` `数据集` `基准测试` `迁移学习` `计算机视觉`

## 📋 核心要点

1. 现有SVG建模方法面临数据集分散、任务间迁移性差以及难以处理结构复杂性等挑战。
2. 本文提出InternSVG，利用多模态大语言模型实现SVG理解、编辑和生成的统一建模。
3. 实验表明，InternSVG在SArena和现有基准测试中均优于其他领先的开源和商业模型。

## 📝 摘要（中文）

由于数据集分散、方法在任务间的迁移性有限以及结构复杂性难以处理，通用SVG建模仍然具有挑战性。为了解决这些问题，本文利用多模态大语言模型（MLLM）强大的迁移和泛化能力，实现了SVG理解、编辑和生成的统一建模。我们提出了InternSVG系列，这是一个集数据、基准和模型于一体的综合套件。其核心是SAgoge，这是最大、最全面的SVG任务多模态数据集，涵盖静态图形和动态动画。它覆盖了图标、长序列插图、科学图表和动态动画，支持不同难度级别的任务，并提供比以前的数据集更深层次的结构和更丰富的属性。基于此，我们引入了SArena，这是一个配套基准，具有全面的任务定义和标准化评估，与SAgoge所涵盖的领域和难度范围相一致。在此基础上，我们提出了InternSVG，一个统一的MLLM，用于SVG理解、编辑和生成，具有SVG特定的特殊token、基于子词的嵌入初始化以及一个两阶段训练策略，从短静态SVG到长序列插图和复杂动画逐步进行。这种统一的公式诱导了正向迁移并提高了整体性能。在SArena和先前的基准上的实验证实，InternSVG取得了显著的收益，并且始终优于领先的开源和专有模型。

## 🔬 方法详解

**问题定义**：现有SVG建模方法存在数据集碎片化，不同任务之间的方法迁移性差，难以处理SVG的结构复杂性等问题。这些问题限制了SVG建模的通用性和效率。

**核心思路**：本文的核心思路是利用多模态大语言模型（MLLM）强大的迁移学习和泛化能力，将SVG理解、编辑和生成任务统一到一个框架中。通过统一建模，可以实现任务之间的知识共享和正向迁移，从而提高整体性能。

**技术框架**：InternSVG的技术框架主要包括三个部分：SAgoge数据集、SArena基准测试和InternSVG模型。SAgoge是一个大规模多模态SVG数据集，涵盖静态图形和动态动画。SArena是一个配套的基准测试，用于评估模型在不同SVG任务上的性能。InternSVG是一个基于MLLM的统一模型，通过SVG特定的token、子词嵌入初始化和两阶段训练策略进行优化。

**关键创新**：本文的关键创新在于提出了一个统一的MLLM框架，用于处理SVG理解、编辑和生成任务。该框架通过统一的数据集、基准测试和模型，实现了任务之间的知识共享和正向迁移。此外，本文还提出了SVG特定的token和子词嵌入初始化方法，以提高模型对SVG结构的理解能力。

**关键设计**：InternSVG模型采用两阶段训练策略。第一阶段，模型在短静态SVG上进行预训练，学习基本的SVG结构和语义。第二阶段，模型在长序列插图和复杂动画上进行微调，提高模型处理复杂SVG的能力。模型使用SVG特定的特殊token来表示SVG元素，并使用子词嵌入初始化方法来提高模型对SVG结构的理解能力。损失函数包括语言建模损失和视觉损失，用于优化模型的生成和理解能力。

## 📊 实验亮点

InternSVG在SArena基准测试中取得了显著的性能提升，并在多个SVG任务上优于现有的开源和商业模型。具体来说，InternSVG在SVG理解、编辑和生成任务上的性能均超过了现有最佳模型，实现了SOTA水平。实验结果表明，InternSVG的统一建模方法能够有效地提高SVG建模的性能。

## 🎯 应用场景

InternSVG具有广泛的应用前景，包括图形设计、动画制作、科学可视化、教育等领域。它可以用于自动生成SVG图形、编辑现有SVG图形、理解SVG图形的内容等。该研究的成果有助于提高SVG建模的效率和质量，并促进SVG技术在各个领域的应用。

## 📄 摘要（原文）

> General SVG modeling remains challenging due to fragmented datasets, limited transferability of methods across tasks, and the difficulty of handling structural complexity. In response, we leverage the strong transfer and generalization capabilities of multimodal large language models (MLLMs) to achieve unified modeling for SVG understanding, editing, and generation. We present the InternSVG family, an integrated data-benchmark-model suite. At its core is SAgoge, the largest and most comprehensive multimodal dataset for SVG tasks, encompassing both static graphics and dynamic animations. It covers icons, long-sequence illustrations, scientific diagrams, and dynamic animations, supporting tasks of varied difficulty levels and providing deeper hierarchies with richer attributes compared to previous datasets. Based on this resource, we introduce SArena, a companion benchmark with comprehensive task definitions and standardized evaluation that aligns with the domains and difficulty spectrum covered by SAgoge. Building on these foundations, we propose InternSVG, a unified MLLM for SVG understanding, editing, and generation with SVG-specific special tokens, subword-based embedding initialization, and a two-stage training strategy that progresses from short static SVGs to long-sequence illustrations and complex animations. This unified formulation induces positive transfer and improves overall performance. Experiments on SArena and prior benchmark confirm that InternSVG achieves substantial gains and consistently outperforms leading open and proprietary counterparts.

