---
layout: default
title: "ADHint: Adaptive Hints with Difficulty Priors for Reinforcement Learning"
---

# ADHint: Adaptive Hints with Difficulty Priors for Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13095" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13095v1</a>
  <a href="https://arxiv.org/pdf/2512.13095.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13095v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13095v1', 'ADHint: Adaptive Hints with Difficulty Priors for Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Zhang, Zezhong Tan, Xinhong Ma, Ziqiang Dong, Xi Leng, Jianfei Zhao, Xin Sun, Yang Yang

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-15

---

## 💡 一句话要点

**ADHint：利用难度先验的自适应提示强化学习，提升推理能力和泛化性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `提示学习` `难度先验` `自适应提示` `优势估计`

## 📋 核心要点

1. 现有基于提示的强化学习方法忽略了样本难度，导致学习不稳定和过度模仿离策略数据。
2. ADHint将样本难度纳入提示比例调度和优势估计，平衡探索与模仿，提升学习效果。
3. 实验表明，ADHint在多种模态、模型规模和领域中，显著提升了推理能力和泛化性能。

## 📝 摘要（中文）

为了结合监督微调(SFT)和强化学习(RL)的优势，现有方法将“提示”（完整推理轨迹的前缀片段）集成到后训练中，旨在实现强大的知识扩展和推理泛化。然而，现有的基于提示的RL方法通常忽略了在调度提示比例和估计相对优势时的难度，导致不稳定的学习和过度模仿离策略提示。本文提出了ADHint，它将难度作为提示比例调度和相对优势估计的关键因素，以在探索和模仿之间实现更好的权衡。具体来说，我们提出了具有样本难度先验的自适应提示，它评估策略模型下每个样本的难度，并相应地调度适当的提示比例来指导其rollout。我们还引入了基于一致性的梯度调制和提示保持的选择性掩码，以调制提示内的token级别梯度，防止有偏差和破坏性的更新。此外，我们提出了具有Rollout难度后验的优势估计，它利用有提示和无提示的rollout的相对难度来估计它们各自的优势，从而实现更平衡的更新。在不同的模态、模型规模和领域中进行的大量实验表明，ADHint提供了卓越的推理能力和分布外泛化能力，在pass@1和avg@8方面始终优于现有方法。我们的代码和数据集将在论文被接受后公开发布。

## 🔬 方法详解

**问题定义**：现有基于提示的强化学习方法在利用提示信息进行策略优化时，忽略了不同样本的难度差异。这导致两个主要问题：一是提示比例的分配不合理，简单样本可能被过度提示，而困难样本则缺乏足够的指导；二是优势函数估计不准确，无法区分提示带来的真实收益和样本本身的难度，从而导致策略学习不稳定，容易陷入局部最优。

**核心思路**：ADHint的核心思路是将样本难度作为关键因素，融入到提示比例的调度和优势函数估计中。通过自适应地调整提示比例，为不同难度的样本提供合适的指导，同时利用rollout的难度后验来更准确地估计优势函数，从而实现更有效的策略学习。

**技术框架**：ADHint主要包含三个核心模块：1) **Adaptive Hint with Sample Difficulty Prior (AH-SDP)**：根据策略模型评估样本难度，自适应地调整提示比例。2) **Consistency-based Gradient Modulation and Selective Masking for Hint Preservation (CGM-SM)**：调制提示内部的梯度，并进行选择性掩码，以防止提示信息被破坏。3) **Advantage Estimation with Rollout Difficulty Posterior (AE-RDP)**：利用有提示和无提示rollout的难度后验，更准确地估计优势函数。整体流程是，首先利用AH-SDP确定提示比例，然后进行rollout，接着利用CGM-SM保护提示信息，最后利用AE-RDP估计优势函数并更新策略。

**关键创新**：ADHint的关键创新在于将样本难度显式地建模到提示强化学习过程中。AH-SDP通过样本难度先验自适应地调整提示比例，CGM-SM通过梯度调制和选择性掩码保护提示信息，AE-RDP通过rollout难度后验更准确地估计优势函数。这些创新共同作用，使得ADHint能够更有效地利用提示信息，提升策略学习的稳定性和泛化能力。

**关键设计**：AH-SDP中，样本难度通过策略模型的置信度或预测概率来衡量，提示比例根据样本难度进行调整，难度高的样本分配更高的提示比例。CGM-SM通过计算提示内部token的一致性来调制梯度，并对不一致的token进行掩码，以防止提示信息被破坏。AE-RDP利用有提示和无提示rollout的奖励和难度信息，计算rollout难度后验，并将其用于优势函数的估计中。

## 📊 实验亮点

实验结果表明，ADHint在多个任务上都取得了显著的性能提升。例如，在推理任务中，ADHint在pass@1和avg@8指标上均优于现有方法。具体来说，ADHint在某些任务上的pass@1指标提升了超过5个百分点，表明其具有更强的推理能力和泛化性能。这些结果证明了ADHint的有效性和优越性。

## 🎯 应用场景

ADHint具有广泛的应用前景，可以应用于各种需要利用提示信息进行强化学习的任务中，例如对话生成、代码生成、机器人控制等。通过引入难度先验，ADHint能够更有效地利用提示信息，提升模型的推理能力和泛化性能，从而在实际应用中取得更好的效果。此外，ADHint还可以应用于教育领域，例如个性化辅导系统，根据学生的学习难度自适应地提供提示信息。

## 📄 摘要（原文）

> To combine the advantages of Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), recent methods have integrated ''hints'' into post-training, which are prefix segments of complete reasoning trajectories, aiming for powerful knowledge expansion and reasoning generalization. However, existing hint-based RL methods typically ignore difficulty when scheduling hint ratios and estimating relative advantages, leading to unstable learning and excessive imitation of off-policy hints. In this work, we propose ADHint, which treats difficulty as a key factor in both hint-ratio schedule and relative-advantage estimation to achieve a better trade-off between exploration and imitation. Specifically, we propose Adaptive Hint with Sample Difficulty Prior, which evaluates each sample's difficulty under the policy model and accordingly schedules an appropriate hint ratio to guide its rollouts. We also introduce Consistency-based Gradient Modulation and Selective Masking for Hint Preservation to modulate token-level gradients within hints, preventing biased and destructive updates. Additionally, we propose Advantage Estimation with Rollout Difficulty Posterior, which leverages the relative difficulty of rollouts with and without hints to estimate their respective advantages, thereby achieving more balanced updates. Extensive experiments across diverse modalities, model scales, and domains demonstrate that ADHint delivers superior reasoning ability and out-of-distribution generalization, consistently surpassing existing methods in both pass@1 and avg@8. Our code and dataset will be made publicly available upon paper acceptance.

