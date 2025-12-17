---
layout: default
title: 4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos
---

# 4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos

**arXiv**: [2511.05229v1](https://arxiv.org/abs/2511.05229) | [PDF](https://arxiv.org/pdf/2511.05229.pdf)

**作者**: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee

---

## 💡 一句话要点

**提出4D3R框架以解决单目视频动态场景的位姿未知新视图合成问题**

**关键词**: `动态神经渲染` `运动感知优化` `高斯溅射` `单目视频重建` `位姿估计`

## 📋 核心要点

1. 核心问题：单目视频动态场景中未知相机位姿的新视图合成仍具挑战性
2. 方法要点：通过两阶段解耦静态与动态组件，结合运动感知优化模块
3. 实验或效果：在真实动态数据集上PSNR提升达1.8dB，计算成本降低5倍

## 📄 摘要（原文）

> Novel view synthesis from monocular videos of dynamic scenes with unknown
> camera poses remains a fundamental challenge in computer vision and graphics.
> While recent advances in 3D representations such as Neural Radiance Fields
> (NeRF) and 3D Gaussian Splatting (3DGS) have shown promising results for static
> scenes, they struggle with dynamic content and typically rely on pre-computed
> camera poses. We present 4D3R, a pose-free dynamic neural rendering framework
> that decouples static and dynamic components through a two-stage approach. Our
> method first leverages 3D foundational models for initial pose and geometry
> estimation, followed by motion-aware refinement. 4D3R introduces two key
> technical innovations: (1) a motion-aware bundle adjustment (MA-BA) module that
> combines transformer-based learned priors with SAM2 for robust dynamic object
> segmentation, enabling more accurate camera pose refinement; and (2) an
> efficient Motion-Aware Gaussian Splatting (MA-GS) representation that uses
> control points with a deformation field MLP and linear blend skinning to model
> dynamic motion, significantly reducing computational cost while maintaining
> high-quality reconstruction. Extensive experiments on real-world dynamic
> datasets demonstrate that our approach achieves up to 1.8dB PSNR improvement
> over state-of-the-art methods, particularly in challenging scenarios with large
> dynamic objects, while reducing computational requirements by 5x compared to
> previous dynamic scene representations.

