---
layout: default
title: Planning as Descent: Goal-Conditioned Latent Trajectory Synthesis in Learned Energy Landscapes
---

# Planning as Descent: Goal-Conditioned Latent Trajectory Synthesis in Learned Energy Landscapes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17846" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17846v1</a>
  <a href="https://arxiv.org/pdf/2512.17846.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17846v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17846v1', 'Planning as Descent: Goal-Conditioned Latent Trajectory Synthesis in Learned Energy Landscapes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Carlos Vélez García, Miguel Cazorla, Jorge Pomares

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出Planning as Descent (PaD)，通过学习能量场进行离线目标条件强化学习。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `目标条件强化学习` `能量场` `轨迹优化` `梯度下降` `机器人规划` `自监督学习`

## 📋 核心要点

1. 现有离线强化学习方法在训练和测试之间存在不匹配，导致泛化能力不足。
2. PaD通过学习目标条件能量函数，将规划转化为能量场中的梯度下降，实现轨迹优化。
3. 实验表明，PaD在魔方操作任务上显著优于现有方法，尤其是在噪声数据上训练时。

## 📝 摘要（中文）

本文提出了一种名为Planning as Descent (PaD)的离线目标条件强化学习框架，该框架将轨迹生成建立在验证的基础上。PaD不学习策略或显式规划器，而是学习一个关于整个潜在轨迹的目标条件能量函数，为可行且与目标一致的未来分配低能量。规划通过在这个能量场中进行基于梯度的优化来实现，训练和推理过程中使用相同的计算方式，从而减少了解耦建模流程中常见的训练-测试不匹配问题。PaD通过自监督的回溯目标重标记进行训练，围绕规划动态塑造能量场。在推理时，多个轨迹候选在不同的时间假设下进行优化，并选择平衡可行性和效率的低能量计划。在OGBench魔方操作任务上的评估表明，在狭窄的专家演示数据上训练时，PaD达到了最先进的95%的成功率，显著优于之前方法的68%。值得注意的是，在嘈杂的、次优数据上训练进一步提高了成功率和计划效率，突出了验证驱动规划的优势。我们的结果表明，学习评估和优化轨迹为离线、无奖励规划提供了一种稳健的替代方案，优于直接策略学习。

## 🔬 方法详解

**问题定义**：现有的离线目标条件强化学习方法，通常依赖于学习策略或显式规划器，这些方法容易受到训练数据质量的影响，并且在训练和测试之间存在不匹配，导致泛化能力较差。特别是在复杂任务中，策略学习可能难以捕捉到最优轨迹的细微之处，而显式规划器则需要大量的计算资源和领域知识。

**核心思路**：PaD的核心思路是将规划问题转化为在学习到的能量场中进行梯度下降的过程。通过学习一个目标条件能量函数，该函数为可行且与目标一致的轨迹分配低能量，从而将规划问题转化为寻找能量最低的轨迹。这种方法避免了直接学习策略或显式规划器，而是通过优化轨迹的能量来实现规划。

**技术框架**：PaD的整体框架包括以下几个主要模块：1）轨迹编码器：将轨迹编码为潜在向量表示。2）目标条件能量函数：学习一个能量函数，该函数以轨迹的潜在向量表示和目标为输入，输出一个能量值。3）梯度下降优化器：使用梯度下降算法在能量场中优化轨迹，寻找能量最低的轨迹。4）回溯目标重标记：使用自监督的回溯目标重标记方法来训练能量函数，从而使能量场围绕规划动态进行塑造。

**关键创新**：PaD的关键创新在于将规划问题转化为能量场中的梯度下降过程。与传统的策略学习或显式规划方法不同，PaD通过学习一个能量函数来评估轨迹的可行性和效率，并通过梯度下降来优化轨迹。这种方法具有以下优点：1）避免了直接学习策略或显式规划器，从而减少了训练和测试之间的不匹配。2）可以通过自监督的回溯目标重标记方法来训练能量函数，从而提高了能量函数的泛化能力。3）可以通过梯度下降来优化轨迹，从而实现高效的规划。

**关键设计**：PaD的关键设计包括：1）能量函数的选择：能量函数可以使用神经网络来表示，例如多层感知机或卷积神经网络。2）梯度下降优化器的选择：可以使用各种梯度下降优化器，例如Adam或SGD。3）回溯目标重标记策略：可以使用不同的回溯目标重标记策略来生成训练数据。4）损失函数的设计：损失函数用于训练能量函数，可以使用各种损失函数，例如均方误差或交叉熵损失。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17846v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17846v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17846v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PaD在OGBench魔方操作任务上取得了显著的成果。在狭窄的专家演示数据上训练时，PaD达到了最先进的95%的成功率，显著优于之前方法的68%。更令人惊讶的是，在嘈杂的、次优数据上训练进一步提高了成功率和计划效率，这表明PaD对噪声数据具有很强的鲁棒性，并且能够从次优数据中学习到有效的规划策略。

## 🎯 应用场景

PaD具有广泛的应用前景，例如机器人导航、运动规划、游戏AI等领域。它可以用于解决离线强化学习中的泛化问题，提高规划的效率和鲁棒性。此外，PaD还可以应用于无奖励规划场景，通过学习能量函数来评估轨迹的可行性和效率，从而实现自主规划。

## 📄 摘要（原文）

> We present Planning as Descent (PaD), a framework for offline goal-conditioned reinforcement learning that grounds trajectory synthesis in verification. Instead of learning a policy or explicit planner, PaD learns a goal-conditioned energy function over entire latent trajectories, assigning low energy to feasible, goal-consistent futures. Planning is realized as gradient-based refinement in this energy landscape, using identical computation during training and inference to reduce train-test mismatch common in decoupled modeling pipelines.
>   PaD is trained via self-supervised hindsight goal relabeling, shaping the energy landscape around the planning dynamics. At inference, multiple trajectory candidates are refined under different temporal hypotheses, and low-energy plans balancing feasibility and efficiency are selected.
>   We evaluate PaD on OGBench cube manipulation tasks. When trained on narrow expert demonstrations, PaD achieves state-of-the-art 95\% success, strongly outperforming prior methods that peak at 68\%. Remarkably, training on noisy, suboptimal data further improves success and plan efficiency, highlighting the benefits of verification-driven planning. Our results suggest learning to evaluate and refine trajectories provides a robust alternative to direct policy learning for offline, reward-free planning.

