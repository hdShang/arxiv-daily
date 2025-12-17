---
layout: default
title: ReMoSPLAT: Reactive Mobile Manipulation Control on a Gaussian Splat
---

# ReMoSPLAT: Reactive Mobile Manipulation Control on a Gaussian Splat

**arXiv**: [2512.09656v1](https://arxiv.org/abs/2512.09656) | [PDF](https://arxiv.org/pdf/2512.09656.pdf)

**作者**: Nicolas Marticorena, Tobias Fischer, Niko Suenderhauf

---

## 💡 一句话要点

**提出ReMoSPLAT，基于高斯溅射表示的反应式移动操作控制器，用于避障和姿态控制。**

**关键词**: `移动操作控制` `反应式控制` `高斯溅射` `避障` `二次规划` `仿真实验`

## 📋 核心要点

1. 核心问题：移动操作器在避障时需准确环境表示，避免高成本规划。
2. 方法要点：使用二次规划结合高斯溅射表示，集成约束和成本以实现反应式控制。
3. 实验或效果：在仿真中验证可行性，性能接近依赖完美地面真值信息的控制器。

## 📄 摘要（原文）

> Reactive control can gracefully coordinate the motion of the base and the arm of a mobile manipulator. However, incorporating an accurate representation of the environment to avoid obstacles without involving costly planning remains a challenge. In this work, we present ReMoSPLAT, a reactive controller based on a quadratic program formulation for mobile manipulation that leverages a Gaussian Splat representation for collision avoidance. By integrating additional constraints and costs into the optimisation formulation, a mobile manipulator platform can reach its intended end effector pose while avoiding obstacles, even in cluttered scenes. We investigate the trade-offs of two methods for efficiently calculating robot-obstacle distances, comparing a purely geometric approach with a rasterisation-based approach. Our experiments in simulation on both synthetic and real-world scans demonstrate the feasibility of our method, showing that the proposed approach achieves performance comparable to controllers that rely on perfect ground-truth information.

