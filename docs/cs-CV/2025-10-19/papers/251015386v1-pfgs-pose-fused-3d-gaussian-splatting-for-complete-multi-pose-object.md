---
layout: default
title: PFGS: Pose-Fused 3D Gaussian Splatting for Complete Multi-Pose Object Reconstruction
---

# PFGS: Pose-Fused 3D Gaussian Splatting for Complete Multi-Pose Object Reconstruction

**arXiv**: [2510.15386v1](https://arxiv.org/abs/2510.15386) | [PDF](https://arxiv.org/pdf/2510.15386.pdf)

**作者**: Ting-Yu Yen, Yu-Sheng Chiu, Shih-Hsuan Hung, Peter Wonka, Hung-Kuo Chu

---

## 💡 一句话要点

**提出PFGS框架以解决多姿态物体完整重建问题**

**关键词**: `3D高斯泼溅` `多姿态重建` `姿态感知融合` `跨姿态配准` `完整物体重建`

## 📋 核心要点

1. 核心问题：现有3D高斯泼溅方法假设物体单姿态，导致重建不完整。
2. 方法要点：通过姿态感知融合策略，迭代整合辅助姿态到主姿态统一表示。
3. 实验或效果：在定性和定量评估中优于基线，生成更完整高保真模型。

## 📄 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have enabled high-quality,
> real-time novel-view synthesis from multi-view images. However, most existing
> methods assume the object is captured in a single, static pose, resulting in
> incomplete reconstructions that miss occluded or self-occluded regions. We
> introduce PFGS, a pose-aware 3DGS framework that addresses the practical
> challenge of reconstructing complete objects from multi-pose image captures.
> Given images of an object in one main pose and several auxiliary poses, PFGS
> iteratively fuses each auxiliary set into a unified 3DGS representation of the
> main pose. Our pose-aware fusion strategy combines global and local
> registration to merge views effectively and refine the 3DGS model. While recent
> advances in 3D foundation models have improved registration robustness and
> efficiency, they remain limited by high memory demands and suboptimal accuracy.
> PFGS overcomes these challenges by incorporating them more intelligently into
> the registration process: it leverages background features for per-pose camera
> pose estimation and employs foundation models for cross-pose registration. This
> design captures the best of both approaches while resolving background
> inconsistency issues. Experimental results demonstrate that PFGS consistently
> outperforms strong baselines in both qualitative and quantitative evaluations,
> producing more complete reconstructions and higher-fidelity 3DGS models.

