---
layout: default
title: Whole-body motion planning and safety-critical control for aerial manipulation
---

# Whole-body motion planning and safety-critical control for aerial manipulation

**arXiv**: [2511.02342v1](https://arxiv.org/abs/2511.02342) | [PDF](https://arxiv.org/pdf/2511.02342.pdf)

**作者**: Lin Yang, Jinwoo Lee, Domenico Campolo, H. Jin Kim, Jeonghyun Byun

---

## 💡 一句话要点

**提出基于超二次曲面的全身运动规划与安全控制框架，用于空中机械臂在复杂环境中的安全操作。**

**关键词**: `空中机械臂` `全身运动规划` `安全关键控制` `超二次曲面` `控制屏障函数` `轨迹优化`

## 📋 核心要点

1. 核心问题：空中机械臂在复杂环境中规划安全、动态可行轨迹困难，常见几何抽象保守。
2. 方法要点：使用超二次曲面建模，结合Voronoi图与平衡流形规划，设计安全屏障控制器。
3. 实验或效果：仿真与硬件实验验证，轨迹更快、更安全、更平滑，几何保真度优于基线。

## 📄 摘要（原文）

> Aerial manipulation combines the maneuverability of multirotors with the
> dexterity of robotic arms to perform complex tasks in cluttered spaces. Yet
> planning safe, dynamically feasible trajectories remains difficult due to
> whole-body collision avoidance and the conservativeness of common geometric
> abstractions such as bounding boxes or ellipsoids. We present a whole-body
> motion planning and safety-critical control framework for aerial manipulators
> built on superquadrics (SQs). Using an SQ-plus-proxy representation, we model
> both the vehicle and obstacles with differentiable, geometry-accurate surfaces.
> Leveraging this representation, we introduce a maximum-clearance planner that
> fuses Voronoi diagrams with an equilibrium-manifold formulation to generate
> smooth, collision-aware trajectories. We further design a safety-critical
> controller that jointly enforces thrust limits and collision avoidance via
> high-order control barrier functions. In simulation, our approach outperforms
> sampling-based planners in cluttered environments, producing faster, safer, and
> smoother trajectories and exceeding ellipsoid-based baselines in geometric
> fidelity. Actual experiments on a physical aerial-manipulation platform confirm
> feasibility and robustness, demonstrating consistent performance across
> simulation and hardware settings. The video can be found at
> https://youtu.be/hQYKwrWf1Ak.

