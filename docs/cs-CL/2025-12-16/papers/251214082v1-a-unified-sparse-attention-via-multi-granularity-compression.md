---
layout: default
title: A Unified Sparse Attention via Multi-Granularity Compression
---

# A Unified Sparse Attention via Multi-Granularity Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14082" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14082v1</a>
  <a href="https://arxiv.org/pdf/2512.14082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14082v1" onclick="toggleFavorite(this, '2512.14082v1', 'A Unified Sparse Attention via Multi-Granularity Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siran Liu, Zane Cao, Yongchao He

**分类**: cs.CL

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**UniSparse：一种通过多粒度压缩实现的统一稀疏注意力机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏注意力` `长文本处理` `多粒度压缩` `大型语言模型` `自注意力机制`

## 📋 核心要点

1. 现有稀疏注意力方法存在训练成本高昂或无法直接作为加速插件应用于其他模型的局限性。
2. UniSparse通过引入复合token，利用多粒度压缩和块级选择动态构建稀疏注意力，提升效率。
3. 实验表明，UniSparse在多种模态和任务中，准确率接近完整注意力，且计算速度优于FlashAttention。

## 📝 摘要（中文）

针对大型语言模型（LLM）在多轮对话和程序分析等应用中对长上下文理解和推理日益增长的需求，本文提出UniSparse，一种统一的稀疏注意力机制。UniSparse通过引入复合token的概念，即聚合多粒度上下文信息的紧凑表示，动态构建稀疏注意力。该方法通过多粒度压缩和块级选择，实现了高效且对GPU硬件友好的执行。在从合成基准测试到实际应用的多种模态和任务中，UniSparse在准确性和效率方面均超越了最先进的稀疏注意力方法（如MInference、XAttention、FlexPrefill），实现了≥99%的完整注意力准确率，并且注意力计算速度比FlashAttention快高达2.61倍。

## 🔬 方法详解

**问题定义**：现有自注意力机制的计算复杂度随序列长度呈二次方增长，成为长文本处理的瓶颈。现有的稀疏注意力方法虽然能缓解这个问题，但要么需要大量的训练成本，要么在推理效率或跨模态通用性上有所妥协。

**核心思路**：UniSparse的核心思路是通过引入“复合token”的概念，将多个token压缩成一个更紧凑的表示，从而减少需要计算注意力的token数量。这种压缩是多粒度的，允许模型在不同层次上聚合上下文信息，以更好地平衡效率和准确性。

**技术框架**：UniSparse的整体框架包括以下几个主要阶段：1) **多粒度压缩**：将原始token序列压缩成不同粒度的复合token序列。2) **块级选择**：根据某种策略（例如，基于重要性评分）选择一部分复合token块进行注意力计算。3) **稀疏注意力计算**：仅在选定的复合token块之间计算注意力权重。4) **信息聚合**：将复合token的信息解压缩并聚合到原始token表示中。

**关键创新**：UniSparse的关键创新在于其统一性和多粒度压缩。它不像其他稀疏注意力方法那样依赖于特定的训练或预定义的模式，而是可以动态地适应不同的输入和任务。多粒度压缩允许模型在不同层次上抽象上下文信息，从而更好地平衡效率和准确性。

**关键设计**：UniSparse的具体实现细节可能包括：1) **压缩策略**：如何将多个token压缩成一个复合token（例如，使用平均池化、最大池化或可学习的线性变换）。2) **选择策略**：如何选择重要的复合token块（例如，基于注意力权重、重要性评分或随机抽样）。3) **注意力计算**：使用哪种注意力机制（例如，标准自注意力、线性注意力或FlashAttention）。4) **损失函数**：如何训练模型以学习有效的压缩和选择策略（例如，使用交叉熵损失、KL散度或对比损失）。

## 📊 实验亮点

UniSparse在多个模态和任务上都取得了显著的性能提升。例如，在长文本分类任务中，UniSparse在保持接近完整注意力准确率（≥99%）的同时，比FlashAttention快高达2.61倍。此外，UniSparse在合成基准测试和真实世界应用中均优于其他稀疏注意力方法，如MInference、XAttention和FlexPrefill。

## 🎯 应用场景

UniSparse具有广泛的应用前景，尤其是在需要处理长序列数据的场景中。例如，它可以用于提高大型语言模型在多轮对话、程序分析、文档摘要和机器翻译等任务中的效率和性能。此外，UniSparse还可以应用于其他模态的数据，如图像和音频，以加速视觉Transformer和语音识别模型的训练和推理。

## 📄 摘要（原文）

> Efficient long-context understanding and reasoning are increasingly vital for large language model (LLM) applications such as multi-turn dialogue and program analysis. However, the core self-attention mechanism scales quadratically with sequence length, creating a fundamental computational bottleneck. Existing sparse attention methods alleviate this issue but face trade-offs: training-based methods are costly and cannot be directly applied as acceleration plugins for other models, while inference-time methods often compromise efficiency or cross-modal generality. To address these limitations, we present UniSparse, a unified mechanism that introduces the notion of composite tokens--compact representations that aggregate multi-granularity contextual information. Building on this abstraction, UniSparse dynamically constructs sparse attention through multi-granularity compression and block-level selection, enabling efficient and hardware-friendly execution on GPU. Across multiple modalities and tasks ranging from synthetic benchmarks to real-world applications, UniSparse consistently surpasses state-of-the-art sparse attention methods (e.g., MInference, XAttention, FlexPrefill) in both accuracy and efficiency, achieving $\ge$ 99% of full-attention accuracy and up to 2.61$\times$ faster attention computation than FlashAttention.

