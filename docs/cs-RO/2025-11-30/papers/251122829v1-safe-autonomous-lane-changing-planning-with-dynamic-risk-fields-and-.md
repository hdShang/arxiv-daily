---
layout: default
title: Safe Autonomous Lane Changing: Planning with Dynamic Risk Fields and Time-Varying Convex Space Generation
---

# Safe Autonomous Lane Changing: Planning with Dynamic Risk Fields and Time-Varying Convex Space Generation

**arXiv**: [2511.22829v1](https://arxiv.org/abs/2511.22829) | [PDF](https://arxiv.org/pdf/2511.22829.pdf)

**作者**: Zhen Tian, Zhihao Lin

---

## 💡 一句话要点

**提出动态风险场与时变凸可行空间规划方法，以解决自动驾驶换道场景中的安全轨迹生成问题。**

**关键词**: `自动驾驶轨迹规划` `动态风险场` `时变凸可行空间` `约束iLQR算法` `安全换道` `碰撞避免`

## 📋 核心要点

1. 核心问题：自动驾驶换道等复杂场景中，需平衡轨迹平滑性、控制效率和碰撞风险，确保安全与舒适性。
2. 方法要点：构建动态风险场评估静态与动态风险，生成时变凸可行空间保证运动学可行性，采用约束iLQR算法优化轨迹。
3. 实验或效果：仿真显示方法优于传统方法，实现更短换道距离（28.59米）和时间（2.84秒），并在密集环岛中表现出更高安全裕度和平滑性。

## 📄 摘要（原文）

> This paper presents a novel trajectory planning pipeline for complex driving scenarios like autonomous lane changing, by integrating risk-aware planning with guaranteed collision avoidance into a unified optimization framework. We first construct a dynamic risk fields (DRF) that captures both the static and dynamic collision risks from surrounding vehicles. Then, we develop a rigorous strategy for generating time-varying convex feasible spaces that ensure kinematic feasibility and safety requirements. The trajectory planning problem is formulated as a finite-horizon optimal control problem and solved using a constrained iterative Linear Quadratic Regulator (iLQR) algorithm that jointly optimizes trajectory smoothness, control effort, and risk exposure while maintaining strict feasibility. Extensive simulations demonstrate that our method outperforms traditional approaches in terms of safety and efficiency, achieving collision-free trajectories with shorter lane-changing distances (28.59 m) and times (2.84 s) while maintaining smooth and comfortable acceleration patterns. In dense roundabout environments the planner further demonstrates robust adaptability, producing larger safety margins, lower jerk, and superior curvature smoothness compared with APF, MPC, and RRT based baselines. These results confirm that the integrated DRF with convex feasible space and constrained iLQR solver provides a balanced solution for safe, efficient, and comfortable trajectory generation in dynamic and interactive traffic scenarios.

