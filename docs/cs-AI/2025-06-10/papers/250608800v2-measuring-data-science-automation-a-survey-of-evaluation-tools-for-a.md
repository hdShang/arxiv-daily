---
layout: default
title: "Measuring Data Science Automation: A Survey of Evaluation Tools for AI Assistants and Agents"
---

# Measuring Data Science Automation: A Survey of Evaluation Tools for AI Assistants and Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08800" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08800v2</a>
  <a href="https://arxiv.org/pdf/2506.08800.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08800v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08800v2', 'Measuring Data Science Automation: A Survey of Evaluation Tools for AI Assistants and Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Irene Testini, José Hernández-Orallo, Lorenzo Pacchiardi

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-10 (更新: 2025-10-22)

**备注**: Published in Transactions of Machine Learning Research (TMLR), 10/2025 https://openreview.net/forum?id=MB0TCLfLn1

---

## 💡 一句话要点

**调查评估工具以提升数据科学自动化的有效性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据科学` `自动化` `大型语言模型` `人机协作` `评估工具` `人工智能助手` `任务转变`

## 📋 核心要点

1. 现有方法主要集中在少数目标导向活动，忽视了数据管理和探索性活动的评估。
2. 论文通过调查现有评估工具，提出了对LLM助手和代理的全面评估框架，强调人机协作的重要性。
3. 研究发现当前评估工具在自动化水平上存在不足，建议关注任务转变以实现更高的自动化潜力。

## 📝 摘要（中文）

数据科学旨在从数据中提取洞察以支持决策过程。近年来，大型语言模型（LLMs）作为数据科学助手的使用日益增加，能够建议思路、技术和小代码片段，或进行结果解释和报告。随着LLM代理的兴起，某些数据科学活动的自动化得到了良好的前景。本文对数据科学中LLM助手和代理的评估进行了调查，发现（1）主要集中在少数目标导向活动上，忽视了数据管理和探索性活动；（2）关注纯粹的辅助或完全自主代理，而未考虑人机协作的中间层次；（3）强调人类替代，忽视了通过任务转变实现更高自动化水平的可能性。

## 🔬 方法详解

**问题定义**：本文旨在解决当前数据科学领域中对LLM助手和代理的评估工具不足的问题。现有方法主要集中在特定活动上，缺乏对数据管理和探索性活动的全面考虑。

**核心思路**：论文提出了一种全面的评估框架，强调人机协作的中间层次，并探讨任务转变如何提升自动化水平。这样的设计旨在填补现有评估工具的空白，促进更高效的自动化实践。

**技术框架**：整体架构包括对现有评估工具的分类、分析和比较，主要模块包括目标导向活动评估、数据管理活动评估和人机协作评估。

**关键创新**：最重要的创新点在于提出了一个综合评估框架，强调了人机协作的多层次性，与现有方法相比，提供了更全面的视角。

**关键设计**：在评估过程中，论文设定了多个关键参数，包括活动类型、自动化水平和人机协作程度，以确保评估的全面性和准确性。

## 📊 实验亮点

研究发现，现有评估工具主要集中在目标导向活动，忽视了数据管理和探索性活动的评估。通过提出新的评估框架，强调人机协作的中间层次，研究为实现更高的自动化水平提供了新的视角和方法。

## 🎯 应用场景

该研究的潜在应用领域包括数据科学、人工智能助手和自动化决策支持系统。通过提供一个全面的评估框架，研究可以帮助开发更高效的AI助手，提升数据科学工作流程的自动化水平，最终推动决策过程的优化。

## 📄 摘要（原文）

> Data science aims to extract insights from data to support decision-making processes. Recently, Large Language Models (LLMs) have been increasingly used as assistants for data science, by suggesting ideas, techniques and small code snippets, or for the interpretation of results and reporting. Proper automation of some data-science activities is now promised by the rise of LLM agents, i.e., AI systems powered by an LLM equipped with additional affordances--such as code execution and knowledge bases--that can perform self-directed actions and interact with digital environments. In this paper, we survey the evaluation of LLM assistants and agents for data science. We find (1) a dominant focus on a small subset of goal-oriented activities, largely ignoring data management and exploratory activities; (2) a concentration on pure assistance or fully autonomous agents, without considering intermediate levels of human-AI collaboration; and (3) an emphasis on human substitution, therefore neglecting the possibility of higher levels of automation thanks to task transformation.

