---
layout: default
title: "Towards Hallucination-Free Music: A Reinforcement Learning Preference Optimization Framework for Reliable Song Generation"
---

# Towards Hallucination-Free Music: A Reinforcement Learning Preference Optimization Framework for Reliable Song Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.05011" class="toolbar-btn" target="_blank">📄 arXiv: 2508.05011v1</a>
  <a href="https://arxiv.org/pdf/2508.05011.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.05011v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.05011v1', 'Towards Hallucination-Free Music: A Reinforcement Learning Preference Optimization Framework for Reliable Song Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huaicheng Zhang, Wei Tan, Guangzheng Li, Yixuan Zhang, Hangting Chen, Shun Lei, Chenyu Yang, Zhiyong Wu, Shuai Wang, Qijun Huang, Dong Yu

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-08-07

---

## 💡 一句话要点

**提出基于强化学习的偏好优化框架以解决音乐生成中的幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `音乐生成` `强化学习` `偏好优化` `内容幻觉` `音素错误率` `自动作曲` `生成模型`

## 📋 核心要点

1. 现有的歌词到歌曲生成模型常常出现内容幻觉，导致生成结果与输入歌词不一致，影响音乐的连贯性。
2. 本文提出了一种基于强化学习的偏好优化框架，通过构建幻觉偏好数据集和实现多种优化策略来控制幻觉现象。
3. 实验结果显示，DPO策略实现了7.4%的音素错误率（PER）降低，而PPO和GRPO分别降低了4.9%和4.7%，有效提升了生成质量。

## 📝 摘要（中文）

近年来，基于音频的生成语言模型在歌词到歌曲生成方面取得了显著进展。然而，这些模型常常遭遇内容幻觉，导致生成的输出与输入歌词不一致，影响音乐的连贯性。现有的监督微调方法由于被动标签拟合的限制，自我改进能力不足，幻觉缓解效果不佳。为了解决这一核心挑战，本文提出了一种新颖的强化学习框架，利用偏好优化进行幻觉控制。主要贡献包括：构建了一个稳健的幻觉偏好数据集，通过音素错误率计算和基于规则的过滤来捕捉与人类期望的对齐；在强化学习框架中实现并评估了三种不同的偏好优化策略，分别为直接偏好优化（DPO）、近端策略优化（PPO）和组相对策略优化（GRPO）。实验结果表明，所提方法有效抑制了幻觉现象，同时保持了音乐质量。

## 🔬 方法详解

**问题定义**：本文旨在解决歌词到歌曲生成中的内容幻觉问题，现有的监督微调方法在幻觉缓解方面表现不佳，缺乏有效的自我改进机制。

**核心思路**：提出基于强化学习的偏好优化框架，通过构建幻觉偏好数据集，利用人类期望对生成内容进行优化，从而控制幻觉现象。

**技术框架**：整体框架包括数据集构建、偏好优化策略实现（DPO、PPO、GRPO）和基于PER的奖励模型训练，形成一个闭环优化过程。

**关键创新**：最重要的创新在于通过强化学习实现对幻觉的系统性控制，尤其是DPO策略的引入，显著提升了生成内容的质量。

**关键设计**：在DPO中，采用离线策略增强正向标记的可能性；PPO和GRPO则通过在线策略训练PER基础的奖励模型，结合奖励最大化和KL正则化进行序列优化。具体参数设置和损失函数设计在实验中进行了详细评估。

## 📊 实验亮点

实验结果显示，DPO策略在幻觉控制方面表现优异，实现了7.4%的音素错误率降低，而PPO和GRPO分别降低了4.9%和4.7%。这些结果表明，所提方法在抑制幻觉的同时，保持了音乐的整体质量。

## 🎯 应用场景

该研究的潜在应用领域包括音乐创作、自动作曲和歌词生成等，能够为音乐创作提供更高质量的生成工具。未来，该框架还可扩展到不同音乐风格的生成和音乐性增强，推动生成音乐研究的发展。

## 📄 摘要（原文）

> Recent advances in audio-based generative language models have accelerated AI-driven lyric-to-song generation. However, these models frequently suffer from content hallucination, producing outputs misaligned with the input lyrics and undermining musical coherence. Current supervised fine-tuning (SFT) approaches, limited by passive label-fitting, exhibit constrained self-improvement and poor hallucination mitigation. To address this core challenge, we propose a novel reinforcement learning (RL) framework leveraging preference optimization for hallucination control. Our key contributions include: (1) Developing a robust hallucination preference dataset constructed via phoneme error rate (PER) computation and rule-based filtering to capture alignment with human expectations; (2) Implementing and evaluating three distinct preference optimization strategies within the RL framework: Direct Preference Optimization (DPO), Proximal Policy Optimization (PPO), and Group Relative Policy Optimization (GRPO). DPO operates off-policy to enhance positive token likelihood, achieving a significant 7.4% PER reduction. PPO and GRPO employ an on-policy approach, training a PER-based reward model to iteratively optimize sequences via reward maximization and KL-regularization, yielding PER reductions of 4.9% and 4.7%, respectively. Comprehensive objective and subjective evaluations confirm that our methods effectively suppress hallucinations while preserving musical quality. Crucially, this work presents a systematic, RL-based solution to hallucination control in lyric-to-song generation. The framework's transferability also unlocks potential for music style adherence and musicality enhancement, opening new avenues for future generative song research.

