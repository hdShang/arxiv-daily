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

**提出基于视觉语言模型的零样本与少样本方法，以解决中东和北非地区废水处理厂卫星图像检测中标注成本高的问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `视觉语言模型` `零样本检测` `少样本学习` `卫星图像分析` `废水处理厂识别` `遥感应用` `中东和北非地区` `环境监测`

## 📋 核心要点

1. 核心问题：传统YOLOv8方法依赖大量人工标注，成本高且难以适应中东和北非地区废水处理厂的快速检测需求。
2. 方法要点：采用视觉语言模型进行零样本和少样本检测，利用专家提示识别废水处理厂组件，减少标注依赖。
3. 实验或效果：多个VLM在零样本评估中真阳性率超越YOLOv8，Gemma-3表现最优，验证了VLM的高效性。

## 📝 摘要（中文）

在中东和北亚地区，废水处理厂对可持续水资源管理至关重要，从卫星图像中精确识别这些设施有助于环境监测。传统方法如YOLOv8分割需要大量人工标注，但研究表明视觉语言模型通过其内在推理和标注能力，能高效实现同等或更优结果。本研究提出了一种结构化的VLM比较方法，分为零样本和少样本流程，专门用于识别废水处理厂。YOLOv8在来自埃及、沙特阿拉伯和阿联酋的83,566张高分辨率卫星图像政府数据集上训练，其中约85%为废水处理厂（正样本），15%为非废水处理厂（负样本）。评估的VLM包括LLaMA 3.2 Vision、Qwen 2.5 VL、DeepSeek-VL2、Gemma 3、Gemini和Pixtral 12B（Mistral），用于识别废水处理厂组件如圆形/矩形罐、曝气池，并通过专家提示区分混淆物，生成带有置信度和描述的JSON输出。数据集包含1,207个已验证的废水处理厂位置（198个阿联酋、354个沙特阿拉伯、655个埃及）和等量的非废水处理厂站点，来自现场/AI数据，作为600米×600米的Geo-TIFF图像（缩放级别18，EPSG:4326）。在废水处理厂图像上的零样本评估显示，多个VLM在真阳性率上优于YOLOv8，其中Gemma-3表现最佳。结果证实，VLM特别是零样本方法，可以替代YOLOv8进行高效、无需标注的废水处理厂分类，实现可扩展的遥感应用。

## 🔬 方法详解

论文提出一种结构化方法，比较视觉语言模型在废水处理厂检测中的性能。整体框架包括零样本和少样本两个流程：零样本直接使用预训练VLM进行推理，少样本则可能涉及少量标注数据微调。关键技术创新在于利用专家设计的提示词，引导VLM识别废水处理厂特定组件（如圆形/矩形罐、曝气池）并区分混淆物，输出结构化JSON结果。与现有方法的主要区别在于，传统YOLOv8依赖全监督训练和大量标注，而VLM通过其多模态理解能力，实现无需或少量标注的检测，显著降低人工成本。

## 📊 实验亮点

在零样本评估中，多个视觉语言模型（如Gemma-3）的真阳性率超过YOLOv8，最高性能模型实现高效检测，验证了VLM在无需标注情况下替代传统方法的潜力，提升遥感应用的可扩展性。

## 🎯 应用场景

该研究可应用于中东和北非地区的环境监测和城市规划，通过卫星图像自动检测废水处理厂，支持可持续水资源管理和基础设施评估，具有远程、高效、可扩展的优势。

## 📄 摘要（原文）

> In regions of the Middle East and North Africa (MENA), there is a high demand for wastewater treatment plants (WWTPs), crucial for sustainable water management. Precise identification of WWTPs from satellite images enables environmental monitoring. Traditional methods like YOLOv8 segmentation require extensive manual labeling. But studies indicate that vision-language models (VLMs) are an efficient alternative to achieving equivalent or superior results through inherent reasoning and annotation. This study presents a structured methodology for VLM comparison, divided into zero-shot and few-shot streams specifically to identify WWTPs. The YOLOv8 was trained on a governmental dataset of 83,566 high-resolution satellite images from Egypt, Saudi Arabia, and UAE: ~85% WWTPs (positives), 15% non-WWTPs (negatives). Evaluated VLMs include LLaMA 3.2 Vision, Qwen 2.5 VL, DeepSeek-VL2, Gemma 3, Gemini, and Pixtral 12B (Mistral), used to identify WWTP components such as circular/rectangular tanks, aeration basins and distinguish confounders via expert prompts producing JSON outputs with confidence and descriptions. The dataset comprises 1,207 validated WWTP locations (198 UAE, 354 KSA, 655 Egypt) and equal non-WWTP sites from field/AI data, as 600mx600m Geo-TIFF images (Zoom 18, EPSG:4326). Zero-shot evaluations on WWTP images showed several VLMs out-performing YOLOv8's true positive rate, with Gemma-3 highest. Results confirm that VLMs, particularly with zero-shot, can replace YOLOv8 for efficient, annotation-free WWTP classification, enabling scalable remote sensing.

