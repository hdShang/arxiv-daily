---
layout: default
title: "Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds"
---

# Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15915" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15915v1</a>
  <a href="https://arxiv.org/pdf/2509.15915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15915v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15915v1', 'Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Remo Sasso, Michelangelo Conserva, Dominik Jeurissen, Paulo Rauber

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-19

**备注**: 20 pages, 9 figures. Accepted for presentation at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop on Embodied World Models for Decision Making

---

## 💡 一句话要点

**提出基于Foundation Model的世界模型与智能体，提升文本网格世界中的强化学习效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Foundation Model` `世界模型` `强化学习` `文本网格世界` `样本效率`

## 📋 核心要点

1. 现有强化学习方法在真实世界应用中，由于交互成本高昂，样本效率成为瓶颈。
2. 利用Foundation Model的先验知识和推理能力，分别构建世界模型（FWM）和智能体（FA），提升强化学习效率。
3. 实验表明，LLM的进步能直接提升FWM和FA的性能，FWM与强化学习结合在复杂环境中有潜力。

## 📝 摘要（中文）

本文研究如何将预训练的Foundation Model（FM）集成到强化学习框架中，以提高样本效率。针对交互代价高昂的现实世界应用，从零开始的强化学习效率较低。本文提出了两种策略：一是利用FM的先验知识构建Foundation World Model（FWM），通过模拟交互训练和评估智能体；二是利用FM的推理能力构建Foundation Agent（FA），直接进行决策。在文本网格世界环境中，实验结果表明，LLM的改进能够转化为更好的FWM和FA。基于当前LLM的FA在简单环境中表现出色，而FWM与强化学习智能体的结合在复杂环境中具有潜力，尤其是在部分可观测和随机环境中。

## 🔬 方法详解

**问题定义**：论文旨在解决强化学习在真实世界应用中样本效率低下的问题。现有方法需要大量的环境交互才能学习到有效的策略，这在交互成本高昂的场景中是不可接受的。因此，如何利用预训练的Foundation Model来提升强化学习的样本效率是一个关键挑战。

**核心思路**：论文的核心思路是利用Foundation Model的两种能力：一是利用其先验知识构建世界模型，从而可以在模拟环境中进行训练，降低真实环境的交互成本；二是利用其推理能力直接进行决策，构建智能体，从而避免从零开始学习策略。

**技术框架**：整体框架包含两个主要分支：基于Foundation World Model（FWM）的强化学习和基于Foundation Agent（FA）的直接决策。在FWM分支中，首先使用FM构建世界模型，然后使用强化学习算法在世界模型中训练智能体。在FA分支中，直接使用FM作为智能体，根据环境状态进行决策。两个分支都在文本网格世界环境中进行评估。

**关键创新**：论文的关键创新在于提出了两种利用Foundation Model进行强化学习的策略，并对这两种策略进行了全面的评估。具体来说，FWM的创新在于利用FM的先验知识构建世界模型，从而可以在模拟环境中进行训练，降低真实环境的交互成本。FA的创新在于利用FM的推理能力直接进行决策，从而避免从零开始学习策略。

**关键设计**：论文的关键设计包括：1) 使用文本网格世界环境作为评估平台，该环境适合当前的大型语言模型（LLM）；2) 设计了基于LLM的FWM和FA，并针对不同的环境复杂度进行了调整；3) 使用标准的强化学习算法（如Q-learning）在FWM中训练智能体；4) 对FWM和FA的性能进行了全面的评估，包括在不同环境下的样本效率和策略质量。

## 📊 实验亮点

实验结果表明，LLM的改进能够转化为更好的FWM和FA。基于当前LLM的FA在足够简单的环境中可以提供出色的策略。FWM与强化学习智能体的结合在更复杂的环境中具有很高的潜力，尤其是在部分可观测和随机环境中。这些结果表明，Foundation Model在强化学习中具有巨大的潜力。

## 🎯 应用场景

该研究成果可应用于机器人导航、游戏AI、自动驾驶等领域。通过利用预训练的Foundation Model，可以显著降低强化学习的样本需求，加速智能体在复杂环境中的学习和部署。未来，可以将该方法扩展到更复杂的环境和任务中，例如，在真实机器人平台上进行实验，或者在更复杂的模拟环境中进行训练。

## 📄 摘要（原文）

> While reinforcement learning from scratch has shown impressive results in solving sequential decision-making tasks with efficient simulators, real-world applications with expensive interactions require more sample-efficient agents. Foundation models (FMs) are natural candidates to improve sample efficiency as they possess broad knowledge and reasoning capabilities, but it is yet unclear how to effectively integrate them into the reinforcement learning framework. In this paper, we anticipate and, most importantly, evaluate two promising strategies. First, we consider the use of foundation world models (FWMs) that exploit the prior knowledge of FMs to enable training and evaluating agents with simulated interactions. Second, we consider the use of foundation agents (FAs) that exploit the reasoning capabilities of FMs for decision-making. We evaluate both approaches empirically in a family of grid-world environments that are suitable for the current generation of large language models (LLMs). Our results suggest that improvements in LLMs already translate into better FWMs and FAs; that FAs based on current LLMs can already provide excellent policies for sufficiently simple environments; and that the coupling of FWMs and reinforcement learning agents is highly promising for more complex settings with partial observability and stochastic elements.

