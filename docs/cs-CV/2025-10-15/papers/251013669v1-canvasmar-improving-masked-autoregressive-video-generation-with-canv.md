---
layout: default
title: CanvasMAR: Improving Masked Autoregressive Video Generation With Canvas
---

# CanvasMAR: Improving Masked Autoregressive Video Generation With Canvas

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13669" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13669v1</a>
  <a href="https://arxiv.org/pdf/2510.13669.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13669v1" onclick="toggleFavorite(this, '2510.13669v1', 'CanvasMAR: Improving Masked Autoregressive Video Generation With Canvas')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zian Li, Muhan Zhang

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-15

---

## 💡 一句话要点

**CanvasMAR：通过画布机制改进掩码自回归视频生成，解决慢启动和误差累积问题。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `视频生成` `掩码自回归模型` `全局先验` `画布机制` `无分类器引导` `Kinetics-600` `BAIR`

## 📋 核心要点

1. 视频掩码自回归模型存在慢启动问题，缺乏早期采样阶段的结构化全局先验。
2. CanvasMAR通过引入画布机制，即下一帧的模糊全局预测，为掩码生成提供初始结构。
3. 实验表明，CanvasMAR能以更少的自回归步骤生成高质量视频，并在Kinetics-600上表现出色。

## 📝 摘要（中文）

本文提出CanvasMAR，一种新型视频掩码自回归模型，旨在缓解视频生成中常见的慢启动和误差累积问题。该模型引入了一种画布机制，即对下一帧进行模糊的全局预测，并将其作为掩码生成的起点。画布在采样的早期阶段提供全局结构，从而实现更快、更连贯的帧合成。此外，本文还引入了组合式的无分类器引导，共同扩大空间（画布）和时间条件，并采用基于噪声的画布增强来提高鲁棒性。在BAIR和Kinetics-600基准测试上的实验表明，CanvasMAR能够以更少的自回归步骤生成高质量的视频。该方法在Kinetics-600数据集上实现了自回归模型中的卓越性能，并与基于扩散的方法相媲美。

## 🔬 方法详解

**问题定义**：视频掩码自回归（MAR）模型在视频生成中面临两个主要问题：一是慢启动问题，由于早期采样阶段缺乏结构化的全局先验；二是误差累积问题，误差在空间和时间维度上的自回归过程中不断累积，导致生成质量下降。

**核心思路**：CanvasMAR的核心思路是引入一个“画布”（Canvas）机制，即首先对下一帧进行一个模糊的全局预测，然后将这个模糊的预测作为后续掩码自回归生成的起点。这个画布提供了一个全局的结构化先验，从而加速了生成过程，并减少了误差累积。

**技术框架**：CanvasMAR的整体框架包括以下几个主要步骤：1) 首先，模型预测下一帧的模糊画布；2) 然后，使用这个画布作为条件，进行掩码自回归生成，逐步完善细节；3) 此外，还使用了组合式的无分类器引导，同时利用空间（画布）和时间信息进行条件控制；4) 最后，采用基于噪声的画布增强，提高模型的鲁棒性。

**关键创新**：CanvasMAR的关键创新在于引入了画布机制，这是一种全新的全局先验引入方式，与传统的自回归模型不同，它不是从一个随机噪声开始，而是从一个粗略的全局预测开始，从而更快地捕捉到视频的整体结构。

**关键设计**：在具体实现上，画布的生成可以通过一个简单的卷积神经网络来实现。组合式的无分类器引导通过调整空间和时间条件的权重来平衡生成质量和多样性。基于噪声的画布增强通过在画布上添加噪声来提高模型的泛化能力。损失函数的设计需要同时考虑画布的准确性和生成视频的质量。

## 📊 实验亮点

CanvasMAR在BAIR和Kinetics-600数据集上进行了评估，实验结果表明，该方法能够以更少的自回归步骤生成高质量的视频。在Kinetics-600数据集上，CanvasMAR在自回归模型中取得了卓越的性能，甚至可以与基于扩散的模型相媲美。这些结果表明，CanvasMAR是一种有效的视频生成方法，具有很强的竞争力。

## 🎯 应用场景

CanvasMAR在视频生成领域具有广泛的应用前景，例如视频编辑、游戏开发、虚拟现实等。它可以用于生成高质量、连贯的视频内容，提升用户体验。此外，该技术还可以应用于视频修复、视频插帧等任务，具有重要的实际价值和潜在的商业机会。未来，CanvasMAR可以进一步扩展到更复杂的视频生成场景，例如生成具有特定风格或内容的视频。

## 📄 摘要（原文）

> Masked autoregressive models (MAR) have recently emerged as a powerful paradigm for image and video generation, combining the flexibility of masked modeling with the potential of continuous tokenizer. However, video MAR models suffer from two major limitations: the slow-start problem, caused by the lack of a structured global prior at early sampling stages, and error accumulation across the autoregression in both spatial and temporal dimensions. In this work, we propose CanvasMAR, a novel video MAR model that mitigates these issues by introducing a canvas mechanism--a blurred, global prediction of the next frame, used as the starting point for masked generation. The canvas provides global structure early in sampling, enabling faster and more coherent frame synthesis. Furthermore, we introduce compositional classifier-free guidance that jointly enlarges spatial (canvas) and temporal conditioning, and employ noise-based canvas augmentation to enhance robustness. Experiments on the BAIR and Kinetics-600 benchmarks demonstrate that CanvasMAR produces high-quality videos with fewer autoregressive steps. Our approach achieves remarkable performance among autoregressive models on Kinetics-600 dataset and rivals diffusion-based methods.

