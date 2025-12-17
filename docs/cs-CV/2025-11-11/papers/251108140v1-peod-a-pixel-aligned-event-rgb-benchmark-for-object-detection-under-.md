---
layout: default
title: PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection under Challenging Conditions
---

# PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection under Challenging Conditions

**arXiv**: [2511.08140v1](https://arxiv.org/abs/2511.08140) | [PDF](https://arxiv.org/pdf/2511.08140.pdf)

**作者**: Luoping Cui, Hanqing Liu, Mingjie Liu, Endian Lin, Donghong Jiang, Yuhao Wang, Chuang Zhu

---

## 💡 一句话要点

**提出PEOD数据集以解决挑战条件下事件-RGB目标检测的基准不足问题**

**关键词**: `事件相机` `目标检测` `多模态融合` `挑战条件` `高分辨率数据集`

## 📋 核心要点

1. 现有事件-RGB数据集覆盖极端条件稀疏且分辨率低，阻碍鲁棒检测评估
2. 构建首个大规模像素对齐高分辨率事件-RGB数据集，含130+序列和34万标注框
3. 基准测试显示融合模型在正常条件下优，事件模型在光照挑战下领先融合模型

## 📄 摘要（原文）

> Robust object detection for challenging scenarios increasingly relies on event cameras, yet existing Event-RGB datasets remain constrained by sparse coverage of extreme conditions and low spatial resolution (<= 640 x 480), which prevents comprehensive evaluation of detectors under challenging scenarios. To address these limitations, we propose PEOD, the first large-scale, pixel-aligned and high-resolution (1280 x 720) Event-RGB dataset for object detection under challenge conditions. PEOD contains 130+ spatiotemporal-aligned sequences and 340k manual bounding boxes, with 57% of data captured under low-light, overexposure, and high-speed motion. Furthermore, we benchmark 14 methods across three input configurations (Event-based, RGB-based, and Event-RGB fusion) on PEOD. On the full test set and normal subset, fusion-based models achieve the excellent performance. However, in illumination challenge subset, the top event-based model outperforms all fusion models, while fusion models still outperform their RGB-based counterparts, indicating limits of existing fusion methods when the frame modality is severely degraded. PEOD establishes a realistic, high-quality benchmark for multimodal perception and facilitates future research.

