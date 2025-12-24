---
layout: default
title: "Cognitive Decision Routing in Large Language Models: When to Think Fast, When to Think Slow"
---

# Cognitive Decision Routing in Large Language Models: When to Think Fast, When to Think Slow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16636" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16636v1</a>
  <a href="https://arxiv.org/pdf/2508.16636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16636v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16636v1', 'Cognitive Decision Routing in Large Language Models: When to Think Fast, When to Think Slow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Y. Du, C. Guo, W. Wang, G. Tang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-17

**备注**: 6 pages

---

## 💡 一句话要点

**提出认知决策路由框架以优化大语言模型的推理策略**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `认知决策` `大语言模型` `推理策略` `计算效率` `专业判断` `元认知层` `查询复杂性`

## 📋 核心要点

1. 现有的大语言模型在推理时缺乏灵活性，无法有效区分何时使用快速反应与深度推理。
2. 提出的认知决策路由框架通过分析查询特征，动态选择推理策略，提升了推理效率。
3. 实验结果显示，CDR在多项任务中性能优越，计算成本降低34%，专业判断任务一致性提高23%。

## 📝 摘要（中文）

大语言模型（LLMs）面临一个基本挑战，即在快速直觉反应与缓慢深思熟虑的推理之间做出选择。受丹尼尔·卡尼曼的双重过程理论启发，我们提出了一种新颖的认知决策路由（CDR）框架，动态确定基于查询特征的适当推理策略。该方法解决了现有模型在所有查询中应用统一推理深度或依赖计算成本高昂的方法的局限性。通过对查询复杂性进行多维度分析，我们的框架在多种推理任务上表现出色，相较于统一深度推理方法，计算成本降低了34%。在专业判断任务中，CDR在一致性和准确性上分别提高了23%和18%。该研究将认知科学原理与实际AI系统设计相结合，为LLMs中的自适应推理提供了原则性的方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型在推理时无法灵活选择快速与深度推理策略的问题。现有方法通常采用统一的推理深度，导致效率低下和计算成本高昂。

**核心思路**：论文提出的认知决策路由（CDR）框架，通过分析查询的复杂性，动态选择适当的推理策略。这种设计灵感来源于人类的认知偏差理论，旨在提高模型的推理效率和准确性。

**技术框架**：CDR框架包括多个模块：首先是元认知层，用于分析查询的复杂性；其次是推理策略选择模块，根据分析结果选择快速或深度推理；最后是推理执行模块，执行选定的推理策略。

**关键创新**：CDR的核心创新在于引入了多维度的查询复杂性分析，能够根据不同的查询特征灵活调整推理策略。这与现有方法的统一推理深度形成了本质区别。

**关键设计**：在关键设计上，CDR框架考虑了多个参数设置，包括信息与结论的相关性强度、领域边界的跨越、利益相关者的多样性和不确定性水平等。这些设计使得模型能够更精准地判断何时使用快速反应或深度推理。

## 📊 实验亮点

实验结果表明，CDR框架在多种推理任务中表现优异，计算成本降低了34%。在专业判断任务中，一致性提高了23%，准确性提升了18%。这些结果显示了CDR在实际应用中的潜力和优势。

## 🎯 应用场景

该研究的潜在应用领域包括法律、医疗和金融等需要专业判断的场景。通过优化推理策略，CDR框架能够提高决策的效率和准确性，具有重要的实际价值和广泛的应用前景。未来，随着大语言模型的不断发展，CDR框架可能会在更多领域得到应用，推动智能系统的进步。

## 📄 摘要（原文）

> Large Language Models (LLMs) face a fundamental challenge in deciding when to rely on rapid, intuitive responses versus engaging in slower, more deliberate reasoning. Inspired by Daniel Kahneman's dual-process theory and his insights on human cognitive biases, we propose a novel Cognitive Decision Routing (CDR) framework that dynamically determines the appropriate reasoning strategy based on query characteristics. Our approach addresses the current limitations where models either apply uniform reasoning depth or rely on computationally expensive methods for all queries. We introduce a meta-cognitive layer that analyzes query complexity through multiple dimensions: correlation strength between given information and required conclusions, domain boundary crossings, stakeholder multiplicity, and uncertainty levels. Through extensive experiments on diverse reasoning tasks, we demonstrate that CDR achieves superior performance while reducing computational costs by 34\% compared to uniform deep reasoning approaches. Our framework shows particular strength in professional judgment tasks, achieving 23\% improvement in consistency and 18\% better accuracy on expert-level evaluations. This work bridges cognitive science principles with practical AI system design, offering a principled approach to adaptive reasoning in LLMs.

