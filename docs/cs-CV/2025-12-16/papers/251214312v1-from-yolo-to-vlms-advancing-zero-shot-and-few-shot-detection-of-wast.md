---
layout: default
title: From YOLO to VLMs: Advancing Zero-Shot and Few-Shot Detection of Wastewater Treatment Plants Using Satellite Imagery in MENA Region
---

# From YOLO to VLMs: Advancing Zero-Shot and Few-Shot Detection of Wastewater Treatment Plants Using Satellite Imagery in MENA Region

**arXiv**: [2512.14312v1](https://arxiv.org/abs/2512.14312) | [PDF](https://arxiv.org/pdf/2512.14312.pdf)

**作者**: Akila Premarathna, Kanishka Hewageegana, Garcia Andarcia Mariangel

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: 9 pages, 9 figures

---

## 💡 一句话要点

**提出基于视觉语言模型的零样本与少样本方法，以替代YOLOv8实现中东和北非地区废水处理厂的卫星图像高效检测。**

**关键词**: `视觉语言模型` `零样本检测` `少样本学习` `卫星图像分析` `废水处理厂识别` `遥感应用` `中东和北非地区` `环境监测`

## 📋 核心要点

1. 核心问题：传统YOLOv8方法依赖大量人工标注，成本高且难以适应中东和北非地区废水处理厂的快速检测需求。
2. 方法要点：采用视觉语言模型进行零样本和少样本检测，利用专家提示识别废水处理厂组件，减少对标注数据的依赖。
3. 实验或效果：多个VLM在零样本评估中超越YOLOv8真阳性率，Gemma-3表现最佳，验证了VLM的高效性和可扩展性。

## 📝 摘要（中文）

在中东和北非地区，废水处理厂对可持续水资源管理至关重要，从卫星图像中精确识别这些设施有助于环境监测。传统方法如YOLOv8分割需要大量人工标注，但研究表明视觉语言模型通过其内在推理和标注能力，能实现同等或更优效果，是一种高效替代方案。本研究提出了一种结构化的VLM比较方法，分为零样本和少样本两个流程，专门用于识别废水处理厂。YOLOv8在来自埃及、沙特阿拉伯和阿联酋的83,566张高分辨率卫星图像政府数据集上训练，其中约85%为废水处理厂（正样本），15%为非废水处理厂（负样本）。评估的VLM包括LLaMA 3.2 Vision、Qwen 2.5 VL、DeepSeek-VL2、Gemma 3、Gemini和Pixtral 12B（Mistral），用于识别废水处理厂组件如圆形/矩形储罐、曝气池，并通过专家提示区分混淆物，生成包含置信度和描述的JSON输出。数据集包含1,207个已验证的废水处理厂位置（198个阿联酋、354个沙特阿拉伯、655个埃及）以及来自现场/AI数据的同等数量的非废水处理厂站点，作为600米×600米的Geo-TIFF图像（缩放级别18，EPSG:4326）。在废水处理厂图像上的零样本评估显示，多个VLM的性能超过了YOLOv8的真阳性率，其中Gemma-3最高。结果证实，VLM特别是零样本方法，可以替代YOLOv8实现高效、无需标注的废水处理厂分类，从而支持可扩展的遥感应用。

## 🔬 方法详解

论文提出一种结构化方法，比较多种视觉语言模型在零样本和少样本设置下的性能。整体框架包括：使用YOLOv8作为基线模型，在包含83,566张高分辨率卫星图像的数据集上训练；同时评估LLaMA 3.2 Vision、Qwen 2.5 VL等VLM，通过专家提示引导模型识别废水处理厂组件（如圆形/矩形储罐、曝气池）并区分混淆物，输出JSON格式结果。关键技术创新点在于将VLM应用于卫星图像中的废水处理厂检测，结合零样本和少样本策略，减少对标注数据的依赖。与现有方法的主要区别是：传统方法如YOLOv8需要大量手动标注，而VLM利用其内在推理能力，在无需或仅需少量标注的情况下实现高效检测，提高了方法的灵活性和可扩展性。

## 📊 实验亮点

在零样本评估中，多个视觉语言模型（如Gemma-3）的真阳性率超过YOLOv8，最高性能模型实现了更高效的废水处理厂分类。这证实了VLM作为标注免费替代方案的可行性，显著提升了检测速度和可扩展性。

## 🎯 应用场景

该研究可应用于中东和北非地区的环境监测和水资源管理，通过卫星图像自动检测废水处理厂，支持可持续城市规划和灾害响应。潜在价值包括降低人工标注成本、提升遥感数据分析效率，并为全球类似区域提供可复制的技术方案。

## 📄 摘要（原文）

> In regions of the Middle East and North Africa (MENA), there is a high demand for wastewater treatment plants (WWTPs), crucial for sustainable water management. Precise identification of WWTPs from satellite images enables environmental monitoring. Traditional methods like YOLOv8 segmentation require extensive manual labeling. But studies indicate that vision-language models (VLMs) are an efficient alternative to achieving equivalent or superior results through inherent reasoning and annotation. This study presents a structured methodology for VLM comparison, divided into zero-shot and few-shot streams specifically to identify WWTPs. The YOLOv8 was trained on a governmental dataset of 83,566 high-resolution satellite images from Egypt, Saudi Arabia, and UAE: ~85% WWTPs (positives), 15% non-WWTPs (negatives). Evaluated VLMs include LLaMA 3.2 Vision, Qwen 2.5 VL, DeepSeek-VL2, Gemma 3, Gemini, and Pixtral 12B (Mistral), used to identify WWTP components such as circular/rectangular tanks, aeration basins and distinguish confounders via expert prompts producing JSON outputs with confidence and descriptions. The dataset comprises 1,207 validated WWTP locations (198 UAE, 354 KSA, 655 Egypt) and equal non-WWTP sites from field/AI data, as 600mx600m Geo-TIFF images (Zoom 18, EPSG:4326). Zero-shot evaluations on WWTP images showed several VLMs out-performing YOLOv8's true positive rate, with Gemma-3 highest. Results confirm that VLMs, particularly with zero-shot, can replace YOLOv8 for efficient, annotation-free WWTP classification, enabling scalable remote sensing.

