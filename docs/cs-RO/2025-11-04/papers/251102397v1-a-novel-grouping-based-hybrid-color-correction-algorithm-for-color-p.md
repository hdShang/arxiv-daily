---
layout: default
title: A Novel Grouping-Based Hybrid Color Correction Algorithm for Color Point Clouds
---

# A Novel Grouping-Based Hybrid Color Correction Algorithm for Color Point Clouds

**arXiv**: [2511.02397v1](https://arxiv.org/abs/2511.02397) | [PDF](https://arxiv.org/pdf/2511.02397.pdf)

**作者**: Kuo-Liang Chung, Ting-Chung Tang

---

## 💡 一句话要点

**提出分组混合颜色校正算法以解决彩色点云颜色一致性问题**

**关键词**: `彩色点云` `颜色校正` `分组算法` `双边插值` `直方图均衡化` `3D渲染`

## 📋 核心要点

1. 核心问题：彩色点云颜色一致性校正，用于3D渲染和压缩应用
2. 方法要点：基于重叠率自适应分组，采用KBI、JKHE和HE方法校正颜色
3. 实验或效果：在1086对测试点云上验证，优于现有方法，代码开源

## 📄 摘要（原文）

> Color consistency correction for color point clouds is a fundamental yet
> important task in 3D rendering and compression applications. In the past, most
> previous color correction methods aimed at correcting color for color images.
> The purpose of this paper is to propose a grouping-based hybrid color
> correction algorithm for color point clouds. Our algorithm begins by estimating
> the overlapping rate between the aligned source and target point clouds, and
> then adaptively partitions the target points into two groups, namely the close
> proximity group Gcl and the moderate proximity group Gmod, or three groups,
> namely Gcl, Gmod, and the distant proximity group Gdist, when the estimated
> overlapping rate is low or high, respectively. To correct color for target
> points in Gcl, a K-nearest neighbors based bilateral interpolation (KBI) method
> is proposed. To correct color for target points in Gmod, a joint KBI and the
> histogram equalization (JKHE) method is proposed. For target points in Gdist, a
> histogram equalization (HE) method is proposed for color correction. Finally,
> we discuss the grouping-effect free property and the ablation study in our
> algorithm. The desired color consistency correction benefit of our algorithm
> has been justified through 1086 testing color point cloud pairs against the
> state-of-the-art methods. The C++ source code of our algorithm can be accessed
> from the website: https://github.com/ivpml84079/Point-cloud-color-correction.

