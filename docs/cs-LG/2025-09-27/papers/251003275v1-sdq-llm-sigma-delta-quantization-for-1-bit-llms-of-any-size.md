---
layout: default
title: "SDQ-LLM: Sigma-Delta Quantization for 1-bit LLMs of any size"
---

# SDQ-LLM: Sigma-Delta Quantization for 1-bit LLMs of any size

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03275" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03275v1</a>
  <a href="https://arxiv.org/pdf/2510.03275.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03275v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03275v1', 'SDQ-LLM: Sigma-Delta Quantization for 1-bit LLMs of any size')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhao Xia, Ming Zhao, Limin Xiao, Xiujun Zhang

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/Dreamlittlecat/LLM-Quant-Factory)

---

## 💡 一句话要点

**SDQ-LLM：面向任意规模LLM的Sigma-Delta量化，实现高效1比特量化。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `量化` `低比特量化` `Sigma-Delta量化` `模型压缩` `过采样` `模型优化`

## 📋 核心要点

1. 现有LLM面临计算和内存挑战，极低比特量化是高效部署的关键，但会严重影响模型精度。
2. SDQ-LLM通过Sigma-Delta量化和可调过采样率，将高精度权重编码为1比特或1.58比特，并用加法代替乘法。
3. 实验表明，SDQ-LLM即使在低过采样率下，也能在OPT和LLaMA模型上实现高效且高精度的性能。

## 📝 摘要（中文）

本文提出SDQ-LLM，一种针对任意规模大语言模型（LLM）的Sigma-Delta量化框架，旨在实现极低比特量化，同时保留语言推理能力。SDQ-LLM的显著特点是可连续调节的过采样率（OSR），通过选择分数OSR（例如2.5倍）动态适应内存或VRAM约束，从而在模型大小和精度之间实现最佳权衡。SDQ-LLM采用过采样结合Sigma-Delta量化器，将LLM权重二值化或三值化，将高精度参数编码为1比特或1.58比特表示，并将线性层中的乘法运算替换为加法，从而显著提高极低比特量化下的推理效率。为了进一步减少量化精度损失，我们在量化前引入基于Hadamard的权重平滑，提高权重表示的稳定性和鲁棒性。此外，为了充分利用OSR的连续性并减少精度损失，我们认识到量化敏感性与权重方差之间的相关性，提出了一种细粒度的、层和线性层级别的OSR分配策略MultiOSR。该策略基于权重方差和参数规模，在层之间和每层内部分配OSR。在OPT和LLaMA模型系列上的大量实验表明，即使在高度激进的低OSR设置下，SDQ-LLM也能实现更高效和高精度的性能。

## 🔬 方法详解

**问题定义**：大语言模型（LLM）的部署面临着巨大的计算和内存压力。极低比特量化是降低资源消耗的有效方法，但现有方法在大幅压缩模型的同时，往往会造成严重的精度损失，尤其是在1比特量化的情况下。因此，如何在保证模型性能的前提下，实现LLM的极低比特量化是一个关键问题。

**核心思路**：SDQ-LLM的核心思路是利用Sigma-Delta量化器和可调节的过采样率（OSR）来实现权重的有效压缩和精度保持。Sigma-Delta量化器能够将高精度参数编码为低比特表示，而OSR则允许在模型大小和精度之间进行权衡。通过动态调整OSR，SDQ-LLM可以适应不同的内存或VRAM约束。此外，论文还通过Hadamard权重平滑和细粒度的OSR分配策略来进一步减少量化误差。

**技术框架**：SDQ-LLM的整体框架包括以下几个主要步骤：1) Hadamard权重平滑：对原始权重进行预处理，提高权重表示的稳定性和鲁棒性。2) Sigma-Delta量化：使用Sigma-Delta量化器将权重转换为1比特或1.58比特表示。3) 过采样：通过调整OSR来控制量化后的模型大小和精度。4) MultiOSR分配：根据权重方差和参数规模，在不同层和线性层之间分配OSR。5) 推理：使用量化后的权重进行推理，将线性层中的乘法运算替换为加法运算。

**关键创新**：SDQ-LLM的关键创新在于以下几个方面：1) 可连续调节的OSR：允许在模型大小和精度之间进行动态权衡，适应不同的资源约束。2) Hadamard权重平滑：减少量化误差，提高模型性能。3) MultiOSR分配策略：根据权重方差和参数规模，在不同层和线性层之间分配OSR，进一步提高量化精度。4) 将乘法运算替换为加法运算：显著提高推理效率。

**关键设计**：1) 过采样率OSR的连续可调性，允许用户根据实际资源情况选择合适的OSR值，例如2.5倍。2) Hadamard权重平滑的具体实现方式，包括Hadamard矩阵的选择和应用。3) MultiOSR分配策略的细节，包括权重方差和参数规模的计算方法，以及OSR的分配比例。4) Sigma-Delta量化器的具体参数设置，例如量化步长和阈值。

## 📊 实验亮点

实验结果表明，SDQ-LLM在OPT和LLaMA模型系列上取得了显著的性能提升。例如，在低过采样率设置下，SDQ-LLM仍然能够保持较高的精度，并且在某些情况下甚至超过了其他量化方法。此外，SDQ-LLM还能够显著降低模型的内存占用和计算复杂度，提高推理速度。

## 🎯 应用场景

SDQ-LLM在资源受限的设备上部署大型语言模型方面具有广泛的应用前景，例如移动设备、嵌入式系统和边缘计算设备。该技术可以降低LLM的内存占用和计算复杂度，使其能够在这些设备上高效运行，从而实现智能助手、自然语言处理等应用。

## 📄 摘要（原文）

> Large language models (LLMs) face significant computational and memory challenges, making extremely low-bit quantization crucial for their efficient deployment. In this work, we introduce SDQ-LLM: Sigma-Delta Quantization for 1-bit LLMs of any size, a novel framework that enables extremely low-bit quantization of LLMs while preserving their linguistic reasoning capabilities. A distinctive feature of SDQ-LLM is the continuous adjustability of the Over-Sampling Ratio (OSR), enabling dynamic adaptation to memory or VRAM constraints by selecting fractional OSR (e.g. 2.5 times) for an optimal trade-off between model size and accuracy. SDQ-LLM uses upsampling combined with Sigma-Delta Quantizer to binarize or ternarize LLMs weights, encoding high-precision parameters into 1-bit or 1.58-bit representations, replacing the multiplication operations within linear layers with addition. This approach significantly enhances inference efficiency under extremely low-bit quantization. To further reduce the loss of quantization precision, we incorporate Hadamard-based weight smoothing prior to quantization, improving the stability and robustness of the weight representations. Furthermore, to fully leverage the continuity of the OSR and reduce precision loss, recognizing the correlation between quantization sensitivity and weight variance, we propose a fine-grained, layer- and linear-wise OSR allocation strategy, MultiOSR. This strategy distributes OSR both across layers and within each layer, based on weight variance and parameter scale. Finally, extensive experiments on OPT and LLaMA model families demonstrate that SDQ-LLM achieves a more efficient and high-precision performance even under highly aggressive low-OSR settings. Our code is available at https://github.com/Dreamlittlecat/LLM-Quant-Factory.

