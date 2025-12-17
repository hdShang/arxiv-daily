---
layout: default
title: RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning
---

# RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning

**arXiv**: [2510.14830v1](https://arxiv.org/abs/2510.14830) | [PDF](https://arxiv.org/pdf/2510.14830.pdf)

**作者**: Kun Lei, Huanyu Li, Dongjie Yu, Zhenyu Wei, Lingxiao Guo, Zhennan Jiang, Ziyu Wang, Shiyu Liang, Huazhe Xu

---

## 💡 一句话要点

**提出RL-100框架，通过三阶段强化学习实现真实世界机器人操作的高性能。**

**关键词**: `机器人操作` `强化学习` `扩散策略` `离线策略评估` `一致性蒸馏` `真实世界应用`

## 📋 核心要点

1. 核心问题：真实世界机器人操作需高可靠性、效率和鲁棒性，以接近或超越人类操作员。
2. 方法要点：采用模仿学习、离线强化学习和在线强化学习三阶段管道，结合扩散策略和一致性蒸馏。
3. 实验或效果：在七项任务中实现100%成功率，共900次试验，并展示多小时不间断操作。

## 📄 摘要（原文）

> Real-world robotic manipulation in homes and factories demands reliability,
> efficiency, and robustness that approach or surpass skilled human operators. We
> present RL-100, a real-world reinforcement learning training framework built on
> diffusion visuomotor policies trained bu supervised learning. RL-100 introduces
> a three-stage pipeline. First, imitation learning leverages human priors.
> Second, iterative offline reinforcement learning uses an Offline Policy
> Evaluation procedure, abbreviated OPE, to gate PPO-style updates that are
> applied in the denoising process for conservative and reliable improvement.
> Third, online reinforcement learning eliminates residual failure modes. An
> additional lightweight consistency distillation head compresses the multi-step
> sampling process in diffusion into a single-step policy, enabling
> high-frequency control with an order-of-magnitude reduction in latency while
> preserving task performance. The framework is task-, embodiment-, and
> representation-agnostic and supports both 3D point clouds and 2D RGB inputs, a
> variety of robot platforms, and both single-step and action-chunk policies. We
> evaluate RL-100 on seven real-robot tasks spanning dynamic rigid-body control,
> such as Push-T and Agile Bowling, fluids and granular pouring, deformable cloth
> folding, precise dexterous unscrewing, and multi-stage orange juicing. RL-100
> attains 100\% success across evaluated trials for a total of 900 out of 900
> episodes, including up to 250 out of 250 consecutive trials on one task. The
> method achieves near-human teleoperation or better time efficiency and
> demonstrates multi-hour robustness with uninterrupted operation lasting up to
> two hours.

