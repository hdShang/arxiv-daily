---
layout: default
title: WaveSeg: Enhancing Segmentation Precision via High-Frequency Prior and Mamba-Driven Spectrum Decomposition
---

# WaveSeg: Enhancing Segmentation Precision via High-Frequency Prior and Mamba-Driven Spectrum Decomposition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21079" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21079v1</a>
  <a href="https://arxiv.org/pdf/2510.21079.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21079v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21079v1', 'WaveSeg: Enhancing Segmentation Precision via High-Frequency Prior and Mamba-Driven Spectrum Decomposition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guoan Xu, Yang Xiao, Wenjing Jia, Guangwei Gao, Guo-Jun Qi, Chia-Wen Lin

**分类**: cs.CV

**发布日期**: 2025-10-24

**备注**: 13 pages, 10 figures

---

## 💡 一句话要点

**WaveSeg：利用高频先验和Mamba驱动的频谱分解增强分割精度**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `语义分割` `高频先验` `Mamba` `小波变换` `频谱分解` `注意力机制` `深度学习`

## 📋 核心要点

1. 现有语义分割网络解码器设计简单，难以兼顾语义信息和精细细节。
2. WaveSeg利用高频先验强化边界细节，并设计Mamba驱动的频谱分解注意力模块。
3. 实验表明，WaveSeg在标准数据集上超越现有方法，实现了高效精确的分割。

## 📝 摘要（中文）

本文提出了一种新的解码器架构WaveSeg，旨在解决语义分割网络中解码器过于简单，导致语义上下文和精细细节保留之间权衡不佳的问题。WaveSeg联合优化空间域和小波域的特征细化。首先，从输入图像中学习高频分量作为显式先验，以增强早期阶段的边界细节。然后，应用多尺度融合机制DDO，并提出新的频谱分解注意力（SDA）块，利用Mamba的线性复杂度长程建模来增强高频结构细节。同时，应用重参数化卷积来保持小波域中的低频语义完整性。最后，残差引导融合将多尺度特征与原始分辨率下的边界感知表示相结合，生成语义和结构丰富的特征图。在标准基准上的大量实验表明，WaveSeg利用小波域频率先验和基于Mamba的注意力机制，在定量和定性方面均优于最先进的方法，实现了高效和精确的分割。

## 🔬 方法详解

**问题定义**：现有语义分割网络通常依赖强大的预训练编码器，但解码器设计相对简单，导致在语义上下文的理解和精细细节的保留之间存在权衡问题。尤其是在高分辨率图像的分割任务中，如何有效捕捉和利用图像的边缘和纹理等高频信息是一个挑战。

**核心思路**：WaveSeg的核心思路是在解码阶段引入高频先验，并利用Mamba架构的长程建模能力，在小波域中对图像的频谱进行分解和处理，从而更有效地提取和利用图像的结构细节。通过显式地学习和利用高频信息，可以增强分割结果的边界清晰度和细节准确性。

**技术框架**：WaveSeg的整体架构包含以下几个主要模块：1) **高频先验学习**：从输入图像中提取高频分量作为先验知识。2) **双域操作（DDO）**：在空间域和小波域中进行多尺度特征融合。3) **频谱分解注意力（SDA）**：利用Mamba架构对小波域中的频谱进行分解和注意力加权，增强高频结构细节。4) **重参数化卷积**：在小波域中保持低频语义完整性。5) **残差引导融合**：将多尺度特征与边界感知表示进行融合，生成最终的分割结果。

**关键创新**：WaveSeg的关键创新在于以下几点：1) **显式高频先验**：将高频信息作为先验知识引入解码器，增强边界细节。2) **Mamba驱动的频谱分解注意力（SDA）**：利用Mamba架构的长程建模能力，在小波域中对频谱进行分解和注意力加权，更有效地提取结构细节。3) **双域操作（DDO）**：在空间域和小波域中进行特征融合，兼顾语义信息和细节信息。与现有方法相比，WaveSeg更注重对图像高频信息的利用，并通过Mamba架构实现了更高效的长程依赖建模。

**关键设计**：1) **高频先验学习**：具体实现方式未知，可能通过卷积或小波变换等方式提取高频分量。2) **频谱分解注意力（SDA）**：使用Mamba架构进行序列建模，具体参数设置未知。3) **重参数化卷积**：具体实现方式未知，可能使用结构重参数化技术来提升卷积的表达能力。4) **损失函数**：可能使用交叉熵损失或Dice损失等常用的分割损失函数，也可能引入针对边界的损失函数。

## 📊 实验亮点

WaveSeg在多个标准数据集上取得了显著的性能提升。具体数据未知，但论文强调WaveSeg在定量和定性方面均优于现有最先进的方法，表明其在分割精度和视觉效果上都有明显优势。尤其是在需要精细分割的任务中，WaveSeg的优势更加明显。

## 🎯 应用场景

WaveSeg在医学图像分析、遥感图像处理、自动驾驶等领域具有广泛的应用前景。例如，在医学图像分割中，可以更精确地分割肿瘤等病灶区域；在遥感图像处理中，可以更准确地识别地物类型；在自动驾驶中，可以更可靠地识别道路和障碍物。该研究有助于提升图像分割的精度和效率，具有重要的实际应用价值。

## 📄 摘要（原文）

> While recent semantic segmentation networks heavily rely on powerful pretrained encoders, most employ simplistic decoders, leading to suboptimal trade-offs between semantic context and fine-grained detail preservation. To address this, we propose a novel decoder architecture, WaveSeg, which jointly optimizes feature refinement in spatial and wavelet domains. Specifically, high-frequency components are first learned from input images as explicit priors to reinforce boundary details at early stages. A multi-scale fusion mechanism, Dual Domain Operation (DDO), is then applied, and the novel Spectrum Decomposition Attention (SDA) block is proposed, which is developed to leverage Mamba's linear-complexity long-range modeling to enhance high-frequency structural details. Meanwhile, reparameterized convolutions are applied to preserve low-frequency semantic integrity in the wavelet domain. Finally, a residual-guided fusion integrates multi-scale features with boundary-aware representations at native resolution, producing semantically and structurally rich feature maps. Extensive experiments on standard benchmarks demonstrate that WaveSeg, leveraging wavelet-domain frequency prior with Mamba-based attention, consistently outperforms state-of-the-art approaches both quantitatively and qualitatively, achieving efficient and precise segmentation.

