---
layout: default
title: Learning Robust Agile Flight Control with Stability Guarantees
---

# Learning Robust Agile Flight Control with Stability Guarantees

**arXiv**: [2510.12611v1](https://arxiv.org/abs/2510.12611) | [PDF](https://arxiv.org/pdf/2510.12611.pdf)

**作者**: Lukas Pries, Markus Ryll

---

## 💡 一句话要点

**提出神经增强反馈控制器以解决高速敏捷四旋翼飞行中的轨迹跟踪问题**

**关键词**: `敏捷飞行控制` `神经增强控制器` `稳定性保证` `轨迹跟踪` `鲁棒控制`

## 📋 核心要点

1. 核心问题：高速敏捷四旋翼飞行需在操作极限下精确跟踪轨迹，同时处理执行器约束和扰动。
2. 方法要点：结合现有控制范式优势，设计非线性反馈结构，提供通用稳定性保证。
3. 实验或效果：在仿真中快速稳定学习，无需调优即可部署到真实平台，提升鲁棒性和跟踪性能。

## 📄 摘要（原文）

> In the evolving landscape of high-speed agile quadrotor flight, achieving
> precise trajectory tracking at the platform's operational limits is paramount.
> Controllers must handle actuator constraints, exhibit robustness to
> disturbances, and remain computationally efficient for safety-critical
> applications. In this work, we present a novel neural-augmented feedback
> controller for agile flight control. The controller addresses individual
> limitations of existing state-of-the-art control paradigms and unifies their
> strengths. We demonstrate the controller's capabilities, including the accurate
> tracking of highly aggressive trajectories that surpass the feasibility of the
> actuators. Notably, the controller provides universal stability guarantees,
> enhancing its robustness and tracking performance even in exceedingly
> disturbance-prone settings. Its nonlinear feedback structure is highly
> efficient enabling fast computation at high update rates. Moreover, the
> learning process in simulation is both fast and stable, and the controller's
> inherent robustness allows direct deployment to real-world platforms without
> the need for training augmentations or fine-tuning.

