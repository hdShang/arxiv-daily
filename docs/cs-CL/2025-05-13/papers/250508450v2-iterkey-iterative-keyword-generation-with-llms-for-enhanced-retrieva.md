---
layout: default
title: IterKey: Iterative Keyword Generation with LLMs for Enhanced Retrieval Augmented Generation
---

# IterKey: Iterative Keyword Generation with LLMs for Enhanced Retrieval Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08450" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08450v2</a>
  <a href="https://arxiv.org/pdf/2505.08450.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08450v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08450v2', 'IterKey: Iterative Keyword Generation with LLMs for Enhanced Retrieval Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kazuki Hayashi, Hidetaka Kamigaito, Shinya Kouda, Taro Watanabe

**分类**: cs.CL

**发布日期**: 2025-05-13 (更新: 2025-07-30)

---

## 💡 一句话要点

**提出IterKey以解决RAG中的准确性与可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `关键词生成` `稀疏检索` `大型语言模型` `问答系统` `信息检索`

## 📋 核心要点

1. 现有的检索增强生成方法在准确性和可解释性之间存在权衡，密集检索方法缺乏透明性，而稀疏检索方法又无法充分理解查询意图。
2. 本文提出的IterKey框架通过迭代生成关键词来优化稀疏检索，增强了RAG的性能，确保了结果的可解释性。
3. 实验结果显示，IterKey在多个问答任务中相比BM25基线提高了5%至20%的准确性，表现与密集检索方法相当。

## 📝 摘要（中文）

检索增强生成（RAG）通过整合外部文档来补充大型语言模型（LLMs）的上下文知识。然而，实际应用不仅需要准确性，还需要可解释性。密集检索方法虽然提供高准确性，但缺乏可解释性；而稀疏检索方法则提供透明性，但由于依赖关键词匹配，常常无法捕捉查询的完整意图。为了解决这些问题，本文提出了IterKey，一个基于LLMs的迭代关键词生成框架，通过稀疏检索增强RAG。IterKey包括三个基于LLMs的阶段：生成检索关键词、基于检索文档生成答案以及验证答案。如果验证失败，过程将迭代重复，使用优化后的关键词。实验结果表明，IterKey在四个问答任务中相较于基于BM25的RAG和简单基线实现了5%到20%的准确性提升，其性能与基于密集检索的RAG和先前的迭代查询优化方法相当。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RAG方法在准确性与可解释性之间的矛盾，尤其是稀疏检索方法在捕捉查询意图方面的不足。

**核心思路**：IterKey通过引入一个迭代的关键词生成过程，利用LLMs不断优化检索关键词，从而提高检索的准确性和结果的可解释性。

**技术框架**：IterKey的整体架构分为三个主要阶段：首先生成用于检索的关键词；其次基于检索到的文档生成答案；最后验证生成的答案。如果验证失败，则返回第一步，使用优化后的关键词重新进行检索。

**关键创新**：IterKey的创新在于其迭代关键词生成机制，使得稀疏检索不仅能保持透明性，还能有效提升准确性，这与传统的静态关键词匹配方法有本质区别。

**关键设计**：在设计上，IterKey采用了基于BM25的检索策略，并结合LLMs进行关键词生成和答案验证，确保了系统的灵活性和适应性。

## 📊 实验亮点

在实验中，IterKey在四个问答任务上实现了5%到20%的准确性提升，相较于BM25基线表现出显著优势，其性能与密集检索方法相当，展示了其在检索增强生成领域的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和知识管理等。通过提高检索的准确性和可解释性，IterKey能够在实际应用中为用户提供更为可靠和透明的信息获取方式，未来可能推动更多基于LLMs的智能应用的发展。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) has emerged as a way to complement the in-context knowledge of Large Language Models (LLMs) by integrating external documents. However, real-world applications demand not only accuracy but also interpretability. While dense retrieval methods provide high accuracy, they lack interpretability; conversely, sparse retrieval methods offer transparency but often fail to capture the full intent of queries due to their reliance on keyword matching. To address these issues, we introduce IterKey, an LLM-driven iterative keyword generation framework that enhances RAG via sparse retrieval. IterKey consists of three LLM-driven stages: generating keywords for retrieval, generating answers based on retrieved documents, and validating the answers. If validation fails, the process iteratively repeats with refined keywords. Across four QA tasks, experimental results show that IterKey achieves 5% to 20% accuracy improvements over BM25-based RAG and simple baselines. Its performance is comparable to dense retrieval-based RAG and prior iterative query refinement methods using dense models. In summary, IterKey is a novel BM25-based approach leveraging LLMs to iteratively refine RAG, effectively balancing accuracy with interpretability.

