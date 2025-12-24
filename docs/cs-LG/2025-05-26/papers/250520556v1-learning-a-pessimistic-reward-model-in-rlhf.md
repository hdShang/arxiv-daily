---
layout: default
title: Learning a Pessimistic Reward Model in RLHF
---

# Learning a Pessimistic Reward Model in RLHF

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20556" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20556v1</a>
  <a href="https://arxiv.org/pdf/2505.20556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20556v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20556v1', 'Learning a Pessimistic Reward Model in RLHF')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinglun Xu, Hangoo Kang, Tarun Suresh, Yuxuan Wan, Gagandeep Singh

**分类**: cs.LG

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出PET方法以解决离线RLHF中的奖励黑客问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `人类反馈` `奖励建模` `悲观奖励` `策略优化` `自然语言处理` `文本摘要`

## 📋 核心要点

1. 现有的奖励建模技术在RLHF中存在不完美的奖励模型，导致奖励黑客问题依然严重。
2. 论文提出的PET方法通过微调悲观奖励模型，能够在不依赖正则化的情况下优化策略，防止奖励黑客。
3. 实验结果表明，使用悲观奖励模型可以学习到高质量的策略，且与数据集分布的KL散度较大，但实际性能依然优秀。

## 📝 摘要（中文）

本文提出了一种新颖的悲观奖励微调方法PET，以学习一种对奖励黑客具有鲁棒性的悲观奖励模型，适用于离线人类反馈强化学习（RLHF）。传统的奖励建模技术在RLHF中训练不完美的奖励模型，KL正则化在优化策略时起着关键作用以减轻奖励黑客的影响。然而，这种基于直觉的方法仍然面临奖励黑客的问题，并且在学习过程中排除了与数据集分布具有较大KL散度的策略。相反，我们展示了通过PET微调的悲观奖励模型优化策略时，可以在不依赖任何正则化的情况下防止奖励黑客。我们在标准的TL;DR摘要数据集上测试了我们的方法，发现可以在没有任何正则化的情况下学习高质量的策略。总之，我们的工作展示了学习针对奖励黑客的悲观奖励模型的可行性。

## 🔬 方法详解

**问题定义**：本文旨在解决离线人类反馈强化学习中的奖励黑客问题。现有方法依赖于KL正则化来缓解这一问题，但仍然无法完全消除奖励黑客的影响，且排除了与数据集分布差异较大的策略。

**核心思路**：论文提出的PET方法通过微调悲观奖励模型，使得在优化策略时能够有效防止奖励黑客，而不需要依赖任何正则化手段。这种设计使得代理能够贪婪地搜索高悲观奖励的策略。

**技术框架**：整体架构包括数据收集、奖励模型训练和策略优化三个主要阶段。首先收集人类反馈数据，然后训练悲观奖励模型，最后在该模型上优化策略。

**关键创新**：最重要的技术创新在于提出了PET方法，通过微调悲观奖励模型来替代传统的正则化方法，从根本上改变了策略优化的方式。

**关键设计**：在模型训练中，采用了特定的损失函数来确保悲观奖励的有效性，同时在策略优化阶段，允许较大的KL散度，以便探索更优的策略。

## 📊 实验亮点

实验结果显示，使用PET方法训练的悲观奖励模型能够在没有任何正则化的情况下学习到高质量的策略。与传统方法相比，该策略在实践中表现出色，尽管与数据集分布的KL散度较大，依然能够实现高性能。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的文本摘要、对话系统以及其他需要人类反馈的强化学习任务。通过有效防止奖励黑客，PET方法能够提高模型的鲁棒性和实际应用效果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This work proposes `PET', a novel pessimistic reward fine-tuning method, to learn a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF). Traditional reward modeling techniques in RLHF train an imperfect reward model, on which a KL regularization plays a pivotal role in mitigating reward hacking when optimizing a policy. Such an intuition-based method still suffers from reward hacking, and the policies with large KL divergence from the dataset distribution are excluded during learning. In contrast, we show that when optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization. We test our methods on the standard TL;DR summarization dataset. We find that one can learn a high-quality policy on our pessimistic reward without using any regularization. Such a policy has a high KL divergence from the dataset distribution while having high performance in practice. In summary, our work shows the feasibility of learning a pessimistic reward model against reward hacking. The agent can greedily search for the policy with a high pessimistic reward without suffering from reward hacking.

