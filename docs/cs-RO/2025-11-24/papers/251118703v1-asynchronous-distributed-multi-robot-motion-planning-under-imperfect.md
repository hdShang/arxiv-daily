---
layout: default
title: Asynchronous Distributed Multi-Robot Motion Planning Under Imperfect Communication
---

# Asynchronous Distributed Multi-Robot Motion Planning Under Imperfect Communication

**arXiv**: [2511.18703v1](https://arxiv.org/abs/2511.18703) | [PDF](https://arxiv.org/pdf/2511.18703.pdf)

**作者**: Ardalan Tajbakhsh, Augustinos Saravanos, James Zhu, Evangelos A. Theodorou, Lorenz T. Biegler, Aaron M. Johnson

---

## 💡 一句话要点

**提出延迟感知ADMM以提升多机器人运动规划在通信延迟下的鲁棒性**

**关键词**: `多机器人系统` `分布式优化` `运动规划` `通信延迟` `ADMM算法` `鲁棒控制`

## 📋 核心要点

1. 核心问题：多机器人系统在通信延迟下协调运动，现有方法对延迟敏感
2. 方法要点：引入DA-ADMM，基于实时延迟统计自适应调整惩罚参数
3. 实验或效果：在多种动态模型中，DA-ADMM显著提高成功率和解质量

## 📄 摘要（原文）

> This paper addresses the challenge of coordinating multi-robot systems under realistic communication delays using distributed optimization. We focus on consensus ADMM as a scalable framework for generating collision-free, dynamically feasible motion plans in both trajectory optimization and receding-horizon control settings. In practice, however, these algorithms are sensitive to penalty tuning or adaptation schemes (e.g. residual balancing and adaptive parameter heuristics) that do not explicitly consider delays. To address this, we introduce a Delay-Aware ADMM (DA-ADMM) variant that adapts penalty parameters based on real-time delay statistics, allowing agents to down-weight stale information and prioritize recent updates during consensus and dual updates. Through extensive simulations in 2D and 3D environments with double-integrator, Dubins-car, and drone dynamics, we show that DA-ADMM significantly improves robustness, success rate, and solution quality compared to fixed-parameter, residual-balancing, and fixed-constraint baselines. Our results highlight that performance degradation is not solely determined by delay length or frequency, but by the optimizer's ability to contextually reason over delayed information. The proposed DA-ADMM achieves consistently better coordination performance across a wide range of delay conditions, offering a principled and efficient mechanism for resilient multi-robot motion planning under imperfect communication.

