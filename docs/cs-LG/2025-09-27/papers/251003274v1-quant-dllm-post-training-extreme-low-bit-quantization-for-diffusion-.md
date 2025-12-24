---
layout: default
title: "Quant-dLLM: Post-Training Extreme Low-Bit Quantization for Diffusion Large Language Models"
---

# Quant-dLLM: Post-Training Extreme Low-Bit Quantization for Diffusion Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03274" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03274v1</a>
  <a href="https://arxiv.org/pdf/2510.03274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03274v1', 'Quant-dLLM: Post-Training Extreme Low-Bit Quantization for Diffusion Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianao Zhang, Zhiteng Li, Xianglong Yan, Haotong Qin, Yong Guo, Yulun Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/ZTA2785/Quant-dLLM)

---

## 💡 一句话要点

**Quant-dLLM：面向扩散大语言模型的后训练极低比特量化框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散大语言模型` `后训练量化` `极低比特量化` `模型压缩` `掩码校准模拟`

## 📋 核心要点

1. 现有后训练量化方法在直接应用于扩散大语言模型时，在极低比特（如2比特）下性能显著下降。
2. Quant-dLLM通过掩码校准模拟(MCS)和数据感知任意阶量化器(DAQ)等技术，专门为dLLMs设计超低比特量化方案。
3. 实验表明，Quant-dLLM在2比特精度下，相比于将AR模型量化方法迁移到dLLM上，能取得更高的准确率。

## 📝 摘要（中文）

扩散大语言模型(dLLMs)提供双向上下文和灵活的掩码去噪生成，正成为自回归(AR) LLMs的一个引人注目的替代方案。然而，与AR LLMs一样，它们的模型大小持续增长，这促使人们对部署进行权重压缩。虽然后训练量化(PTQ)对于AR LLMs是有效的，但直接将其应用于2比特的dLLMs会导致不令人满意的性能。为了应对这些挑战，我们提出了Quant-dLLM，这是一个为dLLMs量身定制的超低比特PTQ框架。由于dLLMs中的掩码去噪激活与标准PTQ方法假设的完全可见信号不同，我们引入了掩码校准模拟(MCS)来使校准与时间步相关的掩码对齐，从而产生更可靠的校准。此外，我们提出了一种数据感知任意阶量化器(DAQ)，它通过优化算法学习超低比特权重表示。它执行由我们模拟的校准数据指导的迭代近似。此外，在严格的2比特预算下，我们引入了自适应分块混合精度(ABMP)，这是一种基于敏感性的精度分配方案，可以自适应地在通道组之间分配比特宽度。当限制为2比特精度时，Quant-dLLM始终比dLLMs上最先进的(SOTA) AR-transfer PTQ方法获得更高的精度。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散大语言模型（dLLMs）在部署时模型体积过大，难以进行低成本部署的问题。现有的后训练量化（PTQ）方法虽然在自回归（AR）LLMs上表现良好，但直接应用于dLLMs，尤其是在极低比特（如2-bit）量化时，性能会急剧下降。这是因为dLLMs的掩码去噪激活与AR模型不同，标准PTQ方法无法有效处理。

**核心思路**：论文的核心思路是针对dLLMs的特性，设计专门的PTQ框架。通过模拟dLLMs的掩码过程进行校准，使量化过程更好地适应dLLMs的激活分布。同时，设计数据感知的量化器，学习更适合dLLMs的权重表示，并根据不同通道的重要性自适应地分配比特数。

**技术框架**：Quant-dLLM框架主要包含三个核心模块：1) 掩码校准模拟（MCS）：模拟dLLMs的掩码过程，生成更可靠的校准数据。2) 数据感知任意阶量化器（DAQ）：通过优化算法学习超低比特权重表示。3) 自适应分块混合精度（ABMP）：根据通道敏感性自适应地分配比特宽度。

**关键创新**：论文的关键创新在于针对dLLMs的特性，提出了掩码校准模拟（MCS）和数据感知任意阶量化器（DAQ）。MCS通过模拟dLLMs的掩码过程，解决了标准PTQ方法无法有效处理dLLMs激活分布的问题。DAQ则通过优化算法，学习更适合dLLMs的权重表示，提高了量化后的模型性能。ABMP进一步提升了量化效率，在有限的比特预算下，实现了更好的性能。

**关键设计**：掩码校准模拟（MCS）的关键在于模拟时间步相关的掩码过程，生成更真实的校准数据。数据感知任意阶量化器（DAQ）的关键在于设计合适的优化算法，学习超低比特权重表示。自适应分块混合精度（ABMP）的关键在于设计合适的敏感性指标，并根据敏感性指标自适应地分配比特宽度。具体的损失函数和网络结构等细节未在摘要中详细描述。

## 📊 实验亮点

Quant-dLLM在2比特精度下，相比于直接将AR模型的PTQ方法应用于dLLMs，取得了显著的性能提升。具体的数据和对比基线需要在论文全文中查找。该方法在极低比特量化下，保持了较高的模型精度，证明了其在dLLMs量化方面的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要部署扩散大语言模型的场景，例如移动设备、边缘计算设备等资源受限的环境。通过极低比特量化，可以显著降低模型体积和计算复杂度，从而实现dLLMs在这些设备上的高效部署和应用。这对于推动dLLMs在自然语言处理、图像生成等领域的广泛应用具有重要意义。

## 📄 摘要（原文）

> Diffusion large language models (dLLMs), which offer bidirectional context and flexible masked-denoising generation, are emerging as a compelling alternative to autoregressive (AR) LLMs. However, like AR LLMs, their model sizes continue to grow, motivating weight compression for deployment. Although post-training quantization (PTQ) is effective for AR LLMs, directly transferring it to dLLMs at 2-bit leads to unsatisfactory performance. To tackle these challenges, we propose Quant-dLLM, an ultra-low-bit PTQ framework tailored to dLLMs. Since masked-denoising activations in dLLMs differ from the fully visible signals assumed by standard PTQ methods, we introduce Masked Calibration Simulation (MCS) to align calibration with the timestep-dependent masking, which yields more reliable calibrations. Moreover, we propose a Data-aware Any-order Quantizer (DAQ) that learns ultra-low-bit weight representations via an optimization algorithm. It performs iterative approximation guided by our simulated calibration data. In addition, under a strict 2-bit budget, we introduce Adaptive Blockwise Mixed Precision (ABMP), a sensitivity-based precision allocation scheme that adaptively assigns bit width across channel groups. When restricted to 2-bit precision, Quant-dLLM consistently achieves higher accuracy than state-of-the-art (SOTA) AR-transfer PTQ methods on dLLMs. The code and models will be available at: https://github.com/ZTA2785/Quant-dLLM.

