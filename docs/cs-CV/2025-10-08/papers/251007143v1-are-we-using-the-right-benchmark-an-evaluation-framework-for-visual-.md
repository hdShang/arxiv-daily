---
layout: default
title: Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods
---

# Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07143" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07143v1</a>
  <a href="https://arxiv.org/pdf/2510.07143.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07143v1" onclick="toggleFavorite(this, '2510.07143v1', 'Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenfei Liao, Wensong Wang, Zichen Wen, Xu Zheng, Yiyu Wang, Haocong He, Yuanhuiyi Lyu, Lutao Jiang, Xin Zou, Yuqian Fu, Bin Ren, Linfeng Zhang, Xuming Hu

**分类**: cs.CV

**发布日期**: 2025-10-08

**🔗 代码/项目**: [GITHUB](https://github.com/Chenfei-Liao/VTC-Bench)

---

## 💡 一句话要点

**提出VTC-Bench，用于更准确评估多模态大模型中视觉Token压缩方法的性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉Token压缩` `多模态大语言模型` `评估框架` `基准测试` `数据过滤` `图像降采样` `性能评估`

## 📋 核心要点

1. 现有视觉Token压缩方法评估依赖的基准测试，与压缩任务本身存在不匹配，导致评估结果不准确。
2. 论文提出VTC-Bench评估框架，通过数据过滤机制降低基准测试中的噪声，从而实现更公平的评估。
3. 实验表明，简单的图像降采样在现有基准上表现优于许多先进的压缩方法，突显了基准测试的局限性。

## 📝 摘要（中文）

为了加速多模态大语言模型（MLLM）的推理，目前的研究主要集中在视觉token压缩上。通常，这些方法的有效性是通过测量在既定基准上的精度下降来评估的，即比较压缩前后模型的性能。然而，这些基准最初旨在评估MLLM的感知和推理能力，而不是评估压缩技术。因此，直接将它们应用于视觉token压缩会引入任务不匹配的问题。令人惊讶的是，我们的研究表明，简单的图像降采样在多个广泛使用的基准测试中始终优于许多先进的压缩方法。通过大量的实验，我们得出以下观察结果：（i）当前的基准测试对于视觉token压缩任务来说是嘈杂的。（ii）降采样可以作为数据过滤器来评估视觉token压缩任务中样本的难度。基于这些发现，我们引入了VTC-Bench，这是一个评估框架，它结合了数据过滤机制来消除现有基准测试中的噪声，从而能够更公平、更准确地评估视觉token压缩方法。所有数据和代码均可在https://github.com/Chenfei-Liao/VTC-Bench获取。

## 🔬 方法详解

**问题定义**：现有视觉Token压缩方法的评估主要依赖于现有的MLLM基准测试。这些基准测试最初设计用于评估MLLM的感知和推理能力，而非专门用于评估压缩算法。因此，直接使用这些基准测试来评估视觉Token压缩方法会导致任务不匹配，使得评估结果不够准确，无法真实反映压缩算法的性能。现有方法的痛点在于无法区分压缩算法带来的性能下降和基准测试本身固有的噪声。

**核心思路**：论文的核心思路是通过引入数据过滤机制来降低现有基准测试中的噪声。具体来说，论文发现简单的图像降采样可以作为一种有效的数据过滤器，能够区分不同样本的难度。通过分析降采样后的性能变化，可以识别出对压缩算法评估具有干扰性的噪声样本，从而提高评估的准确性。

**技术框架**：VTC-Bench评估框架主要包含以下几个阶段：1) 数据集选择：选择现有的MLLM基准测试数据集。2) 数据过滤：使用图像降采样作为数据过滤器，对数据集中的图像进行处理。3) 性能评估：在原始数据集和过滤后的数据集上，分别评估不同的视觉Token压缩方法的性能。4) 结果分析：比较不同压缩方法在不同数据集上的性能表现，分析数据过滤对评估结果的影响。

**关键创新**：VTC-Bench的关键创新在于引入了数据过滤机制，通过图像降采样来降低现有基准测试中的噪声。这种方法能够更准确地评估视觉Token压缩方法的性能，避免了任务不匹配带来的评估偏差。与现有方法相比，VTC-Bench能够提供更可靠、更公平的评估结果。

**关键设计**：VTC-Bench的关键设计包括：1) 降采样策略的选择：论文可能探索了不同的降采样方法和参数设置，以找到最佳的数据过滤效果。2) 性能评估指标的选择：论文可能使用了多种性能评估指标，如精度、召回率等，来全面评估压缩方法的性能。3) 数据集划分策略：论文可能将数据集划分为不同的难度级别，以便更细致地分析压缩方法在不同难度样本上的表现。

## 📊 实验亮点

实验结果表明，简单的图像降采样在多个广泛使用的基准测试中始终优于许多先进的压缩方法，这突显了现有基准测试的局限性。VTC-Bench通过数据过滤机制，能够更准确地评估视觉Token压缩方法的性能，并为未来的研究提供更可靠的评估平台。具体的性能提升数据未知，但论文强调了评估框架的改进。

## 🎯 应用场景

VTC-Bench可用于评估和比较不同的视觉Token压缩方法，帮助研究人员和工程师选择最适合特定应用场景的压缩算法。该框架能够推动多模态大语言模型在资源受限设备上的部署，例如移动设备和嵌入式系统，从而扩展MLLM的应用范围。此外，VTC-Bench还可以促进视觉Token压缩算法的进一步研究和发展。

## 📄 摘要（原文）

> Recent endeavors to accelerate inference in Multimodal Large Language Models (MLLMs) have primarily focused on visual token compression. The effectiveness of these methods is typically assessed by measuring the accuracy drop on established benchmarks, comparing model performance before and after compression. However, these benchmarks are originally designed to assess the perception and reasoning capabilities of MLLMs, rather than to evaluate compression techniques. As a result, directly applying them to visual token compression introduces a task mismatch. Strikingly, our investigation reveals that simple image downsampling consistently outperforms many advanced compression methods across multiple widely used benchmarks. Through extensive experiments, we make the following observations: (i) Current benchmarks are noisy for the visual token compression task. (ii) Down-sampling is able to serve as a data filter to evaluate the difficulty of samples in the visual token compression task. Motivated by these findings, we introduce VTC-Bench, an evaluation framework that incorporates a data filtering mechanism to denoise existing benchmarks, thereby enabling fairer and more accurate assessment of visual token compression methods. All data and code are available at https://github.com/Chenfei-Liao/VTC-Bench.

