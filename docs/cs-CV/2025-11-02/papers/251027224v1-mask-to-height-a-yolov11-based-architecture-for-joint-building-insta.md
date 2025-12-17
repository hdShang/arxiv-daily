---
layout: default
title: Mask-to-Height: A YOLOv11-Based Architecture for Joint Building Instance Segmentation and Height Classification from Satellite Imagery
---

# Mask-to-Height: A YOLOv11-Based Architecture for Joint Building Instance Segmentation and Height Classification from Satellite Imagery

**arXiv**: [2510.27224v1](https://arxiv.org/abs/2510.27224) | [PDF](https://arxiv.org/pdf/2510.27224.pdf)

**作者**: Mahmoud El Hussieni, Bahadır K. Güntürk, Hasan F. Ateş, Oğuz Hanoğlu

---

## 💡 一句话要点

**提出基于YOLOv11的联合建筑实例分割与高度分类方法，用于卫星图像城市建模**

**关键词**: `建筑实例分割` `高度分类` `YOLOv11` `卫星图像` `城市建模` `多任务学习`

## 📋 核心要点

1. 核心问题：卫星图像中建筑实例分割与高度分类对城市规划至关重要
2. 方法要点：YOLOv11改进多尺度特征融合，提升定位精度与复杂场景处理
3. 实验或效果：在DFC2023数据集上实现60.4% mAP@50，优于先前多任务框架

## 📄 摘要（原文）

> Accurate building instance segmentation and height classification are
> critical for urban planning, 3D city modeling, and infrastructure monitoring.
> This paper presents a detailed analysis of YOLOv11, the recent advancement in
> the YOLO series of deep learning models, focusing on its application to joint
> building extraction and discrete height classification from satellite imagery.
> YOLOv11 builds on the strengths of earlier YOLO models by introducing a more
> efficient architecture that better combines features at different scales,
> improves object localization accuracy, and enhances performance in complex
> urban scenes. Using the DFC2023 Track 2 dataset -- which includes over 125,000
> annotated buildings across 12 cities -- we evaluate YOLOv11's performance using
> metrics such as precision, recall, F1 score, and mean average precision (mAP).
> Our findings demonstrate that YOLOv11 achieves strong instance segmentation
> performance with 60.4\% mAP@50 and 38.3\% mAP@50--95 while maintaining robust
> classification accuracy across five predefined height tiers. The model excels
> in handling occlusions, complex building shapes, and class imbalance,
> particularly for rare high-rise structures. Comparative analysis confirms that
> YOLOv11 outperforms earlier multitask frameworks in both detection accuracy and
> inference speed, making it well-suited for real-time, large-scale urban
> mapping. This research highlights YOLOv11's potential to advance semantic urban
> reconstruction through streamlined categorical height modeling, offering
> actionable insights for future developments in remote sensing and geospatial
> intelligence.

