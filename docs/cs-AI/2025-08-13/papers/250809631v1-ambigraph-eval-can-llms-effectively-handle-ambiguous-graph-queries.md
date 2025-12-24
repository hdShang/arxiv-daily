---
layout: default
title: "AmbiGraph-Eval: Can LLMs Effectively Handle Ambiguous Graph Queries?"
---

# AmbiGraph-Eval: Can LLMs Effectively Handle Ambiguous Graph Queries?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09631" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09631v1</a>
  <a href="https://arxiv.org/pdf/2508.09631.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09631v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09631v1', 'AmbiGraph-Eval: Can LLMs Effectively Handle Ambiguous Graph Queries?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchen Tian, Kaixin Li, Hao Chen, Ziyang Luo, Hongzhan Lin, Sebastian Schelter, Lun Du, Jing Ma

**分类**: cs.DB, cs.AI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出AmbiGraph-Eval以评估LLMs处理模糊图查询的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `图查询` `模糊性处理` `数据库查询` `自然语言处理` `评估基准` `机器学习` `信息检索`

## 📋 核心要点

1. 现有大型语言模型在处理模糊图查询时存在显著的性能不足，导致查询结果不准确。
2. 本文提出了AmbiGraph-Eval基准，系统性地评估LLMs在处理模糊图查询的能力，提供了分类法和真实查询数据。
3. 实验结果显示，9个代表性LLMs在模糊图查询上的表现普遍不佳，揭示了当前技术的局限性和未来研究的方向。

## 📝 摘要（中文）

大型语言模型（LLMs）在将自然语言翻译为数据库查询方面表现出色，尤其是在处理复杂的图结构数据时。然而，现实世界中的查询往往包含固有的模糊性，图结构的互联特性可能加剧这些挑战，导致意外或错误的查询结果。为系统性评估LLMs在这一领域的表现，本文提出了一种图查询模糊性的分类法，包括属性模糊性、关系模糊性和属性-关系模糊性三种主要类型，并细分为同实体和跨实体场景。我们引入了AmbiGraph-Eval，一个包含真实世界模糊查询及专家验证的图查询答案的新基准。对9个代表性LLMs的评估显示，即使是顶尖模型在处理模糊图查询时也面临困难。我们的研究揭示了模糊性处理中的关键差距，并激励未来在专门的解决技术上进行深入研究。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理模糊图查询时的不足，尤其是由于图结构的复杂性和查询的模糊性导致的错误结果。现有方法未能有效应对这些模糊性，影响了查询的准确性和可靠性。

**核心思路**：论文提出了一种新的分类法，将图查询的模糊性分为三种主要类型，并引入AmbiGraph-Eval基准，以系统性地评估LLMs在处理这些模糊查询时的能力。通过提供专家验证的查询答案，增强了评估的可靠性。

**技术框架**：整体架构包括模糊查询的分类、基准数据集的构建和对9个LLMs的评估。首先，定义模糊性类型，然后收集和验证真实查询数据，最后进行模型评估和结果分析。

**关键创新**：最重要的技术创新点在于提出了图查询模糊性的系统分类法，并构建了AmbiGraph-Eval基准，使得对LLMs的评估更加全面和系统。这一方法与现有的单一评估标准有本质区别。

**关键设计**：在设计中，采用了专家验证的查询答案，以确保数据的准确性和可靠性。同时，针对不同模糊性类型的查询，设计了相应的评估指标，以全面反映模型的处理能力。实验中使用了多种LLMs进行对比，确保结果的有效性。

## 📊 实验亮点

实验结果表明，9个代表性LLMs在处理模糊图查询时的表现普遍不佳，尤其是在属性模糊性和关系模糊性方面，准确率低于预期。这一发现揭示了当前技术在模糊性处理上的关键差距，强调了未来研究的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、数据库查询优化和信息检索等。通过提升LLMs对模糊查询的处理能力，可以显著提高用户体验和系统的准确性，未来可能推动更智能的图数据库应用和自然语言处理技术的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have recently demonstrated strong capabilities in translating natural language into database queries, especially when dealing with complex graph-structured data. However, real-world queries often contain inherent ambiguities, and the interconnected nature of graph structures can amplify these challenges, leading to unintended or incorrect query results. To systematically evaluate LLMs on this front, we propose a taxonomy of graph-query ambiguities, comprising three primary types: Attribute Ambiguity, Relationship Ambiguity, and Attribute-Relationship Ambiguity, each subdivided into Same-Entity and Cross-Entity scenarios. We introduce AmbiGraph-Eval, a novel benchmark of real-world ambiguous queries paired with expert-verified graph query answers. Evaluating 9 representative LLMs shows that even top models struggle with ambiguous graph queries. Our findings reveal a critical gap in ambiguity handling and motivate future work on specialized resolution techniques.

