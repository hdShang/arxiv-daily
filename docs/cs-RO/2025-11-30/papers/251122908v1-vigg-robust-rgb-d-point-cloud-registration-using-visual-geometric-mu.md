---
layout: default
title: ViGG: Robust RGB-D Point Cloud Registration using Visual-Geometric Mutual Guidance
---

# ViGG: Robust RGB-D Point Cloud Registration using Visual-Geometric Mutual Guidance

**arXiv**: [2511.22908v1](https://arxiv.org/abs/2511.22908) | [PDF](https://arxiv.org/pdf/2511.22908.pdf)

**作者**: Congjia Chen, Shen Yan, Yufu Qu

---

## 💡 一句话要点

**提出ViGG方法，通过视觉-几何互引导实现鲁棒的RGB-D点云配准**

**关键词**: `点云配准` `RGB-D配准` `视觉-几何互引导` `鲁棒性` `学习无关方法`

## 📋 核心要点

1. 核心问题：现有RGB-D配准方法多依赖特征融合，未能充分利用图像信息，影响实际应用。
2. 方法要点：采用视觉-几何互引导策略，包括几何引导抑制模糊团和视觉引导几何匹配提取高质量对应。
3. 实验或效果：在3DMatch、ScanNet和KITTI数据集上优于最新方法，适用于多种RGB-D配准任务。

## 📄 摘要（原文）

> Point cloud registration is a fundamental task in 3D vision. Most existing methods only use geometric information for registration. Recently proposed RGB-D registration methods primarily focus on feature fusion or improving feature learning, which limits their ability to exploit image information and hinders their practical applicability. In this paper, we propose ViGG, a robust RGB-D registration method using mutual guidance. First, we solve clique alignment in a visual-geometric combination form, employing a geometric guidance design to suppress ambiguous cliques. Second, to mitigate accuracy degradation caused by noise in visual matches, we propose a visual-guided geometric matching method that utilizes visual priors to determine the search space, enabling the extraction of high-quality, noise-insensitive correspondences. This mutual guidance strategy brings our method superior robustness, making it applicable for various RGB-D registration tasks. The experiments on 3DMatch, ScanNet and KITTI datasets show that our method outperforms recent state-of-the-art methods in both learning-free and learning-based settings. Code is available at https://github.com/ccjccjccj/ViGG.

