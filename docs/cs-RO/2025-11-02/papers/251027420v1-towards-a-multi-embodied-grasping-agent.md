---
layout: default
title: Towards a Multi-Embodied Grasping Agent
---

# Towards a Multi-Embodied Grasping Agent

**arXiv**: [2510.27420v1](https://arxiv.org/abs/2510.27420) | [PDF](https://arxiv.org/pdf/2510.27420.pdf)

**作者**: Roman Freiberg, Alexander Qualmann, Ngo Anh Vien, Gerhard Neumann

---

## 💡 一句话要点

**提出数据高效、流式等变抓取架构，以处理多类型抓取器并提升性能。**

**关键词**: `多抓取器抓取` `等变抓取合成` `数据高效学习` `JAX实现` `批量处理` `抓取数据集`

## 📋 核心要点

1. 核心问题：多抓取器抓取需大规模数据，现有方法隐含学习运动结构，数据获取困难。
2. 方法要点：基于流式等变抓取合成，从抓取器和场景几何推断运动模型，支持批量处理。
3. 实验或效果：使用JAX实现，学习更平滑、性能提升、推理更快，数据集含25,000场景和2千万抓取。

## 📄 摘要（原文）

> Multi-embodiment grasping focuses on developing approaches that exhibit
> generalist behavior across diverse gripper designs. Existing methods often
> learn the kinematic structure of the robot implicitly and face challenges due
> to the difficulty of sourcing the required large-scale data. In this work, we
> present a data-efficient, flow-based, equivariant grasp synthesis architecture
> that can handle different gripper types with variable degrees of freedom and
> successfully exploit the underlying kinematic model, deducing all necessary
> information solely from the gripper and scene geometry. Unlike previous
> equivariant grasping methods, we translated all modules from the ground up to
> JAX and provide a model with batching capabilities over scenes, grippers, and
> grasps, resulting in smoother learning, improved performance and faster
> inference time. Our dataset encompasses grippers ranging from humanoid hands to
> parallel yaw grippers and includes 25,000 scenes and 20 million grasps.

