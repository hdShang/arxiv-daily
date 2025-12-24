---
layout: default
title: "L-SWAG: Layer-Sample Wise Activation with Gradients information for Zero-Shot NAS on Vision Transformers"
---

# L-SWAG: Layer-Sample Wise Activation with Gradients information for Zero-Shot NAS on Vision Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07300" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07300v1</a>
  <a href="https://arxiv.org/pdf/2505.07300.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07300v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07300v1', 'L-SWAG: Layer-Sample Wise Activation with Gradients information for Zero-Shot NAS on Vision Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sofia Casarin, Sergio Escalera, Oswald Lanz

**分类**: cs.CV

**发布日期**: 2025-05-12

**备注**: accepted at CVPR 2025

---

## 💡 一句话要点

**提出L-SWAG以解决零成本神经架构搜索在视觉变换器中的应用问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零成本神经架构搜索` `视觉变换器` `L-SWAG` `LIBRA-NAS` `深度学习` `自动化模型设计` `计算机视觉`

## 📋 核心要点

1. 现有的零成本神经架构搜索方法主要局限于卷积网络，缺乏对视觉变换器的有效支持。
2. 本文提出L-SWAG度量，能够同时表征卷积和变换器架构，扩展了ZC-NAS的适用范围。
3. 通过LIBRA-NAS方法，结合不同代理的信息，显著提升了NAS的性能，在ImageNet1k上实现了17.0%的测试误差。

## 📝 摘要（中文）

训练无关的神经架构搜索（NAS）有效识别高性能神经网络，利用零成本（ZC）代理实现时间效率和可解释性。尽管该领域迅速发展，当前的最先进ZC代理通常局限于成熟的卷积搜索空间。本文将ZC代理的适用性扩展到视觉变换器（ViTs），提出了一种新的基准，使用Autoformer搜索空间在六个不同任务上进行评估，并提出了一种新颖的通用度量L-SWAG，能够表征卷积和变换器架构。此外，本文还引入LIBRA-NAS方法，战略性地组合代理以最佳表示特定基准，最终在ImageNet1k上以0.1 GPU天的时间实现了17.0%的测试误差，超越了进化和基于梯度的NAS技术。

## 🔬 方法详解

**问题定义**：本文旨在解决当前零成本神经架构搜索（ZC-NAS）在视觉变换器（ViTs）应用中的局限性，现有方法多集中于卷积网络，缺乏对新兴架构的支持。

**核心思路**：提出Layer-Sample Wise Activation with Gradients information（L-SWAG）作为一种新颖的度量，能够有效表征不同架构的特性，并引入LIBRA-NAS方法，通过组合不同的ZC代理来优化架构选择。

**技术框架**：整体架构包括两个主要模块：L-SWAG度量模块用于评估架构性能，LIBRA-NAS模块用于整合和优化不同代理的信息，以便在特定基准上选择最佳架构。

**关键创新**：L-SWAG度量的提出是本文的核心创新，它能够同时适用于卷积和变换器架构，填补了现有ZC-NAS方法的空白。LIBRA-NAS方法则通过智能组合不同代理的信息，提升了架构搜索的效率和效果。

**关键设计**：在设计中，L-SWAG度量考虑了层级和样本的激活信息，结合梯度信息进行评估；LIBRA-NAS则通过低信息增益和偏差重对齐策略，优化了代理组合的选择过程。具体的参数设置和损失函数设计在实验部分进行了详细描述。

## 📊 实验亮点

在实验中，LIBRA-NAS方法在ImageNet1k数据集上实现了17.0%的测试误差，且仅需0.1 GPU天的计算时间，显著优于传统的进化和基于梯度的NAS技术。这一结果展示了新方法在效率和性能上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉中的自动化模型设计，尤其是在需要快速迭代和高效性能的场景，如图像分类、目标检测和图像分割等。通过优化架构搜索过程，能够为实际应用提供更高效的解决方案，推动深度学习技术的进一步发展。

## 📄 摘要（原文）

> Training-free Neural Architecture Search (NAS) efficiently identifies high-performing neural networks using zero-cost (ZC) proxies. Unlike multi-shot and one-shot NAS approaches, ZC-NAS is both (i) time-efficient, eliminating the need for model training, and (ii) interpretable, with proxy designs often theoretically grounded. Despite rapid developments in the field, current SOTA ZC proxies are typically constrained to well-established convolutional search spaces. With the rise of Large Language Models shaping the future of deep learning, this work extends ZC proxy applicability to Vision Transformers (ViTs). We present a new benchmark using the Autoformer search space evaluated on 6 distinct tasks and propose Layer-Sample Wise Activation with Gradients information (L-SWAG), a novel, generalizable metric that characterizes both convolutional and transformer architectures across 14 tasks. Additionally, previous works highlighted how different proxies contain complementary information, motivating the need for a ML model to identify useful combinations. To further enhance ZC-NAS, we therefore introduce LIBRA-NAS (Low Information gain and Bias Re-Alignment), a method that strategically combines proxies to best represent a specific benchmark. Integrated into the NAS search, LIBRA-NAS outperforms evolution and gradient-based NAS techniques by identifying an architecture with a 17.0% test error on ImageNet1k in just 0.1 GPU days.

