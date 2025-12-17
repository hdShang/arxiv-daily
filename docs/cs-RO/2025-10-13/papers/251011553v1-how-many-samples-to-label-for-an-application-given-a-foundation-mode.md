---
layout: default
title: How many samples to label for an application given a foundation model? Chest X-ray classification study
---

# How many samples to label for an application given a foundation model? Chest X-ray classification study

**arXiv**: [2510.11553v1](https://arxiv.org/abs/2510.11553) | [PDF](https://arxiv.org/pdf/2510.11553.pdf)

**作者**: Nikolay Nechaev, Evgenia Przhezdzetskaya, Viktor Gombolevskiy, Dmitry Umerenkov, Dmitry Dylov

---

## 💡 一句话要点

**提出基于幂律拟合的方法，预测胸片分类中基础模型所需标注样本数，以最小化标注成本。**

**关键词**: `胸片分类` `基础模型` `样本需求预测` `幂律拟合` `ROC-AUC` `标注成本优化`

## 📋 核心要点

1. 核心问题：胸片分类依赖大量标注数据，基础模型下所需样本数未知。
2. 方法要点：使用幂律拟合预测训练集大小，以达成特定ROC-AUC阈值。
3. 实验或效果：XrayCLIP和XraySigLIP在少量样本下优于ResNet-50，50例即可预测性能。

## 📄 摘要（原文）

> Chest X-ray classification is vital yet resource-intensive, typically
> demanding extensive annotated data for accurate diagnosis. Foundation models
> mitigate this reliance, but how many labeled samples are required remains
> unclear. We systematically evaluate the use of power-law fits to predict the
> training size necessary for specific ROC-AUC thresholds. Testing multiple
> pathologies and foundation models, we find XrayCLIP and XraySigLIP achieve
> strong performance with significantly fewer labeled examples than a ResNet-50
> baseline. Importantly, learning curve slopes from just 50 labeled cases
> accurately forecast final performance plateaus. Our results enable
> practitioners to minimize annotation costs by labeling only the essential
> samples for targeted performance.

