---
layout: default
title: "OIG-Bench: A Multi-Agent Annotated Benchmark for Multimodal One-Image Guides Understanding"
---

# OIG-Bench: A Multi-Agent Annotated Benchmark for Multimodal One-Image Guides Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00069" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00069v1</a>
  <a href="https://arxiv.org/pdf/2510.00069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00069v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00069v1', 'OIG-Bench: A Multi-Agent Annotated Benchmark for Multimodal One-Image Guides Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiancong Xie, Wenjin Wang, Zhuomeng Zhang, Zihan Liu, Qi Liu, Ke Feng, Zixun Sun, Yuedong Yang

**分类**: cs.CV

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/XiejcSYSU/OIG-Bench)

---

## 💡 一句话要点

**提出OIG-Bench基准，用于评估多模态大语言模型对单图引导的理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `单图引导理解` `基准数据集` `半自动标注` `多智能体协作`

## 📋 核心要点

1. 现有方法在评估多模态大语言模型对单图引导的理解能力方面存在不足，缺乏专门的基准。
2. 提出一种半自动标注流程，利用多智能体协作生成图像描述，辅助人工构建高质量的图像-文本对。
3. 构建OIG-Bench基准并评估了29个MLLM，发现模型在语义理解和逻辑推理方面存在明显弱点。

## 📝 摘要（中文）

本文提出OIG-Bench，一个综合性的基准，专注于评估多模态大语言模型（MLLMs）在理解单图引导方面的能力。单图引导是一种结合文本、图像和符号的视觉形式，旨在以重组和结构化的方式呈现信息，便于人类理解，并体现了人类感知和理解的特性。为了降低手动标注的成本，开发了一种半自动标注流程，其中多个智能体协同生成初步的图像描述，辅助人工构建图像-文本对。使用OIG-Bench对29个最先进的MLLM进行了全面评估，包括专有模型和开源模型。结果表明，Qwen2.5-VL-72B在评估的模型中表现最佳，总体准确率为77%。然而，所有模型在语义理解和逻辑推理方面都表现出明显的弱点，表明当前的MLLM仍然难以准确地解释复杂的视觉-文本关系。此外，还证明了所提出的多智能体标注系统在图像描述方面优于所有MLLM，突显了其作为高质量图像描述生成器和未来数据集构建工具的潜力。数据集可在https://github.com/XiejcSYSU/OIG-Bench获取。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLMs）在理解单图引导（One-Image Guides, OIGs）方面的能力评估问题。现有的评估方法通常侧重于通用图像理解或视觉问答，缺乏针对OIGs这种特殊视觉形式的专门基准。OIGs结合了文本、图像和符号，需要模型具备更强的语义理解和逻辑推理能力，而现有方法难以有效评估这些能力。

**核心思路**：论文的核心思路是构建一个专门用于评估MLLMs对OIGs理解能力的基准数据集OIG-Bench。为了降低标注成本，采用了半自动化的标注流程，利用多个智能体协作生成初步的图像描述，辅助人工进行标注，从而提高标注效率和质量。通过对多个MLLMs在OIG-Bench上的评估，可以更准确地了解它们在理解复杂视觉-文本关系方面的能力。

**技术框架**：OIG-Bench的构建流程主要包括以下几个阶段：1) 数据收集：收集来自不同领域的OIGs图像。2) 多智能体辅助标注：利用多个智能体生成初步的图像描述，例如图像标题、对象检测结果等。3) 人工校对与标注：人工对智能体生成的描述进行校对和补充，构建高质量的图像-文本对。4) 基准评估：使用构建好的OIG-Bench对多个MLLMs进行评估，分析它们的性能表现。

**关键创新**：论文的关键创新在于提出了一个半自动化的多智能体辅助标注流程，用于构建高质量的OIG-Bench数据集。该流程通过利用多个智能体的协作，可以显著降低人工标注的成本，并提高标注效率和质量。此外，OIG-Bench数据集本身也是一个重要的创新，它填补了现有MLLM评估基准在OIGs理解能力评估方面的空白。

**关键设计**：多智能体标注系统包含多个预训练模型，例如图像描述生成模型、目标检测模型等。这些模型并行工作，生成不同的图像描述信息，然后将这些信息整合起来，作为人工标注的参考。在基准评估方面，采用了多种评估指标，例如准确率、召回率等，以全面评估MLLMs在OIGs理解方面的性能。

## 📊 实验亮点

实验结果表明，Qwen2.5-VL-72B在OIG-Bench上取得了最佳性能，总体准确率达到77%。然而，所有被评估的模型在语义理解和逻辑推理方面都存在明显的不足，表明现有MLLM在理解复杂视觉-文本关系方面仍有很大的提升空间。此外，多智能体标注系统在图像描述生成方面优于所有MLLM，验证了其作为高质量图像描述生成器的潜力。

## 🎯 应用场景

该研究成果可应用于开发更智能的视觉助手、教育工具和信息检索系统。例如，可以利用MLLM理解OIGs，为用户提供更便捷的导航、操作指南和知识学习服务。此外，OIG-Bench数据集可以促进MLLM在视觉-文本理解方面的研究，推动相关技术的发展。

## 📄 摘要（原文）

> Recent advances in Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities. However, evaluating their capacity for human-like understanding in One-Image Guides remains insufficiently explored. One-Image Guides are a visual format combining text, imagery, and symbols to present reorganized and structured information for easier comprehension, which are specifically designed for human viewing and inherently embody the characteristics of human perception and understanding. Here, we present OIG-Bench, a comprehensive benchmark focused on One-Image Guide understanding across diverse domains. To reduce the cost of manual annotation, we developed a semi-automated annotation pipeline in which multiple intelligent agents collaborate to generate preliminary image descriptions, assisting humans in constructing image-text pairs. With OIG-Bench, we have conducted a comprehensive evaluation of 29 state-of-the-art MLLMs, including both proprietary and open-source models. The results show that Qwen2.5-VL-72B performs the best among the evaluated models, with an overall accuracy of 77%. Nevertheless, all models exhibit notable weaknesses in semantic understanding and logical reasoning, indicating that current MLLMs still struggle to accurately interpret complex visual-text relationships. In addition, we also demonstrate that the proposed multi-agent annotation system outperforms all MLLMs in image captioning, highlighting its potential as both a high-quality image description generator and a valuable tool for future dataset construction. Datasets are available at https://github.com/XiejcSYSU/OIG-Bench.

