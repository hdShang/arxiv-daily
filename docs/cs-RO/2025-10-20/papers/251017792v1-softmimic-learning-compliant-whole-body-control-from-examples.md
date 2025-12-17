---
layout: default
title: SoftMimic: Learning Compliant Whole-body Control from Examples
---

# SoftMimic: Learning Compliant Whole-body Control from Examples

**arXiv**: [2510.17792v1](https://arxiv.org/abs/2510.17792) | [PDF](https://arxiv.org/pdf/2510.17792.pdf)

**作者**: Gabriel B. Margolis, Michelle Wang, Nolan Fey, Pulkit Agrawal

---

## 💡 一句话要点

**提出SoftMimic框架，从示例运动学习人形机器人柔顺全身控制以应对意外接触。**

**关键词**: `人形机器人控制` `柔顺运动模仿` `强化学习` `逆运动学` `全身控制` `扰动吸收`

## 📋 核心要点

1. 核心问题：现有模仿方法导致僵硬控制，在意外接触时行为脆弱不安全。
2. 方法要点：利用逆运动学生成柔顺运动数据集，训练强化学习策略匹配柔顺响应。
3. 实验或效果：通过仿真和真实实验验证，机器人能吸收扰动并泛化到多种任务。

## 📄 摘要（原文）

> We introduce SoftMimic, a framework for learning compliant whole-body control
> policies for humanoid robots from example motions. Imitating human motions with
> reinforcement learning allows humanoids to quickly learn new skills, but
> existing methods incentivize stiff control that aggressively corrects
> deviations from a reference motion, leading to brittle and unsafe behavior when
> the robot encounters unexpected contacts. In contrast, SoftMimic enables robots
> to respond compliantly to external forces while maintaining balance and
> posture. Our approach leverages an inverse kinematics solver to generate an
> augmented dataset of feasible compliant motions, which we use to train a
> reinforcement learning policy. By rewarding the policy for matching compliant
> responses rather than rigidly tracking the reference motion, SoftMimic learns
> to absorb disturbances and generalize to varied tasks from a single motion
> clip. We validate our method through simulations and real-world experiments,
> demonstrating safe and effective interaction with the environment.

