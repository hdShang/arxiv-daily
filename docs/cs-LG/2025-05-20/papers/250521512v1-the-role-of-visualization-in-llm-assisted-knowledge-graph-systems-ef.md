---
layout: default
title: "The Role of Visualization in LLM-Assisted Knowledge Graph Systems: Effects on User Trust, Exploration, and Workflows"
---

# The Role of Visualization in LLM-Assisted Knowledge Graph Systems: Effects on User Trust, Exploration, and Workflows

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21512" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21512v1</a>
  <a href="https://arxiv.org/pdf/2505.21512.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21512v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21512v1', 'The Role of Visualization in LLM-Assisted Knowledge Graph Systems: Effects on User Trust, Exploration, and Workflows')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harry Li, Gabriel Appleby, Kenneth Alperin, Steven R Gomez, Ashley Suh

**分类**: cs.LG, cs.HC

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出LinkQ以解决知识图谱探索中的用户信任问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `大型语言模型` `用户信任` `可视化设计` `数据分析工具` `探索策略` `决策支持`

## 📋 核心要点

1. 现有知识图谱探索工具难以有效支持用户，尤其是专家用户，导致信任和决策问题。
2. 本文提出LinkQ系统，通过LLM将自然语言问题转化为结构化查询，并设计多种可视化机制以增强用户理解。
3. 定性评估结果显示，用户对LinkQ的输出存在过度信任现象，且用户的工作流程因对KG和LLM的熟悉程度而异。

## 📝 摘要（中文）

知识图谱（KG）是一种强大的数据结构，但即使是专家用户在有效探索时仍面临困难。大型语言模型（LLM）越来越多地被用于解决这一问题，但关于其与KG结合使用对用户信任、探索策略和决策的影响的实证研究仍然较少。为此，本文开发了LinkQ，一个将自然语言问题转换为结构化查询的KG探索系统，并设计了五种可视化机制以帮助用户评估KG查询和LLM响应的准确性。通过与14名从业者的定性评估，发现用户倾向于过度信任LinkQ的输出，尽管LLM的结果可能不正确。这一发现突显了在LLM辅助的数据分析工具中虚假信任的风险，并强调了可视化作为缓解技术的进一步研究需求。

## 🔬 方法详解

**问题定义**：本文旨在解决用户在探索知识图谱时对LLM输出的信任问题。现有方法缺乏有效的可视化支持，导致用户在使用LLM辅助工具时可能产生虚假信任。

**核心思路**：LinkQ系统通过将自然语言问题转化为结构化查询，结合多种可视化机制，帮助用户更好地理解和评估查询结果，从而提升用户的信任度和决策能力。

**技术框架**：LinkQ的整体架构包括五个主要模块：LLM-KG状态图、查询编辑器、实体-关系ID表、查询结构图和交互式图形可视化。这些模块共同构成了一个完整的探索管道，支持用户在不同阶段的需求。

**关键创新**：LinkQ的最大创新在于其多层次的可视化设计，能够实时展示用户的查询状态和结果，显著提升用户对KG的理解和信任。这与传统的KG探索工具形成鲜明对比，后者通常缺乏动态反馈机制。

**关键设计**：在设计中，LinkQ采用了用户友好的界面，确保可视化信息的清晰传达。同时，查询编辑器与LLM解释的结合，增强了用户对生成查询的理解，降低了误解的风险。

## 📊 实验亮点

在与14名从业者的定性评估中，发现用户对LinkQ的输出表现出过度信任，尽管LLM的结果可能不准确。这一现象挑战了现有的设计假设，表明用户的信任程度与其对KG和LLM的熟悉程度密切相关，强调了可视化在数据分析中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括数据分析、知识管理和智能问答系统等。通过提升用户对知识图谱的理解和信任，LinkQ可以帮助企业和研究机构更有效地利用数据资源，促进决策过程的优化。未来，随着LLM和KG技术的不断发展，LinkQ的设计理念和方法可以扩展到更多领域，推动智能数据分析的进步。

## 📄 摘要（原文）

> Knowledge graphs (KGs) are powerful data structures, but exploring them effectively remains difficult for even expert users. Large language models (LLMs) are increasingly used to address this gap, yet little is known empirically about how their usage with KGs shapes user trust, exploration strategies, or downstream decision-making - raising key design challenges for LLM-based KG visual analysis systems. To study these effects, we developed LinkQ, a KG exploration system that converts natural language questions into structured queries with an LLM. We collaborated with KG experts to design five visual mechanisms that help users assess the accuracy of both KG queries and LLM responses: an LLM-KG state diagram that illustrates which stage of the exploration pipeline LinkQ is in, a query editor displaying the generated query paired with an LLM explanation, an entity-relation ID table showing extracted KG entities and relations with semantic descriptions, a query structure graph that depicts the path traversed in the KG, and an interactive graph visualization of query results. From a qualitative evaluation with 14 practitioners, we found that users - even KG experts - tended to overtrust LinkQ's outputs due to its "helpful" visualizations, even when the LLM was incorrect. Users exhibited distinct workflows depending on their prior familiarity with KGs and LLMs, challenging the assumption that these systems are one-size-fits-all - despite often being designed as if they are. Our findings highlight the risks of false trust in LLM-assisted data analysis tools and the need for further investigation into the role of visualization as a mitigation technique.

