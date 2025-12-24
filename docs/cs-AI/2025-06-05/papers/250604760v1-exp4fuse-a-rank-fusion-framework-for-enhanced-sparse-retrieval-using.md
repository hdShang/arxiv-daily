---
layout: default
title: "Exp4Fuse: A Rank Fusion Framework for Enhanced Sparse Retrieval using Large Language Model-based Query Expansion"
---

# Exp4Fuse: A Rank Fusion Framework for Enhanced Sparse Retrieval using Large Language Model-based Query Expansion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04760" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04760v1</a>
  <a href="https://arxiv.org/pdf/2506.04760.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04760v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04760v1', 'Exp4Fuse: A Rank Fusion Framework for Enhanced Sparse Retrieval using Large Language Model-based Query Expansion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingyuan Liu, Mengxiang Zhang

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出Exp4Fuse框架以提升稀疏检索性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `查询扩展` `稀疏检索` `信息检索` `排名融合` `零-shot学习` `机器学习`

## 📋 核心要点

1. 现有的LLM查询扩展方法依赖于生成文档的质量，且通常需要复杂的提示策略，导致计算成本高。
2. 本文提出的Exp4Fuse框架通过零-shot LLM查询扩展，结合两条检索路径，提升稀疏检索器的性能。
3. 实验结果显示，Exp4Fuse在多个数据集上超越了现有方法，并在结合先进稀疏检索器时取得了最先进的结果。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成假设文档以扩展查询方面展现出潜力，从而提升信息检索性能。然而，这种方法的有效性高度依赖于生成文档的质量，通常需要复杂的提示策略和先进的稠密检索技术的整合，导致成本和计算负担加重。为此，本文探索了基于零-shot LLM的查询扩展，以改善稀疏检索，特别是针对学习型稀疏检索器。我们提出了一种新颖的融合排名框架Exp4Fuse，通过间接应用零-shot LLM的查询扩展来增强稀疏检索器的性能。Exp4Fuse同时考虑基于原始查询和LLM增强查询的两条检索路径，生成两个排名列表并使用改进的倒数排名融合方法进行融合。实验结果表明，Exp4Fuse在提升稀疏检索器性能方面超越了现有的LLM查询扩展方法，并在多个基准上与先进的稀疏检索器结合时达到了SOTA结果。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM查询扩展方法在生成文档质量和计算成本上的不足，特别是在稀疏检索场景中的应用痛点。

**核心思路**：提出Exp4Fuse框架，通过零-shot LLM查询扩展，结合原始查询和LLM增强查询的检索路径，提升稀疏检索器的效果。

**技术框架**：Exp4Fuse的整体架构包括两个主要模块：一是基于原始查询的稀疏检索，二是基于LLM增强查询的稀疏检索，最终通过改进的倒数排名融合方法将两个排名列表进行融合。

**关键创新**：Exp4Fuse的创新在于其通过零-shot LLM查询扩展的间接应用，显著提升了稀疏检索器的性能，与现有方法相比，减少了对生成文档质量的依赖。

**关键设计**：在设计中，Exp4Fuse采用了改进的倒数排名融合方法，确保了两个检索路径的有效结合，同时在参数设置上进行了优化，以适应不同数据集的特性。

## 📊 实验亮点

实验结果表明，Exp4Fuse在多个MS MARCO相关数据集和七个低资源数据集上超越了现有的LLM查询扩展方法，结合先进稀疏检索器时达到了最先进的结果，显示出显著的性能提升，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索系统、搜索引擎优化和智能问答系统等。通过提升稀疏检索器的性能，Exp4Fuse能够为用户提供更准确的检索结果，进而提高信息获取的效率和准确性。未来，该方法可能在处理低资源数据集和特定领域检索任务中展现出更大的价值。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown potential in generating hypothetical documents for query expansion, thereby enhancing information retrieval performance. However, the efficacy of this method is highly dependent on the quality of the generated documents, which often requires complex prompt strategies and the integration of advanced dense retrieval techniques. This can be both costly and computationally intensive. To mitigate these limitations, we explore the use of zero-shot LLM-based query expansion to improve sparse retrieval, particularly for learned sparse retrievers. We introduce a novel fusion ranking framework, Exp4Fuse, which enhances the performance of sparse retrievers through an indirect application of zero-shot LLM-based query expansion. Exp4Fuse operates by simultaneously considering two retrieval routes-one based on the original query and the other on the LLM-augmented query. It then generates two ranked lists using a sparse retriever and fuses them using a modified reciprocal rank fusion method. We conduct extensive evaluations of Exp4Fuse against leading LLM-based query expansion methods and advanced retrieval techniques on three MS MARCO-related datasets and seven low-resource datasets. Experimental results reveal that Exp4Fuse not only surpasses existing LLM-based query expansion methods in enhancing sparse retrievers but also, when combined with advanced sparse retrievers, achieves SOTA results on several benchmarks. This highlights the superior performance and effectiveness of Exp4Fuse in improving query expansion for sparse retrieval.

