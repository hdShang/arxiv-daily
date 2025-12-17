---
layout: default
title: Reinforcement Learning-based Robust Wall Climbing Locomotion Controller in Ferromagnetic Environment
---

# Reinforcement Learning-based Robust Wall Climbing Locomotion Controller in Ferromagnetic Environment

**arXiv**: [2510.20174v1](https://arxiv.org/abs/2510.20174) | [PDF](https://arxiv.org/pdf/2510.20174.pdf)

**作者**: Yong Um, Young-Ha Shin, Joon-Ha Kim, Soonpyo Kwon, Hae-Won Park

---

## 💡 一句话要点

**提出强化学习框架以解决四足磁爬机器人在不确定磁吸附环境中的稳健壁面爬行问题**

**关键词**: `强化学习` `四足机器人` `磁吸附控制` `课程学习` `仿真到现实` `稳健爬行`

## 📋 核心要点

1. 核心问题：磁脚吸附不确定性导致机器人壁面爬行失败，如部分接触和概率性脱落。
2. 方法要点：结合物理吸附模型和三阶段课程学习，从平地爬行逐步过渡到垂直壁面并注入故障。
3. 实验或效果：仿真中高成功率、强吸附保持和快速恢复；硬件实验证实稳健垂直爬行。

## 📄 摘要（原文）

> We present a reinforcement learning framework for quadrupedal wall-climbing
> locomotion that explicitly addresses uncertainty in magnetic foot adhesion. A
> physics-based adhesion model of a quadrupedal magnetic climbing robot is
> incorporated into simulation to capture partial contact, air-gap sensitivity,
> and probabilistic attachment failures. To stabilize learning and enable
> reliable transfer, we design a three-phase curriculum: (1) acquire a crawl gait
> on flat ground without adhesion, (2) gradually rotate the gravity vector to
> vertical while activating the adhesion model, and (3) inject stochastic
> adhesion failures to encourage slip recovery. The learned policy achieves a
> high success rate, strong adhesion retention, and rapid recovery from
> detachment in simulation under degraded adhesion. Compared with a model
> predictive control (MPC) baseline that assumes perfect adhesion, our controller
> maintains locomotion when attachment is intermittently lost. Hardware
> experiments with the untethered robot further confirm robust vertical crawling
> on steel surfaces, maintaining stability despite transient misalignment and
> incomplete attachment. These results show that combining curriculum learning
> with realistic adhesion modeling provides a resilient sim-to-real framework for
> magnetic climbing robots in complex environments.

