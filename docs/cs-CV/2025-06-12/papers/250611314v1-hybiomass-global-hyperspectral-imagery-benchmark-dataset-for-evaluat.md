---
layout: default
title: "HyBiomass: Global Hyperspectral Imagery Benchmark Dataset for Evaluating Geospatial Foundation Models in Forest Aboveground Biomass Estimation"
---

# HyBiomass: Global Hyperspectral Imagery Benchmark Dataset for Evaluating Geospatial Foundation Models in Forest Aboveground Biomass Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11314" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11314v1</a>
  <a href="https://arxiv.org/pdf/2506.11314.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11314v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11314v1', 'HyBiomass: Global Hyperspectral Imagery Benchmark Dataset for Evaluating Geospatial Foundation Models in Forest Aboveground Biomass Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aaron Banze, Timothée Stassin, Nassim Ait Ali Braham, Rıdvan Salih Kuzu, Simon Besnard, Michael Schmitt

**分类**: cs.CV, eess.IV

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出HyBiomass数据集以解决森林生物量估计的基准评估问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `高光谱影像` `森林生物量` `地理基础模型` `数据集构建` `像素级回归` `模型评估` `生态监测`

## 📋 核心要点

1. 现有的基准数据集主要集中于分割和分类任务，缺乏针对森林生物量估计的全球性数据支持。
2. 本文提出了一个全球分布的高光谱影像数据集，结合了不同地区的AGB密度估计，解决了现有数据集的局限性。
3. 实验结果显示，Geo-FMs在性能上可与U-Net相媲美，且在特定条件下表现更优，强调了数据集规模和补丁大小的重要性。

## 📝 摘要（中文）

全面评估地理基础模型（Geo-FMs）需要在多样化任务、传感器和地理区域之间进行基准测试。然而，现有的基准数据集大多仅限于分割或分类任务，并且集中于特定地理区域。为了解决这一问题，本文提出了一个全球分布的数据集，用于森林地上生物量（AGB）估计，这是一个逐像素回归任务。该基准数据集结合了来自环境映射与分析计划（EnMAP）卫星的共定位高光谱影像（HSI）和来自全球生态系统动态调查激光雷达的AGB密度估计预测，覆盖七个大陆区域。实验结果表明，评估的Geo-FMs在性能上可以与基线U-Net相匹配，甚至在某些情况下超越它，尤其是在对编码器进行微调时。我们还发现U-Net与Geo-FMs之间的性能差异取决于每个区域的数据集大小，并强调了在逐像素回归任务中，视觉变换器主干中令牌补丁大小的重要性。通过发布这一全球分布的高光谱基准数据集，我们旨在促进Geo-FMs在HSI应用中的开发与评估。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基准数据集在森林生物量估计任务中的不足，特别是缺乏全球范围内的高光谱影像数据。现有方法往往局限于特定区域，无法全面评估Geo-FMs的性能。

**核心思路**：通过构建一个全球分布的高光谱影像数据集，结合AGB密度估计，提供一个多样化的基准测试平台，以促进Geo-FMs在森林生物量估计中的应用和评估。

**技术框架**：该研究的整体架构包括数据集的构建、模型的训练与评估。数据集由来自EnMAP卫星的高光谱影像和激光雷达的AGB预测组成，模型评估则采用U-Net和Geo-FMs进行对比。

**关键创新**：最重要的创新点在于提出了一个全球性的高光谱影像基准数据集，填补了现有数据集在森林生物量估计任务中的空白，且通过实验验证了Geo-FMs的有效性。

**关键设计**：在模型训练中，采用了针对不同区域的数据集大小和补丁大小的优化策略，特别强调了视觉变换器主干中令牌补丁大小对逐像素回归任务的影响。实验中使用了标准的损失函数和网络结构设计，以确保模型的有效性和可比性。

## 📊 实验亮点

实验结果表明，Geo-FMs在多个区域的性能与基线U-Net相当，甚至在某些情况下超越了U-Net，尤其是在对编码器进行微调时。研究还发现，模型性能与数据集大小和补丁大小密切相关，为逐像素回归任务提供了新的见解。

## 🎯 应用场景

该研究的潜在应用领域包括森林资源管理、生态监测和环境保护等。通过提供一个标准化的数据集，研究人员和开发者可以更有效地评估和优化Geo-FMs在高光谱影像分析中的应用，推动相关技术的发展与应用。未来，该数据集还可以用于研究地理偏差和模型的泛化能力，具有重要的实际价值。

## 📄 摘要（原文）

> Comprehensive evaluation of geospatial foundation models (Geo-FMs) requires benchmarking across diverse tasks, sensors, and geographic regions. However, most existing benchmark datasets are limited to segmentation or classification tasks, and focus on specific geographic areas. To address this gap, we introduce a globally distributed dataset for forest aboveground biomass (AGB) estimation, a pixel-wise regression task. This benchmark dataset combines co-located hyperspectral imagery (HSI) from the Environmental Mapping and Analysis Program (EnMAP) satellite and predictions of AGB density estimates derived from the Global Ecosystem Dynamics Investigation lidars, covering seven continental regions. Our experimental results on this dataset demonstrate that the evaluated Geo-FMs can match or, in some cases, surpass the performance of a baseline U-Net, especially when fine-tuning the encoder. We also find that the performance difference between the U-Net and Geo-FMs depends on the dataset size for each region and highlight the importance of the token patch size in the Vision Transformer backbone for accurate predictions in pixel-wise regression tasks. By releasing this globally distributed hyperspectral benchmark dataset, we aim to facilitate the development and evaluation of Geo-FMs for HSI applications. Leveraging this dataset additionally enables research into geographic bias and generalization capacity of Geo-FMs. The dataset and source code will be made publicly available.

