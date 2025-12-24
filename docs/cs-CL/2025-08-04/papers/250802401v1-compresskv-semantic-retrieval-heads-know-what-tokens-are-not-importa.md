---
layout: default
title: "CompressKV: Semantic Retrieval Heads Know What Tokens are Not Important Before Generation"
---

# CompressKV: Semantic Retrieval Heads Know What Tokens are Not Important Before Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02401" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02401v1</a>
  <a href="https://arxiv.org/pdf/2508.02401.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02401v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02401v1', 'CompressKV: Semantic Retrieval Heads Know What Tokens are Not Important Before Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaolin Lin, Jingcun Wang, Olga Kondrateva, Yiyu Shi, Bing Li, Grace Li Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-04

**🔗 代码/项目**: [GITHUB](https://github.com/TUDa-HWAI/CompressKV.git)

---

## 💡 一句话要点

**提出CompressKV以解决长上下文处理中的KV缓存效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文处理` `键值缓存` `注意力机制` `内存优化` `自然语言处理` `模型性能提升` `层自适应策略`

## 📋 核心要点

1. 现有的KV缓存压缩方法未能有效区分注意力头的功能，导致重要标记被错误驱逐，影响LLMs性能。
2. 本文提出通过识别每层中能够检索重要标记的注意力头，优化KV缓存的保留策略，从而提高效率。
3. 实验结果显示，CompressKV在LongBench和Needle-in-a-Haystack基准测试中，始终优于现有方法，提升了内存利用率。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步显著提升了长上下文处理能力。然而，随着键值（KV）缓存大小的增加，内存和执行效率面临重大挑战。现有的KV缓存压缩方法依赖于使用Grouped Query Attention（GQA）中的所有注意力头进行启发式的标记驱逐，这种方法忽视了注意力头的不同功能，导致关键标记被驱逐，从而降低了LLMs的性能。为了解决这一问题，本文提出了一种新方法CompressKV，通过识别每层中能够检索重要标记的注意力头，来优化KV缓存的保留策略。实验结果表明，CompressKV在不同内存预算下的表现优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文解决的是在长上下文处理中的KV缓存效率问题。现有方法依赖于所有注意力头进行标记驱逐，导致重要标记的丢失，影响模型性能。

**核心思路**：本文的核心思路是识别每层中能够有效检索重要标记的注意力头，而非简单依赖所有头。这种方法能够更精准地保留关键标记，提高模型的上下文理解能力。

**技术框架**：整体架构包括三个主要模块：首先，识别每层中重要的注意力头；其次，基于这些头确定需要保留的KV缓存对；最后，实施层自适应的KV缓存分配策略，以优化内存使用。

**关键创新**：最重要的创新点在于通过分析每层的缓存驱逐错误，提出了层自适应的KV缓存分配策略。这与现有方法的全局驱逐策略形成鲜明对比，能够更有效地保留重要信息。

**关键设计**：在设计中，本文对每层的注意力头进行了详细分析，确定了其在检索初始和最终标记及其语义上下文中的能力。此外，采用了新的KV缓存分配策略，以适应不同层的需求。

## 📊 实验亮点

实验结果表明，CompressKV在LongBench和Needle-in-a-Haystack基准测试中，均在不同内存预算下超越了现有最先进的方法，提升幅度达到了XX%（具体数据需根据实验结果填写），显示了其在KV缓存优化方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等。通过提高长上下文处理的效率，CompressKV能够在实际应用中显著提升模型的响应速度和准确性，具有广泛的商业价值和研究意义。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have significantly boosted long-context processing. However, the increasing key-value (KV) cache size poses critical challenges to memory and execution efficiency. Most KV cache compression methods rely on heuristic token eviction using all attention heads in Grouped Query Attention (GQA)-based LLMs. This method ignores the different functionalities of attention heads, leading to the eviction of critical tokens and thus degrades the performance of LLMs.
>   To address the issue above, instead of using all the attention heads in GQA-based LLMs to determine important tokens as in the previous work, we first identify the attention heads in each layer that are not only capable of retrieving the initial and final tokens of a prompt, but also capable of retrieving important tokens within the text and attending to their surrounding semantic context. Afterwards, we exploit such heads to determine the important tokens and retain their corresponding KV cache pairs. Furthermore, we analyze the cache eviction error of each layer individually and introduce a layer-adaptive KV cache allocation strategy. Experimental results demonstrate the proposed CompressKV consistently outperforms state-of-the-art approaches under various memory budgets on LongBench and Needle-in-a-Haystack benchmarks. Our code is publicly available at: https://github.com/TUDa-HWAI/CompressKV.git.

