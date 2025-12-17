---
layout: default
title: Force-Safe Environment Maps and Real-Time Detection for Soft Robot Manipulators
---

# Force-Safe Environment Maps and Real-Time Detection for Soft Robot Manipulators

**arXiv**: [2511.05307v1](https://arxiv.org/abs/2511.05307) | [PDF](https://arxiv.org/pdf/2511.05307.pdf)

**作者**: Akua K. Dickson, Juan C. Pacheco Garcia, Andrew P. Sabelhaus

---

## 💡 一句话要点

**提出力安全环境映射与实时检测框架，用于软体机器人操作器在精细环境中的安全交互。**

**关键词**: `软体机器人操作器` `力安全检测` `环境映射` `实时规划` `配置空间` `任务空间`

## 📋 核心要点

1. 现有方法未考虑软体机器人接触精细障碍物时的力限制问题。
2. 将任务空间力安全标准映射到配置空间，实现实时力安全检测。
3. 仿真和硬件实验验证方法能准确检测与可变形障碍物交互时的力安全。

## 📄 摘要（原文）

> Soft robot manipulators have the potential for deployment in delicate
> environments to perform complex manipulation tasks. However, existing obstacle
> detection and avoidance methods do not consider limits on the forces that
> manipulators may exert upon contact with delicate obstacles. This work
> introduces a framework that maps force safety criteria from task space (i.e.
> positions along the robot's body) to configuration space (i.e. the robot's
> joint angles) and enables real-time force safety detection. We incorporate
> limits on allowable environmental contact forces for given task-space
> obstacles, and map them into configuration space (C-space) through the
> manipulator's forward kinematics. This formulation ensures that configurations
> classified as safe are provably below the maximum force thresholds, thereby
> allowing us to determine force-safe configurations of the soft robot
> manipulator in real-time. We validate our approach in simulation and hardware
> experiments on a two-segment pneumatic soft robot manipulator. Results
> demonstrate that the proposed method accurately detects force safety during
> interactions with deformable obstacles, thereby laying the foundation for
> real-time safe planning of soft manipulators in delicate, cluttered
> environments.

