---
layout: default
title: PGTT: Phase-Guided Terrain Traversal for Perceptive Legged Locomotion
---

# PGTT: Phase-Guided Terrain Traversal for Perceptive Legged Locomotion

**arXiv**: [2510.18348v1](https://arxiv.org/abs/2510.18348) | [PDF](https://arxiv.org/pdf/2510.18348.pdf)

**作者**: Alexandros Ntagkas, Chairi Kiourt, Konstantinos Chatzilygeroudis

---

## 💡 一句话要点

**提出相位引导地形穿越方法，以增强腿式机器人在感知环境中的鲁棒运动。**

**关键词**: `腿式机器人` `强化学习` `感知运动控制` `奖励塑形` `地形适应` `相位引导`

## 📋 核心要点

1. 现有感知强化学习控制器存在动作空间约束或盲操作问题，限制适应性和鲁棒性。
2. 通过奖励塑形编码腿部相位，使用三次Hermite样条调整摆动高度，减少策略学习中的归纳偏差。
3. 在模拟和真实机器人实验中，PGTT在扰动和障碍物上成功率更高，收敛速度更快。

## 📄 摘要（原文）

> State-of-the-art perceptive Reinforcement Learning controllers for legged
> robots either (i) impose oscillator or IK-based gait priors that constrain the
> action space, add bias to the policy optimization and reduce adaptability
> across robot morphologies, or (ii) operate "blind", which struggle to
> anticipate hind-leg terrain, and are brittle to noise. In this paper, we
> propose Phase-Guided Terrain Traversal (PGTT), a perception-aware deep-RL
> approach that overcomes these limitations by enforcing gait structure purely
> through reward shaping, thereby reducing inductive bias in policy learning
> compared to oscillator/IK-conditioned action priors. PGTT encodes per-leg phase
> as a cubic Hermite spline that adapts swing height to local heightmap
> statistics and adds a swing- phase contact penalty, while the policy acts
> directly in joint space supporting morphology-agnostic deployment. Trained in
> MuJoCo (MJX) on procedurally generated stair-like terrains with curriculum and
> domain randomization, PGTT achieves the highest success under push disturbances
> (median +7.5% vs. the next best method) and on discrete obstacles (+9%), with
> comparable velocity tracking, and converging to an effective policy roughly 2x
> faster than strong end-to-end baselines. We validate PGTT on a Unitree Go2
> using a real-time LiDAR elevation-to-heightmap pipeline, and we report
> preliminary results on ANYmal-C obtained with the same hyperparameters. These
> findings indicate that terrain-adaptive, phase-guided reward shaping is a
> simple and general mechanism for robust perceptive locomotion across platforms.

