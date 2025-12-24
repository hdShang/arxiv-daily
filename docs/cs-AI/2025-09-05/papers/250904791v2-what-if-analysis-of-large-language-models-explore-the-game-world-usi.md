---
layout: default
title: "What-If Analysis of Large Language Models: Explore the Game World Using Proactive Thinking"
---

# What-If Analysis of Large Language Models: Explore the Game World Using Proactive Thinking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04791" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04791v2</a>
  <a href="https://arxiv.org/pdf/2509.04791.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04791v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04791v2', 'What-If Analysis of Large Language Models: Explore the Game World Using Proactive Thinking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuan Sui, Yanming Zhang, Yi Liao, Yu Gu, Guohua Tang, Zhongqian Sun, Wei Yang, Bryan Hooi

**分类**: cs.AI

**发布日期**: 2025-09-05 (更新: 2025-12-04)

---

## 💡 一句话要点

**提出WiA-LLM，利用主动思考进行大型语言模型在MOBA游戏中的假设分析。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `反事实推理` `世界模型` `强化学习` `游戏AI`

## 📋 核心要点

1. 现有LLM在动态游戏中决策时，缺乏有效的反事实推理能力，难以准确预测动作的未来影响。
2. WiA-LLM将LLM训练为显式的、基于语言的世界模型，通过语言建模游戏状态演变和提供文本解释。
3. 实验表明，WiA-LLM在王者荣耀中预测游戏状态变化的准确率显著提升，且策略行为更接近专家玩家。

## 📝 摘要（中文）

大型语言模型(LLMs)在推理和信息检索方面表现出色，但在动态、部分可观察、高风险的环境（如MOBA游戏）中进行决策时仍然不可靠。一个关键限制是反事实推理能力薄弱：LLMs难以对候选动作及其未来后果进行精确的假设分析。为了解决这个限制，我们提出了假设分析LLM (WiA-LLM)，该框架将LLM训练成一个显式的、基于语言的世界模型。WiA-LLM不是用潜在向量表示环境，而是使用语言来建模游戏状态如何随时间和候选动作演变，并为这些预测结果提供文本解释。这种显式建模支持（1）可解释性，因为模型的预测和底层原理是人类可读的，以及（2）语义泛化，因为模型可以在共享相似游戏概念（例如，角色、目标或战术）的情况下迁移知识。WiA-LLM的训练分为两个阶段：在类人推理轨迹上进行监督式微调，然后通过基于结果的强化学习，根据预测和真实未来状态之间的差异来获得奖励。在王者荣耀(HoK)环境中，WiA-LLM在预测游戏状态变化方面的准确率达到74.2%（比基础模型提高27%）。此外，我们发现具有WiA-LLM的智能体比纯粹反应式的LLM智能体表现出更接近专家玩家的战略行为，表明其决策更具前瞻性和与专家对齐。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在动态、部分可观察的游戏环境中进行决策时，反事实推理能力不足的问题。现有方法通常依赖于隐向量表示环境，难以进行精确的假设分析，并且缺乏可解释性。这导致LLMs在复杂游戏场景中难以做出可靠的决策。

**核心思路**：论文的核心思路是将LLM训练成一个显式的、基于语言的世界模型。通过使用语言来建模游戏状态随时间和候选动作的演变，WiA-LLM能够提供可解释的预测结果，并支持语义泛化。这种显式建模使得模型能够更好地理解游戏概念，并在不同场景中迁移知识。

**技术框架**：WiA-LLM的训练分为两个阶段。第一阶段是监督式微调，使用类人推理轨迹数据对LLM进行训练，使其能够模仿人类玩家的推理过程。第二阶段是强化学习，使用基于结果的奖励函数来优化模型，奖励函数基于预测的游戏状态与真实游戏状态之间的差异。整体流程包括：输入当前游戏状态和候选动作，WiA-LLM预测未来的游戏状态，并提供文本解释，然后根据预测结果和真实结果计算奖励，用于更新模型参数。

**关键创新**：最重要的技术创新点在于使用语言作为世界模型的表示形式。与传统的隐向量表示相比，语言具有更强的表达能力和可解释性。此外，WiA-LLM通过显式地建模游戏状态的演变过程，能够更好地进行反事实推理，并支持语义泛化。

**关键设计**：WiA-LLM的关键设计包括：(1) 使用Transformer架构作为LLM的基础模型；(2) 设计合适的提示工程（Prompt Engineering）来指导LLM进行推理；(3) 使用基于结果的奖励函数，鼓励模型预测准确的未来游戏状态；(4) 使用监督式微调和强化学习相结合的训练方法，提高模型的性能和泛化能力。

## 📊 实验亮点

实验结果表明，WiA-LLM在王者荣耀(HoK)环境中，预测游戏状态变化的准确率达到74.2%，相比于基础模型提升了27%。此外，配备WiA-LLM的智能体在游戏中的策略行为更接近专家玩家，表明其决策更具前瞻性和与专家对齐。这些结果验证了WiA-LLM在提高LLM反事实推理能力和决策水平方面的有效性。

## 🎯 应用场景

WiA-LLM的研究成果可以应用于各种需要复杂决策和推理的动态环境中，例如自动驾驶、机器人导航、金融交易等。通过提高LLM的反事实推理能力和可解释性，可以使其在这些领域中做出更可靠、更合理的决策，从而提高效率和安全性。此外，该研究还可以促进人机协作，使人类能够更好地理解和信任AI系统的决策过程。

## 📄 摘要（原文）

> Large Language Models (LLMs) are effective at reasoning and information retrieval, but remain unreliable for decision-making in dynamic, partially observable, high-stakes environments such as MOBA games. One key limitation is weak counterfactual reasoning: LLMs struggle to conduct precise what-if analysis over candidate actions and their future consequences. We address this limitation with What-if Analysis LLM (WiA-LLM), a framework that trains an LLM as an explicit language-based world model. Instead of representing the environment in latent vectors, WiA-LLM models how the game state evolves over time with candidate actions using language, and provides textual justifications for these predicted outcomes. This explicit modeling supports (1) interpretability, since the model's predictions and underlying rationales are human-readable, and (2) semantic generalization, as the model can transfer knowledge across situations that share similar game concepts (e.g., roles, objectives, or tactics). WiA-LLM is trained in two stages: supervised fine-tuning on human-like reasoning traces, followed by reinforcement learning with outcome-based rewards that depend on the discrepancy between predicted and ground-truth future states. In the Honor of Kings (HoK) environment, WiA-LLM attains 74.2\% accuracy (27\%$\uparrow$ vs. base model) in forecasting game-state changes. In addition, we find that agents with WiA-LLM exhibit closer strategic behavior to expert players than purely reactive LLM agents, indicating more foresight-aware and expert-aligned decision-making.

