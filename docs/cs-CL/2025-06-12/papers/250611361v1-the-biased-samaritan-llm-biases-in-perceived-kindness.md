---
layout: default
title: "The Biased Samaritan: LLM biases in Perceived Kindness"
---

# The Biased Samaritan: LLM biases in Perceived Kindness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11361" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11361v1</a>
  <a href="https://arxiv.org/pdf/2506.11361.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11361v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11361v1', 'The Biased Samaritan: LLM biases in Perceived Kindness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jack H Fagan, Ruhaan Juyaal, Amy Yue-Ming Yu, Siya Pun

**分类**: cs.CL, cs.CY

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出一种新方法评估大型语言模型的偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `偏见评估` `道德评估` `生成AI` `社会科学` `AI伦理` `人机交互`

## 📋 核心要点

1. 现有方法在评估大型语言模型的偏见时缺乏定量分析，难以明确不同人口特征的影响。
2. 本文通过设计特定的道德评估任务，提出了一种定量评估LLM偏见的新方法，关注不同性别、种族和年龄的表现差异。
3. 研究结果表明，模型普遍将基线人口视为白人男性，而非基线人口在干预意愿上更为积极，揭示了偏见的复杂性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在多个领域的广泛应用，理解和缓解其偏见问题仍然是一个持续的挑战。本文提出了一种新颖的方法，通过提示模型评估道德患者的干预意愿，定量评估不同生成AI模型在性别、种族和年龄等方面的偏见。与现有研究不同，我们旨在确定各种商业模型的基线人口特征及其与其他人口特征之间的关系。我们的分析表明，模型普遍将基线人口视为白人中年或年轻男性，但非基线人口在帮助意愿上普遍高于基线人口。这项研究为大型语言模型的偏见客观评估提供了基础，帮助用户或开发者在LLM输出或未来模型训练中考虑这些偏见。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在性别、种族和年龄等方面的偏见评估问题。现有方法往往缺乏对偏见的定量分析，无法有效识别和理解不同人口特征的影响。

**核心思路**：我们通过设计道德评估任务，提示模型评估道德患者的干预意愿，从而定量分析不同LLMs在各人口特征上的偏见。这种方法使得偏见的评估更加系统和客观。

**技术框架**：研究流程包括数据收集、模型选择、道德评估任务设计和结果分析。主要模块包括模型的基线人口特征识别和非基线人口特征的比较分析。

**关键创新**：本研究的创新点在于首次系统性地评估LLMs的偏见，明确区分基线人口与非基线人口的干预意愿，揭示了偏见的复杂性和多样性。

**关键设计**：在实验中，我们设计了特定的道德评估任务，采用了多种生成AI模型，并通过定量指标来评估模型的偏见程度，确保了实验的可重复性和可靠性。

## 📊 实验亮点

实验结果显示，模型普遍将基线人口视为白人中年男性，而非基线人口在干预意愿上表现出更高的积极性。这一发现揭示了LLMs在处理不同人口特征时的偏见程度，为未来的研究和应用提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括AI伦理、社会科学研究和人机交互设计。通过理解和评估LLMs的偏见，开发者可以在模型训练和应用中更好地考虑这些偏见，从而提高AI系统的公平性和透明度。

## 📄 摘要（原文）

> While Large Language Models (LLMs) have become ubiquitous in many fields, understanding and mitigating LLM biases is an ongoing issue. This paper provides a novel method for evaluating the demographic biases of various generative AI models. By prompting models to assess a moral patient's willingness to intervene constructively, we aim to quantitatively evaluate different LLMs' biases towards various genders, races, and ages. Our work differs from existing work by aiming to determine the baseline demographic identities for various commercial models and the relationship between the baseline and other demographics. We strive to understand if these biases are positive, neutral, or negative, and the strength of these biases. This paper can contribute to the objective assessment of bias in Large Language Models and give the user or developer the power to account for these biases in LLM output or in training future LLMs. Our analysis suggested two key findings: that models view the baseline demographic as a white middle-aged or young adult male; however, a general trend across models suggested that non-baseline demographics are more willing to help than the baseline. These methodologies allowed us to distinguish these two biases that are often tangled together.

