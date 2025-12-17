---
layout: default
title: Systematic Evaluation of Preprocessing Techniques for Accurate Image Registration in Digital Pathology
---

# Systematic Evaluation of Preprocessing Techniques for Accurate Image Registration in Digital Pathology

**arXiv**: [2511.04171v1](https://arxiv.org/abs/2511.04171) | [PDF](https://arxiv.org/pdf/2511.04171.pdf)

**作者**: Fatemehzahra Darzi, Rodrigo Escobar Diaz Guerrero, Thomas Bocklitz

---

## 💡 一句话要点

**评估颜色变换技术以提升数字病理学中多模态图像配准精度**

**关键词**: `图像配准` `数字病理学` `颜色变换` `多模态图像` `配准误差评估`

## 📋 核心要点

1. 核心问题：多模态图像配准在数字病理学中因颜色差异影响对齐准确性。
2. 方法要点：比较CycleGAN等颜色变换方法，结合VALIS配准评估配准误差。
3. 实验或效果：CycleGAN在两种场景下均实现最低配准误差，优于其他方法。

## 📄 摘要（原文）

> Image registration refers to the process of spatially aligning two or more
> images by mapping them into a common coordinate system, so that corresponding
> anatomical or tissue structures are matched across images. In digital
> pathology, registration enables direct comparison and integration of
> information from different stains or imaging modalities, sup-porting
> applications such as biomarker analysis and tissue reconstruction. Accurate
> registration of images from different modalities is an essential step in
> digital pathology. In this study, we investigated how various color
> transformation techniques affect image registration between hematoxylin and
> eosin (H&E) stained images and non-linear multimodal images. We used a dataset
> of 20 tissue sample pairs, with each pair undergoing several preprocessing
> steps, including different color transformation (CycleGAN, Macenko, Reinhard,
> Vahadane), inversion, contrast adjustment, intensity normalization, and
> denoising. All images were registered using the VALIS registration method,
> which first applies rigid registration and then performs non-rigid registration
> in two steps on both low and high-resolution images. Registration performance
> was evaluated using the relative Target Registration Error (rTRE). We reported
> the median of median rTRE values (MMrTRE) and the average of median rTRE values
> (AMrTRE) for each method. In addition, we performed a custom point-based
> evaluation using ten manually selected key points. Registration was done
> separately for two scenarios, using either the original or inverted multimodal
> images. In both scenarios, CycleGAN color transformation achieved the lowest
> registration errors, while the other methods showed higher errors. These
> findings show that applying color transformation before registration improves
> alignment between images from different modalities and supports more reliable
> analysis in digital pathology.

