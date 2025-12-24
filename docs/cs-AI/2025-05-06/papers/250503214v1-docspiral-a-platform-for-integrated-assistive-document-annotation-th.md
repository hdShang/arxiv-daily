---
layout: default
title: DocSpiral: A Platform for Integrated Assistive Document Annotation through Human-in-the-Spiral
---

# DocSpiral: A Platform for Integrated Assistive Document Annotation through Human-in-the-Spiral

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03214" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03214v1</a>
  <a href="https://arxiv.org/pdf/2505.03214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03214v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03214v1', 'DocSpiral: A Platform for Integrated Assistive Document Annotation through Human-in-the-Spiral')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiang Sun, Sirui Li, Tingting Bi, Du Huynh, Mark Reynolds, Yuanyi Luo, Wei Liu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出DocSpiral以解决图像文档结构化数据提取问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文档注释` `人机协作` `结构化数据提取` `图像处理` `机器学习`

## 📋 核心要点

1. 核心问题：现有方法在从图像文档中提取结构化数据时面临文档多样性和人工注释效率低下的挑战。
2. 方法要点：DocSpiral通过人机协作的迭代循环设计，逐步减少人工干预，提高文档注释效率。
3. 实验或效果：实验结果显示，DocSpiral在模型训练中减少了至少41%的注释时间，并在三次迭代中保持一致的性能提升。

## 📝 摘要（中文）

从领域特定的图像文档（如扫描报告）中获取结构化数据对许多下游任务至关重要，但由于文档的多样性，这一过程仍然具有挑战性。许多文档以图像形式存在，而非机器可读文本，因此需要人工注释以训练自动提取系统。我们提出了DocSpiral，这是首个基于人机协作的辅助文档注释平台，旨在解决从领域特定图像文档集合中提取结构化信息的挑战。DocSpiral通过迭代循环的设计，使人工注释能够训练模型，逐步减少人工干预。实验表明，该框架在模型训练过程中减少了至少41%的注释时间，同时在三次迭代中表现出一致的性能提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决从领域特定的图像文档中提取结构化数据的难题。现有方法往往依赖于人工注释，效率低下且难以应对文档的多样性。

**核心思路**：DocSpiral的核心思路是通过人机协作的迭代循环，利用人工注释来训练模型，逐步减少对人工干预的依赖，从而提高注释效率和准确性。

**技术框架**：DocSpiral的整体架构包括文档格式规范化、全面的注释接口、评估指标仪表盘和API端点，形成一个统一的工作流程，支持AI/ML模型的开发。

**关键创新**：最重要的技术创新在于其“人机协作”的迭代设计，使得模型在训练过程中能够不断优化，减少人工干预的需求。这与传统的单一人工注释方法形成了鲜明对比。

**关键设计**：在关键设计方面，DocSpiral采用了灵活的注释接口和标准化的文档格式，确保了注释过程的高效性。同时，系统集成了评估指标，便于实时监控模型性能。具体的参数设置和损失函数设计尚未详细披露，属于未知领域。

## 📊 实验亮点

实验结果表明，DocSpiral在模型训练过程中减少了至少41%的注释时间，并在三次迭代中表现出一致的性能提升。这一显著的效率提升为文档处理领域的AI/ML模型开发提供了强有力的支持。

## 🎯 应用场景

DocSpiral的潜在应用场景包括地球科学和医疗保健等领域，这些领域通常需要处理大量图像文档。通过降低AI/ML模型开发的门槛，DocSpiral能够促进大型语言模型在这些文档密集型领域的应用，提升数据处理效率和准确性。

## 📄 摘要（原文）

> Acquiring structured data from domain-specific, image-based documents such as scanned reports is crucial for many downstream tasks but remains challenging due to document variability. Many of these documents exist as images rather than as machine-readable text, which requires human annotation to train automated extraction systems. We present DocSpiral, the first Human-in-the-Spiral assistive document annotation platform, designed to address the challenge of extracting structured information from domain-specific, image-based document collections. Our spiral design establishes an iterative cycle in which human annotations train models that progressively require less manual intervention. DocSpiral integrates document format normalization, comprehensive annotation interfaces, evaluation metrics dashboard, and API endpoints for the development of AI / ML models into a unified workflow. Experiments demonstrate that our framework reduces annotation time by at least 41\% while showing consistent performance gains across three iterations during model training. By making this annotation platform freely accessible, we aim to lower barriers to AI/ML models development in document processing, facilitating the adoption of large language models in image-based, document-intensive fields such as geoscience and healthcare. The system is freely available at: https://app.ai4wa.com. The demonstration video is available: https://app.ai4wa.com/docs/docspiral/demo.

