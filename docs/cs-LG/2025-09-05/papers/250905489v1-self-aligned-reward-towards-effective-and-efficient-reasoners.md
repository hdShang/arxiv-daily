---
layout: default
title: "Self-Aligned Reward: Towards Effective and Efficient Reasoners"
---

# Self-Aligned Reward: Towards Effective and Efficient Reasoners

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05489" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05489v1</a>
  <a href="https://arxiv.org/pdf/2509.05489.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05489v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05489v1', 'Self-Aligned Reward: Towards Effective and Efficient Reasoners')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peixuan Han, Adit Krishnan, Gerald Friedland, Jiaxuan You, Chris Kong

**分类**: cs.LG

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**提出自对齐奖励(SAR)，提升LLM推理效率和准确性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自对齐奖励` `强化学习` `大型语言模型` `推理效率` `困惑度`

## 📋 核心要点

1. 现有LLM推理方法依赖粗粒度二元奖励，导致推理冗长和高计算成本。
2. 提出自对齐奖励(SAR)，利用困惑度差异引导模型生成简洁准确的答案。
3. 实验表明，SAR能显著提升推理准确率并降低推理成本，实现效率与准确率的平衡。

## 📝 摘要（中文）

本文提出了一种自对齐奖励(SAR)机制，旨在提升大型语言模型(LLM)在推理任务中的效率和准确性。现有基于可验证奖励的强化学习方法通常提供粗粒度的二元反馈，导致推理过程冗长和计算成本高昂，同时现有解决方案又可能牺牲准确性。SAR作为一种自引导信号，补充可验证奖励，鼓励推理的准确性和效率。SAR定义为答案在给定查询条件下的困惑度与独立答案困惑度之间的相对差异，从而倾向于简洁且特定于查询的响应。定量分析表明，SAR能够可靠地区分答案质量。实验结果表明，将SAR与PPO和GRPO等主流强化学习算法相结合，可将准确率提高4%，同时降低30%的推理成本。SAR在正确性和效率之间实现了帕累托最优的权衡，并在保留高级推理行为的同时缩短了响应，证明了其在抑制不必要阐述方面的能力。

## 🔬 方法详解

**问题定义**：现有基于可验证奖励的强化学习方法在训练LLM进行推理时，通常只能提供二元的正确或错误反馈，这种粗粒度的信号导致模型倾向于生成冗长且计算成本高的推理过程。同时，一些旨在提高效率的方法又可能牺牲推理的准确性。因此，如何设计一种既能保证推理准确性，又能提高推理效率的奖励机制是本文要解决的问题。

**核心思路**：本文的核心思路是利用语言模型自身的特性，设计一种自对齐的奖励信号(SAR)。SAR基于一个假设：好的答案应该既准确又简洁，并且与给定的问题密切相关。因此，SAR通过比较在给定问题的情况下生成答案的困惑度与独立生成答案的困惑度之间的差异来衡量答案的质量。如果答案简洁且与问题相关，那么在给定问题的情况下生成答案的困惑度应该更低，SAR值更高。

**技术框架**：整体框架是在现有的强化学习训练流程中，将SAR作为一种额外的奖励信号加入到总奖励中。具体来说，模型首先根据给定的问题生成答案，然后计算SAR值。SAR值与可验证奖励（例如，答案是否正确）结合，作为强化学习算法的奖励信号，用于更新模型的参数。本文主要使用了PPO和GRPO两种强化学习算法，并将SAR与这两种算法结合使用。

**关键创新**：本文最重要的技术创新点在于提出了自对齐奖励(SAR)的概念，并将其应用于LLM的推理训练中。与传统的基于规则或人工设计的奖励函数不同，SAR是一种自引导的奖励信号，它利用了语言模型自身的困惑度信息来衡量答案的质量。这种方法不需要额外的人工标注或规则设计，可以更方便地应用于不同的推理任务和模型。

**关键设计**：SAR的关键设计在于困惑度的计算方式。具体来说，SAR定义为：SAR = perplexity(answer) - perplexity(answer | query)，其中perplexity(answer)表示独立生成答案的困惑度，perplexity(answer | query)表示在给定问题的情况下生成答案的困惑度。通过这种方式，SAR能够有效地衡量答案的简洁性和相关性。此外，本文还探索了不同的SAR权重，以平衡准确性和效率之间的权衡。

## 📊 实验亮点

实验结果表明，将SAR与PPO和GRPO等主流强化学习算法相结合，在7个基准测试中，可以将准确率平均提高4%，同时降低30%的推理成本。此外，SAR在正确性和效率之间实现了帕累托最优的权衡，并且能够在保留高级推理行为的同时缩短响应。

## 🎯 应用场景

该研究成果可广泛应用于各种需要LLM进行推理的场景，例如问答系统、对话系统、代码生成等。通过引入SAR，可以训练出更加高效和准确的推理模型，降低计算成本，并提升用户体验。未来，可以将SAR与其他奖励信号相结合，进一步提升LLM的推理能力。

## 📄 摘要（原文）

> Reinforcement learning with verifiable rewards has significantly advanced reasoning in large language models (LLMs), but such signals remain coarse, offering only binary correctness feedback. This limitation often results in inefficiencies, including overly verbose reasoning and high computational cost, while existing solutions often compromise accuracy. To address this, we introduce self-aligned reward (SAR), a self-guided signal that complements verifiable rewards to encourage both reasoning accuracy and efficiency. SAR is defined as the relative perplexity difference between an answer conditioned on the query and the standalone answer, thereby favoring responses that are concise and query-specific. Quantitative analysis reveals that SAR reliably distinguishes answer quality: concise, correct answers score higher than redundant ones, and partially correct answers score higher than entirely incorrect ones. Evaluation on 4 models across 7 benchmarks shows that integrating SAR with prevalent RL algorithms like PPO and GRPO improves accuracy by 4%, while reducing inference cost by 30%. Further analysis demonstrates that SAR achieves a Pareto-optimal trade-off between correctness and efficiency compared to reward signals based on length or self-confidence. We also show that SAR shortens responses while preserving advanced reasoning behaviors, demonstrating its ability to suppress unnecessary elaboration without losing critical reasoning. These results highlight the promise of self-aligned reward as a fine-grained complement to verifiable rewards, paving the way for more efficient and effective LLM training.

