---
layout: default
title: T-ESKF: Transformed Error-State Kalman Filter for Consistent Visual-Inertial Navigation
---

# T-ESKF: Transformed Error-State Kalman Filter for Consistent Visual-Inertial Navigation

**arXiv**: [2510.23359v1](https://arxiv.org/abs/2510.23359) | [PDF](https://arxiv.org/pdf/2510.23359.pdf)

**作者**: Chungeng Tian, Ning Hao, Fenghua He

---

## 💡 一句话要点

**提出变换误差状态卡尔曼滤波器以解决视觉-惯性导航中的不一致性问题**

**关键词**: `视觉-惯性导航` `误差状态卡尔曼滤波` `可观测性分析` `状态估计` `传感器融合`

## 📋 核心要点

1. 核心问题：视觉-惯性导航系统因可观测性失配导致估计不一致
2. 方法要点：在线性时变变换下变换误差状态，确保可观测子空间与状态无关
3. 实验或效果：仿真与实验验证性能优于或至少与先进方法相当

## 📄 摘要（原文）

> This paper presents a novel approach to address the inconsistency problem
> caused by observability mismatch in visual-inertial navigation systems (VINS).
> The key idea involves applying a linear time-varying transformation to the
> error-state within the Error-State Kalman Filter (ESKF). This transformation
> ensures that \textrr{the unobservable subspace of the transformed error-state
> system} becomes independent of the state, thereby preserving the correct
> observability of the transformed system against variations in linearization
> points. We introduce the Transformed ESKF (T-ESKF), a consistent VINS estimator
> that performs state estimation using the transformed error-state system.
> Furthermore, we develop an efficient propagation technique to accelerate the
> covariance propagation based on the transformation relationship between the
> transition and accumulated matrices of T-ESKF and ESKF. We validate the
> proposed method through extensive simulations and experiments, demonstrating
> better (or competitive at least) performance compared to state-of-the-art
> methods. The code is available at github.com/HITCSC/T-ESKF.

