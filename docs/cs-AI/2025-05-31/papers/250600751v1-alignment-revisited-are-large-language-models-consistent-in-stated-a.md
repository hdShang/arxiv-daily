---
layout: default
title: Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?
---

# Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00751" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00751v1</a>
  <a href="https://arxiv.org/pdf/2506.00751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00751v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00751v1', 'Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuojun Gu, Quan Wang, Shuchu Han

**分类**: cs.AI, cs.LG

**发布日期**: 2025-05-31

---

## 💡 一句话要点

**提出偏好一致性测量方法以解决LLM行为与人类价值不一致问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `偏好一致性` `人机交互` `道德AI` `决策透明性`

## 📋 核心要点

1. 核心问题：现有研究未能充分探讨大型语言模型的陈述偏好与揭示偏好之间的差异，影响其可解释性和信任度。
2. 方法要点：本文提出了一种通过设计强制二元选择的提示来测量LLM偏好偏差的方法，并使用KL散度等指标进行量化。
3. 实验或效果：在四种主流LLM上进行的实验表明，提示格式的微小变化会显著改变模型的偏好选择，揭示了决策过程中的不一致性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展突显了其行为与人类价值观对齐的必要性。本文探讨了LLM的陈述偏好（与一般原则的对齐）与揭示偏好（在特定情境中的决策推断）之间的潜在差异。我们正式定义并提出了一种测量这种偏好偏差的方法，分析了LLM在不同上下文中激活不同指导原则的情况。通过设计一系列强制二元选择的提示，比较LLM对一般原则提示的响应与对情境提示的响应，发现提示格式的微小变化会显著影响LLM的偏好选择。这一现象强调了对LLM决策能力的理解和控制的不足。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在陈述偏好与揭示偏好之间可能存在的偏差问题。现有方法未能有效测量和理解这种偏差，导致LLMs在高风险应用中的可解释性和道德性受到质疑。

**核心思路**：论文提出通过设计一系列强制二元选择的提示，来系统性地测量LLMs的偏好偏差。通过比较模型在不同上下文中的响应，揭示其决策过程中的不一致性。

**技术框架**：整体流程包括数据集的构建、提示设计、模型响应收集和偏差量化。首先，构建一个丰富的提示数据集，然后将其应用于多个主流LLMs，最后使用KL散度等指标量化偏差。

**关键创新**：最重要的创新在于系统性地定义和测量偏好偏差，并通过强制二元选择的方式揭示LLMs在不同上下文下的决策变化。这与现有方法的主要区别在于关注偏好的一致性而非单一的输出。

**关键设计**：在提示设计中，采用了多种格式和内容的提示，以确保覆盖不同的偏好类别。实验中使用的度量标准包括KL散度，以量化不同提示下的偏好变化。

## 📊 实验亮点

实验结果显示，提示格式的微小变化能够显著影响LLMs的偏好选择，KL散度的量化结果表明在不同偏好类别中存在明显的偏差。这一发现强调了对LLM决策过程的深入理解和控制的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、自动化决策系统和道德AI等。通过提高对LLMs偏好一致性的理解，可以增强其在高风险场景中的可解释性和信任度，从而促进其在社会责任和伦理应用中的部署。

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) highlight the need to align their behaviors with human values. A critical, yet understudied, issue is the potential divergence between an LLM's stated preferences (its reported alignment with general principles) and its revealed preferences (inferred from decisions in contextualized scenarios). Such deviations raise fundamental concerns for the interpretability, trustworthiness, reasoning transparency, and ethical deployment of LLMs, particularly in high-stakes applications. This work formally defines and proposes a method to measure this preference deviation. We investigate how LLMs may activate different guiding principles in specific contexts, leading to choices that diverge from previously stated general principles. Our approach involves crafting a rich dataset of well-designed prompts as a series of forced binary choices and presenting them to LLMs. We compare LLM responses to general principle prompts stated preference with LLM responses to contextualized prompts revealed preference, using metrics like KL divergence to quantify the deviation. We repeat the analysis across different categories of preferences and on four mainstream LLMs and find that a minor change in prompt format can often pivot the preferred choice regardless of the preference categories and LLMs in the test. This prevalent phenomenon highlights the lack of understanding and control of the LLM decision-making competence. Our study will be crucial for integrating LLMs into services, especially those that interact directly with humans, where morality, fairness, and social responsibilities are crucial dimensions. Furthermore, identifying or being aware of such deviation will be critically important as LLMs are increasingly envisioned for autonomous agentic tasks where continuous human evaluation of all LLMs' intermediary decision-making steps is impossible.

