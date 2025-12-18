---
layout: default
title: IMTalker: Efficient Audio-driven Talking Face Generation with Implicit Motion Transfer
---

# IMTalker: Efficient Audio-driven Talking Face Generation with Implicit Motion Transfer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22167" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22167v1</a>
  <a href="https://arxiv.org/pdf/2511.22167.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22167v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.22167v1', 'IMTalker: Efficient Audio-driven Talking Face Generation with Implicit Motion Transfer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bo Chen, Tao Liu, Qi Chen, Xie Chen, Zilong Zheng

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-27

**备注**: 11 pages, 5 figures

---

## 💡 一句话要点

**IMTalker：利用隐式运动传递实现高效的音频驱动说话人脸生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)** **支柱四：生成式动作 (Generative Motion)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `说话人脸生成` `隐式运动传递` `交叉注意力机制` `身份保持` `音频驱动`

## 📋 核心要点

1. 现有说话人脸生成方法依赖光流和局部扭曲，难以捕捉全局运动，导致身份信息丢失。
2. IMTalker采用交叉注意力机制隐式建模运动差异和身份对齐，实现鲁棒的全局运动渲染。
3. 实验表明，IMTalker在运动精度、身份保持和音唇同步方面优于现有方法，效率更高。

## 📝 摘要（中文）

本文提出了一种名为IMTalker的新框架，用于高效且高保真地生成说话人脸。现有方法通常依赖于显式的光流和局部扭曲，难以建模复杂的全局运动，并导致身份漂移。IMTalker的核心思想是用交叉注意力机制取代传统的基于光流的扭曲，从而在统一的潜在空间中隐式地建模运动差异和身份对齐，实现鲁棒的全局运动渲染。为了进一步在跨身份重演中保持说话人的身份，引入了一个身份自适应模块，将运动潜在向量投影到个性化的空间中，确保运动和身份之间的清晰解耦。此外，一个轻量级的流匹配运动生成器从音频、姿势和视线线索中产生生动且可控的隐式运动向量。大量实验表明，IMTalker在运动精度、身份保持和音频-嘴唇同步方面超越了现有方法，以卓越的效率实现了最先进的质量，在RTX 4090 GPU上，视频驱动生成速度为40 FPS，音频驱动生成速度为42 FPS。我们将发布我们的代码和预训练模型，以促进应用和未来的研究。

## 🔬 方法详解

**问题定义**：说话人脸生成旨在从单张图像合成逼真的说话人像。现有方法依赖显式光流和局部扭曲，难以建模复杂的全局运动，导致身份漂移，生成效果不佳。

**核心思路**：IMTalker的核心思路是使用交叉注意力机制来隐式地建模运动差异和身份对齐，从而避免了传统方法中显式光流计算和局部扭曲带来的问题。通过在潜在空间中进行操作，能够更好地捕捉全局运动，并保持身份信息。

**技术框架**：IMTalker框架主要包含以下几个模块：1) 一个轻量级的流匹配运动生成器，用于从音频、姿势和视线线索中生成隐式运动向量；2) 一个交叉注意力模块，用于在源图像和驱动信号之间进行运动传递和身份对齐；3) 一个身份自适应模块，用于将运动潜在向量投影到个性化的空间中，以保持说话人的身份。整体流程是，首先通过运动生成器得到运动信息，然后通过交叉注意力和身份自适应模块将运动信息传递到源图像，最终生成说话人脸。

**关键创新**：IMTalker的关键创新在于使用交叉注意力机制进行隐式运动传递，取代了传统方法中基于光流的显式运动传递。这种方法能够更好地捕捉全局运动，并保持身份信息。此外，身份自适应模块的设计也有效地解决了跨身份重演中的身份漂移问题。

**关键设计**：运动生成器采用流匹配模型，能够生成生动且可控的隐式运动向量。交叉注意力模块使用多头注意力机制，能够捕捉不同尺度的运动信息。身份自适应模块通过学习一个映射函数，将运动潜在向量投影到个性化的空间中。损失函数包括重建损失、对抗损失和身份保持损失，用于保证生成图像的质量和身份一致性。

## 📊 实验亮点

IMTalker在运动精度、身份保持和音频-嘴唇同步方面均优于现有方法。在RTX 4090 GPU上，视频驱动生成速度达到40 FPS，音频驱动生成速度达到42 FPS，实现了高效的说话人脸生成。实验结果表明，IMTalker能够生成高质量的说话人脸，同时保持说话人的身份信息。

## 🎯 应用场景

IMTalker可应用于虚拟形象生成、视频会议、电影制作、游戏开发等领域。该技术能够生成逼真且自然的说话人脸，提升用户体验，降低制作成本。未来，该技术有望应用于个性化教育、智能客服等领域，实现更智能的人机交互。

## 📄 摘要（原文）

> Talking face generation aims to synthesize realistic speaking portraits from a single image, yet existing methods often rely on explicit optical flow and local warping, which fail to model complex global motions and cause identity drift. We present IMTalker, a novel framework that achieves efficient and high-fidelity talking face generation through implicit motion transfer. The core idea is to replace traditional flow-based warping with a cross-attention mechanism that implicitly models motion discrepancy and identity alignment within a unified latent space, enabling robust global motion rendering. To further preserve speaker identity during cross-identity reenactment, we introduce an identity-adaptive module that projects motion latents into personalized spaces, ensuring clear disentanglement between motion and identity. In addition, a lightweight flow-matching motion generator produces vivid and controllable implicit motion vectors from audio, pose, and gaze cues. Extensive experiments demonstrate that IMTalker surpasses prior methods in motion accuracy, identity preservation, and audio-lip synchronization, achieving state-of-the-art quality with superior efficiency, operating at 40 FPS for video-driven and 42 FPS for audio-driven generation on an RTX 4090 GPU. We will release our code and pre-trained models to facilitate applications and future research.

