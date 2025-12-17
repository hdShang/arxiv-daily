---
layout: default
title: Formalized Hopfield Networks and Boltzmann Machines
---

# Formalized Hopfield Networks and Boltzmann Machines

**arXiv**: [2512.07766v1](https://arxiv.org/abs/2512.07766) | [PDF](https://arxiv.org/pdf/2512.07766.pdf)

**作者**: Matteo Cipollina, Michail Karatarakis, Freek Wiedijk

---

## 💡 一句话要点

**在Lean 4中形式化Hopfield网络和Boltzmann机，以支持神经网络的分析与验证。**

**关键词**: `形式化验证` `Hopfield网络` `Boltzmann机` `Lean 4` `神经网络分析` `随机模型`

## 📋 核心要点

1. 核心问题：神经网络的分析与验证困难，缺乏形式化工具支持。
2. 方法要点：使用Lean 4形式化确定性和随机性神经网络模型，包括Hopfield网络和Boltzmann机。
3. 实验或效果：证明Hopfield网络的收敛性和Hebbian学习正确性，以及Boltzmann机的遍历性和平稳分布收敛性。

## 📄 摘要（原文）

> Neural networks are widely used, yet their analysis and verification remain challenging. In this work, we present a Lean 4 formalization of neural networks, covering both deterministic and stochastic models. We first formalize Hopfield networks, recurrent networks that store patterns as stable states. We prove convergence and the correctness of Hebbian learning, a training rule that updates network parameters to encode patterns, here limited to the case of pairwise-orthogonal patterns. We then consider stochastic networks, where updates are probabilistic and convergence is to a stationary distribution. As a canonical example, we formalize the dynamics of Boltzmann machines and prove their ergodicity, showing convergence to a unique stationary distribution using a new formalization of the Perron-Frobenius theorem.

