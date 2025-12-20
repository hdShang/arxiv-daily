---
layout: default
title: JustRL: Scaling a 1.5B LLM with a Simple RL Recipe
---

# JustRL: Scaling a 1.5B LLM with a Simple RL Recipe

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16649" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16649v1</a>
  <a href="https://arxiv.org/pdf/2512.16649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16649v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16649v1', 'JustRL: Scaling a 1.5B LLM with a Simple RL Recipe')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingxiang He, Zekai Qu, Zeyuan Liu, Yinghao Chen, Yuxin Zuo, Cheng Qian, Kaiyan Zhang, Weize Chen, Chaojun Xiao, Ganqu Cui, Ning Ding, Zhiyuan Liu

**分类**: cs.CL

**发布日期**: 2025-12-18

**备注**: 12 pages, 3 figures

---

## 💡 一句话要点

**JustRL：通过简单强化学习方法扩展15亿参数LLM，实现数学推理SOTA**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `数学推理` `单阶段训练` `超参数优化`

## 📋 核心要点

1. 现有LLM强化学习方法过度复杂，依赖多阶段训练和动态超参数，缺乏对必要性的深入分析。
2. JustRL采用单阶段训练和固定超参数，简化了训练流程，并实现了优异的性能。
3. 实验表明，JustRL在数学推理任务上超越现有方法，且计算成本更低，并揭示了某些“标准技巧”可能适得其反。

## 📝 摘要（中文）

大型语言模型（LLM）的强化学习研究日益复杂，包括多阶段训练流程、动态超参数调整和课程学习策略。本文质疑这种复杂性是否必要，并提出了JustRL，一种极简方法，采用单阶段训练和固定超参数，在两个15亿参数的推理模型上实现了最先进的性能（在九个数学基准测试中平均准确率分别为54.9％和64.3％），同时计算量比复杂方法少2倍。相同的超参数无需调整即可在两个模型之间迁移，并且训练过程表现出平稳的单调改进，超过4,000个步骤，没有通常需要干预的崩溃或平台期。关键的是，消融实验表明，添加诸如显式长度惩罚和鲁棒验证器之类的“标准技巧”可能会因探索崩溃而降低性能。这些结果表明，该领域可能正在增加复杂性来解决可以通过稳定、扩展的基线来解决的问题。我们发布了我们的模型和代码，以建立一个简单、经过验证的社区基线。

## 🔬 方法详解

**问题定义**：现有基于强化学习的LLM训练方法，为了提升性能，往往引入了复杂的多阶段训练流程、动态调整的超参数以及课程学习策略。然而，这些复杂性是否真正必要，以及它们带来的收益是否超过了其引入的额外成本，是值得探讨的问题。现有方法的痛点在于训练流程复杂、计算资源消耗大，且难以调试和复现。

**核心思路**：JustRL的核心思路是回归简单，通过采用单阶段训练和固定的超参数，避免了复杂流程带来的问题。作者认为，通过稳定且规模化的训练，可以解决现有方法中需要复杂技巧才能解决的问题。这种方法旨在证明，在适当的规模下，简单的强化学习方法也能达到甚至超过复杂方法的效果。

**技术框架**：JustRL的技术框架非常简洁。它使用一个标准的强化学习流程，包括：1）使用LLM生成候选答案；2）使用奖励模型评估答案质量；3）使用强化学习算法（例如PPO）更新LLM的参数。整个训练过程在一个阶段内完成，并且超参数在整个训练过程中保持不变。

**关键创新**：JustRL最重要的创新点在于其对“简单性”的强调。它挑战了当前LLM强化学习领域追求复杂性的趋势，并证明了通过简单的训练方法也能达到SOTA性能。此外，该研究还通过消融实验发现，一些常用的技巧（如长度惩罚和鲁棒验证器）实际上可能会降低性能，这进一步强调了简单性的重要性。

**关键设计**：JustRL的关键设计在于其超参数的选择和奖励函数的设计。作者通过实验找到了一个适用于不同模型的超参数组合，并使用了一个简单的奖励函数来评估答案的质量。具体来说，奖励函数基于答案的正确性，并可能包含一些简单的惩罚项（例如，对过长答案的惩罚）。此外，作者还仔细选择了训练数据，以确保模型的训练效果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16649v1/figures/fig1_aime24_curves_added.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16649v1/figures/fig2_training_dynamics.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16649v1/figures/fig3_training_dynamics.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

JustRL在两个15亿参数的推理模型上实现了SOTA性能，在九个数学基准测试中平均准确率分别达到54.9％和64.3％，同时计算量比复杂方法少2倍。消融实验表明，添加显式长度惩罚和鲁棒验证器等“标准技巧”可能会降低性能。相同的超参数无需调整即可在两个模型之间迁移。

## 🎯 应用场景

JustRL的潜在应用领域包括各种需要语言模型进行推理和决策的任务，例如数学问题求解、代码生成、对话系统等。该研究的实际价值在于提供了一种更简单、更高效的LLM训练方法，降低了训练成本，并促进了LLM在更广泛领域的应用。未来，JustRL可以作为LLM强化学习的一个强大基线，并为后续研究提供参考。

## 📄 摘要（原文）

> Recent advances in reinforcement learning for large language models have converged on increasing complexity: multi-stage training pipelines, dynamic hyperparameter schedules, and curriculum learning strategies. This raises a fundamental question: \textbf{Is this complexity necessary?} We present \textbf{JustRL}, a minimal approach using single-stage training with fixed hyperparameters that achieves state-of-the-art performance on two 1.5B reasoning models (54.9\% and 64.3\% average accuracy across nine mathematical benchmarks) while using 2$\times$ less compute than sophisticated approaches. The same hyperparameters transfer across both models without tuning, and training exhibits smooth, monotonic improvement over 4,000+ steps without the collapses or plateaus that typically motivate interventions. Critically, ablations reveal that adding ``standard tricks'' like explicit length penalties and robust verifiers may degrade performance by collapsing exploration. These results suggest that the field may be adding complexity to solve problems that disappear with a stable, scaled-up baseline. We release our models and code to establish a simple, validated baseline for the community.

