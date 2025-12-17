---
layout: default
title: A Parameter-Linear Formulation of the Optimal Path Following Problem for Robotic Manipulator
---

# A Parameter-Linear Formulation of the Optimal Path Following Problem for Robotic Manipulator

**arXiv**: [2510.20496v1](https://arxiv.org/abs/2510.20496) | [PDF](https://arxiv.org/pdf/2510.20496.pdf)

**作者**: Tobias Marauli, Hubert Gattringer, Andreas Mueller

---

## 💡 一句话要点

**提出最大化路径速度方法以解决机器人时间最优路径跟随的计算挑战**

**关键词**: `机器人路径跟随` `时间最优控制` `优化问题线性化` `轨迹规划` `数值效率`

## 📋 核心要点

1. 核心问题：时间最优路径跟随在零路径速度时出现奇点，导致计算复杂和轨迹不平滑。
2. 方法要点：通过最大化路径速度替代最小化时间，实现线性离散化，提高数值效率。
3. 实验或效果：未知具体实验，但声称能高效规划平滑轨迹，降低计算负担。

## 📄 摘要（原文）

> In this paper the computational challenges of time-optimal path following are
> addressed. The standard approach is to minimize the travel time, which
> inevitably leads to singularities at zero path speed, when reformulating the
> optimization problem in terms of a path parameter. Thus, smooth trajectory
> generation while maintaining a low computational effort is quite challenging,
> since the singularities have to be taken into account. To this end, a different
> approach is presented in this paper. This approach is based on maximizing the
> path speed along a prescribed path. Furthermore, the approach is capable of
> planning smooth trajectories numerically efficient. Moreover, the discrete
> reformulation of the underlying problem is linear in optimization variables.

