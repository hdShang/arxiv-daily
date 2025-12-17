---
layout: default
title: Distributed Spatial-Temporal Trajectory Optimization for Unmanned-Aerial-Vehicle Swarm
---

# Distributed Spatial-Temporal Trajectory Optimization for Unmanned-Aerial-Vehicle Swarm

**arXiv**: [2510.17541v1](https://arxiv.org/abs/2510.17541) | [PDF](https://arxiv.org/pdf/2510.17541.pdf)

**作者**: Xiaobo Zheng, Pan Tang, Defu Lin, Shaoming He

---

## 💡 一句话要点

**提出分布式时空轨迹优化框架以解决无人机集群大规模轨迹优化问题**

**关键词**: `无人机集群` `轨迹优化` `分布式算法` `ADMM` `微分动态规划`

## 📋 核心要点

1. 核心问题：无人机集群轨迹优化存在非线性强、需预设最终时间及迭代耗时等限制
2. 方法要点：结合ADMM实现多无人机共识，使用PDDP进行快速局部轨迹规划
3. 实验或效果：通过模拟验证算法有效性，并引入自适应惩罚参数减少迭代次数

## 📄 摘要（原文）

> Swarm trajectory optimization problems are a well-recognized class of
> multi-agent optimal control problems with strong nonlinearity. However, the
> heuristic nature of needing to set the final time for agents beforehand and the
> time-consuming limitation of the significant number of iterations prohibit the
> application of existing methods to large-scale swarm of Unmanned Aerial
> Vehicles (UAVs) in practice. In this paper, we propose a spatial-temporal
> trajectory optimization framework that accomplishes multi-UAV consensus based
> on the Alternating Direction Multiplier Method (ADMM) and uses Differential
> Dynamic Programming (DDP) for fast local planning of individual UAVs. The
> introduced framework is a two-level architecture that employs Parameterized DDP
> (PDDP) as the trajectory optimizer for each UAV, and ADMM to satisfy the local
> constraints and accomplish the spatial-temporal parameter consensus among all
> UAVs. This results in a fully distributed algorithm called Distributed
> Parameterized DDP (D-PDDP). In addition, an adaptive tuning criterion based on
> the spectral gradient method for the penalty parameter is proposed to reduce
> the number of algorithmic iterations. Several simulation examples are presented
> to verify the effectiveness of the proposed algorithm.

