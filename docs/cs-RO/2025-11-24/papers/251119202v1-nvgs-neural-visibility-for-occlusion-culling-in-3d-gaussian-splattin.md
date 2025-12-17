---
layout: default
title: NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting
---

# NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting

**arXiv**: [2511.19202v1](https://arxiv.org/abs/2511.19202) | [PDF](https://arxiv.org/pdf/2511.19202.pdf)

**作者**: Brent Zoomers, Florian Hahlbohm, Joni Vanherck, Lode Jorissen, Marcus Magnor, Nick Michiels

---

## 💡 一句话要点

**提出神经可见性方法以解决3D高斯泼溅中遮挡剔除问题**

**关键词**: `3D高斯泼溅` `遮挡剔除` `神经可见性` `实例化渲染` `MLP查询`

## 📋 核心要点

1. 核心问题：高斯半透明特性阻碍遮挡剔除，影响渲染效率。
2. 方法要点：使用共享MLP学习高斯可见性函数，集成到实例化光栅器中。
3. 实验或效果：在组合场景中，降低VRAM使用并提升图像质量。

## 📄 摘要（原文）

> 3D Gaussian Splatting can exploit frustum culling and level-of-detail strategies to accelerate rendering of scenes containing a large number of primitives. However, the semi-transparent nature of Gaussians prevents the application of another highly effective technique: occlusion culling. We address this limitation by proposing a novel method to learn the viewpoint-dependent visibility function of all Gaussians in a trained model using a small, shared MLP across instances of an asset in a scene. By querying it for Gaussians within the viewing frustum prior to rasterization, our method can discard occluded primitives during rendering. Leveraging Tensor Cores for efficient computation, we integrate these neural queries directly into a novel instanced software rasterizer. Our approach outperforms the current state of the art for composed scenes in terms of VRAM usage and image quality, utilizing a combination of our instanced rasterizer and occlusion culling MLP, and exhibits complementary properties to existing LoD techniques.

