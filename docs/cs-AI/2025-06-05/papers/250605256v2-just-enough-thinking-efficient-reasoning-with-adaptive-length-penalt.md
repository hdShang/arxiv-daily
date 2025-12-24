---
layout: default
title: "Just Enough Thinking: Efficient Reasoning with Adaptive Length Penalties Reinforcement Learning"
---

# Just Enough Thinking: Efficient Reasoning with Adaptive Length Penalties Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05256" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05256v2</a>
  <a href="https://arxiv.org/pdf/2506.05256.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05256v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05256v2', 'Just Enough Thinking: Efficient Reasoning with Adaptive Length Penalties Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Violet Xiang, Chase Blagden, Rafael Rafailov, Nathan Lile, Sang Truong, Chelsea Finn, Nick Haber

**分类**: cs.AI, cs.LG

**发布日期**: 2025-06-05 (更新: 2025-06-06)

---

## 💡 一句话要点

**提出自适应长度惩罚以提高推理效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自适应长度惩罚` `推理效率` `强化学习` `计算资源优化` `自然语言处理`

## 📋 核心要点

1. 现有方法在处理简单问题时，往往因生成冗长的标记而浪费计算资源，无法有效区分问题的难易程度。
2. 本文提出自适应长度惩罚（ALP），通过动态调整生成长度来优化推理效率，针对不同难度的提示施加不同的惩罚。
3. 实验结果表明，使用ALP的DeepScaleR-1.5B模型在保持性能的同时，平均标记使用量减少了50%，并在最难问题上取得了更高的准确性。

## 📝 摘要（中文）

大型推理模型（LRMs）在复杂推理任务中通过生成更多的标记来提高性能，但这种冗长的生成在简单问题上往往浪费计算资源。现有解决方案如监督微调、用户控制预算或均匀惩罚的强化学习，均需数据整理、手动配置或对所有问题一视同仁。本文提出自适应长度惩罚（ALP），通过监控每个提示的在线解决率，动态调整生成长度。在训练过程中，ALP为自信（简单）提示增加高惩罚，而对困难提示则不受影响。经过训练的DeepScaleR-1.5B在不显著降低性能的情况下，将平均标记使用量减少了50%。与固定预算和均匀惩罚基线相比，ALP更智能地重新分配预算，提升了对最难问题的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在推理过程中因生成冗长标记而导致的计算资源浪费问题。现有方法无法有效区分问题的难易程度，导致在简单问题上也消耗过多计算资源。

**核心思路**：论文提出自适应长度惩罚（ALP），通过监控每个提示的在线解决率，动态调整生成长度。简单问题的生成会受到更高的惩罚，而困难问题则不受影响，从而优化计算资源的使用。

**技术框架**：ALP的整体架构包括多个阶段：首先，通过多次回滚监控每个提示的解决率；然后，根据解决率动态调整惩罚的大小；最后，优化生成过程以减少简单问题的标记生成。

**关键创新**：ALP的主要创新在于其动态调整惩罚机制，能够根据每个提示的解决率灵活调整生成长度，与现有的固定预算和均匀惩罚方法相比，具有更高的智能性和适应性。

**关键设计**：在ALP中，惩罚的大小与解决率成反比，简单问题的额外标记生成会产生较高的惩罚，而困难问题则不受此限制。该设计使得模型能够在训练过程中有效地学习到如何分配计算资源。

## 📊 实验亮点

实验结果显示，使用自适应长度惩罚的DeepScaleR-1.5B模型在不显著降低性能的情况下，平均标记使用量减少了50%。与固定预算和均匀惩罚基线相比，ALP在最难问题上的准确性得到了显著提升，展示了其在推理效率上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动化推理等。通过优化推理过程，ALP能够提高模型在实际应用中的效率，降低计算成本，同时保持或提升模型的性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large reasoning models (LRMs) achieve higher performance on challenging reasoning tasks by generating more tokens at inference time, but this verbosity often wastes computation on easy problems. Existing solutions, including supervised finetuning on shorter traces, user-controlled budgets, or RL with uniform penalties, either require data curation, manual configuration, or treat all problems alike regardless of difficulty. We introduce Adaptive Length Penalty (ALP), a reinforcement learning objective tailoring generation length to per-prompt solve rate. During training, ALP monitors each prompt's online solve rate through multiple rollouts and adds a differentiable penalty whose magnitude scales inversely with that rate, so confident (easy) prompts incur a high cost for extra tokens while hard prompts remain unhindered. Posttraining DeepScaleR-1.5B with ALP cuts average token usage by 50\% without significantly dropping performance. Relative to fixed-budget and uniform penalty baselines, ALP redistributes its reduced budget more intelligently by cutting compute on easy prompts and reallocating saved tokens to difficult ones, delivering higher accuracy on the hardest problems with higher cost.

