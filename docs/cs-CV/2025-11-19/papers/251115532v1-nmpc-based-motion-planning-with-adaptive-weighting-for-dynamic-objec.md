---
layout: default
title: NMPC-based Motion Planning with Adaptive Weighting for Dynamic Object Interception
---

# NMPC-based Motion Planning with Adaptive Weighting for Dynamic Object Interception

**arXiv**: [2511.15532v1](https://arxiv.org/abs/2511.15532) | [PDF](https://arxiv.org/pdf/2511.15532.pdf)

**作者**: Chen Cai, Saksham Kohli, Steven Liu

---

## 💡 一句话要点

**提出自适应终端非线性MPC运动规划器，用于双协作臂动态物体拦截。**

**关键词**: `非线性模型预测控制` `协作机器人` `动态物体拦截` `运动规划` `自适应控制`

## 📋 核心要点

1. 核心问题：协作臂系统在闭环约束下拦截快速移动物体，面临协调挑战和致动器功率限制。
2. 方法要点：采用自适应终端MPC，通过成本塑形减少对终端惩罚的依赖，优化轨迹和控制努力。
3. 实验或效果：实验显示平均规划周期19ms，运动质量和鲁棒性显著提升，优于原始终端方法。

## 📄 摘要（原文）

> Catching fast-moving objects serves as a benchmark for robotic agility, posing significant coordination challenges for cooperative manipulator systems holding a catcher, particularly due to inherent closed-chain constraints. This paper presents a nonlinear model predictive control (MPC)-based motion planner that bridges high-level interception planning with real-time joint space control, enabling dynamic object interception for systems comprising two cooperating arms. We introduce an Adaptive- Terminal (AT) MPC formulation featuring cost shaping, which contrasts with a simpler Primitive-Terminal (PT) approach relying heavily on terminal penalties for rapid convergence. The proposed AT formulation is shown to effectively mitigate issues related to actuator power limit violations frequently encountered with the PT strategy, yielding trajectories and significantly reduced control effort. Experimental results on a robotic platform with two cooperative arms, demonstrating excellent real time performance, with an average planner cycle computation time of approximately 19 ms-less than half the 40 ms system sampling time. These results indicate that the AT formulation achieves significantly improved motion quality and robustness with minimal computational overhead compared to the PT baseline, making it well-suited for dynamic, cooperative interception tasks.

