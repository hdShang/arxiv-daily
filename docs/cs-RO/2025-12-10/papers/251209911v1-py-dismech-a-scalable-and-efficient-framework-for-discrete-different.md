---
layout: default
title: Py-DiSMech: A Scalable and Efficient Framework for Discrete Differential Geometry-Based Modeling and Control of Soft Robots
---

# Py-DiSMech: A Scalable and Efficient Framework for Discrete Differential Geometry-Based Modeling and Control of Soft Robots

**arXiv**: [2512.09911v1](https://arxiv.org/abs/2512.09911) | [PDF](https://arxiv.org/pdf/2512.09911.pdf)

**作者**: Radha Lahoti, Ryan Chaiyakul, M. Khalid Jawed

---

## 💡 一句话要点

**提出Py-DiSMech框架，基于离散微分几何实现软机器人高效建模与控制**

**关键词**: `软机器人仿真` `离散微分几何` `高效建模` `隐式接触模型` `形状控制` `开源框架`

## 📋 核心要点

1. 核心问题：软机器人仿真需高保真度、可扩展性，传统工具难以处理大变形和复杂接触。
2. 方法要点：采用离散微分几何直接离散化曲率与应变，结合向量化NumPy实现和隐式接触模型。
3. 实验或效果：在计算效率上显著超越Elastica，保持物理准确性，支持仿真驱动设计和控制验证。

## 📄 摘要（原文）

> High-fidelity simulation has become essential to the design and control of soft robots, where large geometric deformations and complex contact interactions challenge conventional modeling tools. Recent advances in the field demand simulation frameworks that combine physical accuracy, computational scalability, and seamless integration with modern control and optimization pipelines. In this work, we present Py-DiSMech, a Python-based, open-source simulation framework for modeling and control of soft robotic structures grounded in the principles of Discrete Differential Geometry (DDG). By discretizing geometric quantities such as curvature and strain directly on meshes, Py-DiSMech captures the nonlinear deformation of rods, shells, and hybrid structures with high fidelity and reduced computational cost. The framework introduces (i) a fully vectorized NumPy implementation achieving order-of-magnitude speed-ups over existing geometry-based simulators; (ii) a penalty-energy-based fully implicit contact model that supports rod-rod, rod-shell, and shell-shell interactions; (iii) a natural-strain-based feedback-control module featuring a proportional-integral (PI) controller for shape regulation and trajectory tracking; and (iv) a modular, object-oriented software design enabling user-defined elastic energies, actuation schemes, and integration with machine-learning libraries. Benchmark comparisons demonstrate that Py-DiSMech substantially outperforms the state-of-the-art simulator Elastica in computational efficiency while maintaining physical accuracy. Together, these features establish Py-DiSMech as a scalable, extensible platform for simulation-driven design, control validation, and sim-to-real research in soft robotics.

