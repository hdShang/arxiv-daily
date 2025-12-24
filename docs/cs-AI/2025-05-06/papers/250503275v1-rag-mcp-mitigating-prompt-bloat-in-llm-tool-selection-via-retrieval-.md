---
layout: default
title: "RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection via Retrieval-Augmented Generation"
---

# RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection via Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03275" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03275v1</a>
  <a href="https://arxiv.org/pdf/2505.03275.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03275v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03275v1', 'RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection via Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tiantian Gan, Qiyao Sun

**分类**: cs.AI, cs.SE

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出RAG-MCP以解决大型语言模型工具选择中的提示膨胀问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `工具选择` `语义检索` `生成模型` `模型上下文协议` `提示膨胀` `检索增强生成`

## 📋 核心要点

1. 现有方法在处理大量外部工具时，面临提示膨胀和选择复杂性的问题，导致大型语言模型的性能受限。
2. RAG-MCP通过语义检索技术，提前识别与查询相关的工具，从而减少传递给模型的提示信息量，简化决策过程。
3. 实验结果显示，RAG-MCP显著降低了提示令牌数量，并在工具选择准确率上取得了显著提升，验证了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在有效利用日益增长的外部工具时面临提示膨胀和选择复杂性的问题。为此，本文提出了RAG-MCP，一个基于检索增强生成的框架，通过外部索引的语义检索来识别与给定查询最相关的模型上下文协议（MCP），从而简化决策过程并显著减少提示大小。实验表明，RAG-MCP在基准任务中显著减少了提示令牌数量（超过50%），并将工具选择准确率提高了三倍以上（43.13%对比基线的13.62%）。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在工具选择中面临的提示膨胀和选择复杂性问题。现有方法在处理多个外部工具时，往往需要传递大量信息给模型，导致性能下降。

**核心思路**：RAG-MCP的核心思路是通过语义检索技术，提前识别与用户查询最相关的工具，从而减少传递给模型的提示信息量。这种设计旨在简化决策过程，提高工具选择的效率和准确性。

**技术框架**：RAG-MCP的整体架构包括两个主要模块：首先是语义检索模块，从外部索引中识别相关的MCP；其次是生成模块，将选定的工具描述传递给大型语言模型进行处理。

**关键创新**：RAG-MCP的主要创新在于其检索增强生成的框架，通过外部索引的语义检索来优化工具选择过程。这一方法与传统的直接传递所有工具信息的方式有本质区别，显著降低了提示的复杂性。

**关键设计**：在设计中，RAG-MCP采用了高效的语义检索算法，以确保快速准确地识别相关工具。同时，模型的输入参数经过优化，以适应不同的查询场景，确保生成模块的输出质量。

## 📊 实验亮点

实验结果表明，RAG-MCP在基准任务中显著减少了提示令牌数量，超过50%的减少幅度，同时工具选择准确率从基线的13.62%提升至43.13%，实现了三倍以上的提升，验证了其有效性和实用性。

## 🎯 应用场景

RAG-MCP的研究成果具有广泛的应用潜力，尤其在需要集成多个外部工具的智能助手、自动化系统和复杂查询处理等领域。通过提高工具选择的准确性和效率，该框架能够显著提升大型语言模型在实际应用中的表现，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Large language models (LLMs) struggle to effectively utilize a growing number of external tools, such as those defined by the Model Context Protocol (MCP)\cite{IntroducingMCP}, due to prompt bloat and selection complexity. We introduce RAG-MCP, a Retrieval-Augmented Generation framework that overcomes this challenge by offloading tool discovery. RAG-MCP uses semantic retrieval to identify the most relevant MCP(s) for a given query from an external index before engaging the LLM. Only the selected tool descriptions are passed to the model, drastically reducing prompt size and simplifying decision-making. Experiments, including an MCP stress test, demonstrate RAG-MCP significantly cuts prompt tokens (e.g., by over 50%) and more than triples tool selection accuracy (43.13% vs 13.62% baseline) on benchmark tasks. RAG-MCP enables scalable and accurate tool integration for LLMs.

