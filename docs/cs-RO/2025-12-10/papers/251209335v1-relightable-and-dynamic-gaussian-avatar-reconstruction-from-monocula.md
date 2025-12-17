---
layout: default
title: Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video
---

# Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video

**arXiv**: [2512.09335v1](https://arxiv.org/abs/2512.09335) | [PDF](https://arxiv.org/pdf/2512.09335.pdf)

**作者**: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee

---

## 💡 一句话要点

**提出RnD-Avatar框架，基于3D高斯泼溅重建可重光照和动态的人体化身，以解决单目视频中几何细节不足的问题。**

**关键词**: `人体化身重建` `3D高斯泼溅` `动态蒙皮权重` `可重光照渲染` `单目视频建模` `几何细节优化`

## 📋 核心要点

1. 核心问题：现有方法因几何细节不足（如衣物褶皱）导致重建效果不真实。
2. 方法要点：引入动态蒙皮权重和正则化，以捕捉姿态变化和精细几何细节。
3. 实验或效果：在合成新视角、新姿态和重光照任务中达到先进性能。

## 📄 摘要（原文）

> Modeling relightable and animatable human avatars from monocular video is a long-standing and challenging task. Recently, Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) methods have been employed to reconstruct the avatars. However, they often produce unsatisfactory photo-realistic results because of insufficient geometrical details related to body motion, such as clothing wrinkles. In this paper, we propose a 3DGS-based human avatar modeling framework, termed as Relightable and Dynamic Gaussian Avatar (RnD-Avatar), that presents accurate pose-variant deformation for high-fidelity geometrical details. To achieve this, we introduce dynamic skinning weights that define the human avatar's articulation based on pose while also learning additional deformations induced by body motion. We also introduce a novel regularization to capture fine geometric details under sparse visual cues. Furthermore, we present a new multi-view dataset with varied lighting conditions to evaluate relight. Our framework enables realistic rendering of novel poses and views while supporting photo-realistic lighting effects under arbitrary lighting conditions. Our method achieves state-of-the-art performance in novel view synthesis, novel pose rendering, and relighting.

