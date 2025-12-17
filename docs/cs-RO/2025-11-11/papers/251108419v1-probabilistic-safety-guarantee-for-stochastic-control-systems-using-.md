---
layout: default
title: Probabilistic Safety Guarantee for Stochastic Control Systems Using Average Reward MDPs
---

# Probabilistic Safety Guarantee for Stochastic Control Systems Using Average Reward MDPs

**arXiv**: [2511.08419v1](https://arxiv.org/abs/2511.08419) | [PDF](https://arxiv.org/pdf/2511.08419.pdf)

**作者**: Saber Omidi, Marek Petrik, Se Young Yoon, Momotaz Begum

---

## 💡 一句话要点

**提出基于平均奖励MDP的算法以解决随机控制系统安全策略计算问题**

**关键词**: `随机控制系统` `安全策略` `平均奖励MDP` `线性规划` `策略验证`

## 📋 核心要点

1. 随机控制系统状态变量不确定演化难以满足预定义约束
2. 将安全目标简化为平均奖励MDP目标，利用线性规划计算策略
3. 在双积分器和倒立摆系统验证，收敛更快、质量更高

## 📄 摘要（原文）

> Safety in stochastic control systems, which are subject to random noise with a known probability distribution, aims to compute policies that satisfy predefined operational constraints with high confidence throughout the uncertain evolution of the state variables. The unpredictable evolution of state variables poses a significant challenge for meeting predefined constraints using various control methods. To address this, we present a new algorithm that computes safe policies to determine the safety level across a finite state set. This algorithm reduces the safety objective to the standard average reward Markov Decision Process (MDP) objective. This reduction enables us to use standard techniques, such as linear programs, to compute and analyze safe policies. We validate the proposed method numerically on the Double Integrator and the Inverted Pendulum systems. Results indicate that the average-reward MDPs solution is more comprehensive, converges faster, and offers higher quality compared to the minimum discounted-reward solution.

