---
layout: default
title: Hierarchical Level-Wise News Article Clustering via Multilingual Matryoshka Embeddings
---

# Hierarchical Level-Wise News Article Clustering via Multilingual Matryoshka Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00277" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00277v1</a>
  <a href="https://arxiv.org/pdf/2506.00277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00277v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00277v1', 'Hierarchical Level-Wise News Article Clustering via Multilingual Matryoshka Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hans W. A. Hanley, Zakir Durumeric

**分类**: cs.CL, cs.AI, cs.SI

**发布日期**: 2025-05-30

**备注**: Accepted to The 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025)

---

## 💡 一句话要点

**提出多语言Matryoshka嵌入以解决新闻文章聚类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言处理` `新闻聚类` `Matryoshka嵌入` `层次聚类` `主题建模` `社交媒体分析`

## 📋 核心要点

1. 现有的聚类方法在多语言环境中表现不佳，且扩展性和相似性度量不够透明。
2. 本文提出了一种基于多语言Matryoshka嵌入的层次化聚类方法，能够在不同粒度上评估故事相似性。
3. 该方法在SemEval 2022 Task 8测试数据集上取得了Pearson相关系数0.816的优异表现，显示出显著的效果提升。

## 📝 摘要（中文）

上下文大型语言模型嵌入在主题建模和聚类中越来越多地被使用。然而，现有方法通常扩展性差，依赖不透明的相似性度量，并且在多语言环境中表现不佳。本文提出了一种新颖、可扩展、可解释的层次化多语言新闻文章和社交媒体数据聚类方法。我们首先训练了多语言Matryoshka嵌入，能够根据嵌入维度的不同子集来确定故事相似性。该嵌入模型在SemEval 2022 Task 8测试数据集上达到了最先进的性能（Pearson $ρ$ = 0.816）。训练完成后，我们开发了一种高效的层次聚类算法，利用Matryoshka嵌入的层次特性来识别独特的新闻故事、叙事和主题。最后，我们展示了该方法如何在真实世界新闻数据集中识别和聚类故事、叙事和总体主题。

## 🔬 方法详解

**问题定义**：本文旨在解决现有新闻文章聚类方法在多语言环境中的扩展性差和相似性度量不透明的问题。现有方法在处理多样化和复杂的新闻数据时，往往无法有效识别和聚类相似的故事和主题。

**核心思路**：论文提出了一种基于多语言Matryoshka嵌入的层次化聚类方法，通过不同维度的嵌入来评估故事的相似性，从而实现更灵活和可解释的聚类。这样的设计使得模型能够在不同的粒度上进行聚类，适应多样化的新闻内容。

**技术框架**：整体架构包括两个主要模块：首先是训练多语言Matryoshka嵌入模型，该模型能够捕捉不同语言和文化背景下的故事相似性；其次是基于这些嵌入的高效层次聚类算法，利用嵌入的层次特性来识别独特的新闻故事和主题。

**关键创新**：最重要的技术创新在于引入了多语言Matryoshka嵌入，这种嵌入方法能够根据不同的维度子集来评估故事相似性，显著提升了聚类的灵活性和可解释性。与现有方法相比，该方法在处理多语言数据时表现出更好的适应性和准确性。

**关键设计**：在模型训练中，采用了特定的损失函数来优化嵌入的相似性度量，同时在聚类算法中引入了层次结构，以便更好地识别和聚类新闻故事。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

在SemEval 2022 Task 8测试数据集上，提出的方法达到了Pearson相关系数0.816，显著优于现有基线，展示了在多语言新闻聚类任务中的卓越性能和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括新闻聚合、社交媒体分析和信息检索等。通过有效地聚类多语言新闻数据，能够帮助用户更好地理解和获取信息，提升信息传播的效率和准确性。未来，该方法还可以扩展到其他领域，如多语言内容推荐和舆情监测等。

## 📄 摘要（原文）

> Contextual large language model embeddings are increasingly utilized for topic modeling and clustering. However, current methods often scale poorly, rely on opaque similarity metrics, and struggle in multilingual settings. In this work, we present a novel, scalable, interpretable, hierarchical, and multilingual approach to clustering news articles and social media data. To do this, we first train multilingual Matryoshka embeddings that can determine story similarity at varying levels of granularity based on which subset of the dimensions of the embeddings is examined. This embedding model achieves state-of-the-art performance on the SemEval 2022 Task 8 test dataset (Pearson $ρ$ = 0.816). Once trained, we develop an efficient hierarchical clustering algorithm that leverages the hierarchical nature of Matryoshka embeddings to identify unique news stories, narratives, and themes. We conclude by illustrating how our approach can identify and cluster stories, narratives, and overarching themes within real-world news datasets.

