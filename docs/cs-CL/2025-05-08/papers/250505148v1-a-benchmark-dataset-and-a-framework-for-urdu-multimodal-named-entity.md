---
layout: default
title: A Benchmark Dataset and a Framework for Urdu Multimodal Named Entity Recognition
---

# A Benchmark Dataset and a Framework for Urdu Multimodal Named Entity Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05148" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05148v1</a>
  <a href="https://arxiv.org/pdf/2505.05148.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05148v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05148v1', 'A Benchmark Dataset and a Framework for Urdu Multimodal Named Entity Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hussain Ahmad, Qingyang Zeng, Jing Wan

**分类**: cs.CL

**发布日期**: 2025-05-08

**备注**: 16 pages, 5 figures. Preprint

---

## 💡 一句话要点

**提出U-MNER框架以解决乌尔都语多模态命名实体识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态识别` `命名实体识别` `乌尔都语` `自然语言处理` `深度学习`

## 📋 核心要点

1. 低资源语言如乌尔都语的多模态命名实体识别（MNER）研究相对滞后，缺乏标注数据集和标准化基准。
2. 提出U-MNER框架，发布Twitter2015-乌尔都语数据集，结合文本和视觉信息进行命名实体识别。
3. 在Twitter2015-乌尔都语数据集上，模型实现了最先进的性能，推动了低资源语言MNER的研究进展。

## 📝 摘要（中文）

随着社交媒体上文本和图像等多模态内容的出现，多模态命名实体识别（MNER）在自然语言处理领域变得愈发重要。然而，对于低资源语言如乌尔都语，MNER的研究仍然相对滞后，主要挑战在于缺乏标注的多模态数据集和标准化的基准。为此，本文提出了U-MNER框架，并发布了Twitter2015-乌尔都语数据集，这是乌尔都语MNER的开创性资源。该数据集基于广泛使用的Twitter2015数据集进行改编，并按照乌尔都语特有的语法规则进行了标注。我们在该数据集上评估了文本和多模态模型，建立了基准基线，为未来的乌尔都语MNER研究提供了支持。U-MNER框架结合了文本和视觉上下文，使用乌尔都-BERT进行文本嵌入，使用ResNet进行视觉特征提取，并通过跨模态融合模块对信息进行对齐和融合。我们的模型在Twitter2015-乌尔都语数据集上达到了最先进的性能，为低资源语言的进一步MNER研究奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决乌尔都语的多模态命名实体识别问题，现有方法在低资源语言上缺乏有效的数据集和基准评估，导致研究进展缓慢。

**核心思路**：通过构建U-MNER框架，结合文本和视觉信息，利用乌尔都-BERT和ResNet进行特征提取，旨在提升乌尔都语的MNER性能。

**技术框架**：U-MNER框架包括数据集构建、特征提取、跨模态融合模块等主要部分，首先对Twitter2015-乌尔都语数据集进行标注，然后使用乌尔都-BERT进行文本嵌入，ResNet提取视觉特征，最后通过融合模块整合信息。

**关键创新**：U-MNER框架的创新在于其跨模态融合模块，能够有效对齐和融合文本与视觉信息，显著提升了乌尔都语MNER的性能。

**关键设计**：在模型设计中，使用了乌尔都-BERT作为文本嵌入，ResNet作为视觉特征提取网络，采用了适合多模态学习的损失函数，确保了模型的有效性和准确性。

## 📊 实验亮点

在Twitter2015-乌尔都语数据集上，U-MNER框架实现了最先进的性能，具体提升幅度未知，相较于现有基线模型表现出显著优势，为低资源语言的MNER研究提供了新的方向和基础。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体分析、信息检索和自动内容标注等。通过提升乌尔都语的多模态命名实体识别能力，可以为相关领域的研究和应用提供更准确的工具，推动低资源语言的自然语言处理技术发展。

## 📄 摘要（原文）

> The emergence of multimodal content, particularly text and images on social media, has positioned Multimodal Named Entity Recognition (MNER) as an increasingly important area of research within Natural Language Processing. Despite progress in high-resource languages such as English, MNER remains underexplored for low-resource languages like Urdu. The primary challenges include the scarcity of annotated multimodal datasets and the lack of standardized baselines. To address these challenges, we introduce the U-MNER framework and release the Twitter2015-Urdu dataset, a pioneering resource for Urdu MNER. Adapted from the widely used Twitter2015 dataset, it is annotated with Urdu-specific grammar rules. We establish benchmark baselines by evaluating both text-based and multimodal models on this dataset, providing comparative analyses to support future research on Urdu MNER. The U-MNER framework integrates textual and visual context using Urdu-BERT for text embeddings and ResNet for visual feature extraction, with a Cross-Modal Fusion Module to align and fuse information. Our model achieves state-of-the-art performance on the Twitter2015-Urdu dataset, laying the groundwork for further MNER research in low-resource languages.

