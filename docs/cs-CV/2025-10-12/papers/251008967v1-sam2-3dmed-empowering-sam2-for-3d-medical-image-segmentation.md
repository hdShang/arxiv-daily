---
layout: default
title: SAM2-3dMed: Empowering SAM2 for 3D Medical Image Segmentation
---

# SAM2-3dMed: Empowering SAM2 for 3D Medical Image Segmentation

**arXiv**: [2510.08967v1](https://arxiv.org/abs/2510.08967) | [PDF](https://arxiv.org/pdf/2510.08967.pdf)

**作者**: Yeqing Yang, Le Xu, Lixia Tian

---

## 💡 一句话要点

**提出SAM2-3dMed以解决3D医学图像分割中的领域差距问题**

**关键词**: `3D医学图像分割` `切片相对位置预测` `边界检测` `领域适应` `自监督学习`

## 📋 核心要点

1. 核心问题：SAM2直接应用于3D医学图像存在双向解剖连续性与视频单向时间流的差距，以及边界精确性不足。
2. 方法要点：引入切片相对位置预测模块建模双向依赖，边界检测模块增强分割精度。
3. 实验或效果：在多个医学数据集上显著优于现有方法，提升分割重叠和边界精度。

## 📄 摘要（原文）

> Accurate segmentation of 3D medical images is critical for clinical
> applications like disease assessment and treatment planning. While the Segment
> Anything Model 2 (SAM2) has shown remarkable success in video object
> segmentation by leveraging temporal cues, its direct application to 3D medical
> images faces two fundamental domain gaps: 1) the bidirectional anatomical
> continuity between slices contrasts sharply with the unidirectional temporal
> flow in videos, and 2) precise boundary delineation, crucial for morphological
> analysis, is often underexplored in video tasks. To bridge these gaps, we
> propose SAM2-3dMed, an adaptation of SAM2 for 3D medical imaging. Our framework
> introduces two key innovations: 1) a Slice Relative Position Prediction (SRPP)
> module explicitly models bidirectional inter-slice dependencies by guiding SAM2
> to predict the relative positions of different slices in a self-supervised
> manner; 2) a Boundary Detection (BD) module enhances segmentation accuracy
> along critical organ and tissue boundaries. Extensive experiments on three
> diverse medical datasets (the Lung, Spleen, and Pancreas in the Medical
> Segmentation Decathlon (MSD) dataset) demonstrate that SAM2-3dMed significantly
> outperforms state-of-the-art methods, achieving superior performance in
> segmentation overlap and boundary precision. Our approach not only advances 3D
> medical image segmentation performance but also offers a general paradigm for
> adapting video-centric foundation models to spatial volumetric data.

