---
layout: default
title: "Sotopia-RL: Reward Design for Social Intelligence"
---

# Sotopia-RL: Reward Design for Social Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03905" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03905v3</a>
  <a href="https://arxiv.org/pdf/2508.03905.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03905v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03905v3', 'Sotopia-RL: Reward Design for Social Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haofei Yu, Zhengyang Qi, Yining Zhao, Kolby Nottingham, Keyang Xuan, Bodhisattwa Prasad Majumder, Hao Zhu, Paul Pu Liang, Jiaxuan You

**分类**: cs.CL

**发布日期**: 2025-08-05 (更新: 2025-10-08)

**备注**: 10 pages

---

## 💡 一句话要点

**提出Sotopia-RL以解决社会智能任务中的奖励设计问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社会智能` `强化学习` `奖励设计` `多维度评估` `语言模型`

## 📋 核心要点

1. 现有方法在社会智能任务中面临奖励设计的挑战，个体发言质量与最终成功之间的关系不明确。
2. Sotopia-RL框架通过将粗略的情节级反馈转化为发言级的多维奖励，解决了奖励设计问题。
3. 实验结果显示，Sotopia-RL在Sotopia环境中取得了7.17和8.31的社会目标完成分数，显著优于现有方法。

## 📝 摘要（中文）

社会智能已成为大型语言模型（LLMs）的关键能力，使其能够有效参与协作和谈判等现实社会任务。强化学习（RL）适合训练社会智能体，因为它允许模型通过社交互动直接学习复杂策略，而无需人类标注。然而，社会智能任务存在两个独特之处：一是社交互动中个体发言的质量与最终成功并不严格相关；二是社交互动需要多维度的成功标准。因此，本文提出Sotopia-RL，一个新颖的框架，将粗略的情节级反馈细化为发言级的多维奖励，以促进社会智能任务的RL训练。实验结果表明，Sotopia-RL在Sotopia环境中实现了最先进的社会目标完成分数，显著超越现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决社会智能任务中奖励设计的不足，现有方法未能有效处理个体发言与最终成功之间的关系，以及多维度成功标准的需求。

**核心思路**：Sotopia-RL通过将粗略的情节级反馈细化为发言级的多维奖励，允许模型在社交互动中进行更精确的信用分配，从而提升学习效果。

**技术框架**：该框架包括多个模块，首先收集社交互动数据，然后通过算法将情节级反馈转化为发言级奖励，最后进行强化学习训练以优化模型策略。

**关键创新**：最重要的创新在于发言级信用分配和多维奖励设计的结合，这与传统方法的单一奖励机制形成鲜明对比，能够更全面地捕捉社交互动的复杂性。

**关键设计**：在设计中，采用了多维度的奖励函数，确保能够反映社交互动的多样性，同时设置了适应性损失函数，以优化模型在不同情境下的表现。

## 📊 实验亮点

实验结果表明，Sotopia-RL在Sotopia环境中取得了7.17的Sotopia-hard和8.31的Sotopia-full社会目标完成分数，显著超过了现有方法，展示了其在社会智能任务中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、虚拟助手和在线协作平台等，能够提升这些系统在复杂社交环境中的表现和适应能力。未来，Sotopia-RL可能推动更智能的社交AI的发展，使其在实际应用中更具人性化和有效性。

## 📄 摘要（原文）

> Social intelligence has become a critical capability for large language models (LLMs), enabling them to engage effectively in real-world social tasks such as collaboration and negotiation. Reinforcement learning (RL) is a natural fit for training socially intelligent agents because it allows models to learn sophisticated strategies directly through social interactions without requiring human annotations. However, there are two unique parts about social intelligence tasks: (1) the quality of individual utterances in social interactions is not strictly related to final success; (2) social interactions require multi-dimensional rubrics for success. Therefore, we argue that it is necessary to design rewards for building utterance-level multi-dimensional reward models to facilitate RL training for social intelligence tasks. To address these challenges, we propose Sotopia-RL, a novel framework that refines coarse episode-level feedback into utterance-level, multi-dimensional rewards. Utterance-level credit assignment attributes outcomes to individual utterances, while multi-dimensional rewards capture the full richness of social interactions and reduce reward hacking. Experiments in Sotopia, an open-ended social learning environment, demonstrate that Sotopia-RL achieves state-of-the-art social goal completion scores (7.17 on Sotopia-hard and 8.31 on Sotopia-full), significantly outperforming existing approaches. Ablation studies confirm the necessity of both utterance-level credit assignment and multi-dimensional reward design for RL training.

