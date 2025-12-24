---
layout: default
title: "Democratizing Diplomacy: A Harness for Evaluating Any Large Language Model on Full-Press Diplomacy"
---

# Democratizing Diplomacy: A Harness for Evaluating Any Large Language Model on Full-Press Diplomacy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07485" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07485v1</a>
  <a href="https://arxiv.org/pdf/2508.07485.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07485v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07485v1', 'Democratizing Diplomacy: A Harness for Evaluating Any Large Language Model on Full-Press Diplomacy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexander Duffy, Samuel J Paech, Ishana Shastri, Elizabeth Karpinski, Baptiste Alloui-Cros, Tyler Marques, Matthew Lyle Olson

**分类**: cs.AI, cs.CL, cs.CY, cs.LG

**发布日期**: 2025-08-10

---

## 💡 一句话要点

**提出评估工具以实现大型语言模型在全压外交中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `全压外交` `评估工具` `战略推理` `数据驱动优化`

## 📋 核心要点

1. 现有方法在处理复杂的外交游戏状态时，通常需要前沿的LLMs或进行微调，限制了研究的广泛性。
2. 本研究提出了一种新的评估工具，允许任何大型语言模型在不进行微调的情况下参与全压外交游戏。
3. 实验结果显示，较大的模型在游戏表现上优于小型模型，但后者仍能保持适当的游戏水平。

## 📝 摘要（中文）

本文首次提出了一种评估工具，使任何现成的本地大型语言模型（LLMs）能够在无需微调或专门训练的情况下进行全压外交游戏。以往的研究因外交游戏状态的复杂性和信息密度，需依赖前沿LLMs或进行微调，限制了研究的可行性。我们通过数据驱动的迭代优化了文本游戏状态表示，使得24B模型能够可靠地完成比赛。此外，我们开发了工具以促进假设测试和统计分析，并展示了在说服、激进游戏风格等方面的案例研究。实验结果表明，较大的模型表现最佳，但较小的模型也能达到一定的游戏水平。我们还引入了关键状态分析，快速迭代和分析游戏中的关键时刻。我们的工具使得战略推理的评估变得更加民主化，并提供了对这些能力如何自然涌现于广泛使用的LLMs的见解。代码将在补充材料中提供并开源。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在全压外交游戏中的评估问题。现有方法因游戏复杂性和信息密度，通常需要微调或依赖特定的前沿模型，限制了研究的可行性。

**核心思路**：我们通过优化文本游戏状态的表示，使得大型语言模型能够在不进行微调的情况下完成游戏。这种设计使得模型能够更好地理解和参与复杂的游戏状态。

**技术框架**：整体架构包括数据驱动的迭代优化过程、文本游戏状态的表示、假设测试工具和统计分析模块。主要阶段涵盖了模型的训练、评估和分析。

**关键创新**：最重要的创新在于提出了无需微调的评估工具，使得任何大型语言模型都能参与复杂的外交游戏。这与以往依赖于特定模型或微调的研究方法有本质区别。

**关键设计**：在参数设置上，我们使用了24B模型，并通过优化文本表示来提高游戏的可玩性。损失函数和网络结构的具体细节未在摘要中详细说明，需参考补充材料。

## 📊 实验亮点

实验结果表明，较大的语言模型在全压外交游戏中的表现优于小型模型，尽管小型模型也能保持适当的游戏水平。具体性能数据和对比基线将在补充材料中提供，展示了模型在复杂决策中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、教育、决策支持系统等。通过提供一种无需微调的评估工具，研究者和开发者可以更方便地测试和分析大型语言模型在复杂场景下的表现，从而推动相关领域的进步。

## 📄 摘要（原文）

> We present the first evaluation harness that enables any out-of-the-box, local, Large Language Models (LLMs) to play full-press Diplomacy without fine-tuning or specialized training. Previous work required frontier LLMs, or fine-tuning, due to the high complexity and information density of Diplomacy's game state. Combined with the high variance of matches, these factors made Diplomacy prohibitive for study. In this work, we used data-driven iteration to optimize a textual game state representation such that a 24B model can reliably complete matches without any fine tuning. We develop tooling to facilitate hypothesis testing and statistical analysis, and we present case studies on persuasion, aggressive playstyles, and performance across a range of models. We conduct a variety of experiments across many popular LLMs, finding the larger models perform the best, but the smaller models still play adequately. We also introduce Critical State Analysis: an experimental protocol for rapidly iterating and analyzing key moments in a game at depth. Our harness democratizes the evaluation of strategic reasoning in LLMs by eliminating the need for fine-tuning, and it provides insights into how these capabilities emerge naturally from widely used LLMs. Our code is available in the supplement and will be open sourced.

