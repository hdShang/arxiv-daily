---
layout: default
title: GET-USE: Learning Generalized Tool Usage for Bimanual Mobile Manipulation via Simulated Embodiment Extensions
---

# GET-USE: Learning Generalized Tool Usage for Bimanual Mobile Manipulation via Simulated Embodiment Extensions

**arXiv**: [2510.25754v1](https://arxiv.org/abs/2510.25754) | [PDF](https://arxiv.org/pdf/2510.25754.pdf)

**作者**: Bohan Wu, Paul de La Sayette, Li Fei-Fei, Roberto Martín-Martín

---

## 💡 一句话要点

**提出GeT-USE方法，通过模拟扩展机器人具身学习通用工具使用，提升双手机器人移动操作能力。**

**关键词**: `机器人工具使用` `具身扩展学习` `模拟到真实迁移` `双手机器人操作` `几何知识蒸馏`

## 📋 核心要点

1. 核心问题：现有方法无法从多个对象中选择最佳工具，且依赖单一对象假设。
2. 方法要点：在模拟中学习机器人具身扩展，识别有益任务几何，并迁移到真实机器人。
3. 实验效果：在真实机器人上，成功率比先进方法高30-60%，覆盖三个视觉任务。

## 📄 摘要（原文）

> The ability to use random objects as tools in a generalizable manner is a
> missing piece in robots' intelligence today to boost their versatility and
> problem-solving capabilities. State-of-the-art robotic tool usage methods
> focused on procedurally generating or crowd-sourcing datasets of tools for a
> task to learn how to grasp and manipulate them for that task. However, these
> methods assume that only one object is provided and that it is possible, with
> the correct grasp, to perform the task; they are not capable of identifying,
> grasping, and using the best object for a task when many are available,
> especially when the optimal tool is absent. In this work, we propose GeT-USE, a
> two-step procedure that learns to perform real-robot generalized tool usage by
> learning first to extend the robot's embodiment in simulation and then
> transferring the learned strategies to real-robot visuomotor policies. Our key
> insight is that by exploring a robot's embodiment extensions (i.e., building
> new end-effectors) in simulation, the robot can identify the general tool
> geometries most beneficial for a task. This learned geometric knowledge can
> then be distilled to perform generalized tool usage tasks by selecting and
> using the best available real-world object as tool. On a real robot with 22
> degrees of freedom (DOFs), GeT-USE outperforms state-of-the-art methods by
> 30-60% success rates across three vision-based bimanual mobile manipulation
> tool-usage tasks.

