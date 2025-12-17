---
layout: default
title: Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts
---

# Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts

**arXiv**: [2511.10300v1](https://arxiv.org/abs/2511.10300) | [PDF](https://arxiv.org/pdf/2511.10300.pdf)

**作者**: Sumin Lee, Sungwon Park, Jeasurk Yang, Jihee Kim, Meeyoung Cha

---

## 💡 一句话要点

**提出GRAM框架以解决卫星图像贫民窟检测的泛化性问题**

**关键词**: `卫星图像分割` `贫民窟检测` `混合专家模型` `测试时适应` `泛化学习` `城市贫困估计`

## 📋 核心要点

1. 核心问题：贫民窟形态异质性导致模型难以泛化到未见区域。
2. 方法要点：使用混合专家架构捕获区域特征，测试时适应过滤不可靠伪标签。
3. 实验或效果：在非洲城市等低资源场景中优于现有方法，实现标签高效映射。

## 📄 摘要（原文）

> Satellite-based slum segmentation holds significant promise in generating global estimates of urban poverty. However, the morphological heterogeneity of informal settlements presents a major challenge, hindering the ability of models trained on specific regions to generalize effectively to unseen locations. To address this, we introduce a large-scale high-resolution dataset and propose GRAM (Generalized Region-Aware Mixture-of-Experts), a two-phase test-time adaptation framework that enables robust slum segmentation without requiring labeled data from target regions. We compile a million-scale satellite imagery dataset from 12 cities across four continents for source training. Using this dataset, the model employs a Mixture-of-Experts architecture to capture region-specific slum characteristics while learning universal features through a shared backbone. During adaptation, prediction consistency across experts filters out unreliable pseudo-labels, allowing the model to generalize effectively to previously unseen regions. GRAM outperforms state-of-the-art baselines in low-resource settings such as African cities, offering a scalable and label-efficient solution for global slum mapping and data-driven urban planning.

