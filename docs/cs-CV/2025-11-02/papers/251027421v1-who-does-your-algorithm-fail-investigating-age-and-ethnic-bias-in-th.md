---
layout: default
title: Who Does Your Algorithm Fail? Investigating Age and Ethnic Bias in the MAMA-MIA Dataset
---

# Who Does Your Algorithm Fail? Investigating Age and Ethnic Bias in the MAMA-MIA Dataset

**arXiv**: [2510.27421v1](https://arxiv.org/abs/2510.27421) | [PDF](https://arxiv.org/pdf/2510.27421.pdf)

**作者**: Aditya Parikh, Sneha Das, Aasa Feragen

---

## 💡 一句话要点

**评估MAMA-MIA数据集在年龄和种族上的分割偏见，揭示年轻患者的内在偏见**

**关键词**: `图像分割偏见` `医疗公平性` `年龄偏见` `种族偏见` `数据集审计` `乳腺癌诊断`

## 📋 核心要点

1. 核心问题：深度学习分割模型在乳腺癌肿瘤分割中可能存在年龄和种族偏见，影响医疗公平性。
2. 方法要点：审计MAMA-MIA数据集自动分割标签的公平性，分析年龄、种族和数据源的影响。
3. 实验或效果：发现年轻患者存在内在年龄偏见，且多数据源聚合影响种族偏见，强调细粒度分析必要性。

## 📄 摘要（原文）

> Deep learning models aim to improve diagnostic workflows, but fairness
> evaluation remains underexplored beyond classification, e.g., in image
> segmentation. Unaddressed segmentation bias can lead to disparities in the
> quality of care for certain populations, potentially compounded across clinical
> decision points and amplified through iterative model development. Here, we
> audit the fairness of the automated segmentation labels provided in the breast
> cancer tumor segmentation dataset MAMA-MIA. We evaluate automated segmentation
> quality across age, ethnicity, and data source. Our analysis reveals an
> intrinsic age-related bias against younger patients that continues to persist
> even after controlling for confounding factors, such as data source. We
> hypothesize that this bias may be linked to physiological factors, a known
> challenge for both radiologists and automated systems. Finally, we show how
> aggregating data from multiple data sources influences site-specific ethnic
> biases, underscoring the necessity of investigating data at a granular level.

