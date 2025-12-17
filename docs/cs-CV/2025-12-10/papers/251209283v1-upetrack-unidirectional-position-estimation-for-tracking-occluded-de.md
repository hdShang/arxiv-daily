---
layout: default
title: UPETrack: Unidirectional Position Estimation for Tracking Occluded Deformable Linear Objects
---

# UPETrack: Unidirectional Position Estimation for Tracking Occluded Deformable Linear Objects

**arXiv**: [2512.09283v1](https://arxiv.org/abs/2512.09283) | [PDF](https://arxiv.org/pdf/2512.09283.pdf)

**作者**: Fan Wu, Chenguang Yang, Haibin Yang, Shuo Wang, Yanrui Xu, Xing Zhou, Meng Gao, Yaoqi Xian, Zhihong Zhu, Shifeng Huang

---

## 💡 一句话要点

**提出UPETrack框架，基于单向位置估计解决遮挡下可变形线性物体的实时跟踪问题。**

**关键词**: `可变形线性物体跟踪` `遮挡处理` `几何驱动方法` `实时状态估计` `单向位置估计`

## 📋 核心要点

1. 核心问题：可变形线性物体因高维配置空间、非线性动态和频繁遮挡，难以实现鲁棒实时跟踪。
2. 方法要点：采用几何驱动框架，结合可见段高斯混合模型跟踪和遮挡区域单向位置估计算法，无需物理建模或标记。
3. 实验或效果：在定位精度和计算效率上超越TrackDLO和CDCPD2等先进算法。

## 📄 摘要（原文）

> Real-time state tracking of Deformable Linear Objects (DLOs) is critical for enabling robotic manipulation of DLOs in industrial assembly, medical procedures, and daily-life applications. However, the high-dimensional configuration space, nonlinear dynamics, and frequent partial occlusions present fundamental barriers to robust real-time DLO tracking. To address these limitations, this study introduces UPETrack, a geometry-driven framework based on Unidirectional Position Estimation (UPE), which facilitates tracking without the requirement for physical modeling, virtual simulation, or visual markers. The framework operates in two phases: (1) visible segment tracking is based on a Gaussian Mixture Model (GMM) fitted via the Expectation Maximization (EM) algorithm, and (2) occlusion region prediction employing UPE algorithm we proposed. UPE leverages the geometric continuity inherent in DLO shapes and their temporal evolution patterns to derive a closed-form positional estimator through three principal mechanisms: (i) local linear combination displacement term, (ii) proximal linear constraint term, and (iii) historical curvature term. This analytical formulation allows efficient and stable estimation of occluded nodes through explicit linear combinations of geometric components, eliminating the need for additional iterative optimization. Experimental results demonstrate that UPETrack surpasses two state-of-the-art tracking algorithms, including TrackDLO and CDCPD2, in both positioning accuracy and computational efficiency.

