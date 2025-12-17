---
layout: default
title: Mono4DGS-HDR: High Dynamic Range 4D Gaussian Splatting from Alternating-exposure Monocular Videos
---

# Mono4DGS-HDR: High Dynamic Range 4D Gaussian Splatting from Alternating-exposure Monocular Videos

**arXiv**: [2510.18489v1](https://arxiv.org/abs/2510.18489) | [PDF](https://arxiv.org/pdf/2510.18489.pdf)

**作者**: Jinfeng Liu, Lingtong Kong, Mi Zhou, Jinwen Chen, Dan Xu

---

## 💡 一句话要点

**提出Mono4DGS-HDR以从交替曝光单目视频重建4D高动态范围场景**

**关键词**: `4D高斯泼溅` `高动态范围重建` `单目视频处理` `交替曝光` `无位姿重建` `两阶段优化`

## 📋 核心要点

1. 核心问题：从无位姿单目低动态范围视频重建可渲染4D高动态范围场景。
2. 方法要点：采用两阶段优化框架，基于高斯泼溅，无需相机位姿。
3. 实验或效果：在公开数据集上构建基准，渲染质量和速度显著优于现有方法。

## 📄 摘要（原文）

> We introduce Mono4DGS-HDR, the first system for reconstructing renderable 4D
> high dynamic range (HDR) scenes from unposed monocular low dynamic range (LDR)
> videos captured with alternating exposures. To tackle such a challenging
> problem, we present a unified framework with two-stage optimization approach
> based on Gaussian Splatting. The first stage learns a video HDR Gaussian
> representation in orthographic camera coordinate space, eliminating the need
> for camera poses and enabling robust initial HDR video reconstruction. The
> second stage transforms video Gaussians into world space and jointly refines
> the world Gaussians with camera poses. Furthermore, we propose a temporal
> luminance regularization strategy to enhance the temporal consistency of the
> HDR appearance. Since our task has not been studied before, we construct a new
> evaluation benchmark using publicly available datasets for HDR video
> reconstruction. Extensive experiments demonstrate that Mono4DGS-HDR
> significantly outperforms alternative solutions adapted from state-of-the-art
> methods in both rendering quality and speed.

