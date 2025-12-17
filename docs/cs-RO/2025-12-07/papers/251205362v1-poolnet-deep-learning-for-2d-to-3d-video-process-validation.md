---
layout: default
title: PoolNet: Deep Learning for 2D to 3D Video Process Validation
---

# PoolNet: Deep Learning for 2D to 3D Video Process Validation

**arXiv**: [2512.05362v1](https://arxiv.org/abs/2512.05362) | [PDF](https://arxiv.org/pdf/2512.05362.pdf)

**作者**: Sanchit Kaul, Joseph Luna, Shray Arora

---

## 💡 一句话要点

**提出PoolNet框架，用于验证野外数据是否适合从2D视频重建3D结构**

**关键词**: `运动结构重建` `深度学习验证` `视频处理` `数据筛选` `计算效率`

## 📋 核心要点

1. 核心问题：从序列和非序列图像数据中提取运动结构信息耗时且计算昂贵，公开数据常因相机姿态变化不足、遮挡和噪声而不适用。
2. 方法要点：开发深度学习框架PoolNet，支持帧级和场景级验证，区分适合与不适合运动结构重建的场景。
3. 实验或效果：模型能有效筛选数据，显著缩短获取运动结构数据的时间，优于现有算法。

## 📄 摘要（原文）

> Lifting Structure-from-Motion (SfM) information from sequential and non-sequential image data is a time-consuming and computationally expensive task. In addition to this, the majority of publicly available data is unfit for processing due to inadequate camera pose variation, obscuring scene elements, and noisy data. To solve this problem, we introduce PoolNet, a versatile deep learning framework for frame-level and scene-level validation of in-the-wild data. We demonstrate that our model successfully differentiates SfM ready scenes from those unfit for processing while significantly undercutting the amount of time state of the art algorithms take to obtain structure-from-motion data.

