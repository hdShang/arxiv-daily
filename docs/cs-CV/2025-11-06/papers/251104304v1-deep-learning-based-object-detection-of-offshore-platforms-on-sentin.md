---
layout: default
title: Deep learning-based object detection of offshore platforms on Sentinel-1 Imagery and the impact of synthetic training data
---

# Deep learning-based object detection of offshore platforms on Sentinel-1 Imagery and the impact of synthetic training data

**arXiv**: [2511.04304v1](https://arxiv.org/abs/2511.04304) | [PDF](https://arxiv.org/pdf/2511.04304.pdf)

**作者**: Robin Spanier, Thorsten Hoeser, Claudia Kuenzer

---

## 💡 一句话要点

**提出结合合成与真实数据的YOLOv10模型，提升Sentinel-1图像中海上平台检测性能。**

**关键词**: `海上平台检测` `合成数据增强` `YOLOv10模型` `Sentinel-1图像` `地理可迁移性`

## 📋 核心要点

1. 核心问题：海上基础设施监测中，样本稀缺导致模型性能不足，尤其对少数类对象。
2. 方法要点：使用合成与真实Sentinel-1图像训练YOLOv10模型，评估地理可迁移性。
3. 实验或效果：模型在未见区域检测3529个平台，F1分数从0.85提升至0.90。

## 📄 摘要（原文）

> The recent and ongoing expansion of marine infrastructure, including offshore
> wind farms, oil and gas platforms, artificial islands, and aquaculture
> facilities, highlights the need for effective monitoring systems. The
> development of robust models for offshore infrastructure detection relies on
> comprehensive, balanced datasets, but falls short when samples are scarce,
> particularly for underrepresented object classes, shapes, and sizes. By
> training deep learning-based YOLOv10 object detection models with a combination
> of synthetic and real Sentinel-1 satellite imagery acquired in the fourth
> quarter of 2023 from four regions (Caspian Sea, South China Sea, Gulf of
> Guinea, and Coast of Brazil), this study investigates the use of synthetic
> training data to enhance model performance. We evaluated this approach by
> applying the model to detect offshore platforms in three unseen regions (Gulf
> of Mexico, North Sea, Persian Gulf) and thereby assess geographic
> transferability. This region-holdout evaluation demonstrated that the model
> generalises beyond the training areas. In total, 3,529 offshore platforms were
> detected, including 411 in the North Sea, 1,519 in the Gulf of Mexico, and
> 1,593 in the Persian Gulf. The model achieved an F1 score of 0.85, which
> improved to 0.90 upon incorporating synthetic data. We analysed how synthetic
> data enhances the representation of unbalanced classes and overall model
> performance, taking a first step toward globally transferable detection of
> offshore infrastructure. This study underscores the importance of balanced
> datasets and highlights synthetic data generation as an effective strategy to
> address common challenges in remote sensing, demonstrating the potential of
> deep learning for scalable, global offshore infrastructure monitoring.

