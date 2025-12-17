---
layout: default
title: Differentiable Physics-Neural Models enable Learning of Non-Markovian Closures for Accelerated Coarse-Grained Physics Simulations
---

# Differentiable Physics-Neural Models enable Learning of Non-Markovian Closures for Accelerated Coarse-Grained Physics Simulations

**arXiv**: [2511.21369v1](https://arxiv.org/abs/2511.21369) | [PDF](https://arxiv.org/pdf/2511.21369.pdf)

**作者**: Tingkai Xue, Chin Chun Ooi, Zhengwei Ge, Fong Yew Leong, Hongying Li, Chang Wei Kang

---

## 💡 一句话要点

**提出可微分物理-神经模型以加速粗粒度物理模拟**

**关键词**: `可微分物理` `神经闭包模型` `粗粒度模拟` `标量输运` `非马尔可夫过程`

## 📋 核心要点

1. 核心问题：3D物理模拟计算成本高，但分析仅需简化指标。
2. 方法要点：联合学习物理参数化和非马尔可夫神经闭包模型。
3. 实验或效果：训练数据少，模拟速度提升，相关性强达0.96。

## 📄 摘要（原文）

> Numerical simulations provide key insights into many physical, real-world problems. However, while these simulations are solved on a full 3D domain, most analysis only require a reduced set of metrics (e.g. plane-level concentrations). This work presents a hybrid physics-neural model that predicts scalar transport in a complex domain orders of magnitude faster than the 3D simulation (from hours to less than 1 min). This end-to-end differentiable framework jointly learns the physical model parameterization (i.e. orthotropic diffusivity) and a non-Markovian neural closure model to capture unresolved, 'coarse-grained' effects, thereby enabling stable, long time horizon rollouts. This proposed model is data-efficient (learning with 26 training data), and can be flexibly extended to an out-of-distribution scenario (with a moving source), achieving a Spearman correlation coefficient of 0.96 at the final simulation time. Overall results show that this differentiable physics-neural framework enables fast, accurate, and generalizable coarse-grained surrogates for physical phenomena.

