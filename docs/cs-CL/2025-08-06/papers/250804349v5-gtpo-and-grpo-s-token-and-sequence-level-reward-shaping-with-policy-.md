---
layout: default
title: "GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy"
---

# GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04349" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04349v5</a>
  <a href="https://arxiv.org/pdf/2508.04349.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04349v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04349v5', 'GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongze Tan, Jianfei Pan, Jinghao Lin, Tao Chen, Zhihang Zheng, Zhihao Tang, Haihua Yang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-06 (更新: 2025-09-26)

---

## 💡 一句话要点

**提出动态熵加权机制以解决长链推理中的奖励分配问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `动态熵加权` `长链推理` `奖励塑造` `大型语言模型`

## 📋 核心要点

1. 现有强化学习方法在长链推理任务中存在粗粒度奖励分配的问题，无法有效区分各个标记的贡献。
2. 本文提出动态熵加权机制，通过GTPO和GRPO-S算法实现对每个标记的熵加权奖励，提升奖励分配的精细度。
3. 实验结果显示，所提方法在多个推理基准上显著超越DAPO基线，验证了熵加权机制的有效性。

## 📝 摘要（中文）

强化学习（RL）在提升大型语言模型（LLM）推理能力方面至关重要。然而，传统算法通常采用粗粒度的奖励分配方式，对序列中的所有标记施加统一奖励，这在长链推理任务中存在显著缺陷。本文提出动态熵加权机制，通过两种新算法：组标记策略优化（GTPO）和序列级GRPO（GRPO-S），实现对每个标记的细粒度奖励分配。我们假设推理路径中的高策略熵是认知努力的重要启示，可以转化为学习信号。实验结果表明，我们的方法在多个推理基准上显著优于强基线DAPO，验证了熵加权机制是性能提升的关键驱动因素。

## 🔬 方法详解

**问题定义**：本文旨在解决传统强化学习方法在长链推理任务中对奖励的粗粒度分配问题，导致无法准确评估每个标记的贡献。

**核心思路**：提出动态熵加权机制，通过对每个标记分配基于熵的奖励，利用高策略熵作为认知努力的启示，转化为有效的学习信号。

**技术框架**：整体架构包括两个主要模块：GTPO和GRPO-S。GTPO为每个标记分配熵加权奖励，而GRPO-S则在序列级别进行类似的处理。

**关键创新**：最重要的创新在于将策略熵用于奖励塑造，实现真正的逐标记信用分配，与传统方法的统一奖励机制形成鲜明对比。

**关键设计**：在算法设计中，关键参数包括熵权重的计算方式和奖励函数的构建，确保能够有效反映每个标记在推理过程中的重要性。

## 📊 实验亮点

实验结果表明，所提GTPO和GRPO-S方法在多个推理基准上显著优于DAPO基线，提升幅度达到XX%，验证了熵加权机制在奖励分配中的关键作用。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能问答等。通过提升长链推理能力，能够显著改善模型在复杂任务中的表现，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Reinforcement learning (RL) is a pivotal task for enhancing Large Language Model (LLM) reasoning. Conventional algorithms, however, typically adhere to a coarse-grained credit assignment paradigm, applying a uniform reward to all tokens in a sequence, a critical flaw in long-chain reasoning tasks. In this paper, we address this challenge and propose Dynamic Entropy Weighting, a novel mechanism that facilitates fine-grained rewards through two new algorithms: Group Token Policy Optimization (GTPO), which assigns an entropy-weighted reward to each token, and the analogous algorithm Sequence-Level GRPO (GRPO-S). Our approach is founded on the hypothesis that high policy entropy within a reasoning path is a powerful heuristic for cognitive effort at pivotal junctures, which can be repurposed into a learning signal. By repurposing policy entropy for reward shaping, we achieve true per-token credit assignment. Experimental results across challenging reasoning benchmarks validate the superiority of our approach, showing our methods significantly outperform a strong DAPO baseline and confirming our entropy-weighting mechanism as the key driver of this performance boost.

