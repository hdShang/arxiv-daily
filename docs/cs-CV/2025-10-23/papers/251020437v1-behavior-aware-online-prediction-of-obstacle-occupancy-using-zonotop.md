---
layout: default
title: Behavior-Aware Online Prediction of Obstacle Occupancy using Zonotopes
---

# Behavior-Aware Online Prediction of Obstacle Occupancy using Zonotopes

**arXiv**: [2510.20437v1](https://arxiv.org/abs/2510.20437) | [PDF](https://arxiv.org/pdf/2510.20437.pdf)

**作者**: Alvaro Carrizosa-Rendon, Jian Zhou, Erik Frisk, Vicenc Puig, Fatiha Nejjari

---

## 💡 一句话要点

**提出基于行为感知的在线方法，使用zonotopes预测障碍物占用，以提升自动驾驶安全性。**

**关键词**: `自动驾驶预测` `zonotopes方法` `可达性分析` `在线估计` `运动预测`

## 📋 核心要点

1. 核心问题：在无先验信息环境中，准确预测周围车辆运动对自动驾驶安全至关重要。
2. 方法要点：分两阶段，先估计控制动作zonotopic集，再通过可达性分析预测未来占用。
3. 实验或效果：城市环境模拟验证，预测准确紧凑，无需先验假设或训练数据。

## 📄 摘要（原文）

> Predicting the motion of surrounding vehicles is key to safe autonomous
> driving, especially in unstructured environments without prior information.
> This paper proposes a novel online method to accurately predict the occupancy
> sets of surrounding vehicles based solely on motion observations. The approach
> is divided into two stages: first, an Extended Kalman Filter and a Linear
> Programming (LP) problem are used to estimate a compact zonotopic set of
> control actions; then, a reachability analysis propagates this set to predict
> future occupancy. The effectiveness of the method has been validated through
> simulations in an urban environment, showing accurate and compact predictions
> without relying on prior assumptions or prior training data.

