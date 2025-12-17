---
layout: default
title: PathMamba: A Hybrid Mamba-Transformer for Topologically Coherent Road Segmentation in Satellite Imagery
---

# PathMamba: A Hybrid Mamba-Transformer for Topologically Coherent Road Segmentation in Satellite Imagery

**arXiv**: [2511.21298v1](https://arxiv.org/abs/2511.21298) | [PDF](https://arxiv.org/pdf/2511.21298.pdf)

**作者**: Jules Decaestecker, Nicolas Vigne

---

## 💡 一句话要点

**提出PathMamba混合架构以解决卫星图像道路分割中的拓扑连续性问题**

**关键词**: `道路分割` `卫星图像` `混合架构` `状态空间模型` `拓扑连续性`

## 📋 核心要点

1. 核心问题：卫星图像道路分割需高精度与拓扑连续性，但现有方法如Vision Transformer计算复杂度高
2. 方法要点：结合Mamba的线性效率建模连续道路与Transformer的全局上下文优化特征
3. 实验或效果：在DeepGlobe和Massachusetts数据集上实现新SOTA，显著提升APLS指标

## 📄 摘要（原文）

> Achieving both high accuracy and topological continuity in road segmentation from satellite imagery is a critical goal for applications ranging from urban planning to disaster response. State-of-the-art methods often rely on Vision Transformers, which excel at capturing global context, yet their quadratic complexity is a significant barrier to efficient deployment, particularly for on-board processing in resource-constrained platforms. In contrast, emerging State Space Models like Mamba offer linear-time efficiency and are inherently suited to modeling long, continuous structures. We posit that these architectures have complementary strengths. To this end, we introduce PathMamba, a novel hybrid architecture that integrates Mamba's sequential modeling with the Transformer's global reasoning. Our design strategically uses Mamba blocks to trace the continuous nature of road networks, preserving topological structure, while integrating Transformer blocks to refine features with global context. This approach yields topologically superior segmentation maps without the prohibitive scaling costs of pure attention-based models. Our experiments on the DeepGlobe Road Extraction and Massachusetts Roads datasets demonstrate that PathMamba sets a new state-of-the-art. Notably, it significantly improves topological continuity, as measured by the APLS metric, setting a new benchmark while remaining computationally competitive.

