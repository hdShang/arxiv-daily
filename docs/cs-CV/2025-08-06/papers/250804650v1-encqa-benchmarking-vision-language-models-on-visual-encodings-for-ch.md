---
layout: default
title: "EncQA: Benchmarking Vision-Language Models on Visual Encodings for Charts"
---

# EncQA: Benchmarking Vision-Language Models on Visual Encodings for Charts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04650" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04650v1</a>
  <a href="https://arxiv.org/pdf/2508.04650.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04650v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04650v1', 'EncQA: Benchmarking Vision-Language Models on Visual Encodings for Charts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kushin Mukherjee, Donghao Ren, Dominik Moritz, Yannick Assogba

**分类**: cs.CV

**发布日期**: 2025-08-06

**DOI**: [10.1109/TVCG.2025.3634249](https://doi.org/10.1109/TVCG.2025.3634249)

---

## 💡 一句话要点

**提出EncQA基准以提升图表理解的视觉推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态视觉语言模型` `图表理解` `视觉推理` `基准测试` `数据可视化` `合成问答对`

## 📋 核心要点

1. 现有的多模态视觉语言模型在图表理解方面的进展未能全面反映视觉推理能力的多样性。
2. 本文提出EncQA基准，通过系统性覆盖视觉编码和分析任务，来提升图表理解能力。
3. 实验结果显示，模型在不同编码和任务之间的表现差异显著，且模型规模的增加并未带来预期的性能提升。

## 📝 摘要（中文）

多模态视觉语言模型（VLMs）在图表理解基准上取得了持续进展，但这一进展并未充分反映出图表解读所需的视觉推理能力的广度。为此，本文提出了EncQA，一个基于可视化文献的新基准，旨在系统性覆盖图表理解所需的视觉编码和分析任务。EncQA提供了2076对合成问答对，涵盖六种视觉编码通道和八种任务。对九种最先进的VLM的评估显示，模型在同一任务中的不同编码和不同任务之间的表现差异显著，且许多任务-编码对的表现并未随着模型规模的增加而提升。结果表明，提升图表理解能力需要针对特定视觉推理缺口的策略，而不仅仅是扩大模型或数据集的规模。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态视觉语言模型在图表理解中未能充分捕捉视觉推理能力的不足，尤其是在不同视觉编码和任务之间的表现差异。

**核心思路**：EncQA基准通过提供2076对合成问答对，系统性覆盖六种视觉编码通道和八种分析任务，旨在全面评估和提升图表理解能力。

**技术框架**：EncQA的整体架构包括数据生成模块、视觉编码通道的定义、任务设计和评估模块，确保对图表理解的多维度考察。

**关键创新**：EncQA的创新在于其系统性设计，涵盖了多种视觉编码和任务，填补了现有基准在视觉推理能力评估上的空白。

**关键设计**：在参数设置上，EncQA确保了问答对的平衡分布，损失函数设计上考虑了不同任务的特性，以便更好地评估模型在各个视觉编码下的表现。

## 📊 实验亮点

实验结果显示，九种最先进的VLM在不同视觉编码和任务之间的表现差异显著，且许多任务-编码对的性能并未随着模型规模的增加而提升，表明需要针对性策略来解决视觉推理的不足。

## 🎯 应用场景

该研究的潜在应用领域包括数据可视化、商业智能和教育等，能够帮助开发更智能的图表分析工具，提高用户对复杂数据的理解能力。未来，EncQA基准可能推动更多针对视觉推理的研究，促进多模态模型的进一步发展。

## 📄 摘要（原文）

> Multimodal vision-language models (VLMs) continue to achieve ever-improving scores on chart understanding benchmarks. Yet, we find that this progress does not fully capture the breadth of visual reasoning capabilities essential for interpreting charts. We introduce EncQA, a novel benchmark informed by the visualization literature, designed to provide systematic coverage of visual encodings and analytic tasks that are crucial for chart understanding. EncQA provides 2,076 synthetic question-answer pairs, enabling balanced coverage of six visual encoding channels (position, length, area, color quantitative, color nominal, and shape) and eight tasks (find extrema, retrieve value, find anomaly, filter values, compute derived value exact, compute derived value relative, correlate values, and correlate values relative). Our evaluation of 9 state-of-the-art VLMs reveals that performance varies significantly across encodings within the same task, as well as across tasks. Contrary to expectations, we observe that performance does not improve with model size for many task-encoding pairs. Our results suggest that advancing chart understanding requires targeted strategies addressing specific visual reasoning gaps, rather than solely scaling up model or dataset size.

