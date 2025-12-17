---
layout: default
title: MetaDCSeg: Robust Medical Image Segmentation via Meta Dynamic Center Weighting
---

# MetaDCSeg: Robust Medical Image Segmentation via Meta Dynamic Center Weighting

**arXiv**: [2511.18894v1](https://arxiv.org/abs/2511.18894) | [PDF](https://arxiv.org/pdf/2511.18894.pdf)

**作者**: Chenyu Mu, Guihai Chen, Xun Yang, Erkun Yang, Cheng Deng

---

## 💡 一句话要点

**提出MetaDCSeg以解决医学图像分割中噪声标注和模糊边界问题**

**关键词**: `医学图像分割` `噪声标注处理` `边界不确定性建模` `动态中心加权` `元学习框架`

## 📋 核心要点

1. 核心问题：医学图像分割易受噪声标注和模糊边界干扰，导致模型训练不稳定
2. 方法要点：通过动态中心距离机制学习像素级权重，抑制噪声并聚焦边界区域
3. 实验或效果：在多个基准数据集上优于现有方法，提升分割性能

## 📄 摘要（原文）

> Medical image segmentation is crucial for clinical applications, but it is frequently disrupted by noisy annotations and ambiguous anatomical boundaries, which lead to instability in model training. Existing methods typically rely on global noise assumptions or confidence-based sample selection, which inadequately mitigate the performance degradation caused by annotation noise, especially in challenging boundary regions. To address this issue, we propose MetaDCSeg, a robust framework that dynamically learns optimal pixel-wise weights to suppress the influence of noisy ground-truth labels while preserving reliable annotations. By explicitly modeling boundary uncertainty through a Dynamic Center Distance (DCD) mechanism, our approach utilizes weighted feature distances for foreground, background, and boundary centers, directing the model's attention toward hard-to-segment pixels near ambiguous boundaries. This strategy enables more precise handling of structural boundaries, which are often overlooked by existing methods, and significantly enhances segmentation performance. Extensive experiments across four benchmark datasets with varying noise levels demonstrate that MetaDCSeg consistently outperforms existing state-of-the-art methods.

