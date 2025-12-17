---
layout: default
title: Sim-to-Real Gentle Manipulation of Deformable and Fragile Objects with Stress-Guided Reinforcement Learning
---

# Sim-to-Real Gentle Manipulation of Deformable and Fragile Objects with Stress-Guided Reinforcement Learning

**arXiv**: [2510.25405v1](https://arxiv.org/abs/2510.25405) | [PDF](https://arxiv.org/pdf/2510.25405.pdf)

**作者**: Kei Ikemura, Yifei Dong, David Blanco-Mulero, Alberta Longhini, Li Chen, Florian T. Pokorny

---

## 💡 一句话要点

**提出应力引导强化学习方法，实现模拟到真实世界中对易变形和易碎物体的轻柔操作**

**关键词**: `机器人操作` `强化学习` `模拟到真实迁移` `应力引导` `易碎物体` `课程学习`

## 📋 核心要点

1. 核心问题：机器人操作易变形和易碎物体时，应力过大易导致不可逆损伤，现有方法依赖精确模型或专用设备，泛化性差。
2. 方法要点：采用基于视觉的强化学习，引入应力惩罚奖励，结合离线演示和从刚性代理到易变形物体的课程学习。
3. 实验或效果：在模拟和真实世界评估中，零样本迁移策略降低应力36.5%，实现任务目标并展示轻柔操作行为。

## 📄 摘要（原文）

> Robotic manipulation of deformable and fragile objects presents significant
> challenges, as excessive stress can lead to irreversible damage to the object.
> While existing solutions rely on accurate object models or specialized sensors
> and grippers, this adds complexity and often lacks generalization. To address
> this problem, we present a vision-based reinforcement learning approach that
> incorporates a stress-penalized reward to discourage damage to the object
> explicitly. In addition, to bootstrap learning, we incorporate offline
> demonstrations as well as a designed curriculum progressing from rigid proxies
> to deformables. We evaluate the proposed method in both simulated and
> real-world scenarios, showing that the policy learned in simulation can be
> transferred to the real world in a zero-shot manner, performing tasks such as
> picking up and pushing tofu. Our results show that the learned policies exhibit
> a damage-aware, gentle manipulation behavior, demonstrating their effectiveness
> by decreasing the stress applied to fragile objects by 36.5% while achieving
> the task goals, compared to vanilla RL policies.

