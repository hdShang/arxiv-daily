---
layout: default
title: Towards Fast and Scalable Normal Integration using Continuous Components
---

# Towards Fast and Scalable Normal Integration using Continuous Components

**arXiv**: [2510.11508v1](https://arxiv.org/abs/2510.11508) | [PDF](https://arxiv.org/pdf/2510.11508.pdf)

**作者**: Francesco Milano, Jen Jen Chung, Lionel Ott, Roland Siegwart

---

## 💡 一句话要点

**提出基于连续组件的法向积分方法以解决大规模法向图重建效率问题**

**关键词**: `法向积分` `表面重建` `优化加速` `连续组件` `计算机视觉`

## 📋 核心要点

1. 核心问题：现有法向积分方法依赖迭代全局优化，在大规模法向图上扩展性差。
2. 方法要点：将法向积分重构为连续组件相对尺度估计，减少优化变量数量。
3. 实验效果：在标准基准上实现最优结果，大分辨率法向图速度提升一个数量级。

## 📄 摘要（原文）

> Surface normal integration is a fundamental problem in computer vision,
> dealing with the objective of reconstructing a surface from its corresponding
> normal map. Existing approaches require an iterative global optimization to
> jointly estimate the depth of each pixel, which scales poorly to larger normal
> maps. In this paper, we address this problem by recasting normal integration as
> the estimation of relative scales of continuous components. By constraining
> pixels belonging to the same component to jointly vary their scale, we
> drastically reduce the number of optimization variables. Our framework includes
> a heuristic to accurately estimate continuous components from the start, a
> strategy to rebalance optimization terms, and a technique to iteratively merge
> components to further reduce the size of the problem. Our method achieves
> state-of-the-art results on the standard normal integration benchmark in as
> little as a few seconds and achieves one-order-of-magnitude speedup over
> pixel-level approaches on large-resolution normal maps.

