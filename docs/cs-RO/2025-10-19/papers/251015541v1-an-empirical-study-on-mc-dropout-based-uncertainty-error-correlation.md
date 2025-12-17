---
layout: default
title: An Empirical Study on MC Dropout--Based Uncertainty--Error Correlation in 2D Brain Tumor Segmentation
---

# An Empirical Study on MC Dropout--Based Uncertainty--Error Correlation in 2D Brain Tumor Segmentation

**arXiv**: [2510.15541v1](https://arxiv.org/abs/2510.15541) | [PDF](https://arxiv.org/pdf/2510.15541.pdf)

**作者**: Saumya B

---

## 💡 一句话要点

**实证研究MC Dropout不确定性在2D脑肿瘤分割中与误差的相关性**

**关键词**: `脑肿瘤分割` `MC Dropout` `不确定性估计` `医学图像分析` `U-Net模型` `相关性分析`

## 📋 核心要点

1. 核心问题：MC Dropout不确定性是否能有效识别脑肿瘤MRI分割错误，尤其在边界区域。
2. 方法要点：使用U-Net模型，在四种数据增强设置下计算不确定性，并与像素误差进行相关性分析。
3. 实验效果：全局相关性弱，边界相关性可忽略，表明MC Dropout对边界误差定位有限。

## 📄 摘要（原文）

> Accurate brain tumor segmentation from MRI is vital for diagnosis and
> treatment planning. Although Monte Carlo (MC) Dropout is widely used to
> estimate model uncertainty, its effectiveness in identifying segmentation
> errors -- especially near tumor boundaries -- remains unclear. This study
> empirically examines the relationship between MC Dropout--based uncertainty and
> segmentation error in 2D brain tumor MRI segmentation using a U-Net trained
> under four augmentation settings: none, horizontal flip, rotation, and scaling.
> Uncertainty was computed from 50 stochastic forward passes and correlated with
> pixel-wise errors using Pearson and Spearman coefficients. Results show weak
> global correlations ($r \approx 0.30$--$0.38$) and negligible boundary
> correlations ($\|r\| < 0.05$). Although differences across augmentations were
> statistically significant ($p < 0.001$), they lacked practical relevance. These
> findings suggest that MC Dropout uncertainty provides limited cues for boundary
> error localization, underscoring the need for alternative or hybrid uncertainty
> estimation methods in medical image segmentation.

