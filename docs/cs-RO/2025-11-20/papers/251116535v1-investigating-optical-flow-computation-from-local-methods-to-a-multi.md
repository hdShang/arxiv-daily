---
layout: default
title: Investigating Optical Flow Computation: From Local Methods to a Multiresolution Horn-Schunck Implementation with Bilinear Interpolation
---

# Investigating Optical Flow Computation: From Local Methods to a Multiresolution Horn-Schunck Implementation with Bilinear Interpolation

**arXiv**: [2511.16535v1](https://arxiv.org/abs/2511.16535) | [PDF](https://arxiv.org/pdf/2511.16535.pdf)

**作者**: Haytham Ziani

---

## 💡 一句话要点

**实现多分辨率Horn-Schunck算法，结合双线性插值以提升光流估计精度**

**关键词**: `光流计算` `Horn-Schunck算法` `多分辨率方法` `双线性插值` `运动估计`

## 📋 核心要点

1. 核心问题：光流计算在图像条件变化下的运动估计准确性不足
2. 方法要点：比较局部与全局方法，实现多分辨率Horn-Schunck算法
3. 实验或效果：使用双线性插值和延长操作改进收敛与精度

## 📄 摘要（原文）

> This paper presents an applied analysis of local and global methods, with a focus on the Horn-Schunck algorithm for optical flow computation. We explore the theoretical and practical aspects of local approaches, such as the Lucas-Kanade method, and global techniques such as Horn-Schunck. Additionally, we implement a multiresolution version of the Horn-Schunck algorithm, using bilinear interpolation and prolongation to improve accuracy and convergence. The study investigates the effectiveness of these combined strategies in estimating motion between frames, particularly under varying image conditions.

