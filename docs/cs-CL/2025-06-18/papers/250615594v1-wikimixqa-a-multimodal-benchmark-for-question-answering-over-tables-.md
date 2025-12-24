---
layout: default
title: "WikiMixQA: A Multimodal Benchmark for Question Answering over Tables and Charts"
---

# WikiMixQA: A Multimodal Benchmark for Question Answering over Tables and Charts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15594" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15594v1</a>
  <a href="https://arxiv.org/pdf/2506.15594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15594v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15594v1', 'WikiMixQA: A Multimodal Benchmark for Question Answering over Tables and Charts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Negar Foroutan, Angelika Romanou, Matin Ansaripour, Julian Martin Eisenschlos, Karl Aberer, Rémi Lebret

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-18

**备注**: ACL 2025 (Findings)

---

## 💡 一句话要点

**提出WikiMixQA基准以解决多模态文档理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `文档理解` `视觉-语言模型` `基准测试` `信息综合`

## 📋 核心要点

1. 现有方法在处理复杂文档布局、表格和图表时面临显著挑战，尤其是在长上下文的情况下。
2. 论文提出WikiMixQA基准，包含1000个多项选择题，强调跨模态推理，要求模型综合多种信息。
3. 实验结果显示，专有模型在直接上下文下准确率约70%，但在长文档检索时显著下降，开源模型表现更差。

## 📝 摘要（中文）

文档在信息保存和传播中至关重要，通常包含复杂的布局、表格和图表，这对自动文档理解（DU）提出了重大挑战。尽管视觉-语言大模型（VLLMs）在多个任务上取得了进展，但其在处理长上下文视觉输入方面的有效性仍不明确。本文提出WikiMixQA，一个包含1000个多项选择题（MCQs）的基准，旨在评估从4000个维基百科页面提取的表格和图表的跨模态推理。与现有基准不同，WikiMixQA强调复杂推理，要求模型综合来自多种模态的信息。我们评估了12个最先进的视觉-语言模型，发现尽管专有模型在提供直接上下文时能达到约70%的准确率，但在需要从长文档中检索信息时，其性能显著下降。GPT-4-o是唯一在此设置中超过50%准确率的模型，而开源模型的表现则相对较差，最高准确率为27%。这些发现突显了长上下文多模态推理的挑战，并确立了WikiMixQA作为推动文档理解研究的重要基准。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态文档理解中的长上下文推理问题，现有方法在处理复杂信息时表现不佳，尤其在需要综合多种模态信息时。

**核心思路**：提出WikiMixQA基准，通过设计1000个多项选择题，要求模型在表格和图表中进行复杂推理，从而评估其跨模态理解能力。

**技术框架**：整体架构包括数据收集、问题设计和模型评估三个主要模块。数据来自4000个维基百科页面，问题设计强调多模态信息的综合，模型评估则采用多种视觉-语言模型进行对比。

**关键创新**：WikiMixQA的创新在于其强调复杂推理和多模态信息的综合，区别于现有基准的简单问答任务，推动了文档理解的研究进展。

**关键设计**：在模型评估中，采用了多种视觉-语言模型，包括专有和开源模型，设置了不同的上下文长度，以测试模型在长文档检索中的表现。

## 📊 实验亮点

实验结果显示，专有模型在直接上下文下的准确率约为70%，但在长文档检索时显著下降，只有GPT-4-o模型在此设置中超过50%的准确率，而开源模型的最高准确率仅为27%。这些结果凸显了长上下文多模态推理的挑战。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、智能问答系统和自动文档分析等。WikiMixQA基准的建立将为多模态文档理解的研究提供新的评估标准，促进相关技术的发展，提升实际应用的效果。

## 📄 摘要（原文）

> Documents are fundamental to preserving and disseminating information, often incorporating complex layouts, tables, and charts that pose significant challenges for automatic document understanding (DU). While vision-language large models (VLLMs) have demonstrated improvements across various tasks, their effectiveness in processing long-context vision inputs remains unclear. This paper introduces WikiMixQA, a benchmark comprising 1,000 multiple-choice questions (MCQs) designed to evaluate cross-modal reasoning over tables and charts extracted from 4,000 Wikipedia pages spanning seven distinct topics. Unlike existing benchmarks, WikiMixQA emphasizes complex reasoning by requiring models to synthesize information from multiple modalities. We evaluate 12 state-of-the-art vision-language models, revealing that while proprietary models achieve ~70% accuracy when provided with direct context, their performance deteriorates significantly when retrieval from long documents is required. Among these, GPT-4-o is the only model exceeding 50% accuracy in this setting, whereas open-source models perform considerably worse, with a maximum accuracy of 27%. These findings underscore the challenges of long-context, multi-modal reasoning and establish WikiMixQA as a crucial benchmark for advancing document understanding research.

