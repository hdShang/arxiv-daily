---
layout: default
title: Schoenfeld's Anatomy of Mathematical Reasoning by Language Models
---

# Schoenfeld's Anatomy of Mathematical Reasoning by Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19995" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19995v1</a>
  <a href="https://arxiv.org/pdf/2512.19995.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19995v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19995v1', 'Schoenfeld\'s Anatomy of Mathematical Reasoning by Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ming Li, Chenrui Fan, Yize Cheng, Soheil Feizi, Tianyi Zhou

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出ThinkARM框架，剖析语言模型数学推理过程中的认知结构与步骤**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `数学推理` `认知结构` `推理步骤` `Episode Theory`

## 📋 核心要点

1. 现有方法难以识别和分析语言模型推理过程中的认知结构和具体步骤，仅停留在表面统计层面。
2. 论文提出ThinkARM框架，将推理轨迹抽象为分析、探索、实现、验证等功能性步骤，便于分析。
3. 实验表明，ThinkARM能揭示推理模型和非推理模型在思维动态和结构上的差异，并诊断关键步骤。

## 📝 摘要（中文）

大型语言模型越来越多地展示出推理轨迹，但其潜在的认知结构和步骤仍然难以识别和分析，而不仅仅是表面层面的统计。我们采用Schoenfeld的Episode Theory作为一种归纳的、中等尺度的视角，并引入ThinkARM（模型推理剖析），这是一个可扩展的框架，它将推理轨迹显式地抽象为功能性的推理步骤，如分析、探索、实现、验证等。当应用于不同模型解决数学问题时，这种抽象揭示了可重复的思维动态以及推理模型和非推理模型之间的结构差异，这些差异在token级别视图中并不明显。我们进一步提出了两个诊断案例研究，表明探索是与正确性相关的关键分支步骤，并且面向效率的方法选择性地抑制评估反馈步骤，而不是统一地缩短响应。总之，我们的结果表明，episode级别的表示使推理步骤显式化，从而能够系统地分析现代语言模型中推理是如何构建、稳定和改变的。

## 🔬 方法详解

**问题定义**：现有方法难以深入理解大型语言模型在数学问题求解过程中的推理机制。仅仅关注token级别的统计信息无法揭示模型内部的认知结构和推理步骤，导致难以诊断和改进模型的推理能力。因此，需要一种更高级别的抽象方法来分析模型的推理过程。

**核心思路**：论文的核心思路是借鉴Schoenfeld的Episode Theory，将复杂的推理过程分解为一系列功能性的推理步骤（Episodes），例如分析问题、探索解决方案、实施解决方案以及验证结果。通过将模型的推理轨迹映射到这些预定义的Episodes，可以更清晰地理解模型的推理流程和潜在问题。

**技术框架**：ThinkARM框架主要包含以下几个阶段：1) **推理轨迹提取**：从语言模型的输出中提取推理过程的文本记录。2) **Episode识别**：使用自然语言处理技术（例如，文本分类或序列标注）将推理轨迹中的每个步骤映射到预定义的Episode类型（例如，分析、探索、实现、验证）。3) **推理动态分析**：分析不同Episode之间的转换关系和频率，从而揭示模型的推理模式和结构。4) **诊断性案例研究**：通过特定的案例研究，分析不同Episode对最终结果的影响，并识别模型推理过程中的瓶颈。

**关键创新**：ThinkARM的关键创新在于它提供了一种可扩展的、中间尺度的抽象方法，可以将语言模型的推理轨迹转化为功能性的推理步骤。这种抽象方法使得研究人员可以更系统地分析模型的推理过程，并识别影响模型性能的关键因素。与传统的token级别分析相比，ThinkARM能够揭示更深层次的认知结构和推理动态。

**关键设计**：ThinkARM框架的关键设计包括：1) **Episode类型的定义**：根据Schoenfeld的Episode Theory，定义了一组通用的推理步骤，例如分析、探索、实现、验证等。2) **Episode识别模型**：使用预训练的语言模型（例如，BERT或RoBERTa）对推理轨迹进行分类，从而识别每个步骤所属的Episode类型。3) **推理动态分析方法**：使用图论或马尔可夫链等方法分析不同Episode之间的转换关系，从而揭示模型的推理模式。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19995v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19995v1/figures/word_cloud.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19995v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ThinkARM能够有效区分推理模型和非推理模型，并揭示它们在思维动态和结构上的差异。案例研究表明，探索步骤与正确性密切相关，而效率优化方法可能会抑制评估反馈步骤。这些发现为改进语言模型的推理能力提供了有价值的见解。

## 🎯 应用场景

该研究成果可应用于提升大型语言模型的数学推理能力，例如通过优化模型的探索策略或增强验证环节。此外，该框架还可用于评估不同模型的推理能力，并为模型设计提供指导。该方法具有通用性，可以推广到其他需要复杂推理的任务中，例如代码生成、逻辑推理等。

## 📄 摘要（原文）

> Large language models increasingly expose reasoning traces, yet their underlying cognitive structure and steps remain difficult to identify and analyze beyond surface-level statistics. We adopt Schoenfeld's Episode Theory as an inductive, intermediate-scale lens and introduce ThinkARM (Anatomy of Reasoning in Models), a scalable framework that explicitly abstracts reasoning traces into functional reasoning steps such as Analysis, Explore, Implement, Verify, etc. When applied to mathematical problem solving by diverse models, this abstraction reveals reproducible thinking dynamics and structural differences between reasoning and non-reasoning models, which are not apparent from token-level views. We further present two diagnostic case studies showing that exploration functions as a critical branching step associated with correctness, and that efficiency-oriented methods selectively suppress evaluative feedback steps rather than uniformly shortening responses. Together, our results demonstrate that episode-level representations make reasoning steps explicit, enabling systematic analysis of how reasoning is structured, stabilized, and altered in modern language models.

