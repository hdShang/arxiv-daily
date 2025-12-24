---
layout: default
title: Learn from the Past: Fast Sparse Indexing for Large Language Model Decoding
---

# Learn from the Past: Fast Sparse Indexing for Large Language Model Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15704" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15704v1</a>
  <a href="https://arxiv.org/pdf/2506.15704.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15704v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15704v1', 'Learn from the Past: Fast Sparse Indexing for Large Language Model Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feiyu Yao, Qian Wang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出LFPS以解决长上下文解码中的稀疏索引问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `稀疏注意力` `解码优化` `历史信息利用` `长上下文`

## 📋 核心要点

1. 现有稀疏注意力机制在解码过程中需要遍历所有键向量，导致计算和数据传输开销过大。
2. LFPS方法通过动态构建稀疏索引候选，利用历史注意力模式中的时间相关性来优化索引检索。
3. 在长上下文基准测试中，LFPS在RTX 4090 GPU上实现了22.8倍的速度提升，同时保持生成准确性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）对更长上下文的支持，解码过程中对键值（KV）缓存的内存需求迅速增长，成为GPU内存容量和PCIe带宽的关键瓶颈。稀疏注意力机制通过仅计算选定键值对的注意力权重来缓解这一问题。然而，现有方法在索引计算时通常需要遍历所有键向量，导致显著的计算和数据传输开销。为降低索引检索成本，现有方法往往将每个解码步骤视为独立过程，未能利用历史解码信息中的时间相关性。为此，本文提出LFPS（Learn From the Past for Sparse Indexing），一种加速方法，基于历史注意力模式动态构建稀疏索引候选。LFPS捕捉解码器注意力中的两种普遍趋势，并结合位置扩展策略有效预测当前步骤的Top-k索引。实验结果表明，LFPS在长上下文基准测试中实现了显著的加速效果，同时保持生成准确性。

## 🔬 方法详解

**问题定义**：本文解决的是在长上下文解码中，稀疏注意力机制由于遍历所有键向量而导致的计算和数据传输开销过大的问题。现有方法未能有效利用历史解码信息中的时间相关性。

**核心思路**：LFPS方法的核心思路是基于历史注意力模式动态构建稀疏索引候选，捕捉解码器注意力中的垂直模式和斜线模式，并通过位置扩展策略预测当前步骤的Top-k索引。

**技术框架**：LFPS的整体架构包括历史注意力模式的提取、稀疏索引候选的构建和Top-k索引的预测三个主要模块。首先，从历史解码中提取注意力模式，然后根据这些模式动态生成索引候选，最后进行Top-k索引的选择。

**关键创新**：LFPS的主要创新在于利用历史解码信息中的时间相关性，动态构建稀疏索引候选，从而显著降低索引检索的计算开销。这与现有方法将每个解码步骤视为独立过程的做法本质上不同。

**关键设计**：LFPS在设计上结合了位置扩展策略，以有效预测Top-k索引，并在实验中使用了Llama-3.1-8B-Instruct作为基础模型，确保了生成的准确性与速度的平衡。实验中还使用了RTX 4090 GPU和Xeon Gold 6430 CPU进行性能评估。

## 📊 实验亮点

实验结果表明，LFPS在长上下文基准测试中实现了高达22.8倍的速度提升，相较于完整注意力机制和精确Top-k检索分别提升了9.6倍。这些结果展示了LFPS在解码优化中的实用性和高效性。

## 🎯 应用场景

LFPS方法在长上下文的语言模型解码中具有广泛的应用潜力，特别是在需要高效处理大规模文本生成任务的场景中，如对话系统、文本摘要和机器翻译等。其高效的索引检索机制能够显著提升解码速度，降低计算资源消耗，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> As large language models (LLMs) continue to support increasingly longer contexts, the memory demand for key-value (KV) caches during decoding grows rapidly, becoming a critical bottleneck in both GPU memory capacity and PCIe bandwidth. Sparse attention mechanisms alleviate this issue by computing attention weights only for selected key-value pairs. However, their indexing computation typically requires traversing all key vectors, resulting in significant computational and data transfer overhead. To reduce the cost of index retrieval, existing methods often treat each decoding step as an independent process, failing to exploit the temporal correlations embedded in historical decoding information. To this end, we propose LFPS(Learn From the Past for Sparse Indexing), an acceleration method that dynamically constructs sparse indexing candidates based on historical attention patterns. LFPS captures two prevalent trends in decoder attention -vertical patterns (attending to fixed positions) and slash patterns (attending to relative positions) -and incorporates a positional expansion strategy to effectively predict the Top-k indices for the current step. We validate LFPS on challenging long-context benchmarks such as LongBench-RULER, using Llama-3.1-8B-Instruct as the base model. Experimental results show that LFPS achieves up to 22.8$\times$ speedup over full attention and 9.6$\times$ speedup over exact Top-k retrieval on an RTX 4090 GPU and a single CPU core of a Xeon Gold 6430, respectively, while preserving generation accuracy. These results demonstrate that LFPS offers a practical and efficient solution for decoding optimization in long-context LLM inference.

