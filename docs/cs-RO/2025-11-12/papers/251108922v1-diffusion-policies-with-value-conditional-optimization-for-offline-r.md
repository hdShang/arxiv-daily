---
layout: default
title: Diffusion Policies with Value-Conditional Optimization for Offline Reinforcement Learning
---

# Diffusion Policies with Value-Conditional Optimization for Offline Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08922" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08922v1</a>
  <a href="https://arxiv.org/pdf/2511.08922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08922v1" onclick="toggleFavorite(this, '2511.08922v1', 'Diffusion Policies with Value-Conditional Optimization for Offline Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunchang Ma, Tenglong Liu, Yixing Lan, Xin Yin, Changxin Zhang, Xinglong Zhang, Xin Xu

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-11-12

**备注**: IROS 2025

---

## 💡 一句话要点

**提出DIVO，通过价值条件优化扩散策略解决离线强化学习中的过估计问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `扩散模型` `价值条件优化` `优势函数` `策略学习`

## 📋 核心要点

1. 离线强化学习中，值过估计是策略性能瓶颈，现有方法保守性过强，难以平衡表达能力和效率。
2. DIVO利用优势值引导扩散模型训练，精确对齐数据集分布，选择性扩展高优势动作边界。
3. DIVO在D4RL基准测试中表现出色，尤其在AntMaze等稀疏奖励环境中，显著优于现有方法。

## 📝 摘要（中文）

在离线强化学习中，由于分布外(OOD)动作导致的值过估计严重限制了策略性能。最近，扩散模型因其强大的分布匹配能力而被利用，通过行为策略约束来强制保守性。然而，现有方法通常对低质量数据集中的冗余动作进行无差别正则化，导致过度保守以及扩散模型表达能力和效率之间的不平衡。为了解决这些问题，我们提出了一种新的方法，即具有价值条件优化的扩散策略(DIVO)，该方法利用扩散模型生成高质量、广泛覆盖的分布内状态-动作样本，同时促进有效的策略改进。具体来说，DIVO引入了一种二元加权机制，该机制利用离线数据集中动作的优势值来指导扩散模型训练。这使得能够更精确地与数据集的分布对齐，同时选择性地扩展高优势动作的边界。在策略改进过程中，DIVO动态地过滤来自扩散模型的高回报潜力动作，有效地引导学习到的策略朝着更好的性能发展。这种方法在离线强化学习中实现了保守性和可探索性之间的关键平衡。我们在D4RL基准上评估了DIVO，并将其与最先进的基线进行比较。实验结果表明，DIVO实现了卓越的性能，在运动任务中实现了平均回报的显著提高，并且在具有稀疏奖励的具有挑战性的AntMaze领域中优于现有方法。

## 🔬 方法详解

**问题定义**：离线强化学习面临值函数过估计的问题，尤其是在数据集质量不高的情况下。现有方法，如使用扩散模型约束策略，容易对所有动作进行过度保守的正则化，限制了策略的探索能力和性能提升。这种一刀切的方法忽略了数据集中不同动作的价值差异，导致次优解。

**核心思路**：DIVO的核心在于利用动作的优势值来指导扩散模型的训练，从而实现更精细的策略约束。通过优势值，DIVO能够区分有价值和无价值的动作，并选择性地对高价值动作进行探索，避免对所有动作进行无差别的保守约束。这种方法旨在平衡保守性和探索性，从而在离线数据集中学习到更好的策略。

**技术框架**：DIVO包含两个主要阶段：扩散模型训练和策略改进。在扩散模型训练阶段，DIVO使用二元加权机制，根据动作的优势值对扩散模型的损失函数进行加权。优势值高的动作在训练中获得更高的权重，从而引导扩散模型更多地关注这些动作。在策略改进阶段，DIVO从扩散模型中采样动作，并根据其潜在回报进行过滤，选择更有可能带来高回报的动作来更新策略。

**关键创新**：DIVO的关键创新在于价值条件优化，即利用动作的优势值来指导扩散模型的训练和策略改进。与现有方法不同，DIVO不是对所有动作进行无差别的约束，而是根据其价值进行选择性的约束和探索。这种方法能够更有效地利用离线数据，学习到更好的策略。

**关键设计**：DIVO的关键设计包括：1) 二元加权机制，用于根据动作的优势值对扩散模型的损失函数进行加权。具体来说，优势值高于某个阈值的动作被赋予更高的权重，而优势值低于阈值的动作则被赋予较低的权重。2) 动态过滤机制，用于在策略改进阶段从扩散模型中采样动作，并根据其潜在回报进行过滤。该机制选择更有可能带来高回报的动作来更新策略。

## 📊 实验亮点

DIVO在D4RL基准测试中取得了显著的性能提升。在运动任务中，DIVO的平均回报显著高于现有方法。在具有挑战性的AntMaze环境中，DIVO也优于现有方法，证明了其在稀疏奖励环境下的有效性。实验结果表明，DIVO能够有效地平衡保守性和探索性，从而学习到更好的策略。

## 🎯 应用场景

DIVO在机器人控制、自动驾驶、游戏AI等领域具有广泛的应用前景。它可以利用离线数据学习高性能策略，无需在线交互，降低了学习成本和风险。尤其是在数据获取困难或成本高昂的场景下，DIVO的价值更加突出。未来，DIVO可以进一步扩展到多智能体强化学习、元强化学习等领域。

## 📄 摘要（原文）

> In offline reinforcement learning, value overestimation caused by out-of-distribution (OOD) actions significantly limits policy performance. Recently, diffusion models have been leveraged for their strong distribution-matching capabilities, enforcing conservatism through behavior policy constraints. However, existing methods often apply indiscriminate regularization to redundant actions in low-quality datasets, resulting in excessive conservatism and an imbalance between the expressiveness and efficiency of diffusion modeling. To address these issues, we propose DIffusion policies with Value-conditional Optimization (DIVO), a novel approach that leverages diffusion models to generate high-quality, broadly covered in-distribution state-action samples while facilitating efficient policy improvement. Specifically, DIVO introduces a binary-weighted mechanism that utilizes the advantage values of actions in the offline dataset to guide diffusion model training. This enables a more precise alignment with the dataset's distribution while selectively expanding the boundaries of high-advantage actions. During policy improvement, DIVO dynamically filters high-return-potential actions from the diffusion model, effectively guiding the learned policy toward better performance. This approach achieves a critical balance between conservatism and explorability in offline RL. We evaluate DIVO on the D4RL benchmark and compare it against state-of-the-art baselines. Empirical results demonstrate that DIVO achieves superior performance, delivering significant improvements in average returns across locomotion tasks and outperforming existing methods in the challenging AntMaze domain, where sparse rewards pose a major difficulty.

