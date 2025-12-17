---
layout: default
title: UTrice: Unifying Primitives in Differentiable Ray Tracing and Rasterization via Triangles for Particle-Based 3D Scenes
---

# UTrice: Unifying Primitives in Differentiable Ray Tracing and Rasterization via Triangles for Particle-Based 3D Scenes

**arXiv**: [2512.04421v1](https://arxiv.org/abs/2512.04421) | [PDF](https://arxiv.org/pdf/2512.04421.pdf)

**作者**: Changhe Liu, Ehsan Javanmardi, Naren Bao, Alex Orsholits, Manabu Tsukada

---

## 💡 一句话要点

**提出基于三角形的可微光线追踪管道，统一渲染基元以提升新视角合成质量与效率。**

**关键词**: `可微渲染` `光线追踪` `三角形基元` `新视角合成` `实时渲染`

## 📋 核心要点

1. 现有方法依赖代理几何体进行光线追踪，导致复杂网格构建和高成本相交测试。
2. 直接使用三角形作为渲染基元，避免代理几何体，实现可微光线追踪。
3. 实验显示渲染质量显著优于现有方法，保持实时性能，并能直接渲染基于光栅化的优化三角形。

## 📄 摘要（原文）

> Ray tracing 3D Gaussian particles enables realistic effects such as depth of field, refractions, and flexible camera modeling for novel-view synthesis. However, existing methods trace Gaussians through proxy geometry, which requires constructing complex intermediate meshes and performing costly intersection tests. This limitation arises because Gaussian-based particles are not well suited as unified primitives for both ray tracing and rasterization. In this work, we propose a differentiable triangle-based ray tracing pipeline that directly treats triangles as rendering primitives without relying on any proxy geometry. Our results show that the proposed method achieves significantly higher rendering quality than existing ray tracing approaches while maintaining real-time rendering performance. Moreover, our pipeline can directly render triangles optimized by the rasterization-based method Triangle Splatting, thus unifying the primitives used in novel-view synthesis.

