---
layout: default
title: "Gen-n-Val: Agentic Image Data Generation and Validation"
---

# Gen-n-Val: Agentic Image Data Generation and Validation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04676" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04676v1</a>
  <a href="https://arxiv.org/pdf/2506.04676.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04676v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04676v1', 'Gen-n-Val: Agentic Image Data Generation and Validation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing-En Huang, I-Sheng Fang, Tzuhsuan Huang, Chih-Yu Wang, Jun-Cheng Chen

**分类**: cs.CV, cs.AI, cs.LG, cs.MA

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出Gen-n-Val框架以解决计算机视觉中的数据稀缺与标签噪声问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据生成` `计算机视觉` `目标检测` `实例分割` `层扩散` `大型语言模型` `数据验证`

## 📋 核心要点

1. 现有的合成数据生成方法在处理多对象掩膜、不准确的分割和错误的类别标签等方面存在显著不足，限制了其在计算机视觉任务中的有效性。
2. Gen-n-Val框架通过引入层扩散和大型语言模型，优化生成单对象合成数据的过程，确保生成的实例掩膜精确且背景干净。
3. 与MosaicFusion等最先进的合成数据方法相比，Gen-n-Val将无效合成数据比例从50%降低至7%，并在COCO实例分割中提升了1%的mAP。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）和视觉大型语言模型（VLLMs）在多个任务中表现出色，但在计算机视觉任务中，数据稀缺和标签噪声仍然是重大挑战。为了解决这些问题，本文提出了Gen-n-Val，一个新颖的代理数据生成框架，利用层扩散（Layer Diffusion）、LLMs和VLLMs生成高质量的单对象掩膜和多样化背景。Gen-n-Val由两个代理组成：LD提示代理和数据验证代理。实验表明，与现有的合成数据方法相比，Gen-n-Val显著减少了无效合成数据，并在COCO实例分割和开放词汇目标检测基准上提高了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决计算机视觉任务中的数据稀缺和标签噪声问题，现有合成数据生成方法在生成多对象掩膜和准确性方面存在显著不足。

**核心思路**：Gen-n-Val框架通过结合层扩散、LLMs和VLLMs，优化合成数据生成过程，确保生成的单对象掩膜高质量且背景多样。

**技术框架**：Gen-n-Val由两个主要模块组成：LD提示代理和数据验证代理。LD提示代理优化生成提示以产生高质量前景图像和分割掩膜，而数据验证代理则过滤低质量合成实例图像。

**关键创新**：Gen-n-Val的核心创新在于通过优化提示生成单对象合成数据，并利用图像和谐化技术将多个实例结合在场景中，显著提高了合成数据的质量。

**关键设计**：在设计中，使用TextGrad对两个代理的提示进行精细调整，确保生成的合成数据在实例掩膜和背景方面达到高标准。

## 📊 实验亮点

实验结果显示，Gen-n-Val在COCO实例分割中将无效合成数据比例从50%降低至7%，并在稀有类别上提升了1%的mAP。此外，在开放词汇目标检测基准上，Gen-n-Val相较于YOLO-Worldv2-M提升了7.1%的mAP，显示出显著的性能改进。

## 🎯 应用场景

Gen-n-Val框架在计算机视觉领域具有广泛的应用潜力，特别是在需要大量标注数据的任务中，如目标检测和实例分割。通过生成高质量的合成数据，该框架可以有效缓解数据稀缺问题，提升模型的训练效果，未来可能在自动驾驶、智能监控等领域发挥重要作用。

## 📄 摘要（原文）

> Recently, Large Language Models (LLMs) and Vision Large Language Models (VLLMs) have demonstrated impressive performance as agents across various tasks while data scarcity and label noise remain significant challenges in computer vision tasks, such as object detection and instance segmentation. A common solution for resolving these issues is to generate synthetic data. However, current synthetic data generation methods struggle with issues, such as multiple objects per mask, inaccurate segmentation, and incorrect category labels, limiting their effectiveness. To address these issues, we introduce Gen-n-Val, a novel agentic data generation framework that leverages Layer Diffusion (LD), LLMs, and VLLMs to produce high-quality, single-object masks and diverse backgrounds. Gen-n-Val consists of two agents: (1) The LD prompt agent, an LLM, optimizes prompts for LD to generate high-quality foreground instance images and segmentation masks. These optimized prompts ensure the generation of single-object synthetic data with precise instance masks and clean backgrounds. (2) The data validation agent, a VLLM, which filters out low-quality synthetic instance images. The system prompts for both agents are refined through TextGrad. Additionally, we use image harmonization to combine multiple instances within scenes. Compared to state-of-the-art synthetic data approaches like MosaicFusion, our approach reduces invalid synthetic data from 50% to 7% and improves performance by 1% mAP on rare classes in COCO instance segmentation with YOLOv9c and YOLO11m. Furthermore, Gen-n-Val shows significant improvements (7. 1% mAP) over YOLO-Worldv2-M in open-vocabulary object detection benchmarks with YOLO11m. Moreover, Gen-n-Val improves the performance of YOLOv9 and YOLO11 families in instance segmentation and object detection.

