---
layout: default
title: "Omniwise: Predicting GPU Kernels Performance with LLMs"
---

# Omniwise: Predicting GPU Kernels Performance with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20886" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20886v1</a>
  <a href="https://arxiv.org/pdf/2506.20886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20886v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20886v1', 'Omniwise: Predicting GPU Kernels Performance with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixian Wang, Cole Ramos, Muhammad A. Awad, Keith Lowery

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出Omniwise以解决GPU内核性能预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GPU性能预测` `大型语言模型` `自监督学习` `深度学习` `高性能计算`

## 📋 核心要点

1. 现有的GPU内核性能预测方法通常依赖于代码执行和复杂的分析工具，效率低下且难以扩展。
2. Omniwise提出了一种自监督微调管道，利用大型语言模型直接从内核代码进行性能预测，避免了传统方法的局限性。
3. 实验结果显示，Omniwise在AMD MI250和MI300X架构上实现了90%以上的预测相对误差在10%以内，表现出色。

## 📝 摘要（中文）

近年来，深度神经网络的快速发展彻底改变了人工智能，促使模型在理解、生成和处理复杂数据方面具备前所未有的能力。本文介绍了Omniwise，这是第一个端到端的自监督微调管道，利用大型语言模型（LLMs）进行GPU内核性能预测，开创了性能分析的新应用。Omniwise具有模型无关性和轻量级特性，即使使用小型的3B参数模型也能取得良好效果。它能够直接从内核代码预测关键性能指标，如内存带宽、缓存命中率、GFLOPs和算术强度，无需代码执行或分析工具。我们的研究在AMD MI250和MI300X架构上实现了90%以上的预测相对误差在10%以内。此外，我们还开发了一个在线推理服务器和Visual Studio Code插件，将基于LLM的性能预测无缝集成到开发者的工作流程中。

## 🔬 方法详解

**问题定义**：本文旨在解决GPU内核性能预测中的效率和准确性问题。现有方法依赖于代码执行和复杂的分析工具，导致预测过程缓慢且难以适应不同的模型和架构。

**核心思路**：Omniwise的核心思路是利用大型语言模型（LLMs）进行自监督学习，从内核代码中提取特征并预测性能指标。这种方法避免了传统性能分析的复杂性，提供了一种轻量级且高效的解决方案。

**技术框架**：Omniwise的整体架构包括数据预处理、模型训练和在线推理三个主要模块。首先，从内核代码中提取特征，然后使用自监督学习进行模型微调，最后通过在线推理服务器提供实时性能预测。

**关键创新**：Omniwise的主要创新在于将大型语言模型应用于GPU内核性能预测，这是一个全新的研究方向。与现有方法相比，Omniwise能够在不依赖代码执行的情况下，直接从代码中进行高效的性能预测。

**关键设计**：在模型设计上，Omniwise使用了3B参数的轻量级语言模型，并通过自监督学习优化了损失函数，以提高预测的准确性和效率。

## 📊 实验亮点

实验结果表明，Omniwise在AMD MI250和MI300X架构上实现了超过90%的预测相对误差在10%以内，显示出其在性能预测方面的高效性和准确性。这一成果显著优于传统依赖代码执行的性能分析方法，具有重要的实际应用价值。

## 🎯 应用场景

Omniwise的研究成果在GPU性能优化、深度学习模型开发和高性能计算等领域具有广泛的应用潜力。通过提供快速、准确的性能预测，开发者可以更高效地优化代码，提升计算资源的利用率，进而推动人工智能和高性能计算的进一步发展。

## 📄 摘要（原文）

> In recent years, the rapid advancement of deep neural networks (DNNs) has revolutionized artificial intelligence, enabling models with unprecedented capabilities in understanding, generating, and processing complex data. These powerful architectures have transformed a wide range of downstream applications, tackling tasks beyond human reach. In this paper, we introduce Omniwise, the first end-to-end, self-supervised fine-tuning pipeline that applies large language models (LLMs) to GPU kernel performance prediction--a novel use case in performance profiling. Omniwise is model-agnostic and lightweight, achieving strong results even with a small 3B-parameter model. It can predict key performance metrics, including memory bandwidth, cache hit rates, GFLOPs, and arithmetic intensity, directly from kernel code without the need for code execution or profiling tools. Our approach achieves over 90% of predictions within 10% relative error on GPU kernels executed on AMD MI250 and MI300X architectures. In addition to the pipeline, we develop an online inference server and a Visual Studio Code plugin that seamlessly integrate LLM-based performance prediction into developers' workflows.

