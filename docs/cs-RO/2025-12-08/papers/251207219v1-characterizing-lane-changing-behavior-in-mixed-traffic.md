---
layout: default
title: Characterizing Lane-Changing Behavior in Mixed Traffic
---

# Characterizing Lane-Changing Behavior in Mixed Traffic

**arXiv**: [2512.07219v1](https://arxiv.org/abs/2512.07219) | [PDF](https://arxiv.org/pdf/2512.07219.pdf)

**作者**: Sungyong Chung, Alireza Talebpour, Samer H. Hamdar

---

## 💡 一句话要点

**提出博弈论框架以分析混合交通中换道行为的合作与缺陷模式**

**关键词**: `混合交通` `换道行为` `博弈论` `自动驾驶` `社会困境` `进化博弈`

## 📋 核心要点

1. 核心问题：混合交通中自动驾驶车辆与人类驾驶车辆换道交互行为的特征与演化
2. 方法要点：基于真实轨迹数据，应用聚类和量化响应均衡框架估计车辆效用并构建收益表
3. 实验或效果：揭示约4%和11%换道事件存在社会困境，模拟显示重复交互促进合作行为

## 📄 摘要（原文）

> Characterizing and understanding lane-changing behavior in the presence of automated vehicles (AVs) is crucial to ensuring safety and efficiency in mixed traffic. Accordingly, this study aims to characterize the interactions between the lane-changing vehicle (active vehicle) and the vehicle directly impacted by the maneuver in the target lane (passive vehicle). Utilizing real-world trajectory data from the Waymo Open Motion Dataset (WOMD), this study explores patterns in lane-changing behavior and provides insight into how these behaviors evolve under different AV market penetration rates (MPRs). In particular, we propose a game-theoretic framework to analyze cooperative and defective behaviors in mixed traffic, applied to the 7,636 observed lane-changing events in the WOMD. First, we utilize k-means clustering to classify vehicles as cooperative or defective, revealing that the proportions of cooperative AVs are higher than those of HDVs in both active and passive roles. Next, we jointly estimate the utilities of active and passive vehicles to model their behaviors using the quantal response equilibrium framework. Empirical payoff tables are then constructed based on these utilities. Using these payoffs, we analyze the presence of social dilemmas and examine the evolution of cooperative behaviors using evolutionary game theory. Our results reveal the presence of social dilemmas in approximately 4% and 11% of lane-changing events for active and passive vehicles, respectively, with most classified as Stag Hunt or Prisoner's Dilemma (Chicken Game rarely observed). Moreover, the Monte Carlo simulation results show that repeated lane-changing interactions consistently lead to increased cooperative behavior over time, regardless of the AV penetration rate.

