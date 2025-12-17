---
layout: default
title: GLOW: Global Illumination-Aware Inverse Rendering of Indoor Scenes Captured with Dynamic Co-Located Light & Camera
---

# GLOW: Global Illumination-Aware Inverse Rendering of Indoor Scenes Captured with Dynamic Co-Located Light & Camera

**arXiv**: [2511.22857v1](https://arxiv.org/abs/2511.22857) | [PDF](https://arxiv.org/pdf/2511.22857.pdf)

**作者**: Jiaye Wu, Saeed Hadadan, Geng Lin, Peihan Tu, Matthias Zwicker, David Jacobs, Roni Sengupta

---

## 💡 一句话要点

**提出GLOW框架以解决共置光相机室内场景逆渲染中的全局光照和材质反射率估计问题**

**关键词**: `逆渲染` `全局光照` `神经辐射缓存` `共置光相机` `材质估计` `室内场景`

## 📋 核心要点

1. 核心问题：共置光相机室内场景逆渲染中，强互反射、动态阴影和移动高光导致材质与光照解耦困难
2. 方法要点：结合神经隐式表面和神经辐射缓存，通过动态缓存和表面角度加权损失优化几何与反射率
3. 实验或效果：在自然和共置光照下，GLOW在材质反射率估计上显著优于现有方法

## 📄 摘要（原文）

> Inverse rendering of indoor scenes remains challenging due to the ambiguity between reflectance and lighting, exacerbated by inter-reflections among multiple objects. While natural illumination-based methods struggle to resolve this ambiguity, co-located light-camera setups offer better disentanglement as lighting can be easily calibrated via Structure-from-Motion. However, such setups introduce additional complexities like strong inter-reflections, dynamic shadows, near-field lighting, and moving specular highlights, which existing approaches fail to handle. We present GLOW, a Global Illumination-aware Inverse Rendering framework designed to address these challenges. GLOW integrates a neural implicit surface representation with a neural radiance cache to approximate global illumination, jointly optimizing geometry and reflectance through carefully designed regularization and initialization. We then introduce a dynamic radiance cache that adapts to sharp lighting discontinuities from near-field motion, and a surface-angle-weighted radiometric loss to suppress specular artifacts common in flashlight captures. Experiments show that GLOW substantially outperforms prior methods in material reflectance estimation under both natural and co-located illumination.

