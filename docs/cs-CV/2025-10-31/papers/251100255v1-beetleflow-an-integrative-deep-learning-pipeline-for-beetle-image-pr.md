---
layout: default
title: BeetleFlow: An Integrative Deep Learning Pipeline for Beetle Image Processing
---

# BeetleFlow: An Integrative Deep Learning Pipeline for Beetle Image Processing

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00255" target="_blank" class="toolbar-btn">arXiv: 2511.00255v1</a>
    <a href="https://arxiv.org/pdf/2511.00255.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00255v1" 
            onclick="toggleFavorite(this, '2511.00255v1', 'BeetleFlow: An Integrative Deep Learning Pipeline for Beetle Image Processing')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Fangxun Liu, S M Rayeed, Samuel Stevens, Alyson East, Cheng Hsuan Chiang, Colin Lee, Daniel Yi, Junke Yang, Tejas Naik, Ziyi Wang, Connor Kilrain, Elijah H Buckwalter, Jiacheng Hou, Saul Ibaven Bueno, Shuheng Wang, Xinyue Ma, Yifan Liu, Zhiyuan Tao, Ziheng Zhang, Eric Sokol, Michael Belitz, Sydne Record, Charles V. Stewart, Wei-Lun Chao

**分类**: cs.CV

**发布日期**: 2025-10-31

**备注**: 4 pages, NeurIPS 2025 Workshop Imageomics

---

## 💡 一句话要点

**BeetleFlow：用于甲虫图像处理的集成深度学习流水线**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `甲虫图像处理` `深度学习流水线` `对象检测` `图像分割` `Transformer模型` `视觉-语言模型` `昆虫学` `自动化`

## 📋 核心要点

1. 生物学家需要处理大量甲虫图像，但手动处理效率低下，缺乏自动化的解决方案。
2. 论文提出BeetleFlow流水线，集成了对象检测、图像裁剪和形态分割等深度学习技术，实现甲虫图像的自动化处理。
3. 通过Transformer模型和视觉-语言模型，BeetleFlow在甲虫检测和分割任务上取得了较好的效果，提升了处理效率。

## 📝 摘要（中文）

在昆虫学和生态学研究中，生物学家经常需要收集大量的昆虫，其中甲虫是最常见的物种。生物学家组织甲虫的一个常见做法是将它们放在托盘上，并拍摄每个托盘的照片。鉴于数千个此类托盘的图像，拥有一个自动化的流水线来处理大规模数据以供进一步研究非常重要。因此，我们开发了一个三阶段的流水线来检测每个托盘上的所有甲虫，对每个甲虫的图像进行排序和裁剪，并对裁剪后的甲虫进行形态分割。对于检测，我们设计了一个迭代过程，利用基于Transformer的开放词汇对象检测器和一个视觉-语言模型。对于分割，我们手动标记了670张甲虫图像，并微调了基于Transformer的分割模型的两个变体，以实现相对较高精度的甲虫精细分割。该流水线集成了多种深度学习方法，专门用于甲虫图像处理，可以大大提高处理大规模甲虫数据的效率，并加速生物学研究。

## 🔬 方法详解

**问题定义**：论文旨在解决生物学家在处理大规模甲虫图像数据时面临的效率问题。现有方法主要依赖手动操作，耗时且容易出错。缺乏一个自动化的、高效的图像处理流水线来支持后续的生物学研究。

**核心思路**：论文的核心思路是构建一个集成的深度学习流水线，该流水线能够自动检测图像中的甲虫，裁剪出单个甲虫的图像，并进行精细的形态分割。通过自动化处理流程，显著减少人工干预，提高数据处理效率。

**技术框架**：BeetleFlow流水线包含三个主要阶段：1) **甲虫检测**：使用基于Transformer的开放词汇对象检测器和视觉-语言模型进行迭代检测；2) **图像裁剪**：根据检测结果，对每个甲虫的图像进行排序和裁剪；3) **形态分割**：使用微调后的基于Transformer的分割模型对裁剪后的甲虫图像进行精细分割。

**关键创新**：论文的关键创新在于将开放词汇对象检测器和视觉-语言模型应用于甲虫检测，并设计了一个迭代的检测过程，提高了检测的准确性和鲁棒性。此外，通过微调Transformer分割模型，实现了对甲虫形态的精细分割。

**关键设计**：在甲虫检测阶段，采用了迭代检测策略，即先使用开放词汇对象检测器进行初步检测，然后利用视觉-语言模型对检测结果进行验证和修正，从而提高检测的准确率。在形态分割阶段，使用了手动标注的670张甲虫图像对Transformer分割模型进行微调，以适应甲虫图像的特点。

## 📊 实验亮点

论文通过实验验证了BeetleFlow流水线的有效性。在甲虫检测任务中，该流水线能够准确地检测出图像中的甲虫。在形态分割任务中，通过微调Transformer分割模型，实现了对甲虫形态的精细分割，达到了相对较高的精度。这些实验结果表明，BeetleFlow能够显著提高甲虫图像处理的效率和准确性。

## 🎯 应用场景

BeetleFlow流水线可广泛应用于昆虫学、生态学等领域，加速生物多样性研究、物种识别和保护工作。该流水线能够自动化处理大规模甲虫图像数据，为生物学家提供高效的数据分析工具，促进相关领域的研究进展。未来，该方法可以扩展到其他昆虫或生物物种的图像处理。

## 📄 摘要（原文）

> In entomology and ecology research, biologists often need to collect a large number of insects, among which beetles are the most common species. A common practice for biologists to organize beetles is to place them on trays and take a picture of each tray. Given the images of thousands of such trays, it is important to have an automated pipeline to process the large-scale data for further research. Therefore, we develop a 3-stage pipeline to detect all the beetles on each tray, sort and crop the image of each beetle, and do morphological segmentation on the cropped beetles. For detection, we design an iterative process utilizing a transformer-based open-vocabulary object detector and a vision-language model. For segmentation, we manually labeled 670 beetle images and fine-tuned two variants of a transformer-based segmentation model to achieve fine-grained segmentation of beetles with relatively high accuracy. The pipeline integrates multiple deep learning methods and is specialized for beetle image processing, which can greatly improve the efficiency to process large-scale beetle data and accelerate biological research.

