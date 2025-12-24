---
layout: default
title: "Prospect Theory Fails for LLMs: Revealing Instability of Decision-Making under Epistemic Uncertainty"
---

# Prospect Theory Fails for LLMs: Revealing Instability of Decision-Making under Epistemic Uncertainty

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08992" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08992v1</a>
  <a href="https://arxiv.org/pdf/2508.08992.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08992v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08992v1', 'Prospect Theory Fails for LLMs: Revealing Instability of Decision-Making under Epistemic Uncertainty')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Wang, Qihan Lin, Jiayu Liu, Qing Zong, Tianshi Zheng, Weiqi Wang, Yangqiu Song

**分类**: cs.AI

**发布日期**: 2025-08-12

**🔗 代码/项目**: [GITHUB](https://github.com/HKUST-KnowComp/MarPT)

---

## 💡 一句话要点

**提出新的评估框架以揭示LLMs在不确定性下的决策不稳定性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `前景理论` `大型语言模型` `不确定性` `决策行为` `语言标记` `经济问卷` `评估框架`

## 📋 核心要点

1. 现有的前景理论在解释大型语言模型（LLMs）决策行为时存在不一致性，尤其是在不确定性表达方面。
2. 本文提出了一种新的评估框架，结合经验概率值和语言标记，系统性地分析LLMs的决策行为。
3. 实验结果表明，LLMs在面对不同语言形式的不确定性时，其决策表现出显著的不稳定性，挑战了前景理论的适用性。

## 📝 摘要（中文）

前景理论（PT）用于建模人类在不确定性下的决策，而表述不确定性的语言标记（如“也许”）在此过程中扮演重要角色。然而，前景理论是否适用于当代大型语言模型（LLMs）以及这些语言标记对其决策行为的影响尚未得到充分探索。为此，本文设计了一个基于经济问卷的三阶段实验，提出了一种更为通用和精确的评估框架，以模型化LLMs在前景理论下的决策行为。通过引入与常用语言标记相关的经验概率值，本文考察了这些标记对LLM决策行为的影响。研究结果表明，使用前景理论模型化LLMs的决策并不总是可靠，尤其是在不确定性以多样化语言形式表达时。

## 🔬 方法详解

**问题定义**：本文旨在探讨前景理论是否适用于大型语言模型（LLMs），并分析语言中的不确定性标记如何影响其决策行为。现有方法未能充分考虑这些因素，导致对LLMs决策的理解不足。

**核心思路**：通过设计一个三阶段实验，结合经济问卷和语言标记的经验概率值，构建一个更为精确的评估框架，以系统性地分析LLMs在不确定性下的决策行为。

**技术框架**：整体流程包括三个阶段：首先，设计经济问卷以收集数据；其次，构建评估框架，将语言标记的概率值纳入决策模型；最后，分析不同标记对LLMs决策的影响。

**关键创新**：本文的主要创新在于引入语言标记的经验概率值，提供了一种新的视角来理解LLMs在不确定性下的决策行为，这与传统的前景理论模型存在本质区别。

**关键设计**：在评估框架中，关键参数包括语言标记的选择及其对应的概率值，损失函数设计为能够反映决策的不确定性，确保模型能够有效捕捉LLMs的决策特征。

## 📊 实验亮点

实验结果显示，LLMs在面对不同语言形式的不确定性时，其决策表现出显著的不稳定性，尤其是在使用前景理论进行建模时，可靠性不足。这一发现为理解LLMs的决策机制提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能决策系统和人机交互等。通过深入理解LLMs在不确定性下的决策行为，可以提升其在实际应用中的可靠性和有效性，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Prospect Theory (PT) models human decision-making under uncertainty, while epistemic markers (e.g., maybe) serve to express uncertainty in language. However, it remains largely unexplored whether Prospect Theory applies to contemporary Large Language Models and whether epistemic markers, which express human uncertainty, affect their decision-making behaviour. To address these research gaps, we design a three-stage experiment based on economic questionnaires. We propose a more general and precise evaluation framework to model LLMs' decision-making behaviour under PT, introducing uncertainty through the empirical probability values associated with commonly used epistemic markers in comparable contexts. We then incorporate epistemic markers into the evaluation framework based on their corresponding probability values to examine their influence on LLM decision-making behaviours. Our findings suggest that modelling LLMs' decision-making with PT is not consistently reliable, particularly when uncertainty is expressed in diverse linguistic forms. Our code is released in https://github.com/HKUST-KnowComp/MarPT.

