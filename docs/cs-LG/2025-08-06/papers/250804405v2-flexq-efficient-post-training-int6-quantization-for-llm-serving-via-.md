---
layout: default
title: "FlexQ: Efficient Post-training INT6 Quantization for LLM Serving via Algorithm-System Co-Design"
---

# FlexQ: Efficient Post-training INT6 Quantization for LLM Serving via Algorithm-System Co-Design

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04405" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04405v2</a>
  <a href="https://arxiv.org/pdf/2508.04405.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04405v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04405v2', 'FlexQ: Efficient Post-training INT6 Quantization for LLM Serving via Algorithm-System Co-Design')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Zhang, Aining Jia, Weifeng Bu, Yushu Cai, Kai Sheng, Hao Chen, Xin He

**分类**: cs.LG

**发布日期**: 2025-08-06 (更新: 2025-11-03)

**🔗 代码/项目**: [GITHUB](https://github.com/FlyFoxPlayer/FlexQ)

---

## 💡 一句话要点

**提出FlexQ以解决大语言模型量化效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `大语言模型` `推理加速` `GPU优化` `深度学习`

## 📋 核心要点

1. 现有的INT4/INT8量化方法在降低大语言模型的内存和计算成本时，往往会导致准确性下降或效率不足。
2. FlexQ提出了一种后训练INT6量化框架，结合算法创新与系统优化，采用统一的6位权重量化和自适应的8位激活保留策略。
3. 实验结果表明，FlexQ在保持接近FP16准确性的同时，推理加速达到1.33倍，内存节省达到1.21倍，表现优于现有方法。

## 📝 摘要（中文）

大语言模型（LLMs）表现出色，但其高内存和计算成本限制了实际部署。现有的INT4/INT8量化方法虽然降低了这些成本，但往往会降低准确性或效率不佳。INT6量化在模型准确性和推理效率之间提供了更好的平衡，但现代GPU缺乏硬件支持，导致只能通过高精度算术单元进行仿真，从而限制了加速。本文提出了FlexQ，一个结合算法创新与系统级优化的后训练INT6量化框架。FlexQ在所有层中采用统一的6位权重量化，并通过层级敏感性分析自适应保留8位激活。为最大化硬件效率，我们开发了一个支持W6A6和W6A8表示的高性能GPU内核，成功绕过了缺乏原生INT6张量核心的问题。对LLaMA系列模型的评估显示，FlexQ在WikiText2上保持了接近FP16的准确性，困惑度增加不超过0.1。该内核在LLaMA-2-70B线性层上实现了平均1.39倍的加速，整体上，FlexQ在推理上实现了1.33倍的加速和1.21倍的内存节省。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理过程中面临的高内存和计算成本问题。现有的INT4/INT8量化方法虽然能够降低这些成本，但通常会导致模型准确性下降或效率不足。

**核心思路**：FlexQ框架通过引入INT6量化，提供了更优的模型准确性与推理效率之间的平衡。该方法在所有层中采用统一的6位权重量化，并通过层级敏感性分析自适应保留8位激活，以提高整体性能。

**技术框架**：FlexQ的整体架构包括权重量化模块、激活保留模块和高性能GPU内核。权重量化模块负责将模型权重转换为6位表示，激活保留模块则根据层的敏感性决定是否保留8位激活，最后通过专门的GPU内核实现高效的矩阵乘法运算。

**关键创新**：FlexQ的主要创新在于结合了算法与系统级的优化，尤其是开发了支持W6A6和W6A8表示的高性能GPU内核，成功绕过了缺乏原生INT6张量核心的问题。这一设计显著提升了推理效率。

**关键设计**：在参数设置上，FlexQ采用了统一的6位权重量化，并通过层级敏感性分析来决定激活的位数。此外，所设计的GPU内核利用了二进制张量核心（BTC）等效技术，确保了高效的矩阵运算。整体设计旨在最大化硬件利用率和推理性能。

## 📊 实验亮点

FlexQ在LLaMA系列模型上的实验结果显示，保持了接近FP16的准确性，困惑度增加不超过0.1。同时，该框架在LLaMA-2-70B线性层上实现了平均1.39倍的加速，整体推理加速达到1.33倍，内存节省达到1.21倍，展现了显著的性能提升。

## 🎯 应用场景

FlexQ的研究成果具有广泛的应用潜力，特别是在需要高效推理的大语言模型部署场景中。其高效的量化方法和优化的GPU内核设计，可以显著降低内存和计算成本，推动大语言模型在实际应用中的普及，如智能助手、自动翻译和内容生成等领域。未来，FlexQ的技术可以进一步扩展到其他深度学习模型的优化中，提升整体计算效率。

## 📄 摘要（原文）

> Large Language Models (LLMs) demonstrate exceptional performance but entail significant memory and computational costs, restricting their practical deployment. While existing INT4/INT8 quantization reduces these costs, they often degrade accuracy or lack optimal efficiency. INT6 quantization offers a superior trade-off between model accuracy and inference efficiency, but lacks hardware support in modern GPUs, forcing emulation via higher-precision arithmetic units that limit acceleration. In this paper, we propose FlexQ, a novel post-training INT6 quantization framework combining algorithmic innovation with system-level optimizations. FlexQ employs uniform 6-bit weight quantization across all layers, with adaptive retention of 8-bit activations in layers identified through layer-wise sensitivity analysis. To maximize hardware efficiency, we develop a specialized high-performance GPU kernel supporting matrix multiplication for W6A6 and W6A8 representations via Binary Tensor Core (BTC) equivalents, effectively bypassing the lack of native INT6 tensor cores. Evaluations on LLaMA family models show FlexQ maintains near-FP16 accuracy, with perplexity increases of no more than 0.1 on WikiText2. The proposed kernel achieves an average 1.39$\times$ speedup over ABQ-LLM on LLaMA-2-70B linear layers. End-to-end, FlexQ delivers 1.33$\times$ inference acceleration and 1.21$\times$ memory savings over SmoothQuant. Code is released at https://github.com/FlyFoxPlayer/FlexQ.

