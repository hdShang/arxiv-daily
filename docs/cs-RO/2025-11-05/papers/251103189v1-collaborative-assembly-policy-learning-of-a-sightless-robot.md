---
layout: default
title: Collaborative Assembly Policy Learning of a Sightless Robot
---

# Collaborative Assembly Policy Learning of a Sightless Robot

**arXiv**: [2511.03189v1](https://arxiv.org/abs/2511.03189) | [PDF](https://arxiv.org/pdf/2511.03189.pdf)

**作者**: Zeqing Zhang, Weifeng Lu, Lei Yang, Wei Jing, Bowei Tang, Jia Pan

---

## 💡 一句话要点

**提出强化学习方法以解决盲机器人协作装配中意图估计难的问题**

**关键词**: `物理人机协作` `强化学习` `导纳控制` `意图估计` `盲机器人` `装配任务`

## 📋 核心要点

1. 核心问题：盲机器人在物理人机协作中难以准确估计人类意图，导致协助能力受限
2. 方法要点：结合人设计的导纳控制器，通过强化学习提升机器人主动行为，减少人力
3. 实验或效果：仿真与真实实验显示，方法在成功率和任务时间上优于导纳控制，力/扭矩显著降低

## 📄 摘要（原文）

> This paper explores a physical human-robot collaboration (pHRC) task
> involving the joint insertion of a board into a frame by a sightless robot and
> a human operator. While admittance control is commonly used in pHRC tasks, it
> can be challenging to measure the force/torque applied by the human for
> accurate human intent estimation, limiting the robot's ability to assist in the
> collaborative task. Other methods that attempt to solve pHRC tasks using
> reinforcement learning (RL) are also unsuitable for the board-insertion task
> due to its safety constraints and sparse rewards. Therefore, we propose a novel
> RL approach that utilizes a human-designed admittance controller to facilitate
> more active robot behavior and reduce human effort. Through simulation and
> real-world experiments, we demonstrate that our approach outperforms admittance
> control in terms of success rate and task completion time. Additionally, we
> observed a significant reduction in measured force/torque when using our
> proposed approach compared to admittance control. The video of the experiments
> is available at https://youtu.be/va07Gw6YIog.

