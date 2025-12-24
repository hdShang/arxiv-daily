---
layout: default
title: Textual Steering Vectors Can Improve Visual Understanding in Multimodal Large Language Models
---

# Textual Steering Vectors Can Improve Visual Understanding in Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14071" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14071v1</a>
  <a href="https://arxiv.org/pdf/2505.14071.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14071v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14071v1', 'Textual Steering Vectors Can Improve Visual Understanding in Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Woody Haosheng Gan, Deqing Fu, Julian Asilis, Ollie Liu, Dani Yogatama, Vatsal Sharan, Robin Jia, Willie Neiswanger

**分类**: cs.LG, cs.CL, cs.CV

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出文本引导向量以提升多模态大语言模型的视觉理解能力**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `文本引导` `视觉理解` `稀疏自编码器` `均值漂移` `线性探测` `模型引导` `计算机视觉`

## 📋 核心要点

1. 现有的多模态大语言模型缺乏有效的引导技术，导致其在视觉理解任务中的表现不佳。
2. 本文提出通过文本导出的向量来引导多模态大语言模型，利用稀疏自编码器等技术实现。
3. 实验结果表明，文本引导显著提升了多模态模型的准确性，尤其在空间关系和计数任务上表现突出。

## 📝 摘要（中文）

引导方法已成为有效的工具，用于在不修改大语言模型参数的情况下引导其行为。然而，现有的多模态大语言模型（MLLMs）尚未充分利用这些技术。本文探讨了如何通过稀疏自编码器、均值漂移和线性探测等方法，利用文本导出的向量来引导MLLMs。研究发现，文本导向的引导在不同的MLLM架构和视觉任务中均能显著提升多模态准确性，特别是在CV-Bench上，均值漂移在空间关系准确性上提升了7.3%，计数准确性提升了3.3%。这些结果表明，文本引导向量是一种强大且高效的机制，能够在最小的数据收集和计算开销下增强MLLM的基础能力。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在视觉理解任务中缺乏有效引导技术的问题。现有方法未能充分利用文本信息，导致模型性能受限。

**核心思路**：通过从文本基础的大语言模型中提取向量，结合稀疏自编码器、均值漂移和线性探测等方法，引导多模态模型的行为，以提升其视觉理解能力。

**技术框架**：整体架构包括三个主要模块：首先是文本向量的提取，其次是通过均值漂移和线性探测进行引导，最后是将引导结果应用于多模态模型的训练和评估。

**关键创新**：最重要的创新在于提出了文本导向的引导向量，显著提升了多模态模型的准确性，尤其是在空间关系和计数任务上，超越了传统的提示方法。

**关键设计**：在设计中，采用了稀疏自编码器来提取文本特征，均值漂移用于优化空间关系的准确性，线性探测则用于评估引导效果，确保模型在不同数据集上的强泛化能力。

## 📊 实验亮点

实验结果显示，均值漂移方法在CV-Bench数据集上提升了空间关系准确性7.3%，计数准确性提升3.3%。这些结果不仅超越了传统的提示方法，还展现了在不同分布数据集上的强泛化能力，证明了文本引导向量的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理和人机交互等。通过提升多模态大语言模型的视觉理解能力，可以在自动驾驶、智能监控和虚拟助手等实际场景中发挥重要作用，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Steering methods have emerged as effective and targeted tools for guiding large language models' (LLMs) behavior without modifying their parameters. Multimodal large language models (MLLMs), however, do not currently enjoy the same suite of techniques, due in part to their recency and architectural diversity. Inspired by this gap, we investigate whether MLLMs can be steered using vectors derived from their text-only LLM backbone, via sparse autoencoders (SAEs), mean shift, and linear probing. We find that text-derived steering consistently enhances multimodal accuracy across diverse MLLM architectures and visual tasks. In particular, mean shift boosts spatial relationship accuracy on CV-Bench by up to +7.3% and counting accuracy by up to +3.3%, outperforming prompting and exhibiting strong generalization to out-of-distribution datasets. These results highlight textual steering vectors as a powerful, efficient mechanism for enhancing grounding in MLLMs with minimal additional data collection and computational overhead.

