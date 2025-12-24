---
layout: default
title: Accelerating RL for LLM Reasoning with Optimal Advantage Regression
---

# Accelerating RL for LLM Reasoning with Optimal Advantage Regression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20686" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20686v1</a>
  <a href="https://arxiv.org/pdf/2505.20686.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20686v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20686v1', 'Accelerating RL for LLM Reasoning with Optimal Advantage Regression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kianté Brantley, Mingyu Chen, Zhaolin Gao, Jason D. Lee, Wen Sun, Wenhao Zhan, Xuezhou Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-27

**🔗 代码/项目**: [GITHUB](https://github.com/ZhaolinGao/A-PO)

---

## 💡 一句话要点

**提出A*-PO以解决RL在LLM推理中的高计算开销问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `推理能力` `政策优化` `最优优势函数` `最小二乘回归` `KL正则化` `计算效率`

## 📋 核心要点

1. 现有的政策优化方法在强化学习中面临高计算开销和内存消耗的问题，限制了其在大型语言模型推理中的应用。
2. 本文提出的A*-PO框架通过两阶段策略优化，直接近似最优优势函数，显著提高了训练效率。
3. 实验结果显示，A*-PO在多个数学推理基准上表现优异，训练时间减少最多2倍，内存使用降低超过30%。

## 📝 摘要（中文）

强化学习（RL）已成为微调大型语言模型（LLMs）以提升复杂推理能力的有效工具。然而，现有的政策优化方法通常面临高计算开销和内存消耗的问题，主要由于每个提示需要多次生成以及依赖于当前政策的评论网络或优势估计。本文提出了一种新颖的两阶段政策优化框架A*-PO，该框架直接近似最优优势函数，从而实现LLMs在推理任务中的高效训练。通过离线采样参考政策来估计最优价值函数，消除了昂贵的在线价值估计需求，并在第二阶段使用简单的最小二乘回归损失进行在线更新。理论上，我们建立了性能保证，并证明KL正则化的RL目标可以在不需要复杂探索策略的情况下进行优化。实证结果表明，A*-PO在多种数学推理基准上表现出竞争力，同时训练时间减少了最多2倍，峰值内存使用减少超过30%。

## 🔬 方法详解

**问题定义**：本文旨在解决强化学习在大型语言模型推理任务中面临的高计算开销和内存消耗问题。现有方法需要多次生成和复杂的评论网络，导致效率低下。

**核心思路**：A*-PO框架的核心思想是通过两阶段优化，第一阶段利用离线采样来估计最优价值函数，第二阶段则通过简单的最小二乘回归进行在线更新，从而减少计算需求。

**技术框架**：A*-PO的整体架构分为两个主要阶段：第一阶段进行离线采样以估计最优价值函数V*，第二阶段进行基于单次生成的在线更新，使用最小二乘回归损失进行优化。

**关键创新**：A*-PO的最大创新在于其直接近似最优优势函数的能力，避免了复杂的在线价值估计和探索策略，与现有方法相比显著提高了训练效率。

**关键设计**：在设计中，A*-PO采用了KL正则化的RL目标，确保了优化过程的稳定性，并通过简单的损失函数设计降低了计算复杂度。

## 📊 实验亮点

实验结果表明，A*-PO在多个数学推理基准上达到了竞争力的性能，相较于PPO、GRPO和REBEL，训练时间减少最多2倍，峰值内存使用降低超过30%，显示出其在效率和效果上的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动推理等。通过提高大型语言模型的推理能力，A*-PO能够在教育、金融、医疗等多个行业中提供更高效的智能解决方案，推动AI技术的实际应用和发展。

## 📄 摘要（原文）

> Reinforcement learning (RL) has emerged as a powerful tool for fine-tuning large language models (LLMs) to improve complex reasoning abilities. However, state-of-the-art policy optimization methods often suffer from high computational overhead and memory consumption, primarily due to the need for multiple generations per prompt and the reliance on critic networks or advantage estimates of the current policy. In this paper, we propose $A$*-PO, a novel two-stage policy optimization framework that directly approximates the optimal advantage function and enables efficient training of LLMs for reasoning tasks. In the first stage, we leverage offline sampling from a reference policy to estimate the optimal value function $V$*, eliminating the need for costly online value estimation. In the second stage, we perform on-policy updates using a simple least-squares regression loss with only a single generation per prompt. Theoretically, we establish performance guarantees and prove that the KL-regularized RL objective can be optimized without requiring complex exploration strategies. Empirically, $A$*-PO achieves competitive performance across a wide range of mathematical reasoning benchmarks, while reducing training time by up to 2$\times$ and peak memory usage by over 30% compared to PPO, GRPO, and REBEL. Implementation of $A$*-PO can be found at https://github.com/ZhaolinGao/A-PO.

