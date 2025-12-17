---
layout: default
title: TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models
---

# TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14141" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14141</a>
  <a href="https://arxiv.org/pdf/2512.14141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14141" onclick="toggleFavorite(this, '2512.14141', 'TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanning Chen, Keyu Man, Kevin Zhu, Chenguang Zhu, Haonan Li, Tongbo Luo, Xizhou Feng, Wei Sun, Sreen Tallam, Mohsen Imani, Partha Kanuparthy

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出TorchTraceAP基准数据集，用于检测计算机视觉模型中的性能反模式。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `性能反模式检测` `PyTorch traces` `机器学习模型优化` `大型语言模型` `基准数据集`

## 📋 核心要点

1. 现有方法难以在冗长的执行traces中精确定位性能反模式，自动化程度低，依赖人工专家。
2. 提出一种迭代方法，首先使用轻量级ML模型检测trace片段，然后利用LLM进行细粒度分类和反馈。
3. 实验结果表明，该方法显著优于无监督聚类和基于规则的统计技术，并能有效弥补LLM的不足。

## 📝 摘要（中文）

识别和解决机器学习(ML)模型中的性能反模式对于高效的训练和推理至关重要，但这通常需要系统基础设施、ML模型和内核开发方面的深厚专业知识。大型科技公司依靠专门的ML基础设施工程师来分析torch traces和基准，但这种资源密集型工作流程对于一般的计算机视觉研究人员来说在很大程度上是无法实现的。其中，在冗长的执行traces中精确定位有问题的trace片段仍然是最耗时的任务，并且很难用当前的ML模型（包括LLM）自动完成。本文提出了第一个专门用于评估和提高ML模型检测traces中反模式能力的基准数据集。该数据集包含来自多种硬件平台上收集的各种计算机视觉模型（分类、检测、分割和生成）的600多个PyTorch traces。此外，还提出了一种新颖的迭代方法：一个轻量级的ML模型首先检测具有反模式的trace片段，然后使用大型语言模型(LLM)进行细粒度分类和有针对性的反馈。实验结果表明，该方法在检测反模式区域方面明显优于无监督聚类和基于规则的统计技术。该方法还有效地弥补了LLM有限的上下文长度和推理效率。

## 🔬 方法详解

**问题定义**：论文旨在解决计算机视觉模型性能优化中，难以自动检测PyTorch traces中性能反模式的问题。现有方法依赖人工分析，耗时且需要专家知识，而现有的ML模型，包括LLM，难以处理长序列的trace数据，且推理效率不高。

**核心思路**：论文的核心思路是将问题分解为两个阶段：首先使用轻量级ML模型快速定位可能存在性能反模式的trace片段，然后利用LLM对这些片段进行细粒度分类和提供反馈。这种迭代方法旨在结合两者的优势，降低对LLM上下文长度的要求，并提高整体效率。

**技术框架**：整体框架包含两个主要阶段：1) 轻量级ML模型（例如，一个简单的分类器或回归器）对PyTorch trace进行扫描，识别出可能包含性能反模式的片段。这个模型可以基于统计特征、规则或简单的机器学习算法。2) 将识别出的片段输入到LLM中，LLM对这些片段进行更深入的分析，识别具体的性能反模式类型，并提供优化建议。这两个阶段可以迭代进行，以提高检测精度。

**关键创新**：关键创新在于将轻量级ML模型和LLM结合起来，形成一个迭代的检测框架。这种方法既利用了轻量级模型的高效性，又利用了LLM的强大推理能力。此外，构建的TorchTraceAP数据集是首个专门用于评估和改进ML模型检测trace中反模式能力的基准数据集。

**关键设计**：轻量级ML模型的设计需要考虑计算效率和检测准确率之间的平衡。可以使用简单的统计特征（例如，执行时间、内存占用等）作为输入，并采用浅层神经网络或决策树等模型。LLM的选择需要考虑其推理能力和上下文长度的限制。可以通过prompt工程来指导LLM的分析过程，并提供相关的背景知识和约束条件。迭代次数可以根据实际情况进行调整，以达到最佳的检测效果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14141/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14141/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14141/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文构建了包含600多个PyTorch traces的TorchTraceAP数据集，并验证了所提出的迭代方法在检测性能反模式区域方面的有效性。实验结果表明，该方法显著优于无监督聚类和基于规则的统计技术，并且能够有效弥补LLM的上下文长度限制和推理效率问题。具体的性能提升数据未知，但定性结果表明该方法具有显著优势。

## 🎯 应用场景

该研究成果可应用于计算机视觉模型的自动性能优化。通过自动检测和诊断性能瓶颈，可以帮助开发者更高效地训练和部署模型，降低计算成本，提高模型在各种硬件平台上的运行效率。该方法还有助于降低性能优化的门槛，使更多的研究人员和工程师能够参与到模型优化工作中。

## 📄 摘要（原文）

> Identifying and addressing performance anti-patterns in machine learning (ML) models is critical for efficient training and inference, but it typically demands deep expertise spanning system infrastructure, ML models and kernel development. While large tech companies rely on dedicated ML infrastructure engineers to analyze torch traces and benchmarks, such resource-intensive workflows are largely inaccessible to computer vision researchers in general. Among the challenges, pinpointing problematic trace segments within lengthy execution traces remains the most time-consuming task, and is difficult to automate with current ML models, including LLMs. In this work, we present the first benchmark dataset specifically designed to evaluate and improve ML models' ability to detect anti patterns in traces. Our dataset contains over 600 PyTorch traces from diverse computer vision models classification, detection, segmentation, and generation collected across multiple hardware platforms. We also propose a novel iterative approach: a lightweight ML model first detects trace segments with anti patterns, followed by a large language model (LLM) for fine grained classification and targeted feedback. Experimental results demonstrate that our method significantly outperforms unsupervised clustering and rule based statistical techniques for detecting anti pattern regions. Our method also effectively compensates LLM's limited context length and reasoning inefficiencies.

