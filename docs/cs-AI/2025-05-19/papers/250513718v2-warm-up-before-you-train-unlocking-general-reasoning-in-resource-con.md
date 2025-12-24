---
layout: default
title: "Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings"
---

# Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13718" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13718v2</a>
  <a href="https://arxiv.org/pdf/2505.13718.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13718v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13718v2', 'Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Safal Shrestha, Minwu Kim, Aadim Nepal, Anubhav Shrestha, Keith Ross

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-19 (更新: 2025-05-26)

**DOI**: [10.18653/v1/2025.emnlp-main.727](https://doi.org/10.18653/v1/2025.emnlp-main.727)

---

## 💡 一句话要点

**提出双阶段训练策略以解决数据稀缺下的推理能力问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理能力` `大型语言模型` `强化学习` `长链思维` `样本效率` `数据稀缺` `双阶段训练`

## 📋 核心要点

1. 现有的推理能力模型训练方法依赖大量高质量数据，导致在数据稀缺环境中面临挑战。
2. 提出的双阶段训练策略通过先在玩具领域进行热身，再在目标领域进行强化学习，提升模型推理能力。
3. 实验结果显示，热身阶段显著提高了模型在多个任务上的表现，且在小数据集上热身模型优于基础模型。

## 📝 摘要（中文）

设计有效的推理能力大型语言模型（LLMs）通常需要使用可验证奖励的强化学习（RLVR）或经过精心策划的长链思维（CoT）蒸馏，这两者都依赖大量的训练数据。当高质量训练数据稀缺时，这就成为一个重大挑战。本文提出了一种样本高效的双阶段训练策略，以在有限监督下开发推理LLMs。在第一阶段，我们通过从玩具领域（骑士与骗子逻辑谜题）蒸馏长链思维来“热身”模型，以获取一般推理技能。在第二阶段，我们使用有限的目标领域示例对热身后的模型应用RLVR。实验表明，这种两阶段方法在多个任务上显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决在数据稀缺环境下，如何有效训练具有推理能力的LLMs的问题。现有方法如RLVR和CoT蒸馏依赖大量高质量数据，难以适应数据稀缺的场景。

**核心思路**：论文提出的双阶段训练策略，首先通过玩具领域的长链思维蒸馏进行模型热身，获取一般推理技能，随后在目标领域进行强化学习训练，以提高模型的推理能力和样本效率。

**技术框架**：整体架构分为两个主要阶段：第一阶段为热身阶段，通过骑士与骗子逻辑谜题进行长链思维的蒸馏；第二阶段为强化学习阶段，使用有限的目标领域示例进行RLVR训练。

**关键创新**：最重要的创新在于引入热身阶段，使得模型在进行强化学习训练之前，能够先获得一般推理能力，从而提升跨领域的泛化能力。与现有方法相比，这种设计显著提高了模型在小数据集上的表现。

**关键设计**：在热身阶段，使用骑士与骗子逻辑谜题进行长链思维蒸馏，确保模型能够学习到基本的推理规则；在强化学习阶段，采用有限的目标领域示例进行训练，优化模型的推理能力和样本效率。

## 📊 实验亮点

实验结果显示，热身阶段显著提升了模型的推理能力，尤其是在MATH、HumanEval$^{+}$和MMLU-Pro等任务上表现优异。热身模型在相同小数据集（≤100个示例）上始终优于基础模型，且在RLVR训练中提高了整体样本效率。

## 🎯 应用场景

该研究的潜在应用领域包括教育、游戏设计和智能助手等，能够在数据稀缺的情况下，提升模型的推理能力，具有重要的实际价值。未来，该方法可能推动更广泛的推理能力模型的开发，尤其是在资源受限的环境中。

## 📄 摘要（原文）

> Designing effective reasoning-capable LLMs typically requires training using Reinforcement Learning with Verifiable Rewards (RLVR) or distillation with carefully curated Long Chain of Thoughts (CoT), both of which depend heavily on extensive training data. This creates a major challenge when the amount of quality training data is scarce. We propose a sample-efficient, two-stage training strategy to develop reasoning LLMs under limited supervision. In the first stage, we "warm up" the model by distilling Long CoTs from a toy domain, namely, Knights \& Knaves (K\&K) logic puzzles to acquire general reasoning skills. In the second stage, we apply RLVR to the warmed-up model using a limited set of target-domain examples. Our experiments demonstrate that this two-phase approach offers several benefits: $(i)$ the warmup phase alone facilitates generalized reasoning, leading to performance improvements across a range of tasks, including MATH, HumanEval$^{+}$, and MMLU-Pro; $(ii)$ When both the base model and the warmed-up model are RLVR trained on the same small dataset ($\leq100$ examples), the warmed-up model consistently outperforms the base model; $(iii)$ Warming up before RLVR training allows a model to maintain cross-domain generalizability even after training on a specific domain; $(iv)$ Introducing warmup in the pipeline improves not only accuracy but also overall sample efficiency during RLVR training. The results in this paper highlight the promise of warmup for building robust reasoning LLMs in data-scarce environments.

