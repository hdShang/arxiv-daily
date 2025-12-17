---
layout: default
title: Gaussian-Augmented Physics Simulation and System Identification with Complex Colliders
---

# Gaussian-Augmented Physics Simulation and System Identification with Complex Colliders

**arXiv**: [2511.06846v1](https://arxiv.org/abs/2511.06846) | [PDF](https://arxiv.org/pdf/2511.06846.pdf)

**作者**: Federico Vasile, Ri-Zhao Qiu, Lorenzo Natale, Xiaolong Wang

---

## 💡 一句话要点

**提出AS-DiffMPM以解决复杂碰撞体下的系统识别问题**

**关键词**: `系统识别` `可微物理模拟` `复杂碰撞体` `端到端优化` `新视角合成`

## 📋 核心要点

1. 核心问题：现有方法局限于平面碰撞体，无法处理非平面表面碰撞。
2. 方法要点：扩展可微MPM，引入可微碰撞处理机制，支持任意形状碰撞体。
3. 实验或效果：可与多种新视角合成方法结合，实现端到端优化。

## 📄 摘要（原文）

> System identification involving the geometry, appearance, and physical
> properties from video observations is a challenging task with applications in
> robotics and graphics. Recent approaches have relied on fully differentiable
> Material Point Method (MPM) and rendering for simultaneous optimization of
> these properties. However, they are limited to simplified object-environment
> interactions with planar colliders and fail in more challenging scenarios where
> objects collide with non-planar surfaces. We propose AS-DiffMPM, a
> differentiable MPM framework that enables physical property estimation with
> arbitrarily shaped colliders. Our approach extends existing methods by
> incorporating a differentiable collision handling mechanism, allowing the
> target object to interact with complex rigid bodies while maintaining
> end-to-end optimization. We show AS-DiffMPM can be easily interfaced with
> various novel view synthesis methods as a framework for system identification
> from visual observations.

