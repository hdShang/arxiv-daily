---
layout: default
title: "GRPO-$λ$: Credit Assignment improves LLM Reasoning"
---

# GRPO-$λ$: Credit Assignment improves LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00194" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00194v1</a>
  <a href="https://arxiv.org/pdf/2510.00194.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00194v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00194v1', 'GRPO-$λ$: Credit Assignment improves LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prasanna Parthasarathi, Mathieu Reymond, Boxing Chen, Yufei Cui, Sarath Chandar

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**GRPO-λ：通过改进信用分配提升大型语言模型推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `信用分配` `推理能力` `资格迹`

## 📋 核心要点

1. 现有GRPO方法在大型语言模型推理任务中表现出色，但缺乏细粒度的信用分配机制，限制了其性能。
2. GRPO-λ通过引入基于资格迹的λ-return近似，以及无评论家的时间差分误差估计，增强了token级别的信用分配。
3. 实验结果表明，GRPO-λ在多个数学推理数据集上显著优于GRPO，性能提升高达30-40%，并在多个基准测试中取得了更高的分数。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被部署于需要复杂推理的任务中，这激发了人们对通过后训练来提高其推理能力的极大兴趣。特别是基于强化学习（RL）并使用可验证奖励的方法，如最先进的GRPO，在作为后训练方法应用时，已经显示出极大地改善推理行为。然而，缺乏显式的奖励或评论家模型限制了GRPO在token序列中进行细粒度信用分配的能力。本文提出了GRPO-λ，这是GRPO的一个新扩展，旨在增强LLM在复杂推理任务的RL微调中的信用分配。我们通过在使用token级别对数概率的资格迹（eligibility traces）进行重新公式化，以及对时间差分误差进行新颖的无评论家近似，来近似从λ-return中学习。我们引入了λ-return加权的一些变体，以及它们在资格迹中的应用，所有这些变体都比GRPO提供了显著的增益。我们将GRPO-λ与GRPO进行了比较，通过在4个不同的数学推理数据集上训练参数从1.5B到7B的模型。训练曲线表明，在LLaMA-3.1和Qwen-2.5架构上，RL训练期间的性能提高了30-40%。最后，我们表明，使用GRPO-λ，在AIME24、Math500、OlympiadMath、MinervaMath和AMC上的平均性能比GRPO提高了3个多点，并且在7B模型上提高了4.5个点。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在复杂推理任务中，使用强化学习进行微调时，信用分配不明确的问题。现有方法，如GRPO，虽然能够利用可验证的奖励来提升推理能力，但缺乏对token序列中每个token贡献的细粒度评估，导致学习效率降低。

**核心思路**：论文的核心思路是通过引入λ-return的概念，并结合资格迹（eligibility traces）来近似计算每个token对最终奖励的贡献。同时，为了避免引入额外的评论家模型，论文提出了一种无评论家的时间差分误差估计方法，从而在不增加计算复杂度的前提下，实现更精确的信用分配。

**技术框架**：GRPO-λ的整体框架仍然基于GRPO，但在奖励计算和反向传播阶段进行了改进。具体来说，在生成token序列后，首先计算每个token的对数概率。然后，利用这些对数概率和λ-return的近似值，计算资格迹。最后，使用资格迹来更新模型参数，从而实现更有效的强化学习微调。

**关键创新**：GRPO-λ的关键创新在于：1) 使用资格迹近似λ-return，从而实现token级别的信用分配；2) 提出了一种无评论家的时间差分误差估计方法，避免了引入额外的模型，降低了计算成本。

**关键设计**：论文提出了几种λ-return的加权变体，并将其应用于资格迹的计算中。这些变体旨在平衡短期奖励和长期奖励的影响，从而提高学习的稳定性。此外，论文还详细描述了无评论家的时间差分误差估计方法的具体实现，包括如何利用token的对数概率来近似计算时间差分误差。

## 📊 实验亮点

GRPO-λ在多个数学推理数据集上进行了广泛的实验，结果表明其性能显著优于GRPO。具体来说，在LLaMA-3.1和Qwen-2.5架构上，RL训练期间的性能提高了30-40%。此外，在AIME24、Math500、OlympiadMath、MinervaMath和AMC等基准测试中，GRPO-λ的平均性能比GRPO提高了3个多点，并且在7B模型上提高了4.5个点。这些结果表明，GRPO-λ是一种有效的提升大型语言模型推理能力的方法。

## 🎯 应用场景

GRPO-λ的潜在应用领域包括需要复杂推理的自然语言处理任务，如数学问题求解、代码生成、逻辑推理等。通过更精确的信用分配，GRPO-λ可以提高大型语言模型在这些任务中的性能，从而提升其解决实际问题的能力。该研究的实际价值在于降低了强化学习微调的难度，并为开发更强大的推理模型提供了新的思路。未来，GRPO-λ可以被进一步扩展到其他类型的任务和模型中。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly deployed for tasks requiring complex reasoning, prompting significant interest in improving their reasoning abilities through post-training. Especially RL based methods using verifiable reward, like the state-of-the-art GRPO, have shown to tremendously improve reasoning behaviors when applied as post-training methods. However, the lack of an explicit reward or critic model limits GRPO's ability to assign fine-grained credit across token sequences. In this work, we present GRPO-$λ$, a novel extension to GRPO that enhances credit assignment in RL finetuning of LLMs for complex reasoning tasks. We approximate learning from $λ$-return with a reformulation of eligibility traces using token-level log-probabilities applied after each sequence generation, and a novel critic-free approximation of the temporal-difference error. We introduce a few variations for the weighting of the $λ$-return, and their applications to the eligibility-trace, where all the variations provide significant gains over GRPO. We compare GRPO-$λ$ against GRPO by training models from 1.5B to 7B parameters on $4$ different math reasoning datasets. The training plots demonstrate 30-40% improved performance during RL training on both LLaMA-3.1 and Qwen-2.5 architectures. Finally, we show that with GRPO-$λ$, the resulting average performance on AIME24, Math500, OlympiadMath, MinervaMath, and AMC improves over GRPO by over $3$ points and a $4.5$ points improvement on the 7B model.

