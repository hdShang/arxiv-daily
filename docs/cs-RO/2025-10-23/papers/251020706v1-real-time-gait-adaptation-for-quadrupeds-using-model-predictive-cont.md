---
layout: default
title: Real-Time Gait Adaptation for Quadrupeds using Model Predictive Control and Reinforcement Learning
---

# Real-Time Gait Adaptation for Quadrupeds using Model Predictive Control and Reinforcement Learning

**arXiv**: [2510.20706v1](https://arxiv.org/abs/2510.20706) | [PDF](https://arxiv.org/pdf/2510.20706.pdf)

**作者**: Ganga Nair B, Prakrut Kotecha, Shishir Kolathaya

---

## 💡 一句话要点

**提出结合MPPI与Dreamer的优化框架，实现四足机器人实时步态自适应以提升性能。**

**关键词**: `四足机器人` `模型预测控制` `强化学习` `步态自适应` `能量效率` `实时优化`

## 📋 核心要点

1. 核心问题：模型无关强化学习易收敛到单一步态，模型预测控制难以适应环境变化。
2. 方法要点：在连续步态空间中联合优化动作与步态变量，使用Dreamer奖励和值函数。
3. 实验或效果：在Unitree Go1仿真中，能耗平均降低36.48%，保持准确跟踪和自适应步态。

## 📄 摘要（原文）

> Model-free reinforcement learning (RL) has enabled adaptable and agile
> quadruped locomotion; however, policies often converge to a single gait,
> leading to suboptimal performance. Traditionally, Model Predictive Control
> (MPC) has been extensively used to obtain task-specific optimal policies but
> lacks the ability to adapt to varying environments. To address these
> limitations, we propose an optimization framework for real-time gait adaptation
> in a continuous gait space, combining the Model Predictive Path Integral (MPPI)
> algorithm with a Dreamer module to produce adaptive and optimal policies for
> quadruped locomotion. At each time step, MPPI jointly optimizes the actions and
> gait variables using a learned Dreamer reward that promotes velocity tracking,
> energy efficiency, stability, and smooth transitions, while penalizing abrupt
> gait changes. A learned value function is incorporated as terminal reward,
> extending the formulation to an infinite-horizon planner. We evaluate our
> framework in simulation on the Unitree Go1, demonstrating an average reduction
> of up to 36.48\% in energy consumption across varying target speeds, while
> maintaining accurate tracking and adaptive, task-appropriate gaits.

