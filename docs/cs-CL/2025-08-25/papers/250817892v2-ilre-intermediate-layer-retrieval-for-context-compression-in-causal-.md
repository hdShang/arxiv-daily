---
layout: default
title: "ILRe: Intermediate Layer Retrieval for Context Compression in Causal Language Models"
---

# ILRe: Intermediate Layer Retrieval for Context Compression in Causal Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17892" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17892v2</a>
  <a href="https://arxiv.org/pdf/2508.17892.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17892v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17892v2', 'ILRe: Intermediate Layer Retrieval for Context Compression in Causal Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manlai Liang, Mandi Liu, Jiangzhou Ji, Huaijun Li, Haobo Yang, Yaohan He, Jinlong Li

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-25 (更新: 2025-09-25)

---

## 💡 一句话要点

**提出ILRe以解决长上下文处理中的效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文处理` `中间层检索` `上下文压缩` `大型语言模型` `计算效率` `内存优化`

## 📋 核心要点

1. 现有大型语言模型在处理长上下文时面临短有效上下文长度和高计算复杂度等挑战，导致性能受限。
2. 本文提出中间层检索（ILRe）方法，通过离线选择中间解码层并优化上下文编码过程，有效降低计算和内存开销。
3. 实验结果表明，ILRe在处理单个1M令牌请求时速度提升约180倍，并在RULER-1M基准测试中取得约79.8的得分。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个基准测试中取得了成功，但在长上下文场景中仍然存在短有效上下文长度、计算复杂度高和内存开销大的问题。为了解决这些问题，本文提出了一种新的上下文压缩管道——中间层检索（ILRe），该方法通过离线确定一个中间解码器层，仅对该层进行上下文编码，并通过输入查询与完整键缓存之间的注意力得分来回忆令牌。我们还提出了一种多池核分配策略，以保持语义的完整性。该方法将预填充复杂度从O(L²)降低到O(L)，并将内存占用减少到全上下文所需的几十分之一，同时在长上下文场景中表现出与全上下文设置相当或更优的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长上下文处理中的效率问题，现有方法在处理长输入时面临短有效上下文长度、计算复杂度为O(L²)和高内存开销等痛点。

**核心思路**：ILRe通过离线选择一个中间解码器层，仅对该层进行上下文编码，并利用注意力得分进行令牌回忆，从而有效降低计算复杂度和内存占用。

**技术框架**：ILRe的整体架构包括离线中间层选择、流式分块预填充和基于注意力得分的令牌回忆三个主要模块，形成一个高效的上下文压缩管道。

**关键创新**：ILRe的核心创新在于引入了多池核分配策略，以保持语义的完整性，同时将预填充复杂度从O(L²)降低到O(L)，显著提升了处理效率。

**关键设计**：在令牌回忆过程中，采用了多池核分配策略，确保在减少内存占用的同时，尽可能保留语义信息，此外，ILRe无需额外的后期训练或操作开发，直接提高了处理速度。

## 📊 实验亮点

ILRe在处理单个1M令牌请求时，速度提升约180倍，处理时间不足半分钟。此外，在RULER-1M基准测试中，ILRe取得了约79.8的得分，表现优于传统的全上下文设置，展示了其在长上下文处理中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等，尤其适用于需要处理长文本的场景，如法律文书分析、长篇文章摘要等。ILRe的高效性和低内存占用将推动大型语言模型在实际应用中的广泛部署，提升用户体验。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated success across many benchmarks. However, they still exhibit limitations in long-context scenarios, primarily due to their short effective context length, quadratic computational complexity, and high memory overhead when processing lengthy inputs. To mitigate these issues, we introduce a novel context compression pipeline, called Intermediate Layer Retrieval (ILRe), which determines one intermediate decoder layer offline, encodes context by streaming chunked prefill only up to that layer, and recalls tokens by the attention scores between the input query and full key cache in that specified layer. In particular, we propose a multi-pooling kernels allocating strategy in the token recalling process to maintain the completeness of semantics. Our approach not only reduces the prefilling complexity from $O(L^2)$ to $O(L)$ and trims the memory footprint to a few tenths of that required for the full context, but also delivers performance comparable to or superior to the full-context setup in long-context scenarios. Without additional post training or operator development, ILRe can process a single $1M$ tokens request in less than half a minute (speedup $\approx 180\times$) and scores RULER-$1M$ benchmark of $\approx 79.8$ with model Llama-3.1-UltraLong-8B-1M-Instruct on a Huawei Ascend 910B NPU.

