---
layout: default
title: Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere
---

# Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere

**arXiv**: [2512.14180v1](https://arxiv.org/abs/2512.14180) | [PDF](https://arxiv.org/pdf/2512.14180.pdf)

**作者**: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出球面Voronoi作为3D高斯泼溅中外观建模的统一框架，以解决球谐函数在高频信号和镜面反射方面的局限性。**

**关键词**: `球面Voronoi` `3D高斯泼溅` `外观建模` `新视角合成` `镜面反射` `可学习参数化` `辐射场方法` `真实感渲染`

## 📋 核心要点

1. 现有球谐函数在3D高斯泼溅中处理高频信号时存在吉布斯振铃伪影，且无法有效建模镜面反射，限制了真实感渲染效果。
2. 提出球面Voronoi框架，通过将方向域划分为可学习区域来参数化外观，利用平滑边界实现稳定优化，并作为反射探针处理镜面效果。
3. 在合成和真实数据集上实现最先进性能，漫反射场景优化更简单，反射建模显著优于球谐函数，验证了方法的有效性和通用性。

## 📝 摘要（中文）

辐射场方法（如3D高斯泼溅）已成为新视角合成的强大范式，但其外观建模通常依赖于球谐函数（SH），这带来了根本性限制。SH难以处理高频信号，会出现吉布斯振铃伪影，且无法捕捉镜面反射——这是真实感渲染的关键组成部分。尽管球面高斯等替代方法有所改进，但它们显著增加了优化复杂性。我们提出球面Voronoi（SV）作为3D高斯泼溅中外观表示的统一框架。SV将方向域划分为具有平滑边界的可学习区域，为视角相关效果提供了直观且稳定的参数化。对于漫反射外观，SV在保持优化比现有替代方法更简单的同时，取得了有竞争力的结果。对于SH失败的反射场景，我们利用SV作为可学习的反射探针，遵循经典图形学原理，以反射方向作为输入。该公式在合成和真实世界数据集上取得了最先进的结果，表明SV为显式3D表示中的外观建模提供了一个原则性、高效且通用的解决方案。

## 🔬 方法详解

论文提出球面Voronoi（SV）作为3D高斯泼溅中外观建模的统一框架。整体框架基于将球面方向域划分为多个可学习区域，每个区域对应一个外观参数，通过Voronoi图实现平滑边界划分。关键技术创新点包括：利用SV作为可学习的反射探针，以反射方向为输入，遵循经典图形学原理处理镜面反射；通过参数化区域边界实现稳定优化，避免球谐函数的高频限制。与现有方法的主要区别在于：相比球谐函数，SV能更好地捕捉高频和镜面效果；相比球面高斯，SV优化更简单，提供更直观的参数化，适用于显式3D表示中的通用外观建模。

## 📊 实验亮点

在合成和真实世界数据集上，球面Voronoi在反射建模方面显著优于球谐函数，达到最先进性能；漫反射场景中保持优化简单性，同时取得有竞争力结果；整体框架在多个基准测试中验证了高效性和通用性，为外观建模提供了新解决方案。

## 🎯 应用场景

该研究主要应用于计算机视觉和图形学领域，特别是新视角合成和真实感渲染任务。潜在应用包括虚拟现实、增强现实、电影特效和游戏开发中的高质量3D场景重建，以及机器人视觉和自动驾驶中的环境感知模拟，提升渲染效率和真实感。

## 📄 摘要（原文）

> Radiance field methods (e.g. 3D Gaussian Splatting) have emerged as a powerful paradigm for novel view synthesis, yet their appearance modeling often relies on Spherical Harmonics (SH), which impose fundamental limitations. SH struggle with high-frequency signals, exhibit Gibbs ringing artifacts, and fail to capture specular reflections - a key component of realistic rendering. Although alternatives like spherical Gaussians offer improvements, they add significant optimization complexity. We propose Spherical Voronoi (SV) as a unified framework for appearance representation in 3D Gaussian Splatting. SV partitions the directional domain into learnable regions with smooth boundaries, providing an intuitive and stable parameterization for view-dependent effects. For diffuse appearance, SV achieves competitive results while keeping optimization simpler than existing alternatives. For reflections - where SH fail - we leverage SV as learnable reflection probes, taking reflected directions as input following principles from classical graphics. This formulation attains state-of-the-art results on synthetic and real-world datasets, demonstrating that SV offers a principled, efficient, and general solution for appearance modeling in explicit 3D representations.

