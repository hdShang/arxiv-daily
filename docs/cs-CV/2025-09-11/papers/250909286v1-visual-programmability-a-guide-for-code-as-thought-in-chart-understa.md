---
layout: default
title: "Visual Programmability: A Guide for Code-as-Thought in Chart Understanding"
---

# Visual Programmability: A Guide for Code-as-Thought in Chart Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09286" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09286v1</a>
  <a href="https://arxiv.org/pdf/2509.09286.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09286v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09286v1', 'Visual Programmability: A Guide for Code-as-Thought in Chart Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bohao Tang, Yan Ma, Fei Zhang, Jiadi Su, Ethan Chern, Zhulin Hu, Zhixin Wang, Pengfei Liu, Ya Zhang

**分类**: cs.CV

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**提出Visual Programmability，自适应选择代码推理或视觉推理解决图表理解任务。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图表理解` `视觉-语言模型` `代码即思维` `自适应推理` `强化学习`

## 📋 核心要点

1. 现有图表理解方法依赖外部工具或单一推理策略，缺乏灵活性和可验证性，限制了模型性能。
2. 提出Visual Programmability，使模型能够自适应地选择代码推理（CaT）或直接视觉推理，提升处理复杂图表的能力。
3. 通过双重奖励强化学习训练模型，在多个图表理解基准测试中取得了显著提升，验证了方法的有效性。

## 📝 摘要（中文）

图表理解是视觉-语言模型（VLMs）推理能力的关键测试。现有方法存在局限：一些依赖外部工具，受限于预定义工具集；另一些微调专门模型，采用单一推理策略，如基于文本的思维链（CoT）。文本推理的中间步骤难以验证，阻碍了使用强化学习信号奖励事实准确性。为此，我们提出代码即思维（CaT）方法，以可验证的符号格式表示图表的视觉信息。关键在于这种策略必须是自适应的：固定的纯代码实现始终无法处理复杂的图表，因为符号表示不总是适用。因此，我们引入Visual Programmability：一种可学习的属性，决定图表-问题对更适合用代码还是直接视觉分析解决。我们在一个自适应框架中实现这一概念，VLM学习在CaT路径和直接视觉推理路径之间选择。模型的选择策略通过强化学习训练，使用一种新颖的双重奖励系统。该系统结合了数据准确性奖励，使模型基于事实并防止数值幻觉，以及决策奖励，指导模型何时使用每种策略，防止其默认使用单一推理模式。实验表明，该方法在各种图表理解基准测试中表现出强大而稳健的性能。我们的工作表明，可以教导VLM不仅进行推理，还包括如何推理，动态地为每个任务选择最佳推理路径。

## 🔬 方法详解

**问题定义**：现有图表理解方法主要面临两个问题：一是依赖外部工具，导致系统脆弱且受限于预定义的工具集；二是微调的专门模型通常采用单一的推理策略，例如基于文本的思维链（CoT），缺乏灵活性。此外，基于文本的推理过程难以验证，阻碍了利用强化学习信号来提升事实准确性。

**核心思路**：论文的核心思路是引入“Visual Programmability”，即让模型能够根据图表和问题的特点，自适应地选择合适的推理路径。具体来说，模型可以选择将图表信息转化为可验证的符号代码（CaT），或者直接进行视觉推理。这种自适应选择能力使得模型能够更好地处理各种复杂度的图表，并提高推理的准确性和鲁棒性。

**技术框架**：整体框架包含两个主要路径：代码即思维（CaT）路径和直接视觉推理路径。模型首先判断当前图表-问题对更适合哪种路径。然后，如果选择CaT路径，则将图表信息转化为符号代码，并基于代码进行推理；如果选择直接视觉推理路径，则直接利用视觉信息进行推理。最终，模型输出答案。选择策略通过强化学习进行训练。

**关键创新**：最重要的创新点在于“Visual Programmability”的概念，即模型能够学习并动态选择最适合当前任务的推理路径。与现有方法中固定使用单一推理策略不同，该方法能够根据图表和问题的特点进行自适应调整，从而提高模型的泛化能力和鲁棒性。

**关键设计**：论文设计了一个双重奖励系统来训练模型的选择策略。数据准确性奖励用于鼓励模型生成准确的答案，防止数值幻觉。决策奖励用于指导模型何时使用CaT路径，何时使用直接视觉推理路径，避免模型倾向于使用单一路径。具体参数设置和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在多个图表理解基准测试中取得了显著的性能提升。具体的性能数据和对比基线在论文中未明确给出，属于未知信息。但论文强调，该方法在各种图表理解基准测试中表现出强大而稳健的性能，证明了Visual Programmability的有效性。

## 🎯 应用场景

该研究成果可应用于智能报表分析、数据可视化辅助、教育领域等。例如，可以帮助用户自动理解和分析各种图表数据，提取关键信息，辅助决策。未来，该技术有望扩展到更广泛的视觉-语言任务中，例如文档理解、信息抽取等，提升人工智能系统的理解和推理能力。

## 📄 摘要（原文）

> Chart understanding presents a critical test to the reasoning capabilities of Vision-Language Models (VLMs). Prior approaches face critical limitations: some rely on external tools, making them brittle and constrained by a predefined toolkit, while others fine-tune specialist models that often adopt a single reasoning strategy, such as text-based chain-of-thought (CoT). The intermediate steps of text-based reasoning are difficult to verify, which complicates the use of reinforcement-learning signals that reward factual accuracy. To address this, we propose a Code-as-Thought (CaT) approach to represent the visual information of a chart in a verifiable, symbolic format. Our key insight is that this strategy must be adaptive: a fixed, code-only implementation consistently fails on complex charts where symbolic representation is unsuitable. This finding leads us to introduce Visual Programmability: a learnable property that determines if a chart-question pair is better solved with code or direct visual analysis. We implement this concept in an adaptive framework where a VLM learns to choose between the CaT pathway and a direct visual reasoning pathway. The selection policy of the model is trained with reinforcement learning using a novel dual-reward system. This system combines a data-accuracy reward to ground the model in facts and prevent numerical hallucination, with a decision reward that teaches the model when to use each strategy, preventing it from defaulting to a single reasoning mode. Experiments demonstrate strong and robust performance across diverse chart-understanding benchmarks. Our work shows that VLMs can be taught not only to reason but also how to reason, dynamically selecting the optimal reasoning pathway for each task.

