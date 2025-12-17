---
layout: default
title: A Generalizable Light Transport 3D Embedding for Global Illumination
---

# A Generalizable Light Transport 3D Embedding for Global Illumination

**arXiv**: [2510.18189v1](https://arxiv.org/abs/2510.18189) | [PDF](https://arxiv.org/pdf/2510.18189.pdf)

**作者**: Bing Xu, Mukund Varma T, Cheng Wang, Tzumao Li, Lifan Wu, Bartlomiej Wronski, Ravi Ramamoorthi, Marco Salvi

---

## 💡 一句话要点

**提出可泛化3D光传输嵌入以从3D场景配置预测全局光照**

**关键词**: `全局光照` `3D场景嵌入` `Transformer模型` `点云表示` `神经渲染` `光传输`

## 📋 核心要点

1. 全局光照模拟计算昂贵，现有方法依赖逐场景优化或2D空间，存在视图不一致问题。
2. 使用点云表示场景，通过Transformer建模全局交互，编码为神经基元以预测渲染量。
3. 在多样室内场景验证漫反射全局光照预测，并可快速适应新任务，初步支持光泽材料。

## 📄 摘要（原文）

> Global illumination (GI) is essential for realistic rendering but remains
> computationally expensive due to the complexity of simulating indirect light
> transport. Recent neural methods have mainly relied on per-scene optimization,
> sometimes extended to handle changes in camera or geometry. Efforts toward
> cross-scene generalization have largely stayed in 2D screen space, such as
> neural denoising or G-buffer based GI prediction, which often suffer from view
> inconsistency and limited spatial understanding. We propose a generalizable 3D
> light transport embedding that approximates global illumination directly from
> 3D scene configurations, without using rasterized or path-traced cues. Each
> scene is represented as a point cloud with geometric and material features. A
> scalable transformer models global point-to-point interactions to encode these
> features into neural primitives. At render time, each query point retrieves
> nearby primitives via nearest-neighbor search and aggregates their latent
> features through cross-attention to predict the desired rendering quantity. We
> demonstrate results on diffuse global illumination prediction across diverse
> indoor scenes with varying layouts, geometry, and materials. The embedding
> trained for irradiance estimation can be quickly adapted to new rendering tasks
> with limited fine-tuning. We also present preliminary results for
> spatial-directional radiance field estimation for glossy materials and show how
> the normalized field can accelerate unbiased path guiding. This approach
> highlights a path toward integrating learned priors into rendering pipelines
> without explicit ray-traced illumination cues.

