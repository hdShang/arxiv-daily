---
layout: default
title: Delving into Cascaded Instability: A Lipschitz Continuity View on Image Restoration and Object Detection Synergy
---

# Delving into Cascaded Instability: A Lipschitz Continuity View on Image Restoration and Object Detection Synergy

**arXiv**: [2510.24232v1](https://arxiv.org/abs/2510.24232) | [PDF](https://arxiv.org/pdf/2510.24232.pdf)

**作者**: Qing Zhao, Weijian Deng, Pengxu Wei, ZiYi Dong, Hannan Lu, Xiangyang Ji, Liang Lin

---

## 💡 一句话要点

**提出Lipschitz正则化目标检测框架以解决图像恢复与检测集成中的不稳定性问题**

**关键词**: `图像恢复` `目标检测` `Lipschitz连续性` `级联框架` `YOLO检测器` `稳定性优化`

## 📋 核心要点

1. 核心问题：图像恢复与目标检测网络功能不匹配导致级联不稳定性，放大微小扰动影响检测
2. 方法要点：通过Lipschitz连续性分析，提出LROD框架，将恢复集成到检测特征学习中
3. 实验或效果：在雾霾和低光基准测试中，LR-YOLO提升检测稳定性、优化平滑性和准确率

## 📄 摘要（原文）

> To improve detection robustness in adverse conditions (e.g., haze and low
> light), image restoration is commonly applied as a pre-processing step to
> enhance image quality for the detector. However, the functional mismatch
> between restoration and detection networks can introduce instability and hinder
> effective integration -- an issue that remains underexplored. We revisit this
> limitation through the lens of Lipschitz continuity, analyzing the functional
> differences between restoration and detection networks in both the input space
> and the parameter space. Our analysis shows that restoration networks perform
> smooth, continuous transformations, while object detectors operate with
> discontinuous decision boundaries, making them highly sensitive to minor
> perturbations. This mismatch introduces instability in traditional cascade
> frameworks, where even imperceptible noise from restoration is amplified during
> detection, disrupting gradient flow and hindering optimization. To address
> this, we propose Lipschitz-regularized object detection (LROD), a simple yet
> effective framework that integrates image restoration directly into the
> detector's feature learning, harmonizing the Lipschitz continuity of both tasks
> during training. We implement this framework as Lipschitz-regularized YOLO
> (LR-YOLO), extending seamlessly to existing YOLO detectors. Extensive
> experiments on haze and low-light benchmarks demonstrate that LR-YOLO
> consistently improves detection stability, optimization smoothness, and overall
> accuracy.

