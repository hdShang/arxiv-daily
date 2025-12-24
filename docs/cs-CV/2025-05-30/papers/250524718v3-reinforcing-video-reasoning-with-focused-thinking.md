---
layout: default
title: Reinforcing Video Reasoning with Focused Thinking
---

# Reinforcing Video Reasoning with Focused Thinking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24718" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24718v3</a>
  <a href="https://arxiv.org/pdf/2505.24718.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24718v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24718v3', 'Reinforcing Video Reasoning with Focused Thinking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jisheng Dang, Jingze Wu, Teng Wang, Xuanhui Lin, Nannan Zhu, Hongbo Chen, Wei-Shi Zheng, Meng Wang, Tat-Seng Chua

**分类**: cs.CV

**发布日期**: 2025-05-30 (更新: 2025-06-08)

**🔗 代码/项目**: [GITHUB](https://github.com/longmalongma/TW-GRPO)

---

## 💡 一句话要点

**提出TW-GRPO以解决视频推理中的无效链条和奖励稀疏问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频推理` `强化学习` `多模态模型` `信息加权` `奖励机制` `数据增强` `深度学习`

## 📋 核心要点

1. 现有方法在视频推理中产生冗长且无效的推理链条，难以聚焦于重要的时空信息。
2. 提出TW-GRPO框架，通过令牌加权机制和多选题训练，提升推理的聚焦性和奖励的细粒度。
3. TW-GRPO在CLEVRER和MMVU基准上分别取得了50.4%和65.8%的准确率，显著提升了性能。

## 📝 摘要（中文）

近年来，强化学习的进展，特别是通过群体相对策略优化（GRPO），显著提升了多模态大语言模型在复杂推理任务中的表现。然而，仍存在两个关键限制：一是推理链条往往冗长且缺乏聚焦，遮蔽了重要的时空线索；二是二元奖励机制未能考虑部分正确答案，导致奖励方差高、学习效率低。本文提出了TW-GRPO，一个通过聚焦思维和密集奖励粒度增强视觉推理的新框架。具体而言，我们采用了一个令牌加权机制，优先考虑信息密度高的令牌，抑制冗余令牌。此外，我们将强化学习训练从单选题转变为多选题，利用软奖励实现更细粒度的梯度估计。实验结果表明，TW-GRPO在多个视频推理和通用理解基准上表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频推理方法中推理链条冗长且奖励机制稀疏的问题。现有方法往往无法有效聚焦于重要的时空线索，导致学习效率低下。

**核心思路**：TW-GRPO框架通过引入令牌加权机制，优先考虑信息密度高的令牌，从而抑制冗余信息的干扰。同时，将训练任务从单选题转变为多选题，以实现更细致的奖励反馈。

**技术框架**：TW-GRPO的整体架构包括令牌加权模块和多选题训练模块。令牌加权模块通过计算信息熵来评估令牌的重要性，而多选题训练模块则通过软奖励机制来优化学习过程。

**关键创新**：最重要的创新在于令牌加权机制和多选题训练的结合，这一设计使得模型能够更有效地聚焦于关键信息，并在奖励反馈上实现更细致的区分。

**关键设计**：在参数设置上，采用了基于信息熵的令牌加权策略，损失函数设计上引入了软奖励机制，以支持部分正确答案的评估。

## 📊 实验亮点

TW-GRPO在多个基准测试中表现出色，特别是在CLEVRER上达到了50.4%的准确率，相较于Video-R1提高了18.8%；在MMVU上则达到了65.8%的准确率，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括视频理解、智能监控和自动驾驶等场景。通过提升视频推理的准确性和效率，TW-GRPO能够为多模态交互系统提供更强的支持，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Recent advancements in reinforcement learning, particularly through Group Relative Policy Optimization (GRPO), have significantly improved multimodal large language models for complex reasoning tasks. However, two critical limitations persist: 1) they often produce unfocused, verbose reasoning chains that obscure salient spatiotemporal cues and 2) binary rewarding fails to account for partially correct answers, resulting in high reward variance and inefficient learning. In this paper, we propose TW-GRPO, a novel framework that enhances visual reasoning with focused thinking and dense reward granularity. Specifically, we employs a token weighting mechanism that prioritizes tokens with high informational density (estimated by intra-group information entropy), suppressing redundant tokens like generic reasoning prefixes. Furthermore, we reformulate RL training by shifting from single-choice to multi-choice QA tasks, where soft rewards enable finer-grained gradient estimation by distinguishing partial correctness. Additionally, we propose question-answer inversion, a data augmentation strategy to generate diverse multi-choice samples from existing benchmarks. Experiments demonstrate state-of-the-art performance on several video reasoning and general understanding benchmarks. Notably, TW-GRPO achieves 50.4\% accuracy on CLEVRER (18.8\% improvement over Video-R1) and 65.8\% on MMVU. Our codes are available at \href{https://github.com/longmalongma/TW-GRPO}.

