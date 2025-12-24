---
layout: default
title: Generating time-consistent dynamics with discriminator-guided image diffusion models
---

# Generating time-consistent dynamics with discriminator-guided image diffusion models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09089" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09089v2</a>
  <a href="https://arxiv.org/pdf/2505.09089.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09089v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09089v2', 'Generating time-consistent dynamics with discriminator-guided image diffusion models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Philipp Hess, Maximilian Gelbrecht, Christof Schötz, Michael Aich, Yu Huang, Shangshang Yang, Niklas Boers

**分类**: cs.LG

**发布日期**: 2025-05-14 (更新: 2025-05-15)

---

## 💡 一句话要点

**提出时间一致性判别器以解决视频生成中的动态一致性问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频生成` `时间一致性` `扩散模型` `气候模拟` `不确定性校准` `动态模拟` `计算流体动力学`

## 📋 核心要点

1. 现有的视频扩散模型在训练时需要大量计算资源，且从头训练存在挑战，限制了其应用。
2. 本文提出了一种时间一致性判别器，能够引导预训练图像扩散模型生成真实的时空动态，无需额外的微调。
3. 实验结果显示，该方法在时间一致性、降低偏差和不确定性校准方面优于从头训练的VDM，并实现了稳定的气候模拟。

## 📝 摘要（中文）

现实的时间动态对于许多视频生成、处理和建模应用至关重要，例如计算流体动力学、天气预测或长期气候模拟。视频扩散模型（VDMs）是生成高度真实动态的当前最先进方法。然而，从头训练VDMs具有挑战性，并且需要大量计算资源，限制了其更广泛的应用。本文提出了一种时间一致性判别器，使预训练的图像扩散模型能够生成真实的时空动态。该判别器引导采样推理过程，无需对图像扩散模型进行扩展或微调。我们在理想化的湍流模拟和真实的全球降水数据集上将我们的方法与从头训练的VDM进行了比较，结果表明我们的方法在时间一致性方面表现相当，且不确定性校准更好，偏差更低，实现了以日为时间步的稳定百年气候模拟。

## 🔬 方法详解

**问题定义**：本文旨在解决视频生成中的时间一致性问题。现有的视频扩散模型在训练时需要大量计算资源，且从头训练存在挑战，限制了其应用。

**核心思路**：论文提出了一种时间一致性判别器，能够引导预训练的图像扩散模型生成真实的时空动态。该判别器在采样推理过程中提供指导，避免了对模型的扩展或微调。

**技术框架**：整体架构包括预训练的图像扩散模型和时间一致性判别器。判别器在推理阶段与扩散模型协同工作，确保生成的动态在时间上保持一致。

**关键创新**：最重要的技术创新点在于引入时间一致性判别器，使得预训练模型能够在不进行额外训练的情况下生成高质量的时空动态。这与传统的从头训练VDM方法形成鲜明对比。

**关键设计**：关键设计包括判别器的损失函数设置，以及如何在推理过程中有效地引导图像扩散模型生成时间一致的动态。具体的网络结构和参数设置在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，提出的方法在时间一致性方面与从头训练的VDM表现相当，同时在不确定性校准和偏差控制上有显著提升。具体而言，该方法在稳定的百年气候模拟中表现出色，能够以日为时间步进行有效模拟。

## 🎯 应用场景

该研究的潜在应用领域包括气候模拟、天气预测和计算流体动力学等。通过提高视频生成的时间一致性，该方法可以为科学研究和工业应用提供更可靠的动态模拟，推动相关领域的发展。

## 📄 摘要（原文）

> Realistic temporal dynamics are crucial for many video generation, processing and modelling applications, e.g. in computational fluid dynamics, weather prediction, or long-term climate simulations. Video diffusion models (VDMs) are the current state-of-the-art method for generating highly realistic dynamics. However, training VDMs from scratch can be challenging and requires large computational resources, limiting their wider application. Here, we propose a time-consistency discriminator that enables pretrained image diffusion models to generate realistic spatiotemporal dynamics. The discriminator guides the sampling inference process and does not require extensions or finetuning of the image diffusion model. We compare our approach against a VDM trained from scratch on an idealized turbulence simulation and a real-world global precipitation dataset. Our approach performs equally well in terms of temporal consistency, shows improved uncertainty calibration and lower biases compared to the VDM, and achieves stable centennial-scale climate simulations at daily time steps.

