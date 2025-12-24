---
layout: default
title: "RLSR: Reinforcement Learning from Self Reward"
---

# RLSR: Reinforcement Learning from Self Reward

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08827" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08827v2</a>
  <a href="https://arxiv.org/pdf/2505.08827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08827v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08827v2', 'RLSR: Reinforcement Learning from Self Reward')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Toby Simonds, Kevin Lopez, Akira Yoshiyama, Dominique Garmier

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-12 (更新: 2025-08-06)

---

## 💡 一句话要点

**提出自我奖励强化学习方法以解决奖励工程挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我奖励` `强化学习` `大型语言模型` `自我判断` `自我改进` `无监督学习` `奖励信号` `复杂问题求解`

## 📋 核心要点

1. 现有的强化学习方法依赖于可验证的奖励，这在许多领域中难以实现，限制了模型的自我改进能力。
2. 本文提出了一种自我奖励的强化学习方法，允许模型通过自我判断生成奖励信号，从而实现自我改进。
3. 实验结果显示，模型在没有真实答案的情况下，能够在Countdown谜题和积分问题上达到与正式验证相当的性能。

## 📝 摘要（中文）

大型语言模型（LLMs）能够生成复杂问题的解决方案，但使用强化学习进行训练通常需要可验证的奖励，这些奖励的创建成本高且在某些领域不可行。本文展示了LLMs如何通过自我判断进行有效的自我改进，利用生成与验证解决方案之间的内在不对称性。实验表明，模型能够在没有真实答案的情况下提供可靠的奖励信号，从而在可验证奖励不切实际的领域实现强化学习。通过在Countdown谜题和积分问题上实施自我判断，我们的性能与正式验证相当，且无需真实答案。最显著的是，经过自我奖励训练的Qwen 2.5 7B DeepSeek Distilled模型有资格参加MIT积分竞赛，展现出自我监督改进的能力。结合合成问题生成，我们建立了一个完整的自我改进循环，使模型能够生成练习问题、解决问题并评估自身表现，无需外部验证。我们的研究表明，LLM评判者可以为训练提供有效的奖励信号，开启了在奖励工程挑战限制下的强化学习新领域。

## 🔬 方法详解

**问题定义**：本文旨在解决在许多领域中可验证奖励难以获取的问题，现有方法在此情况下无法有效进行强化学习。

**核心思路**：通过自我判断，LLMs能够在没有外部参考答案的情况下生成奖励信号，从而实现自我改进和学习。

**技术框架**：整体流程包括模型生成问题、解决问题、评估自身表现三个主要模块，形成一个闭环的自我改进系统。

**关键创新**：最重要的创新在于模型能够自我生成奖励信号，打破了传统强化学习对真实奖励的依赖，提升了模型在复杂领域的适应性。

**关键设计**：在训练过程中，模型使用自我生成的奖励信号进行优化，设计了特定的损失函数以适应自我判断的反馈机制。

## 📊 实验亮点

实验结果表明，经过自我奖励训练的Qwen 2.5 7B DeepSeek Distilled模型在Countdown谜题和积分问题上表现出色，性能与传统的正式验证方法相当，且无需真实答案，展示了自我监督学习的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括教育、游戏和复杂问题求解等场景，能够帮助模型在缺乏标注数据的情况下进行有效学习。未来，这种自我奖励机制可能推动自主AI系统的发展，使其在多种领域中实现持续自我改进。

## 📄 摘要（原文）

> Large language models can generate solutions to complex problems, but training them with reinforcement learning typically requires verifiable rewards that are expensive to create and not possible for all domains. We demonstrate that LLMs can effectively self-improve through self-judging without reference solutions, leveraging the inherent asymmetry between generating and verifying solutions. Our experiments show that models can provide reliable reward signals without ground truth answers, enabling reinforcement learning in domains where verifiable rewards are impractical. By implementing self-judging across Countdown puzzles and integration problems, we achieve performance comparable to formal verification without ground truth solutions. Most notably, Qwen 2.5 7B DeepSeek Distilled trained with self-rewards qualifies for the prestigious MIT Integration Bee competition, performance through self-supervised improvement. When combined with synthetic question generation, we establish a complete self-improvement loop where models generate practice problems, solve them, and evaluate their own performance without any external validation. Our findings demonstrate that LLM judges can provide effective reward signals for training, unlocking reinforcement learning in countless domains previously limited by reward engineering challenges. This work represents a significant step toward autonomous AI systems that continuously improve through self-directed learning rather than human-guided training, potentially accelerating progress across domains where training data is scarce or evaluation is complex.

