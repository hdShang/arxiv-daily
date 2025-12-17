---
layout: default
title: MoLingo: Motion-Language Alignment for Text-to-Motion Generation
---

# MoLingo: Motion-Language Alignment for Text-to-Motion Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13840" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13840</a>
  <a href="https://arxiv.org/pdf/2512.13840.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13840" onclick="toggleFavorite(this, '2512.13840', 'MoLingo: Motion-Language Alignment for Text-to-Motion Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yannan He, Garvita Tiwari, Xiaohan Zhang, Pankaj Bora, Tolga Birdal, Jan Eric Lenssen, Gerard Pons-Moll

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**MoLingo：通过运动-语言对齐实现文本到动作生成，达到新的SOTA**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `文本到动作生成` `运动生成` `扩散模型` `语义对齐` `交叉注意力`

## 📋 核心要点

1. 现有文本到动作生成方法在语义对齐的潜在空间构建和文本条件注入方面存在不足，影响了生成动作的真实性和文本一致性。
2. MoLingo通过训练语义对齐的运动编码器，并结合多token交叉注意力机制，增强了潜在空间的语义表达能力和文本条件的有效性。
3. 实验结果表明，MoLingo在人体运动生成任务上取得了显著的性能提升，并在标准指标和用户研究中均达到了新的state-of-the-art。

## 📝 摘要（中文）

本文提出了一种名为MoLingo的文本到动作(T2M)模型，该模型通过在连续潜在空间中去噪来生成逼真、栩栩如生的人体运动。现有工作主要在潜在空间中进行扩散，要么一次性处理整个潜在空间，要么自回归地处理多个潜在空间。本文研究了如何使连续运动潜在空间的扩散效果最佳。我们关注两个问题：(1)如何构建语义对齐的潜在空间，使扩散更有效；(2)如何最好地注入文本条件，使运动紧密遵循描述。我们提出了一种语义对齐的运动编码器，该编码器使用帧级别的文本标签进行训练，以便具有相似文本含义的潜在变量保持接近，从而使潜在空间更适合扩散。我们还将单token条件与多token交叉注意力方案进行了比较，发现交叉注意力可以提供更好的运动真实感和文本-运动对齐。凭借语义对齐的潜在变量、自回归生成和交叉注意力文本条件，我们的模型在标准指标和用户研究中，在人体运动生成方面达到了新的state-of-the-art。我们将发布我们的代码和模型，以供进一步研究和下游使用。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到动作生成任务中，生成动作的真实性和与文本描述一致性不足的问题。现有方法在构建语义对齐的运动潜在空间以及有效利用文本信息方面存在局限性，导致生成的动作不够自然，或者与文本描述不符。

**核心思路**：MoLingo的核心思路是通过构建一个语义对齐的运动潜在空间，并采用多token交叉注意力机制来更好地融合文本信息，从而提高生成动作的真实性和文本一致性。语义对齐的潜在空间使得具有相似语义的动作在潜在空间中更加接近，有利于扩散模型的学习和生成。交叉注意力机制能够更精细地捕捉文本信息，并将其融入到动作生成过程中。

**技术框架**：MoLingo的整体框架包含以下几个主要模块：1) 运动编码器：将运动数据编码到潜在空间中；2) 文本编码器：将文本描述编码为文本特征；3) 扩散模型：在潜在空间中进行去噪，生成新的运动；4) 文本条件注入模块：将文本特征融入到扩散模型的生成过程中。该框架采用自回归生成的方式，逐步生成运动序列。

**关键创新**：MoLingo的关键创新在于：1) 提出了语义对齐的运动编码器，通过帧级别的文本标签训练，使得潜在空间具有更好的语义表达能力；2) 采用了多token交叉注意力机制，能够更有效地利用文本信息，提高生成动作的文本一致性。

**关键设计**：在语义对齐的运动编码器中，使用了对比学习损失，使得具有相似文本描述的运动在潜在空间中更加接近。在多token交叉注意力机制中，使用了多个注意力头，以捕捉文本信息的不同方面。扩散模型采用了标准的扩散模型结构，并使用余弦噪声调度策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13840/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MoLingo在HumanML3D和KIT-ML数据集上进行了评估，并在多个指标上取得了显著的提升。例如，在HumanML3D数据集上，MoLingo在FID指标上优于现有方法，并在用户研究中获得了更高的偏好度。这些结果表明，MoLingo能够生成更真实、更符合文本描述的人体运动。

## 🎯 应用场景

MoLingo在游戏开发、虚拟现实、动画制作等领域具有广泛的应用前景。它可以根据文本描述自动生成逼真的人体运动，从而降低了人工制作运动的成本和时间。此外，MoLingo还可以用于人机交互，例如，用户可以通过语音或文本指令控制虚拟角色的运动。

## 📄 摘要（原文）

> We introduce MoLingo, a text-to-motion (T2M) model that generates realistic, lifelike human motion by denoising in a continuous latent space. Recent works perform latent space diffusion, either on the whole latent at once or auto-regressively over multiple latents. In this paper, we study how to make diffusion on continuous motion latents work best. We focus on two questions: (1) how to build a semantically aligned latent space so diffusion becomes more effective, and (2) how to best inject text conditioning so the motion follows the description closely. We propose a semantic-aligned motion encoder trained with frame-level text labels so that latents with similar text meaning stay close, which makes the latent space more diffusion-friendly. We also compare single-token conditioning with a multi-token cross-attention scheme and find that cross-attention gives better motion realism and text-motion alignment. With semantically aligned latents, auto-regressive generation, and cross-attention text conditioning, our model sets a new state of the art in human motion generation on standard metrics and in a user study. We will release our code and models for further research and downstream usage.

