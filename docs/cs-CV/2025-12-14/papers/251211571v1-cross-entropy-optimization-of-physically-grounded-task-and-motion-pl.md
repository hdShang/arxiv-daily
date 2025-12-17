---
layout: default
title: Cross-Entropy Optimization of Physically Grounded Task and Motion Plans
---

# Cross-Entropy Optimization of Physically Grounded Task and Motion Plans

**arXiv**: [2512.11571v1](https://arxiv.org/abs/2512.11571) | [PDF](https://arxiv.org/pdf/2512.11571.pdf)

**作者**: Andreu Matoses Gimenez, Nils Wilde, Chris Pek, Javier Alonso-Mora

---

## 💡 一句话要点

**提出基于交叉熵优化的物理仿真方法，以解决机器人任务与运动规划中的动态和接触问题。**

**关键词**: `任务与运动规划` `物理仿真` `交叉熵优化` `GPU并行计算` `机器人控制`

## 📋 核心要点

1. 核心问题：传统TAMP算法因简化可能忽略动态和接触，导致规划不可靠或不可行。
2. 方法要点：使用GPU并行物理仿真计算规划实现，结合交叉熵优化采样控制器参数以获取低成本解。
3. 实验或效果：在机器人利用环境几何移动物体的任务中，规划可直接执行，提升可靠性。

## 📄 摘要（原文）

> Autonomously performing tasks often requires robots to plan high-level discrete actions and continuous low-level motions to realize them. Previous TAMP algorithms have focused mainly on computational performance, completeness, or optimality by making the problem tractable through simplifications and abstractions. However, this comes at the cost of the resulting plans potentially failing to account for the dynamics or complex contacts necessary to reliably perform the task when object manipulation is required. Additionally, approaches that ignore effects of the low-level controllers may not obtain optimal or feasible plan realizations for the real system. We investigate the use of a GPU-parallelized physics simulator to compute realizations of plans with motion controllers, explicitly accounting for dynamics, and considering contacts with the environment. Using cross-entropy optimization, we sample the parameters of the controllers, or actions, to obtain low-cost solutions. Since our approach uses the same controllers as the real system, the robot can directly execute the computed plans. We demonstrate our approach for a set of tasks where the robot is able to exploit the environment's geometry to move an object. Website and code: https://andreumatoses.github.io/research/parallel-realization

