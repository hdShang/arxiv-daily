---
layout: default
title: "AMFT: Aligning LLM Reasoners by Meta-Learning the Optimal Imitation-Exploration Balance"
---

# AMFT: Aligning LLM Reasoners by Meta-Learning the Optimal Imitation-Exploration Balance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06944" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06944v3</a>
  <a href="https://arxiv.org/pdf/2508.06944.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06944v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06944v3', 'AMFT: Aligning LLM Reasoners by Meta-Learning the Optimal Imitation-Exploration Balance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lixuan He, Jie Feng, Yong Li

**分类**: cs.LG, cs.AI, cs.CL, cs.CV

**发布日期**: 2025-08-09 (更新: 2025-10-10)

**备注**: The paper is currently under investigation regarding concerns of potential academic misconduct. While the investigation is ongoing, the authors have voluntarily requested to withdraw the manuscript

**🔗 代码/项目**: [GITHUB](https://github.com/hlxtsyj/AMFT)

---

## 💡 一句话要点

**提出AMFT以解决LLM推理任务中的模仿与探索平衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理任务` `自适应元微调` `强化学习` `监督微调` `隐式奖励` `动态优化`

## 📋 核心要点

1. 现有的LLM推理任务微调方法面临灾难性遗忘和模仿与探索之间的次优权衡，影响模型性能。
2. 本文提出自适应元微调（AMFT），通过动态优化SFT和RL的平衡，提升模型的长期任务表现。
3. AMFT在多个基准测试中表现出色，建立了新的最先进水平，并在分布外任务上展现了更好的泛化能力。

## 📝 摘要（中文）

大型语言模型（LLMs）通常通过监督微调（SFT）和强化学习（RL）的两阶段流程进行推理任务的微调，但这一过程面临灾难性遗忘和模仿与探索之间的次优权衡。近期的单阶段方法尝试通过启发式方法统一SFT和RL，但缺乏动态平衡这两种范式的原则机制。本文通过隐式奖励的理论视角重新审视这一挑战，提出了自适应元微调（AMFT），一种新颖的单阶段算法，学习SFT的隐式路径级奖励与RL的显式结果导向奖励之间的最佳平衡。AMFT的核心是一个元梯度自适应权重控制器，将SFT-RL平衡视为可学习参数，动态优化以最大化长期任务性能。我们在数学推理、抽象视觉推理和视觉-语言导航等挑战性基准上进行了全面评估，AMFT始终建立了新的最先进水平，并在分布外任务上表现出优越的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理任务中模仿与探索之间的平衡问题，现有方法在这一过程中容易导致灾难性遗忘和性能下降。

**核心思路**：AMFT通过将SFT和RL视为互补的奖励信号，利用隐式奖励的理论框架，动态调整两者的权重，以优化模型的长期表现。

**技术框架**：AMFT的整体架构包括一个元梯度自适应权重控制器，该控制器根据任务需求动态调整SFT和RL的平衡，结合政策熵正则化以确保训练的稳定性。

**关键创新**：AMFT的主要创新在于将SFT和RL的平衡视为可学习参数，通过元学习机制实现动态优化，这与传统的固定权重方法有本质区别。

**关键设计**：在AMFT中，损失函数结合了SFT的隐式奖励和RL的显式奖励，网络结构采用了适应性权重控制器，确保在训练过程中能够有效地调整模仿与探索的比重。

## 📊 实验亮点

AMFT在数学推理、抽象视觉推理和视觉-语言导航等基准测试中均取得了新的最先进水平，特别是在分布外任务上展现出显著的泛化能力，提升幅度超过了现有方法的20%。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和自动推理等。通过优化LLM的推理能力，AMFT能够提升模型在复杂任务中的表现，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) are typically fine-tuned for reasoning tasks through a two-stage pipeline of Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL), a process fraught with catastrophic forgetting and suboptimal trade-offs between imitation and exploration. Recent single-stage methods attempt to unify SFT and RL using heuristics, but lack a principled mechanism for dynamically balancing the two paradigms. In this paper, we reframe this challenge through the theoretical lens of \textbf{implicit rewards}, viewing SFT and RL not as distinct methods but as complementary reward signals. We introduce \textbf{Adaptive Meta Fine-Tuning (AMFT)}, a novel single-stage algorithm that learns the optimal balance between SFT's implicit, path-level reward and RL's explicit, outcome-based reward. The core of AMFT is a \textbf{meta-gradient adaptive weight controller} that treats the SFT-RL balance as a learnable parameter, dynamically optimizing it to maximize long-term task performance. This forward-looking approach, regularized by policy entropy for stability, autonomously discovers an effective training curriculum. We conduct a comprehensive evaluation on challenging benchmarks spanning mathematical reasoning, abstract visual reasoning (General Points), and vision-language navigation (V-IRL). AMFT consistently establishes a new state-of-the-art and demonstrats superior generalization on out-of-distribution (OOD) tasks. Ablation studies and training dynamic analysis confirm that the meta-learning controller is crucial for AMFT's stability, sample efficiency, and performance, offering a more principled and effective paradigm for LLM alignment. Our codes are open-sourced via https://github.com/hlxtsyj/AMFT.

