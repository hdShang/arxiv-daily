---
layout: default
title: "VisCodex: Unified Multimodal Code Generation via Merging Vision and Coding Models"
---

# VisCodex: Unified Multimodal Code Generation via Merging Vision and Coding Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09945" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09945v1</a>
  <a href="https://arxiv.org/pdf/2508.09945.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09945v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09945v1', 'VisCodex: Unified Multimodal Code Generation via Merging Vision and Coding Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingjie Jiang, Shaohan Huang, Xun Wu, Yixia Li, Dongdong Zhang, Furu Wei

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出VisCodex以解决多模态代码生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态代码生成` `视觉理解` `编码语言模型` `模型合并` `数据集构建` `编程教育` `智能助手`

## 📋 核心要点

1. 现有多模态大型语言模型在从视觉和文本输入生成代码方面能力有限，无法满足复杂编程需求。
2. 本文提出VisCodex，通过将视觉和编码语言模型无缝融合，提升多模态代码生成能力，采用任务向量模型合并技术。
3. 实验结果显示，VisCodex在开源MLLMs中表现优异，接近专有模型的性能，验证了模型合并策略的有效性。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在视觉与文本理解的整合上取得了显著进展，但在从多模态输入生成代码的能力上仍然有限。本文提出了VisCodex，一个统一框架，通过无缝融合视觉和编码语言模型，赋予MLLMs强大的多模态代码生成能力。我们采用基于任务向量的模型合并技术，将最先进的编码LLM集成到强大的视觉-语言骨干中，同时保留视觉理解和高级编码技能。为支持训练和评估，我们引入了多模态编码数据集（MCD），这是一个包含598k样本的大规模多样化集合，涵盖高质量HTML代码、图表图像-代码对、图像增强的StackOverflow问答和算法问题。此外，我们提出了InfiBench-V，这是一个新颖且具有挑战性的基准，专门设计用于评估模型在需要细致理解文本和视觉上下文的视觉丰富的现实编程问题上的表现。大量实验表明，VisCodex在开源MLLMs中实现了最先进的性能，并接近于GPT-4o等专有模型，突显了我们的模型合并策略和新数据集的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大型语言模型在生成代码时的能力不足，尤其是在处理复杂的视觉和文本输入时的局限性。现有方法往往无法有效结合视觉理解与编程能力，导致生成的代码质量不高。

**核心思路**：VisCodex的核心思路是通过任务向量模型合并技术，将先进的编码语言模型与强大的视觉-语言骨干无缝结合，从而提升模型在多模态输入下的代码生成能力。这样的设计旨在同时保留视觉理解和编码技能，使模型能够更好地处理复杂的编程任务。

**技术框架**：VisCodex的整体架构包括视觉理解模块、编码生成模块和任务向量合并模块。视觉理解模块负责提取输入图像的特征，编码生成模块则基于提取的特征和文本输入生成代码，任务向量合并模块则实现两者的有效融合。

**关键创新**：本文的关键创新在于提出了一种新的模型合并策略，能够有效整合视觉和编码模型的优势，与现有方法相比，VisCodex在多模态代码生成任务中表现出更高的准确性和灵活性。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡视觉理解与代码生成的性能，同时在网络结构上进行了优化，以确保在处理复杂输入时的高效性和准确性。

## 📊 实验亮点

实验结果表明，VisCodex在多模态代码生成任务中达到了最先进的性能，尤其是在与开源MLLMs的对比中，表现出显著的提升，接近于GPT-4o等专有模型，验证了模型合并策略的有效性和新数据集的贡献。

## 🎯 应用场景

VisCodex的研究成果具有广泛的应用潜力，特别是在教育、软件开发和自动化编程等领域。通过提升多模态代码生成能力，该模型可以帮助开发者更高效地编写代码，甚至在教育场景中辅助学生学习编程。此外，未来可能在智能助手和编程工具中得到应用，推动编程的自动化和智能化进程。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have significantly advanced the integration of visual and textual understanding. However, their ability to generate code from multimodal inputs remains limited. In this work, we introduce VisCodex, a unified framework that seamlessly merges vision and coding language models to empower MLLMs with strong multimodal code generation abilities. Leveraging a task vector-based model merging technique, we integrate a state-of-the-art coding LLM into a strong vision-language backbone, while preserving both visual comprehension and advanced coding skills. To support training and evaluation, we introduce the Multimodal Coding Dataset (MCD), a large-scale and diverse collection of 598k samples, including high-quality HTML code, chart image-code pairs, image-augmented StackOverflow QA, and algorithmic problems. Furthermore, we propose InfiBench-V, a novel and challenging benchmark specifically designed to assess models on visually-rich, real-world programming questions that demand a nuanced understanding of both textual and visual contexts. Extensive experiments show that VisCodex achieves state-of-the-art performance among open-source MLLMs and approaches proprietary models like GPT-4o, highlighting the effectiveness of our model merging strategy and new datasets.

