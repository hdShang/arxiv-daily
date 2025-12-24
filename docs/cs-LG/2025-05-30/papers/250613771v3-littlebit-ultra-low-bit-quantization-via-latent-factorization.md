---
layout: default
title: LittleBit: Ultra Low-Bit Quantization via Latent Factorization
---

# LittleBit: Ultra Low-Bit Quantization via Latent Factorization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13771" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13771v3</a>
  <a href="https://arxiv.org/pdf/2506.13771.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13771v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13771v3', 'LittleBit: Ultra Low-Bit Quantization via Latent Factorization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Banseok Lee, Dongkyu Kim, Youngcheon You, Youngmin Kim

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-30 (更新: 2025-12-04)

**备注**: Accepted to NeurIPS 2025. Banseok Lee and Dongkyu Kim contributed equally

**🔗 代码/项目**: [GITHUB](https://github.com/SamsungLabs/LittleBit)

---

## 💡 一句话要点

**提出LittleBit以解决大语言模型超低比特量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `大语言模型` `低比特量化` `潜在矩阵分解` `模型压缩` `计算效率` `资源优化`

## 📋 核心要点

1. 现有的量化方法在亚1比特量化中面临显著的性能下降，限制了大型语言模型的实际应用。
2. LittleBit通过潜在矩阵分解和多尺度补偿机制，提出了一种新的极端量化方法，能够有效减少内存占用。
3. 实验表明，LittleBit在Llama2-7B上的0.1 BPW性能优于现有最佳方法的0.7 BPW，显示出显著的性能提升。

## 📝 摘要（中文）

在部署大型语言模型（LLMs）时，通常面临显著的内存和计算成本挑战。量化提供了一种解决方案，但在亚1比特范围内的性能下降尤其困难。本文介绍了LittleBit，这是一种极端LLM压缩的新方法，目标是每个权重0.1比特（BPW），实现了近31倍的内存减少，例如将Llama2-13B压缩至0.9 GB以下。LittleBit通过潜在矩阵分解以低秩形式表示权重，并随后对这些因子进行二值化。为抵消极端精度带来的信息损失，它集成了多尺度补偿机制，包括行、列和额外的潜在维度，以学习每个秩的重要性。实验结果确认LittleBit在亚1比特量化中的优越性，其在Llama2-7B上的0.1 BPW性能超过了领先方法的0.7 BPW。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在量化过程中面临的内存和计算成本高的问题，尤其是在亚1比特量化时性能下降的挑战。现有方法在极低比特量化时往往无法保持模型性能，限制了其在资源受限环境中的应用。

**核心思路**：LittleBit的核心思路是通过潜在矩阵分解将权重表示为低秩形式，并对这些因子进行二值化。通过引入多尺度补偿机制，LittleBit能够有效抵消因极端量化带来的信息损失，从而保持模型性能。

**技术框架**：LittleBit的整体架构包括权重的低秩表示、因子的二值化以及多尺度补偿机制。具体而言，模型首先通过潜在矩阵分解获取低秩表示，然后对这些表示进行二值化，最后通过行、列和额外的潜在维度进行补偿，以学习每个秩的重要性。

**关键创新**：本研究的关键创新在于提出了双符号值独立分解（Dual-SVID）用于量化感知训练（QAT）初始化，以及集成残差补偿机制以减轻误差。这些创新使得在极低比特量化下仍能保持较高的模型性能。

**关键设计**：在参数设置上，LittleBit采用了低秩矩阵分解的策略，损失函数设计考虑了量化误差和补偿机制的结合，网络结构则通过引入多尺度补偿来增强模型的鲁棒性。

## 📊 实验亮点

实验结果显示，LittleBit在Llama2-7B上的0.1 BPW性能超过了现有最佳方法的0.7 BPW，展现出显著的性能提升。此外，LittleBit在内存占用上实现了近31倍的减少，并在内核级别上提供了11.6倍的速度提升，相较于FP16，极大地改善了模型的实用性。

## 🎯 应用场景

LittleBit的研究成果在资源受限的环境中具有广泛的应用潜力，尤其是在移动设备、边缘计算和嵌入式系统中。通过极端量化，大型语言模型能够在保持性能的同时显著降低内存和计算需求，从而推动智能应用的普及和发展。

## 📄 摘要（原文）

> Deploying large language models (LLMs) often faces challenges from substantial memory and computational costs. Quantization offers a solution, yet performance degradation in the sub-1-bit regime remains particularly difficult. This paper introduces LittleBit, a novel method for extreme LLM compression. It targets levels like 0.1 bits per weight (BPW), achieving nearly 31$\times$ memory reduction, e.g., Llama2-13B to under 0.9 GB. LittleBit represents weights in a low-rank form using latent matrix factorization, subsequently binarizing these factors. To counteract information loss from this extreme precision, it integrates a multi-scale compensation mechanism. This includes row, column, and an additional latent dimension that learns per-rank importance. Two key contributions enable effective training: Dual Sign-Value-Independent Decomposition (Dual-SVID) for quantization-aware training (QAT) initialization, and integrated Residual Compensation to mitigate errors. Extensive experiments confirm LittleBit's superiority in sub-1-bit quantization: e.g., its 0.1 BPW performance on Llama2-7B surpasses the leading method's 0.7 BPW. LittleBit establishes a new, viable size-performance trade-off--unlocking a potential 11.6$\times$ speedup over FP16 at the kernel level--and makes powerful LLMs practical for resource-constrained environments. Our code can be found at https://github.com/SamsungLabs/LittleBit.

