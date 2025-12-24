---
layout: default
title: "MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents"
---

# MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20231" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20231v2</a>
  <a href="https://arxiv.org/pdf/2505.20231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20231v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20231v2', 'MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiming Du, Bingbing Wang, Yang He, Bin Liang, Baojun Wang, Zhongyang Li, Lin Gui, Jeff Z. Pan, Ruifeng Xu, Kam-Fai Wong

**分类**: cs.CL

**发布日期**: 2025-05-26 (更新: 2025-08-13)

---

## 💡 一句话要点

**提出MemGuide以解决多会话对话系统中的意图驱动记忆选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `任务导向对话` `大型语言模型` `意图驱动` `记忆选择` `多会话对话` `检索增强生成` `对话系统`

## 📋 核心要点

1. 现有的任务导向对话系统在多会话对话中主要依赖语义相似性，忽视了任务意图，导致任务连贯性不足。
2. 本文提出MemGuide框架，通过意图对齐检索和缺失槽引导过滤，优化记忆单元选择以提高对话质量。
3. 在MS-TOD基准上，MemGuide显著提高了任务成功率和对话效率，展示了其在多会话任务完成中的有效性。

## 📝 摘要（中文）

现代任务导向对话系统越来越依赖大型语言模型（LLM）代理，利用检索增强生成（RAG）和长上下文能力进行长期记忆的使用。然而，这些方法主要基于语义相似性，忽视了任务意图，从而降低了多会话对话的任务连贯性。为了解决这一挑战，本文提出了MemGuide，一个用于意图驱动记忆选择的两阶段框架。该框架通过意图对齐检索和缺失槽引导过滤来优化记忆单元的选择。基于此框架，我们引入了MS-TOD，这是第一个包含132种多样化角色、956个任务目标和注释意图对齐记忆目标的多会话对话基准。评估结果表明，MemGuide在多会话设置中将任务成功率提高了11%（88% -> 99%），并减少了对话长度2.84轮，同时在单会话基准上保持了一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多会话对话系统中基于语义相似性的记忆选择方法忽视任务意图的问题，导致对话连贯性不足。

**核心思路**：MemGuide框架通过意图对齐检索和缺失槽引导过滤，确保所检索的记忆单元与当前对话意图一致，从而提高对话的连贯性和效率。

**技术框架**：MemGuide分为两个主要阶段：第一阶段是意图对齐检索，通过匹配当前对话上下文与存储的意图描述来检索相关的记忆单元；第二阶段是缺失槽引导过滤，利用链式思维槽推理器枚举未填槽，并使用微调的LLaMA-8B过滤器重新排序检索到的单元。

**关键创新**：MemGuide的创新在于引入了意图驱动的记忆选择机制，显著提高了多会话对话的任务成功率和对话效率，这与传统的基于语义相似性的检索方法有本质区别。

**关键设计**：在缺失槽引导过滤阶段，采用了链式思维槽推理器来识别未填槽，并通过微调的LLaMA-8B模型进行记忆单元的重新排序，以最大化槽填充增益。

## 📊 实验亮点

在MS-TOD基准上，MemGuide将任务成功率从88%提升至99%，同时减少了对话长度2.84轮，显示出其在多会话任务完成中的显著优势。

## 🎯 应用场景

MemGuide的研究成果可广泛应用于智能客服、虚拟助手和其他任务导向的对话系统中，提升用户体验和任务完成效率。未来，随着多会话对话需求的增加，该框架有望在更复杂的对话场景中发挥重要作用。

## 📄 摘要（原文）

> Modern task-oriented dialogue (TOD) systems increasingly rely on large language model (LLM) agents, leveraging Retrieval-Augmented Generation (RAG) and long-context capabilities for long-term memory utilization. However, these methods are primarily based on semantic similarity, overlooking task intent and reducing task coherence in multi-session dialogues. To address this challenge, we introduce MemGuide, a two-stage framework for intent-driven memory selection. (1) Intent-Aligned Retrieval matches the current dialogue context with stored intent descriptions in the memory bank, retrieving QA-formatted memory units that share the same goal. (2) Missing-Slot Guided Filtering employs a chain-of-thought slot reasoner to enumerate unfilled slots, then uses a fine-tuned LLaMA-8B filter to re-rank the retrieved units by marginal slot-completion gain. The resulting memory units inform a proactive strategy that minimizes conversational turns by directly addressing information gaps. Based on this framework, we introduce the MS-TOD, the first multi-session TOD benchmark comprising 132 diverse personas, 956 task goals, and annotated intent-aligned memory targets, supporting efficient multi-session task completion. Evaluations on MS-TOD show that MemGuide raises the task success rate by 11% (88% -> 99%) and reduces dialogue length by 2.84 turns in multi-session settings, while maintaining parity with single-session benchmarks.

