---
layout: default
title: "Revoking Amnesia: RL-based Trajectory Optimization to Resurrect Erased Concepts in Diffusion Models"
---

# Revoking Amnesia: RL-based Trajectory Optimization to Resurrect Erased Concepts in Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03302" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03302v1</a>
  <a href="https://arxiv.org/pdf/2510.03302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03302v1', 'Revoking Amnesia: RL-based Trajectory Optimization to Resurrect Erased Concepts in Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daiheng Gao, Nanxiang Jiang, Andi Zhang, Shilin Lu, Yufei Tang, Wenbo Zhou, Weiming Zhang, Zhaoxin Fan

**分类**: cs.LG, cs.CV

**发布日期**: 2025-09-30

**备注**: 21 pages, 10 figures

---

## 💡 一句话要点

**提出RevAm，通过强化学习优化扩散模型采样轨迹，恢复被擦除的概念**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `扩散模型` `概念擦除` `强化学习` `轨迹优化` `安全性` `内容生成` `GRPO` `概念恢复`

## 📋 核心要点

1. 现有概念擦除方法在新型扩散模型中效果下降，无法真正实现概念的遗忘，存在安全隐患。
2. 提出RevAm框架，利用强化学习优化扩散模型的采样轨迹，从而恢复被擦除的概念，无需修改模型权重。
3. 实验表明，RevAm能高效恢复概念，计算时间减少10倍，揭示了现有安全机制的脆弱性。

## 📝 摘要（中文）

为了安全和版权考虑，概念擦除技术被广泛应用于文本到图像（T2I）扩散模型中，以防止生成不当内容。然而，随着模型发展到Flux等下一代架构，现有的擦除方法（如ESD、UCE、AC）的效果降低，引发了对其真正机制的质疑。通过系统分析，我们发现概念擦除仅创造了一种“失忆”的错觉：这些方法并非真正遗忘，而是使采样轨迹偏离目标概念，使得擦除本质上是可逆的。这一发现促使我们区分表面安全和真正的概念移除。本文提出了RevAm（Revoking Amnesia），一个基于强化学习的轨迹优化框架，通过动态引导去噪过程来恢复被擦除的概念，而无需修改模型权重。通过将Group Relative Policy Optimization (GRPO) 应用于扩散模型，RevAm通过轨迹级别的奖励探索多样化的恢复轨迹，克服了限制现有方法的局部最优。大量实验表明，RevAm实现了卓越的概念恢复保真度，同时将计算时间减少了10倍，揭示了当前安全机制的关键漏洞，并强调了需要超越轨迹操作的更强大的擦除技术。

## 🔬 方法详解

**问题定义**：论文旨在解决文本到图像扩散模型中概念擦除技术失效的问题。现有方法（如ESD、UCE、AC）在新型扩散模型架构下，无法彻底擦除概念，仅仅是使生成轨迹偏离目标概念，存在被轻易恢复的风险。这些方法的痛点在于缺乏对采样轨迹的全局优化，容易陷入局部最优，导致擦除效果不佳。

**核心思路**：论文的核心思路是将概念恢复问题建模为一个强化学习任务，通过优化扩散模型的采样轨迹，引导其重新生成被擦除的概念。核心在于利用强化学习的探索能力，克服局部最优，找到更有效的概念恢复路径。这种方法无需修改模型权重，而是通过外部控制来改变生成过程。

**技术框架**：RevAm框架主要包含以下几个模块：1) 扩散模型：作为生成图像的基础模型。2) 强化学习智能体：负责学习优化采样轨迹的策略。3) 奖励函数：用于评估生成图像与目标概念的相似度，指导智能体学习。4) 轨迹优化器：根据智能体的策略，调整扩散模型的采样过程，生成新的图像。整体流程是：首先，扩散模型生成初始图像；然后，智能体根据当前图像状态，选择一个动作（即对采样轨迹的调整）；接着，扩散模型根据该动作生成新的图像；最后，奖励函数评估新图像与目标概念的相似度，并将奖励反馈给智能体，用于更新策略。

**关键创新**：论文最重要的技术创新点在于将强化学习引入到扩散模型的采样轨迹优化中，从而实现对被擦除概念的恢复。与现有方法相比，RevAm能够通过探索多样化的轨迹，克服局部最优，实现更彻底的概念恢复。此外，论文还针对扩散模型的特点，对Group Relative Policy Optimization (GRPO) 算法进行了改进，使其更适合于处理连续的采样轨迹。

**关键设计**：论文的关键设计包括：1) 奖励函数的设计：奖励函数需要能够准确评估生成图像与目标概念的相似度，论文可能采用了CLIP相似度等指标。2) 智能体的策略网络结构：策略网络需要能够根据当前图像状态，输出合适的动作，论文可能采用了卷积神经网络等结构。3) GRPO算法的参数设置：包括学习率、折扣因子等，这些参数需要根据具体任务进行调整。

## 📊 实验亮点

实验结果表明，RevAm能够以更高的保真度恢复被擦除的概念，并且计算时间比现有方法减少了10倍。这表明RevAm在概念恢复方面具有显著的优势，并揭示了当前安全机制的脆弱性。具体的性能数据（如FID分数、CLIP相似度等）将在论文中详细展示。

## 🎯 应用场景

该研究成果可应用于评估和改进现有扩散模型的安全机制，提高内容生成的安全性。同时，该方法也可用于图像编辑和修复，例如恢复图像中被恶意擦除的内容。此外，该研究对于理解扩散模型的内部机制和控制生成过程具有重要意义，为未来的研究方向提供了新的思路。

## 📄 摘要（原文）

> Concept erasure techniques have been widely deployed in T2I diffusion models to prevent inappropriate content generation for safety and copyright considerations. However, as models evolve to next-generation architectures like Flux, established erasure methods (\textit{e.g.}, ESD, UCE, AC) exhibit degraded effectiveness, raising questions about their true mechanisms. Through systematic analysis, we reveal that concept erasure creates only an illusion of ``amnesia": rather than genuine forgetting, these methods bias sampling trajectories away from target concepts, making the erasure fundamentally reversible. This insight motivates the need to distinguish superficial safety from genuine concept removal. In this work, we propose \textbf{RevAm} (\underline{Rev}oking \underline{Am}nesia), an RL-based trajectory optimization framework that resurrects erased concepts by dynamically steering the denoising process without modifying model weights. By adapting Group Relative Policy Optimization (GRPO) to diffusion models, RevAm explores diverse recovery trajectories through trajectory-level rewards, overcoming local optima that limit existing methods. Extensive experiments demonstrate that RevAm achieves superior concept resurrection fidelity while reducing computational time by 10$\times$, exposing critical vulnerabilities in current safety mechanisms and underscoring the need for more robust erasure techniques beyond trajectory manipulation.

