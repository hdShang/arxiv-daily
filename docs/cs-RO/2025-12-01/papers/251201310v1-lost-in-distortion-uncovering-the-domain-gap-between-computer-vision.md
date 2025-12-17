---
layout: default
title: Lost in Distortion: Uncovering the Domain Gap Between Computer Vision and Brain Imaging - A Study on Pretraining for Age Prediction
---

# Lost in Distortion: Uncovering the Domain Gap Between Computer Vision and Brain Imaging - A Study on Pretraining for Age Prediction

**arXiv**: [2512.01310v1](https://arxiv.org/abs/2512.01310) | [PDF](https://arxiv.org/pdf/2512.01310.pdf)

**作者**: Yanteng Zhang, Songheng Li, Zeyu Shen, Qizhen Lan, Lipei Zhang, Yang Liu, Vince Calhoun

---

## 💡 一句话要点

**探索数据质量对脑影像预训练的影响，揭示计算机视觉与脑成像的领域差距**

**关键词**: `脑影像预训练` `数据质量影响` `脑年龄预测` `领域差距` `模型泛化`

## 📋 核心要点

1. 核心问题：脑影像数据质量异质性高，低质量扫描是否有助于预训练或阻碍学习
2. 方法要点：在不同质量水平的数据集上进行预训练，并对外部队列进行脑年龄预测微调
3. 实验或效果：结果显示不同质量水平间性能差异显著，强调领域感知数据管理的必要性

## 📄 摘要（原文）

> Large-scale brain imaging datasets provide unprecedented opportunities for developing domain foundation models through pretraining. However, unlike natural image datasets in computer vision, these neuroimaging data often exhibit high heterogeneity in quality, ranging from well-structured scans to severely distorted or incomplete brain volumes. This raises a fundamental question: can noise or low-quality scans contribute meaningfully to pretraining, or do they instead hinder model learning? In this study, we systematically explore the role of data quality level in pretraining and its impact on downstream tasks. Specifically, we perform pretraining on datasets with different quality levels and perform fine-tuning for brain age prediction on external cohorts. Our results show significant performance differences across quality levels, revealing both opportunities and limitations. We further discuss the gap between computer vision practices and clinical neuroimaging standards, emphasizing the necessity of domain-aware curation to ensure trusted and generalizable domain-specific foundation models.

