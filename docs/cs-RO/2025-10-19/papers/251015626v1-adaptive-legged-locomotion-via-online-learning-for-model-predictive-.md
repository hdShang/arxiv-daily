---
layout: default
title: Adaptive Legged Locomotion via Online Learning for Model Predictive Control
---

# Adaptive Legged Locomotion via Online Learning for Model Predictive Control

**arXiv**: [2510.15626v1](https://arxiv.org/abs/2510.15626) | [PDF](https://arxiv.org/pdf/2510.15626.pdf)

**作者**: Hongyu Zhou, Xiaoyu Zhang, Vasileios Tzoumas

---

## 💡 一句话要点

**提出在线学习与模型预测控制算法，实现四足机器人在未知扰动下的自适应运动。**

**关键词**: `四足机器人` `模型预测控制` `在线学习` `残差动力学` `自适应运动` `模拟验证`

## 📋 核心要点

1. 核心问题：四足机器人在未知负载和地形等不确定性下难以稳定运动。
2. 方法要点：结合模型预测控制和在线学习残差动力学，使用随机傅里叶特征近似。
3. 实验或效果：在Gazebo和MuJoCo模拟中验证，能处理大外力、斜坡和粗糙地形。

## 📄 摘要（原文）

> We provide an algorithm for adaptive legged locomotion via online learning
> and model predictive control. The algorithm is composed of two interacting
> modules: model predictive control (MPC) and online learning of residual
> dynamics. The residual dynamics can represent modeling errors and external
> disturbances. We are motivated by the future of autonomy where quadrupeds will
> autonomously perform complex tasks despite real-world unknown uncertainty, such
> as unknown payload and uneven terrains. The algorithm uses random Fourier
> features to approximate the residual dynamics in reproducing kernel Hilbert
> spaces. Then, it employs MPC based on the current learned model of the residual
> dynamics. The model is updated online in a self-supervised manner using least
> squares based on the data collected while controlling the quadruped. The
> algorithm enjoys sublinear \textit{dynamic regret}, defined as the
> suboptimality against an optimal clairvoyant controller that knows how the
> residual dynamics. We validate our algorithm in Gazebo and MuJoCo simulations,
> where the quadruped aims to track reference trajectories. The Gazebo
> simulations include constant unknown external forces up to $12\boldsymbol{g}$,
> where $\boldsymbol{g}$ is the gravity vector, in flat terrain, slope terrain
> with $20\degree$ inclination, and rough terrain with $0.25m$ height variation.
> The MuJoCo simulations include time-varying unknown disturbances with payload
> up to $8~kg$ and time-varying ground friction coefficients in flat terrain.

