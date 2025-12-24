---
layout: default
title: "Nested-ReFT: Efficient Reinforcement Learning for Large Language Model Fine-Tuning via Off-Policy Rollouts"
---

# Nested-ReFT: Efficient Reinforcement Learning for Large Language Model Fine-Tuning via Off-Policy Rollouts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10123" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10123v2</a>
  <a href="https://arxiv.org/pdf/2508.10123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10123v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10123v2', 'Nested-ReFT: Efficient Reinforcement Learning for Large Language Model Fine-Tuning via Off-Policy Rollouts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maxime Heuillet, Yufei Cui, Boxing Chen, Audrey Durand, Prasanna Parthasarathi

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-13 (更新: 2025-11-22)

---

## 💡 一句话要点

**提出Nested-ReFT以解决大语言模型微调的高计算成本问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大语言模型` `微调` `计算效率` `数学推理` `离线策略` `动态层选择`

## 📋 核心要点

1. 现有的ReFT方法在训练过程中需要多次推理，导致计算成本高昂，限制了其应用。
2. Nested-ReFT通过部分层作为行为模型生成离线策略的完成，降低了推理成本，提升了训练效率。
3. 实验证明，Nested-ReFT在多个数学推理基准上表现出更高的计算效率，提升幅度显著。

## 📝 摘要（中文）

在复杂领域如数学推理中，先进的推理能力可以通过可验证奖励的强化微调（ReFT）来实现。传统ReFT框架中，行为模型为每个问题生成多个答案，随后通过奖励函数进行评分。然而，这种方法在训练过程中需要多次推理，导致计算成本显著。为了解决这一问题，本文提出了一种新颖的ReFT框架Nested-ReFT，利用目标模型的部分层作为行为模型，在训练期间生成离线策略的完成，从而降低推理成本。理论分析表明，Nested-ReFT能够提供无偏的梯度估计，并控制方差。实证分析显示，在多个数学推理基准和模型规模上，计算效率得到了显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决传统ReFT方法在训练过程中高昂的计算成本问题。现有方法需要多次推理生成答案，导致效率低下。

**核心思路**：Nested-ReFT的核心思想是利用目标模型的部分层作为行为模型，生成离线策略的完成，从而减少推理步骤，降低计算负担。

**技术框架**：整体架构包括行为模型和目标模型，行为模型在训练期间动态选择层进行推理，生成多个答案供后续评分。

**关键创新**：Nested-ReFT的主要创新在于引入了动态层跳过机制，使得推理过程更加高效，同时保持无偏的梯度估计。

**关键设计**：在设计中，采用了动态层选择的策略，确保在每个批次中根据需要选择不同的层进行推理，优化了计算资源的使用。

## 📊 实验亮点

实验结果表明，Nested-ReFT在多个数学推理基准上实现了显著的计算效率提升，具体表现为每秒处理的token数量大幅增加，且在性能上与基线ReFT方法相当，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和科学研究等需要复杂推理的场景。通过提高大语言模型在这些领域的推理能力，Nested-ReFT能够为决策支持和自动化分析提供更高效的解决方案，未来可能对相关行业产生深远影响。

## 📄 摘要（原文）

> Advanced reasoning in LLMs on challenging domains like mathematical reasoning can be tackled using verifiable rewards based reinforced fine-tuning (ReFT). In standard ReFT frameworks, a behavior model generates multiple completions with answers per problem, for the answer to be then scored by a reward function. While such RL post-training methods demonstrate significant performance improvements across challenging reasoning domains, the computational cost of generating completions during training with multiple inference steps makes the training cost non-trivial. To address this, we draw inspiration from off-policy RL, and speculative decoding to introduce a novel ReFT framework, dubbed Nested-ReFT, where a subset of layers of the target model acts as the behavior model to generate off-policy completions during training. The behavior model configured with dynamic layer skipping per batch during training decreases the inference cost compared to the standard ReFT frameworks. Our theoretical analysis shows that Nested-ReFT yields unbiased gradient estimates with controlled variance. Our empirical analysis demonstrates improved computational efficiency measured as tokens/sec across multiple math reasoning benchmarks and model sizes. Additionally, we explore three variants of bias mitigation to minimize the off-policyness in the gradient updates that allows for maintaining performance that matches the baseline ReFT performance.

