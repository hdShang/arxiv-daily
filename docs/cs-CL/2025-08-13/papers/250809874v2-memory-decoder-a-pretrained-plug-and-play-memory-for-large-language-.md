---
layout: default
title: "Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models"
---

# Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09874" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09874v2</a>
  <a href="https://arxiv.org/pdf/2508.09874.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09874v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09874v2', 'Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Cao, Jiarui Wang, Rubin Wei, Qipeng Guo, Kai Chen, Bowen Zhou, Zhouhan Lin

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-13 (更新: 2025-10-23)

---

## 💡 一句话要点

**提出Memory Decoder以解决大语言模型领域适应问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `领域适应` `Memory Decoder` `非参数检索` `变换器解码器` `生物医学` `金融` `法律`

## 📋 核心要点

1. 现有方法如DAPT在领域适应中需要昂贵的全参数训练，并且容易导致灾难性遗忘。
2. Memory Decoder是一种可插拔的预训练内存，能够在不修改原始模型参数的情况下实现高效的领域适应。
3. 实验表明，Memory Decoder在生物医学、金融和法律领域的应用中，平均降低了6.17分的困惑度。

## 📝 摘要（中文）

大语言模型（LLMs）在通用语言任务中表现出色，但在特定领域的适应性仍然面临挑战。现有的方法如领域自适应预训练（DAPT）需要昂贵的全参数训练，并且容易出现灾难性遗忘。同时，检索增强生成（RAG）由于昂贵的最近邻搜索和更长的上下文引入了显著的推理延迟。本文提出Memory Decoder，这是一种可插拔的预训练内存，能够在不改变原始模型参数的情况下实现高效的领域适应。Memory Decoder使用一个小型的变换器解码器，学习模仿外部非参数检索器的行为。经过训练后，Memory Decoder可以无缝集成到任何共享相同分词器的预训练语言模型中，无需特定模型的修改。实验结果表明，Memory Decoder有效地将多种Qwen和Llama模型适应于生物医学、金融和法律三个特定领域，平均降低困惑度6.17分。总体而言，Memory Decoder引入了一种以特定预训练内存组件为中心的新范式，旨在实现领域特定的适应。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在特定领域适应中的挑战，现有方法如DAPT和RAG存在高成本和效率低下的问题。

**核心思路**：Memory Decoder通过引入一个小型变换器解码器，模仿外部非参数检索器的行为，从而实现高效的领域适应，而无需修改原始模型的参数。

**技术框架**：Memory Decoder的整体架构包括一个小型变换器解码器和一个外部检索器。解码器学习如何从检索器中获取信息，并将其整合到语言模型的生成过程中。

**关键创新**：Memory Decoder的主要创新在于其可插拔的内存架构，允许与任何共享相同分词器的预训练语言模型无缝集成，这与传统的全参数训练方法形成鲜明对比。

**关键设计**：在设计中，Memory Decoder的损失函数和网络结构经过精心调整，以确保其能够有效模仿外部检索器的行为，同时保持较低的推理延迟。具体的参数设置和训练策略在实验中进行了优化。

## 📊 实验亮点

实验结果显示，Memory Decoder在将Qwen和Llama模型适应于生物医学、金融和法律领域时，平均降低了6.17分的困惑度，显著提升了模型在特定领域的表现，展示了其在领域适应中的有效性。

## 🎯 应用场景

Memory Decoder的潜在应用领域包括生物医学、金融和法律等专业领域，能够帮助大语言模型更好地适应特定领域的需求，提升其在专业任务中的表现。未来，该技术可能会在更多领域中推广应用，推动领域特定模型的快速开发与部署。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown strong abilities in general language tasks, yet adapting them to specific domains remains a challenge. Current method like Domain Adaptive Pretraining (DAPT) requires costly full-parameter training and suffers from catastrophic forgetting. Meanwhile, Retrieval-Augmented Generation (RAG) introduces substantial inference latency due to expensive nearest-neighbor searches and longer context. This paper introduces Memory Decoder, a plug-and-play pretrained memory that enables efficient domain adaptation without changing the original model's parameters. Memory Decoder employs a small transformer decoder that learns to imitate the behavior of an external non-parametric retriever. Once trained, Memory Decoder can be seamlessly integrated with any pretrained language model that shares the same tokenizer, requiring no model-specific modifications. Experimental results demonstrate that Memory Decoder enables effective adaptation of various Qwen and Llama models to three distinct specialized domains: biomedicine, finance, and law, reducing perplexity by an average of 6.17 points. Overall, Memory Decoder introduces a novel paradigm centered on a specially pretrained memory component designed for domain-specific adaptation. This memory architecture can be integrated in a plug-and-play manner, consistently enhancing performance across multiple models within the target domain.

