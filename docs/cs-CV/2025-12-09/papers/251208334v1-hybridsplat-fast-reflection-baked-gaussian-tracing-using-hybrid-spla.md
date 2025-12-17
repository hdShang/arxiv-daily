---
layout: default
title: HybridSplat: Fast Reflection-baked Gaussian Tracing using Hybrid Splatting
---

# HybridSplat: Fast Reflection-baked Gaussian Tracing using Hybrid Splatting

**arXiv**: [2512.08334v1](https://arxiv.org/abs/2512.08334) | [PDF](https://arxiv.org/pdf/2512.08334.pdf)

**作者**: Chang Liu, Hongliang Yuan, Lianghao Zhang, Sichao Wang, Jianwei Guo, Shi-Sheng Huang

---

## 💡 一句话要点

**提出HybridSplat机制，通过反射烘焙高斯追踪和混合溅射，加速复杂反射场景渲染并减少内存占用。**

**关键词**: `3D高斯溅射` `反射渲染` `混合溅射` `渲染加速` `内存优化` `复杂场景重建`

## 📋 核心要点

1. 核心问题：基于3D高斯溅射的复杂反射渲染存在速度慢和内存占用高的瓶颈。
2. 方法要点：引入反射烘焙高斯追踪，在单个高斯基元内烘焙视图相关反射，结合基于瓦片的高斯溅射进行渲染。
3. 实验或效果：在Ref-NeRF和NeRF-Casting数据集上，渲染速度提升约7倍，高斯基元数量减少4倍，保持反射质量。

## 📄 摘要（原文）

> Rendering complex reflection of real-world scenes using 3D Gaussian splatting has been a quite promising solution for photorealistic novel view synthesis, but still faces bottlenecks especially in rendering speed and memory storage. This paper proposes a new Hybrid Splatting(HybridSplat) mechanism for Gaussian primitives. Our key idea is a new reflection-baked Gaussian tracing, which bakes the view-dependent reflection within each Gaussian primitive while rendering the reflection using tile-based Gaussian splatting. Then we integrate the reflective Gaussian primitives with base Gaussian primitives using a unified hybrid splatting framework for high-fidelity scene reconstruction. Moreover, we further introduce a pipeline-level acceleration for the hybrid splatting, and reflection-sensitive Gaussian pruning to reduce the model size, thus achieving much faster rendering speed and lower memory storage while preserving the reflection rendering quality. By extensive evaluation, our HybridSplat accelerates about 7x rendering speed across complex reflective scenes from Ref-NeRF, NeRF-Casting with 4x fewer Gaussian primitives than similar ray-tracing based Gaussian splatting baselines, serving as a new state-of-the-art method especially for complex reflective scenes.

