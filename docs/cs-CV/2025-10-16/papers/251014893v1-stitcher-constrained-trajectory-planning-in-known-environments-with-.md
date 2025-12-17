---
layout: default
title: STITCHER: Constrained Trajectory Planning in Known Environments with Real-Time Motion Primitive Search
---

# STITCHER: Constrained Trajectory Planning in Known Environments with Real-Time Motion Primitive Search

**arXiv**: [2510.14893v1](https://arxiv.org/abs/2510.14893) | [PDF](https://arxiv.org/pdf/2510.14893.pdf)

**作者**: Helene J. Levy, Brett T. Lopez

---

## 💡 一句话要点

**提出STITCHER框架，通过实时运动基元搜索在已知环境中规划约束轨迹**

**关键词**: `轨迹规划` `实时运动基元搜索` `无优化规划` `约束满足` `自主导航` `图搜索`

## 📋 核心要点

1. 核心问题：高速自主导航需实时生成动态可行、无碰撞且满足约束的轨迹，优化方法存在计算时间和数值稳定性限制
2. 方法要点：采用无优化方法，缝合短轨迹段，结合图搜索实现长距离、表达性强且近最优的实时规划
3. 实验或效果：仿真测试显示在50m x 50m环境中数毫秒内生成安全轨迹，硬件测试验证实时跟踪路径并处理非凸约束

## 📄 摘要（原文）

> Autonomous high-speed navigation through large, complex environments requires
> real-time generation of agile trajectories that are dynamically feasible,
> collision-free, and satisfy state or actuator constraints. Modern trajectory
> planning techniques primarily use numerical optimization, as they enable the
> systematic computation of high-quality, expressive trajectories that satisfy
> various constraints. However, stringent requirements on computation time and
> the risk of numerical instability can limit the use of optimization-based
> planners in safety-critical scenarios. This work presents an optimization-free
> planning framework called STITCHER that stitches short trajectory segments
> together with graph search to compute long-range, expressive, and near-optimal
> trajectories in real-time. STITCHER outperforms modern optimization-based
> planners through our innovative planning architecture and several algorithmic
> developments that make real-time planning possible. Extensive simulation
> testing is performed to analyze the algorithmic components that make up
> STITCHER, along with a thorough comparison with two state-of-the-art
> optimization planners. Simulation tests show that safe trajectories can be
> created within a few milliseconds for paths that span the entirety of two 50 m
> x 50 m environments. Hardware tests with a custom quadrotor verify that
> STITCHER can produce trackable paths in real-time while respecting nonconvex
> constraints, such as limits on tilt angle and motor forces, which are otherwise
> hard to include in optimization-based planners.

