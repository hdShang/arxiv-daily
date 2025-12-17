---
layout: default
title: GeoDiffMM: Geometry-Guided Conditional Diffusion for Motion Magnification
---

# GeoDiffMM: Geometry-Guided Conditional Diffusion for Motion Magnification

**arXiv**: [2512.08325v1](https://arxiv.org/abs/2512.08325) | [PDF](https://arxiv.org/pdf/2512.08325.pdf)

**作者**: Xuedeng Liu, Jiabao Guo, Zheng Zhang, Fei Wang, Zhi Liu, Dan Guo

---

## 💡 一句话要点

**提出GeoDiffMM，一种基于扩散的拉格朗日视频运动放大框架，利用光流作为几何先验以提升放大效果。**

**关键词**: `视频运动放大` `扩散模型` `光流引导` `拉格朗日方法` `几何先验`

## 📋 核心要点

1. 核心问题：现有欧拉方法在微小位移下难以分离光子噪声与真实微运动，导致放大噪声。
2. 方法要点：设计无噪声光流增强策略和扩散运动放大器，以光流为条件选择性放大结构一致的运动。
3. 实验或效果：在真实和合成数据集上优于先进方法，显著改善运动放大质量。

## 📄 摘要（原文）

> Video Motion Magnification (VMM) amplifies subtle macroscopic motions to a perceptible level. Recently, existing mainstream Eulerian approaches address amplification-induced noise via decoupling representation learning such as texture, shape and frequancey schemes, but they still struggle to separate photon noise from true micro-motion when motion displacements are very small. We propose GeoDiffMM, a novel diffusion-based Lagrangian VMM framework conditioned on optical flow as a geometric cue, enabling structurally consistent motion magnification. Specifically, we design a Noise-free Optical Flow Augmentation strategy that synthesizes diverse nonrigid motion fields without photon noise as supervision, helping the model learn more accurate geometry-aware optial flow and generalize better. Next, we develop a Diffusion Motion Magnifier that conditions the denoising process on (i) optical flow as a geometry prior and (ii) a learnable magnification factor controlling magnitude, thereby selectively amplifying motion components consistent with scene semantics and structure while suppressing content-irrelevant perturbations. Finally, we perform Flow-based Video Synthesis to map the amplified motion back to the image domain with high fidelity. Extensive experiments on real and synthetic datasets show that GeoDiffMM outperforms state-of-the-art methods and significantly improves motion magnification.

