---
layout: default
title: Explicit Memory through Online 3D Gaussian Splatting Improves Class-Agnostic Video Segmentation
---

# Explicit Memory through Online 3D Gaussian Splatting Improves Class-Agnostic Video Segmentation

**arXiv**: [2510.23521v1](https://arxiv.org/abs/2510.23521) | [PDF](https://arxiv.org/pdf/2510.23521.pdf)

**作者**: Anthony Opipari, Aravindhan K Krishnan, Shreekant Gayaka, Min Sun, Cheng-Hao Kuo, Arnie Sen, Odest Chadwicke Jenkins

---

## 💡 一句话要点

**提出在线3D高斯泼溅显式记忆以提升类无关视频分割的准确性与一致性**

**关键词**: `视频分割` `3D高斯泼溅` `显式记忆` `类无关分割` `在线学习`

## 📋 核心要点

1. 现有视频分割算法缺乏对象级显式记忆，导致预测不一致。
2. 开发在线3D高斯泼溅技术存储对象片段，并融合FastSAM和SAM2模型。
3. 实验验证显式记忆优于无记忆或隐式记忆，提升分割准确性和一致性。

## 📄 摘要（原文）

> Remembering where object segments were predicted in the past is useful for
> improving the accuracy and consistency of class-agnostic video segmentation
> algorithms. Existing video segmentation algorithms typically use either no
> object-level memory (e.g. FastSAM) or they use implicit memories in the form of
> recurrent neural network features (e.g. SAM2). In this paper, we augment both
> types of segmentation models using an explicit 3D memory and show that the
> resulting models have more accurate and consistent predictions. For this, we
> develop an online 3D Gaussian Splatting (3DGS) technique to store predicted
> object-level segments generated throughout the duration of a video. Based on
> this 3DGS representation, a set of fusion techniques are developed, named
> FastSAM-Splat and SAM2-Splat, that use the explicit 3DGS memory to improve
> their respective foundation models' predictions. Ablation experiments are used
> to validate the proposed techniques' design and hyperparameter settings.
> Results from both real-world and simulated benchmarking experiments show that
> models which use explicit 3D memories result in more accurate and consistent
> predictions than those which use no memory or only implicit neural network
> memories. Project Page: https://topipari.com/projects/FastSAM-Splat/

