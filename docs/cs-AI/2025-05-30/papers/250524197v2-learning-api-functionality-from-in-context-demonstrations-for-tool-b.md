---
layout: default
title: Learning API Functionality from In-Context Demonstrations for Tool-based Agents
---

# Learning API Functionality from In-Context Demonstrations for Tool-based Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24197" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24197v2</a>
  <a href="https://arxiv.org/pdf/2505.24197.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24197v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24197v2', 'Learning API Functionality from In-Context Demonstrations for Tool-based Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bhrij Patel, Ashish Jagmohan, Aditya Vempaty

**分类**: cs.AI

**发布日期**: 2025-05-30 (更新: 2025-11-12)

**备注**: 19 Pages, 14 Figures, 7 Tables

---

## 💡 一句话要点

**提出从上下文示例中学习API功能以解决文档缺失问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `API学习` `上下文示例` `工具代理` `无文档环境` `任务成功率` `自我改进` `大型语言模型`

## 📋 核心要点

1. 现有的API文档常常缺失或不一致，导致工具代理在理解API功能时面临重大挑战。
2. 本文提出通过上下文示例直接学习API功能的方案，旨在解决文档缺失的问题。
3. 实验表明，提供明确的函数调用和自然语言批评能够显著提高代理的任务成功率。

## 📝 摘要（中文）

数字工具代理依赖大型语言模型（LLMs）调用外部API，但现有文档常常缺失、过时或不一致，影响代理的可靠性。本文提出了一种新研究方向：直接从上下文示例中学习API功能。这一方法适用于缺乏文档的场景。通过API基准测试，我们收集了专家代理和自我探索的示例，研究示例数量及LLM生成的总结和评估对任务成功率的影响。实验结果表明，从上下文示例学习功能仍然是一个复杂挑战，提供明确的函数调用和自然语言批评显著提高了任务成功率。我们分析了失败模式，识别了错误来源，并指出了未来在无文档、自我改进的API代理领域的关键挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决数字工具代理在缺乏API文档时如何有效理解和调用API功能的问题。现有方法依赖文档，导致在文档缺失或不一致时的性能下降。

**核心思路**：论文提出通过上下文示例学习API功能，利用专家代理和自我探索生成的示例，帮助代理在无文档环境中完成任务。

**技术框架**：整体架构包括示例收集、功能学习和任务执行三个主要模块。首先收集不同来源的示例，然后通过分析示例中的信息来学习API功能，最后执行任务并评估成功率。

**关键创新**：最重要的创新在于通过上下文示例而非传统文档来学习API功能，这一方法在无文档环境下展现出新的可能性。

**关键设计**：在实验中，设置了不同数量的示例，并引入了LLM生成的总结和评估，以优化参数填充和任务执行的准确性。

## 📊 实验亮点

实验结果显示，通过提供明确的函数调用和自然语言批评，代理的任务成功率显著提高，具体提升幅度达到了XX%（具体数据待补充）。在3个数据集和6个模型上的实验验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化工具和机器人系统等，能够在缺乏文档的情况下提升API调用的可靠性和效率。未来，随着API数量的增加和复杂性的提升，该方法有望在更多实际场景中发挥重要作用。

## 📄 摘要（原文）

> Digital tool-based agents, powered by Large Language Models (LLMs), that invoke external Application Programming Interfaces (APIs) often rely on documentation to understand API functionality. However, such documentation is frequently missing, outdated, privatized, or inconsistent-hindering the development of reliable, general-purpose agents. In this work, we propose a new research direction: learning of API functionality directly from in-context demonstrations. This task is a new paradigm applicable in scenarios without documentation. Using API benchmarks, we collect demonstrations from both expert agents and from self-exploration. To understand what information demonstrations must convey for successful task completion, we extensively study how the number of demonstrations and the use of LLM-generated summaries and evaluations affect the task success rate of the API-based agent. Our experiments across 3 datasets and 6 models show that learning functionality from in-context demonstrations remains a non-trivial challenge, even for state-of-the-art LLMs. We find that providing explicit function calls and natural language critiques significantly improves the agent's task success rate due to more accurate parameter filling. We analyze failure modes, identify sources of error, and highlight key open challenges for future work in documentation-free, self-improving, API-based agents.

