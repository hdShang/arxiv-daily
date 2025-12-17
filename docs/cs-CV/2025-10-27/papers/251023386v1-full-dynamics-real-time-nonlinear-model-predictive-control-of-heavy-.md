---
layout: default
title: Full-Dynamics Real-Time Nonlinear Model Predictive Control of Heavy-Duty Hydraulic Manipulator for Trajectory Tracking Tasks
---

# Full-Dynamics Real-Time Nonlinear Model Predictive Control of Heavy-Duty Hydraulic Manipulator for Trajectory Tracking Tasks

**arXiv**: [2510.23386v1](https://arxiv.org/abs/2510.23386) | [PDF](https://arxiv.org/pdf/2510.23386.pdf)

**作者**: Alvaro Paz, Mahdi Hejrati, Pauli Mustalahti, Jouni Mattila

---

## 💡 一句话要点

**提出非线性模型预测控制框架，用于重型液压机械臂实时轨迹跟踪，确保约束满足。**

**关键词**: `非线性模型预测控制` `重型液压机械臂` `轨迹跟踪` `约束满足` `实时控制` `虚拟分解控制`

## 📋 核心要点

1. 重型液压机械臂在严格物理约束下操作，实时控制中约束满足问题未充分探索。
2. 结合多射击策略与实时传感器反馈，采用虚拟分解控制实现精确关节跟踪。
3. 实验验证框架在关节和笛卡尔空间均满足约束，实现高精度轨迹跟踪。

## 📄 摘要（原文）

> Heavy-duty hydraulic manipulators (HHMs) operate under strict physical and
> safety-critical constraints due to their large size, high power, and complex
> nonlinear dynamics. Ensuring that both joint-level and end-effector
> trajectories remain compliant with actuator capabilities, such as force,
> velocity, and position limits, is essential for safe and reliable operation,
> yet remains largely underexplored in real-time control frameworks. This paper
> presents a nonlinear model predictive control (NMPC) framework designed to
> guarantee constraint satisfaction throughout the full nonlinear dynamics of
> HHMs, while running at a real-time control frequency of 1 kHz. The proposed
> method combines a multiple-shooting strategy with real-time sensor feedback,
> and is supported by a robust low-level controller based on virtual
> decomposition control (VDC) for precise joint tracking. Experimental validation
> on a full-scale hydraulic manipulator shows that the NMPC framework not only
> enforces actuator constraints at the joint level, but also ensures
> constraint-compliant motion in Cartesian space for the end-effector. These
> results demonstrate the method's capability to deliver high-accuracy trajectory
> tracking while strictly respecting safety-critical limits, setting a new
> benchmark for real-time control in large-scale hydraulic systems.

