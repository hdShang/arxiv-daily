---
layout: default
title: A Unified Sparse Attention via Multi-Granularity Compression
---

# A Unified Sparse Attention via Multi-Granularity Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14082" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14082v1</a>
  <a href="https://arxiv.org/pdf/2512.14082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14082v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14082v1', 'A Unified Sparse Attention via Multi-Granularity Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siran Liu, Zane Cao, Yongchao He

**分类**: cs.CL

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出UniSparse以解决长序列自注意力计算瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长序列处理` `稀疏注意力` `大型语言模型` `多粒度压缩` `复合标记` `计算效率` `程序分析`

## 📋 核心要点

1. 现有稀疏注意力方法在训练和推理时面临效率与准确率的权衡，难以满足长序列处理的需求。
2. 本文提出UniSparse，通过引入复合标记和多粒度压缩，动态构建稀疏注意力，提升计算效率。
3. 实验表明，UniSparse在多个基准和实际应用中，准确率超过99%，计算速度比现有方法快2.61倍。

## 📝 摘要（中文）

高效的长上下文理解与推理对于大型语言模型（LLM）应用如多轮对话和程序分析至关重要。然而，核心自注意力机制的计算复杂度随序列长度呈平方增长，形成了根本的计算瓶颈。现有的稀疏注意力方法虽然缓解了这一问题，但存在训练成本高或推理效率低等权衡。为了解决这些局限性，本文提出了UniSparse，这是一种统一机制，引入了复合标记的概念，聚合多粒度上下文信息。基于这一抽象，UniSparse通过多粒度压缩和块级选择动态构建稀疏注意力，实现了高效且适合GPU执行的方案。实验结果表明，UniSparse在多个模态和任务上均超越了现有的稀疏注意力方法，准确率达到全注意力的99%以上，计算速度比FlashAttention快2.61倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理长序列时自注意力计算的高复杂度问题。现有方法在训练和推理阶段存在效率低下和准确率不足的痛点。

**核心思路**：UniSparse的核心思路是引入复合标记，聚合多粒度的上下文信息，从而实现动态稀疏注意力的构建。这种设计旨在提高计算效率并降低资源消耗。

**技术框架**：UniSparse的整体架构包括复合标记生成、多粒度压缩和块级选择三个主要模块。复合标记用于表示上下文信息，多粒度压缩则用于减少计算量，块级选择确保了高效的注意力计算。

**关键创新**：UniSparse的最大创新在于其复合标记的引入和动态稀疏注意力的构建方式。这与现有方法的静态稀疏策略形成了本质区别，能够更灵活地适应不同的上下文需求。

**关键设计**：在设计中，UniSparse采用了特定的参数设置以优化计算效率，并利用适应性损失函数来平衡准确率与计算速度。此外，网络结构经过精心设计，以支持多模态数据的处理。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14082v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14082v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14082v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，UniSparse在多个基准测试中均超越了现有的稀疏注意力方法，如MInference、XAttention和FlexPrefill，准确率达到全注意力的99%以上，且计算速度比FlashAttention快2.61倍，展现出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括多轮对话系统、程序分析、长文本理解等。UniSparse的高效计算能力和准确性使其在实际应用中具有重要价值，能够显著提升大型语言模型在复杂任务中的表现，未来可能推动更多智能系统的发展。

## 📄 摘要（原文）

> Efficient long-context understanding and reasoning are increasingly vital for large language model (LLM) applications such as multi-turn dialogue and program analysis. However, the core self-attention mechanism scales quadratically with sequence length, creating a fundamental computational bottleneck. Existing sparse attention methods alleviate this issue but face trade-offs: training-based methods are costly and cannot be directly applied as acceleration plugins for other models, while inference-time methods often compromise efficiency or cross-modal generality. To address these limitations, we present UniSparse, a unified mechanism that introduces the notion of composite tokens--compact representations that aggregate multi-granularity contextual information. Building on this abstraction, UniSparse dynamically constructs sparse attention through multi-granularity compression and block-level selection, enabling efficient and hardware-friendly execution on GPU. Across multiple modalities and tasks ranging from synthetic benchmarks to real-world applications, UniSparse consistently surpasses state-of-the-art sparse attention methods (e.g., MInference, XAttention, FlexPrefill) in both accuracy and efficiency, achieving $\ge$ 99% of full-attention accuracy and up to 2.61$\times$ faster attention computation than FlashAttention.

