---
layout: default
title: PaveSync: A Unified and Comprehensive Dataset for Pavement Distress Analysis and Classification
---

# PaveSync: A Unified and Comprehensive Dataset for Pavement Distress Analysis and Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20011" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20011v1</a>
  <a href="https://arxiv.org/pdf/2512.20011.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20011v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20011v1', 'PaveSync: A Unified and Comprehensive Dataset for Pavement Distress Analysis and Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Blessing Agyei Kyem, Joshua Kofi Asamoah, Anthony Dontoh, Andrews Danyo, Eugene Denteh, Armstrong Aboah

**分类**: cs.CV

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**PaveSync：统一全面的路面病害分析与分类数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `路面病害检测` `数据集` `目标检测` `基准测试` `标准化` `计算机视觉` `智能交通`

## 📋 核心要点

1. 现有路面病害数据集缺乏统一标准，标注方式、病害定义各异，阻碍了模型的泛化能力和统一训练。
2. PaveSync数据集整合了多个公开数据源，标准化标注格式和病害类型，构建了包含多国数据的综合基准。
3. 实验表明，基于PaveSync训练的YOLOv8-YOLOv12、Faster R-CNN和DETR等模型在多种场景下表现出竞争优势。

## 📝 摘要（中文）

由于缺乏标准化数据集，自动路面缺陷检测通常难以在各种真实条件下推广。现有数据集在标注风格、病害类型定义和格式上存在差异，限制了它们在统一训练中的集成。为了解决这一差距，我们引入了一个全面的基准数据集，该数据集将多个公开可用的来源整合为一个标准化的集合，包含来自七个国家的52747张图像，以及覆盖13种不同病害类型的135277个边界框标注。该数据集捕捉了图像质量、分辨率、视角和天气条件等方面的广泛真实变化，为一致的训练和评估提供了独特的资源。通过使用包括YOLOv8-YOLOv12、Faster R-CNN和DETR在内的最先进的目标检测模型进行基准测试，证明了其有效性，这些模型在各种场景中都取得了具有竞争力的性能。通过标准化类别定义和标注格式，该数据集为路面缺陷检测提供了第一个具有全球代表性的基准，并能够对模型进行公平比较，包括零样本迁移到新环境。

## 🔬 方法详解

**问题定义**：现有路面病害检测数据集存在标注风格不统一、病害类型定义不一致、数据格式各异等问题，导致模型难以在不同数据集上进行统一训练和评估，泛化能力受限。缺乏一个全球代表性的、标准化的路面病害数据集，阻碍了该领域的研究进展。

**核心思路**：PaveSync的核心思路是将多个公开可用的路面病害数据集进行整合，并对数据进行清洗、标注格式标准化、病害类型定义统一，从而构建一个统一且全面的基准数据集。通过提供一个标准化的数据集，PaveSync旨在促进路面病害检测模型的公平比较、统一训练和零样本迁移。

**技术框架**：PaveSync数据集的构建流程主要包括以下几个阶段：1) 数据收集：从多个公开可用的路面病害数据集中收集图像数据。2) 数据清洗：对收集到的图像数据进行清洗，去除质量较差或不相关的图像。3) 标注格式标准化：将不同数据集的标注格式统一为一种标准格式，例如COCO格式。4) 病害类型定义统一：将不同数据集中的病害类型定义统一为一组标准的病害类型，例如裂缝、坑洼、车辙等。5) 数据集划分：将整合后的数据集划分为训练集、验证集和测试集。

**关键创新**：PaveSync的关键创新在于：1) 它是第一个全球代表性的路面病害基准数据集，包含了来自七个国家的数据，具有广泛的地域覆盖性。2) 它对多个公开数据集进行了整合和标准化，解决了现有数据集之间不兼容的问题。3) 它提供了统一的标注格式和病害类型定义，方便研究人员进行模型训练和评估。

**关键设计**：PaveSync数据集包含了52747张图像和135277个边界框标注，覆盖了13种不同的病害类型。数据集的图像质量、分辨率、视角和天气条件等都具有广泛的变化，能够模拟真实的道路场景。论文没有详细说明具体的参数设置、损失函数或网络结构，而是侧重于数据集的构建和评估。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20011v1/images_distribution_pie_chart_with_legend.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20011v1/Cropped_Image.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20011v1/weather-conditions.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文使用YOLOv8-YOLOv12、Faster R-CNN和DETR等先进目标检测模型在PaveSync数据集上进行了基准测试，验证了数据集的有效性。实验结果表明，这些模型在各种场景下都取得了具有竞争力的性能，证明了PaveSync数据集能够为路面病害检测模型的训练和评估提供有效的支持。

## 🎯 应用场景

PaveSync数据集可广泛应用于智能交通、道路维护和城市管理等领域。通过训练基于PaveSync数据集的路面病害检测模型，可以实现对道路状况的自动评估，辅助道路维护决策，提高道路安全性和使用寿命，并降低维护成本。该数据集的标准化特性也为模型的跨区域应用提供了可能。

## 📄 摘要（原文）

> Automated pavement defect detection often struggles to generalize across diverse real-world conditions due to the lack of standardized datasets. Existing datasets differ in annotation styles, distress type definitions, and formats, limiting their integration for unified training. To address this gap, we introduce a comprehensive benchmark dataset that consolidates multiple publicly available sources into a standardized collection of 52747 images from seven countries, with 135277 bounding box annotations covering 13 distinct distress types. The dataset captures broad real-world variation in image quality, resolution, viewing angles, and weather conditions, offering a unique resource for consistent training and evaluation. Its effectiveness was demonstrated through benchmarking with state-of-the-art object detection models including YOLOv8-YOLOv12, Faster R-CNN, and DETR, which achieved competitive performance across diverse scenarios. By standardizing class definitions and annotation formats, this dataset provides the first globally representative benchmark for pavement defect detection and enables fair comparison of models, including zero-shot transfer to new environments.

