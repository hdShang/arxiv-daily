---
layout: default
title: Homogeneous Proportional-Integral-Derivative Controller in Mobile Robotic Manipulators
---

# Homogeneous Proportional-Integral-Derivative Controller in Mobile Robotic Manipulators

**arXiv**: [2511.16406v1](https://arxiv.org/abs/2511.16406) | [PDF](https://arxiv.org/pdf/2511.16406.pdf)

**作者**: Luis Luna, Isaac Chairez, Andrey Polyakov

---

## 💡 一句话要点

**提出同质PID控制器以解决移动机器人操纵器的非线性控制挑战**

**关键词**: `移动机器人操纵器` `同质控制` `PID控制器` `非线性控制` `轨迹跟踪` `稳定性分析`

## 📋 核心要点

1. 移动机器人操纵器存在非线性动力学、欠驱动和子系统耦合等控制难题
2. 基于同质控制理论设计非线性PID，提升系统稳定性和收敛性
3. 实验验证控制器在轨迹跟踪中优于传统PID，响应更快、误差更小

## 📄 摘要（原文）

> Mobile robotic manipulators (MRMs), which integrate mobility and manipulation capabilities, present significant control challenges due to their nonlinear dynamics, underactuation, and coupling between the base and manipulator subsystems. This paper proposes a novel homogeneous Proportional-Integral-Derivative (hPID) control strategy tailored for MRMs to achieve robust and coordinated motion control. Unlike classical PID controllers, the hPID controller leverages the mathematical framework of homogeneous control theory to systematically enhance the stability and convergence properties of the closed-loop system, even in the presence of dynamic uncertainties and external disturbances involved into a system in a homogeneous way. A homogeneous PID structure is designed, ensuring improved convergence of tracking errors through a graded homogeneity approach that generalizes traditional PID gains to nonlinear, state-dependent functions. Stability analysis is conducted using Lyapunov-based methods, demonstrating that the hPID controller guarantees global asymptotic stability and finite-time convergence under mild assumptions. Experimental results on a representative MRM model validate the effectiveness of the hPID controller in achieving high-precision trajectory tracking for both the mobile base and manipulator arm, outperforming conventional linear PID controllers in terms of response time, steady-state error, and robustness to model uncertainties. This research contributes a scalable and analytically grounded control framework for enhancing the autonomy and reliability of next-generation mobile manipulation systems in structured and unstructured environments.

