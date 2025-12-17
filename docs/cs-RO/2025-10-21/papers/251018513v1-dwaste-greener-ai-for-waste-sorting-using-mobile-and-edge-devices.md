---
layout: default
title: DWaste: Greener AI for Waste Sorting using Mobile and Edge Devices
---

# DWaste: Greener AI for Waste Sorting using Mobile and Edge Devices

**arXiv**: [2510.18513v1](https://arxiv.org/abs/2510.18513) | [PDF](https://arxiv.org/pdf/2510.18513.pdf)

**作者**: Suman Kunwar

---

## 💡 一句话要点

**提出DWaste平台，利用计算机视觉在移动和边缘设备上实现实时垃圾分类。**

**关键词**: `垃圾分类` `计算机视觉` `边缘计算` `模型量化` `实时推理`

## 📋 核心要点

1. 核心问题：便利包装导致大量垃圾，需高效分类以支持可持续废物管理。
2. 方法要点：开发DWaste平台，集成图像分类和物体检测模型，支持离线实时处理。
3. 实验或效果：轻量检测模型在精度、速度和碳排放间取得平衡，量化优化效率。

## 📄 摘要（原文）

> The rise of convenience packaging has led to generation of enormous waste,
> making efficient waste sorting crucial for sustainable waste management. To
> address this, we developed DWaste, a computer vision-powered platform designed
> for real-time waste sorting on resource-constrained smartphones and edge
> devices, including offline functionality. We benchmarked various image
> classification models (EfficientNetV2S/M, ResNet50/101, MobileNet) and object
> detection (YOLOv8n, YOLOv11n) using a subset of our own waste data set and
> annotated it using the custom tool Annotated Lab. We found a clear trade-off
> between accuracy and resource consumption: the best classifier,
> EfficientNetV2S, achieved high accuracy (~ 96%) but suffered from high latency
> (~ 0.22s) and elevated carbon emissions. In contrast, lightweight object
> detection models delivered strong performance (up to 77% mAP) with ultra-fast
> inference (~ 0.03s) and significantly smaller model sizes (< 7MB), making them
> ideal for real-time, low-power use. Model quantization further maximized
> efficiency, substantially reducing model size and VRAM usage by up to 75%. Our
> work demonstrates the successful implementation of "Greener AI" models to
> support real-time, sustainable waste sorting on edge devices.

