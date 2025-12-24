---
layout: default
title: "HoliTom: Holistic Token Merging for Fast Video Large Language Models"
---

# HoliTom: Holistic Token Merging for Fast Video Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21334" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21334v3</a>
  <a href="https://arxiv.org/pdf/2505.21334.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21334v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21334v3', 'HoliTom: Holistic Token Merging for Fast Video Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kele Shao, Keda Tao, Can Qin, Haoxuan You, Yang Sui, Huan Wang

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-10-10)

**备注**: code link: https://github.com/cokeshao/HoliTom

---

## 💡 一句话要点

**提出HoliTom以解决视频大语言模型的计算效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `大语言模型` `标记合并` `计算效率` `时空处理` `多模态学习`

## 📋 核心要点

1. 现有视频大语言模型在处理长视频时存在冗余标记导致的计算效率低下问题。
2. HoliTom通过全球冗余感知的时间分割和时空合并，提出了一种新的无训练的整体标记合并框架。
3. 实验表明，HoliTom在计算成本上降低至6.9% FLOPs，同时保持99.1%的性能，显著提升了推理效率。

## 📝 摘要（中文）

视频大语言模型（视频LLMs）在视频理解方面表现出色，但由于冗余视频标记，面临显著的计算效率问题。现有的标记修剪方法虽然提供了解决方案，但在LLM内部进行的修剪方法（如FastV）在浅层中引入了固有的计算开销。相对而言，外部LLM修剪方法主要解决单帧或有限时间窗口内的空间冗余，忽视了长视频序列中的全球时间动态和相关性。为进一步减少冗余，本文提出了一种新颖的无训练的整体标记合并框架HoliTom，通过全球冗余感知的时间分割进行外部LLM修剪，随后进行时空合并，减少视觉标记超过90%，显著减轻了LLM的计算负担。评估结果显示，该方法在LLaVA-OneVision-7B上实现了6.9%的FLOPs计算成本，同时保持99.1%的原始性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视频大语言模型在处理长视频时因冗余标记导致的计算效率低下问题。现有方法在LLM内部修剪时引入了额外的计算开销，而外部修剪方法则未能充分利用视频的全局时间动态。

**核心思路**：HoliTom的核心思想是通过全球冗余感知的时间分割进行外部LLM修剪，结合时空合并技术，以减少冗余标记，从而显著降低计算负担。该方法不需要训练，便于快速应用。

**技术框架**：HoliTom的整体架构包括两个主要模块：首先是全球冗余感知的时间分割，识别并去除冗余的时间段；其次是时空合并，通过合并相似的标记来减少视觉标记的数量。

**关键创新**：HoliTom的创新在于将外部LLM修剪与内部LLM标记相似性合并相结合，充分利用了两者的优势，显著提升了处理效率。与现有方法相比，该方法在减少计算成本的同时保持了高性能。

**关键设计**：在设计中，HoliTom采用了基于相似性的标记合并策略，确保合并后的标记仍然能够有效传递视频信息。此外，参数设置和损失函数的选择经过精心调整，以优化合并效果和计算效率。

## 📊 实验亮点

实验结果显示，HoliTom在LLaVA-OneVision-7B上实现了6.9%的FLOPs计算成本，同时保持99.1%的原始性能。此外，时间到第一个标记（TTFT）减少了2.28倍，解码吞吐量加速了1.32倍，展示了其在推理效率上的显著提升。

## 🎯 应用场景

HoliTom的研究成果在视频理解、视频生成和多模态学习等领域具有广泛的应用潜力。通过提高视频大语言模型的计算效率，该方法能够加速视频分析和处理，促进实时应用的发展，如智能监控、自动驾驶和内容推荐系统等。

## 📄 摘要（原文）

> Video large language models (video LLMs) excel at video comprehension but face significant computational inefficiency due to redundant video tokens. Existing token pruning methods offer solutions. However, approaches operating within the LLM (inner-LLM pruning), such as FastV, incur intrinsic computational overhead in shallow layers. In contrast, methods performing token pruning before the LLM (outer-LLM pruning) primarily address spatial redundancy within individual frames or limited temporal windows, neglecting the crucial global temporal dynamics and correlations across longer video sequences. This leads to sub-optimal spatio-temporal reduction and does not leverage video compressibility fully. Crucially, the synergistic potential and mutual influence of combining these strategies remain unexplored. To further reduce redundancy, we introduce HoliTom, a novel training-free holistic token merging framework. HoliTom employs outer-LLM pruning through global redundancy-aware temporal segmentation, followed by spatial-temporal merging to reduce visual tokens by over 90%, significantly alleviating the LLM's computational burden. Complementing this, we introduce a robust inner-LLM token similarity-based merging approach, designed for superior performance and compatibility with outer-LLM pruning. Evaluations demonstrate our method's promising efficiency-performance trade-off on LLaVA-OneVision-7B, reducing computational costs to 6.9% of FLOPs while maintaining 99.1% of the original performance. Furthermore, we achieve a 2.28x reduction in Time-To-First-Token (TTFT) and a 1.32x acceleration in decoding throughput, highlighting the practical benefits of our integrated pruning approach for efficient video LLMs inference.

