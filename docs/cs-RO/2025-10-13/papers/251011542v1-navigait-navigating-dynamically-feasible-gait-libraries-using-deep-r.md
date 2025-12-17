---
layout: default
title: NaviGait: Navigating Dynamically Feasible Gait Libraries using Deep Reinforcement Learning
---

# NaviGait: Navigating Dynamically Feasible Gait Libraries using Deep Reinforcement Learning

**arXiv**: [2510.11542v1](https://arxiv.org/abs/2510.11542) | [PDF](https://arxiv.org/pdf/2510.11542.pdf)

**作者**: Neil C. Janwani, Varun Madabushi, Maegan Tucker

---

## 💡 一句话要点

**提出NaviGait框架，结合轨迹优化与强化学习，实现稳健双足运动控制。**

**关键词**: `双足运动控制` `强化学习` `轨迹优化` `步态库` `残差修正`

## 📋 核心要点

1. 核心问题：强化学习奖励设计复杂，轨迹优化方法对扰动脆弱。
2. 方法要点：利用离线优化步态库，插值生成参考运动并添加残差修正。
3. 实验或效果：训练更快，运动更接近参考，提升稳健性和可解释性。

## 📄 摘要（原文）

> Reinforcement learning (RL) has emerged as a powerful method to learn robust
> control policies for bipedal locomotion. Yet, it can be difficult to tune
> desired robot behaviors due to unintuitive and complex reward design. In
> comparison, offline trajectory optimization methods, like Hybrid Zero Dynamics,
> offer more tuneable, interpretable, and mathematically grounded motion plans
> for high-dimensional legged systems. However, these methods often remain
> brittle to real-world disturbances like external perturbations.
>   In this work, we present NaviGait, a hierarchical framework that combines the
> structure of trajectory optimization with the adaptability of RL for robust and
> intuitive locomotion control. NaviGait leverages a library of offline-optimized
> gaits and smoothly interpolates between them to produce continuous reference
> motions in response to high-level commands. The policy provides both
> joint-level and velocity command residual corrections to modulate and stabilize
> the reference trajectories in the gait library. One notable advantage of
> NaviGait is that it dramatically simplifies reward design by encoding rich
> motion priors from trajectory optimization, reducing the need for finely tuned
> shaping terms and enabling more stable and interpretable learning. Our
> experimental results demonstrate that NaviGait enables faster training compared
> to conventional and imitation-based RL, and produces motions that remain
> closest to the original reference. Overall, by decoupling high-level motion
> generation from low-level correction, NaviGait offers a more scalable and
> generalizable approach for achieving dynamic and robust locomotion.

