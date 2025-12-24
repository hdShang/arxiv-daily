---
layout: default
title: "DiffusionNFT: Online Diffusion Reinforcement with Forward Process"
---

# DiffusionNFT: Online Diffusion Reinforcement with Forward Process

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16117" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16117v1</a>
  <a href="https://arxiv.org/pdf/2509.16117.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16117v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16117v1', 'DiffusionNFT: Online Diffusion Reinforcement with Forward Process')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiwen Zheng, Huayu Chen, Haotian Ye, Haoxiang Wang, Qinsheng Zhang, Kai Jiang, Hang Su, Stefano Ermon, Jun Zhu, Ming-Yu Liu

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出DiffusionNFT，通过前向过程优化扩散模型，实现高效在线强化学习。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `扩散模型` `在线强化学习` `流匹配` `前向过程` `策略优化`

## 📋 核心要点

1. 现有扩散模型在线强化学习方法受限于求解器，存在正向-反向不一致，且难以与无分类器引导集成。
2. DiffusionNFT通过流匹配直接在前向过程上优化扩散模型，对比正负样本定义策略改进方向。
3. 实验表明，DiffusionNFT比FlowGRPO效率提升高达25倍，且无需无分类器引导，性能显著提升。

## 📝 摘要（中文）

在线强化学习在后训练语言模型中至关重要，但由于难以处理的似然性，将其扩展到扩散模型仍然具有挑战性。最近的研究通过离散化逆向采样过程来实现GRPO风格的训练，但它们继承了根本缺陷，包括求解器限制、正向-反向不一致以及与无分类器引导（CFG）的复杂集成。我们引入了Diffusion Negative-aware FineTuning (DiffusionNFT)，这是一种新的在线强化学习范式，它通过流匹配直接在前向过程上优化扩散模型。DiffusionNFT对比了正向和负向生成，以定义一个隐式的策略改进方向，自然地将强化信号整合到监督学习目标中。这种公式允许使用任意黑盒求解器进行训练，消除了对似然估计的需求，并且只需要干净的图像而不是采样轨迹来进行策略优化。在直接比较中，DiffusionNFT比FlowGRPO的效率高出25倍，并且无需CFG。例如，DiffusionNFT在1k步内将GenEval分数从0.24提高到0.98，而FlowGRPO在超过5k步和额外使用CFG的情况下达到0.95。通过利用多个奖励模型，DiffusionNFT显著提高了SD3.5-Medium在每个测试基准中的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散模型在线强化学习中存在的挑战，具体来说，现有方法（如FlowGRPO）依赖于离散化的逆向采样过程，这导致了求解器选择的限制、正向和反向过程的不一致性，以及与无分类器引导（CFG）集成的复杂性。这些问题限制了扩散模型在在线强化学习中的应用。

**核心思路**：DiffusionNFT的核心思路是通过流匹配直接在前向过程上优化扩散模型。它避免了对逆向过程的依赖，从而消除了求解器限制和正向-反向不一致的问题。此外，DiffusionNFT通过对比正向和负向生成样本来定义一个隐式的策略改进方向，将强化学习信号自然地融入到监督学习目标中。

**技术框架**：DiffusionNFT的整体框架包括以下几个主要步骤：1) 使用扩散模型生成图像；2) 使用奖励模型评估生成的图像，得到奖励信号；3) 对比正向（高奖励）和负向（低奖励）的生成样本，计算策略改进方向；4) 利用流匹配方法，在前向过程中优化扩散模型，使其生成更符合奖励目标的图像。该框架不需要对逆向过程进行建模或采样，简化了训练流程。

**关键创新**：DiffusionNFT最重要的技术创新点在于它直接在前向过程上进行策略优化，避免了对逆向过程的依赖。这与现有方法（如FlowGRPO）形成了本质区别，FlowGRPO需要离散化逆向采样过程，并进行复杂的似然估计。DiffusionNFT的创新之处还在于它通过对比正负样本来定义策略改进方向，将强化学习信号自然地融入到监督学习目标中，无需额外的策略梯度估计。

**关键设计**：DiffusionNFT的关键设计包括：1) 使用流匹配损失函数来优化前向过程，使得扩散模型生成的样本更接近目标分布；2) 定义正负样本的选取策略，例如选择奖励最高的k个样本作为正样本，奖励最低的k个样本作为负样本；3) 使用多个奖励模型来提高奖励信号的鲁棒性；4) 采用合适的网络结构来表示扩散模型，例如U-Net。

## 📊 实验亮点

DiffusionNFT在实验中表现出色，与FlowGRPO相比，效率提升高达25倍。例如，DiffusionNFT在1k步内将GenEval分数从0.24提高到0.98，而FlowGRPO需要超过5k步和额外的CFG才能达到0.95。此外，通过利用多个奖励模型，DiffusionNFT显著提高了SD3.5-Medium在所有测试基准上的性能，证明了其有效性和鲁棒性。

## 🎯 应用场景

DiffusionNFT具有广泛的应用前景，例如图像生成、文本生成、机器人控制等。它可以用于优化扩散模型，使其生成更符合用户期望的图像或文本。在机器人控制领域，DiffusionNFT可以用于训练机器人生成更有效的动作序列，从而完成复杂的任务。该研究的实际价值在于提高了扩散模型在在线强化学习中的效率和性能，为扩散模型的应用开辟了新的方向。

## 📄 摘要（原文）

> Online reinforcement learning (RL) has been central to post-training language models, but its extension to diffusion models remains challenging due to intractable likelihoods. Recent works discretize the reverse sampling process to enable GRPO-style training, yet they inherit fundamental drawbacks, including solver restrictions, forward-reverse inconsistency, and complicated integration with classifier-free guidance (CFG). We introduce Diffusion Negative-aware FineTuning (DiffusionNFT), a new online RL paradigm that optimizes diffusion models directly on the forward process via flow matching. DiffusionNFT contrasts positive and negative generations to define an implicit policy improvement direction, naturally incorporating reinforcement signals into the supervised learning objective. This formulation enables training with arbitrary black-box solvers, eliminates the need for likelihood estimation, and requires only clean images rather than sampling trajectories for policy optimization. DiffusionNFT is up to $25\times$ more efficient than FlowGRPO in head-to-head comparisons, while being CFG-free. For instance, DiffusionNFT improves the GenEval score from 0.24 to 0.98 within 1k steps, while FlowGRPO achieves 0.95 with over 5k steps and additional CFG employment. By leveraging multiple reward models, DiffusionNFT significantly boosts the performance of SD3.5-Medium in every benchmark tested.

