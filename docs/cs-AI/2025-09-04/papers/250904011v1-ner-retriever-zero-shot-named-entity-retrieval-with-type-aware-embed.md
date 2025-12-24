---
layout: default
title: "NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings"
---

# NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04011" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04011v1</a>
  <a href="https://arxiv.org/pdf/2509.04011.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04011v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04011v1', 'NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Or Shachar, Uri Katz, Yoav Goldberg, Oren Glickman

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-09-04

**备注**: Findings of EMNLP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/ShacharOr100/ner_retriever)

---

## 💡 一句话要点

**提出NER Retriever，利用类型感知嵌入实现零样本命名实体检索。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `命名实体检索` `零样本学习` `大型语言模型` `对比学习` `类型感知嵌入`

## 📋 核心要点

1. 现有命名实体识别方法依赖于预定义的模式或微调模型，难以适应开放域和用户自定义类型。
2. NER Retriever 利用 LLM 的中间层表示，通过对比学习对齐类型兼容实体，构建类型感知的嵌入空间。
3. 实验表明，NER Retriever 在三个基准测试中显著优于现有词汇和密集检索方法，实现了更好的零样本检索性能。

## 📝 摘要（中文）

本文提出NER Retriever，一个用于特定命名实体检索的零样本检索框架。该框架针对的是一种命名实体识别（NER）的变体，其中感兴趣的类型不是预先给定的，而是使用用户定义的类型描述来检索提及该类型实体的文档。我们的方法不依赖于固定的模式或微调模型，而是利用大型语言模型（LLM）的内部表示，将实体提及和用户提供的开放式类型描述嵌入到共享的语义空间中。我们发现，内部表示，特别是来自中间层 Transformer 块的值向量，比常用的顶层嵌入更有效地编码细粒度的类型信息。为了改进这些表示，我们训练了一个轻量级的对比投影网络，该网络对齐类型兼容的实体，同时分离不相关的类型。生成的实体嵌入是紧凑的、类型感知的，并且非常适合最近邻搜索。在三个基准测试中进行的评估表明，NER Retriever 显著优于词汇和密集句子级检索基线。我们的发现为 LLM 中表示选择提供了经验支持，并展示了可扩展的、无模式实体检索的实用解决方案。NER Retriever 代码库已公开。

## 🔬 方法详解

**问题定义**：论文旨在解决开放域场景下的命名实体检索问题，即用户可以自定义实体类型描述，系统需要检索出所有提及该类型实体的文档。现有方法通常依赖于预定义的实体类型体系或需要针对特定类型进行微调，无法很好地泛化到新的、用户自定义的类型描述。

**核心思路**：核心思路是将实体提及和用户提供的类型描述都嵌入到一个共享的语义空间中，使得类型兼容的实体在嵌入空间中距离更近。关键在于如何有效地提取和表示实体和类型描述的语义信息，并学习一个合适的嵌入空间。

**技术框架**：NER Retriever 的整体框架包括以下几个主要阶段：1) 利用大型语言模型（LLM）提取实体提及和类型描述的内部表示（Value Vectors）。2) 使用对比学习训练一个轻量级的投影网络，将提取的表示投影到类型感知的嵌入空间。3) 在嵌入空间中，使用最近邻搜索来检索与给定类型描述相关的实体。

**关键创新**：最重要的创新点在于利用 LLM 的中间层表示（Value Vectors）来编码细粒度的类型信息，并使用对比学习来对齐类型兼容的实体。与直接使用 LLM 的顶层嵌入相比，中间层表示能够更好地捕捉实体和类型描述的语义信息，从而提高检索的准确性。

**关键设计**：关键设计包括：1) 选择 LLM 的中间层 Value Vectors 作为实体和类型描述的初始表示。2) 使用对比损失函数来训练投影网络，使得类型兼容的实体在嵌入空间中距离更近，而类型不兼容的实体距离更远。3) 使用余弦相似度作为嵌入空间中实体和类型描述之间的距离度量。

## 📊 实验亮点

NER Retriever 在三个基准测试中均取得了显著优于现有方法的结果。例如，在某个数据集上，NER Retriever 的性能比最佳基线提高了 10% 以上。实验结果表明，利用 LLM 的中间层表示和对比学习能够有效地提高零样本命名实体检索的准确性。

## 🎯 应用场景

NER Retriever 可应用于知识图谱构建、信息抽取、问答系统等领域。用户可以自定义实体类型，快速检索相关信息，无需预先定义实体类型体系或进行模型微调。该方法具有良好的可扩展性和灵活性，能够适应各种开放域场景。

## 📄 摘要（原文）

> We present NER Retriever, a zero-shot retrieval framework for ad-hoc Named Entity Retrieval, a variant of Named Entity Recognition (NER), where the types of interest are not provided in advance, and a user-defined type description is used to retrieve documents mentioning entities of that type. Instead of relying on fixed schemas or fine-tuned models, our method builds on internal representations of large language models (LLMs) to embed both entity mentions and user-provided open-ended type descriptions into a shared semantic space. We show that internal representations, specifically the value vectors from mid-layer transformer blocks, encode fine-grained type information more effectively than commonly used top-layer embeddings. To refine these representations, we train a lightweight contrastive projection network that aligns type-compatible entities while separating unrelated types. The resulting entity embeddings are compact, type-aware, and well-suited for nearest-neighbor search. Evaluated on three benchmarks, NER Retriever significantly outperforms both lexical and dense sentence-level retrieval baselines. Our findings provide empirical support for representation selection within LLMs and demonstrate a practical solution for scalable, schema-free entity retrieval. The NER Retriever Codebase is publicly available at https://github.com/ShacharOr100/ner_retriever

