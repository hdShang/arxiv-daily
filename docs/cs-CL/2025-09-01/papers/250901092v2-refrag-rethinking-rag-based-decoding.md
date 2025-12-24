---
layout: default
title: "REFRAG: Rethinking RAG based Decoding"
---

# REFRAG: Rethinking RAG based Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01092" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01092v2</a>
  <a href="https://arxiv.org/pdf/2509.01092.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01092v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01092v2', 'REFRAG: Rethinking RAG based Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoqiang Lin, Aritra Ghosh, Bryan Kian Hsiang Low, Anshumali Shrivastava, Vijai Mohan

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-01 (更新: 2025-10-12)

**备注**: fix typo perplexity->log perplexity; added recent papers

---

## 💡 一句话要点

**提出REFRAG以解决RAG解码效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文处理` `检索增强生成` `解码效率` `大型语言模型` `系统优化` `多轮对话` `长文档摘要`

## 📋 核心要点

1. 现有的RAG方法在处理长上下文输入时面临显著的系统延迟和内存消耗问题，影响了整体效率。
2. REFRAG通过识别并消除大部分不必要的计算，优化了RAG解码过程，从而提升了系统的响应速度。
3. 实验结果显示，REFRAG在多种任务上实现了30.85的首次令牌加速，且在准确性上没有损失，优于现有模型。

## 📝 摘要（中文）

大型语言模型（LLMs）在多轮对话和智能应用中展现了卓越的能力，尤其是在检索增强生成（RAG）中。然而，处理长上下文输入会导致系统延迟和内存需求增加，从而影响效率。本文提出REFRAG，一个高效的解码框架，通过压缩、感知和扩展来提升RAG应用的延迟性能。实验表明，REFRAG在不损失困惑度的情况下，实现了30.85的首次令牌加速，且能够将上下文大小扩展16倍。我们在多种长上下文任务上对REFRAG进行了严格验证，结果显示其在速度和准确性上均优于LLaMA模型及其他先进基线。

## 🔬 方法详解

**问题定义**：本文旨在解决RAG解码过程中由于长上下文输入导致的系统延迟和内存消耗问题。现有方法在处理长上下文时，往往需要大量的计算资源，影响了系统的整体效率。

**核心思路**：REFRAG的核心思想是通过压缩、感知和扩展的方式，识别并消除大部分不必要的计算，从而提升RAG应用的解码效率。该方法特别关注于RAG上下文中大部分信息的冗余性，认为可以在不影响性能的情况下减少计算量。

**技术框架**：REFRAG的整体架构包括三个主要模块：压缩模块用于减少输入数据的冗余，感知模块用于识别重要信息，扩展模块则用于在必要时恢复上下文信息。该框架通过高效的计算流程，优化了RAG的解码过程。

**关键创新**：REFRAG的主要创新在于其能够有效利用上下文的稀疏性结构，显著减少了计算需求，同时保持了模型的性能。这一设计与传统的RAG方法相比，具有本质上的区别，能够在不牺牲准确性的前提下提升效率。

**关键设计**：在REFRAG中，关键的参数设置包括上下文压缩比例和感知阈值，损失函数则设计为平衡计算效率与模型性能。此外，网络结构采用了针对长上下文优化的设计，以支持更大规模的上下文输入。

## 📊 实验亮点

REFRAG在多种长上下文任务中表现出色，实验结果显示其实现了30.85的首次令牌加速，相较于之前的工作提高了3.75倍，同时在准确性上没有任何损失。这一显著的性能提升使得REFRAG在处理长上下文输入时成为一种有效的解决方案。

## 🎯 应用场景

REFRAG的研究成果在多个领域具有潜在应用价值，包括智能对话系统、长文档摘要生成和多轮交互应用等。通过提升RAG的解码效率，REFRAG能够为用户提供更快速的响应，改善用户体验，并推动智能系统在实际应用中的广泛采用。未来，REFRAG的技术框架也可能被扩展到其他需要处理长上下文的任务中，进一步提升其应用范围。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities in leveraging extensive external knowledge to enhance responses in multi-turn and agentic applications, such as retrieval-augmented generation (RAG). However, processing long-context inputs introduces significant system latency and demands substantial memory for the key-value cache, resulting in reduced throughput and a fundamental trade-off between knowledge enrichment and system efficiency. While minimizing latency for long-context inputs is a primary objective for LLMs, we contend that RAG require specialized consideration. In RAG, much of the LLM context consists of concatenated passages from retrieval, with only a small subset directly relevant to the query. These passages often exhibit low semantic similarity due to diversity or deduplication during re-ranking, leading to block-diagonal attention patterns that differ from those in standard LLM generation tasks. Based on this observation, we argue that most computations over the RAG context during decoding are unnecessary and can be eliminated with minimal impact on performance. To this end, we propose REFRAG, an efficient decoding framework that compresses, senses, and expands to improve latency in RAG applications. By exploiting the sparsity structure, we demonstrate a 30.85 the time-to-first-token acceleration (3.75 improvement to previous work) without loss in perplexity. In addition, our optimization framework for large context enables REFRAG to extend the context size of LLMs by 16. We provide rigorous validation of REFRAG across diverse long-context tasks, including RAG, multi-turn conversations, and long document summarization, spanning a wide range of datasets. Experimental results confirm that REFRAG delivers substantial speedup with no loss in accuracy compared to LLaMA models and other state-of-the-art baselines across various context sizes.

