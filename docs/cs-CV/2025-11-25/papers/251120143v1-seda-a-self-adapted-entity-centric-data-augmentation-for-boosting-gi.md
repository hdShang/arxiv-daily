---
layout: default
title: SEDA: A Self-Adapted Entity-Centric Data Augmentation for Boosting Gird-based Discontinuous NER Models
---

# SEDA: A Self-Adapted Entity-Centric Data Augmentation for Boosting Gird-based Discontinuous NER Models

**arXiv**: [2511.20143v1](https://arxiv.org/abs/2511.20143) | [PDF](https://arxiv.org/pdf/2511.20143.pdf)

**作者**: Wen-Fang Su, Hsiao-Wei Chou, Wen-Yang Lin

---

## 💡 一句话要点

**提出自适应实体中心数据增强方法，提升基于网格的非连续命名实体识别模型性能**

**关键词**: `命名实体识别` `非连续实体` `网格标记方法` `数据增强` `自然语言处理`

## 📋 核心要点

1. 核心问题：传统文本分割方法难以处理跨句非连续实体，导致识别准确率下降。
2. 方法要点：将图像数据增强技术（如裁剪、缩放、填充）集成到网格标记模型中。
3. 实验效果：在多个数据集上，整体F1分数提升1-2.5%，非连续实体提升3.7-8.4%。

## 📄 摘要（原文）

> Named Entity Recognition (NER) is a critical task in natural language processing, yet it remains particularly challenging for discontinuous entities. The primary difficulty lies in text segmentation, as traditional methods often missegment or entirely miss cross-sentence discontinuous entities, significantly affecting recognition accuracy. Therefore, we aim to address the segmentation and omission issues associated with such entities. Recent studies have shown that grid-tagging methods are effective for information extraction due to their flexible tagging schemes and robust architectures. Building on this, we integrate image data augmentation techniques, such as cropping, scaling, and padding, into grid-based models to enhance their ability to recognize discontinuous entities and handle segmentation challenges. Experimental results demonstrate that traditional segmentation methods often fail to capture cross-sentence discontinuous entities, leading to decreased performance. In contrast, our augmented grid models achieve notable improvements. Evaluations on the CADEC, ShARe13, and ShARe14 datasets show F1 score gains of 1-2.5% overall and 3.7-8.4% for discontinuous entities, confirming the effectiveness of our approach.

