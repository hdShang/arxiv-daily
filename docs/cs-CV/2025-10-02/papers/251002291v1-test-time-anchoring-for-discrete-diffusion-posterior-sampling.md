---
layout: default
title: Test-Time Anchoring for Discrete Diffusion Posterior Sampling
---

# Test-Time Anchoring for Discrete Diffusion Posterior Sampling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02291" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02291v1</a>
  <a href="https://arxiv.org/pdf/2510.02291.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02291v1" onclick="toggleFavorite(this, '2510.02291v1', 'Test-Time Anchoring for Discrete Diffusion Posterior Sampling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Litu Rout, Andreas Lugmayr, Yasamin Jafarian, Srivatsan Varadharajan, Constantine Caramanis, Sanjay Shakkottai, Ira Kemelmacher-Shlizerman

**分类**: cs.LG, cs.CV, stat.ML

**发布日期**: 2025-10-02

**备注**: Preprint

---

## 💡 一句话要点

**提出Anchored Posterior Sampling (APS)，用于离散扩散后验采样，解决逆问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `离散扩散模型` `后验采样` `图像逆问题` `量化期望` `锚定重掩码` `免训练` `图像恢复`

## 📋 核心要点

1. 现有离散扩散后验采样方法面临稀疏信号、适用性受限和维度灾难等挑战。
2. 提出Anchored Posterior Sampling (APS)，利用量化期望进行梯度引导，并采用锚定重掩码进行自适应解码。
3. APS在图像逆问题上取得了SOTA性能，并在免训练风格化和文本引导编辑中展现了优势。

## 📝 摘要（中文）

本文研究了使用预训练离散扩散基础模型进行后验采样的问题，旨在从带噪声的测量数据中恢复图像，而无需重新训练特定任务的模型。虽然扩散模型在生成建模方面取得了显著成功，但大多数进展依赖于连续高斯扩散。相比之下，离散扩散为联合建模分类数据（如文本和图像）提供了一个统一的框架。除了统一性之外，离散扩散还提供更快的推理、更精细的控制和有原则的免训练贝叶斯推理，使其特别适合后验采样。然而，现有的离散扩散后验采样方法面临严峻挑战：无导数引导产生稀疏信号，连续松弛限制了适用性，并且分裂吉布斯采样器遭受维度灾难。为了克服这些限制，我们为掩码扩散基础模型引入了Anchored Posterior Sampling (APS)，它建立在两个关键创新之上——离散嵌入空间中用于类梯度引导的量化期望，以及用于自适应解码的锚定重掩码。我们的方法在标准基准上的线性和非线性逆问题中，实现了离散扩散采样器中的最先进性能。我们进一步展示了我们的方法在免训练风格化和文本引导编辑中的优势。

## 🔬 方法详解

**问题定义**：论文旨在解决离散扩散模型在后验采样中面临的挑战，特别是在图像逆问题中，如何从噪声测量中恢复图像。现有方法，如无导数引导、连续松弛和分裂吉布斯采样器，存在信号稀疏、适用性受限和维度灾难等问题，导致性能不佳。

**核心思路**：论文的核心思路是利用量化期望来近似梯度，从而在离散嵌入空间中提供更有效的引导信号。同时，通过锚定重掩码策略，实现自适应的解码过程，克服传统方法的局限性。这种设计旨在充分利用离散扩散模型的优势，实现更精确、更高效的后验采样。

**技术框架**：APS方法主要包含两个关键模块：量化期望模块和锚定重掩码模块。量化期望模块用于在离散嵌入空间中计算类梯度引导，为扩散过程提供方向。锚定重掩码模块则根据当前状态自适应地调整掩码区域，从而实现更精细的解码过程。整体流程包括：首先，对输入图像进行掩码处理；然后，通过扩散过程逐步添加噪声；接着，利用量化期望和锚定重掩码进行后验采样，逐步恢复图像。

**关键创新**：APS的关键创新在于：1) 使用量化期望来近似梯度，克服了离散空间中梯度计算的难题，提供了更有效的引导信号。2) 引入锚定重掩码策略，实现了自适应的解码过程，避免了传统方法中固定掩码带来的局限性。这些创新使得APS能够在离散扩散模型中实现更精确、更高效的后验采样。

**关键设计**：量化期望模块通过计算离散嵌入空间中相邻状态的期望值，来近似梯度方向。锚定重掩码模块则根据当前状态的置信度，自适应地调整掩码区域的大小和位置。具体的参数设置和网络结构取决于所使用的离散扩散基础模型。损失函数通常包括重构损失和正则化项，以保证恢复图像的质量和一致性。

## 📊 实验亮点

APS在图像逆问题上取得了显著的性能提升，在标准基准测试中达到了SOTA水平。与现有离散扩散采样器相比，APS在恢复图像的质量和效率方面均有明显优势。此外，APS在免训练风格化和文本引导编辑等任务中也展现了良好的效果。

## 🎯 应用场景

该研究成果可广泛应用于图像修复、图像去噪、图像超分辨率等图像逆问题，以及风格迁移、图像编辑等生成任务。其免训练的特性使其在资源受限的场景下具有重要价值。未来，该方法有望扩展到其他离散数据领域，如文本生成、语音合成等。

## 📄 摘要（原文）

> We study the problem of posterior sampling using pretrained discrete diffusion foundation models, aiming to recover images from noisy measurements without retraining task-specific models. While diffusion models have achieved remarkable success in generative modeling, most advances rely on continuous Gaussian diffusion. In contrast, discrete diffusion offers a unified framework for jointly modeling categorical data such as text and images. Beyond unification, discrete diffusion provides faster inference, finer control, and principled training-free Bayesian inference, making it particularly well-suited for posterior sampling. However, existing approaches to discrete diffusion posterior sampling face severe challenges: derivative-free guidance yields sparse signals, continuous relaxations limit applicability, and split Gibbs samplers suffer from the curse of dimensionality. To overcome these limitations, we introduce Anchored Posterior Sampling (APS) for masked diffusion foundation models, built on two key innovations -- quantized expectation for gradient-like guidance in discrete embedding space, and anchored remasking for adaptive decoding. Our approach achieves state-of-the-art performance among discrete diffusion samplers across linear and nonlinear inverse problems on the standard benchmarks. We further demonstrate the benefits of our approach in training-free stylization and text-guided editing.

