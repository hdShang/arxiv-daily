---
layout: default
title: "MotionGPT3: Human Motion as a Second Modality"
---

# MotionGPT3: Human Motion as a Second Modality

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24086" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24086v3</a>
  <a href="https://arxiv.org/pdf/2506.24086.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24086v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24086v3', 'MotionGPT3: Human Motion as a Second Modality')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingfan Zhu, Biao Jiang, Sunyi Wang, Shixiang Tang, Tao Chen, Linjie Luo, Youyi Zheng, Xin Chen

**分类**: cs.CV, cs.CL

**发布日期**: 2025-06-30 (更新: 2025-11-03)

**备注**: 26 pages, 11 figures

---

## 💡 一句话要点

**提出MotionGPT3以解决多模态运动理解与生成问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `运动生成` `语言模型` `变分自编码器` `Transformer架构` `模型收敛` `运动理解` `信息流动`

## 📋 核心要点

1. 现有多模态框架在处理运动与语言的结合时，面临着量化误差和跨模态干扰的问题，影响了模型的性能。
2. MotionGPT3通过变分自编码器将运动编码为连续潜在空间，采用双流Transformer架构以减少模态间干扰，提升信息流动性。
3. 实验结果显示，MotionGPT3在训练和验证阶段的收敛速度分别提升了2倍和4倍，同时在运动理解与生成任务上达到了最先进的性能。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，统一理解与生成的多模态框架变得越来越有前景，但随着模态和任务数量的增加，复杂性也在增加。本文观察到运动量化引入的近似误差限制了运动质量，而将离散文本和连续运动统一在单一流骨干中则加剧了跨模态干扰。为此，本文提出了MotionGPT3，一个用于理解和生成的双模态运动-语言模型。该模型利用变分自编码器（VAE）将原始运动编码为连续潜在空间，避免了量化引起的伪影，同时利用了预训练语言模型的语义先验。双流Transformer与共享注意力机制相结合，保留了模态特定的路径，同时实现了受控的双向信息流，减少了干扰，稳定了优化，并在不降低保真度的情况下加速了收敛。实验表明，MotionGPT3在训练损失上实现了2倍的收敛速度提升，在验证上实现了高达4倍的收敛速度，同时在标准运动理解和生成基准上保持了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态运动理解与生成中的量化误差和跨模态干扰问题。现有方法在将离散文本与连续运动结合时，常常导致性能下降。

**核心思路**：提出MotionGPT3模型，通过变分自编码器（VAE）将运动数据编码为连续潜在空间，避免量化伪影，同时结合预训练语言模型的语义信息，提升模型的理解与生成能力。

**技术框架**：MotionGPT3采用双流Transformer架构，分别处理运动和语言模态。共享注意力机制允许模态间的信息流动，同时保持模态特定的特征，减少干扰。模型训练采用生成-对齐的三阶段调度，进一步提高稳定性。

**关键创新**：最重要的创新在于采用双流结构与VAE相结合，显著降低了模态间的干扰，并加速了模型的收敛速度。这一设计与传统的单流模型形成了鲜明对比。

**关键设计**：模型的关键参数设置包括VAE的潜在空间维度、双流Transformer的层数和注意力头数。损失函数设计上，结合了重构损失与对抗损失，以确保生成运动的质量和多样性。整体架构经过多轮实验优化，确保了高效的训练与推理。

## 📊 实验亮点

实验结果表明，MotionGPT3在训练损失上实现了2倍的收敛速度提升，在验证阶段的收敛速度高达4倍，相较于现有基线模型，保持了最先进的性能，展示了其在多模态任务中的有效性与优势。

## 🎯 应用场景

MotionGPT3的研究成果在虚拟现实、动画制作、游戏开发等领域具有广泛的应用潜力。通过提升运动理解与生成的质量，该模型能够为人机交互、自动动画生成等应用提供更自然的体验，推动相关技术的发展与创新。

## 📄 摘要（原文）

> With the rapid progress of large language models (LLMs), multimodal frameworks that unify understanding and generation have become promising, yet they face increasing complexity as the number of modalities and tasks grows. We observe that motion quantization introduces approximation errors that cap motion quality, and that unifying discrete text and continuous motion within a single-stream backbone amplifies cross-modal interference. Motivated by recent multi-branch Transformer designs that separate signals from different modalities, we propose MotionGPT3, a bimodal motion-language model for both understanding and generation. MotionGPT3 encodes raw motion into a continuous latent space using a variational autoencoder (VAE), thereby avoiding quantization-induced artifacts, while leveraging the semantic prior of pretrained language models. A dual-stream Transformer with shared attention preserves modality-specific routes while enabling controlled, bidirectional information flow, which reduces interference, stabilizing optimization, and empirically accelerates convergence without degrading fidelity. For multimodal joint training, a generate-then-align three-stage schedule further improves stability and limits cross-task interference. Experiments show that MotionGPT3 achieves 2x faster convergence in training loss and up to 4x faster convergence in validation, while maintaining state-of-the-art performance on standard motion understanding and motion generation benchmarks.

