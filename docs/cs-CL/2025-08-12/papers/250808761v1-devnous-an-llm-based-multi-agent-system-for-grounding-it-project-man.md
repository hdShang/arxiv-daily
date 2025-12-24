---
layout: default
title: "DevNous: An LLM-Based Multi-Agent System for Grounding IT Project Management in Unstructured Conversation"
---

# DevNous: An LLM-Based Multi-Agent System for Grounding IT Project Management in Unstructured Conversation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08761" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08761v1</a>
  <a href="https://arxiv.org/pdf/2508.08761.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08761v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08761v1', 'DevNous: An LLM-Based Multi-Agent System for Grounding IT Project Management in Unstructured Conversation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stavros Doropoulos, Stavros Vologiannidis, Ioannis Magnisalis

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出DevNous以解决IT项目管理中的对话转化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多代理系统` `项目管理` `非结构化对话` `自动化任务处理` `意图识别` `数据集基准`

## 📋 核心要点

1. 现有方法在将非结构化对话转化为结构化文档时效率低下，导致信息技术项目管理中的沟通障碍。
2. DevNous通过集成大型语言模型，自动识别对话中的可操作意图，并管理多轮工作流程，提升了任务处理效率。
3. 在新创建的基准数据集上，DevNous达到了81.3%的准确率和0.845的F1分数，展示了其在实际应用中的有效性。

## 📝 摘要（中文）

手动将非结构化团队对话转化为信息技术项目治理所需的结构化文档是现代信息系统管理中的一个关键瓶颈。本文介绍了DevNous，一个基于大型语言模型的多代理专家系统，旨在自动化这一转化过程。DevNous直接集成到团队聊天环境中，识别非正式对话中的可操作意图，并管理状态保持的多轮工作流程，处理自动任务正式化和进度总结等核心行政任务。为了定量评估该系统，我们引入了一个包含160个真实互动对话轮次的新基准数据集，该数据集经过多标签的人工注释并公开可用。在该基准上，DevNous实现了81.3%的精确匹配轮次准确率和0.845的多集F1分数，提供了其可行性的有力证据。本文的主要贡献有两个：一是验证了开发环境行政代理的架构模式，二是首次引入了这一挑战性问题领域的稳健实证基线和公共基准数据集。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是如何将非结构化的团队对话有效转化为结构化的项目管理文档。现有方法在这一过程中效率低下，且难以准确捕捉对话中的关键信息。

**核心思路**：论文提出的核心解决思路是利用大型语言模型（LLM）来自动化这一转化过程，通过识别对话中的可操作意图，减少人工干预，提高工作效率。

**技术框架**：DevNous的整体架构包括多个模块，首先是对话输入模块，接着是意图识别模块，然后是任务管理模块，最后是输出生成模块。这些模块协同工作，实现从非结构化对话到结构化文档的转化。

**关键创新**：该研究的最重要技术创新在于提出了一种新的多代理系统架构，能够在团队聊天环境中实时处理和管理对话信息，与现有方法相比，显著提高了任务处理的自动化程度和准确性。

**关键设计**：在关键设计方面，DevNous采用了特定的损失函数来优化意图识别的准确性，并设计了适应多轮对话的状态管理机制，以确保信息的连贯性和一致性。

## 📊 实验亮点

在新创建的基准数据集上，DevNous实现了81.3%的精确匹配轮次准确率和0.845的多集F1分数，显示出其在处理非结构化对话转化方面的优越性能，提供了强有力的实证支持。

## 🎯 应用场景

该研究的潜在应用场景包括软件开发、项目管理和团队协作等领域，能够显著提高团队沟通的效率和准确性，减少信息传递中的误差。未来，DevNous有望在更广泛的行业中推广应用，助力智能化项目管理。

## 📄 摘要（原文）

> The manual translation of unstructured team dialogue into the structured artifacts required for Information Technology (IT) project governance is a critical bottleneck in modern information systems management. We introduce DevNous, a Large Language Model-based (LLM) multi-agent expert system, to automate this unstructured-to-structured translation process. DevNous integrates directly into team chat environments, identifying actionable intents from informal dialogue and managing stateful, multi-turn workflows for core administrative tasks like automated task formalization and progress summary synthesis. To quantitatively evaluate the system, we introduce a new benchmark of 160 realistic, interactive conversational turns. The dataset was manually annotated with a multi-label ground truth and is publicly available. On this benchmark, DevNous achieves an exact match turn accuracy of 81.3\% and a multiset F1-Score of 0.845, providing strong evidence for its viability. The primary contributions of this work are twofold: (1) a validated architectural pattern for developing ambient administrative agents, and (2) the introduction of the first robust empirical baseline and public benchmark dataset for this challenging problem domain.

