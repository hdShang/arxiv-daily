---
layout: default
title: "ChartReasoner: Code-Driven Modality Bridging for Long-Chain Reasoning in Chart Question Answering"
---

# ChartReasoner: Code-Driven Modality Bridging for Long-Chain Reasoning in Chart Question Answering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10116" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10116v1</a>
  <a href="https://arxiv.org/pdf/2506.10116.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10116v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10116v1', 'ChartReasoner: Code-Driven Modality Bridging for Long-Chain Reasoning in Chart Question Answering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Caijun Jia, Nan Xu, Jingxuan Wei, Qingli Wang, Lei Wang, Bihui Yu, Junnan Zhu

**分类**: cs.CL

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出ChartReasoner以解决图表问答中的视觉推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图表问答` `视觉推理` `多模态推理` `长链推理` `ECharts` `数据合成` `代码驱动` `强化学习`

## 📋 核心要点

1. 现有的多模态推理方法在处理图表问答时，常常通过图像到文本的转换，导致重要的结构和语义信息丢失。
2. 本文提出ChartReasoner，一个两阶段框架，通过将图表图像转换为结构化的ECharts代码来实现精确推理。
3. 实验结果显示，ChartReasoner在多个公共基准测试中表现优异，使用更少参数的同时接近最先进的专有系统性能。

## 📝 摘要（中文）

近年来，大型语言模型在长链推理方面展现了显著的能力，但如何将这一能力扩展到视觉推理任务仍然是一个开放性挑战。现有的多模态推理方法通过多次图像到文本的转换来处理视觉推理任务，常常会丢失嵌入在可视化中的重要结构和语义信息，尤其是在需要大量视觉细节的图表问答任务中。为了解决这一问题，本文提出了ChartReasoner，一个基于代码驱动的两阶段框架，旨在实现对图表的精确和可解释的推理。我们首先训练一个高保真模型，将多样的图表图像转换为结构化的ECharts代码，尽可能无损地保留布局和数据语义。然后，我们设计了一个通用的图表推理数据合成管道，利用该预训练的传输模型自动生成图表推理轨迹，并使用代码验证器过滤低质量样本。最后，我们通过监督微调和强化学习在合成的图表推理数据集上训练最终的多模态模型，实验结果表明，ChartReasoner在保留图表原始细节的同时，使用更少的参数与最先进的开源模型表现相当，接近于GPT-4o等专有系统的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决图表问答中的视觉推理问题，现有方法通过图像到文本的转换导致重要信息丢失，影响推理效果。

**核心思路**：提出ChartReasoner框架，通过将图表图像转换为结构化的ECharts代码，保留图表的布局和数据语义，从而实现更精确的推理。

**技术框架**：框架分为两个主要阶段：第一阶段训练高保真模型进行图表图像到ECharts代码的转换，第二阶段设计数据合成管道生成推理轨迹并进行质量过滤。

**关键创新**：最重要的创新在于通过代码驱动的方法实现图表推理，避免了传统方法中信息丢失的问题，提升了推理的准确性和可解释性。

**关键设计**：在模型训练中，采用了监督微调和强化学习的结合，设计了代码验证器以确保生成样本的质量，同时优化了模型参数以提高推理效率。

## 📊 实验亮点

在四个公共基准测试中，ChartReasoner的实验结果显示出优越的性能，能够在保留图表细节的同时，使用更少的参数，接近于GPT-4o等专有系统的表现，展示了显著的提升。

## 🎯 应用场景

ChartReasoner的研究成果可广泛应用于数据分析、商业智能、教育等领域，帮助用户更好地理解和分析图表数据。未来，该框架有潜力推动更多复杂视觉推理任务的发展，提升人机交互的智能化水平。

## 📄 摘要（原文）

> Recently, large language models have shown remarkable reasoning capabilities through long-chain reasoning before responding. However, how to extend this capability to visual reasoning tasks remains an open challenge. Existing multimodal reasoning approaches transfer such visual reasoning task into textual reasoning task via several image-to-text conversions, which often lose critical structural and semantic information embedded in visualizations, especially for tasks like chart question answering that require a large amount of visual details. To bridge this gap, we propose ChartReasoner, a code-driven novel two-stage framework designed to enable precise, interpretable reasoning over charts. We first train a high-fidelity model to convert diverse chart images into structured ECharts codes, preserving both layout and data semantics as lossless as possible. Then, we design a general chart reasoning data synthesis pipeline, which leverages this pretrained transport model to automatically and scalably generate chart reasoning trajectories and utilizes a code validator to filter out low-quality samples. Finally, we train the final multimodal model using a combination of supervised fine-tuning and reinforcement learning on our synthesized chart reasoning dataset and experimental results on four public benchmarks clearly demonstrate the effectiveness of our proposed ChartReasoner. It can preserve the original details of the charts as much as possible and perform comparably with state-of-the-art open-source models while using fewer parameters, approaching the performance of proprietary systems like GPT-4o in out-of-domain settings.

