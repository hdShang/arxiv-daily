---
layout: default
title: IPCD: Intrinsic Point-Cloud Decomposition
---

# IPCD: Intrinsic Point-Cloud Decomposition

**arXiv**: [2511.09866v1](https://arxiv.org/abs/2511.09866) | [PDF](https://arxiv.org/pdf/2511.09866.pdf)

**作者**: Shogo Sato, Takuhiro Kaneko, Shoichiro Takeda, Tomoyasu Shimada, Kazuhiko Murasaki, Taiga Yoshida, Ryuichi Tanida, Akisato Kimura

---

## 💡 一句话要点

**提出IPCD方法以解决点云中反照率与阴影分离的挑战**

**关键词**: `点云分解` `反照率分离` `阴影估计` `多视图投影` `纹理编辑` `重光照`

## 📋 核心要点

1. 核心问题：点云非网格结构及缺乏全局光照方向导致反照率与阴影分离困难
2. 方法要点：IPCD-Net扩展图像模型处理点云，PLD通过多视图投影捕获全局光照
3. 实验或效果：合成数据集验证减少阴影伪影，提升颜色精度，应用于纹理编辑和重光照

## 📄 摘要（原文）

> Point clouds are widely used in various fields, including augmented reality (AR) and robotics, where relighting and texture editing are crucial for realistic visualization. Achieving these tasks requires accurately separating albedo from shade. However, performing this separation on point clouds presents two key challenges: (1) the non-grid structure of point clouds makes conventional image-based decomposition models ineffective, and (2) point-cloud models designed for other tasks do not explicitly consider global-light direction, resulting in inaccurate shade. In this paper, we introduce \textbf{Intrinsic Point-Cloud Decomposition (IPCD)}, which extends image decomposition to the direct decomposition of colored point clouds into albedo and shade. To overcome challenge (1), we propose \textbf{IPCD-Net} that extends image-based model with point-wise feature aggregation for non-grid data processing. For challenge (2), we introduce \textbf{Projection-based Luminance Distribution (PLD)} with a hierarchical feature refinement, capturing global-light ques via multi-view projection. For comprehensive evaluation, we create a synthetic outdoor-scene dataset. Experimental results demonstrate that IPCD-Net reduces cast shadows in albedo and enhances color accuracy in shade. Furthermore, we showcase its applications in texture editing, relighting, and point-cloud registration under varying illumination. Finally, we verify the real-world applicability of IPCD-Net.

