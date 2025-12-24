---
layout: default
title: "MultiFinRAG: An Optimized Multimodal Retrieval-Augmented Generation (RAG) Framework for Financial Question Answering"
---

# MultiFinRAG: An Optimized Multimodal Retrieval-Augmented Generation (RAG) Framework for Financial Question Answering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20821" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20821v1</a>
  <a href="https://arxiv.org/pdf/2506.20821.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20821v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20821v1', 'MultiFinRAG: An Optimized Multimodal Retrieval-Augmented Generation (RAG) Framework for Financial Question Answering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chinmay Gondhalekar, Urjitkumar Patel, Fang-Chun Yeh

**分类**: cs.CL, cs.AI, cs.CE

**发布日期**: 2025-06-25

**备注**: Preprint Copy

---

## 💡 一句话要点

**提出MultiFinRAG以解决金融问答中的多模态推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `金融问答` `检索增强生成` `跨模态推理` `轻量化模型`

## 📋 核心要点

1. 现有方法在处理金融文档时面临多模态推理的挑战，尤其是由于令牌限制和布局丢失，导致信息碎片化。
2. MultiFinRAG通过轻量化的多模态LLM进行多模态提取，并采用分层回退策略，实现跨模态推理。
3. 在复杂的金融问答任务中，MultiFinRAG的准确率比基线模型提高了19个百分点，表现出色。

## 📝 摘要（中文）

金融文档如10-K、10-Q和投资者演示文稿通常包含数百页内容，结合了密集的叙述文本、结构化表格和复杂图形。回答这些内容的问题常常需要跨模态的联合推理，这对传统的大型语言模型（LLMs）和检索增强生成（RAG）管道造成了挑战。本文提出了MultiFinRAG，一个专为金融问答设计的检索增强生成框架。该框架通过将表格和图像分组并发送至轻量化的多模态LLM进行提取，生成结构化的JSON输出和简洁的文本摘要。随后，这些输出与叙述文本一起进行嵌入和索引，以实现精确检索。最终，MultiFinRAG在复杂的金融问答任务中，准确率比ChatGPT-4o（免费版）提高了19个百分点。

## 🔬 方法详解

**问题定义**：本文旨在解决在金融文档中进行问答时，传统方法面临的多模态推理困难，尤其是信息的令牌限制和布局丢失问题。

**核心思路**：MultiFinRAG的核心思路是通过轻量化的多模态LLM进行信息提取，并结合分层回退策略，以便在需要时动态调整上下文，增强跨模态推理能力。

**技术框架**：该框架包括多个主要模块：首先进行多模态提取，将表格和图像分批处理；然后生成结构化的JSON输出和文本摘要；接着进行嵌入和索引；最后实施分层回退策略以优化检索过程。

**关键创新**：MultiFinRAG的创新在于其专为金融问答设计的检索增强生成框架，能够有效处理多模态信息，并在动态上下文中进行推理，显著提升了问答准确性。

**关键设计**：该框架采用了量化的轻量化多模态LLM，设置了模态感知的相似性阈值，并设计了分层回退策略，以确保在不同上下文下的有效信息检索。

## 📊 实验亮点

在复杂的金融问答任务中，MultiFinRAG的准确率比ChatGPT-4o（免费版）高出19个百分点，展示了其在处理多模态信息时的显著优势。这一结果表明，MultiFinRAG在金融领域的应用潜力巨大。

## 🎯 应用场景

MultiFinRAG在金融领域的潜在应用广泛，包括投资分析、财务报告解读和风险评估等。其高效的多模态推理能力能够帮助金融专业人士快速获取关键信息，提高决策效率。未来，该框架还可以扩展到其他需要多模态信息处理的领域，如法律文档分析和医疗记录解读。

## 📄 摘要（原文）

> Financial documents--such as 10-Ks, 10-Qs, and investor presentations--span hundreds of pages and combine diverse modalities, including dense narrative text, structured tables, and complex figures. Answering questions over such content often requires joint reasoning across modalities, which strains traditional large language models (LLMs) and retrieval-augmented generation (RAG) pipelines due to token limitations, layout loss, and fragmented cross-modal context. We introduce MultiFinRAG, a retrieval-augmented generation framework purpose-built for financial QA. MultiFinRAG first performs multimodal extraction by grouping table and figure images into batches and sending them to a lightweight, quantized open-source multimodal LLM, which produces both structured JSON outputs and concise textual summaries. These outputs, along with narrative text, are embedded and indexed with modality-aware similarity thresholds for precise retrieval. A tiered fallback strategy then dynamically escalates from text-only to text+table+image contexts when necessary, enabling cross-modal reasoning while reducing irrelevant context. Despite running on commodity hardware, MultiFinRAG achieves 19 percentage points higher accuracy than ChatGPT-4o (free-tier) on complex financial QA tasks involving text, tables, images, and combined multimodal reasoning.

