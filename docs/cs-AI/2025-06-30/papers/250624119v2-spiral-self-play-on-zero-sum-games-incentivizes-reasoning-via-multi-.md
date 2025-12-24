---
layout: default
title: "SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning"
---

# SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24119" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24119v2</a>
  <a href="https://arxiv.org/pdf/2506.24119.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24119v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24119v2', 'SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-30 (更新: 2025-07-01)

**备注**: Work in Progress

---

## 💡 一句话要点

**提出SPIRAL框架以解决自我监督的推理能力培养问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自我对弈` `零和游戏` `强化学习` `推理能力` `多智能体系统` `在线训练` `角色条件优势估计` `自主学习`

## 📋 核心要点

1. 现有方法依赖人工策划的问题和奖励，限制了推理能力的自主发展。
2. SPIRAL通过自我对弈的方式，模型在零和游戏中不断提升，消除人工监督需求。
3. 在Kuhn Poker上训练Qwen3-4B-Base，数学和一般推理分别提升8.6%和8.4%，超越了基于专家轨迹的SFT。

## 📝 摘要（中文）

近年来强化学习的进展表明，语言模型可以通过训练获得复杂的推理能力，但这些方法依赖于人工策划的问题-答案对和领域特定的奖励工程。我们提出SPIRAL，一个自我对弈框架，模型通过与不断改进的自身进行多回合零和游戏学习，从而消除对人工监督的需求。SPIRAL通过自我对弈生成无限的逐步挑战问题，模型必须不断适应更强的对手。我们实现了一个完全在线的多回合多智能体强化学习系统，并提出了基于角色的优势估计（RAE）以稳定多智能体训练。使用SPIRAL，零和游戏的自我对弈产生了广泛转移的推理能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有强化学习方法中对人工监督的依赖，限制了模型推理能力的自主发展。现有方法通常需要人工策划的问题和奖励，导致训练效率低下。

**核心思路**：SPIRAL框架通过自我对弈的方式，让模型在零和游戏中与不断改进的自身进行对抗，生成逐步递进的挑战，从而实现自主学习和推理能力的提升。

**技术框架**：SPIRAL的整体架构包括自我对弈的多回合多智能体强化学习系统，主要模块包括角色条件优势估计（RAE）和在线训练机制。模型在每一轮对弈中不断适应对手的策略，形成一个动态的学习环境。

**关键创新**：SPIRAL的核心创新在于通过自我对弈生成无限的训练课程，模型能够在没有人工干预的情况下，逐步提高推理能力。这种方法与传统的依赖人工设计的训练方式本质上不同。

**关键设计**：在技术细节上，SPIRAL采用了角色条件优势估计（RAE）来稳定多智能体训练过程，确保模型在对弈中能够有效学习。此外，训练过程中使用的损失函数和网络结构经过精心设计，以适应多回合的对抗环境。

## 📊 实验亮点

SPIRAL在Kuhn Poker上训练Qwen3-4B-Base，数学和一般推理分别提升8.6%和8.4%，超越了基于25,000条专家游戏轨迹的SFT。此外，多游戏训练（如TicTacToe和简单谈判）进一步提升了模型的推理能力，显示出零和游戏在推理能力转移中的有效性。

## 🎯 应用场景

SPIRAL框架的潜在应用场景包括教育、游戏AI和自动推理系统等领域。通过自主学习和推理能力的提升，SPIRAL可以用于开发更智能的对话系统、决策支持工具以及复杂问题求解的自动化系统，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in reinforcement learning have shown that language models can develop sophisticated reasoning through training on tasks with verifiable rewards, but these approaches depend on human-curated problem-answer pairs and domain-specific reward engineering. We introduce SPIRAL, a self-play framework where models learn by playing multi-turn, zero-sum games against continuously improving versions of themselves, eliminating the need for human supervision. Through self-play, SPIRAL generates an infinite curriculum of progressively challenging problems as models must constantly adapt to stronger opponents. To enable this self-play training at scale, We implement a fully online, multi-turn, multi-agent reinforcement learning system for LLMs and propose role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Using SPIRAL, self-play on zero-sum games produces reasoning capabilities that transfer broadly. Training Qwen3-4B-Base on Kuhn Poker alone achieves 8.6% improvement on math and 8.4% on general reasoning, outperforming SFT on 25,000 expert game trajectories. Analysis reveals that this transfer occurs through three cognitive patterns: systematic decomposition, expected value calculation, and case-by-case analysis. Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) further enhances performance as each game develops distinct reasoning strengths. Applying SPIRAL to a strong reasoning model (DeepSeek-R1-Distill-Qwen-7B) can still lead to 2.0% average improvement. These results demonstrate that zero-sum games naturally develop transferable reasoning capabilities, highlighting a promising direction for autonomous reasoning development.

