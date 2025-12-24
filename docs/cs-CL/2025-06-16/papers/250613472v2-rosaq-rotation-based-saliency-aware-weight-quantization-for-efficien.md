---
layout: default
title: "ROSAQ: Rotation-based Saliency-Aware Weight Quantization for Efficiently Compressing Large Language Models"
---

# ROSAQ: Rotation-based Saliency-Aware Weight Quantization for Efficiently Compressing Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13472" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13472v2</a>
  <a href="https://arxiv.org/pdf/2506.13472.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13472v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13472v2', 'ROSAQ: Rotation-based Saliency-Aware Weight Quantization for Efficiently Compressing Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junho Yoon, Geom Lee, Donghyeon Jeon, Inho Kang, Seung-Hoon Na

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-16 (更新: 2025-06-17)

**备注**: 10 pages, 2 figures

---

## 💡 一句话要点

**提出ROSAQ以解决大语言模型量化效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `大语言模型` `显著性感知` `主成分分析` `混合精度`

## 📋 核心要点

1. 现有的量化方法在处理大型语言模型时，往往无法有效识别和利用显著特征，导致性能损失。
2. ROSAQ通过利用变换器的旋转不变性，提出了一种在投影特征空间中识别显著通道的量化方法，提升了量化效率。
3. 实验结果显示，ROSAQ在生成256个token时，相比于FP16实现，速度提升约2.3倍，且在显著性感知量化上表现优于基线方法。

## 📝 摘要（中文）

量化作为一种有效的技术，广泛应用于减少大型语言模型（LLMs）的内存需求，并可能改善延迟时间。本文提出了一种基于旋转的显著性感知权重量化方法（ROSAQ），该方法在投影特征空间中识别显著通道，而非在原始特征空间中进行识别。ROSAQ包括三个主要步骤：1）基于主成分分析（PCA）的投影，首先对校准集进行PCA分析并通过PCA投影进行转换；2）显著通道识别，选择与K个最大特征值对应的维度作为显著通道；3）显著性感知的混合精度量化，对显著维度使用FP16，对其他维度使用INT3/4。实验结果表明，ROSAQ在原始特征空间的显著性感知量化和其他现有量化方法上均有改进。通过内核融合，ROSAQ在生成256个token时，相比FP16实现速度提升约2.3倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型量化过程中显著特征识别不足的问题，现有方法在原始特征空间中难以有效识别显著通道，导致量化效果不佳。

**核心思路**：ROSAQ的核心思路是利用变换器的旋转不变性，在投影特征空间中识别显著通道，从而实现更高效的权重量化。通过选择与最大特征值对应的维度，ROSAQ能够更好地保留重要信息。

**技术框架**：ROSAQ的整体架构包括三个主要模块：1）PCA投影模块，对校准集进行主成分分析并进行特征转换；2）显著通道识别模块，选择K个最大特征值对应的维度作为显著通道；3）混合精度量化模块，对显著维度使用FP16，对其他维度使用INT3/4进行量化。

**关键创新**：ROSAQ的关键创新在于其在投影特征空间中进行显著性感知量化，这一方法与传统在原始特征空间中进行量化的方式有本质区别，能够更有效地识别和利用显著特征。

**关键设计**：在ROSAQ中，PCA的参数设置和K值的选择是关键设计因素，确保显著通道的准确识别和量化效果的优化。此外，混合精度量化的设计使得在不同维度上使用不同的精度，从而进一步提升了模型的性能。

## 📊 实验亮点

ROSAQ在实验中表现出显著的性能提升，生成256个token时，相比于FP16实现速度提升约2.3倍。此外，ROSAQ在显著性感知量化方面的表现优于现有的基线方法，展现了其在量化效率上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等大型语言模型的优化。ROSAQ能够有效减少模型的内存占用，提高推理速度，具有重要的实际价值和广泛的应用前景，尤其是在资源受限的环境中。

## 📄 摘要（原文）

> Quantization has been widely studied as an effective technique for reducing the memory requirement of large language models (LLMs), potentially improving the latency time as well. Utilizing the characteristic of rotational invariance of transformer, we propose the rotation-based saliency-aware weight quantization (ROSAQ), which identifies salient channels in the projection feature space, not in the original feature space, where the projected "principal" dimensions are naturally considered as "salient" features. The proposed ROSAQ consists of 1) PCA-based projection, which first performs principal component analysis (PCA) on a calibration set and transforms via the PCA projection, 2) Salient channel dentification, which selects dimensions corresponding to the K-largest eigenvalues as salient channels, and 3) Saliency-aware quantization with mixed-precision, which uses FP16 for salient dimensions and INT3/4 for other dimensions. Experiment results show that ROSAQ shows improvements over the baseline saliency-aware quantization on the original feature space and other existing quantization methods. With kernel fusion, ROSAQ presents about 2.3x speed up over FP16 implementation in generating 256 tokens with a batch size of 64.

