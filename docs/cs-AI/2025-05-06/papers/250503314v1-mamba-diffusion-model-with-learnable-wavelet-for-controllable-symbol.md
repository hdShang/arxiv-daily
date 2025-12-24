---
layout: default
title: Mamba-Diffusion Model with Learnable Wavelet for Controllable Symbolic Music Generation
---

# Mamba-Diffusion Model with Learnable Wavelet for Controllable Symbolic Music Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03314" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03314v1</a>
  <a href="https://arxiv.org/pdf/2505.03314.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03314v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03314v1', 'Mamba-Diffusion Model with Learnable Wavelet for Controllable Symbolic Music Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jincheng Zhang, György Fazekas, Charalampos Saitis

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-05-06

**🔗 代码/项目**: [GITHUB](https://github.com/jinchengzhanggg/proffusion)

---

## 💡 一句话要点

**提出Mamba-Diffusion模型以解决符号音乐生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `符号音乐生成` `扩散模型` `小波变换` `Transformer` `音乐创作` `机器学习`

## 📋 核心要点

1. 现有的扩散模型在符号音乐生成中应用不足，主要因为符号音乐的离散表示形式与标准扩散模型不匹配。
2. 本文提出了一种新型的扩散模型，利用Transformer-Mamba模块和可学习的小波变换来生成符号音乐。
3. 实验结果显示，该方法在音乐质量和可控性方面优于现有强基线，展现了显著的提升。

## 📝 摘要（中文）

近年来，扩散模型在图像合成中的广泛应用引发了对其在其他领域生成任务潜力的新关注。然而，符号音乐生成的应用仍然未被充分探索，因为符号音乐通常以离散事件序列表示，而标准扩散模型不适合处理离散数据。本文将符号音乐表示为类似图像的钢琴卷轴，从而促进扩散模型在符号音乐生成中的应用。此外，研究引入了一种新型扩散模型，结合了提出的Transformer-Mamba模块和可学习的小波变换。通过无分类器引导生成目标和弦的符号音乐。评估结果表明，该方法在音乐质量和可控性方面表现出色，超越了强基线的钢琴卷轴生成效果。代码可在https://github.com/jinchengzhanggg/proffusion获取。

## 🔬 方法详解

**问题定义**：本文旨在解决符号音乐生成中的离散数据处理问题，现有的扩散模型无法有效处理符号音乐的离散事件序列。

**核心思路**：通过将符号音乐表示为图像样式的钢琴卷轴，论文设计了一种新型扩散模型，使其能够适应符号音乐的生成需求。

**技术框架**：整体架构包括Transformer-Mamba模块和可学习的小波变换，结合无分类器引导生成目标和弦的音乐。主要模块包括数据预处理、模型训练和生成阶段。

**关键创新**：最重要的创新在于引入了Transformer-Mamba模块和可学习的小波变换，这使得扩散模型能够有效处理符号音乐的生成，与传统方法相比具有更好的适应性。

**关键设计**：在模型设计中，采用了特定的损失函数以优化生成质量，并在网络结构中引入了可学习的小波变换，以增强模型对音乐特征的捕捉能力。

## 📊 实验亮点

实验结果表明，Mamba-Diffusion模型在音乐生成质量和可控性方面显著优于基线模型，具体提升幅度未知，展示了其在钢琴卷轴生成中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括音乐创作、自动作曲和音乐教育等。通过提高符号音乐生成的质量和可控性，该模型可以为音乐创作者提供更强大的工具，促进音乐创作的多样性和创新性。未来，该技术可能会在音乐生成领域产生深远的影响。

## 📄 摘要（原文）

> The recent surge in the popularity of diffusion models for image synthesis has attracted new attention to their potential for generation tasks in other domains. However, their applications to symbolic music generation remain largely under-explored because symbolic music is typically represented as sequences of discrete events and standard diffusion models are not well-suited for discrete data. We represent symbolic music as image-like pianorolls, facilitating the use of diffusion models for the generation of symbolic music. Moreover, this study introduces a novel diffusion model that incorporates our proposed Transformer-Mamba block and learnable wavelet transform. Classifier-free guidance is utilised to generate symbolic music with target chords. Our evaluation shows that our method achieves compelling results in terms of music quality and controllability, outperforming the strong baseline in pianoroll generation. Our code is available at https://github.com/jinchengzhanggg/proffusion.

