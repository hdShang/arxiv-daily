---
layout: default
title: Deceptron: Learned Local Inverses for Fast and Stable Physics Inversion
---

# Deceptron: Learned Local Inverses for Fast and Stable Physics Inversion

**arXiv**: [2511.21076v1](https://arxiv.org/abs/2511.21076) | [PDF](https://arxiv.org/pdf/2511.21076.pdf)

**作者**: Aaditya L. Kachhadiya

---

## 💡 一句话要点

**提出Deceptron模块以加速和稳定物理逆问题求解**

**关键词**: `逆问题求解` `局部逆学习` `梯度预处理` `物理模拟` `迭代优化`

## 📋 核心要点

1. 物理逆问题在输入空间常为病态，导致步长敏感和收敛缓慢
2. Deceptron学习局部逆函数，结合多种损失函数训练，用于梯度下降预处理
3. 在1D热传导和阻尼振荡器问题中，迭代次数显著减少，性能媲美高斯-牛顿法

## 📄 摘要（原文）

> Inverse problems in the physical sciences are often ill-conditioned in input space, making progress step-size sensitive. We propose the Deceptron, a lightweight bidirectional module that learns a local inverse of a differentiable forward surrogate. Training combines a supervised fit, forward-reverse consistency, a lightweight spectral penalty, a soft bias tie, and a Jacobian Composition Penalty (JCP) that encourages $J_g(f(x))\,J_f(x)\!\approx\!I$ via JVP/VJP probes. At solve time, D-IPG (Deceptron Inverse-Preconditioned Gradient) takes a descent step in output space, pulls it back through $g$, and projects under the same backtracking and stopping rules as baselines. On Heat-1D initial-condition recovery and a Damped Oscillator inverse problem, D-IPG reaches a fixed normalized tolerance with $\sim$20$\times$ fewer iterations on Heat and $\sim$2-3$\times$ fewer on Oscillator than projected gradient, competitive in iterations and cost with Gauss-Newton. Diagnostics show JCP reduces a measured composition error and tracks iteration gains. We also preview a single-scale 2D instantiation, DeceptronNet (v0), that learns few-step corrections under a strict fairness protocol and exhibits notably fast convergence.

