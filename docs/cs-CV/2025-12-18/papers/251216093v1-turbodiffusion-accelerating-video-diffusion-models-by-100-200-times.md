---
layout: default
title: TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times
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

**TurboDiffusion：通过多重加速策略实现视频扩散模型100-200倍的加速。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频生成` `扩散模型` `模型加速` `注意力机制` `模型量化` `步骤蒸馏` `低比特计算`

## 📋 核心要点

1. 视频扩散模型计算成本高昂，限制了其在实际应用中的部署和使用。
2. TurboDiffusion通过注意力加速、步骤蒸馏和模型量化等多重策略，显著降低计算复杂度。
3. 实验表明，TurboDiffusion在保证视频质量的前提下，实现了100-200倍的加速效果。

## 📝 摘要（中文）

TurboDiffusion是一个视频生成加速框架，能够在保持视频质量的同时，将端到端扩散生成速度提高100-200倍。TurboDiffusion主要依赖于以下几个加速组件：（1）注意力加速：TurboDiffusion使用低比特SageAttention和可训练的稀疏线性注意力（SLA）来加速注意力计算。（2）步骤蒸馏：TurboDiffusion采用rCM进行高效的步骤蒸馏。（3）W8A8量化：TurboDiffusion将模型参数和激活量化为8位，以加速线性层并压缩模型。此外，TurboDiffusion还包含其他一些工程优化。我们在Wan2.2-I2V-14B-720P、Wan2.1-T2V-1.3B-480P、Wan2.1-T2V-14B-720P和Wan2.1-T2V-14B-480P模型上进行了实验。实验结果表明，即使在单个RTX 5090 GPU上，TurboDiffusion也能实现100-200倍的视频生成加速，同时保持相当的视频质量。包含模型检查点和易于使用的代码的GitHub存储库可在https://github.com/thu-ml/TurboDiffusion上找到。

## 🔬 方法详解

**问题定义**：现有视频扩散模型计算量巨大，推理速度慢，难以满足实时或快速生成视频的需求。尤其是在高分辨率视频生成时，计算瓶颈更加明显。因此，如何加速视频扩散模型的推理过程，同时保持生成视频的质量，是一个重要的研究问题。

**核心思路**：TurboDiffusion的核心思路是通过多方面的优化，包括算法层面的注意力机制加速和步骤蒸馏，以及系统层面的模型量化和工程优化，来降低计算复杂度，从而实现整体的加速效果。这种多管齐下的方法能够在不显著降低视频质量的前提下，大幅提升生成速度。

**技术框架**：TurboDiffusion的整体框架主要包含以下几个模块：1) **注意力加速模块**：使用低比特SageAttention和可训练的稀疏线性注意力（SLA）来减少注意力计算的复杂度。2) **步骤蒸馏模块**：采用rCM（未知具体含义，原文如此）进行高效的步骤蒸馏，减少生成视频所需的迭代步骤。3) **模型量化模块**：将模型参数和激活量化为8位（W8A8），以加速线性层计算并压缩模型大小。4) **工程优化模块**：包含一系列其他的工程优化手段，进一步提升整体性能。

**关键创新**：TurboDiffusion的关键创新在于其综合利用多种加速策略，并针对视频扩散模型的特点进行了优化。例如，稀疏线性注意力（SLA）能够有效地减少注意力计算中的冗余，而步骤蒸馏则能够减少生成视频所需的迭代次数。此外，W8A8量化能够在保证模型精度的前提下，显著降低计算量和内存占用。多种优化策略的结合是TurboDiffusion能够实现显著加速的关键。

**关键设计**：论文中提到了SageAttention、稀疏线性注意力（SLA）、rCM步骤蒸馏和W8A8量化等关键技术，但具体的技术细节（例如SLA的具体稀疏模式、rCM的具体实现方式、量化的具体策略等）并未详细描述。这些细节对于理解TurboDiffusion的性能至关重要，但目前信息不足，无法进行深入分析。

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

TurboDiffusion在多个视频生成模型上实现了100-200倍的加速，同时保持了与原始模型相当的视频质量。即使在单个RTX 5090 GPU上，也能达到如此显著的加速效果，表明TurboDiffusion具有很高的实用价值。开源的代码和模型检查点也方便了其他研究者和开发者使用和改进。

## 🎯 应用场景

TurboDiffusion的加速技术可以广泛应用于视频生成、视频编辑、游戏开发、虚拟现实等领域。更快的视频生成速度可以提升用户体验，降低计算成本，并促进相关应用的普及。例如，在游戏开发中，可以利用TurboDiffusion快速生成游戏场景和角色动画；在虚拟现实中，可以实时生成高质量的虚拟环境。

## 📄 摘要（原文）

> We introduce TurboDiffusion, a video generation acceleration framework that can speed up end-to-end diffusion generation by 100-200x while maintaining video quality. TurboDiffusion mainly relies on several components for acceleration: (1) Attention acceleration: TurboDiffusion uses low-bit SageAttention and trainable Sparse-Linear Attention (SLA) to speed up attention computation. (2) Step distillation: TurboDiffusion adopts rCM for efficient step distillation. (3) W8A8 quantization: TurboDiffusion quantizes model parameters and activations to 8 bits to accelerate linear layers and compress the model. In addition, TurboDiffusion incorporates several other engineering optimizations.
>   We conduct experiments on the Wan2.2-I2V-14B-720P, Wan2.1-T2V-1.3B-480P, Wan2.1-T2V-14B-720P, and Wan2.1-T2V-14B-480P models. Experimental results show that TurboDiffusion achieves 100-200x speedup for video generation even on a single RTX 5090 GPU, while maintaining comparable video quality. The GitHub repository, which includes model checkpoints and easy-to-use code, is available at https://github.com/thu-ml/TurboDiffusion.

