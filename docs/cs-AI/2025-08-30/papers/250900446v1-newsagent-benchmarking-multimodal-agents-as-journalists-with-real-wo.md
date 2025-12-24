---
layout: default
title: "NEWSAGENT: Benchmarking Multimodal Agents as Journalists with Real-World Newswriting Tasks"
---

# NEWSAGENT: Benchmarking Multimodal Agents as Journalists with Real-World Newswriting Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00446" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00446v1</a>
  <a href="https://arxiv.org/pdf/2509.00446.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00446v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00446v1', 'NEWSAGENT: Benchmarking Multimodal Agents as Journalists with Real-World Newswriting Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yen-Che Chien, Kuang-Da Wang, Wei-Yao Wang, Wen-Chih Peng

**分类**: cs.AI

**发布日期**: 2025-08-30

**备注**: Preprint

---

## 💡 一句话要点

**提出NEWSAGENT以评估多模态智能体在新闻写作中的应用**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态智能体` `新闻写作` `信息检索` `叙事整合` `自动化写作` `基准评估` `真实世界应用`

## 📋 核心要点

1. 现有智能体在多模态数据处理中的能力尚未得到充分评估，尤其是在新闻写作领域的实际应用中。
2. 论文提出NEWSAGENT基准，旨在评估智能体如何从多模态原始内容中自动生成结构化新闻，强调信息检索与叙事整合的能力。
3. 实验结果表明，智能体在信息检索方面表现良好，但在规划和叙事整合上仍面临挑战，显示出该领域的进一步研究需求。

## 📝 摘要（中文）

随着自主数字智能体的进步，如何提高多模态网络数据的生产力仍不明确。本文研究了新闻写作领域，提出了NEWSAGENT基准，评估智能体如何自动搜索、选择信息并生成新闻文章。该基准包含6000个经过人工验证的真实新闻示例，评估结果显示，智能体在检索相关事实方面表现良好，但在规划和叙事整合上存在困难。NEWSAGENT为评估智能体在多模态数据处理中的能力提供了现实的测试平台。

## 🔬 方法详解

**问题定义**：本文旨在解决智能体在新闻写作中如何有效处理多模态数据的问题。现有方法在信息检索和叙事整合方面存在不足，无法满足真实新闻写作的需求。

**核心思路**：论文的核心思路是通过NEWSAGENT基准评估智能体在新闻写作中的能力，特别是如何从多模态内容中提取信息并生成结构化文章。这样的设计旨在模拟真实新闻写作过程中的复杂性。

**技术框架**：整体架构包括信息检索、叙事规划和文章生成三个主要模块。智能体首先根据写作指令进行信息检索，然后进行叙事规划，最后生成完整的新闻文章。

**关键创新**：最重要的技术创新点在于引入了一个真实的新闻写作基准，包含6000个经过验证的实例，强调了信息检索与叙事整合的挑战，这与现有的简单摘要或检索任务有本质区别。

**关键设计**：在设计中，采用了特定的参数设置和损失函数，以优化智能体在信息检索和叙事整合方面的表现，确保生成的新闻文章符合实际新闻写作的标准。

## 📊 实验亮点

实验结果显示，智能体在信息检索方面表现出色，能够有效获取相关事实。然而，在规划和叙事整合方面仍存在显著不足，表明该领域仍需进一步研究与改进。具体性能数据和对比基线尚未详细披露。

## 🎯 应用场景

该研究的潜在应用领域包括新闻自动化写作、信息检索系统和智能内容生成。通过提升智能体在多模态数据处理中的能力，未来可实现更高效的新闻生产和信息传播，推动新闻行业的数字化转型。

## 📄 摘要（原文）

> Recent advances in autonomous digital agents from industry (e.g., Manus AI and Gemini's research mode) highlight potential for structured tasks by autonomous decision-making and task decomposition; however, it remains unclear to what extent the agent-based systems can improve multimodal web data productivity. We study this in the realm of journalism, which requires iterative planning, interpretation, and contextual reasoning from multimodal raw contents to form a well structured news. We introduce NEWSAGENT, a benchmark for evaluating how agents can automatically search available raw contents, select desired information, and edit and rephrase to form a news article by accessing core journalistic functions. Given a writing instruction and firsthand data as how a journalist initiates a news draft, agents are tasked to identify narrative perspectives, issue keyword-based queries, retrieve historical background, and generate complete articles. Unlike typical summarization or retrieval tasks, essential context is not directly available and must be actively discovered, reflecting the information gaps faced in real-world news writing. NEWSAGENT includes 6k human-verified examples derived from real news, with multimodal contents converted to text for broad model compatibility. We evaluate open- and closed-sourced LLMs with commonly-used agentic frameworks on NEWSAGENT, which shows that agents are capable of retrieving relevant facts but struggling with planning and narrative integration. We believe that NEWSAGENT serves a realistic testbed for iterating and evaluating agent capabilities in terms of multimodal web data manipulation to real-world productivity.

