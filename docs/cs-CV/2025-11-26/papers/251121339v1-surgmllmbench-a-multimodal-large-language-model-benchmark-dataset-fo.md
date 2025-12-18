---
layout: default
title: SurgMLLMBench: A Multimodal Large Language Model Benchmark Dataset for Surgical Scene Understanding
---

# SurgMLLMBench: A Multimodal Large Language Model Benchmark Dataset for Surgical Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21339" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21339v1</a>
  <a href="https://arxiv.org/pdf/2511.21339.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21339v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21339v1', 'SurgMLLMBench: A Multimodal Large Language Model Benchmark Dataset for Surgical Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tae-Min Choi, Tae Kyeong Jeong, Garam Kim, Jaemin Lee, Yeongyoon Koh, In Cheul Choi, Jae-Ho Chung, Jong Woong Park, Juyoun Park

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-26

**备注**: 10 pages, 5 figures

---

## 💡 一句话要点

**SurgMLLMBench：用于手术场景理解的多模态大语言模型基准数据集**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多模态学习` `大语言模型` `手术场景理解` `视觉问答` `像素级分割`

## 📋 核心要点

1. 现有手术数据集主要采用VQA格式，分类体系不统一，缺乏像素级分割支持，限制了多模态LLM的评估和应用。
2. SurgMLLMBench通过统一的分类体系整合了多种手术方式的像素级器械分割掩码和结构化VQA注释，支持更全面的评估和交互。
3. 实验表明，在SurgMLLMBench上训练的模型在不同手术领域表现一致，并能有效泛化到新的数据集。

## 📝 摘要（中文）

多模态大语言模型（LLM）的最新进展凸显了其在医疗和外科应用中的潜力。然而，现有的手术数据集主要采用视觉问答（VQA）格式，具有异构的分类体系，并且缺乏对像素级分割的支持，限制了一致的评估和适用性。我们提出了SurgMLLMBench，这是一个统一的多模态基准，专门用于开发和评估用于手术场景理解的交互式多模态LLM，包括新收集的显微外科人工血管吻合（MAVIS）数据集。它在统一的分类体系下整合了腹腔镜、机器人辅助和显微外科领域的像素级器械分割掩码和结构化VQA注释，从而能够进行超越传统VQA任务的全面评估，并实现更丰富的视觉对话交互。广泛的基线实验表明，在SurgMLLMBench上训练的单个模型可以在不同领域实现一致的性能，并有效地推广到未见过的数据集。SurgMLLMBench将公开发布，作为一个强大的资源，以推进多模态手术AI研究，支持可重复的评估和交互式手术推理模型的开发。

## 🔬 方法详解

**问题定义**：现有手术数据集主要采用视觉问答（VQA）格式，且不同数据集的标注体系不统一，缺乏像素级别的分割信息，这使得训练和评估用于手术场景理解的多模态大语言模型（LLM）变得困难。现有方法难以进行一致性评估，并且限制了模型在不同手术场景下的泛化能力。

**核心思路**：论文的核心思路是构建一个统一的多模态基准数据集SurgMLLMBench，该数据集包含多种手术方式（腹腔镜、机器人辅助、显微外科）的图像和视频数据，并提供统一的标注体系，包括像素级别的器械分割掩码和结构化的VQA注释。通过统一的数据格式和标注，可以更方便地训练和评估多模态LLM在手术场景理解方面的能力。

**技术框架**：SurgMLLMBench数据集包含三个主要部分：腹腔镜手术数据、机器人辅助手术数据和显微外科手术数据（MAVIS）。对于每种手术数据，都提供了像素级别的器械分割掩码和结构化的VQA注释。数据集的构建流程包括数据收集、标注和验证三个阶段。标注过程采用统一的分类体系，确保不同手术方式的数据具有可比性。

**关键创新**：SurgMLLMBench的关键创新在于其统一的多模态基准数据集，它整合了多种手术方式的数据，并提供了像素级别的器械分割掩码和结构化的VQA注释。这种统一的数据格式和标注体系使得可以更方便地训练和评估多模态LLM在手术场景理解方面的能力，并促进了不同模型之间的比较和分析。此外，新收集的MAVIS数据集也为显微外科手术场景理解提供了新的数据资源。

**关键设计**：SurgMLLMBench数据集的关键设计包括：1) 统一的分类体系，用于标注不同手术方式的数据；2) 像素级别的器械分割掩码，用于提供更精细的视觉信息；3) 结构化的VQA注释，用于评估模型对手术场景的理解能力。具体参数设置和网络结构取决于使用的多模态LLM模型，论文主要关注数据集的构建和评估，而非特定模型的优化。

## 📊 实验亮点

实验结果表明，在SurgMLLMBench上训练的单个模型可以在不同手术领域实现一致的性能，并且能够有效地泛化到未见过的数据集。这表明SurgMLLMBench是一个有效的基准数据集，可以用于训练和评估多模态LLM在手术场景理解方面的能力。具体的性能数据和提升幅度需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于开发智能手术辅助系统，例如，通过理解手术场景，为医生提供实时的器械定位、操作建议和风险预警。此外，该数据集还可以用于训练机器人手术系统，提高手术的精准性和安全性。未来，该研究有望推动手术AI的智能化发展，提升医疗水平。

## 📄 摘要（原文）

> Recent advances in multimodal large language models (LLMs) have highlighted their potential for medical and surgical applications. However, existing surgical datasets predominantly adopt a Visual Question Answering (VQA) format with heterogeneous taxonomies and lack support for pixel-level segmentation, limiting consistent evaluation and applicability. We present SurgMLLMBench, a unified multimodal benchmark explicitly designed for developing and evaluating interactive multimodal LLMs for surgical scene understanding, including the newly collected Micro-surgical Artificial Vascular anastomosIS (MAVIS) dataset. It integrates pixel-level instrument segmentation masks and structured VQA annotations across laparoscopic, robot-assisted, and micro-surgical domains under a unified taxonomy, enabling comprehensive evaluation beyond traditional VQA tasks and richer visual-conversational interactions. Extensive baseline experiments show that a single model trained on SurgMLLMBench achieves consistent performance across domains and generalizes effectively to unseen datasets. SurgMLLMBench will be publicly released as a robust resource to advance multimodal surgical AI research, supporting reproducible evaluation and development of interactive surgical reasoning models.

