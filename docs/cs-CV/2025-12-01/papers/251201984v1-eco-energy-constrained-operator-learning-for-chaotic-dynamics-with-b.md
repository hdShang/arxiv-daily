---
layout: default
title: ECO: Energy-Constrained Operator Learning for Chaotic Dynamics with Boundedness Guarantees
---

# ECO: Energy-Constrained Operator Learning for Chaotic Dynamics with Boundedness Guarantees

**arXiv**: [2512.01984v1](https://arxiv.org/abs/2512.01984) | [PDF](https://arxiv.org/pdf/2512.01984.pdf)

**作者**: Andrea Goertzen, Sunbochen Tang, Navid Azizan

---

## 💡 一句话要点

**提出能量约束算子以解决混沌动力学预测中的无界性问题，确保轨迹有界性。**

**关键词**: `混沌动力学` `能量约束算子` `轨迹有界性` `数据驱动模型` `不变统计` `控制理论`

## 📋 核心要点

1. 混沌系统预测易产生无界预测，阻碍统计评估。
2. 引入能量约束算子，结合控制理论确保学习动力学耗散且有界。
3. 在Kuramoto-Sivashinsky和Navier-Stokes方程等系统上验证稳定预测和不变统计捕获。

## 📄 摘要（原文）

> Chaos is a fundamental feature of many complex dynamical systems, including weather systems and fluid turbulence. These systems are inherently difficult to predict due to their extreme sensitivity to initial conditions. Many chaotic systems are dissipative and ergodic, motivating data-driven models that aim to learn invariant statistical properties over long time horizons. While recent models have shown empirical success in preserving invariant statistics, they are prone to generating unbounded predictions, which prevent meaningful statistics evaluation. To overcome this, we introduce the Energy-Constrained Operator (ECO) that simultaneously learns the system dynamics while enforcing boundedness in predictions. We leverage concepts from control theory to develop algebraic conditions based on a learnable energy function, ensuring the learned dynamics is dissipative. ECO enforces these algebraic conditions through an efficient closed-form quadratic projection layer, which provides provable trajectory boundedness. To our knowledge, this is the first work establishing such formal guarantees for data-driven chaotic dynamics models. Additionally, the learned invariant level set provides an outer estimate for the strange attractor, a complex structure that is computationally intractable to characterize. We demonstrate empirical success in ECO's ability to generate stable long-horizon forecasts, capturing invariant statistics on systems governed by chaotic PDEs, including the Kuramoto--Sivashinsky and the Navier--Stokes equations.

