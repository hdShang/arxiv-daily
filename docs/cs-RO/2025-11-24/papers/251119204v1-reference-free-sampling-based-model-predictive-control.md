---
layout: default
title: Reference-Free Sampling-Based Model Predictive Control
---

# Reference-Free Sampling-Based Model Predictive Control

**arXiv**: [2511.19204v1](https://arxiv.org/abs/2511.19204) | [PDF](https://arxiv.org/pdf/2511.19204.pdf)

**作者**: Fabian Schramm, Pierre Fabre, Nicolas Perrin-Gilbert, Justin Carpentier

---

## 💡 一句话要点

**提出无参考采样模型预测控制框架，实现四足机器人涌现运动**

**关键词**: `模型预测控制` `采样优化` `四足机器人` `涌现运动` `实时控制`

## 📋 核心要点

1. 核心问题：模型预测控制依赖预设步态或接触序列，限制运动多样性。
2. 方法要点：基于MPPI，采用双空间样条参数化，优化高层目标自动发现运动。
3. 实验效果：在Go2机器人上验证涌现步态和跳跃，仿真中实现后空翻等复杂行为。

## 📄 摘要（原文）

> We present a sampling-based model predictive control (MPC) framework that enables emergent locomotion without relying on handcrafted gait patterns or predefined contact sequences. Our method discovers diverse motion patterns, ranging from trotting to galloping, robust standing policies, jumping, and handstand balancing, purely through the optimization of high-level objectives. Building on model predictive path integral (MPPI), we propose a dual-space spline parameterization that operates on position and velocity control points. Our approach enables contact-making and contact-breaking strategies that adapt automatically to task requirements, requiring only a limited number of sampled trajectories. This sample efficiency allows us to achieve real-time control on standard CPU hardware, eliminating the need for GPU acceleration typically required by other state-of-the-art MPPI methods. We validate our approach on the Go2 quadrupedal robot, demonstrating various emergent gaits and basic jumping capabilities. In simulation, we further showcase more complex behaviors, such as backflips, dynamic handstand balancing and locomotion on a Humanoid, all without requiring reference tracking or offline pre-training.

