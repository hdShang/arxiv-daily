---
layout: default
title: From Competition to Synergy: Unlocking Reinforcement Learning for Subject-Driven Image Generation
---

# From Competition to Synergy: Unlocking Reinforcement Learning for Subject-Driven Image Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.18263" class="toolbar-btn" target="_blank">📄 arXiv: 2510.18263v1</a>
  <a href="https://arxiv.org/pdf/2510.18263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18263v1" onclick="toggleFavorite(this, '2510.18263v1', 'From Competition to Synergy: Unlocking Reinforcement Learning for Subject-Driven Image Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziwei Huang, Ying Shu, Hao Fang, Quanyu Long, Wenya Wang, Qiushi Guo, Tiezheng Ge, Leilei Gan

**分类**: cs.LG, cs.CV, cs.GR

**发布日期**: 2025-10-21

---

## 💡 一句话要点

**提出Customized-GRPO，解决主体驱动图像生成中保真度和可编辑性的trade-off问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `主体驱动图像生成` `强化学习` `扩散模型` `奖励塑造` `动态加权`

## 📋 核心要点

1. 主体驱动图像生成需要在身份保持和提示遵循之间权衡，现有方法难以兼顾。
2. Customized-GRPO通过协同感知奖励塑造和时间感知动态加权，优化强化学习过程。
3. 实验表明，该方法显著优于现有基线，在保真度和可编辑性上取得了更好的平衡。

## 📝 摘要（中文）

主体驱动的图像生成模型面临着身份保持（保真度）和提示遵循（可编辑性）之间的根本权衡。在线强化学习（RL），特别是GPRO，为此提供了一个有希望的解决方案。然而，我们发现简单地应用GRPO会导致竞争性退化，因为具有静态权重的奖励的简单线性聚合会导致冲突的梯度信号，并与扩散过程的时间动态不一致。为了克服这些限制，我们提出了Customized-GRPO，这是一个新颖的框架，包含两个关键创新：（i）协同感知奖励塑造（SARS），一种非线性机制，它明确地惩罚冲突的奖励信号并放大协同的奖励信号，从而提供更清晰和更果断的梯度。（ii）时间感知动态加权（TDW），它通过优先考虑早期阶段的提示遵循和后期阶段的身份保持，使优化压力与模型的时间动态保持一致。大量的实验表明，我们的方法明显优于朴素的GRPO基线，成功地减轻了竞争性退化。我们的模型实现了卓越的平衡，生成既保留了关键身份特征又准确地遵循复杂文本提示的图像。

## 🔬 方法详解

**问题定义**：主体驱动图像生成旨在根据给定的主体图像和文本提示生成新的图像。现有方法在身份保持（保真度）和提示遵循（可编辑性）之间存在trade-off。简单地应用强化学习方法（如GPRO）会导致梯度冲突和与扩散模型时间动态的不匹配，从而导致性能下降。

**核心思路**：Customized-GRPO的核心思路是通过定制化的奖励塑造和动态权重调整，优化强化学习过程，从而在身份保持和提示遵循之间取得更好的平衡。具体来说，它通过非线性方式处理奖励信号，并根据扩散过程的时间步调整优化重点。

**技术框架**：Customized-GRPO框架主要包含两个关键模块：协同感知奖励塑造（SARS）和时间感知动态加权（TDW）。SARS模块用于处理来自不同奖励函数的信号，通过非线性方式放大协同信号并抑制冲突信号。TDW模块根据扩散过程的时间步动态调整身份保持和提示遵循的权重，早期更注重提示遵循，后期更注重身份保持。

**关键创新**：Customized-GRPO的关键创新在于：(1) 提出了协同感知奖励塑造（SARS），它能够有效地处理来自不同奖励函数的冲突信号，并提供更清晰的梯度。(2) 提出了时间感知动态加权（TDW），它能够根据扩散过程的时间步动态调整优化重点，从而更好地适应扩散模型的时间动态。与现有方法相比，Customized-GRPO能够更好地平衡身份保持和提示遵循。

**关键设计**：SARS模块使用非线性函数来处理奖励信号，具体形式未知（论文未明确给出）。TDW模块使用时间步的函数来动态调整权重，具体形式未知（论文未明确给出）。损失函数是强化学习中的标准损失函数，但奖励信号经过了SARS处理，权重经过了TDW调整。网络结构基于现有的扩散模型架构，没有进行显著修改。

## 📊 实验亮点

实验结果表明，Customized-GRPO显著优于朴素的GRPO基线，在身份保持和提示遵循方面都取得了更好的性能。具体性能数据未知（论文摘要未提供具体数值），但强调了该方法成功减轻了竞争性退化，实现了卓越的平衡。

## 🎯 应用场景

该研究成果可应用于图像编辑、内容创作、虚拟人物生成等领域。例如，用户可以上传一张人脸照片，并输入一段文字描述，生成具有该人脸特征并符合文字描述的新图像。该技术在游戏开发、广告设计、社交媒体等领域具有广泛的应用前景，能够降低创作成本，提高创作效率。

## 📄 摘要（原文）

> Subject-driven image generation models face a fundamental trade-off between identity preservation (fidelity) and prompt adherence (editability). While online reinforcement learning (RL), specifically GPRO, offers a promising solution, we find that a naive application of GRPO leads to competitive degradation, as the simple linear aggregation of rewards with static weights causes conflicting gradient signals and a misalignment with the temporal dynamics of the diffusion process. To overcome these limitations, we propose Customized-GRPO, a novel framework featuring two key innovations: (i) Synergy-Aware Reward Shaping (SARS), a non-linear mechanism that explicitly penalizes conflicted reward signals and amplifies synergistic ones, providing a sharper and more decisive gradient. (ii) Time-Aware Dynamic Weighting (TDW), which aligns the optimization pressure with the model's temporal dynamics by prioritizing prompt-following in the early, identity preservation in the later. Extensive experiments demonstrate that our method significantly outperforms naive GRPO baselines, successfully mitigating competitive degradation. Our model achieves a superior balance, generating images that both preserve key identity features and accurately adhere to complex textual prompts.

