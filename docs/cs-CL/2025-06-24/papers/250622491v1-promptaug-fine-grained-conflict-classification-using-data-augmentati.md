---
layout: default
title: "PromptAug: Fine-grained Conflict Classification Using Data Augmentation"
---

# PromptAug: Fine-grained Conflict Classification Using Data Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22491" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22491v1</a>
  <a href="https://arxiv.org/pdf/2506.22491.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22491v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22491v1', 'PromptAug: Fine-grained Conflict Classification Using Data Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Oliver Warke, Joemon M. Jose, Faegheh Hasibi, Jan Breitsohl

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-06-24

---

## 💡 一句话要点

**提出PromptAug以解决社交媒体冲突行为分类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据增强` `冲突检测` `社交媒体` `情感分析` `大型语言模型`

## 📋 核心要点

1. 现有方法在处理社交媒体冲突行为分类时面临数据稀缺和标注困难的挑战。
2. PromptAug通过利用大型语言模型进行数据增强，生成高质量的训练数据以提高分类性能。
3. 实验结果显示，PromptAug在冲突和情感数据集上分别提高了2%的准确率和F1分数，验证了其有效性。

## 📝 摘要（中文）

随着社交媒体上冲突行为的增加，开发有效的分类模型以检测有害行为变得至关重要。机器学习的性能高度依赖于训练数据的质量，而高质量的标注数据在识别冲突行为等细微任务中往往稀缺且昂贵。本文提出了PromptAug，一种基于大型语言模型（LLM）的数据增强方法，旨在克服数据稀缺带来的挑战。PromptAug在冲突和情感数据集上实现了2%的准确率和F1分数的显著提升。通过对比分析，本文还识别出增强文本中的四种问题模式，为敏感任务的数据增强提供了独特的跨学科评估。

## 🔬 方法详解

**问题定义**：本文旨在解决社交媒体上冲突行为分类中数据稀缺和标注困难的问题。现有方法往往依赖于高质量的标注数据，但这类数据难以获得，限制了模型的性能。

**核心思路**：PromptAug的核心思路是利用大型语言模型（LLM）进行数据增强，以生成多样化且高质量的训练数据，从而提高分类模型的准确性和鲁棒性。

**技术框架**：PromptAug的整体架构包括数据收集、数据增强和模型训练三个主要模块。首先，收集冲突相关的文本数据；然后，使用LLM进行数据增强，生成新的训练样本；最后，将增强后的数据用于训练分类模型。

**关键创新**：PromptAug的主要创新在于其针对冲突行为分类的特定设计，能够在遵循LLM的内容生成限制的同时，生成有效的训练数据。这与传统的数据增强方法有本质区别，后者往往无法处理敏感内容。

**关键设计**：在设计上，PromptAug采用了特定的提示策略，以引导LLM生成符合要求的文本。同时，设置了多样性评估指标，以确保生成内容的多样性和有效性，从而提升模型的泛化能力。

## 📊 实验亮点

实验结果表明，PromptAug在冲突和情感数据集上实现了2%的准确率和F1分数的显著提升，验证了其在数据稀缺场景下的有效性。与其他数据增强方法相比，PromptAug展现出更高的性能和适用性。

## 🎯 应用场景

PromptAug可广泛应用于社交媒体监控、在线社区管理和情感分析等领域，帮助研究人员和企业更有效地识别和应对有害行为。其方法论的创新也为其他领域的数据增强提供了借鉴，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Given the rise of conflicts on social media, effective classification models to detect harmful behaviours are essential. Following the garbage-in-garbage-out maxim, machine learning performance depends heavily on training data quality. However, high-quality labelled data, especially for nuanced tasks like identifying conflict behaviours, is limited, expensive, and difficult to obtain. Additionally, as social media platforms increasingly restrict access to research data, text data augmentation is gaining attention as an alternative to generate training data. Augmenting conflict-related data poses unique challenges due to Large Language Model (LLM) guardrails that prevent generation of offensive content. This paper introduces PromptAug, an innovative LLM-based data augmentation method. PromptAug achieves statistically significant improvements of 2% in both accuracy and F1-score on conflict and emotion datasets. To thoroughly evaluate PromptAug against other data augmentation methods we conduct a robust evaluation using extreme data scarcity scenarios, quantitative diversity analysis and a qualitative thematic analysis. The thematic analysis identifies four problematic patterns in augmented text: Linguistic Fluidity, Humour Ambiguity, Augmented Content Ambiguity, and Augmented Content Misinterpretation.
>   Overall, this work presents PromptAug as an effective method for augmenting data in sensitive tasks like conflict detection, offering a unique, interdisciplinary evaluation grounded in both natural language processing and social science methodology.

