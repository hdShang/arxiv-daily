---
layout: default
title: "GOLFer: Smaller LM-Generated Documents Hallucination Filter & Combiner for Query Expansion in Information Retrieval"
---

# GOLFer: Smaller LM-Generated Documents Hallucination Filter & Combiner for Query Expansion in Information Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04762" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04762v1</a>
  <a href="https://arxiv.org/pdf/2506.04762.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04762v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04762v1', 'GOLFer: Smaller LM-Generated Documents Hallucination Filter & Combiner for Query Expansion in Information Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingyuan Liu, Mengxiang Zhang

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出GOLFer以解决小型语言模型生成文档的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `查询扩展` `小型语言模型` `信息检索` `幻觉过滤` `文档组合`

## 📋 核心要点

1. 现有基于大型语言模型的查询扩展方法依赖于模型规模，导致高成本和计算负担。
2. GOLFer通过小型开源语言模型，设计了幻觉过滤器和文档组合器来提升查询扩展效果。
3. 实验结果显示，GOLFer在多个数据集上超越其他小型模型方法，并与大型模型方法竞争。
4. method_zh

## 📝 摘要（中文）

基于大型语言模型（LLMs）的查询扩展方法通过生成假设文档来增强查询，但其性能高度依赖于模型规模，导致成本高、计算密集且可访问性有限。为了解决这些问题，本文提出了GOLFer——一种利用小型开源语言模型进行查询扩展的新方法。GOLFer包括两个模块：幻觉过滤器和文档组合器，前者检测并移除生成文档中的非事实和不一致句子，后者使用权重向量将过滤后的内容与查询结合。实验结果表明，GOLFer在使用小型语言模型时的表现优于其他方法，并在与大型语言模型的方法对比中保持竞争力，证明了其有效性。

## 🔬 方法详解

**问题定义**：当前基于大型语言模型的查询扩展方法在生成假设文档时，常常面临高成本和计算资源消耗的问题。此外，小型语言模型生成的文档可能包含非事实和不一致的信息，影响查询的有效性。

**核心思路**：GOLFer的核心思路是利用小型开源语言模型，通过设计幻觉过滤器来清理生成文档中的不准确内容，并通过文档组合器将有效信息与查询进行有效结合，从而提升查询扩展的质量和效率。

**技术框架**：GOLFer的整体架构包括两个主要模块：幻觉过滤器负责检测和移除不准确的句子，文档组合器则使用权重向量将过滤后的内容与原始查询进行融合。整个流程从生成文档开始，经过过滤和组合，最终输出增强的查询。

**关键创新**：GOLFer的主要创新在于其能够在使用小型语言模型的情况下，依然保持较高的查询扩展效果，且通过幻觉过滤器有效解决了小型模型生成内容的准确性问题。这与传统依赖大型模型的方式形成了鲜明对比。

**关键设计**：在设计上，GOLFer的幻觉过滤器采用了特定的句子评估机制，以识别和剔除不一致的信息。文档组合器则通过动态权重调整，确保生成内容与查询之间的平衡，从而提升最终结果的相关性和准确性。

## 📊 实验亮点

实验结果表明，GOLFer在三个网络搜索和十个低资源数据集上均表现优异，使用小型语言模型时的性能超越了其他主流方法，并在与大型语言模型的对比中保持竞争力，展示了其有效性和实用性。

## 🎯 应用场景

GOLFer的研究成果具有广泛的应用潜力，特别是在信息检索、搜索引擎优化和自然语言处理等领域。通过有效利用小型语言模型，GOLFer能够降低计算成本，提高查询扩展的效率，适用于资源受限的环境。未来，该方法还可以扩展到其他需要生成和过滤文本的应用场景，如智能问答系统和内容推荐。

## 📄 摘要（原文）

> Large language models (LLMs)-based query expansion for information retrieval augments queries with generated hypothetical documents with LLMs. However, its performance relies heavily on the scale of the language models (LMs), necessitating larger, more advanced LLMs. This approach is costly, computationally intensive, and often has limited accessibility. To address these limitations, we introduce GOLFer - Smaller LMs-Generated Documents Hallucination Filter & Combiner - a novel method leveraging smaller open-source LMs for query expansion. GOLFer comprises two modules: a hallucination filter and a documents combiner. The former detects and removes non-factual and inconsistent sentences in generated documents, a common issue with smaller LMs, while the latter combines the filtered content with the query using a weight vector to balance their influence. We evaluate GOLFer alongside dominant LLM-based query expansion methods on three web search and ten low-resource datasets. Experimental results demonstrate that GOLFer consistently outperforms other methods using smaller LMs, and maintains competitive performance against methods using large-size LLMs, demonstrating its effectiveness.

