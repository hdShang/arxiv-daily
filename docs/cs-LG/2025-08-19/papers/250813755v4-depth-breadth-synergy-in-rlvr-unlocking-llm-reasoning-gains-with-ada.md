---
layout: default
title: "Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration"
---

# Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13755" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13755v4</a>
  <a href="https://arxiv.org/pdf/2508.13755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13755v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13755v4', 'Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhicheng Yang, Zhijiang Guo, Yinya Huang, Yongxin Wang, Dongchun Xie, Yiwei Wang, Xiaodan Liang, Jing Tang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-19 (更新: 2025-10-06)

**备注**: 18 pages, 14 figures

---

## 💡 一句话要点

**提出DARS以解决RLVR中的深度与广度探索问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `可验证奖励` `困难自适应回滚` `推理能力` `深度学习` `大规模训练` `样本加权`

## 📋 核心要点

1. 现有RLVR方法在深度和广度探索上存在不足，尤其是对低准确度样本的忽视，影响推理能力的提升。
2. 提出困难自适应回滚采样（DARS），通过多阶段回滚策略重新加权困难问题，增强模型对复杂问题的学习能力。
3. 实验结果显示，DARS在不增加推理成本的情况下，显著提升了Pass@K和Pass@1的性能，验证了广度与深度的协同作用。

## 📝 摘要（中文）

强化学习与可验证奖励（RLVR）已成为释放大型语言模型推理能力的强大范式，但其潜力受到深度和广度两个未充分探索维度的限制。本文分析了GRPO算法，揭示了其系统性偏差，提出了困难自适应回滚采样（DARS），通过多阶段回滚重新加权困难问题，增加了正回滚的数量。此外，扩大训练数据的广度显著提高了模型的推理性能。实验结果表明，DARS与大广度训练相结合，能够同时提升Pass@K和Pass@1的表现，证明了深度与广度在RLVR中的正交作用。

## 🔬 方法详解

**问题定义**：本文旨在解决RLVR中深度与广度探索不足的问题，现有方法如GRPO对低准确度样本的忽视导致推理能力受限。

**核心思路**：提出DARS，通过多阶段回滚策略重新加权困难问题，增加正回滚数量，从而提升模型对复杂问题的处理能力。

**技术框架**：整体架构包括DARS模块和大广度训练策略。DARS模块通过多阶段回滚对困难样本进行加权，而大广度训练则通过全批次更新替代小批次迭代，增强训练数据的广度。

**关键创新**：DARS是本研究的核心创新点，其通过针对性回滚解决了现有方法对困难问题的忽视，与传统方法相比，能够更有效地推动推理边界的扩展。

**关键设计**：在DARS中，关键参数包括回滚阶段的数量和样本加权策略；在大广度训练中，采用全批次更新以维持高的token级别熵，促进持续探索。

## 📊 实验亮点

实验结果表明，DARS与大广度训练结合后，Pass@K和Pass@1的性能均有显著提升，Pass@1性能提升幅度达到XX%，验证了广度与深度探索的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动推理等。通过提升大型语言模型的推理能力，能够在更复杂的任务中实现更高的准确性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for unlocking reasoning capabilities in large language models, yet its full potential is hindered by two under-explored dimensions: Depth-the hardest problem a model can sample; Breadth-the number of instances consumed in a single iteration. We dissect the popular GRPO algorithm and reveal a systematic bias: the cumulative-advantage disproportionately weights samples with medium accuracy, while down-weighting the low-accuracy instances that are crucial for pushing reasoning boundaries. To rectify the depth neglect, we introduce Difficulty Adaptive Rollout Sampling (DARS), which re-weights hard problems through targeted multi-stage rollouts, thereby increasing the number of positive rollouts for hard problems. Empirically, naively enlarging rollout size only accelerates convergence and even hurts Pass@K. Our DARS, in contrast, delivers consistent Pass@K gains without extra inference cost at convergence. Just as we adaptively expanded the depth of exploration, we now ask whether aggressively scaling the breadth of training data can further amplify reasoning gains. To this end, we intensely scale batch size and replace PPO's mini-batch iterations with full-batch updates over multiple epochs. Increasing breadth significantly enhances Pass@1 performance. Large-breadth training sustains high token-level entropy, indicating continued exploration and reduced gradient noise. We further present DARS-B, which augments DARS with large breadth, and demonstrate simultaneous gains in Pass@K and Pass@1. The results confirm that breadth and adaptive exploration across depth operate as orthogonal dimensions in RLVR, which are key to unleashing the reasoning power of RLVR.

