---
layout: default
title: TR-Gaussians: High-fidelity Real-time Rendering of Planar Transmission and Reflection with 3D Gaussian Splatting
---

# TR-Gaussians: High-fidelity Real-time Rendering of Planar Transmission and Reflection with 3D Gaussian Splatting

**arXiv**: [2511.13009v1](https://arxiv.org/abs/2511.13009) | [PDF](https://arxiv.org/pdf/2511.13009.pdf)

**作者**: Yong Liu, Keyang Ye, Tianjia Shao, Kun Zhou

---

## 💡 一句话要点

**提出TR-Gaussians以高保真实时渲染室内场景中的平面透射和反射**

**关键词**: `3D高斯渲染` `平面反射` `实时渲染` `新视角合成` `室内场景`

## 📋 核心要点

1. 核心问题：室内场景中平面透射和反射的高保真渲染难以实时实现
2. 方法要点：结合3D高斯与可学习反射平面，通过Fresnel权重混合透射和反射组件
3. 实验或效果：在多个数据集上实现实时高保真新视角合成，优于现有方法

## 📄 摘要（原文）

> We propose Transmission-Reflection Gaussians (TR-Gaussians), a novel 3D-Gaussian-based representation for high-fidelity rendering of planar transmission and reflection, which are ubiquitous in indoor scenes. Our method combines 3D Gaussians with learnable reflection planes that explicitly model the glass planes with view-dependent reflectance strengths. Real scenes and transmission components are modeled by 3D Gaussians and the reflection components are modeled by the mirrored Gaussians with respect to the reflection plane. The transmission and reflection components are blended according to a Fresnel-based, view-dependent weighting scheme, allowing for faithful synthesis of complex appearance effects under varying viewpoints. To effectively optimize TR-Gaussians, we develop a multi-stage optimization framework incorporating color and geometry constraints and an opacity perturbation mechanism. Experiments on different datasets demonstrate that TR-Gaussians achieve real-time, high-fidelity novel view synthesis in scenes with planar transmission and reflection, and outperform state-of-the-art approaches both quantitatively and qualitatively.

