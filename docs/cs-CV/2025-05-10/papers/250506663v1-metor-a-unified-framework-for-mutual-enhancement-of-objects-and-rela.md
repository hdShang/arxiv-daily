---
layout: default
title: METOR: A Unified Framework for Mutual Enhancement of Objects and Relationships in Open-vocabulary Video Visual Relationship Detection
---

# METOR: A Unified Framework for Mutual Enhancement of Objects and Relationships in Open-vocabulary Video Visual Relationship Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06663" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06663v1</a>
  <a href="https://arxiv.org/pdf/2505.06663.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06663v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06663v1', 'METOR: A Unified Framework for Mutual Enhancement of Objects and Relationships in Open-vocabulary Video Visual Relationship Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongqi Wang, Xinxiao Wu, Shuo Yang

**分类**: cs.CV

**发布日期**: 2025-05-10

**备注**: IJCAI2025

---

## 💡 一句话要点

**提出METOR框架以解决开放词汇视频视觉关系检测问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇检测` `视频理解` `视觉关系检测` `CLIP模型` `互增强机制` `多模态学习` `深度学习`

## 📋 核心要点

1. 现有方法通常采用级联管道，先检测物体再分类关系，容易导致错误传播，影响整体性能。
2. 提出METOR框架，通过查询基础的统一建模，互相增强物体检测与关系分类，提升开放词汇场景下的识别能力。
3. 在VidVRD和VidOR数据集上进行的实验表明，METOR框架在性能上超越了现有的最先进方法。

## 📝 摘要（中文）

开放词汇视频视觉关系检测旨在识别视频中的物体及其关系，而不受预定义类别的限制。现有方法通常依赖于预训练的视觉-语言模型（如CLIP）来识别新类别，并采用级联管道先检测物体再分类关系，这可能导致错误传播，影响性能。本文提出了互增强物体与关系的框架METOR，采用查询基础的统一框架共同建模并增强物体检测与关系分类。该框架设计了基于CLIP的上下文细化编码模块，以提取物体和关系的视觉上下文，从而改善文本特征和物体查询的编码。通过迭代增强模块，充分利用物体与关系的相互依赖性，提升识别性能。大量实验表明，该框架在VidVRD和VidOR两个公共数据集上达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文解决开放词汇视频视觉关系检测中的物体与关系识别问题。现有方法的痛点在于采用级联管道，容易导致错误传播，影响最终的检测效果。

**核心思路**：METOR框架通过查询基础的统一建模，旨在共同增强物体检测与关系分类，充分利用它们之间的相互依赖性，从而提升识别性能。

**技术框架**：该框架主要包括两个模块：1) 基于CLIP的上下文细化编码模块，用于提取物体和关系的视觉上下文；2) 迭代增强模块，通过交替增强物体和关系的表示来提升识别效果。

**关键创新**：最重要的创新在于提出了互增强机制，能够在物体与关系之间建立更强的联系，从而克服传统方法的局限性。

**关键设计**：在设计中，使用了CLIP模型进行上下文细化，确保文本特征和物体查询的编码更具泛化能力。此外，迭代增强模块的设计使得物体与关系的表示能够相互促进，提升整体性能。

## 📊 实验亮点

在VidVRD和VidOR数据集上的实验结果显示，METOR框架在多个指标上均超越了现有最先进的方法，具体提升幅度达到X%（具体数据待补充），验证了其在开放词汇视频视觉关系检测中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括视频监控、智能交通、自动驾驶等场景，能够帮助系统更准确地理解视频内容中的物体及其相互关系，提升决策能力。未来，随着开放词汇检测技术的进步，可能会在更多复杂场景中得到应用，推动相关领域的发展。

## 📄 摘要（原文）

> Open-vocabulary video visual relationship detection aims to detect objects and their relationships in videos without being restricted by predefined object or relationship categories. Existing methods leverage the rich semantic knowledge of pre-trained vision-language models such as CLIP to identify novel categories. They typically adopt a cascaded pipeline to first detect objects and then classify relationships based on the detected objects, which may lead to error propagation and thus suboptimal performance. In this paper, we propose Mutual EnhancemenT of Objects and Relationships (METOR), a query-based unified framework to jointly model and mutually enhance object detection and relationship classification in open-vocabulary scenarios. Under this framework, we first design a CLIP-based contextual refinement encoding module that extracts visual contexts of objects and relationships to refine the encoding of text features and object queries, thus improving the generalization of encoding to novel categories. Then we propose an iterative enhancement module to alternatively enhance the representations of objects and relationships by fully exploiting their interdependence to improve recognition performance. Extensive experiments on two public datasets, VidVRD and VidOR, demonstrate that our framework achieves state-of-the-art performance.

