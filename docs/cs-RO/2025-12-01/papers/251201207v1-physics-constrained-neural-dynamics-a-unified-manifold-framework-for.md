---
layout: default
title: Physics-Constrained Neural Dynamics: A Unified Manifold Framework for Large-Scale Power Flow Computation
---

# Physics-Constrained Neural Dynamics: A Unified Manifold Framework for Large-Scale Power Flow Computation

**arXiv**: [2512.01207v1](https://arxiv.org/abs/2512.01207) | [PDF](https://arxiv.org/pdf/2512.01207.pdf)

**作者**: Xuezhi Liu

---

## 💡 一句话要点

**提出基于流形几何与梯度流的神经物理潮流计算方法，以解决传统方法初始值敏感与深度学习物理一致性不足的问题。**

**关键词**: `潮流计算` `物理约束学习` `流形几何` `梯度流` `无监督学习`

## 📋 核心要点

1. 核心问题：传统牛顿-拉夫森法初始值敏感、批量计算效率低，现有深度学习潮流求解器依赖监督学习且难以保证物理一致性。
2. 方法要点：将潮流方程描述为约束流形，构建能量函数与梯度流，将求解转化为动力系统平衡点寻找问题，实现无监督物理约束学习。
3. 实验或效果：未知。

## 📄 摘要（原文）

> Power flow analysis is a fundamental tool for power system analysis, planning, and operational control. Traditional Newton-Raphson methods suffer from limitations such as initial value sensitivity and low efficiency in batch computation, while existing deep learning-based power flow solvers mostly rely on supervised learning, requiring pre-solving of numerous cases and struggling to guarantee physical consistency. This paper proposes a neural physics power flow solving method based on manifold geometry and gradient flow, by describing the power flow equations as a constraint manifold, and constructing an energy function \(V(\mathbf{x}) = \frac{1}{2}\\|\mathbf{F}(\mathbf{x})\\|^2\) and gradient flow \(\frac{d\mathbf{x}}{dt} = -\nabla V(\mathbf{x})\), transforming power flow solving into an equilibrium point finding problem for dynamical systems. Neural networks are trained in an unsupervised manner by directly minimizing physical residuals, requiring no labeled data, achieving true "end-to-end" physics-constrained learning.

