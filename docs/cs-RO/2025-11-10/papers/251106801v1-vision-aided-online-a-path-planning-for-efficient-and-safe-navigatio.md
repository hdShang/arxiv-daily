---
layout: default
title: Vision-Aided Online A* Path Planning for Efficient and Safe Navigation of Service Robots
---

# Vision-Aided Online A* Path Planning for Efficient and Safe Navigation of Service Robots

**arXiv**: [2511.06801v1](https://arxiv.org/abs/2511.06801) | [PDF](https://arxiv.org/pdf/2511.06801.pdf)

**作者**: Praveen Kumar, Tushar Sandhan

---

## 💡 一句话要点

**提出视觉辅助在线A*路径规划框架，实现服务机器人在人机环境中的高效安全导航**

**关键词**: `服务机器人导航` `语义分割` `在线A*规划` `视觉约束` `实时路径规划`

## 📋 核心要点

1. 传统导航依赖激光雷达，语义感知不足，无法区分关键物体与普通障碍物
2. 集成轻量级语义分割与在线A*规划器，将视觉约束投影为地图障碍物
3. 在仿真和真实机器人实验中验证了实时性能和上下文感知导航能力

## 📄 摘要（原文）

> The deployment of autonomous service robots in human-centric environments is
> hindered by a critical gap in perception and planning. Traditional navigation
> systems rely on expensive LiDARs that, while geometrically precise, are seman-
> tically unaware, they cannot distinguish a important document on an office
> floor from a harmless piece of litter, treating both as physically traversable.
> While advanced semantic segmentation exists, no prior work has successfully
> integrated this visual intelligence into a real-time path planner that is
> efficient enough for low-cost, embedded hardware. This paper presents a frame-
> work to bridge this gap, delivering context-aware navigation on an affordable
> robotic platform. Our approach centers on a novel, tight integration of a
> lightweight perception module with an online A* planner. The perception system
> employs a semantic segmentation model to identify user-defined visual
> constraints, enabling the robot to navigate based on contextual importance
> rather than physical size alone. This adaptability allows an operator to define
> what is critical for a given task, be it sensitive papers in an office or
> safety lines in a factory, thus resolving the ambiguity of what to avoid. This
> semantic perception is seamlessly fused with geometric data. The identified
> visual constraints are projected as non-geometric obstacles onto a global map
> that is continuously updated from sensor data, enabling robust navigation
> through both partially known and unknown environments. We validate our
> framework through extensive experiments in high-fidelity simulations and on a
> real-world robotic platform. The results demonstrate robust, real-time
> performance, proving that a cost- effective robot can safely navigate complex
> environments while respecting critical visual cues invisible to traditional
> planners.

