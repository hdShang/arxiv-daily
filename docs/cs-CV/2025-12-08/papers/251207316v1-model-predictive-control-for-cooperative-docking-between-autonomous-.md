---
layout: default
title: Model Predictive Control for Cooperative Docking Between Autonomous Surface Vehicles with Disturbance Rejection
---

# Model Predictive Control for Cooperative Docking Between Autonomous Surface Vehicles with Disturbance Rejection

**arXiv**: [2512.07316v1](https://arxiv.org/abs/2512.07316) | [PDF](https://arxiv.org/pdf/2512.07316.pdf)

**作者**: Gianpietro Battocletti, Dimitris Boskos, Bart De Schutter

---

## 💡 一句话要点

**提出基于模型预测控制的协同对接方法，以解决无人水面艇在扰动下的高效对接问题。**

**关键词**: `无人水面艇` `协同对接` `模型预测控制` `扰动抑制` `集中式控制` `仿真验证`

## 📋 核心要点

1. 核心问题：现有无人水面艇对接方法通常假设一艇静止，另一艇主动接近，缺乏协同性，且难以处理扰动。
2. 方法要点：采用集中式模型预测控制，两艇协同运动至约定位置，通过预测模型实现扰动（如水流）的抑制。
3. 实验或效果：仿真显示，该方法相比现有方法能实现更快、更高效的对接，并保证约束满足。

## 📄 摘要（原文）

> Uncrewed Surface Vehicles (USVs) are a popular and efficient type of marine craft that find application in a large number of water-based tasks. When multiple USVs operate in the same area, they may be required to dock to each other to perform a shared task. Existing approaches for the docking between autonomous USVs generally consider one USV as a stationary target, while the second one is tasked to reach the required docking pose. In this work, we propose a cooperative approach for USV-USV docking, where two USVs work together to dock at an agreed location. We use a centralized Model Predictive Control (MPC) approach to solve the control problem, obtaining feasible trajectories that also guarantee constraint satisfaction. Owing to its model-based nature, this approach allows the rejection of disturbances, inclusive of exogenous inputs, by anticipating their effect on the USVs through the MPC prediction model. This is particularly effective in case of almost-stationary disturbances such as water currents. In simulations, we demonstrate how the proposed approach allows for a faster and more efficient docking with respect to existing approaches.

