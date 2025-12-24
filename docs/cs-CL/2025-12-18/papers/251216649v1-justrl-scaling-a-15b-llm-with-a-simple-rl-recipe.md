---
layout: default
title: "JustRL: Scaling a 1.5B LLM with a Simple RL Recipe"
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

**关键词**: `强化学习` `大型语言模型` `数学推理` `单阶段训练` `固定超参数`

## 📋 核心要点

1. 现有LLM强化学习方法过于复杂，包含多阶段训练和动态超参数调整，缺乏对必要性的深入研究。
2. JustRL采用单阶段训练和固定超参数，避免复杂调整，旨在探索简化强化学习流程在LLM中的潜力。
3. 实验表明，JustRL在数学推理任务上达到SOTA，且计算量更少，证明了简单方法的可行性与优越性。

## 📝 摘要（中文）

大型语言模型（LLM）的强化学习研究日益复杂，包括多阶段训练流程、动态超参数调整和课程学习策略。本文质疑这种复杂性是否必要，并提出了JustRL，一种极简方法，使用单阶段训练和固定超参数，在两个15亿参数的推理模型上实现了最先进的性能（在九个数学基准测试中平均准确率分别为54.9％和64.3％），同时计算量比复杂方法少2倍。相同的超参数无需调整即可在两个模型之间迁移，并且训练过程表现出平稳的单调改进，超过4,000步，没有通常需要干预的崩溃或停滞。关键的是，消融实验表明，添加诸如显式长度惩罚和鲁棒验证器之类的“标准技巧”可能会因崩溃探索而降低性能。这些结果表明，该领域可能正在增加复杂性来解决可以通过稳定、扩展的基线来解决的问题。我们发布了我们的模型和代码，以建立一个简单、经过验证的社区基线。

## 🔬 方法详解

**问题定义**：现有的大型语言模型强化学习方法通常采用复杂的多阶段训练流程、动态调整的超参数以及课程学习策略。这些复杂性使得训练过程难以理解和优化，并且需要大量的计算资源。论文旨在解决的问题是：是否必须采用如此复杂的强化学习方法才能训练出高性能的LLM？现有方法的痛点在于其复杂性和计算成本。

**核心思路**：论文的核心思路是采用一种极简的强化学习方法，即JustRL。JustRL使用单阶段训练和固定的超参数，避免了复杂的调整过程。作者认为，通过稳定和扩展的基线，可以解决一些原本需要复杂方法才能解决的问题。这种方法旨在降低计算成本，并提高训练过程的可理解性。

**技术框架**：JustRL的技术框架非常简单，主要包括以下几个步骤：首先，使用一个预训练的1.5B参数的LLM作为基础模型。然后，使用强化学习算法（具体算法未明确说明，但暗示是常见的策略梯度方法）对模型进行微调。在训练过程中，使用固定的超参数，并且只进行单阶段的训练。最后，对训练好的模型进行评估，并在数学推理基准测试上进行性能测试。

**关键创新**：JustRL最重要的技术创新点在于其极简的设计理念。与现有方法相比，JustRL避免了复杂的多阶段训练流程和动态超参数调整，从而降低了计算成本，并提高了训练过程的可理解性。此外，论文还发现，一些常用的“标准技巧”，如显式长度惩罚和鲁棒验证器，可能会降低性能，这与现有认知有所不同。

**关键设计**：JustRL的关键设计在于其单阶段训练和固定超参数。作者通过实验证明，使用相同的超参数可以在不同的模型之间迁移，并且训练过程表现出平稳的单调改进。此外，作者还进行了消融实验，以评估不同技术细节对性能的影响。具体的技术细节包括损失函数的设计、奖励函数的设计以及探索策略的选择（虽然论文没有明确说明，但这些都是强化学习中需要考虑的关键因素）。

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

JustRL在两个15亿参数的推理模型上实现了最先进的性能，在九个数学基准测试中平均准确率分别达到54.9％和64.3％，同时计算量比复杂方法少2倍。消融实验表明，添加显式长度惩罚和鲁棒验证器等“标准技巧”可能会降低性能。相同的超参数无需调整即可在两个模型之间迁移，训练过程表现出平稳的单调改进。

## 🎯 应用场景

JustRL的潜在应用领域包括各种需要复杂推理和决策能力的自然语言处理任务，例如数学问题求解、代码生成、对话系统等。该研究的实际价值在于降低了训练高性能LLM的计算成本，并提高了训练过程的可理解性。未来，JustRL可以作为一种简单有效的基线方法，用于评估和改进其他更复杂的强化学习方法。

## 📄 摘要（原文）

> Recent advances in reinforcement learning for large language models have converged on increasing complexity: multi-stage training pipelines, dynamic hyperparameter schedules, and curriculum learning strategies. This raises a fundamental question: \textbf{Is this complexity necessary?} We present \textbf{JustRL}, a minimal approach using single-stage training with fixed hyperparameters that achieves state-of-the-art performance on two 1.5B reasoning models (54.9\% and 64.3\% average accuracy across nine mathematical benchmarks) while using 2$\times$ less compute than sophisticated approaches. The same hyperparameters transfer across both models without tuning, and training exhibits smooth, monotonic improvement over 4,000+ steps without the collapses or plateaus that typically motivate interventions. Critically, ablations reveal that adding ``standard tricks'' like explicit length penalties and robust verifiers may degrade performance by collapsing exploration. These results suggest that the field may be adding complexity to solve problems that disappear with a stable, scaled-up baseline. We release our models and code to establish a simple, validated baseline for the community.

