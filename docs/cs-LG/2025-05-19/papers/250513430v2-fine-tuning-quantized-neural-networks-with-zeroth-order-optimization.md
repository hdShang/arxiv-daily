---
layout: default
title: Fine-tuning Quantized Neural Networks with Zeroth-order Optimization
---

# Fine-tuning Quantized Neural Networks with Zeroth-order Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13430" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13430v2</a>
  <a href="https://arxiv.org/pdf/2505.13430.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13430v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13430v2', 'Fine-tuning Quantized Neural Networks with Zeroth-order Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sifeng Shang, Jiayi Zhou, Chenyu Lin, Minxian Li, Kaiyang Zhou

**分类**: cs.LG, cs.CL, cs.CV

**发布日期**: 2025-05-19 (更新: 2025-09-01)

---

## 💡 一句话要点

**提出量化神经网络的零阶优化方法以解决内存瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化神经网络` `零阶优化` `内存高效训练` `大型语言模型` `GPU优化` `模型微调` `深度学习`

## 📋 核心要点

1. 现有方法在处理大型语言模型时面临GPU内存瓶颈，限制了模型的适应性和灵活性。
2. 本文提出量化零阶优化（QZO）方法，通过扰动量化尺度来近似梯度，消除梯度和优化器状态的内存需求。
3. 实验结果表明，QZO在4位LLM中将内存成本降低超过18倍，能够在单个24GB GPU上成功微调大型模型。

## 📝 摘要（中文）

随着大型语言模型规模的指数增长，GPU内存成为适应下游任务的瓶颈。本文旨在通过在统一框架内最小化模型权重、梯度和优化器状态的内存使用，推动内存高效训练的极限。我们提出零阶优化方法，通过在前向传播中扰动权重来近似梯度，从而消除梯度和优化器状态。为减少权重的内存使用，我们采用模型量化技术。然而，直接将零阶优化应用于量化权重是不可行的，因此我们提出了量化零阶优化（QZO），该方法通过扰动连续量化尺度来估计梯度，并使用方向导数裁剪方法来稳定训练。与16位全参数微调相比，QZO在4位LLM中可将总内存成本降低超过18倍，并能够在单个24GB GPU上微调Llama-2-13B。代码将公开发布。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在微调过程中GPU内存不足的问题，现有方法在权重、梯度和优化器状态的内存使用上存在显著瓶颈。

**核心思路**：提出量化零阶优化（QZO）方法，通过扰动量化尺度来近似梯度，避免了传统方法中对梯度和优化器状态的内存需求，从而实现更高效的内存使用。

**技术框架**：整体架构包括权重量化、零阶优化和方向导数裁剪三个主要模块。首先对模型权重进行量化，然后在前向传播中扰动权重以估计梯度，最后通过裁剪方法稳定训练过程。

**关键创新**：QZO的核心创新在于通过扰动量化尺度来实现梯度估计，这一方法与现有的基于标量和代码本的后训练量化方法是正交的，提供了一种新的思路来解决量化模型的训练问题。

**关键设计**：在QZO中，采用了特定的扰动策略和方向导数裁剪技术，以确保在量化权重的情况下仍能有效估计梯度并稳定训练过程。

## 📊 实验亮点

实验结果显示，与16位全参数微调相比，QZO在4位LLM中将内存成本降低超过18倍，能够在单个24GB GPU上成功微调Llama-2-13B，展现出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉等需要大规模模型的任务。通过降低内存需求，QZO方法使得在资源受限的环境中训练大型模型成为可能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> As the size of large language models grows exponentially, GPU memory has become a bottleneck for adapting these models to downstream tasks. In this paper, we aim to push the limits of memory-efficient training by minimizing memory usage on model weights, gradients, and optimizer states, within a unified framework. Our idea is to eliminate both gradients and optimizer states using zeroth-order optimization, which approximates gradients by perturbing weights during forward passes to identify gradient directions. To minimize memory usage on weights, we employ model quantization, e.g., converting from bfloat16 to int4. However, directly applying zeroth-order optimization to quantized weights is infeasible due to the precision gap between discrete weights and continuous gradients, which would otherwise require de-quantization and re-quantization. To overcome this challenge, we propose Quantized Zeroth-order Optimization (QZO), a simple yet effective approach that perturbs the continuous quantization scale for gradient estimation and uses a directional derivative clipping method to stabilize training. QZO is orthogonal to both scalar-based and codebook-based post-training quantization methods. Compared to full-parameter fine-tuning in 16 bits, QZO can reduce the total memory cost by more than 18$\times$ for 4-bit LLMs, and enables fine-tuning Llama-2-13B within a single 24GB GPU. Code will be released publicly.

