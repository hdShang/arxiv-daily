---
layout: default
title: Controllable Collision Scenario Generation via Collision Pattern Prediction
---

# Controllable Collision Scenario Generation via Collision Pattern Prediction

**arXiv**: [2510.12206v1](https://arxiv.org/abs/2510.12206) | [PDF](https://arxiv.org/pdf/2510.12206.pdf)

**作者**: Pin-Lun Chen, Chi-Hsi Kung, Che-Han Chang, Wei-Chen Chiu, Yi-Ting Chen

---

## 💡 一句话要点

**提出可控碰撞场景生成框架，通过预测碰撞模式实现指定碰撞类型与时间**

**关键词**: `自动驾驶安全` `碰撞场景生成` `可控模拟` `碰撞模式预测` `规划器评估`

## 📋 核心要点

1. 核心问题：自动驾驶安全评估需多样碰撞场景，但真实收集困难且模拟中控制属性如碰撞类型和时间具挑战性
2. 方法要点：构建COLLIDE数据集，预测碰撞模式以紧凑表示空间配置，再生成完整对抗轨迹
3. 实验或效果：方法在碰撞率和可控性上优于基线，生成场景提高规划器失败率并增强其鲁棒性

## 📄 摘要（原文）

> Evaluating the safety of autonomous vehicles (AVs) requires diverse,
> safety-critical scenarios, with collisions being especially important yet rare
> and unsafe to collect in the real world. Therefore, the community has been
> focusing on generating safety-critical scenarios in simulation. However,
> controlling attributes such as collision type and time-to-accident (TTA)
> remains challenging. We introduce a new task called controllable collision
> scenario generation, where the goal is to produce trajectories that realize a
> user-specified collision type and TTA, to investigate the feasibility of
> automatically generating desired collision scenarios. To support this task, we
> present COLLIDE, a large-scale collision scenario dataset constructed by
> transforming real-world driving logs into diverse collisions, balanced across
> five representative collision types and different TTA intervals. We propose a
> framework that predicts Collision Pattern, a compact and interpretable
> representation that captures the spatial configuration of the ego and the
> adversarial vehicles at impact, before rolling out full adversarial
> trajectories. Experiments show that our approach outperforms strong baselines
> in both collision rate and controllability. Furthermore, generated scenarios
> consistently induce higher planner failure rates, revealing limitations of
> existing planners. We demonstrate that these scenarios fine-tune planners for
> robustness improvements, contributing to safer AV deployment in different
> collision scenarios.

