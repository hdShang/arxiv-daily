---
layout: default
title: Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game
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

**提出Stackelberg学习框架SLHF，通过序贯博弈优化人类反馈偏好**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `偏好学习` `强化学习` `Stackelberg博弈` `大型语言模型`

## 📋 核心要点

1. 现有基于人类反馈的强化学习（RLHF）和纳什学习（NLHF）方法在处理复杂偏好结构时存在局限性。
2. SLHF将偏好优化建模为领导者-跟随者的序贯博弈，利用序贯博弈的不对称性来捕捉更丰富的偏好结构。
3. 实验表明，SLHF在不同规模的语言模型上实现了强大的对齐，并能进行跨模型迁移的推理时优化。

## 📝 摘要（中文）

本文提出了一种新的偏好优化框架——Stackelberg学习框架（SLHF）。SLHF将对齐问题建模为两个策略之间的序贯博弈：领导者（Leader）承诺一个动作，跟随者（Follower）根据领导者的动作做出响应。这种方法将偏好优化分解为跟随者的优化问题和领导者对抗性优化问题。与为动作分配标量奖励的RLHF或寻求同步博弈均衡的NLHF不同，SLHF利用序贯博弈的不对称性来捕获更丰富的偏好结构。SLHF的序贯设计自然地实现了推理时优化，因为跟随者学会改进领导者的动作，并且这些改进可以通过迭代采样来利用。我们比较了SLHF、RLHF和NLHF的解概念，并阐述了在一致性、数据敏感性和对非传递偏好的鲁棒性方面的关键优势。对大型语言模型的实验表明，SLHF在不同的偏好数据集上实现了强大的对齐，可以从0.5B扩展到8B参数，并产生了可以在模型系列之间转移而无需进一步微调的推理时优化。

## 🔬 方法详解

**问题定义**：现有基于人类反馈的强化学习（RLHF）方法通常将人类反馈转化为标量奖励，简化了复杂的偏好结构。纳什学习（NLHF）则假设策略同步进行，忽略了策略之间的依赖关系。这些方法在处理非传递偏好或需要细粒度调整的场景下表现不佳。

**核心思路**：SLHF的核心思想是将偏好学习建模为一个Stackelberg博弈，其中领导者（Leader）策略先行动，跟随者（Follower）策略根据领导者的行动做出反应。这种序贯博弈结构能够更好地捕捉策略之间的依赖关系，并允许跟随者对领导者的行为进行细化和改进。

**技术框架**：SLHF的整体框架包含两个主要阶段：跟随者学习和领导者优化。首先，跟随者通过学习人类反馈，学习如何根据领导者的动作进行改进。然后，领导者通过对抗性优化，学习如何生成能够最大化人类偏好的动作，同时考虑到跟随者的反应。在推理阶段，跟随者可以对领导者的输出进行迭代优化，从而提高整体性能。

**关键创新**：SLHF的关键创新在于将偏好学习问题建模为一个序贯博弈，从而能够捕捉更丰富的偏好结构。与RLHF和NLHF相比，SLHF能够更好地处理非传递偏好，并且允许在推理时进行细粒度优化。此外，SLHF的序贯设计使得跟随者学习到的知识可以跨模型迁移。

**关键设计**：SLHF的关键设计包括：1) 使用合适的损失函数来训练跟随者，使其能够准确预测人类对领导者动作的偏好；2) 设计有效的对抗性优化算法来训练领导者，使其能够生成能够最大化人类偏好的动作；3) 探索不同的迭代优化策略，以提高推理时的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16626v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SLHF在不同的偏好数据集上实现了强大的对齐，并且能够扩展到不同规模的语言模型（从0.5B到8B参数）。更重要的是，SLHF产生的推理时优化可以跨模型系列转移，无需进一步微调，这表明SLHF具有很强的泛化能力。SLHF在一致性、数据敏感性和对非传递偏好的鲁棒性方面优于RLHF和NLHF。

## 🎯 应用场景

SLHF可应用于各种需要从人类反馈中学习的场景，例如对话系统、文本生成、图像生成和机器人控制。通过利用SLHF，可以训练出更符合人类偏好、更安全可靠的智能系统。此外，SLHF的推理时优化能力使其能够适应不同的用户需求和环境变化。

## 📄 摘要（原文）

> We introduce Stackelberg Learning from Human Feedback (SLHF), a new framework for preference optimization. SLHF frames the alignment problem as a sequential-move game between two policies: a Leader, which commits to an action, and a Follower, which responds conditionally on the Leader's action. This approach decomposes preference optimization into a refinement problem for the Follower and an optimization problem against an adversary for the Leader. Unlike Reinforcement Learning from Human Feedback (RLHF), which assigns scalar rewards to actions, or Nash Learning from Human Feedback (NLHF), which seeks a simultaneous-move equilibrium, SLHF leverages the asymmetry of sequential play to capture richer preference structures. The sequential design of SLHF naturally enables inference-time refinement, as the Follower learns to improve the Leader's actions, and these refinements can be leveraged through iterative sampling. We compare the solution concepts of SLHF, RLHF, and NLHF, and lay out key advantages in consistency, data sensitivity, and robustness to intransitive preferences. Experiments on large language models demonstrate that SLHF achieves strong alignment across diverse preference datasets, scales from 0.5B to 8B parameters, and yields inference-time refinements that transfer across model families without further fine-tuning.

