---
layout: default
title: "QuantMCP: Grounding Large Language Models in Verifiable Financial Reality"
---

# QuantMCP: Grounding Large Language Models in Verifiable Financial Reality

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06622" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06622v2</a>
  <a href="https://arxiv.org/pdf/2506.06622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06622v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06622v2', 'QuantMCP: Grounding Large Language Models in Verifiable Financial Reality')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Zeng

**分类**: cs.CE, cs.AI

**发布日期**: 2025-06-07 (更新: 2025-06-12)

---

## 💡 一句话要点

**提出QuantMCP以解决LLM在金融数据应用中的现实性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

## 📋 核心要点

1. 现有大型语言模型在金融领域应用时，常面临数据幻觉和缺乏实时可验证信息的问题，限制了其有效性。
2. QuantMCP框架通过模型上下文协议（MCP）实现标准化的工具调用，使LLMs能够与多种金融数据API无缝对接，提升数据检索的准确性。
3. 通过使用QuantMCP，LLMs能够获得结构化的金融数据，从而增强其分析能力，支持更为精准的金融决策。
4. method_zh

## 📝 摘要（中文）

大型语言模型（LLMs）在金融分析和决策中具有巨大的潜力，但由于数据幻觉和缺乏实时可验证的金融信息，其直接应用受到限制。本文介绍了QuantMCP，一个旨在严格将LLMs与金融现实相结合的新框架。通过利用模型上下文协议（MCP）进行标准化和安全的工具调用，QuantMCP使LLMs能够准确地与多种可通过Python访问的金融数据API（如Wind、yfinance）进行交互。用户可以通过自然语言精确检索最新的金融数据，从而克服LLMs在事实数据回忆方面的固有局限性。更重要的是，一旦获得这些经过验证的结构化数据，LLMs的分析能力将被激发，能够进行复杂的数据解读、生成洞察，并最终支持更为明智的金融决策过程。QuantMCP为对话式AI与复杂金融数据世界之间提供了一个稳健、可扩展和安全的桥梁，旨在增强LLM在金融应用中的可靠性和分析深度。

## 📄 摘要（原文）

> Large Language Models (LLMs) hold immense promise for revolutionizing financial analysis and decision-making, yet their direct application is often hampered by issues of data hallucination and lack of access to real-time, verifiable financial information. This paper introduces QuantMCP, a novel framework designed to rigorously ground LLMs in financial reality. By leveraging the Model Context Protocol (MCP) for standardized and secure tool invocation, QuantMCP enables LLMs to accurately interface with a diverse array of Python-accessible financial data APIs (e.g., Wind, yfinance). Users can interact via natural language to precisely retrieve up-to-date financial data, thereby overcoming LLM's inherent limitations in factual data recall. More critically, once furnished with this verified, structured data, the LLM's analytical capabilities are unlocked, empowering it to perform sophisticated data interpretation, generate insights, and ultimately support more informed financial decision-making processes. QuantMCP provides a robust, extensible, and secure bridge between conversational AI and the complex world of financial data, aiming to enhance both the reliability and the analytical depth of LLM applications in finance.

