---
layout: default
title: Bayesian Optimization for Automatic Tuning of Torque-Level Nonlinear Model Predictive Control
---

# Bayesian Optimization for Automatic Tuning of Torque-Level Nonlinear Model Predictive Control

**arXiv**: [2512.03772v1](https://arxiv.org/abs/2512.03772) | [PDF](https://arxiv.org/pdf/2512.03772.pdf)

**作者**: Gabriele Fadini, Deepak Ingole, Tong Duy Son, Alisa Rupenyan

---

## 💡 一句话要点

**提出基于贝叶斯优化的扭矩级非线性模型预测控制自动调参框架，以提升机器人轨迹跟踪性能。**

**关键词**: `贝叶斯优化` `非线性模型预测控制` `自动调参` `机器人控制` `数字孪生` `轨迹跟踪`

## 📋 核心要点

1. 核心问题：扭矩级非线性模型预测控制参数手动调优困难，影响机器人末端执行器轨迹跟踪精度。
2. 方法要点：采用高维贝叶斯优化（SAASBO）结合数字孪生，自动优化MPC成本函数权重和低层控制器增益。
3. 实验或效果：仿真中跟踪性能提升41.9%，求解时间减少2.5%；真实机器人实验验证了25.8%的改进趋势。

## 📄 摘要（原文）

> This paper presents an auto-tuning framework for torque-based Nonlinear Model Predictive Control (nMPC), where the MPC serves as a real-time controller for optimal joint torque commands. The MPC parameters, including cost function weights and low-level controller gains, are optimized using high-dimensional Bayesian Optimization (BO) techniques, specifically Sparse Axis-Aligned Subspace (SAASBO) with a digital twin (DT) to achieve precise end-effector trajectory real-time tracking on an UR10e robot arm. The simulation model allows efficient exploration of the high-dimensional parameter space, and it ensures safe transfer to hardware. Our simulation results demonstrate significant improvements in tracking performance (+41.9%) and reduction in solve times (-2.5%) compared to manually-tuned parameters. Moreover, experimental validation on the real robot follows the trend (with a +25.8% improvement), emphasizing the importance of digital twin-enabled automated parameter optimization for robotic operations.

