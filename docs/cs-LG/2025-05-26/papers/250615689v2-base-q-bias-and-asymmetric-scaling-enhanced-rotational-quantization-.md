---
layout: default
title: "BASE-Q: Bias and Asymmetric Scaling Enhanced Rotational Quantization for Large Language Models"
---

# BASE-Q: Bias and Asymmetric Scaling Enhanced Rotational Quantization for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15689" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15689v2</a>
  <a href="https://arxiv.org/pdf/2506.15689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15689v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15689v2', 'BASE-Q: Bias and Asymmetric Scaling Enhanced Rotational Quantization for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liulu He, Shenli Zheng, Karwei Sun, Yijiang Liu, Yufei Zhao, Chongkang Tan, Huanrui Yang, Yuan Du, Li Du

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-26 (更新: 2025-08-29)

---

## 💡 一句话要点

**提出BASE-Q以解决大语言模型量化中的偏差与剪切误差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `大语言模型` `旋转量化` `偏差修正` `非对称缩放` `深度学习` `模型优化`

## 📋 核心要点

1. 现有的旋转量化方法存在两个主要问题：未能对齐通道均值和导致激活分布更高斯化，增加了舍入和剪切误差。
2. BASE-Q通过结合偏差修正和非对称缩放，旨在有效减少量化过程中的舍入和剪切误差，同时支持块级优化以降低内存消耗。
3. 实验结果显示，BASE-Q在多个大语言模型上相较于现有方法（如QuaRot、SpinQuant和OSTQuant）分别缩小了50.5%、42.9%和29.2%的准确性差距。

## 📝 摘要（中文）

旋转在大语言模型的量化管道中变得至关重要，能够有效平滑权重和激活值中的异常值。然而，进一步优化旋转参数的效果有限，并且引入了显著的训练开销。本文识别了当前旋转量化方法的两个基本局限性：旋转未能对齐通道均值，导致量化范围更宽和舍入误差增加；旋转使激活分布更接近高斯分布，增加了因剪切误差造成的能量损失。为了解决这些问题，本文提出了BASE-Q，这是一种结合偏差修正和非对称缩放的简单而有效的方法，能够有效减少舍入和剪切误差。此外，BASE-Q支持块级优化，消除了对内存密集型全模型反向传播的需求。大量实验表明，BASE-Q在多个基准上显著提高了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决当前旋转量化方法在对齐通道均值和激活分布方面的不足，导致的量化误差和能量损失问题。现有方法在优化旋转参数时，需加载全模型进行反向传播，造成显著的内存消耗。

**核心思路**：BASE-Q的核心思想是结合偏差修正和非对称缩放，通过优化量化过程中的参数设置，减少舍入和剪切误差，同时支持块级优化，降低内存需求。

**技术框架**：BASE-Q的整体架构包括偏差修正模块和非对称缩放模块，首先对权重和激活值进行偏差修正，然后应用非对称缩放以优化量化过程，最后通过块级优化实现高效的模型训练。

**关键创新**：BASE-Q的主要创新在于引入了偏差修正和非对称缩放的结合，显著改善了旋转量化的效果，并且支持块级优化，避免了全模型反向传播的内存瓶颈。

**关键设计**：在设计中，BASE-Q采用了特定的损失函数来平衡舍入和剪切误差，同时在参数设置上进行了优化，以确保在不同模型和数据集上均能有效运行。

## 📊 实验亮点

实验结果表明，BASE-Q在多个大语言模型上相较于现有的量化方法（如QuaRot、SpinQuant和OSTQuant）分别缩小了50.5%、42.9%和29.2%的准确性差距，显示出显著的性能提升。

## 🎯 应用场景

BASE-Q的研究成果在大语言模型的量化领域具有广泛的应用潜力，尤其是在资源受限的环境中，能够有效降低内存消耗并提高模型的推理效率。未来，该方法可扩展至其他深度学习模型和任务，推动量化技术的进一步发展。

## 📄 摘要（原文）

> Rotations have become essential to state-of-the-art quantization pipelines for large language models (LLMs) by effectively smoothing outliers in weights and activations. However, further optimizing the rotation parameters offers only limited performance gains and introduces significant training overhead: due to rotation parameter sharing, full-model must be loaded simultaneously to enable backpropagation, resulting in substantial memory consumption and limited practical utility. In this work, we identify two fundamental limitations of current rotational quantization methods: (i) rotation fails to align channel means, resulting in wider quantization bounds and increased rounding errors; and (ii) rotation makes the activation distribution more Gaussian-like, increasing energy loss caused by clipping errors. To address these issues, we introduce \textbf{BASE-Q}, a simple yet powerful approach that combines bias correction and asymmetric scaling to effectively reduce rounding and clipping errors. Furthermore, BASE-Q enables blockwise optimization, eliminating the need for memory-intensive full-model backpropagation. Extensive experiments on various LLMs and benchmarks demonstrate the effectiveness of BASE-Q, narrowing the accuracy gap to full-precision models by 50.5\%, 42.9\%, and 29.2\% compared to QuaRot, SpinQuant, and OSTQuant, respectively. The code will be released soon.

