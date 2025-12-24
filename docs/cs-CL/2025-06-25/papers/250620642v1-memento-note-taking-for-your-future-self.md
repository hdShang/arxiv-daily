---
layout: default
title: "Memento: Note-Taking for Your Future Self"
---

# Memento: Note-Taking for Your Future Self

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20642" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20642v1</a>
  <a href="https://arxiv.org/pdf/2506.20642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20642v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20642v1', 'Memento: Note-Taking for Your Future Self')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao Wan, Albert Gong, Mihir Mishra, Carl-Leander Henneking, Claas Beger, Kilian Q. Weinberger

**分类**: cs.CL

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出Memento以解决多跳问答中的推理与检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多跳问答` `信息检索` `推理策略` `动态数据库` `性能提升`

## 📋 核心要点

1. 现有方法在多跳问答中难以有效结合推理与信息检索，导致性能不足。
2. Memento通过将复杂问题分解为小步骤，动态构建事实数据库，提升了问答能力。
3. 在多个基准测试中，Memento显著提升了性能，如在PhantomWiki基准上性能翻倍。

## 📝 摘要（中文）

大型语言模型（LLMs）在仅依赖推理的任务中表现优异，但在推理与检索紧密结合的多跳问答中却面临挑战。为了解决这些局限性，本文提出了一种新的提示策略Memento，该策略首先将复杂问题分解为更小的步骤，然后动态构建事实数据库，最后将这些事实组合起来以解决问题。实验结果表明，Memento在多个基准测试中显著提升了现有提示策略的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多跳问答中推理与检索结合不佳的问题。现有方法在处理复杂问题时，往往无法有效整合所需信息，导致回答准确性降低。

**核心思路**：Memento的核心思路是将复杂问题分解为多个小步骤，通过动态构建事实数据库来支持推理过程。这种设计使得模型能够更好地利用上下文信息，从而提高回答的准确性。

**技术框架**：Memento的整体架构分为三个主要阶段：第一阶段是将复杂问题分解；第二阶段是利用LLMs动态构建事实数据库；第三阶段是将收集到的事实整合以得出最终答案。

**关键创新**：Memento的主要创新在于其三阶段的处理流程，显著区别于传统的链式推理方法，能够更有效地处理多跳问答任务。

**关键设计**：在实现过程中，Memento采用了特定的参数设置和损失函数，以优化模型在动态构建事实时的表现，确保信息的准确性和相关性。

## 📊 实验亮点

在9步的PhantomWiki基准测试中，Memento使得链式推理的性能翻倍。在开放域的2WikiMultiHopQA中，Memento使得CoT-RAG的F1得分提升超过20个百分点，相较于多跳RAG基线IRCoT提升超过13个百分点。在MuSiQue数据集上，Memento使ReAct的F1得分提升超过3个百分点，显示出其在代理设置中的有效性。

## 🎯 应用场景

Memento的研究成果在多个领域具有潜在应用价值，包括智能问答系统、信息检索、教育辅助工具等。通过提升多跳问答的准确性，Memento能够帮助用户更高效地获取信息，促进知识的传播与学习。

## 📄 摘要（原文）

> Large language models (LLMs) excel at reasoning-only tasks, but struggle when reasoning must be tightly coupled with retrieval, as in multi-hop question answering. To overcome these limitations, we introduce a prompting strategy that first decomposes a complex question into smaller steps, then dynamically constructs a database of facts using LLMs, and finally pieces these facts together to solve the question. We show how this three-stage strategy, which we call Memento, can boost the performance of existing prompting strategies across diverse settings. On the 9-step PhantomWiki benchmark, Memento doubles the performance of chain-of-thought (CoT) when all information is provided in context. On the open-domain version of 2WikiMultiHopQA, CoT-RAG with Memento improves over vanilla CoT-RAG by more than 20 F1 percentage points and over the multi-hop RAG baseline, IRCoT, by more than 13 F1 percentage points. On the challenging MuSiQue dataset, Memento improves ReAct by more than 3 F1 percentage points, demonstrating its utility in agentic settings.

