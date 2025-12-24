---
layout: default
title: "EvoEmo: Towards Evolved Emotional Policies for Adversarial LLM Agents in Multi-Turn Price Negotiation"
---

# EvoEmo: Towards Evolved Emotional Policies for Adversarial LLM Agents in Multi-Turn Price Negotiation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04310" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04310v3</a>
  <a href="https://arxiv.org/pdf/2509.04310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04310v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04310v3', 'EvoEmo: Towards Evolved Emotional Policies for Adversarial LLM Agents in Multi-Turn Price Negotiation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunbo Long, Liming Xu, Lukas Beckenbauer, Yuhan Liu, Alexandra Brintrup

**分类**: cs.AI

**发布日期**: 2025-09-04 (更新: 2025-10-13)

---

## 💡 一句话要点

**EvoEmo：面向多轮价格谈判中对抗性LLM智能体的演化情感策略**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感计算` `多轮谈判` `大型语言模型` `强化学习` `演化算法` `人机交互` `智能体`

## 📋 核心要点

1. 现有LLM智能体在谈判中情感表达被动，易受对抗方操纵，缺乏策略性情感运用。
2. EvoEmo通过演化强化学习优化动态情感表达，将情感状态转移建模为马尔可夫决策过程。
3. 实验表明，EvoEmo显著提升谈判成功率、效率和买方收益，验证了自适应情感表达的重要性。

## 📝 摘要（中文）

现有大型语言模型（LLM）智能体在复杂、多轮谈判中展现出潜力，但它们通常忽略了情感在谈判中的作用，仅产生被动的、由偏好驱动的情感反应，容易受到对抗方的操纵和策略性利用。为了解决这个问题，我们提出了EvoEmo，一个演化强化学习框架，用于优化谈判中的动态情感表达。EvoEmo将情感状态转移建模为马尔可夫决策过程，并采用基于种群的遗传优化来演化各种谈判场景下的高回报情感策略。我们还提出了一个包含vanilla策略和固定情感策略的评估框架，用于评估情感感知谈判。广泛的实验和消融研究表明，EvoEmo始终优于这两个基线，实现了更高的成功率、更高的效率和更高的买方节省。这些发现突出了自适应情感表达在使LLM智能体更有效地进行多轮谈判中的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM智能体在多轮价格谈判中，由于缺乏策略性情感表达而容易被对手利用的问题。现有方法通常采用被动的情感反应，无法根据谈判态势动态调整情感，导致谈判效率和结果不佳。

**核心思路**：论文的核心思路是通过演化强化学习，学习一种能够根据谈判状态动态调整情感表达的策略。这种策略能够使LLM智能体在谈判中更加灵活和具有竞争力，从而提高谈判成功率和收益。核心在于将情感表达视为一种可学习的策略，而非固定的反应。

**技术框架**：EvoEmo框架包含以下主要模块：1) 情感状态空间定义：定义智能体在谈判中可能经历的情感状态。2) 情感转移模型：将情感状态转移建模为马尔可夫决策过程（MDP），其中状态是谈判状态和当前情感，动作是情感表达的变化，奖励是谈判结果。3) 演化强化学习：使用基于种群的遗传算法来优化情感策略，种群中的每个个体代表一种情感策略。4) 评估框架：设计了包含vanilla策略和固定情感策略的基线，用于评估EvoEmo的性能。

**关键创新**：最重要的技术创新点在于将情感表达视为一种可学习的策略，并通过演化强化学习来优化这种策略。与现有方法相比，EvoEmo能够根据谈判状态动态调整情感表达，从而提高谈判效率和结果。此外，使用遗传算法进行策略优化，能够探索更广阔的策略空间，找到更优的情感策略。

**关键设计**：情感状态空间的设计需要考虑谈判中可能出现的情感，例如愤怒、高兴、沮丧等。奖励函数的设计需要能够反映谈判结果的好坏，例如买方节省的金额或谈判的成功率。遗传算法的关键参数包括种群大小、交叉概率和变异概率。此外，论文还设计了特定的评估指标，例如谈判成功率、谈判轮数和买方节省的金额。

## 📊 实验亮点

实验结果表明，EvoEmo在多轮价格谈判中显著优于vanilla策略和固定情感策略。具体而言，EvoEmo实现了更高的谈判成功率（提升超过10%），更高的谈判效率（减少谈判轮数），以及更高的买方节省（平均节省金额增加）。消融研究进一步验证了动态情感表达在提高谈判性能中的重要性。

## 🎯 应用场景

EvoEmo的研究成果可应用于各种人机交互场景，例如在线购物、商务谈判、客户服务等。通过赋予AI智能体更丰富的情感表达能力，可以提高用户满意度、改善沟通效率，并最终提升商业价值。未来，该技术还可以扩展到其他领域，例如心理咨询、教育等，以提供更个性化和有效的人工智能服务。

## 📄 摘要（原文）

> Recent research on Chain-of-Thought (CoT) reasoning in Large Language Models (LLMs) has demonstrated that agents can engage in \textit{complex}, \textit{multi-turn} negotiations, opening new avenues for agentic AI. However, existing LLM agents largely overlook the functional role of emotions in such negotiations, instead generating passive, preference-driven emotional responses that make them vulnerable to manipulation and strategic exploitation by adversarial counterparts. To address this gap, we present EvoEmo, an evolutionary reinforcement learning framework that optimizes dynamic emotional expression in negotiations. EvoEmo models emotional state transitions as a Markov Decision Process and employs population-based genetic optimization to evolve high-reward emotion policies across diverse negotiation scenarios. We further propose an evaluation framework with two baselines -- vanilla strategies and fixed-emotion strategies -- for benchmarking emotion-aware negotiation. Extensive experiments and ablation studies show that EvoEmo consistently outperforms both baselines, achieving higher success rates, higher efficiency, and increased buyer savings. This findings highlight the importance of adaptive emotional expression in enabling more effective LLM agents for multi-turn negotiation.

