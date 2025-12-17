---
layout: default
title: PartUV: Part-Based UV Unwrapping of 3D Meshes
---

# PartUV: Part-Based UV Unwrapping of 3D Meshes

**arXiv**: [2511.16659v1](https://arxiv.org/abs/2511.16659) | [PDF](https://arxiv.org/pdf/2511.16659.pdf)

**作者**: Zhaoning Wang, Xinyue Wei, Ruoxi Shi, Xiaoshuai Zhang, Hao Su, Minghua Liu

---

## 💡 一句话要点

**提出PartUV基于部件分解的UV展开方法，以处理AI生成网格的噪声和碎片化问题。**

**关键词**: `UV展开` `部件分解` `网格参数化` `AI生成网格` `多图表打包`

## 📋 核心要点

1. 核心问题：现有UV展开方法对AI生成网格处理不佳，导致碎片化图表和边界问题。
2. 方法要点：结合语义部件分解与几何启发式，在递归框架中控制失真并最小化图表数。
3. 实验效果：在多个数据集上优于现有方法，图表数和接缝长度减少，失真可比较。

## 📄 摘要（原文）

> UV unwrapping flattens 3D surfaces to 2D with minimal distortion, often requiring the complex surface to be decomposed into multiple charts. Although extensively studied, existing UV unwrapping methods frequently struggle with AI-generated meshes, which are typically noisy, bumpy, and poorly conditioned. These methods often produce highly fragmented charts and suboptimal boundaries, introducing artifacts and hindering downstream tasks. We introduce PartUV, a part-based UV unwrapping pipeline that generates significantly fewer, part-aligned charts while maintaining low distortion. Built on top of a recent learning-based part decomposition method PartField, PartUV combines high-level semantic part decomposition with novel geometric heuristics in a top-down recursive framework. It ensures each chart's distortion remains below a user-specified threshold while minimizing the total number of charts. The pipeline integrates and extends parameterization and packing algorithms, incorporates dedicated handling of non-manifold and degenerate meshes, and is extensively parallelized for efficiency. Evaluated across four diverse datasets, including man-made, CAD, AI-generated, and Common Shapes, PartUV outperforms existing tools and recent neural methods in chart count and seam length, achieves comparable distortion, exhibits high success rates on challenging meshes, and enables new applications like part-specific multi-tiles packing. Our project page is at https://www.zhaoningwang.com/PartUV.

