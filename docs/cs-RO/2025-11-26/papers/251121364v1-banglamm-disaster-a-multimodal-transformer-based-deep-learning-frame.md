---
layout: default
title: BanglaMM-Disaster: A Multimodal Transformer-Based Deep Learning Framework for Multiclass Disaster Classification in Bangla
---

# BanglaMM-Disaster: A Multimodal Transformer-Based Deep Learning Framework for Multiclass Disaster Classification in Bangla

**arXiv**: [2511.21364v1](https://arxiv.org/abs/2511.21364) | [PDF](https://arxiv.org/pdf/2511.21364.pdf)

**作者**: Ariful Islam, Md Rifat Hossen, Md. Mahmudul Arif, Abdullah Al Noman, Md Arifur Rahman

---

## 💡 一句话要点

**提出BanglaMM-Disaster多模态框架，用于孟加拉语社交媒体灾难分类。**

**关键词**: `多模态学习` `灾难分类` `Transformer模型` `孟加拉语处理` `早期融合` `社交媒体分析`

## 📋 核心要点

1. 核心问题：孟加拉国自然灾害频发，需实时监测与快速响应系统。
2. 方法要点：融合Transformer文本编码器与CNN视觉骨干，采用早期融合处理多模态数据。
3. 实验或效果：最佳模型准确率达83.76%，优于单模态基线，减少误分类。

## 📄 摘要（原文）

> Natural disasters remain a major challenge for Bangladesh, so real-time monitoring and quick response systems are essential. In this study, we present BanglaMM-Disaster, an end-to-end deep learning-based multimodal framework for disaster classification in Bangla, using both textual and visual data from social media. We constructed a new dataset of 5,037 Bangla social media posts, each consisting of a caption and a corresponding image, annotated into one of nine disaster-related categories. The proposed model integrates transformer-based text encoders, including BanglaBERT, mBERT, and XLM-RoBERTa, with CNN backbones such as ResNet50, DenseNet169, and MobileNetV2, to process the two modalities. Using early fusion, the best model achieves 83.76% accuracy. This surpasses the best text-only baseline by 3.84% and the image-only baseline by 16.91%. Our analysis also shows reduced misclassification across all classes, with noticeable improvements for ambiguous examples. This work fills a key gap in Bangla multimodal disaster analysis and demonstrates the benefits of combining multiple data types for real-time disaster response in low-resource settings.

