---
layout: default
title: A Task-Efficient Reinforcement Learning Task-Motion Planner for Safe Human-Robot Cooperation
---

# A Task-Efficient Reinforcement Learning Task-Motion Planner for Safe Human-Robot Cooperation

**arXiv**: [2510.12477v1](https://arxiv.org/abs/2510.12477) | [PDF](https://arxiv.org/pdf/2510.12477.pdf)

**作者**: Gaoyuan Liu, Joris de Winter, Kelly Merckaert, Denis Steckelmacher, Ann Nowe, Bram Vanderborght

---

## 💡 一句话要点

**提出混合强化学习任务运动规划框架，以提升人机协作的安全性与效率**

**关键词**: `人机协作` `强化学习规划` `运动规划` `安全机器人` `任务效率`

## 📋 核心要点

1. 核心问题：人机协作中安全机制常降低任务效率，频繁运动重规划增加计算负担与失败风险
2. 方法要点：结合强化学习任务规划器与交互式运动规划器，学习安全任务序列并实时避障
3. 实验或效果：在仿真与真实机器人验证，减少重规划次数与失败命令重复，提升反应能力

## 📄 摘要（原文）

> In a Human-Robot Cooperation (HRC) environment, safety and efficiency are the
> two core properties to evaluate robot performance. However, safety mechanisms
> usually hinder task efficiency since human intervention will cause backup
> motions and goal failures of the robot. Frequent motion replanning will
> increase the computational load and the chance of failure. In this paper, we
> present a hybrid Reinforcement Learning (RL) planning framework which is
> comprised of an interactive motion planner and a RL task planner. The RL task
> planner attempts to choose statistically safe and efficient task sequences
> based on the feedback from the motion planner, while the motion planner keeps
> the task execution process collision-free by detecting human arm motions and
> deploying new paths when the previous path is not valid anymore. Intuitively,
> the RL agent will learn to avoid dangerous tasks, while the motion planner
> ensures that the chosen tasks are safe. The proposed framework is validated on
> the cobot in both simulation and the real world, we compare the planner with
> hard-coded task motion planning methods. The results show that our planning
> framework can 1) react to uncertain human motions at both joint and task
> levels; 2) reduce the times of repeating failed goal commands; 3) reduce the
> total number of replanning requests.

