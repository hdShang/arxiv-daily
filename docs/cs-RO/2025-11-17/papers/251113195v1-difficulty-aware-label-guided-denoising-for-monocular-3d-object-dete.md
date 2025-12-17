---
layout: default
title: Difficulty-Aware Label-Guided Denoising for Monocular 3D Object Detection
---

# Difficulty-Aware Label-Guided Denoising for Monocular 3D Object Detection

**arXiv**: [2511.13195v1](https://arxiv.org/abs/2511.13195) | [PDF](https://arxiv.org/pdf/2511.13195.pdf)

**作者**: Soyul Lee, Seungmin Baek, Dongbo Min

---

## 💡 一句话要点

**提出MonoDLGD框架以解决单目3D检测中深度估计不准和实例难度忽略问题**

**关键词**: `单目3D物体检测` `难度感知学习` `标签去噪` `几何监督` `KITTI基准`

## 📋 核心要点

1. 核心问题：单目3D检测因深度模糊和忽略实例难度（如遮挡、距离）导致性能不佳
2. 方法要点：基于检测不确定性自适应扰动和重建标签，提供显式几何监督
3. 实验或效果：在KITTI基准上实现所有难度级别的先进性能

## 📄 摘要（原文）

> Monocular 3D object detection is a cost-effective solution for applications like autonomous driving and robotics, but remains fundamentally ill-posed due to inherently ambiguous depth cues. Recent DETR-based methods attempt to mitigate this through global attention and auxiliary depth prediction, yet they still struggle with inaccurate depth estimates. Moreover, these methods often overlook instance-level detection difficulty, such as occlusion, distance, and truncation, leading to suboptimal detection performance. We propose MonoDLGD, a novel Difficulty-Aware Label-Guided Denoising framework that adaptively perturbs and reconstructs ground-truth labels based on detection uncertainty. Specifically, MonoDLGD applies stronger perturbations to easier instances and weaker ones into harder cases, and then reconstructs them to effectively provide explicit geometric supervision. By jointly optimizing label reconstruction and 3D object detection, MonoDLGD encourages geometry-aware representation learning and improves robustness to varying levels of object complexity. Extensive experiments on the KITTI benchmark demonstrate that MonoDLGD achieves state-of-the-art performance across all difficulty levels.

