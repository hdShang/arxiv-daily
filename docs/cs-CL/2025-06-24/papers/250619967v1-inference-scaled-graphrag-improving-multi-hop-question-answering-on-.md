---
layout: default
title: "Inference Scaled GraphRAG: Improving Multi Hop Question Answering on Knowledge Graphs"
---

# Inference Scaled GraphRAG: Improving Multi Hop Question Answering on Knowledge Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19967" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19967v1</a>
  <a href="https://arxiv.org/pdf/2506.19967.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19967v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19967v1', 'Inference Scaled GraphRAG: Improving Multi Hop Question Answering on Knowledge Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Travis Thompson, Seung-Hwan Lim, Paul Liu, Ruoying He, Dongkuan Xu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-24

---

## 💡 一句话要点

**提出Inference-Scaled GraphRAG以解决知识图谱多跳问答问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `多跳问答` `推理增强` `大型语言模型` `图遍历` `计算扩展` `信息检索`

## 📋 核心要点

1. 现有的RAG和GraphRAG方法在处理知识图谱中的多跳推理时，无法有效捕捉节点间的关系结构，导致性能不足。
2. 论文提出的Inference-Scaled GraphRAG框架，通过推理时计算扩展，结合深度思维链图遍历和多数投票机制，提升了图推理能力。
3. 在GRBench基准测试中，该方法显著提高了多跳问答的性能，相较于传统方法有显著的提升，展示了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在语言理解和生成方面取得了显著进展，但在知识密集型推理任务上仍表现不佳，主要由于对结构化上下文和多跳信息的访问有限。检索增强生成（RAG）部分缓解了这一问题，但传统的RAG和GraphRAG方法往往无法有效捕捉知识图谱中节点之间的关系结构。我们提出了Inference-Scaled GraphRAG，这是一种通过推理时计算扩展来增强基于LLM的图推理的新框架。该方法结合了顺序扩展与深度思维链图遍历，以及在交错推理-执行循环中对采样轨迹进行多数投票的并行扩展。实验结果表明，我们的方法在GRBench基准上显著提高了多跳问答性能，相较于传统的GraphRAG和先前的图遍历基线取得了显著提升。这些发现表明，推理时扩展是一种实用且与架构无关的解决方案，适用于结构化知识推理。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在知识图谱多跳问答任务中的性能不足，现有的RAG和GraphRAG方法未能有效利用知识图谱中的关系结构，导致推理能力受限。

**核心思路**：提出Inference-Scaled GraphRAG框架，通过推理时计算扩展，结合深度思维链图遍历和多数投票机制，旨在提升LLM在知识图谱上的推理能力。

**技术框架**：该框架主要包括两个扩展阶段：顺序扩展和并行扩展。顺序扩展通过深度思维链遍历知识图谱，而并行扩展则通过对采样轨迹进行多数投票来增强推理的准确性。

**关键创新**：最重要的创新在于推理时计算扩展的应用，这种方法与传统的RAG和GraphRAG方法相比，能够更好地捕捉知识图谱中的关系结构，从而提升推理效果。

**关键设计**：在设计中，采用了深度思维链的图遍历策略，结合了对多个轨迹的投票机制，以确保推理结果的准确性和鲁棒性。

## 📊 实验亮点

实验结果显示，Inference-Scaled GraphRAG在GRBench基准上显著提高了多跳问答性能，相较于传统GraphRAG方法，性能提升幅度达到XX%（具体数据未知），并且在多个图遍历基线中也表现出色，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、知识管理和信息检索等。通过提升多跳问答的能力，Inference-Scaled GraphRAG能够在实际应用中提供更为准确和高效的知识获取方式，推动智能系统在复杂推理任务中的应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved impressive capabilities in language understanding and generation, yet they continue to underperform on knowledge-intensive reasoning tasks due to limited access to structured context and multi-hop information. Retrieval-Augmented Generation (RAG) partially mitigates this by grounding generation in retrieved context, but conventional RAG and GraphRAG methods often fail to capture relational structure across nodes in knowledge graphs. We introduce Inference-Scaled GraphRAG, a novel framework that enhances LLM-based graph reasoning by applying inference-time compute scaling. Our method combines sequential scaling with deep chain-of-thought graph traversal, and parallel scaling with majority voting over sampled trajectories within an interleaved reasoning-execution loop. Experiments on the GRBench benchmark demonstrate that our approach significantly improves multi-hop question answering performance, achieving substantial gains over both traditional GraphRAG and prior graph traversal baselines. These findings suggest that inference-time scaling is a practical and architecture-agnostic solution for structured knowledge reasoning with LLMs

