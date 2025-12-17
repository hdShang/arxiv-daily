---
layout: default
title: TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models
---

# TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models

**arXiv**: [2512.14141v1](https://arxiv.org/abs/2512.14141) | [PDF](https://arxiv.org/pdf/2512.14141.pdf)

**作者**: Hanning Chen, Keyu Man, Kevin Zhu, Chenguang Zhu, Haonan Li, Tongbo Luo, Xizhou Feng, Wei Sun, Sreen Tallam, Mohsen Imani, Partha Kanuparthy

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出TorchTraceAP基准数据集与迭代方法，以解决计算机视觉模型中性能反模式检测的自动化难题。**

**关键词**: `性能反模式检测` `PyTorch跟踪分析` `基准数据集` `迭代机器学习方法` `计算机视觉模型优化` `大型语言模型应用` `自动化调试工具` `ML基础设施`

## 📋 核心要点

1. 现有方法依赖专家手动分析跟踪，耗时且难以自动化，尤其对计算机视觉研究人员资源不足。
2. 提出迭代方法：轻量级ML模型初步检测反模式段，LLM进行细粒度分类和反馈，结合两者优势。
3. 实验显示，该方法在检测反模式区域上显著优于无监督聚类和基于规则技术，并提升LLM效率。

## 📝 摘要（中文）

识别和解决机器学习模型中的性能反模式对于高效训练和推理至关重要，但这通常需要跨越系统基础设施、ML模型和内核开发的深厚专业知识。虽然大型科技公司依赖专门的ML基础设施工程师来分析torch跟踪和基准测试，但这种资源密集型工作流程对大多数计算机视觉研究人员来说难以实现。在众多挑战中，在冗长的执行跟踪中精确定位有问题的跟踪段仍然是最耗时的任务，并且难以用当前的ML模型（包括LLM）实现自动化。在这项工作中，我们提出了第一个专门设计用于评估和改进ML模型检测跟踪中反模式能力的基准数据集。我们的数据集包含超过600个来自不同计算机视觉模型（分类、检测、分割和生成）的PyTorch跟踪，这些跟踪是在多个硬件平台上收集的。我们还提出了一种新颖的迭代方法：首先使用轻量级ML模型检测具有反模式的跟踪段，然后使用大型语言模型进行细粒度分类和针对性反馈。实验结果表明，我们的方法在检测反模式区域方面显著优于无监督聚类和基于规则的统计技术。我们的方法还有效地弥补了LLM有限的上下文长度和推理效率低下的问题。

## 🔬 方法详解

论文提出一种迭代框架，整体分为两个阶段：首先，使用轻量级ML模型（如小型神经网络）对PyTorch跟踪进行初步扫描，快速识别出可能包含性能反模式的跟踪段；然后，将这些候选段输入大型语言模型进行细粒度分类和生成针对性反馈。关键技术创新点在于结合了轻量级模型的高效检测能力和LLM的复杂推理能力，通过迭代方式优化检测精度。与现有方法的主要区别在于，它避免了纯规则或统计方法的局限性，同时解决了LLM上下文长度限制和推理效率低下的问题，实现了更自动化和精准的反模式检测。

## 📊 实验亮点

实验结果表明，提出的迭代方法在检测反模式区域方面显著优于无监督聚类和基于规则的统计技术，具体性能提升未量化但强调“显著”。此外，该方法有效补偿了LLM的上下文长度限制和推理效率问题，展示了在自动化检测任务中的实用优势。

## 🎯 应用场景

该研究可应用于计算机视觉模型的性能优化领域，帮助研究人员和工程师自动化检测训练和推理中的效率瓶颈，如内存泄漏、计算冗余等反模式。潜在价值包括降低对专家依赖、加速模型调试过程，并提升ML基础设施的智能化水平，适用于学术研究和工业部署场景。

## 📄 摘要（原文）

> Identifying and addressing performance anti-patterns in machine learning (ML) models is critical for efficient training and inference, but it typically demands deep expertise spanning system infrastructure, ML models and kernel development. While large tech companies rely on dedicated ML infrastructure engineers to analyze torch traces and benchmarks, such resource-intensive workflows are largely inaccessible to computer vision researchers in general. Among the challenges, pinpointing problematic trace segments within lengthy execution traces remains the most time-consuming task, and is difficult to automate with current ML models, including LLMs. In this work, we present the first benchmark dataset specifically designed to evaluate and improve ML models' ability to detect anti patterns in traces. Our dataset contains over 600 PyTorch traces from diverse computer vision models classification, detection, segmentation, and generation collected across multiple hardware platforms. We also propose a novel iterative approach: a lightweight ML model first detects trace segments with anti patterns, followed by a large language model (LLM) for fine grained classification and targeted feedback. Experimental results demonstrate that our method significantly outperforms unsupervised clustering and rule based statistical techniques for detecting anti pattern regions. Our method also effectively compensates LLM's limited context length and reasoning inefficiencies.

