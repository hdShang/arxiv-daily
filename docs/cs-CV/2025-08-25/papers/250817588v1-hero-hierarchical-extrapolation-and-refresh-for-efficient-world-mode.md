---
layout: default
title: "HERO: Hierarchical Extrapolation and Refresh for Efficient World Models"
---

# HERO: Hierarchical Extrapolation and Refresh for Efficient World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17588" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17588v1</a>
  <a href="https://arxiv.org/pdf/2508.17588.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17588v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17588v1', 'HERO: Hierarchical Extrapolation and Refresh for Efficient World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Quanjian Song, Xinyu Wang, Donghao Zhou, Jingyu Lin, Cunjian Chen, Yue Ma, Xiu Li

**分类**: cs.CV

**发布日期**: 2025-08-25

**备注**: 12 pages in total

---

## 💡 一句话要点

**提出HERO框架以解决世界模型推理效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `扩散模型` `推理加速` `分层策略` `特征耦合` `虚拟环境` `生成模型`

## 📋 核心要点

1. 现有的生成驱动世界模型在推理时速度较慢，主要由于扩散模型的迭代计算特性。
2. HERO框架通过分层策略加速推理，浅层采用补丁刷新机制，深层则使用线性外推方案。
3. 实验表明，HERO实现了1.73倍的速度提升，同时保持了较高的生成质量，优于现有方法。

## 📝 摘要（中文）

生成驱动的世界模型能够创建沉浸式虚拟环境，但由于扩散模型的迭代特性，推理速度较慢。尽管近期的研究提升了扩散模型的效率，但直接将这些技术应用于世界模型时，常常会导致质量下降。本文提出了HERO，一个无需训练的分层加速框架，旨在提高世界模型的推理效率。HERO通过识别特征耦合现象，采用分层策略加速推理，具体包括在浅层使用补丁刷新机制和在深层使用线性外推方案。实验结果表明，HERO实现了1.73倍的速度提升，且质量下降极小，显著优于现有的扩散加速方法。

## 🔬 方法详解

**问题定义**：本文旨在解决生成驱动世界模型推理效率低下的问题。现有的扩散模型在推理时需要多次迭代计算，导致速度缓慢，且直接应用新技术可能导致生成质量下降。

**核心思路**：HERO框架的核心思路是利用分层策略来加速推理过程。通过识别特征耦合现象，浅层特征具有高时间变异性，而深层特征则更稳定，因此可以采用不同的加速策略。

**技术框架**：HERO框架分为两个主要模块：在浅层，使用补丁刷新机制高效选择需要重新计算的token；在深层，采用线性外推方案直接估计中间特征，从而避免注意力模块和前馈网络的计算。

**关键创新**：HERO的主要创新在于其训练无关的分层加速策略，特别是在浅层和深层采用不同的处理机制，显著提高了推理速度而不损失生成质量。

**关键设计**：在浅层，HERO实现了补丁采样和频率感知跟踪，避免了额外的度量计算，并与FlashAttention兼容；在深层，线性外推方案直接估计特征，完全绕过了注意力模块和前馈网络的计算。

## 📊 实验亮点

实验结果显示，HERO框架在推理速度上实现了1.73倍的提升，同时保持了生成质量的稳定性，显著优于现有的扩散加速方法。这一成果为生成模型的实际应用提供了新的可能性。

## 🎯 应用场景

HERO框架的潜在应用场景包括虚拟现实、游戏开发和自动驾驶等领域，能够显著提升生成模型的推理效率，进而改善用户体验和系统响应速度。未来，HERO可能会推动更高效的世界模型设计，促进智能体在复杂环境中的应用。

## 📄 摘要（原文）

> Generation-driven world models create immersive virtual environments but suffer slow inference due to the iterative nature of diffusion models. While recent advances have improved diffusion model efficiency, directly applying these techniques to world models introduces limitations such as quality degradation. In this paper, we present HERO, a training-free hierarchical acceleration framework tailored for efficient world models. Owing to the multi-modal nature of world models, we identify a feature coupling phenomenon, wherein shallow layers exhibit high temporal variability, while deeper layers yield more stable feature representations. Motivated by this, HERO adopts hierarchical strategies to accelerate inference: (i) In shallow layers, a patch-wise refresh mechanism efficiently selects tokens for recomputation. With patch-wise sampling and frequency-aware tracking, it avoids extra metric computation and remain compatible with FlashAttention. (ii) In deeper layers, a linear extrapolation scheme directly estimates intermediate features. This completely bypasses the computations in attention modules and feed-forward networks. Our experiments show that HERO achieves a 1.73$\times$ speedup with minimal quality degradation, significantly outperforming existing diffusion acceleration methods.

