---
layout: default
title: Dual-Stream Spectral Decoupling Distillation for Remote Sensing Object Detection
---

# Dual-Stream Spectral Decoupling Distillation for Remote Sensing Object Detection

**arXiv**: [2512.04413v1](https://arxiv.org/abs/2512.04413) | [PDF](https://arxiv.org/pdf/2512.04413.pdf)

**作者**: Xiangyi Gao, Danpei Zhao, Bo Yuan, Wentao Li

---

## 💡 一句话要点

**提出双流谱解耦蒸馏方法以解决遥感目标检测中的特征混淆问题**

**关键词**: `遥感目标检测` `知识蒸馏` `谱分解` `特征解耦` `轻量化模型` `双流网络`

## 📋 核心要点

1. 核心问题：遥感图像特征混合与细微特征差异导致知识蒸馏中的知识混淆
2. 方法要点：基于谱分解整合显隐式蒸馏，设计密度无关尺度权重和全频/高频放大器
3. 实验或效果：在DIOR和DOTA数据集上验证，提升RetinaNet和Faster R-CNN的AP50约4%

## 📄 摘要（原文）

> Knowledge distillation is an effective and hardware-friendly method, which plays a key role in lightweighting remote sensing object detection. However, existing distillation methods often encounter the issue of mixed features in remote sensing images (RSIs), and neglect the discrepancies caused by subtle feature variations, leading to entangled knowledge confusion. To address these challenges, we propose an architecture-agnostic distillation method named Dual-Stream Spectral Decoupling Distillation (DS2D2) for universal remote sensing object detection tasks. Specifically, DS2D2 integrates explicit and implicit distillation grounded in spectral decomposition. Firstly, the first-order wavelet transform is applied for spectral decomposition to preserve the critical spatial characteristics of RSIs. Leveraging this spatial preservation, a Density-Independent Scale Weight (DISW) is designed to address the challenges of dense and small object detection common in RSIs. Secondly, we show implicit knowledge hidden in subtle student-teacher feature discrepancies, which significantly influence predictions when activated by detection heads. This implicit knowledge is extracted via full-frequency and high-frequency amplifiers, which map feature differences to prediction deviations. Extensive experiments on DIOR and DOTA datasets validate the effectiveness of the proposed method. Specifically, on DIOR dataset, DS2D2 achieves improvements of 4.2% in AP50 for RetinaNet and 3.8% in AP50 for Faster R-CNN, outperforming existing distillation approaches. The source code will be available at https://github.com/PolarAid/DS2D2.

