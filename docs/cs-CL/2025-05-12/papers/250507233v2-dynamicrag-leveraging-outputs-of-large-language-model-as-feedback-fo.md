---
layout: default
title: "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation"
---

# DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07233" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07233v2</a>
  <a href="https://arxiv.org/pdf/2505.07233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07233v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07233v2', 'DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiashuo Sun, Xianrui Zhong, Sizhe Zhou, Jiawei Han

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-12 (更新: 2025-05-16)

**备注**: 24 pages, 7 figures, 15 tables

**🔗 代码/项目**: [GITHUB](https://github.com/GasolSun36/DynamicRAG)

---

## 💡 一句话要点

**提出DynamicRAG以解决RAG系统中文档重排序问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `大型语言模型` `动态重排序` `强化学习` `知识密集型任务` `生成质量优化`

## 📋 核心要点

1. 现有RAG系统中的重排序器未能充分利用LLM的输出质量作为反馈，导致生成质量不高。
2. DynamicRAG框架通过强化学习优化重排序器，使其动态调整检索文档的顺序和数量，提升生成效果。
3. 在七个知识密集型数据集上，DynamicRAG表现优于同参数模型，达到了最先进的性能水平。

## 📝 摘要（中文）

检索增强生成（RAG）系统将大型语言模型（LLM）与外部知识检索结合，适用于知识密集型任务。然而，现有的重排序器往往未能充分利用LLM提供的丰富监督信号。本文提出DynamicRAG框架，重排序器根据查询动态调整检索文档的顺序和数量，利用强化学习优化决策。实验结果表明，DynamicRAG在七个知识密集型数据集上表现优异，达到了同参数模型中的最先进水平。

## 🔬 方法详解

**问题定义**：本文旨在解决RAG系统中重排序器的不足，特别是如何选择合适数量的文档（$k$）以避免信息缺失或噪声干扰。现有方法主要依赖内部模型知识，未能利用LLM的输出质量作为反馈。

**核心思路**：DynamicRAG通过将重排序器建模为一个强化学习代理，利用LLM输出的质量作为奖励信号，动态调整检索文档的顺序和数量，从而优化生成效果。

**技术框架**：DynamicRAG框架包括三个主要模块：文档检索模块、重排序模块和生成模块。文档检索模块负责从外部知识库中获取相关文档，重排序模块根据LLM的反馈动态调整文档顺序，生成模块则基于优化后的文档生成最终输出。

**关键创新**：DynamicRAG的创新在于将重排序器视为一个强化学习代理，利用LLM输出质量作为反馈信号，显著提升了重排序的有效性和生成质量。这一方法与传统依赖内部知识的重排序器形成鲜明对比。

**关键设计**：在设计中，重排序器的奖励函数基于LLM生成的响应质量，采用了强化学习中的策略优化方法。此外，模型的参数设置经过多次实验调优，以确保在不同数据集上的最佳性能。

## 📊 实验亮点

在七个知识密集型数据集上的实验结果显示，DynamicRAG在同参数模型中达到了最先进的性能，具体提升幅度超过了现有方法，证明了其在文档重排序和生成质量上的显著优势。

## 🎯 应用场景

DynamicRAG的研究成果可广泛应用于信息检索、问答系统和对话生成等领域，尤其是在需要结合外部知识的知识密集型任务中。其动态调整文档重排序的能力将提升生成系统的准确性和用户体验，具有重要的实际价值和潜在影响。

## 📄 摘要（原文）

> Retrieval-augmented generation (RAG) systems combine large language models (LLMs) with external knowledge retrieval, making them highly effective for knowledge-intensive tasks. A crucial but often under-explored component of these systems is the reranker. Since irrelevant documents in RAG systems can mislead the generator, the reranker plays a vital role in refining retrieved documents to enhance generation quality and explainability. However, it is challenging to determine the appropriate number of documents ($k$) that the reranker should select: too few may result in missing critical information, while too many introduce noise and inefficiencies. Although recent studies have explored LLM-based rerankers, they primarily leverage internal model knowledge and overlook the rich supervisory signals that LLMs can provide, such as using response quality as feedback for optimizing reranking decisions. In this paper, we propose DynamicRAG, a novel RAG framework where the reranker dynamically adjusts both the order and number of retrieved documents based on the query. We model the reranker as an agent optimized through reinforcement learning (RL), using rewards derived from LLM output quality. Across seven knowledge-intensive datasets, DynamicRAG demonstrates superior performance, achieving state-of-the-art results among models of same parameter sizes. The model, data and code are available at https://github.com/GasolSun36/DynamicRAG.

