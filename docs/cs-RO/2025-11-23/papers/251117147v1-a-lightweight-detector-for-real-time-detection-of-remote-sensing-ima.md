---
layout: default
title: A lightweight detector for real-time detection of remote sensing images
---

# A lightweight detector for real-time detection of remote sensing images

**arXiv**: [2511.17147v1](https://arxiv.org/abs/2511.17147) | [PDF](https://arxiv.org/pdf/2511.17147.pdf)

**作者**: Qianyi Wang, Guoqiang Ren

---

## 💡 一句话要点

**提出DMG-YOLO轻量检测器以解决遥感图像小目标实时检测问题**

**关键词**: `遥感图像检测` `轻量检测器` `小目标检测` `实时检测` `特征融合`

## 📋 核心要点

1. 遥感图像小目标检测与实时性平衡是核心挑战
2. 采用双分支特征提取与全局局部融合模块提升检测性能
3. 在VisDrone2019等数据集上实现高mAP与轻量模型

## 📄 摘要（原文）

> Remote sensing imagery is widely used across various fields, yet real-time detection remains challenging due to the prevalence of small objects and the need to balance accuracy with efficiency. To address this, we propose DMG-YOLO, a lightweight real-time detector tailored for small object detection in remote sensing images. Specifically, we design a Dual-branch Feature Extraction (DFE) module in the backbone, which partitions feature maps into two parallel branches: one extracts local features via depthwise separable convolutions, and the other captures global context using a vision transformer with a gating mechanism. Additionally, a Multi-scale Feature Fusion (MFF) module with dilated convolutions enhances multi-scale integration while preserving fine details. In the neck, we introduce the Global and Local Aggregate Feature Pyramid Network (GLAFPN) to further boost small object detection through global-local feature fusion. Extensive experiments on the VisDrone2019 and NWPU VHR-10 datasets show that DMG-YOLO achieves competitive performance in terms of mAP, model size, and other key metrics.

