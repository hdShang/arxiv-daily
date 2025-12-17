---
layout: default
title: ERNet: Efficient Non-Rigid Registration Network for Point Sequences
---

# ERNet: Efficient Non-Rigid Registration Network for Point Sequences

**arXiv**: [2510.15800v1](https://arxiv.org/abs/2510.15800) | [PDF](https://arxiv.org/pdf/2510.15800.pdf)

**作者**: Guangzhao He, Yuxi Xiao, Zhen Xu, Xiaowei Zhou, Sida Peng

---

## 💡 一句话要点

**提出ERNet以高效解决点序列非刚性配准中的局部最小值和误差累积问题**

**关键词**: `点云配准` `非刚性变形` `序列处理` `变形图预测` `滑动窗口优化`

## 📋 核心要点

1. 核心问题：非刚性配准中局部最小值和长序列误差累积阻碍准确变形估计
2. 方法要点：采用两阶段管道预测变形图，先粗估节点再滑动窗口精炼轨迹
3. 实验或效果：在DeformingThings4D和D-FAUST数据集上优于SOTA，速度提升4倍以上

## 📄 摘要（原文）

> Registering an object shape to a sequence of point clouds undergoing
> non-rigid deformation is a long-standing challenge. The key difficulties stem
> from two factors: (i) the presence of local minima due to the non-convexity of
> registration objectives, especially under noisy or partial inputs, which
> hinders accurate and robust deformation estimation, and (ii) error accumulation
> over long sequences, leading to tracking failures. To address these challenges,
> we introduce to adopt a scalable data-driven approach and propose ERNet, an
> efficient feed-forward model trained on large deformation datasets. It is
> designed to handle noisy and partial inputs while effectively leveraging
> temporal information for accurate and consistent sequential registration. The
> key to our design is predicting a sequence of deformation graphs through a
> two-stage pipeline, which first estimates frame-wise coarse graph nodes for
> robust initialization, before refining their trajectories over time in a
> sliding-window fashion. Extensive experiments show that our proposed approach
> (i) outperforms previous state-of-the-art on both the DeformingThings4D and
> D-FAUST datasets, and (ii) achieves more than 4x speedup compared to the
> previous best, offering significant efficiency improvement.

