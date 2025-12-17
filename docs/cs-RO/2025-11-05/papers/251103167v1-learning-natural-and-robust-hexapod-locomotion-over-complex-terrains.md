---
layout: default
title: Learning Natural and Robust Hexapod Locomotion over Complex Terrains via Motion Priors based on Deep Reinforcement Learning
---

# Learning Natural and Robust Hexapod Locomotion over Complex Terrains via Motion Priors based on Deep Reinforcement Learning

**arXiv**: [2511.03167v1](https://arxiv.org/abs/2511.03167) | [PDF](https://arxiv.org/pdf/2511.03167.pdf)

**作者**: Xin Liu, Jinze Wu, Yinghui Li, Chenkun Qi, Yufei Xue, Feng Gao

---

## 💡 一句话要点

**提出基于运动先验的深度强化学习方法，实现六足机器人在复杂地形上的自然稳健运动。**

**关键词**: `六足机器人` `深度强化学习` `运动先验` `对抗判别器` `复杂地形导航` `步态生成`

## 📋 核心要点

1. 核心问题：多足机器人在大动作空间中协调多腿以生成自然稳健运动。
2. 方法要点：生成优化运动先验数据集，并训练对抗判别器指导学习自然步态。
3. 实验或效果：学习策略成功迁移至真实机器人，在无视觉信息下展示自然步态和强鲁棒性。

## 📄 摘要（原文）

> Multi-legged robots offer enhanced stability to navigate complex terrains
> with their multiple legs interacting with the environment. However, how to
> effectively coordinate the multiple legs in a larger action exploration space
> to generate natural and robust movements is a key issue. In this paper, we
> introduce a motion prior-based approach, successfully applying deep
> reinforcement learning algorithms to a real hexapod robot. We generate a
> dataset of optimized motion priors, and train an adversarial discriminator
> based on the priors to guide the hexapod robot to learn natural gaits. The
> learned policy is then successfully transferred to a real hexapod robot, and
> demonstrate natural gait patterns and remarkable robustness without visual
> information in complex terrains. This is the first time that a reinforcement
> learning controller has been used to achieve complex terrain walking on a real
> hexapod robot.

