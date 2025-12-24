---
layout: default
title: "Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game"
---

# Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16626" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16626v1</a>
  <a href="https://arxiv.org/pdf/2512.16626.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16626v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16626v1', 'Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Barna Pásztor, Thomas Kleine Buening, Andreas Krause

**分类**: cs.LG, cs.AI, cs.GT, cs.MA, stat.ML

**发布日期**: 2025-12-18

**备注**: 10 pages, 5 tables, 1 figures

---

## 💡 一句话要点

**提出Stackelberg Learning from Human Feedback (SLHF)框架，用于偏好优化。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机反馈` `偏好学习` `序贯博弈` `大型语言模型` `对齐` `强化学习` `Stackelberg学习`

## 📋 核心要点

1. 现有RLHF方法为动作分配标量奖励，NLHF寻求同步博弈均衡，无法捕捉复杂偏好结构。
2. SLHF将对齐问题建模为领导者和跟随者之间的序贯博弈，利用序贯博弈的不对称性。
3. 实验表明，SLHF在不同数据集上实现了强大的对齐，且推理时优化可跨模型迁移。

## 📝 摘要（中文）

本文提出了一种新的偏好优化框架，即Stackelberg Learning from Human Feedback (SLHF)。SLHF将对齐问题建模为两个策略之间的序贯博弈：领导者(Leader)首先采取行动，然后跟随者(Follower)根据领导者的行动做出响应。这种方法将偏好优化分解为跟随者的优化问题和领导者对抗性优化问题。与为动作分配标量奖励的Reinforcement Learning from Human Feedback (RLHF)或寻求同步博弈均衡的Nash Learning from Human Feedback (NLHF)不同，SLHF利用序贯博弈的不对称性来捕获更丰富的偏好结构。SLHF的序贯设计自然地实现了推理时优化，因为跟随者学习改进领导者的动作，并且这些改进可以通过迭代采样来利用。我们比较了SLHF、RLHF和NLHF的解概念，并阐述了在一致性、数据敏感性和对非传递偏好的鲁棒性方面的关键优势。对大型语言模型的实验表明，SLHF在不同的偏好数据集上实现了强大的对齐，可以从0.5B扩展到8B参数，并产生可以在模型系列之间转移而无需进一步微调的推理时优化。

## 🔬 方法详解

**问题定义**：现有基于人类反馈的强化学习方法（如RLHF）通常将人类反馈转化为标量奖励，然后使用强化学习算法进行优化。这种方法难以捕捉人类偏好的复杂性和细微差别。此外，NLHF方法试图找到一个同步博弈的纳什均衡，但可能无法有效地利用序贯决策的优势。因此，如何更有效地利用人类反馈来对齐模型，特别是捕捉人类偏好的复杂结构，是一个关键问题。

**核心思路**：SLHF的核心思路是将对齐问题建模为一个序贯博弈，其中领导者（Leader）策略首先采取行动，然后跟随者（Follower）策略根据领导者的行动做出响应。这种序贯博弈的结构允许模型学习更丰富的偏好结构，因为跟随者可以学习如何改进领导者的行动。通过这种方式，SLHF能够更好地捕捉人类偏好的细微差别和上下文依赖性。

**技术框架**：SLHF的整体框架包含两个主要阶段：跟随者优化和领导者优化。首先，跟随者策略通过学习人类反馈来优化，目标是根据领导者的行动做出最佳响应。然后，领导者策略通过对抗性优化来学习，目标是最大化其在跟随者响应下的表现。这个过程可以迭代进行，以不断改进领导者和跟随者的策略。在推理阶段，跟随者可以用于改进领导者的输出，从而提高模型的整体性能。

**关键创新**：SLHF的关键创新在于其将对齐问题建模为一个序贯博弈。与传统的RLHF方法相比，SLHF能够捕捉更丰富的偏好结构，并利用序贯决策的优势。此外，SLHF的序贯设计允许在推理时进行优化，从而进一步提高模型的性能。与NLHF相比，SLHF避免了寻找同步博弈均衡的复杂性，并更有效地利用了序贯决策的信息。

**关键设计**：SLHF的关键设计包括跟随者策略和领导者策略的建模方式，以及用于优化这些策略的损失函数。跟随者策略通常使用监督学习方法进行训练，目标是预测人类对不同响应的偏好。领导者策略可以使用强化学习或对抗性学习方法进行训练，目标是最大化其在跟随者响应下的表现。损失函数的设计需要考虑到人类反馈的噪声和不确定性，并鼓励模型学习鲁棒的策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16626v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SLHF在多个偏好数据集上实现了强大的对齐效果，并且可以扩展到具有数十亿参数的大型语言模型。此外，SLHF产生的推理时优化可以跨模型系列转移，无需进一步微调，这表明SLHF具有良好的泛化能力。

## 🎯 应用场景

SLHF框架可应用于各种需要与人类偏好对齐的场景，例如对话系统、文本生成、图像生成和机器人控制。通过学习人类的偏好，SLHF可以帮助模型生成更符合人类期望的输出，提高用户满意度，并促进人机协作。

## 📄 摘要（原文）

> We introduce Stackelberg Learning from Human Feedback (SLHF), a new framework for preference optimization. SLHF frames the alignment problem as a sequential-move game between two policies: a Leader, which commits to an action, and a Follower, which responds conditionally on the Leader's action. This approach decomposes preference optimization into a refinement problem for the Follower and an optimization problem against an adversary for the Leader. Unlike Reinforcement Learning from Human Feedback (RLHF), which assigns scalar rewards to actions, or Nash Learning from Human Feedback (NLHF), which seeks a simultaneous-move equilibrium, SLHF leverages the asymmetry of sequential play to capture richer preference structures. The sequential design of SLHF naturally enables inference-time refinement, as the Follower learns to improve the Leader's actions, and these refinements can be leveraged through iterative sampling. We compare the solution concepts of SLHF, RLHF, and NLHF, and lay out key advantages in consistency, data sensitivity, and robustness to intransitive preferences. Experiments on large language models demonstrate that SLHF achieves strong alignment across diverse preference datasets, scales from 0.5B to 8B parameters, and yields inference-time refinements that transfer across model families without further fine-tuning.

