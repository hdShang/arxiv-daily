---
layout: default
title: Dynamically-Consistent Trajectory Optimization for Legged Robots via Contact Point Decomposition
---

# Dynamically-Consistent Trajectory Optimization for Legged Robots via Contact Point Decomposition

**arXiv**: [2510.24069v1](https://arxiv.org/abs/2510.24069) | [PDF](https://arxiv.org/pdf/2510.24069.pdf)

**作者**: Sangmin Kim, Hajun Kim, Gijeong Kim, Min-Gyu Kim, Hae-Won Park

---

## 💡 一句话要点

**提出基于接触点分解的轨迹优化方法，确保足式机器人动态一致性。**

**关键词**: `足式机器人` `轨迹优化` `动态一致性` `接触点分解` `Bézier多项式`

## 📋 核心要点

1. 核心问题：轨迹优化需同时计算路径与接触序列，并准确考虑动态约束。
2. 方法要点：利用线性微分方程叠加性分解接触点动态，结合Bézier多项式确保动态一致性。
3. 实验或效果：在四足机器人模型上验证动态可行性与运动生成能力。

## 📄 摘要（原文）

> To generate reliable motion for legged robots through trajectory
> optimization, it is crucial to simultaneously compute the robot's path and
> contact sequence, as well as accurately consider the dynamics in the problem
> formulation. In this paper, we present a phase-based trajectory optimization
> that ensures the feasibility of translational dynamics and friction cone
> constraints throughout the entire trajectory. Specifically, our approach
> leverages the superposition properties of linear differential equations to
> decouple the translational dynamics for each contact point, which operates
> under different phase sequences. Furthermore, we utilize the differentiation
> matrix of B{\'e}zier polynomials to derive an analytical relationship between
> the robot's position and force, thereby ensuring the consistent satisfaction of
> translational dynamics. Additionally, by exploiting the convex closure property
> of B{\'e}zier polynomials, our method ensures compliance with friction cone
> constraints. Using the aforementioned approach, the proposed trajectory
> optimization framework can generate dynamically reliable motions with various
> gait sequences for legged robots. We validate our framework using a quadruped
> robot model, focusing on the feasibility of dynamics and motion generation.

