---
layout: default
title: MoMaps: Semantics-Aware Scene Motion Generation with Motion Maps
---

# MoMaps: Semantics-Aware Scene Motion Generation with Motion Maps

**arXiv**: [2510.11107v1](https://arxiv.org/abs/2510.11107) | [PDF](https://arxiv.org/pdf/2510.11107.pdf)

**作者**: Jiahui Lei, Kyle Genova, George Kopanas, Noah Snavely, Leonidas Guibas

---

## 💡 一句话要点

**提出MoMaps表示以从单张图像预测语义一致的3D场景运动**

**关键词**: `3D场景运动生成` `运动地图表示` `扩散模型` `视频合成` `语义运动先验`

## 📋 核心要点

1. 核心问题：从真实视频学习语义和功能有意义的3D运动先验，用于单图像预测未来运动。
2. 方法要点：引入像素对齐的MoMap表示，基于扩散模型从大规模视频数据库生成3D运动。
3. 实验或效果：生成合理且语义一致的3D场景运动，并支持2D视频合成新流程。

## 📄 摘要（原文）

> This paper addresses the challenge of learning semantically and functionally
> meaningful 3D motion priors from real-world videos, in order to enable
> prediction of future 3D scene motion from a single input image. We propose a
> novel pixel-aligned Motion Map (MoMap) representation for 3D scene motion,
> which can be generated from existing generative image models to facilitate
> efficient and effective motion prediction. To learn meaningful distributions
> over motion, we create a large-scale database of MoMaps from over 50,000 real
> videos and train a diffusion model on these representations. Our motion
> generation not only synthesizes trajectories in 3D but also suggests a new
> pipeline for 2D video synthesis: first generate a MoMap, then warp an image
> accordingly and complete the warped point-based renderings. Experimental
> results demonstrate that our approach generates plausible and semantically
> consistent 3D scene motion.

