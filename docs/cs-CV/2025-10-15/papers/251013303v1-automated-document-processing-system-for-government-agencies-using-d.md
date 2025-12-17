---
layout: default
title: Automated document processing system for government agencies using DBNET++ and BART models
---

# Automated document processing system for government agencies using DBNET++ and BART models

**arXiv**: [2510.13303v1](https://arxiv.org/abs/2510.13303) | [PDF](https://arxiv.org/pdf/2510.13303.pdf)

**作者**: Aya Kaysan Bahjat

---

## 💡 一句话要点

**提出基于DBNet++和BART的自动文档分类系统，用于政府机构处理多源图像文档。**

**关键词**: `文档图像处理` `文本检测` `文档分类` `DBNet++` `BART模型` `政府应用`

## 📋 核心要点

1. 核心问题：解决图像文档在变光照、任意方向、遮挡等挑战下的文本检测与分类。
2. 方法要点：采用DBNet++检测文本，BART分类文档为发票、报告、信件和表格。
3. 实验或效果：在Total-Text数据集上文本检测准确率达92.88%，适用于非约束场景。

## 📄 摘要（原文）

> An automatic document classification system is presented that detects textual
> content in images and classifies documents into four predefined categories
> (Invoice, Report, Letter, and Form). The system supports both offline images
> (e.g., files on flash drives, HDDs, microSD) and real-time capture via
> connected cameras, and is designed to mitigate practical challenges such as
> variable illumination, arbitrary orientation, curved or partially occluded
> text, low resolution, and distant text. The pipeline comprises four stages:
> image capture and preprocessing, text detection [1] using a DBNet++
> (Differentiable Binarization Network Plus) detector, and text classification
> [2] using a BART (Bidirectional and Auto-Regressive Transformers) classifier,
> all integrated within a user interface implemented in Python with PyQt5. The
> achieved results by the system for text detection in images were good at about
> 92.88% through 10 hours on Total-Text dataset that involve high resolution
> images simulate a various and very difficult challenges. The results indicate
> the proposed approach is effective for practical, mixed-source document
> categorization in unconstrained imaging scenarios.

