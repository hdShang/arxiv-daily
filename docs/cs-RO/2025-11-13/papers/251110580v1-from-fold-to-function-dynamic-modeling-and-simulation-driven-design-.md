---
layout: default
title: From Fold to Function: Dynamic Modeling and Simulation-Driven Design of Origami Mechanisms
---

# From Fold to Function: Dynamic Modeling and Simulation-Driven Design of Origami Mechanisms

**arXiv**: [2511.10580v1](https://arxiv.org/abs/2511.10580) | [PDF](https://arxiv.org/pdf/2511.10580.pdf)

**作者**: Tianhui Han, Shashwat Singh, Sarvesh Patil, Zeynep Temel

---

## 💡 一句话要点

**提出基于MuJoCo的折纸机制仿真框架，以解决动态建模和优化设计问题。**

**关键词**: `折纸机制仿真` `可变形体建模` `优化设计` `MuJoCo框架` `物理仿真`

## 📋 核心要点

1. 核心问题：折纸机制在环境和交互中的精确仿真仍具挑战性。
2. 方法要点：使用图形界面定义约束，结合MuJoCo进行可变形体仿真。
3. 实验或效果：通过折纸弹射器案例优化参数，实验验证性能提升。

## 📄 摘要（原文）

> Origami-inspired mechanisms can transform flat sheets into functional three-dimensional dynamic structures that are lightweight, compact, and capable of complex motion. These properties make origami increasingly valuable in robotic and deployable systems. However, accurately simulating their folding behavior and interactions with the environment remains challenging. To address this, we present a design framework for origami mechanism simulation that utilizes MuJoCo's deformable-body capabilities. In our approach, origami sheets are represented as graphs of interconnected deformable elements with user-specified constraints such as creases and actuation, defined through an intuitive graphical user interface (GUI). This framework allows users to generate physically consistent simulations that capture both the geometric structure of origami mechanisms and their interactions with external objects and surfaces. We demonstrate our method's utility through a case study on an origami catapult, where design parameters are optimized in simulation using the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) and validated experimentally on physical prototypes. The optimized structure achieves improved throwing performance, illustrating how our system enables rapid, simulation-driven origami design, optimization, and analysis.

