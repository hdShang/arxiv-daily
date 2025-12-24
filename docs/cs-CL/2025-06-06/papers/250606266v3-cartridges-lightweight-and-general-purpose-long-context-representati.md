---
layout: default
title: "Cartridges: Lightweight and general-purpose long context representations via self-study"
---

# Cartridges: Lightweight and general-purpose long context representations via self-study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06266" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06266v3</a>
  <a href="https://arxiv.org/pdf/2506.06266.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06266v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06266v3', 'Cartridges: Lightweight and general-purpose long context representations via self-study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sabri Eyuboglu, Ryan Ehrlich, Simran Arora, Neel Guha, Dylan Zinsley, Emily Liu, Will Tennien, Atri Rudra, James Zou, Azalia Mirhoseini, Christopher Re

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-06 (更新: 2025-06-13)

---

## 💡 一句话要点

**提出Cartridges以解决长文本上下文处理的高成本问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本处理` `自学习` `KV缓存` `上下文蒸馏` `大型语言模型` `推理效率` `内存优化`

## 📋 核心要点

1. 当前大型语言模型在处理长文本上下文时，内存消耗高，成本昂贵，限制了其应用。
2. 本文提出的Cartridge通过自学习方法训练KV缓存，显著降低了内存使用和推理成本。
3. 实验结果显示，Cartridges在长上下文基准测试中与ICL性能相当，但内存使用减少38.6倍，吞吐量提高26.4倍。

## 📝 摘要（中文）

大型语言模型通常通过将整个文本语料放入上下文窗口来回答基于大文本语料（如代码库、法律文件或聊天记录）的查询。然而，当前模型的上下文支持范围为10万到100万标记，这种设置在内存消耗上成本高昂。本文提出了一种替代方案：在每个语料上离线训练一个较小的KV缓存，称为Cartridge。在推理时加载该缓存并解码响应。我们发现，使用简单的下一个标记预测训练Cartridge的方式并不具竞争力，因此提出了自学习的方法，通过生成关于语料的合成对话并使用上下文蒸馏目标来训练Cartridge。实验表明，使用自学习训练的Cartridges在长上下文基准测试中表现出与ICL相当的性能，同时内存使用量减少38.6倍，吞吐量提高26.4倍。

## 🔬 方法详解

**问题定义**：当前大型语言模型在处理长文本上下文时，内存消耗随着输入长度增加而显著上升，导致服务成本高昂。现有方法如ICL虽然支持长上下文，但在实际应用中面临资源限制和高成本的问题。

**核心思路**：本文提出了一种名为Cartridge的KV缓存，通过离线训练并在推理时加载，旨在降低内存使用和提高推理效率。通过自学习方法生成合成对话并使用上下文蒸馏目标进行训练，使得Cartridge能够在不牺牲性能的情况下，显著降低资源消耗。

**技术框架**：整体架构包括两个主要阶段：第一阶段是离线训练Cartridge，生成合成对话并进行上下文蒸馏；第二阶段是在推理时加载训练好的Cartridge并解码响应。该框架有效地将训练成本分摊到多个查询中。

**关键创新**：最重要的创新在于自学习训练方法，通过生成合成对话而非简单的下一个标记预测，提升了Cartridge的性能，使其在长上下文任务中表现出与ICL相当的效果。

**关键设计**：在训练过程中，使用了上下文蒸馏的损失函数，确保Cartridge能够有效捕捉语料的上下文信息。此外，Cartridge的设计允许在推理时进行组合，而无需重新训练，进一步提高了灵活性和效率。

## 📊 实验亮点

实验结果显示，使用自学习训练的Cartridges在长上下文基准测试中与ICL的性能相当，同时内存使用量减少38.6倍，吞吐量提高26.4倍。这一显著的性能提升表明Cartridges在处理长文本时具有极高的效率和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括法律文书分析、代码自动补全、聊天记录处理等需要处理长文本上下文的场景。通过降低内存消耗和提高推理效率，Cartridges可以在资源受限的环境中实现更高效的文本处理，推动大型语言模型的实际应用和普及。

## 📄 摘要（原文）

> Large language models are often used to answer queries grounded in large text corpora (e.g. codebases, legal documents, or chat histories) by placing the entire corpus in the context window and leveraging in-context learning (ICL). Although current models support contexts of 100K-1M tokens, this setup is costly to serve because the memory consumption of the KV cache scales with input length. We explore an alternative: training a smaller KV cache offline on each corpus. At inference time, we load this trained KV cache, which we call a Cartridge, and decode a response. Critically, the cost of training a Cartridge can be amortized across all the queries referencing the same corpus. However, we find that the naive approach of training the Cartridge with next-token prediction on the corpus is not competitive with ICL. Instead, we propose self-study, a training recipe in which we generate synthetic conversations about the corpus and train the Cartridge with a context-distillation objective. We find that Cartridges trained with self-study replicate the functionality of ICL, while being significantly cheaper to serve. On challenging long-context benchmarks, Cartridges trained with self-study match ICL performance while using 38.6x less memory and enabling 26.4x higher throughput. Self-study also extends the model's effective context length (e.g. from 128k to 484k tokens on MTOB) and surprisingly, leads to Cartridges that can be composed at inference time without retraining.

