---
layout: default
title: Diagonalizing the Softmax: Hadamard Initialization for Tractable Cross-Entropy Dynamics
---

# Diagonalizing the Softmax: Hadamard Initialization for Tractable Cross-Entropy Dynamics

**arXiv**: [2512.04006v1](https://arxiv.org/abs/2512.04006) | [PDF](https://arxiv.org/pdf/2512.04006.pdf)

**作者**: Connall Garrod, Jonathan P. Keating, Christos Thrampoulidis

---

## 💡 一句话要点

**提出Hadamard初始化以分析交叉熵训练动态，证明梯度流收敛到神经崩溃几何**

**关键词**: `交叉熵训练` `非凸优化` `神经崩溃` `梯度流` `Hadamard初始化` `两层线性网络`

## 📋 核心要点

1. 核心问题：交叉熵训练动态缺乏非凸理论分析，现有简化方法忽略其与平方损失的本质差异
2. 方法要点：通过Hadamard初始化对角化softmax算子，简化两层线性神经网络动态分析
3. 实验或效果：构建Lyapunov函数证明全局收敛，首次理论证实神经崩溃几何的收敛性

## 📄 摘要（原文）

> Cross-entropy (CE) training loss dominates deep learning practice, yet existing theory often relies on simplifications, either replacing it with squared loss or restricting to convex models, that miss essential behavior. CE and squared loss generate fundamentally different dynamics, and convex linear models cannot capture the complexities of non-convex optimization. We provide an in-depth characterization of multi-class CE optimization dynamics beyond the convex regime by analyzing a canonical two-layer linear neural network with standard-basis vectors as inputs: the simplest non-convex extension for which the implicit bias remained unknown. This model coincides with the unconstrained features model used to study neural collapse, making our work the first to prove that gradient flow on CE converges to the neural collapse geometry. We construct an explicit Lyapunov function that establishes global convergence, despite the presence of spurious critical points in the non-convex landscape. A key insight underlying our analysis is an inconspicuous finding: Hadamard Initialization diagonalizes the softmax operator, freezing the singular vectors of the weight matrices and reducing the dynamics entirely to their singular values. This technique opens a pathway for analyzing CE training dynamics well beyond our specific setting considered here.

