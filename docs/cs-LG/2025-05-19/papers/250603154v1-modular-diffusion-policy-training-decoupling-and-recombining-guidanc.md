---
layout: default
title: Modular Diffusion Policy Training: Decoupling and Recombining Guidance and Diffusion for Offline RL
---

# Modular Diffusion Policy Training: Decoupling and Recombining Guidance and Diffusion for Offline RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03154" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03154v1</a>
  <a href="https://arxiv.org/pdf/2506.03154.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03154v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03154v1', 'Modular Diffusion Policy Training: Decoupling and Recombining Guidance and Diffusion for Offline RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoyang Chen, Cody Fleming

**分类**: cs.LG

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出模块化扩散策略训练以优化离线强化学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `离线强化学习` `模块化训练` `扩散模型` `引导模块` `样本效率` `可转移性` `价值估计`

## 📋 核心要点

1. 现有方法在早期阶段依赖于引导模块和扩散模型的联合训练，导致引导不准确和学习信号噪声过大。
2. 论文提出将引导模块与扩散模型解耦的模块化训练方法，首先独立训练引导模块作为价值估计器，然后引导扩散模型。
3. 实验结果表明，使用两个独立训练的引导模型显著降低了标准化得分方差，展示了强大的模块化和可转移性。

## 📝 摘要（中文）

无分类器引导在基于扩散的强化学习中展现出强大的潜力。然而，现有方法依赖于引导模块和扩散模型的联合训练，这在早期阶段可能导致不理想的结果。本文提出模块化训练方法，将引导模块与扩散模型解耦，基于三个关键发现：引导的必要性、引导优先的扩散训练和跨模块的可转移性。通过独立训练的引导模型，显著降低了标准化得分方差，展示了模块化和可重用性的强大潜力。我们在D4RL基准上提供了理论依据和实证验证，提出了一种新的离线强化学习训练范式。

## 🔬 方法详解

**问题定义**：本文解决了现有离线强化学习方法中引导模块与扩散模型联合训练的不足，特别是在早期阶段引导不准确导致的学习信号噪声问题。

**核心思路**：论文的核心思路是将引导模块与扩散模型解耦，通过独立训练引导模块来优化学习过程，从而提高样本效率和最终性能。

**技术框架**：整体架构包括三个主要阶段：首先独立训练引导模块作为价值估计器；然后将其冻结并用于指导扩散模型；最后在推理阶段应用独立训练的引导模型。

**关键创新**：最重要的技术创新在于引导模块的独立训练和跨模块的可转移性，允许不同算法间的引导模块重用，显著提高了性能和效率。

**关键设计**：关键设计包括引导模块的损失函数设置、网络结构的选择，以及在训练和推理阶段的参数调整，以确保引导模块的有效性和稳定性。

## 📊 实验亮点

实验结果显示，使用独立训练的引导模型可以将标准化得分方差降低86%，并且不同算法间的引导模块可以直接重用，展示了强大的模块化和可转移性，显著提升了样本效率和最终性能。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、游戏智能体等，能够有效提升离线强化学习的性能和效率。未来，模块化的训练管道可能会推动更复杂任务的解决方案，促进智能体在动态环境中的适应能力。

## 📄 摘要（原文）

> Classifier free guidance has shown strong potential in diffusion-based reinforcement learning. However, existing methods rely on joint training of the guidance module and the diffusion model, which can be suboptimal during the early stages when the guidance is inaccurate and provides noisy learning signals. In offline RL, guidance depends solely on offline data: observations, actions, and rewards, and is independent of the policy module's behavior, suggesting that joint training is not required. This paper proposes modular training methods that decouple the guidance module from the diffusion model, based on three key findings:
>   Guidance Necessity: We explore how the effectiveness of guidance varies with the training stage and algorithm choice, uncovering the roles of guidance and diffusion. A lack of good guidance in the early stage presents an opportunity for optimization.
>   Guidance-First Diffusion Training: We introduce a method where the guidance module is first trained independently as a value estimator, then frozen to guide the diffusion model using classifier-free reward guidance. This modularization reduces memory usage, improves computational efficiency, and enhances both sample efficiency and final performance.
>   Cross-Module Transferability: Applying two independently trained guidance models, one during training and the other during inference, can significantly reduce normalized score variance (e.g., reducing IQR by 86%). We show that guidance modules trained with one algorithm (e.g., IDQL) can be directly reused with another (e.g., DQL), with no additional training required, demonstrating baseline-level performance as well as strong modularity and transferability.
>   We provide theoretical justification and empirical validation on bullet D4RL benchmarks. Our findings suggest a new paradigm for offline RL: modular, reusable, and composable training pipelines.

