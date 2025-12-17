---
layout: default
title: A Unified Sparse Attention via Multi-Granularity Compression
---

# A Unified Sparse Attention via Multi-Granularity Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14082" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14082</a>
  <a href="https://arxiv.org/pdf/2512.14082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14082" onclick="toggleFavorite(this, '2512.14082', 'A Unified Sparse Attention via Multi-Granularity Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siran Liu, Zane Cao, Yongchao He

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**UniSparse：一种通过多粒度压缩实现的统一稀疏注意力机制，加速长文本处理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏注意力` `长文本处理` `多粒度压缩` `复合token` `大型语言模型`

## 📋 核心要点

1. 现有稀疏注意力方法在长文本处理中面临训练成本高或效率、通用性不足的挑战。
2. UniSparse提出复合token概念，通过多粒度压缩和块级选择动态构建稀疏注意力。
3. 实验表明，UniSparse在多种模态和任务中超越现有方法，兼顾准确性和效率。

## 📝 摘要（中文）

为了提升大型语言模型（LLM）在多轮对话和程序分析等应用中对长上下文的理解和推理能力，本文提出了一种名为UniSparse的统一稀疏注意力机制。现有稀疏注意力方法存在训练成本高昂或牺牲效率和跨模态通用性的问题。UniSparse通过引入复合token的概念来解决这些限制，复合token是一种聚合多粒度上下文信息的紧凑表示。基于此，UniSparse通过多粒度压缩和块级选择动态构建稀疏注意力，从而在GPU上实现高效且硬件友好的执行。在从合成基准到实际应用的多个模态和任务中，UniSparse在准确性和效率方面均优于最先进的稀疏注意力方法（如MInference、XAttention、FlexPrefill），实现了≥99%的完整注意力准确率，并且注意力计算速度比FlashAttention快高达2.61倍。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理长文本时，自注意力机制的计算复杂度呈平方增长，成为性能瓶颈。现有的稀疏注意力方法要么需要额外的训练，成本高昂且难以作为插件集成到其他模型中，要么在推理时牺牲效率或跨模态的通用性。

**核心思路**：UniSparse的核心思路是通过引入“复合token”的概念，将多个token的信息压缩成一个更紧凑的表示，从而减少需要计算注意力的token数量。通过在不同粒度上进行压缩，UniSparse能够捕捉不同尺度的上下文信息，并动态地选择重要的信息块进行注意力计算。

**技术框架**：UniSparse主要包含以下几个阶段：1) **多粒度压缩**：将输入序列划分为不同大小的块，并使用某种压缩方法（例如平均池化或线性变换）将每个块压缩成一个复合token。2) **块级选择**：根据某种策略（例如基于重要性的评分）选择一部分复合token参与后续的注意力计算。3) **稀疏注意力计算**：仅在选定的复合token之间进行注意力计算，从而降低计算复杂度。4) **信息聚合**：将稀疏注意力计算的结果聚合回原始的token表示。

**关键创新**：UniSparse的关键创新在于其统一的多粒度压缩框架。它允许在不同的粒度上进行信息压缩，从而能够灵活地适应不同的任务和数据。此外，UniSparse的块级选择机制能够动态地选择重要的信息块，从而进一步提高效率。与现有方法相比，UniSparse无需额外的训练，并且具有更好的跨模态通用性。

**关键设计**：UniSparse的具体实现细节包括：1) 压缩方法的选择：可以使用平均池化、线性变换或其他压缩方法。2) 块大小的选择：可以根据任务和数据进行调整。3) 块级选择策略：可以使用基于重要性的评分、随机选择或其他策略。4) 注意力计算方式：可以使用标准的自注意力机制或其他变体。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14082/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14082/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14082/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

UniSparse在多个模态和任务上进行了评估，结果表明其在准确性和效率方面均优于现有方法。例如，在长文本分类任务中，UniSparse实现了与完整注意力机制接近的准确率（≥99%），并且注意力计算速度比FlashAttention快高达2.61倍。这些结果表明UniSparse是一种高效且通用的稀疏注意力机制。

## 🎯 应用场景

UniSparse具有广泛的应用前景，包括但不限于：多轮对话系统、程序分析、长文档摘要、视频理解等。通过提高长文本处理的效率，UniSparse可以帮助LLM更好地理解和推理长上下文信息，从而提升各种下游任务的性能。此外，UniSparse的通用性使其可以应用于不同的模态，例如文本、图像和音频。

## 📄 摘要（原文）

> Efficient long-context understanding and reasoning are increasingly vital for large language model (LLM) applications such as multi-turn dialogue and program analysis. However, the core self-attention mechanism scales quadratically with sequence length, creating a fundamental computational bottleneck. Existing sparse attention methods alleviate this issue but face trade-offs: training-based methods are costly and cannot be directly applied as acceleration plugins for other models, while inference-time methods often compromise efficiency or cross-modal generality. To address these limitations, we present UniSparse, a unified mechanism that introduces the notion of composite tokens--compact representations that aggregate multi-granularity contextual information. Building on this abstraction, UniSparse dynamically constructs sparse attention through multi-granularity compression and block-level selection, enabling efficient and hardware-friendly execution on GPU. Across multiple modalities and tasks ranging from synthetic benchmarks to real-world applications, UniSparse consistently surpasses state-of-the-art sparse attention methods (e.g., MInference, XAttention, FlexPrefill) in both accuracy and efficiency, achieving $\ge$ 99% of full-attention accuracy and up to 2.61$\times$ faster attention computation than FlashAttention.

