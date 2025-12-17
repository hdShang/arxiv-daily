---
layout: default
title: Nonholonomic Robot Parking by Feedback -- Part I: Modular Strict CLF Designs
---

# Nonholonomic Robot Parking by Feedback -- Part I: Modular Strict CLF Designs

**arXiv**: [2511.15119v1](https://arxiv.org/abs/2511.15119) | [PDF](https://arxiv.org/pdf/2511.15119.pdf)

**作者**: Velimir Todorovski, Kwang Hak Kim, Alessandro Astolfi, Miroslav Krstic

---

## 💡 一句话要点

**提出模块化严格CLF设计框架，以解决非完整独轮车机器人停车问题。**

**关键词**: `非完整机器人控制` `控制Lyapunov函数` `模块化设计` `反馈稳定` `机器人停车` `渐近稳定性`

## 📋 核心要点

1. 核心问题：非完整独轮车在极坐标下的渐近稳定控制，已知可平滑反馈全局稳定。
2. 方法要点：模块化设计分离径向坐标，使用无源性、反步法和积分前馈构建反馈律。
3. 实验或效果：严格CLF提供KL收敛估计和特征值分配，支持角度约束和后续优化。

## 📄 摘要（原文）

> It has been known in the robotics literature since about 1995 that, in polar coordinates, the nonholonomic unicycle is asymptotically stabilizable by smooth feedback, even globally. We introduce a modular design framework that selects the forward velocity to decouple the radial coordinate, allowing the steering subsystem to be stabilized independently. Within this structure, we develop families of feedback laws using passivity, backstepping, and integrator forwarding. Each law is accompanied by a strict control Lyapunov function, including barrier variants that enforce angular constraints. These strict CLFs provide constructive class KL convergence estimates and enable eigenvalue assignment at the target equilibrium. The framework generalizes and extends prior modular and nonmodular approaches, while preparing the ground for inverse optimal and adaptive redesigns in the sequel paper.

