---
layout: default
title: Manifold-constrained Hamilton-Jacobi Reachability Learning for Decentralized Multi-Agent Motion Planning
---

# Manifold-constrained Hamilton-Jacobi Reachability Learning for Decentralized Multi-Agent Motion Planning

**arXiv**: [2511.03591v1](https://arxiv.org/abs/2511.03591) | [PDF](https://arxiv.org/pdf/2511.03591.pdf)

**作者**: Qingyi Chen, Ruiqi Ni, Jun Kim, Ahmed H. Qureshi

---

## 💡 一句话要点

**提出流形约束哈密顿-雅可比可达性学习框架，以解决去中心化多智能体运动规划中的任务约束安全问题。**

**关键词**: `多智能体运动规划` `流形约束` `哈密顿-雅可比可达性` `去中心化规划` `轨迹优化` `机器人安全`

## 📋 核心要点

1. 核心问题：多智能体在动态环境中运动时，需满足任务施加的流形约束，如服务机器人端杯避障。
2. 方法要点：结合流形约束求解HJR问题，捕捉任务感知安全条件，并集成到去中心化轨迹优化规划器中。
3. 实验或效果：在多种流形约束任务中优于现有约束运动规划器，运行速度适合实际应用。

## 📄 摘要（原文）

> Safe multi-agent motion planning (MAMP) under task-induced constraints is a
> critical challenge in robotics. Many real-world scenarios require robots to
> navigate dynamic environments while adhering to manifold constraints imposed by
> tasks. For example, service robots must carry cups upright while avoiding
> collisions with humans or other robots. Despite recent advances in
> decentralized MAMP for high-dimensional systems, incorporating manifold
> constraints remains difficult. To address this, we propose a
> manifold-constrained Hamilton-Jacobi reachability (HJR) learning framework for
> decentralized MAMP. Our method solves HJR problems under manifold constraints
> to capture task-aware safety conditions, which are then integrated into a
> decentralized trajectory optimization planner. This enables robots to generate
> motion plans that are both safe and task-feasible without requiring assumptions
> about other agents' policies. Our approach generalizes across diverse
> manifold-constrained tasks and scales effectively to high-dimensional
> multi-agent manipulation problems. Experiments show that our method outperforms
> existing constrained motion planners and operates at speeds suitable for
> real-world applications. Video demonstrations are available at
> https://youtu.be/RYcEHMnPTH8 .

