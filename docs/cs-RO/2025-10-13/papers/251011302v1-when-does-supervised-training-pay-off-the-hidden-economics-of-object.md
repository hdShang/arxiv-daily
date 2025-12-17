---
layout: default
title: When Does Supervised Training Pay Off? The Hidden Economics of Object Detection in the Era of Vision-Language Models
---

# When Does Supervised Training Pay Off? The Hidden Economics of Object Detection in the Era of Vision-Language Models

**arXiv**: [2510.11302v1](https://arxiv.org/abs/2510.11302) | [PDF](https://arxiv.org/pdf/2510.11302.pdf)

**作者**: Samer Al-Hamadani

---

## 💡 一句话要点

**提出监督与零-shot检测的成本效益分析框架，指导架构选择**

**关键词**: `目标检测` `视觉语言模型` `成本效益分析` `监督学习` `零-shot检测`

## 📋 核心要点

1. 核心问题：监督学习与零-shot VLM在目标检测中的成本效益权衡
2. 方法要点：结合COCO和产品图像评估，建模总拥有成本
3. 实验或效果：监督YOLO准确率91.2%，零-shot Gemini 68.5%，成本优势取决于推理量

## 📄 摘要（原文）

> Object detection systems have traditionally relied on supervised learning
> with manually annotated bounding boxes, achieving high accuracy at the cost of
> substantial annotation investment. The emergence of Vision-Language Models
> (VLMs) offers an alternative paradigm enabling zero-shot detection through
> natural language queries, eliminating annotation requirements but operating
> with reduced accuracy. This paper presents the first comprehensive
> cost-effectiveness analysis comparing supervised detection (YOLO) with
> zero-shot VLM inference (Gemini Flash 2.5). Through systematic evaluation on
> 1,000 stratified COCO images and 200 diverse product images spanning consumer
> electronics and rare categories, combined with detailed Total Cost of Ownership
> modeling, we establish quantitative break-even thresholds governing
> architecture selection. Our findings reveal that supervised YOLO achieves 91.2%
> accuracy versus 68.5% for zero-shot Gemini on standard categories, representing
> a 22.7 percentage point advantage that costs $10,800 in annotation for
> 100-category systems. However, this advantage justifies investment only beyond
> 55 million inferences, equivalent to 151,000 images daily for one year.
> Zero-shot Gemini demonstrates 52.3% accuracy on diverse product categories
> (ranging from highly web-prevalent consumer electronics at 75-85% to rare
> specialized equipment at 25-40%) where supervised YOLO achieves 0% due to
> architectural constraints preventing detection of untrained classes. Cost per
> Correct Detection analysis reveals substantially lower per-detection costs for
> Gemini ($0.00050 vs $0.143) at 100,000 inferences despite accuracy deficits. We
> develop decision frameworks demonstrating that optimal architecture selection
> depends critically on deployment volume, category stability, budget
> constraints, and accuracy requirements rather than purely technical performance
> metrics.

