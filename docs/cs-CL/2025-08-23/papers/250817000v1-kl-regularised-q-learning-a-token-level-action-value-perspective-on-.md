---
layout: default
title: "KL-Regularised Q-Learning: A Token-level Action-Value perspective on Online RLHF"
---

# KL-Regularised Q-Learning: A Token-level Action-Value perspective on Online RLHF

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17000" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17000v1</a>
  <a href="https://arxiv.org/pdf/2508.17000.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17000v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17000v1', 'KL-Regularised Q-Learning: A Token-level Action-Value perspective on Online RLHF')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jason R Brown, Lennie Wells, Edward James Young, Sergio Bacallado

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-23

---

## 💡 一句话要点

**提出KL正则化Q学习以优化语言模型的强化学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `语言模型` `KL散度` `策略优化` `对话生成` `文本摘要` `人类反馈`

## 📋 核心要点

1. 现有的PPO算法在处理KL散度约束时缺乏系统性，存在一定的局限性。
2. 本文提出的KL正则化Q学习（KLQ）方法为LM-RLHF设置提供了一种新的动作值强化学习框架。
3. 实验结果显示，KLQ在语言生成任务上与PPO表现相当，并在评估中胜率更高，展示了其潜力。

## 📝 摘要（中文）

近端策略优化（PPO）是一种有效的策略梯度算法，广泛应用于基于人类反馈的语言模型强化学习（LM-RLHF）。尽管PPO在实际应用中表现良好，但其处理KL散度约束的方式较为随意。本文提出了一种新的动作值强化学习方法KL正则化Q学习（KLQ），并证明该方法在某种特定意义上等价于PPO，尽管其动机截然不同。我们在两个关键的语言生成任务上对KLQ进行了基准测试，结果表明KLQ在优化LM-RLHF目标时与PPO表现相当，并在大型语言模型评估中对PPO的胜率更高。

## 🔬 方法详解

**问题定义**：本文旨在解决现有PPO算法在处理KL散度约束时的随意性和缺乏系统性的问题，提升LM-RLHF的效果。

**核心思路**：KL正则化Q学习（KLQ）通过引入KL散度正则化项，提供了一种新的动作值学习框架，旨在更有效地优化语言模型的策略。

**技术框架**：KLQ的整体架构包括状态表示、动作选择和价值评估三个主要模块。通过引入KL散度约束，KLQ能够在学习过程中保持策略的稳定性。

**关键创新**：KLQ的主要创新在于其将动作值学习与KL散度正则化结合，形成了一种新的学习机制，与传统的PPO方法在动机和实现上有本质区别。

**关键设计**：在KLQ中，关键参数包括KL散度的权重设置和动作价值函数的设计，损失函数则结合了传统的Q学习损失和KL正则化项，以确保学习过程的有效性和稳定性。

## 📊 实验亮点

实验结果表明，KLQ在优化LM-RLHF目标时与PPO表现相当，并在大型语言模型作为评估者的测试中，KLQ的胜率 consistently 高于PPO，显示出其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的对话系统、文本摘要生成等任务。通过优化语言模型的学习过程，KLQ能够提升生成文本的质量和相关性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Proximal Policy Optimisation (PPO) is an established and effective policy gradient algorithm used for Language Model Reinforcement Learning from Human Feedback (LM-RLHF). PPO performs well empirically but has a heuristic motivation and handles the KL-divergence constraint used in LM-RLHF in an ad-hoc manner. In this paper, we develop a a new action-value RL method for the LM-RLHF setting, KL-regularised Q-Learning (KLQ). We then show that our method is equivalent to a version of PPO in a certain specific sense, despite its very different motivation. Finally, we benchmark KLQ on two key language generation tasks -- summarisation and single-turn dialogue. We demonstrate that KLQ performs on-par with PPO at optimising the LM-RLHF objective, and achieves a consistently higher win-rate against PPO on LLM-as-a-judge evaluations.

