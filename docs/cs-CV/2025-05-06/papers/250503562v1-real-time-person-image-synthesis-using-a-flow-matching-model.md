---
layout: default
title: Real-Time Person Image Synthesis Using a Flow Matching Model
---

# Real-Time Person Image Synthesis Using a Flow Matching Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03562" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03562v1</a>
  <a href="https://arxiv.org/pdf/2505.03562.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03562v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03562v1', 'Real-Time Person Image Synthesis Using a Flow Matching Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiwoo Jeong, Kirok Kim, Wooju Kim, Nam-Joon Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出基于流匹配模型的实时人物图像合成方法以解决生成速度问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `实时图像合成` `流匹配模型` `姿态引导` `生成对抗网络` `深度学习` `计算机视觉` `手语视频生成`

## 📋 核心要点

1. 现有的扩散模型在图像合成质量上表现优异，但其慢速采样限制了实时应用的可行性。
2. 本文提出了一种基于流匹配的生成模型，旨在提高图像合成的速度和稳定性，适用于实时交互系统。
3. 实验结果显示，RPFM在生成速度上提升超过两倍，同时保持与最先进模型相当的性能，确保实时性。

## 📝 摘要（中文）

姿态引导的人物图像合成（PGPIS）旨在根据目标姿态和源图像生成逼真的人物图像。这一任务在手语视频生成、增强现实/虚拟现实、游戏和直播等多种现实应用中至关重要。然而，实现实时性能仍然是一个重大挑战，因为从多样化和动态的人体姿态合成高保真图像的复杂性使得速度受到限制。尽管最近的扩散模型在图像质量上表现出色，但其较慢的采样速度限制了在时间敏感应用中的部署。为此，本文提出了一种基于流匹配的生成模型（RPFM），该模型在保持图像质量的同时，实现了更快、更稳定的训练和采样。实验结果表明，RPFM在DeepFashion数据集上实现了接近实时的采样速度，且性能与现有最先进模型相当。

## 🔬 方法详解

**问题定义**：本文旨在解决实时人物图像合成中的速度瓶颈问题，现有的扩散模型虽然在图像质量上表现良好，但其慢速采样使得在时间敏感的应用中难以部署。

**核心思路**：提出基于流匹配的生成模型（RPFM），通过优化训练和采样过程，实现更快的生成速度和更高的稳定性，特别适合实时应用。

**技术框架**：该模型的整体架构包括数据预处理、流匹配生成模块和后处理阶段。流匹配模块负责在潜在空间中进行条件生成，以提高生成效率。

**关键创新**：RPFM的核心创新在于流匹配机制的引入，使得模型在生成速度上显著提升，同时保持图像质量，区别于传统的扩散模型。

**关键设计**：在模型设计中，采用了特定的损失函数以平衡生成速度与图像质量，并优化了网络结构以适应潜在空间的操作。

## 📊 实验亮点

实验结果表明，RPFM在DeepFashion数据集上实现了接近实时的采样速度，生成速度提升超过两倍，同时保持与最先进模型相当的性能，确保在实时应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括手语视频生成、增强现实和虚拟现实等实时交互系统。通过提高图像合成的速度和质量，RPFM能够为用户提供更流畅的视觉体验，增强沉浸感，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Pose-Guided Person Image Synthesis (PGPIS) generates realistic person images conditioned on a target pose and a source image. This task plays a key role in various real-world applications, such as sign language video generation, AR/VR, gaming, and live streaming. In these scenarios, real-time PGPIS is critical for providing immediate visual feedback and maintaining user immersion.However, achieving real-time performance remains a significant challenge due to the complexity of synthesizing high-fidelity images from diverse and dynamic human poses. Recent diffusion-based methods have shown impressive image quality in PGPIS, but their slow sampling speeds hinder deployment in time-sensitive applications. This latency is particularly problematic in tasks like generating sign language videos during live broadcasts, where rapid image updates are required. Therefore, developing a fast and reliable PGPIS model is a crucial step toward enabling real-time interactive systems. To address this challenge, we propose a generative model based on flow matching (FM). Our approach enables faster, more stable, and more efficient training and sampling. Furthermore, the proposed model supports conditional generation and can operate in latent space, making it especially suitable for real-time PGPIS applications where both speed and quality are critical. We evaluate our proposed method, Real-Time Person Image Synthesis Using a Flow Matching Model (RPFM), on the widely used DeepFashion dataset for PGPIS tasks. Our results show that RPFM achieves near-real-time sampling speeds while maintaining performance comparable to the state-of-the-art models. Our methodology trades off a slight, acceptable decrease in generated-image accuracy for over a twofold increase in generation speed, thereby ensuring real-time performance.

