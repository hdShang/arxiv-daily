---
layout: default
title: "VisioFirm: Cross-Platform AI-assisted Annotation Tool for Computer Vision"
---

# VisioFirm: Cross-Platform AI-assisted Annotation Tool for Computer Vision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04180" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04180v1</a>
  <a href="https://arxiv.org/pdf/2509.04180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04180v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04180v1', 'VisioFirm: Cross-Platform AI-assisted Annotation Tool for Computer Vision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Safouane El Ghazouali, Umberto Michelucci

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-04

**🔗 代码/项目**: [GITHUB](https://github.com/OschAI/VisioFirm)

---

## 💡 一句话要点

**提出VisioFirm以解决计算机视觉标注效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算机视觉` `图像标注` `AI辅助` `自动化工具` `开源软件` `数据集处理` `深度学习`

## 📋 核心要点

1. 现有标注工具通常需要大量手动输入，导致在处理大规模数据集时效率低下，难以满足快速发展的计算机视觉需求。
2. VisioFirm通过集成先进的AI模型和过滤管道，提供了一种AI辅助的自动化标注解决方案，显著减少人工干预。
3. 在多种数据集上进行的基准测试表明，VisioFirm能够将人工标注工作量减少高达90%，同时保持高标注准确率。

## 📝 摘要（中文）

AI模型依赖于标注数据进行模式学习和预测，而标注通常是一个劳动密集型的过程，涉及从简单分类标签到更复杂任务（如目标检测、定向边界框估计和实例分割）的标签关联。传统工具往往需要大量手动输入，限制了大规模数据集的可扩展性。为此，本文提出了VisioFirm，一个开源的Web应用程序，旨在通过AI辅助自动化来简化图像标注。VisioFirm将最先进的基础模型集成到一个过滤管道的界面中，以减少人工干预。该混合方法结合了CLIP和预训练检测器（如Ultralytics模型）以及零样本模型（如Grounding DINO），生成初步标注并通过低置信度阈值最大化召回率。经过测试，VisioFirm在COCO类上的初步预测大多正确，用户可以通过交互工具进行精细调整。

## 🔬 方法详解

**问题定义**：本文旨在解决计算机视觉领域中图像标注的低效率问题。现有方法通常依赖于大量手动输入，难以应对大规模数据集的需求。

**核心思路**：VisioFirm的核心思路是通过AI辅助自动化来简化标注过程，结合多种先进模型生成初步标注，降低人工干预的需求。

**技术框架**：VisioFirm的整体架构包括数据输入、AI模型推理、初步标注生成和用户交互四个主要模块。用户可以通过交互工具对生成的标注进行精细调整。

**关键创新**：VisioFirm的关键创新在于将CLIP与预训练检测器和零样本模型结合，生成初步标注并通过低置信度阈值最大化召回率。这种混合方法显著提高了标注的效率和准确性。

**关键设计**：在技术细节上，VisioFirm使用了WebGPU加速分割过程，支持多种导出格式（如YOLO、COCO、Pascal VOC、CSV），并在模型缓存后支持离线操作，增强了工具的可访问性。通过聚类和IoU图抑制冗余检测，进一步提高了标注的准确性。

## 📊 实验亮点

在多种数据集上的基准测试中，VisioFirm实现了高达90%的人工工作量减少，同时保持了高标注准确率。与传统方法相比，该工具通过聚类和冗余检测抑制技术，显著提升了标注的质量和效率。

## 🎯 应用场景

VisioFirm可广泛应用于计算机视觉领域的图像标注任务，尤其适用于需要处理大规模数据集的场景，如自动驾驶、智能监控和医疗影像分析等。其AI辅助的特性不仅提高了标注效率，还降低了人工成本，具有重要的实际价值和潜在影响。

## 📄 摘要（原文）

> AI models rely on annotated data to learn pattern and perform prediction. Annotation is usually a labor-intensive step that require associating labels ranging from a simple classification label to more complex tasks such as object detection, oriented bounding box estimation, and instance segmentation. Traditional tools often require extensive manual input, limiting scalability for large datasets. To address this, we introduce VisioFirm, an open-source web application designed to streamline image labeling through AI-assisted automation. VisioFirm integrates state-of-the-art foundation models into an interface with a filtering pipeline to reduce human-in-the-loop efforts. This hybrid approach employs CLIP combined with pre-trained detectors like Ultralytics models for common classes and zero-shot models such as Grounding DINO for custom labels, generating initial annotations with low-confidence thresholding to maximize recall. Through this framework, when tested on COCO-type of classes, initial prediction have been proven to be mostly correct though the users can refine these via interactive tools supporting bounding boxes, oriented bounding boxes, and polygons. Additionally, VisioFirm has on-the-fly segmentation powered by Segment Anything accelerated through WebGPU for browser-side efficiency. The tool supports multiple export formats (YOLO, COCO, Pascal VOC, CSV) and operates offline after model caching, enhancing accessibility. VisioFirm demonstrates up to 90\% reduction in manual effort through benchmarks on diverse datasets, while maintaining high annotation accuracy via clustering of connected CLIP-based disambiguate components and IoU-graph for redundant detection suppression. VisioFirm can be accessed from \href{https://github.com/OschAI/VisioFirm}{https://github.com/OschAI/VisioFirm}.

