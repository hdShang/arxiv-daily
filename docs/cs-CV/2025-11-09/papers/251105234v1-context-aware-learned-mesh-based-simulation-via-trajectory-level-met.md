---
layout: default
title: Context-aware Learned Mesh-based Simulation via Trajectory-Level Meta-Learning
---

# Context-aware Learned Mesh-based Simulation via Trajectory-Level Meta-Learning

**arXiv**: [2511.05234v1](https://arxiv.org/abs/2511.05234) | [PDF](https://arxiv.org/pdf/2511.05234.pdf)

**作者**: Philipp Dahlinger, Niklas Freymuth, Tai Hoang, Tobias Würth, Michael Volpp, Luise Kärger, Gerhard Neumann

---

## 💡 一句话要点

**提出M3GN方法以解决网格模拟中缺乏时间上下文和误差累积问题**

**关键词**: `网格模拟` `轨迹级元学习` `条件神经过程` `运动基元` `学习图网络模拟器`

## 📋 核心要点

1. 核心问题：现有学习模拟器依赖单步观测，无法推断材料属性，且自回归推演误差累积
2. 方法要点：采用轨迹级元学习和条件神经过程，从有限数据快速适应新场景
3. 实验或效果：在多个任务中，相比先进GNS，精度更高且运行成本大幅降低

## 📄 摘要（原文）

> Simulating object deformations is a critical challenge across many scientific
> domains, including robotics, manufacturing, and structural mechanics. Learned
> Graph Network Simulators (GNSs) offer a promising alternative to traditional
> mesh-based physics simulators. Their speed and inherent differentiability make
> them particularly well suited for applications that require fast and accurate
> simulations, such as robotic manipulation or manufacturing optimization.
> However, existing learned simulators typically rely on single-step
> observations, which limits their ability to exploit temporal context. Without
> this information, these models fail to infer, e.g., material properties.
> Further, they rely on auto-regressive rollouts, which quickly accumulate error
> for long trajectories. We instead frame mesh-based simulation as a
> trajectory-level meta-learning problem. Using Conditional Neural Processes, our
> method enables rapid adaptation to new simulation scenarios from limited
> initial data while capturing their latent simulation properties. We utilize
> movement primitives to directly predict fast, stable and accurate simulations
> from a single model call. The resulting approach, Movement-primitive
> Meta-MeshGraphNet (M3GN), provides higher simulation accuracy at a fraction of
> the runtime cost compared to state-of-the-art GNSs across several tasks.

