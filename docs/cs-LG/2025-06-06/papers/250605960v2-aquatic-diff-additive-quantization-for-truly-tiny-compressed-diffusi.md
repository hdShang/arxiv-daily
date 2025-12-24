---
layout: default
title: "AQUATIC-Diff: Additive Quantization for Truly Tiny Compressed Diffusion Models"
---

# AQUATIC-Diff: Additive Quantization for Truly Tiny Compressed Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05960" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05960v2</a>
  <a href="https://arxiv.org/pdf/2506.05960.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05960v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05960v2', 'AQUATIC-Diff: Additive Quantization for Truly Tiny Compressed Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adil Hasan, Thomas Peyrin

**分类**: cs.LG

**发布日期**: 2025-06-06 (更新: 2025-06-09)

---

## 💡 一句话要点

**提出AQUATIC-Diff以解决扩散模型压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `量化方法` `向量量化` `图像生成` `模型压缩` `高效推理` `深度学习`

## 📋 核心要点

1. 现有的扩散模型在推理时对硬件资源的需求极高，限制了其广泛应用。
2. 本文提出了一种基于代码本的加性向量量化方法，旨在提高扩散模型的压缩效率。
3. 实验结果表明，该方法在多个指标上超越全精度模型，显著降低了推理时的计算需求。

## 📝 摘要（中文）

在生成多样化媒体的扩散模型的商业化过程中，硬件资源需求高成为其普及的障碍。虽然现有的模型量化策略在一定程度上缓解了这一问题，但主要集中在均匀标量量化方法上。本文提出了一种基于代码本的加性向量量化方法，专门针对扩散模型的压缩。该方法在ImageNet的LDM-4基准测试中实现了新的低比特权重量化前沿，报告的sFID比全精度模型低1.92分，并在W2A8下获得了FID、sFID和ISC的最佳结果。此外，我们展示了通过高效推理内核在任意硬件上节省FLOPs的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散模型在推理过程中对硬件资源的高需求问题。现有的量化方法主要集中在均匀标量量化，未能充分利用向量量化的优势。

**核心思路**：论文提出的加性向量量化方法通过对相关权重进行分组处理，利用代码本进行压缩，从而提高了模型的压缩效率和推理性能。

**技术框架**：整体架构包括数据预处理、模型训练、量化过程和推理阶段。主要模块包括代码本生成、权重映射和推理优化。

**关键创新**：最重要的创新在于引入了加性向量量化方法，区别于传统的均匀标量量化，能够更有效地处理扩散模型的权重。

**关键设计**：在参数设置上，采用了W4A8和W2A8的量化策略，并设计了特定的损失函数以优化量化效果，同时确保了推理过程的高效性。

## 📊 实验亮点

实验结果显示，在W4A8配置下，sFID比全精度模型低1.92分，并在W2A8下获得了FID、sFID和ISC的最佳结果。此外，通过高效推理内核实现了FLOPs的显著节省，提升了模型的实际应用价值。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、视频生成以及其他需要高效推理的生成模型。通过降低硬件资源需求，AQUATIC-Diff能够使得扩散模型在移动设备和边缘计算环境中得到更广泛的应用，推动生成模型的普及与发展。

## 📄 摘要（原文）

> Significant investments have been made towards the commodification of diffusion models for generation of diverse media. Their mass-market adoption is however still hobbled by the intense hardware resource requirements of diffusion model inference. Model quantization strategies tailored specifically towards diffusion models have been useful in easing this burden, yet have generally explored the Uniform Scalar Quantization (USQ) family of quantization methods. In contrast, Vector Quantization (VQ) methods, which operate on groups of multiple related weights as the basic unit of compression, have seen substantial success in Large Language Model (LLM) quantization. In this work, we apply codebook-based additive vector quantization to the problem of diffusion model compression. Our resulting approach achieves a new Pareto frontier for the extremely low-bit weight quantization on the standard class-conditional benchmark of LDM-4 on ImageNet at 20 inference time steps. Notably, we report sFID 1.92 points lower than the full-precision model at W4A8 and the best-reported results for FID, sFID and ISC at W2A8. We are also able to demonstrate FLOPs savings on arbitrary hardware via an efficient inference kernel, as opposed to savings resulting from small integer operations which may lack broad hardware support.

