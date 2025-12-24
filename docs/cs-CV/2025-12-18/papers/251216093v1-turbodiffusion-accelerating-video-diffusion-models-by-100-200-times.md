---
layout: default
title: "TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times"
---

# TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16093" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16093v1</a>
  <a href="https://arxiv.org/pdf/2512.16093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16093v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16093v1', 'TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jintao Zhang, Kaiwen Zheng, Kai Jiang, Haoxu Wang, Ion Stoica, Joseph E. Gonzalez, Jianfei Chen, Jun Zhu

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/thu-ml/TurboDiffusion)

---

## 💡 一句话要点

**TurboDiffusion：通过多重加速策略将视频扩散模型提速100-200倍**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频生成` `扩散模型` `模型加速` `注意力机制` `模型量化` `步骤蒸馏` `稀疏注意力`

## 📋 核心要点

1. 现有视频扩散模型计算成本高昂，限制了其在实际应用中的部署和使用。
2. TurboDiffusion通过注意力加速、步骤蒸馏和模型量化等多重策略，大幅降低计算复杂度。
3. 实验表明，TurboDiffusion在保证视频质量的前提下，实现了100-200倍的加速效果。

## 📝 摘要（中文）

本文提出了一种名为TurboDiffusion的视频生成加速框架，能够在保持视频质量的同时，将端到端扩散生成速度提高100-200倍。TurboDiffusion主要依赖于以下几个加速组件：（1）注意力加速：使用低比特SageAttention和可训练的稀疏线性注意力（SLA）来加速注意力计算。（2）步骤蒸馏：采用rCM进行高效的步骤蒸馏。（3）W8A8量化：将模型参数和激活量化到8位，以加速线性层并压缩模型。此外，TurboDiffusion还包含其他一些工程优化。在Wan2.2-I2V-14B-720P、Wan2.1-T2V-1.3B-480P、Wan2.1-T2V-14B-720P和Wan2.1-T2V-14B-480P模型上进行的实验结果表明，即使在单个RTX 5090 GPU上，TurboDiffusion也能实现100-200倍的视频生成加速，同时保持相当的视频质量。代码和模型已开源。

## 🔬 方法详解

**问题定义**：视频扩散模型在生成高质量视频方面表现出色，但其计算复杂度极高，推理速度慢，难以在资源受限的设备上部署，阻碍了其广泛应用。现有方法在加速方面效果有限，或者会显著降低视频质量。

**核心思路**：TurboDiffusion的核心思路是通过多方面的优化，包括降低注意力计算的复杂度、减少扩散步骤以及量化模型参数，从而在不显著降低视频质量的前提下，大幅提升视频生成的速度。这种多管齐下的方法能够充分利用硬件资源，实现更高的效率。

**技术框架**：TurboDiffusion的整体框架包含以下几个主要模块：1) **注意力加速模块**：使用低比特SageAttention和可训练的稀疏线性注意力（SLA）来减少注意力计算的复杂度。2) **步骤蒸馏模块**：采用rCM进行高效的步骤蒸馏，减少生成视频所需的扩散步骤。3) **量化模块**：将模型参数和激活量化到8位（W8A8），以加速线性层计算并压缩模型大小。此外，还包括一些工程优化，例如kernel优化等。

**关键创新**：TurboDiffusion的关键创新在于其综合利用多种加速技术，并针对视频扩散模型的特点进行了优化。例如，可训练的稀疏线性注意力（SLA）能够自适应地学习重要的注意力模式，从而在减少计算量的同时保持性能。rCM蒸馏方法能够更有效地减少扩散步骤，而不会引入过多的伪影。

**关键设计**：在注意力加速方面，SageAttention使用低比特量化来减少计算量，而SLA则通过学习稀疏的注意力矩阵来减少计算量。rCM蒸馏方法通过引入一个重构损失来提高蒸馏的质量。W8A8量化使用对称量化方案，并针对不同的层进行了不同的量化策略选择。具体的参数设置和损失函数细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16093v1/src/figs/original/outputs_1.3B/frames/12-1.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16093v1/src/figs/turbodiffusion/outputs_1.3B/frames/12-1.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16093v1/src/figs/i2v/original/outputs_A14B_720p/frames/1-1.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TurboDiffusion在多个视频生成模型上实现了显著的加速效果，达到了100-200倍的加速，同时保持了与原始模型相当的视频质量。即使在单个RTX 5090 GPU上，也能实现如此高的加速比，证明了该框架的有效性和实用性。开源的代码和模型方便了研究人员和开发者进行进一步的研究和应用。

## 🎯 应用场景

TurboDiffusion具有广泛的应用前景，包括视频编辑、游戏开发、虚拟现实、社交媒体等领域。它可以加速视频内容的生成，降低计算成本，使得在移动设备或云端进行高质量视频生成成为可能。未来，TurboDiffusion可以进一步扩展到其他生成模型，例如图像生成、音频生成等。

## 📄 摘要（原文）

> We introduce TurboDiffusion, a video generation acceleration framework that can speed up end-to-end diffusion generation by 100-200x while maintaining video quality. TurboDiffusion mainly relies on several components for acceleration: (1) Attention acceleration: TurboDiffusion uses low-bit SageAttention and trainable Sparse-Linear Attention (SLA) to speed up attention computation. (2) Step distillation: TurboDiffusion adopts rCM for efficient step distillation. (3) W8A8 quantization: TurboDiffusion quantizes model parameters and activations to 8 bits to accelerate linear layers and compress the model. In addition, TurboDiffusion incorporates several other engineering optimizations.
>   We conduct experiments on the Wan2.2-I2V-14B-720P, Wan2.1-T2V-1.3B-480P, Wan2.1-T2V-14B-720P, and Wan2.1-T2V-14B-480P models. Experimental results show that TurboDiffusion achieves 100-200x speedup for video generation even on a single RTX 5090 GPU, while maintaining comparable video quality. The GitHub repository, which includes model checkpoints and easy-to-use code, is available at https://github.com/thu-ml/TurboDiffusion.

