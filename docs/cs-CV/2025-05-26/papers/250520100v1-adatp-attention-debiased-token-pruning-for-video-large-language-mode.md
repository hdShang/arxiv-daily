---
layout: default
title: "AdaTP: Attention-Debiased Token Pruning for Video Large Language Models"
---

# AdaTP: Attention-Debiased Token Pruning for Video Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20100" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20100v1</a>
  <a href="https://arxiv.org/pdf/2505.20100.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20100v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20100v1', 'AdaTP: Attention-Debiased Token Pruning for Video Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengyuan Sun, Leqi Shen, Hui Chen, Sicheng Zhao, Jungong Han, Guiguang Ding

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出AdaTP以解决视频大语言模型中的注意力偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频大语言模型` `注意力机制` `标记修剪` `计算效率` `多模态学习`

## 📋 核心要点

1. 现有视频大语言模型在处理大量视觉标记时面临计算开销大的挑战，影响了其应用效率。
2. 提出的AdaTP通过集成全局和局部去偏差模块，有效修剪视觉标记，减少计算负担。
3. 实验结果显示，AdaTP在多个视频理解基准上表现优异，使用的FLOPs仅为原模型的27.3%，性能未受影响。

## 📝 摘要（中文）

视频大语言模型（Video LLMs）在视频理解任务中取得了显著成果，但由于从多个视频帧生成的大量视觉标记，计算开销较大。现有的视觉标记压缩方法通常依赖于语言模型的注意力分数作为指导，但这些分数存在固有偏差：全局偏差使得模型倾向于关注视觉标记序列的两端，而局部偏差则导致在不同帧中对相同空间位置的过度集中。为了解决注意力偏差问题，本文提出了注意力去偏差标记修剪（AdaTP），该方法集成了两个专门的去偏差模块，分别针对全局和局部注意力偏差。我们的实验表明，AdaTP在不需要额外训练的情况下，显著降低了视频LLMs的计算开销，同时保持了原始模型的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视频大语言模型中由于视觉标记数量庞大而导致的计算开销问题。现有方法依赖的注意力分数存在全局和局部偏差，影响了标记的有效性和模型的性能。

**核心思路**：提出的AdaTP方法通过引入全局和局部去偏差模块，针对性地修剪视觉标记，旨在减少计算开销的同时保持模型性能。这样的设计使得模型在处理视频数据时更加高效。

**技术框架**：AdaTP的整体架构包括两个主要模块：全局去偏差模块和局部去偏差模块。全局模块关注视觉标记序列的整体结构，而局部模块则针对同一空间位置的标记进行优化。

**关键创新**：AdaTP的核心创新在于其去偏差机制，通过专门设计的模块有效消除了注意力偏差，显著提升了视觉标记的选择效率，与传统方法相比，具有更好的性能和更低的计算需求。

**关键设计**：在设计中，AdaTP不需要额外的训练过程，直接在现有模型上进行标记修剪。关键参数设置和损失函数的选择经过精心调整，以确保模型在修剪后仍能保持高效的性能。

## 📊 实验亮点

实验结果表明，AdaTP在LLaVA-OneVision-7B模型上实现了性能的无损保持，同时计算开销仅为原模型的27.3%。这一结果展示了AdaTP在视频理解任务中的优越性，达到了当前最先进的性能水平。

## 🎯 应用场景

该研究的潜在应用领域包括视频分析、智能监控、自动驾驶等场景，能够显著提升视频理解任务的效率和准确性。未来，AdaTP有望在更广泛的多模态学习任务中发挥重要作用，推动相关技术的发展。

## 📄 摘要（原文）

> Video Large Language Models (Video LLMs) have achieved remarkable results in video understanding tasks. However, they often suffer from heavy computational overhead due to the large number of visual tokens generated from multiple video frames. Existing visual token compression methods often rely on attention scores from language models as guidance. However, these scores exhibit inherent biases: global bias reflects a tendency to focus on the two ends of the visual token sequence, while local bias leads to an over-concentration on the same spatial positions across different frames. To address the issue of attention bias, we propose $\textbf{A}$ttention-$\textbf{D}$ebi$\textbf{a}$sed $\textbf{T}$oken $\textbf{P}$runing for Video Large Language Models ($\textbf{AdaTP}$), a novel token pruning pipeline for Video LLMs. AdaTP integrates two dedicated debiasing modules into the pipeline, targeting global attention bias and local attention bias, respectively. Without the need for additional training, our method significantly reduces the computational overhead of Video LLMs while retaining the performance of vanilla models. Extensive evaluation shows that AdaTP achieves state-of-the-art performance in various commonly used video understanding benchmarks. In particular, on LLaVA-OneVision-7B, AdaTP maintains performance without degradation while using only up to $27.3\%$ FLOPs compared to the vanilla model. Our code will be released soon.

