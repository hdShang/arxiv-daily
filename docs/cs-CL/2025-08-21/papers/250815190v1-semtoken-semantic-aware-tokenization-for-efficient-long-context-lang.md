---
layout: default
title: "SemToken: Semantic-Aware Tokenization for Efficient Long-Context Language Modeling"
---

# SemToken: Semantic-Aware Tokenization for Efficient Long-Context Language Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15190" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15190v1</a>
  <a href="https://arxiv.org/pdf/2508.15190.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15190v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15190v1', 'SemToken: Semantic-Aware Tokenization for Efficient Long-Context Language Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dong Liu, Yanxuan Yu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-21

---

## 💡 一句话要点

**提出SemToken以解决长文本语言建模中的语义感知分词问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语义感知` `分词` `长文本建模` `语言模型` `计算效率` `上下文理解` `聚类算法`

## 📋 核心要点

1. 现有的分词方法主要依赖频率统计，未能有效利用文本的语义结构，导致冗余分词和上下文连贯性不足。
2. SemToken通过提取上下文语义嵌入和局部语义聚类，优化了分词过程，减少了冗余并提高了计算效率。
3. 在WikiText-103和LongBench等长文本语言建模基准上，SemToken实现了2.4倍的标记减少和1.9倍的速度提升。

## 📝 摘要（中文）

分词在语言建模中起着关键作用，但现有方法如字节对编码（BPE）或WordPiece仅基于频率统计，忽视了文本的语义结构。这导致语义冗余的片段被过度分词，而上下文连贯性未得到充分利用，尤其是在长文本场景中。本文提出了SemToken，一个语义感知的分词框架，旨在减少分词冗余并提高计算效率。SemToken首先通过轻量级编码器提取上下文语义嵌入，并进行局部语义聚类以合并语义等价的标记。然后，根据语义密度分配异构的标记粒度，在内容丰富的区域进行更细粒度的分词，而在重复或低熵的片段中进行粗粒度压缩。实验表明，SemToken在长文本语言建模基准上实现了高达2.4倍的标记数量减少和1.9倍的速度提升，同时在困惑度和下游准确性上几乎没有下降。

## 🔬 方法详解

**问题定义**：本文旨在解决现有分词方法在长文本语言建模中存在的语义冗余和上下文连贯性不足的问题。现有方法如BPE和WordPiece仅依赖于频率统计，未考虑文本的语义结构，导致过度分词和计算效率低下。

**核心思路**：SemToken的核心思路是通过语义感知的方式进行分词，首先提取上下文的语义嵌入，然后进行局部语义聚类，以合并语义相似的标记，从而减少冗余并提高计算效率。

**技术框架**：SemToken的整体架构包括两个主要模块：首先是轻量级编码器用于提取上下文语义嵌入，其次是局部语义聚类模块用于合并语义等价的标记。最后，根据语义密度动态调整标记的粒度。

**关键创新**：SemToken的创新在于引入了语义感知的分词策略，通过语义聚类和动态粒度分配，显著改善了分词的效率和效果。这与传统方法的频率统计方法形成了鲜明对比。

**关键设计**：在设计上，SemToken采用了轻量级的编码器以降低计算复杂度，并通过局部聚类算法实现语义标记的合并。此外，动态粒度分配策略使得在内容丰富区域使用细粒度分词，而在低熵区域则采用粗粒度压缩。

## 📊 实验亮点

SemToken在长文本语言建模基准上表现出色，标记数量减少高达2.4倍，计算速度提升1.9倍，同时在困惑度和下游任务准确性上几乎没有下降，显示出其在实际应用中的优越性。

## 🎯 应用场景

SemToken的研究成果在长文本处理、自然语言理解和生成等领域具有广泛的应用潜力。其语义感知的分词方法可以提高大型语言模型的效率，降低计算成本，进而推动智能对话系统、文本生成和信息检索等技术的发展。

## 📄 摘要（原文）

> Tokenization plays a critical role in language modeling, yet existing approaches such as Byte-Pair Encoding (BPE) or WordPiece operate purely on frequency statistics, ignoring the underlying semantic structure of text. This leads to over-tokenization of semantically redundant spans and underutilization of contextual coherence, particularly in long-context scenarios. In this work, we propose \textbf{SemToken}, a semantic-aware tokenization framework that jointly reduces token redundancy and improves computation efficiency. SemToken first extracts contextual semantic embeddings via lightweight encoders and performs local semantic clustering to merge semantically equivalent tokens. Then, it allocates heterogeneous token granularity based on semantic density, allowing finer-grained tokenization in content-rich regions and coarser compression in repetitive or low-entropy spans. SemToken can be seamlessly integrated with modern language models and attention acceleration methods. Experiments on long-context language modeling benchmarks such as WikiText-103 and LongBench show that SemToken achieves up to $2.4\times$ reduction in token count and $1.9\times$ speedup, with negligible or no degradation in perplexity and downstream accuracy. Our findings suggest that semantic structure offers a promising new axis for optimizing tokenization and computation in large language models.

