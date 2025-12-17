---
layout: default
title: Text images processing system using artificial intelligence models
---

# Text images processing system using artificial intelligence models

**arXiv**: [2512.11691v1](https://arxiv.org/abs/2512.11691) | [PDF](https://arxiv.org/pdf/2512.11691.pdf)

**作者**: Aya Kaysan Bahjat

---

## 💡 一句话要点

**提出基于DBNet++和BART的文本图像处理系统，用于在复杂条件下分类Invoice、Form、Letter或Report。**

**关键词**: `文本图像分类` `DBNet++` `BART模型` `复杂条件处理` `用户界面集成`

## 📋 核心要点

1. 核心问题：解决图像中文本识别与分类的挑战，如光照变化、低分辨率、文本部分覆盖等。
2. 方法要点：采用DBNet++检测文本元素，BART模型进行分类，集成Python/PyQt5用户界面。
3. 实验或效果：在Total-Text数据集上测试10小时，文本识别率约94.62%，验证了方法的有效性。

## 📄 摘要（原文）

> This is to present a text image classifier device that identifies textual content in images and then categorizes each image into one of four predefined categories, including Invoice, Form, Letter, or Report. The device supports a gallery mode, in which users browse files on flash disks, hard disk drives, or microSD cards, and a live mode which renders feeds of cameras connected to it. Its design is specifically aimed at addressing pragmatic challenges, such as changing light, random orientation, curvature or partial coverage of text, low resolution, and slightly visible text. The steps of the processing process are divided into four steps: image acquisition and preprocessing, textual elements detection with the help of DBNet++ (Differentiable Binarization Network Plus) model, BART (Bidirectional Auto-Regressive Transformers) model that classifies detected textual elements, and the presentation of the results through a user interface written in Python and PyQt5. All the stages are connected in such a way that they form a smooth workflow. The system achieved a text recognition rate of about 94.62% when tested over ten hours on the mentioned Total-Text dataset, that includes high resolution images, created so as to represent a wide range of problematic conditions. These experimental results support the effectiveness of the suggested methodology to practice, mixed-source text categorization, even in uncontrolled imaging conditions.

