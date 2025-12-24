---
layout: default
title: "RAGuard: A Novel Approach for in-context Safe Retrieval Augmented Generation for LLMs"
---

# RAGuard: A Novel Approach for in-context Safe Retrieval Augmented Generation for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03768" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03768v1</a>
  <a href="https://arxiv.org/pdf/2509.03768.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03768v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03768v1', 'RAGuard: A Novel Approach for in-context Safe Retrieval Augmented Generation for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Connor Walker, Koorosh Aslansefat, Mohammad Naveed Akram, Yiannis Papadopoulos

**分类**: cs.AI, stat.ML

**发布日期**: 2025-09-03

---

## 💡 一句话要点

**RAGuard：面向LLM，用于安全检索增强生成的新框架，提升海上风电维护安全性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `大型语言模型` `安全性` `海上风电` `信息检索` `安全关键系统` `双索引` `SafetyClamp`

## 📋 核心要点

1. 传统LLM在海上风电维护等专业领域面临准确性和安全性的挑战，尤其是在处理专业或意外情况时。
2. RAGuard通过并行查询技术和安全文档索引，并分配独立的检索预算，确保技术深度和安全覆盖。
3. 实验表明，RAGuard显著提升了安全召回率，从接近0%提升到50%以上，同时保持了较高的技术召回率。

## 📝 摘要（中文）

本文提出RAGuard，一种增强的检索增强生成（RAG）框架，它显式地将安全关键文档与技术手册集成，以解决大型语言模型（LLM）在海上风电（OSW）维护中面对高度专业化或意外情况时准确性和安全性不足的问题。RAGuard通过向两个索引并行发出查询，并为知识和安全分配单独的检索预算，从而保证技术深度和安全覆盖。此外，还开发了SafetyClamp扩展，它获取更大的候选池，对安全进行“硬钳制”，保证精确的槽位。在稀疏（BM25）、密集（密集段落检索）和混合检索范式下进行了评估，测量了技术召回率@K和安全召回率@K。RAGuard及其SafetyClamp扩展将安全召回率@K从RAG的几乎0%提高到50%以上，同时保持技术召回率在60%以上。这些结果表明，RAGuard和SafetyClamp有潜力为关键维护环境中LLM驱动的决策支持集成安全保障建立新标准。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在处理诸如海上风电维护等高度专业化和安全关键型任务时，面临着准确性和安全性的挑战。传统的RAG方法可能无法充分检索到安全相关的文档，导致LLM生成不安全的或不完整的响应。因此，需要一种能够同时保证技术深度和安全覆盖的RAG框架。

**核心思路**：RAGuard的核心思路是将安全相关的文档与技术文档分开索引，并为它们分配独立的检索预算。通过并行查询两个索引，RAGuard可以确保在检索过程中同时考虑技术信息和安全信息。SafetyClamp扩展进一步强化了安全保障，通过扩大候选池并强制包含安全文档，确保安全信息不会被遗漏。

**技术框架**：RAGuard框架包含以下主要模块：1) **双索引构建**：分别构建技术文档索引和安全文档索引。2) **并行查询**：同时向两个索引发出查询，分别检索技术文档和安全文档。3) **检索预算分配**：为技术检索和安全检索分配独立的预算，控制检索结果的数量。4) **SafetyClamp (可选)**：从更大的候选池中检索安全文档，并强制包含在最终的检索结果中。5) **LLM生成**：将检索到的技术文档和安全文档作为上下文，输入LLM生成最终的响应。

**关键创新**：RAGuard的关键创新在于其双索引结构和独立的检索预算分配机制。与传统的RAG方法相比，RAGuard能够更有效地检索到安全相关的文档，从而提高LLM生成的响应的安全性。SafetyClamp扩展进一步强化了安全保障，通过强制包含安全文档，避免了安全信息的遗漏。

**关键设计**：RAGuard的关键设计包括：1) **索引构建策略**：选择合适的索引方法（如BM25、DPR）来构建技术文档索引和安全文档索引。2) **检索预算分配比例**：根据任务的特点，合理分配技术检索预算和安全检索预算。3) **SafetyClamp参数**：设置合适的候选池大小和强制包含的安全文档数量，以平衡安全性和效率。

## 📊 实验亮点

实验结果表明，RAGuard及其SafetyClamp扩展在提高安全召回率方面表现出色。在RAG框架中，安全召回率@K几乎为0%，而RAGuard可以将安全召回率@K提高到50%以上，同时保持技术召回率在60%以上。这表明RAGuard能够有效地检索到安全相关的文档，从而提高LLM生成的响应的安全性。

## 🎯 应用场景

RAGuard可应用于各种安全关键型领域，例如：海上风电维护、航空航天、医疗保健等。通过将安全知识融入LLM的决策过程中，RAGuard可以提高操作的安全性，降低事故发生的风险，并为专业人员提供更可靠的决策支持。未来，RAGuard有望成为LLM在安全关键领域应用的重要基石。

## 📄 摘要（原文）

> Accuracy and safety are paramount in Offshore Wind (OSW) maintenance, yet conventional Large Language Models (LLMs) often fail when confronted with highly specialised or unexpected scenarios. We introduce RAGuard, an enhanced Retrieval-Augmented Generation (RAG) framework that explicitly integrates safety-critical documents alongside technical manuals.By issuing parallel queries to two indices and allocating separate retrieval budgets for knowledge and safety, RAGuard guarantees both technical depth and safety coverage. We further develop a SafetyClamp extension that fetches a larger candidate pool, "hard-clamping" exact slot guarantees to safety. We evaluate across sparse (BM25), dense (Dense Passage Retrieval) and hybrid retrieval paradigms, measuring Technical Recall@K and Safety Recall@K. Both proposed extensions of RAG show an increase in Safety Recall@K from almost 0\% in RAG to more than 50\% in RAGuard, while maintaining Technical Recall above 60\%. These results demonstrate that RAGuard and SafetyClamp have the potential to establish a new standard for integrating safety assurance into LLM-powered decision support in critical maintenance contexts.

