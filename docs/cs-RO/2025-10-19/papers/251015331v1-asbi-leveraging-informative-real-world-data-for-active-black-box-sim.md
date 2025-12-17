---
layout: default
title: ASBI: Leveraging Informative Real-World Data for Active Black-Box Simulator Tuning
---

# ASBI: Leveraging Informative Real-World Data for Active Black-Box Simulator Tuning

**arXiv**: [2510.15331v1](https://arxiv.org/abs/2510.15331) | [PDF](https://arxiv.org/pdf/2510.15331.pdf)

**作者**: Gahee Kim, Takamitsu Matsubara

---

## 💡 一句话要点

**提出主动仿真推断框架以解决黑盒模拟器参数优化问题**

**关键词**: `黑盒模拟器` `主动学习` `仿真推断` `参数估计` `机器人控制`

## 📋 核心要点

1. 黑盒模拟器参数优化困难，因似然函数不可访问且观测数据信息不足
2. 使用主动数据收集和神经后验估计，最大化信息增益以优化参数
3. 仿真和真实机器人实验验证参数估计准确，后验分布集中

## 📄 摘要（原文）

> Black-box simulators are widely used in robotics, but optimizing their
> parameters remains challenging due to inaccessible likelihoods.
> Simulation-Based Inference (SBI) tackles this issue using simulation-driven
> approaches, estimating the posterior from offline real observations and forward
> simulations. However, in black-box scenarios, preparing observations that
> contain sufficient information for parameter estimation is difficult due to the
> unknown relationship between parameters and observations. In this work, we
> present Active Simulation-Based Inference (ASBI), a parameter estimation
> framework that uses robots to actively collect real-world online data to
> achieve accurate black-box simulator tuning. Our framework optimizes robot
> actions to collect informative observations by maximizing information gain,
> which is defined as the expected reduction in Shannon entropy between the
> posterior and the prior. While calculating information gain requires the
> likelihood, which is inaccessible in black-box simulators, our method solves
> this problem by leveraging Neural Posterior Estimation (NPE), which leverages a
> neural network to learn the posterior estimator. Three simulation experiments
> quantitatively verify that our method achieves accurate parameter estimation,
> with posteriors sharply concentrated around the true parameters. Moreover, we
> show a practical application using a real robot to estimate the simulation
> parameters of cubic particles corresponding to two real objects, beads and
> gravel, with a bucket pouring action.

