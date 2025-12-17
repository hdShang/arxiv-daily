---
layout: default
title: Residual MPC: Blending Reinforcement Learning with GPU-Parallelized Model Predictive Control
---

# Residual MPC: Blending Reinforcement Learning with GPU-Parallelized Model Predictive Control

**arXiv**: [2510.12717v1](https://arxiv.org/abs/2510.12717) | [PDF](https://arxiv.org/pdf/2510.12717.pdf)

**作者**: Se Hwan Jeon, Ho Jae Lee, Seungwoo Hong, Sangbae Kim

---

## 💡 一句话要点

**提出残差MPC架构，融合强化学习与模型预测控制以提升机器人运动控制性能。**

**关键词**: `模型预测控制` `强化学习` `残差架构` `GPU并行化` `机器人运动控制` `扭矩控制`

## 📋 核心要点

1. 核心问题：模型预测控制受限于模型失配和实时计算，强化学习缺乏可解释性和泛化性。
2. 方法要点：在扭矩控制层融合MPC与RL输出，利用GPU并行化实现高效训练。
3. 实验效果：相比单独方法，样本效率更高，适应未见步态和地形，提升奖励和速度跟踪范围。

## 📄 摘要（原文）

> Model Predictive Control (MPC) provides interpretable, tunable locomotion
> controllers grounded in physical models, but its robustness depends on frequent
> replanning and is limited by model mismatch and real-time computational
> constraints. Reinforcement Learning (RL), by contrast, can produce highly
> robust behaviors through stochastic training but often lacks interpretability,
> suffers from out-of-distribution failures, and requires intensive reward
> engineering. This work presents a GPU-parallelized residual architecture that
> tightly integrates MPC and RL by blending their outputs at the torque-control
> level. We develop a kinodynamic whole-body MPC formulation evaluated across
> thousands of agents in parallel at 100 Hz for RL training. The residual policy
> learns to make targeted corrections to the MPC outputs, combining the
> interpretability and constraint handling of model-based control with the
> adaptability of RL. The model-based control prior acts as a strong bias,
> initializing and guiding the policy towards desirable behavior with a simple
> set of rewards. Compared to standalone MPC or end-to-end RL, our approach
> achieves higher sample efficiency, converges to greater asymptotic rewards,
> expands the range of trackable velocity commands, and enables zero-shot
> adaptation to unseen gaits and uneven terrain.

