---
layout: default
title: An Anatomy Aware Hybrid Deep Learning Framework for Lung Cancer Tumor Stage Classification
---

# An Anatomy Aware Hybrid Deep Learning Framework for Lung Cancer Tumor Stage Classification

**arXiv**: [2511.19367v1](https://arxiv.org/abs/2511.19367) | [PDF](https://arxiv.org/pdf/2511.19367.pdf)

**作者**: Saniah Kayenat Chowdhury, Rusab Sarmun, Muhammad E. H. Chowdhury, Sohaib Bassam Zoghoul, Israa Al-Hashimi, Adam Mushtak, Amith Khandakar

---

## 💡 一句话要点

**提出基于解剖感知的混合深度学习框架，用于肺癌肿瘤分期分类。**

**关键词**: `肺癌分期` `解剖分割` `混合深度学习` `规则分类` `医学影像分析`

## 📋 核心要点

1. 核心问题：端到端深度学习方法常忽略肿瘤-淋巴结-转移系统的空间和解剖信息，影响分期准确性。
2. 方法要点：使用编码器-解码器网络分割解剖结构，提取肿瘤尺寸和距离属性，结合规则进行分期。
3. 实验或效果：在Lung-PET-CT-Dx数据集上达到91.36%准确率，各阶段F1分数为0.93至0.96。

## 📄 摘要（原文）

> Accurate lung cancer tumor staging is crucial for prognosis and treatment planning. However, it remains challenging for end-to-end deep learning approaches, as such approaches often overlook spatial and anatomical information that are central to the tumor-node-metastasis system. The tumor stage depends on multiple quantitative criteria, including the tumor size and its proximity to the nearest anatomical structures, and small variations can alter the staging outcome. We propose a medically grounded hybrid pipeline that performs staging by explicitly measuring the tumor's size and distance properties rather than treating it as a pure image classification task. Our method employs specialized encoder-decoder networks to precisely segment the lung and adjacent anatomy, including the lobes, tumor, mediastinum, and diaphragm. Subsequently, we extract the necessary tumor properties, i.e. measure the largest tumor dimension and calculate the distance between the tumor and neighboring anatomical structures by a quantitative analysis of the segmentation masks. Finally, we apply rule-based tumor staging aligned with the medical guidelines. This novel framework has been evaluated on the Lung-PET-CT-Dx dataset, demonstrating superior performance compared to traditional deep learning models, achieving an overall classification accuracy of 91.36%. We report the per-stage F1-scores of 0.93 (T1), 0.89 (T2), 0.96 (T3), and 0.90 (T4), a critical evaluation aspect often omitted in prior literature. To our knowledge, this is the first study that embeds explicit clinical context into tumor stage classification. Unlike standard convolutional neural networks that operate in an uninterpretable "black box" manner, our method offers both state-of-the-art performance and transparent decision support.

