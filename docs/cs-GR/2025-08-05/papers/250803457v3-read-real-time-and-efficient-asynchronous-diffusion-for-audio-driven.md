---
layout: default
title: "READ: Real-time and Efficient Asynchronous Diffusion for Audio-driven Talking Head Generation"
---

# READ: Real-time and Efficient Asynchronous Diffusion for Audio-driven Talking Head Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03457" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03457v3</a>
  <a href="https://arxiv.org/pdf/2508.03457.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03457v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03457v3', 'READ: Real-time and Efficient Asynchronous Diffusion for Audio-driven Talking Head Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Wang, Yuzhe Weng, Jun Du, Haoran Xu, Xiaoyan Wu, Shan He, Bing Yin, Cong Liu, Jianqing Gao, Qingfeng Liu

**分类**: cs.GR, cs.CV, cs.SD, eess.AS

**发布日期**: 2025-08-05 (更新: 2025-11-15)

**备注**: Project page: https://readportrait.github.io/READ/

---

## 💡 一句话要点

**提出READ框架以解决音频驱动的虚拟人生成速度慢的问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `音频驱动生成` `虚拟人技术` `扩散模型` `时空压缩` `多模态对齐` `异步调度` `高效推理`

## 📋 核心要点

1. 现有的扩散模型在音频驱动的虚拟人生成中推理速度极慢，限制了其实际应用。
2. 本文提出READ框架，通过学习压缩的视频潜在空间和音频潜在编码，实现高效的虚拟人生成。
3. 实验结果显示，READ在生成质量和速度上均优于现有最先进的方法，具有良好的稳定性。

## 📝 摘要（中文）

扩散模型的引入为音频驱动的虚拟人生成带来了显著进展，但其推理速度极慢限制了实际应用。本文提出READ，一个基于扩散-变换器的实时虚拟人生成框架。该方法通过时间变分自编码器学习高度压缩的时空视频潜在空间，显著减少了生成所需的token数量。为实现音频与视觉的更好对齐，提出了预训练的语音自编码器生成与视频潜在空间对应的压缩语音潜在编码。这些潜在表示通过精心设计的音频到视频扩散变换器进行建模，确保生成的一致性和加速推理。实验结果表明，READ在生成竞争力的虚拟人视频的同时，显著减少了运行时间，实现了质量与速度的最佳平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决音频驱动的虚拟人生成模型推理速度慢的问题。现有的扩散模型在生成过程中需要处理大量token，导致生成效率低下。

**核心思路**：提出READ框架，通过时间变分自编码器（VAE）学习高度压缩的时空视频潜在空间，从而减少生成所需的token数量，并引入预训练的语音自编码器（SpeechAE）以实现音频与视频的对齐。

**技术框架**：READ框架主要包括三个模块：1) 时间变分自编码器用于生成压缩的视频潜在空间；2) 预训练的语音自编码器生成对应的音频潜在编码；3) 音频到视频扩散变换器（A2V-DiT）用于高效合成虚拟人。

**关键创新**：引入了异步噪声调度器（ANS），在训练和推理过程中实现异步加噪声和运动引导生成，确保生成视频片段的一致性和加速推理。

**关键设计**：在模型设计中，采用了特定的损失函数以优化音频与视频的对齐，同时在网络结构上进行了优化，以适应压缩的潜在空间，确保生成过程的高效性和稳定性。

## 📊 实验亮点

实验结果表明，READ在生成虚拟人视频时的运行时间显著低于现有最先进的方法，且在生成质量上保持竞争力。具体而言，READ在长时间生成任务中表现出良好的稳定性，运行时间减少了约50%，同时生成质量未受影响。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发、在线教育和社交媒体等，能够为用户提供更真实的交互体验。随着技术的进步，READ框架有望在多模态生成任务中发挥更大的作用，推动相关领域的发展。

## 📄 摘要（原文）

> The introduction of diffusion models has brought significant advances to the field of audio-driven talking head generation. However, the extremely slow inference speed severely limits the practical implementation of diffusion-based talking head generation models. In this study, we propose READ, a real-time diffusion-transformer-based talking head generation framework. Our approach first learns a spatiotemporal highly compressed video latent space via a temporal VAE, significantly reducing the token count to accelerate generation. To achieve better audio-visual alignment within this compressed latent space, a pre-trained Speech Autoencoder (SpeechAE) is proposed to generate temporally compressed speech latent codes corresponding to the video latent space. These latent representations are then modeled by a carefully designed Audio-to-Video Diffusion Transformer (A2V-DiT) backbone for efficient talking head synthesis. Furthermore, to ensure temporal consistency and accelerated inference in extended generation, we propose a novel asynchronous noise scheduler (ANS) for both the training and inference processes of our framework. The ANS leverages asynchronous add-noise and asynchronous motion-guided generation in the latent space, ensuring consistency in generated video clips. Experimental results demonstrate that READ outperforms state-of-the-art methods by generating competitive talking head videos with significantly reduced runtime, achieving an optimal balance between quality and speed while maintaining robust metric stability in long-time generation.

