---
layout: default
title: $\mathcal{V}isi\mathcal{P}runer$: Decoding Discontinuous Cross-Modal Dynamics for Efficient Multimodal LLMs
---

# $\mathcal{V}isi\mathcal{P}runer$: Decoding Discontinuous Cross-Modal Dynamics for Efficient Multimodal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17205" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17205v1</a>
  <a href="https://arxiv.org/pdf/2510.17205.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17205v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17205v1', '$\mathcal{V}isi\mathcal{P}runer$: Decoding Discontinuous Cross-Modal Dynamics for Efficient Multimodal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingqi Fan, Anhao Zhao, Jinlan Fu, Junlong Tong, Hui Su, Yijie Pan, Wei Zhang, Xiaoyu Shen

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-20

**备注**: EMNLP 2025 Main

**🔗 代码/项目**: [GITHUB](https://github.com/EIT-NLP/VisiPruner)

---

## 💡 一句话要点

**VisiPruner：解码多模态LLM中的非连续跨模态动态，实现高效剪枝**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `token剪枝` `跨模态交互` `计算效率` `视觉语言任务`

## 📋 核心要点

1. 现有MLLM的token剪枝方法缺乏对跨模态信息处理和融合机制的深入理解。
2. VisiPruner通过分析MLLM的跨模态交互过程，提出了一种无需训练的剪枝框架。
3. VisiPruner在LLaVA-v1.5 7B上实现了显著的计算效率提升，并具有良好的泛化能力。

## 📝 摘要（中文）

多模态大型语言模型(MLLMs)在视觉-语言任务中表现出色，但由于注意力计算随多模态token数量呈二次增长，导致计算开销巨大。尽管已经有一些关于MLLM中token剪枝的工作，但它们缺乏对MLLM如何处理和融合多模态信息的根本理解。通过系统分析，我们揭示了一个三阶段的跨模态交互过程：(1)浅层识别任务意图，视觉token充当被动注意力接收器；(2)跨模态融合在中间层突然发生，由少数关键视觉token驱动；(3)深层丢弃视觉token，仅关注语言细化。基于这些发现，我们提出了VisiPruner，一个无需训练的剪枝框架，在LLaVA-v1.5 7B上最多可减少99%的视觉相关注意力计算和53.9%的FLOPs。它显著优于现有的token剪枝方法，并可推广到不同的MLLM。除了剪枝，我们的见解还为通过将模型架构与其内在的逐层处理动态对齐来训练高效的MLLM提供了可操作的指导。

## 🔬 方法详解

**问题定义**：多模态大型语言模型（MLLMs）在视觉-语言任务中表现出色，但其计算复杂度高，特别是注意力机制的计算量随输入token数量呈平方增长。现有的token剪枝方法虽然尝试减少计算量，但缺乏对MLLM内部跨模态信息处理机制的深入理解，导致剪枝效果不佳或影响模型性能。

**核心思路**：该论文的核心思路是通过深入分析MLLM内部的跨模态交互过程，揭示不同层对视觉和语言信息的处理方式，从而有针对性地进行token剪枝。作者发现MLLM存在一个三阶段的跨模态交互过程，并据此设计剪枝策略。

**技术框架**：VisiPruner是一个无需训练的剪枝框架，它依赖于对预训练MLLM的分析。该框架主要包含以下几个阶段：1) 通过实验分析MLLM各层对视觉和语言信息的处理方式，确定跨模态交互的关键层；2) 基于分析结果，设计针对不同层的剪枝策略，例如在浅层保留更多视觉token以辅助任务意图识别，在深层则更多关注语言信息；3) 应用剪枝策略，减少视觉相关的注意力计算。

**关键创新**：该论文最重要的创新在于对MLLM跨模态交互过程的深入分析，揭示了其三阶段特性，并据此提出了针对性的剪枝策略。与现有方法相比，VisiPruner不是盲目地进行token剪枝，而是基于对模型内部机制的理解，从而在保证模型性能的同时，显著降低计算量。

**关键设计**：VisiPruner的关键设计在于其无需训练的特性，避免了额外的训练开销。此外，该方法根据不同层的特点采用不同的剪枝策略，例如在浅层，视觉token主要作为“注意力接收器”，因此可以适当保留；而在深层，视觉token的重要性降低，可以进行更激进的剪枝。具体的剪枝比例和策略需要根据实验分析确定。

## 📊 实验亮点

VisiPruner在LLaVA-v1.5 7B模型上实现了显著的性能提升，最多可减少99%的视觉相关注意力计算和53.9%的FLOPs，同时保持了模型性能。实验结果表明，VisiPruner优于现有的token剪枝方法，并且具有良好的泛化能力，可以应用于不同的MLLM。

## 🎯 应用场景

VisiPruner可应用于各种需要高效多模态信息处理的场景，例如移动设备上的视觉问答、机器人导航、智能监控等。通过降低MLLM的计算复杂度，该研究有助于将这些强大的模型部署到资源受限的平台上，并加速多模态人工智能技术的普及。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved strong performance across vision-language tasks, but suffer from significant computational overhead due to the quadratic growth of attention computations with the number of multimodal tokens. Though efforts have been made to prune tokens in MLLMs, \textit{they lack a fundamental understanding of how MLLMs process and fuse multimodal information.} Through systematic analysis, we uncover a \textbf{three-stage} cross-modal interaction process: (1) Shallow layers recognize task intent, with visual tokens acting as passive attention sinks; (2) Cross-modal fusion occurs abruptly in middle layers, driven by a few critical visual tokens; (3) Deep layers discard vision tokens, focusing solely on linguistic refinement. Based on these findings, we propose \emph{VisiPruner}, a training-free pruning framework that reduces up to 99\% of vision-related attention computations and 53.9\% of FLOPs on LLaVA-v1.5 7B. It significantly outperforms existing token pruning methods and generalizes across diverse MLLMs. Beyond pruning, our insights further provide actionable guidelines for training efficient MLLMs by aligning model architecture with its intrinsic layer-wise processing dynamics. Our code is available at: https://github.com/EIT-NLP/VisiPruner.

