---
layout: default
title: K-Stain: Keypoint-Driven Correspondence for H&E-to-IHC Virtual Staining
---

# K-Stain: Keypoint-Driven Correspondence for H&E-to-IHC Virtual Staining

**arXiv**: [2511.06709v1](https://arxiv.org/abs/2511.06709) | [PDF](https://arxiv.org/pdf/2511.06709.pdf)

**作者**: Sicheng Yang, Zhaohu Xing, Haipeng Zhou, Lei Zhu

---

## 💡 一句话要点

**提出K-Stain框架，利用关键点解决H&E到IHC虚拟染色中的空间对齐问题**

**关键词**: `虚拟染色` `关键点检测` `图像生成` `空间对齐` `组织病理学`

## 📋 核心要点

1. 核心问题：现有方法因组织切片错位难以有效利用空间信息，影响虚拟染色准确性
2. 方法要点：引入关键点驱动空间对应，结合HSKD、KEG和KGD组件提升图像生成保真度
3. 实验或效果：实验显示K-Stain在定量指标和视觉质量上优于现有先进方法

## 📄 摘要（原文）

> Virtual staining offers a promising method for converting Hematoxylin and
> Eosin (H&E) images into Immunohistochemical (IHC) images, eliminating the need
> for costly chemical processes. However, existing methods often struggle to
> utilize spatial information effectively due to misalignment in tissue slices.
> To overcome this challenge, we leverage keypoints as robust indicators of
> spatial correspondence, enabling more precise alignment and integration of
> structural details in synthesized IHC images. We introduce K-Stain, a novel
> framework that employs keypoint-based spatial and semantic relationships to
> enhance synthesized IHC image fidelity. K-Stain comprises three main
> components: (1) a Hierarchical Spatial Keypoint Detector (HSKD) for identifying
> keypoints in stain images, (2) a Keypoint-aware Enhancement Generator (KEG)
> that integrates these keypoints during image generation, and (3) a Keypoint
> Guided Discriminator (KGD) that improves the discriminator's sensitivity to
> spatial details. Our approach leverages contextual information from adjacent
> slices, resulting in more accurate and visually consistent IHC images.
> Extensive experiments show that K-Stain outperforms state-of-the-art methods in
> quantitative metrics and visual quality.

