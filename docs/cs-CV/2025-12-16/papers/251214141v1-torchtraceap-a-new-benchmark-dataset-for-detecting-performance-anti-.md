---
layout: default
title: TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models
---

# TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14141" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14141v1</a>
  <a href="https://arxiv.org/pdf/2512.14141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14141v1" onclick="toggleFavorite(this, '2512.14141v1', 'TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanning Chen, Keyu Man, Kevin Zhu, Chenguang Zhu, Haonan Li, Tongbo Luo, Xizhou Feng, Wei Sun, Sreen Tallam, Mohsen Imani, Partha Kanuparthy

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出TorchTraceAP基准数据集，用于检测计算机视觉模型中的性能反模式。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `性能反模式检测` `PyTorch跟踪` `大型语言模型` `计算机视觉模型优化` `基准数据集`

## 📋 核心要点

1. 现有方法难以在冗长的模型执行跟踪中自动定位性能反模式，阻碍了计算机视觉研究。
2. 提出一种迭代方法，先用轻量级ML模型检测反模式片段，再用LLM进行细粒度分类和反馈。
3. 实验表明，该方法显著优于无监督聚类和规则方法，并能有效弥补LLM的局限性。

## 📝 摘要（中文）

识别和解决机器学习（ML）模型中的性能反模式对于高效的训练和推理至关重要，但这通常需要系统基础设施、ML模型和内核开发方面的深厚专业知识。大型科技公司依靠专门的ML基础设施工程师来分析torch traces和基准测试，但这种资源密集型工作流程对于一般的计算机视觉研究人员来说在很大程度上是无法实现的。其中，在冗长的执行跟踪中精确定位有问题的跟踪片段仍然是最耗时的任务，并且很难用当前的ML模型（包括LLM）自动完成。本文提出了第一个专门用于评估和提高ML模型检测跟踪中反模式能力的基准数据集。我们的数据集包含来自多种硬件平台上收集的各种计算机视觉模型（分类、检测、分割和生成）的600多个PyTorch跟踪。我们还提出了一种新颖的迭代方法：一个轻量级ML模型首先检测具有反模式的跟踪片段，然后使用大型语言模型（LLM）进行细粒度分类和有针对性的反馈。实验结果表明，我们的方法在检测反模式区域方面明显优于无监督聚类和基于规则的统计技术。我们的方法还有效地弥补了LLM有限的上下文长度和推理效率。

## 🔬 方法详解

**问题定义**：论文旨在解决计算机视觉模型性能优化中，难以自动检测和定位PyTorch执行跟踪中的性能反模式的问题。现有方法，如无监督聚类和基于规则的统计技术，在处理复杂和冗长的跟踪数据时效果不佳，且大型语言模型（LLM）由于上下文长度限制和推理效率问题，也难以直接应用。

**核心思路**：论文的核心思路是将问题分解为两个阶段：首先使用轻量级的机器学习模型快速定位可能存在性能反模式的跟踪片段，然后利用大型语言模型（LLM）对这些片段进行更细粒度的分类和分析，并提供针对性的反馈。这种迭代方法旨在结合两者的优势，提高检测效率和准确性。

**技术框架**：整体框架包含两个主要阶段：1) 反模式片段检测：使用轻量级ML模型（具体模型类型未知）对PyTorch执行跟踪进行分析，识别出可能包含性能反模式的片段。2) 细粒度分类与反馈：将检测到的片段输入到大型语言模型（LLM）中，LLM对这些片段进行分类，识别具体的反模式类型，并提供优化建议。这两个阶段迭代进行，不断优化检测结果。

**关键创新**：该方法的主要创新在于将轻量级ML模型和大型语言模型（LLM）结合起来，形成一个迭代的检测流程。轻量级模型负责快速定位，LLM负责细粒度分析，从而克服了单一模型在处理复杂跟踪数据时的局限性。此外，构建了TorchTraceAP数据集，为该领域的研究提供了基准。

**关键设计**：论文中关于轻量级ML模型的具体架构、训练方式，以及LLM的使用方式（例如prompt设计、微调策略等）的细节未知。数据集的构建过程和规模（600多个PyTorch traces）是关键设计的一部分，但具体的数据增强、清洗等细节未知。

## 📊 实验亮点

实验结果表明，该方法在检测反模式区域方面明显优于无监督聚类和基于规则的统计技术。具体性能数据和提升幅度未知，但论文强调该方法能有效弥补LLM有限的上下文长度和推理效率，表明其在处理复杂跟踪数据方面具有优势。

## 🎯 应用场景

该研究成果可应用于计算机视觉模型的自动性能优化，帮助研究人员和工程师快速定位和解决模型中的性能瓶颈。通过自动化反模式检测，可以显著降低模型优化所需的人力成本，提高模型训练和推理的效率，加速计算机视觉算法的开发和部署。

## 📄 摘要（原文）

> Identifying and addressing performance anti-patterns in machine learning (ML) models is critical for efficient training and inference, but it typically demands deep expertise spanning system infrastructure, ML models and kernel development. While large tech companies rely on dedicated ML infrastructure engineers to analyze torch traces and benchmarks, such resource-intensive workflows are largely inaccessible to computer vision researchers in general. Among the challenges, pinpointing problematic trace segments within lengthy execution traces remains the most time-consuming task, and is difficult to automate with current ML models, including LLMs. In this work, we present the first benchmark dataset specifically designed to evaluate and improve ML models' ability to detect anti patterns in traces. Our dataset contains over 600 PyTorch traces from diverse computer vision models classification, detection, segmentation, and generation collected across multiple hardware platforms. We also propose a novel iterative approach: a lightweight ML model first detects trace segments with anti patterns, followed by a large language model (LLM) for fine grained classification and targeted feedback. Experimental results demonstrate that our method significantly outperforms unsupervised clustering and rule based statistical techniques for detecting anti pattern regions. Our method also effectively compensates LLM's limited context length and reasoning inefficiencies.

