---
layout: default
title: Combining High Level Scheduling and Low Level Control to Manage Fleets of Mobile Robots
---

# Combining High Level Scheduling and Low Level Control to Manage Fleets of Mobile Robots

**arXiv**: [2510.23129v1](https://arxiv.org/abs/2510.23129) | [PDF](https://arxiv.org/pdf/2510.23129.pdf)

**作者**: Sabino Francesco Roselli, Ze Zhang, Knut Åkesson

---

## 💡 一句话要点

**提出两层框架结合高层调度与低层控制以管理工业移动机器人车队**

**关键词**: `移动机器人调度` `模型预测控制` `工业自动化` `车队管理` `实时控制`

## 📋 核心要点

1. 核心问题：工业环境中大规模移动机器人车队的可扩展协调与动态障碍处理。
2. 方法要点：使用ComSat算法调度任务，分布式MPC实时控制轨迹，确保安全无碰撞。
3. 实验效果：在模拟2D环境中评估，高任务完成率，拥堵下鲁棒性强。

## 📄 摘要（原文）

> The deployment of mobile robots for material handling in industrial
> environments requires scalable coordination of large fleets in dynamic
> settings. This paper presents a two-layer framework that combines high-level
> scheduling with low-level control. Tasks are assigned and scheduled using the
> compositional algorithm ComSat, which generates time-parameterized routes for
> each robot. These schedules are then used by a distributed Model Predictive
> Control (MPC) system in real time to compute local reference trajectories,
> accounting for static and dynamic obstacles. The approach ensures safe,
> collision-free operation, and supports rapid rescheduling in response to
> disruptions such as robot failures or environmental changes. We evaluate the
> method in simulated 2D environments with varying road capacities and traffic
> conditions, demonstrating high task completion rates and robust behavior even
> under congestion. The modular structure of the framework allows for
> computational tractability and flexibility, making it suitable for deployment
> in complex, real-world industrial scenarios.

