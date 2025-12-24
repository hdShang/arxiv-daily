---
layout: default
title: On the Robustness of Reward Models for Language Model Alignment
---

# On the Robustness of Reward Models for Language Model Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07271" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07271v1</a>
  <a href="https://arxiv.org/pdf/2505.07271.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07271v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07271v1', 'On the Robustness of Reward Models for Language Model Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiwoo Hong, Noah Lee, Eunki Kim, Guijin Son, Woojin Chung, Aman Gupta, Shao Tang, James Thorne

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-12

**备注**: ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/LinkedIn-XFACT/RM-Robustness)

---

## 💡 一句话要点

**提出批量归零正则化以解决奖励模型的过度优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `奖励模型` `强化学习` `鲁棒性` `人类反馈` `模型优化` `批量归零正则化` `自然语言处理` `偏好预测`

## 📋 核心要点

1. 现有的奖励模型在训练过程中容易出现过度优化，导致对新输入的泛化能力不足。
2. 本文提出批量归零正则化（BSR），通过强制每个批次的奖励和为零来解决过度优化问题。
3. 实验结果表明，使用BSR的奖励模型在RLHF训练中更好地对齐了策略，并在复杂任务中提升了超过5%的性能。

## 📝 摘要（中文）

Bradley-Terry (BT) 模型在基于人类反馈的强化学习（RLHF）中广泛应用于奖励建模。尽管其有效性显著，但使用BT模型损失训练的奖励模型（RMs）容易过度优化，导致对未见输入分布的泛化能力下降。本文研究了RM训练中过度优化的原因及其对RLHF过程的影响，强调了RMs在未见数据中的分布鲁棒性的重要性。我们发现隐藏状态范数的过度分散是过度优化的主要来源，并提出了批量归零正则化（BSR），以强制每个批次的奖励和为零，从而限制极端幅度的奖励。通过四种过度优化场景评估BSR的影响，结果表明BSR在提高RMs的鲁棒性方面表现出色。最终，BSR在高质量数据和模型上的应用超越了8B规模的最先进RMs，在复杂偏好预测任务中提升超过5%。

## 🔬 方法详解

**问题定义**：本文旨在解决奖励模型在训练过程中出现的过度优化问题，现有的BT模型损失导致模型对未见数据的泛化能力下降。

**核心思路**：提出批量归零正则化（BSR），通过限制每个批次的奖励和为零，来减少奖励的极端幅度，从而提高模型的鲁棒性。

**技术框架**：整体架构包括数据预处理、BSR正则化应用、模型训练和评估四个主要模块。BSR在每个训练批次中应用，确保奖励的分布更为均匀。

**关键创新**：BSR是本文的核心创新点，与传统的BT模型相比，BSR通过控制奖励的分布，显著提高了模型在未见数据上的鲁棒性。

**关键设计**：在损失函数中引入BSR正则化项，确保每个批次的奖励和为零，此外，调整隐藏状态的范数以避免过度分散。

## 📊 实验亮点

实验结果显示，使用BSR的奖励模型在复杂偏好预测任务中提升超过5%，并且在8B规模的模型中，通过RLOO训练，生成长度减少了40%，胜率提高了7%，进一步验证了鲁棒性对RLHF训练的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、推荐系统和人机交互等。通过提高奖励模型的鲁棒性，可以在多种复杂任务中实现更好的性能，进而推动RLHF技术的实际应用和发展。

## 📄 摘要（原文）

> The Bradley-Terry (BT) model is widely practiced in reward modeling for reinforcement learning with human feedback (RLHF). Despite its effectiveness, reward models (RMs) trained with BT model loss are prone to over-optimization, losing generalizability to unseen input distributions. In this paper, we study the cause of over-optimization in RM training and its downstream effects on the RLHF procedure, accentuating the importance of distributional robustness of RMs in unseen data. First, we show that the excessive dispersion of hidden state norms is the main source of over-optimization. Then, we propose batch-wise sum-to-zero regularization (BSR) to enforce zero-centered reward sum per batch, constraining the rewards with extreme magnitudes. We assess the impact of BSR in improving robustness in RMs through four scenarios of over-optimization, where BSR consistently manifests better robustness. Subsequently, we compare the plain BT model and BSR on RLHF training and empirically show that robust RMs better align the policy to the gold preference model. Finally, we apply BSR to high-quality data and models, which surpasses state-of-the-art RMs in the 8B scale by adding more than 5% in complex preference prediction tasks. By conducting RLOO training with 8B RMs, AlpacaEval 2.0 reduces generation length by 40% while adding a 7% increase in win rate, further highlighting that robustness in RMs induces robustness in RLHF training. We release the code, data, and models: https://github.com/LinkedIn-XFACT/RM-Robustness.

