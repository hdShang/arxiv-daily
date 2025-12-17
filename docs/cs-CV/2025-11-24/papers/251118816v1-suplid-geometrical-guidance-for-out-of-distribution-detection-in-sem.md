---
layout: default
title: SupLID: Geometrical Guidance for Out-of-Distribution Detection in Semantic Segmentation
---

# SupLID: Geometrical Guidance for Out-of-Distribution Detection in Semantic Segmentation

**arXiv**: [2511.18816v1](https://arxiv.org/abs/2511.18816) | [PDF](https://arxiv.org/pdf/2511.18816.pdf)

**作者**: Nimeshika Udayangani, Sarah Erfani, Christopher Leckie

---

## 💡 一句话要点

**提出SupLID框架，利用几何结构增强语义分割中的分布外检测**

**关键词**: `语义分割` `分布外检测` `几何结构` `超像素处理` `后处理评分`

## 📋 核心要点

1. 核心问题：语义分割中像素级分布外检测易受分类器过度自信影响
2. 方法要点：构建几何核心集，在超像素级别计算分布外分数
3. 实验或效果：显著提升现有方法性能，在AUR等指标上达到最优

## 📄 摘要（原文）

> Out-of-Distribution (OOD) detection in semantic segmentation aims to localize anomalous regions at the pixel level, advancing beyond traditional image-level OOD techniques to better suit real-world applications such as autonomous driving. Recent literature has successfully explored the adaptation of commonly used image-level OOD methods--primarily based on classifier-derived confidence scores (e.g., energy or entropy)--for this pixel-precise task. However, these methods inherit a set of limitations, including vulnerability to overconfidence. In this work, we introduce SupLID, a novel framework that effectively guides classifier-derived OOD scores by exploiting the geometrical structure of the underlying semantic space, particularly using Linear Intrinsic Dimensionality (LID). While LID effectively characterizes the local structure of high-dimensional data by analyzing distance distributions, its direct application at the pixel level remains challenging. To overcome this, SupLID constructs a geometrical coreset that captures the intrinsic structure of the in-distribution (ID) subspace. It then computes OOD scores at the superpixel level, enabling both efficient real-time inference and improved spatial smoothness. We demonstrate that geometrical cues derived from SupLID serve as a complementary signal to traditional classifier confidence, enhancing the model's ability to detect diverse OOD scenarios. Designed as a post-hoc scoring method, SupLID can be seamlessly integrated with any semantic segmentation classifier at deployment time. Our results demonstrate that SupLID significantly enhances existing classifier-based OOD scores, achieving state-of-the-art performance across key evaluation metrics, including AUR, FPR, and AUP. Code is available at https://github.com/hdnugit/SupLID.

