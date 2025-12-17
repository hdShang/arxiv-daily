---
layout: default
title: RVC-NMPC: Nonlinear Model Predictive Control with Reciprocal Velocity Constraints for Mutual Collision Avoidance in Agile UAV Flight
---

# RVC-NMPC: Nonlinear Model Predictive Control with Reciprocal Velocity Constraints for Mutual Collision Avoidance in Agile UAV Flight

**arXiv**: [2512.08574v1](https://arxiv.org/abs/2512.08574) | [PDF](https://arxiv.org/pdf/2512.08574.pdf)

**作者**: Vit Kratky, Robert Penicka, Parakh M. Gupta, Ondrej Prochazka, Martin Saska

---

## 💡 一句话要点

**提出基于非线性模型预测控制与互惠速度约束的无人机敏捷飞行互避方法**

**关键词**: `无人机互避` `非线性模型预测控制` `互惠速度约束` `实时控制` `敏捷飞行`

## 📋 核心要点

1. 核心问题：无人机敏捷飞行中的互避需高效、低通信依赖的实时控制。
2. 方法要点：集成互惠速度约束至非线性模型预测控制，仅依赖可观测信息，实现100Hz处理。
3. 实验或效果：仿真与实飞验证，在10架无人机、25m/s速度下，飞行时间减少31%，无碰撞。

## 📄 摘要（原文）

> This paper presents an approach to mutual collision avoidance based on Nonlinear Model Predictive Control (NMPC) with time-dependent Reciprocal Velocity Constraints (RVCs). Unlike most existing methods, the proposed approach relies solely on observable information about other robots, eliminating the necessity of excessive communication use. The computationally efficient algorithm for computing RVCs, together with the direct integration of these constraints into NMPC problem formulation on a controller level, allows the whole pipeline to run at 100 Hz. This high processing rate, combined with modeled nonlinear dynamics of the controlled Uncrewed Aerial Vehicles (UAVs), is a key feature that facilitates the use of the proposed approach for an agile UAV flight. The proposed approach was evaluated through extensive simulations emulating real-world conditions in scenarios involving up to 10 UAVs and velocities of up to 25 m/s, and in real-world experiments with accelerations up to 30 m/s$^2$. Comparison with state of the art shows 31% improvement in terms of flight time reduction in challenging scenarios, while maintaining a collision-free navigation in all trials.

