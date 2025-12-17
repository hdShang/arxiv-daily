---
layout: default
title: Scene Coordinate Reconstruction Priors
---

# Scene Coordinate Reconstruction Priors

**arXiv**: [2510.12387v1](https://arxiv.org/abs/2510.12387) | [PDF](https://arxiv.org/pdf/2510.12387.pdf)

**作者**: Wenjing Bian, Axel Barroso-Laguna, Tommaso Cavallari, Victor Adrian Prisacariu, Eric Brachmann

---

## 💡 一句话要点

**提出场景坐标重建先验以提升SCR模型在训练图像不足时的性能**

**关键词**: `场景坐标回归` `重建先验` `点云扩散模型` `视觉重定位` `室内场景` `多视角约束`

## 📋 核心要点

1. 核心问题：SCR模型在训练图像多视角约束不足时退化，导致场景表示不准确
2. 方法要点：引入概率重解释，融合深度分布和点云扩散先验，优化预测场景点
3. 实验或效果：在室内数据集上提升点云一致性、注册率和相机位姿，改善下游任务

## 📄 摘要（原文）

> Scene coordinate regression (SCR) models have proven to be powerful implicit
> scene representations for 3D vision, enabling visual relocalization and
> structure-from-motion. SCR models are trained specifically for one scene. If
> training images imply insufficient multi-view constraints SCR models
> degenerate. We present a probabilistic reinterpretation of training SCR models,
> which allows us to infuse high-level reconstruction priors. We investigate
> multiple such priors, ranging from simple priors over the distribution of
> reconstructed depth values to learned priors over plausible scene coordinate
> configurations. For the latter, we train a 3D point cloud diffusion model on a
> large corpus of indoor scans. Our priors push predicted 3D scene points towards
> plausible geometry at each training step to increase their likelihood. On three
> indoor datasets our priors help learning better scene representations,
> resulting in more coherent scene point clouds, higher registration rates and
> better camera poses, with a positive effect on down-stream tasks such as novel
> view synthesis and camera relocalization.

