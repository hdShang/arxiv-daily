---
layout: default
title: KineDiff3D: Kinematic-Aware Diffusion for Category-Level Articulated Object Shape Reconstruction and Generation
---

# KineDiff3D: Kinematic-Aware Diffusion for Category-Level Articulated Object Shape Reconstruction and Generation

**arXiv**: [2510.17137v1](https://arxiv.org/abs/2510.17137) | [PDF](https://arxiv.org/pdf/2510.17137.pdf)

**作者**: WenBo Xu, Liu Liu, Li Zhang, Ran Zhang, Hao Wu, Dan Guo, Meng Wang

---

## 💡 一句话要点

**提出KineDiff3D以解决单视角下铰接物体形状重建与姿态估计问题**

**关键词**: `铰接物体重建` `扩散模型` `运动学感知` `3D形状生成` `姿态估计`

## 📋 核心要点

1. 铰接物体因多部件几何和关节配置导致结构多样性，重建与姿态估计困难
2. 使用KA-VAE编码几何、关节角和分割，结合扩散模型回归姿态和生成潜在码
3. 实验在合成和真实数据集验证了准确重建和运动学参数估计的有效性

## 📄 摘要（原文）

> Articulated objects, such as laptops and drawers, exhibit significant
> challenges for 3D reconstruction and pose estimation due to their multi-part
> geometries and variable joint configurations, which introduce structural
> diversity across different states. To address these challenges, we propose
> KineDiff3D: Kinematic-Aware Diffusion for Category-Level Articulated Object
> Shape Reconstruction and Generation, a unified framework for reconstructing
> diverse articulated instances and pose estimation from single view input.
> Specifically, we first encode complete geometry (SDFs), joint angles, and part
> segmentation into a structured latent space via a novel Kinematic-Aware VAE
> (KA-VAE). In addition, we employ two conditional diffusion models: one for
> regressing global pose (SE(3)) and joint parameters, and another for generating
> the kinematic-aware latent code from partial observations. Finally, we produce
> an iterative optimization module that bidirectionally refines reconstruction
> accuracy and kinematic parameters via Chamfer-distance minimization while
> preserving articulation constraints. Experimental results on synthetic,
> semi-synthetic, and real-world datasets demonstrate the effectiveness of our
> approach in accurately reconstructing articulated objects and estimating their
> kinematic properties.

