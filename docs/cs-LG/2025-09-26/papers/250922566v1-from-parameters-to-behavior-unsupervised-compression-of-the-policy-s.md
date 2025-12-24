---
layout: default
title: "From Parameters to Behavior: Unsupervised Compression of the Policy Space"
---

# From Parameters to Behavior: Unsupervised Compression of the Policy Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22566" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22566v1</a>
  <a href="https://arxiv.org/pdf/2509.22566.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22566v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22566v1', 'From Parameters to Behavior: Unsupervised Compression of the Policy Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Davide Tenedini, Riccardo Zamboni, Mirco Mutti, Marcello Restelli

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出无监督方法压缩策略空间以提高深度强化学习效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `策略优化` `无监督学习` `参数压缩` `行为重构` `生成模型` `多任务学习`

## 📋 核心要点

1. 现有的深度强化学习方法在高维参数空间中优化策略，导致样本效率低下，尤其在多任务环境中更为明显。
2. 本文提出了一种无监督的方法，通过将策略参数空间压缩到低维潜在空间，优化行为重构损失以组织潜在空间。
3. 在连续控制任务中，实验表明该方法能够将策略网络的参数化压缩至五个数量级，同时保持其表达能力。

## 📝 摘要（中文）

尽管深度强化学习（DRL）取得了显著成功，但其样本效率低下的问题依然突出。本文认为，这种低效源于直接在高维且高度冗余的参数空间中优化策略。为此，作者提出了一种新颖的无监督方法，将策略参数空间压缩到低维潜在空间。通过优化行为重构损失，训练生成模型，使潜在空间按功能相似性组织，而非参数化的接近性。实验结果表明，在连续控制领域，该方法能够将标准策略网络的参数化压缩至五个数量级，同时保持大部分表达能力，并支持通过潜在空间进行任务特定的适应。

## 🔬 方法详解

**问题定义**：本文旨在解决深度强化学习中策略优化的样本效率低下问题，现有方法在高维且冗余的参数空间中进行优化，导致效率低下，尤其在多任务设置中更为明显。

**核心思路**：作者提出了一种无监督的策略空间压缩方法，通过将策略参数空间映射到低维潜在空间，优化行为重构损失，使潜在空间按功能相似性组织，而非简单的参数接近性。

**技术框架**：整体架构包括生成模型的训练，该模型将低维潜在空间映射回高维参数空间。主要模块包括潜在空间的构建、行为重构损失的优化和策略生成。

**关键创新**：最重要的创新在于通过无监督学习将策略参数化压缩至低维潜在空间，显著提高了样本效率，并允许在潜在空间中进行任务特定的适应。

**关键设计**：在技术细节上，损失函数设计为行为重构损失，确保潜在空间的功能相似性；网络结构上，采用生成模型来实现潜在空间与参数空间的映射。

## 📊 实验亮点

实验结果显示，所提出的方法能够将标准策略网络的参数化压缩至五个数量级，同时保持大部分表达能力。这一压缩显著提高了样本效率，并支持在潜在空间中进行任务特定的适应，展示了其在连续控制任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、游戏智能体和多任务学习等。通过提高深度强化学习的样本效率，该方法能够加速智能体的训练过程，降低对大量数据的依赖，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Despite its recent successes, Deep Reinforcement Learning (DRL) is notoriously sample-inefficient. We argue that this inefficiency stems from the standard practice of optimizing policies directly in the high-dimensional and highly redundant parameter space $Θ$. This challenge is greatly compounded in multi-task settings. In this work, we develop a novel, unsupervised approach that compresses the policy parameter space $Θ$ into a low-dimensional latent space $\mathcal{Z}$. We train a generative model $g:\mathcal{Z}\toΘ$ by optimizing a behavioral reconstruction loss, which ensures that the latent space is organized by functional similarity rather than proximity in parameterization. We conjecture that the inherent dimensionality of this manifold is a function of the environment's complexity, rather than the size of the policy network. We validate our approach in continuous control domains, showing that the parameterization of standard policy networks can be compressed up to five orders of magnitude while retaining most of its expressivity. As a byproduct, we show that the learned manifold enables task-specific adaptation via Policy Gradient operating in the latent space $\mathcal{Z}$.

