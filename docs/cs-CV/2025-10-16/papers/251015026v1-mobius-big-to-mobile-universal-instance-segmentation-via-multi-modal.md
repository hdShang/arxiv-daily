---
layout: default
title: "MOBIUS: Big-to-Mobile Universal Instance Segmentation via Multi-modal Bottleneck Fusion and Calibrated Decoder Pruning"
---

# MOBIUS: Big-to-Mobile Universal Instance Segmentation via Multi-modal Bottleneck Fusion and Calibrated Decoder Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15026" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15026v1</a>
  <a href="https://arxiv.org/pdf/2510.15026.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15026v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15026v1', 'MOBIUS: Big-to-Mobile Universal Instance Segmentation via Multi-modal Bottleneck Fusion and Calibrated Decoder Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mattia Segu, Marta Tintore Gazulla, Yongqin Xian, Luc Van Gool, Federico Tombari

**分类**: cs.CV

**发布日期**: 2025-10-16

**备注**: ICCV 2025

---

## 💡 一句话要点

**MOBIUS：通过多模态瓶颈融合与校准解码器剪枝实现Big-to-Mobile通用实例分割**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实例分割` `模型压缩` `移动设备` `多模态融合` `解码器剪枝` `不确定性校准` `瓶颈结构`

## 📋 核心要点

1. 现有实例分割模型计算成本高昂，难以在资源受限的边缘设备上部署，限制了其应用范围。
2. MOBIUS通过瓶颈像素解码器、语言引导的不确定性校准损失和统一训练策略，降低训练和推理需求。
3. 实验表明，MOBIUS在显著降低计算量的同时，保持了最先进的性能，并在移动设备上实现了高效分割。

## 📝 摘要（中文）

本文提出MOBIUS，一个面向通用实例分割的基础模型家族，旨在实现Pareto最优的缩放，以支持从高端加速器到移动硬件的部署。为了降低训练和推理需求，本文提出了：（i）用于高效多尺度和多模态融合的瓶颈像素解码器；（ii）用于自适应解码器剪枝的语言引导的不确定性校准损失；（iii）简化的统一训练策略。与以牺牲精度为代价来降低复杂性的高效基线不同，MOBIUS将像素和Transformer解码器的FLOPs分别降低高达55%和75%，同时在仅三分之一的训练迭代中保持了最先进的性能。MOBIUS为高性能计算平台和移动设备上的高效分割建立了一个新的基准。

## 🔬 方法详解

**问题定义**：现有实例分割模型，特别是基于Transformer的大型模型，虽然在精度上取得了显著进展，但其庞大的计算量和内存需求使其难以在移动设备等资源受限的平台上部署。现有的模型压缩方法通常以牺牲精度为代价来降低计算复杂度，无法在精度和效率之间取得平衡。

**核心思路**：MOBIUS的核心思路是通过设计高效的模块和训练策略，在不显著降低精度的前提下，大幅降低模型的计算量和内存需求，从而实现模型在不同硬件平台上的灵活部署。具体来说，通过多模态瓶颈融合减少特征维度，并通过语言引导的不确定性校准损失实现自适应的解码器剪枝。

**技术框架**：MOBIUS的整体框架包括以下几个主要模块：(1) Backbone网络：用于提取图像特征。(2) 瓶颈像素解码器：用于高效地融合多尺度和多模态特征，降低特征维度。(3) 分割头：用于预测实例分割结果。(4) 语言引导的不确定性校准模块：用于评估解码器的不确定性，并指导解码器的剪枝。整个训练过程采用统一的训练策略，简化了训练流程。

**关键创新**：MOBIUS的关键创新在于：(1) 瓶颈像素解码器：通过引入瓶颈结构，降低了特征维度，从而减少了计算量。(2) 语言引导的不确定性校准损失：利用语言信息来评估解码器的不确定性，并指导解码器的剪枝，从而实现了自适应的解码器压缩。与现有方法相比，MOBIUS能够在保持精度的前提下，更有效地降低计算量。

**关键设计**：(1) 瓶颈像素解码器：采用多层感知机（MLP）作为瓶颈结构，将高维特征映射到低维空间。(2) 语言引导的不确定性校准损失：利用预训练的语言模型来提取图像描述的语义信息，并将其用于评估解码器的不确定性。损失函数的设计旨在鼓励模型学习到更准确的分割结果，并降低对不确定区域的过度关注。(3) 统一训练策略：采用端到端的训练方式，简化了训练流程，并提高了模型的性能。

## 📊 实验亮点

MOBIUS在多个数据集上进行了实验，结果表明，与现有的高效实例分割模型相比，MOBIUS在显著降低计算量的同时，保持了最先进的性能。具体来说，MOBIUS将像素和Transformer解码器的FLOPs分别降低高达55%和75%，同时在仅三分之一的训练迭代中保持了相当甚至更好的精度。这表明MOBIUS在效率和精度之间取得了良好的平衡。

## 🎯 应用场景

MOBIUS具有广泛的应用前景，包括移动机器人、自动驾驶、增强现实和虚拟现实等领域。它能够使这些应用在资源受限的设备上实现高性能的实例分割，从而提高系统的智能化水平和用户体验。此外，MOBIUS还可以应用于医学图像分析、遥感图像处理等领域，为这些领域提供高效的图像分割解决方案。

## 📄 摘要（原文）

> Scaling up model size and training data has advanced foundation models for instance-level perception, achieving state-of-the-art in-domain and zero-shot performance across object detection and segmentation. However, their high computational cost limits adoption on resource-constrained platforms. We first examine the limitations of existing architectures in enabling efficient edge deployment without compromising performance. We then introduce MOBIUS, a family of foundation models for universal instance segmentation, designed for Pareto-optimal downscaling to support deployment across devices ranging from high-end accelerators to mobile hardware. To reduce training and inference demands, we propose: (i) a bottleneck pixel decoder for efficient multi-scale and multi-modal fusion, (ii) a language-guided uncertainty calibration loss for adaptive decoder pruning, and (iii) a streamlined, unified training strategy. Unlike efficient baselines that trade accuracy for reduced complexity, MOBIUS reduces pixel and transformer decoder FLOPs by up to 55% and 75%, respectively, while maintaining state-of-the-art performance in just a third of the training iterations. MOBIUS establishes a new benchmark for efficient segmentation on both high-performance computing platforms and mobile devices.

