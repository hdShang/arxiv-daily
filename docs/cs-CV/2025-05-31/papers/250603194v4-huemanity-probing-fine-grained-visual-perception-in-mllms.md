---
layout: default
title: "HueManity: Probing Fine-Grained Visual Perception in MLLMs"
---

# HueManity: Probing Fine-Grained Visual Perception in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03194" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03194v4</a>
  <a href="https://arxiv.org/pdf/2506.03194.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03194v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03194v4', 'HueManity: Probing Fine-Grained Visual Perception in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rynaa Grover, Jayant Sravan Tamarapalli, Sahiti Yerramilli, Nilay Pande

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-05-31 (更新: 2025-09-12)

**期刊**: ICML 2025 Workshop on Assessing World Models

**DOI**: [10.48550/arXiv.2506.03194](https://doi.org/10.48550/arXiv.2506.03194)

---

## 💡 一句话要点

**提出HueManity基准以评估多模态大语言模型的视觉感知能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉感知` `基准数据集` `模式识别` `Ishihara测试` `计算机视觉` `模型评估`

## 📋 核心要点

1. 当前多模态大语言模型在细致的视觉感知任务上表现不足，存在显著的性能差距。
2. HueManity基准通过嵌入Ishihara测试风格的图像，专注于评估MLLMs的精确模式识别能力。
3. 实验结果显示，最佳MLLM在简单任务上的准确率为33.6%，而人类参与者接近完美，揭示了模型的感知能力缺陷。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在高层次视觉推理方面表现优异，但在细致的感知任务上表现却相对有限。本文提出HueManity，一个旨在评估MLLMs视觉感知能力的基准数据集。该数据集包含83,850张图像，图像中嵌入了以Ishihara测试风格的点阵模式呈现的两字符字母数字字符串，挑战模型进行精确的模式识别。对九种最先进的MLLMs在HueManity上的评估显示，与人类和传统计算机视觉基线相比，模型的表现存在显著差距。表现最佳的MLLM在数字“简单”任务上的准确率为33.6%，而在字母数字“困难”任务上仅为3%。相比之下，人类参与者的得分接近完美（100%和95.6%），而经过微调的ResNet50模型的准确率分别为96.5%和94.5%。这些结果突显了当前MLLMs在视觉能力方面的关键差距。我们进一步分析了可能导致这一感知差距的架构和训练范式因素，并开源HueManity数据集和代码，以促进对MLLMs感知鲁棒性的进一步研究。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在细致视觉感知任务中的表现不足，现有方法在精确模式识别上存在明显短板。

**核心思路**：HueManity基准通过设计具有挑战性的图像数据集，评估MLLMs在视觉感知方面的能力，旨在揭示模型的局限性并促进改进。

**技术框架**：HueManity数据集包含83,850张图像，采用Ishihara测试风格的点阵模式，模型需识别嵌入的字母数字字符串。评估过程中，比较MLLMs与人类及传统计算机视觉模型的表现。

**关键创新**：HueManity基准的设计是一个重要创新，特别是在视觉感知任务的细粒度评估上，与现有的高层次推理任务形成鲜明对比。

**关键设计**：数据集的构建中，选择了特定的图像样式和字符组合，以确保任务的难度和多样性，同时在评估中使用了多种先进的MLLMs进行对比分析。

## 📊 实验亮点

实验结果显示，最佳表现的MLLM在数字“简单”任务上的准确率为33.6%，而在字母数字“困难”任务上仅为3%。相比之下，人类参与者的得分接近完美（100%和95.6%），而微调的ResNet50模型的准确率分别为96.5%和94.5%，揭示了当前MLLMs在视觉感知上的显著不足。

## 🎯 应用场景

HueManity基准的提出为多模态大语言模型的视觉感知能力提供了新的评估标准，具有广泛的应用潜力。该研究不仅可以帮助改进现有模型的视觉理解能力，还能为未来的多模态学习研究提供重要参考，推动人工智能在视觉感知领域的进步。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) excel at high-level visual reasoning, but their performance on nuanced perceptual tasks remains surprisingly limited. We present HueManity, a benchmark designed to assess visual perception in MLLMs. The dataset comprises 83,850 images featuring two-character alphanumeric strings embedded in Ishihara test style dot patterns, challenging models on precise pattern recognition. Our evaluation of nine state-of-the-art MLLMs on HueManity demonstrates a significant performance deficit compared to human and traditional computer vision baselines. The best-performing MLLM achieved a 33.6% accuracy on the numeric `easy' task and a striking 3% on the alphanumeric `hard' task. In contrast, human participants achieved near-perfect scores (100% and 95.6%), and a fine-tuned ResNet50 model reached accuracies of 96.5% and 94.5%. These results highlight a critical gap in the visual capabilities of current MLLMs. Our analysis further explores potential architectural and training-paradigm factors contributing to this perceptual gap in MLLMs. We open-source HueManity dataset and code to foster further research in improving perceptual robustness of MLLMs.

