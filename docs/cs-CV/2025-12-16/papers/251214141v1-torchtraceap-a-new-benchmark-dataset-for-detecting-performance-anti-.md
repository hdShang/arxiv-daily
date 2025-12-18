---
layout: default
title: TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models
---

# TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14141" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14141v1</a>
  <a href="https://arxiv.org/pdf/2512.14141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14141v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14141v1', 'TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanning Chen, Keyu Man, Kevin Zhu, Chenguang Zhu, Haonan Li, Tongbo Luo, Xizhou Feng, Wei Sun, Sreen Tallam, Mohsen Imani, Partha Kanuparthy

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出TorchTraceAP基准数据集，用于检测计算机视觉模型中的性能反模式。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `性能反模式检测` `PyTorch traces` `计算机视觉模型` `大型语言模型` `基准数据集`

## 📋 核心要点

1. 现有方法难以在冗长的执行traces中精确定位性能反模式，自动化程度低，依赖人工分析。
2. 提出一种迭代方法，先用轻量级ML模型检测trace片段，再用LLM进行细粒度分类和反馈。
3. 实验表明，该方法显著优于无监督聚类和基于规则的统计技术，并能有效弥补LLM的不足。

## 📝 摘要（中文）

识别和解决机器学习（ML）模型中的性能反模式对于高效的训练和推理至关重要，但这通常需要跨越系统基础设施、ML模型和内核开发的深厚专业知识。大型科技公司依靠专门的ML基础设施工程师来分析torch traces和基准测试，但这种资源密集型工作流程对于一般的计算机视觉研究人员来说在很大程度上是无法实现的。其中，在冗长的执行traces中精确定位有问题的trace片段仍然是最耗时的任务，并且很难用当前的ML模型（包括LLM）自动完成。本文提出了第一个专门用于评估和提高ML模型检测traces中反模式能力的基准数据集。该数据集包含来自多个硬件平台上收集的各种计算机视觉模型（分类、检测、分割和生成）的600多个PyTorch traces。我们还提出了一种新颖的迭代方法：一个轻量级的ML模型首先检测具有反模式的trace片段，然后使用大型语言模型（LLM）进行细粒度分类和有针对性的反馈。实验结果表明，我们的方法在检测反模式区域方面明显优于无监督聚类和基于规则的统计技术。我们的方法还有效地弥补了LLM有限的上下文长度和推理效率。

## 🔬 方法详解

**问题定义**：论文旨在解决计算机视觉模型性能分析中，难以自动检测和定位PyTorch traces中的性能反模式的问题。现有方法主要依赖人工分析，耗时且需要专业知识，而现有的ML模型，包括LLM，难以处理长序列的trace数据，且推理效率较低。

**核心思路**：论文的核心思路是将问题分解为两个阶段：首先使用轻量级的ML模型快速检测出可能存在性能反模式的trace片段，然后利用LLM对这些片段进行细粒度的分类和分析，并给出针对性的反馈。这种迭代的方法旨在结合两者的优势，提高检测效率和准确性。

**技术框架**：整体框架包含两个主要阶段：1) **反模式区域检测**：使用轻量级ML模型（具体模型未知）对PyTorch trace进行分析，识别出可能包含性能反模式的trace片段。2) **细粒度分类与反馈**：将检测到的trace片段输入到LLM中，LLM对这些片段进行分类，识别出具体的性能反模式类型，并给出相应的优化建议。

**关键创新**：该方法的主要创新在于将轻量级ML模型和LLM结合起来，用于检测和分析PyTorch traces中的性能反模式。轻量级模型负责快速定位，LLM负责细粒度分析，从而提高了整体的效率和准确性。此外，该方法还提出了一种迭代的流程，可以不断优化模型的性能。

**关键设计**：论文中提到使用轻量级ML模型进行初步检测，但未明确指出具体模型结构和参数设置。LLM的使用旨在弥补上下文长度和推理效率的不足，但具体如何弥补，例如prompt工程的设计，论文中没有详细说明。损失函数和网络结构等技术细节也未在摘要中提及。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14141v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14141v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14141v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在检测反模式区域方面明显优于无监督聚类和基于规则的统计技术。具体性能数据和提升幅度未在摘要中给出，但强调了该方法在效率和准确性方面的优势，以及对LLM局限性的有效补偿。

## 🎯 应用场景

该研究成果可应用于计算机视觉模型的性能优化，帮助研究人员和工程师快速定位和解决模型中的性能瓶颈，提高模型的训练和推理效率。此外，该数据集可以促进相关领域的研究，推动自动化性能分析工具的发展，降低模型优化的门槛。

## 📄 摘要（原文）

> Identifying and addressing performance anti-patterns in machine learning (ML) models is critical for efficient training and inference, but it typically demands deep expertise spanning system infrastructure, ML models and kernel development. While large tech companies rely on dedicated ML infrastructure engineers to analyze torch traces and benchmarks, such resource-intensive workflows are largely inaccessible to computer vision researchers in general. Among the challenges, pinpointing problematic trace segments within lengthy execution traces remains the most time-consuming task, and is difficult to automate with current ML models, including LLMs. In this work, we present the first benchmark dataset specifically designed to evaluate and improve ML models' ability to detect anti patterns in traces. Our dataset contains over 600 PyTorch traces from diverse computer vision models classification, detection, segmentation, and generation collected across multiple hardware platforms. We also propose a novel iterative approach: a lightweight ML model first detects trace segments with anti patterns, followed by a large language model (LLM) for fine grained classification and targeted feedback. Experimental results demonstrate that our method significantly outperforms unsupervised clustering and rule based statistical techniques for detecting anti pattern regions. Our method also effectively compensates LLM's limited context length and reasoning inefficiencies.

