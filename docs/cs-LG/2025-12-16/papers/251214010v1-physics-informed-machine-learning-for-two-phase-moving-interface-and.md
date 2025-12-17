---
layout: default
title: Physics-Informed Machine Learning for Two-Phase Moving-Interface and Stefan Problems
---

# Physics-Informed Machine Learning for Two-Phase Moving-Interface and Stefan Problems

**arXiv**: [2512.14010v1](https://arxiv.org/abs/2512.14010) | [PDF](https://arxiv.org/pdf/2512.14010.pdf)

**作者**: Che-Chia Chang, Te-Sheng Lin, Ming-Chih Lai

**分类**: physics.comp-ph, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于物理信息神经网络的框架以解决两相Stefan移动界面问题**

**关键词**: `物理信息神经网络` `Stefan问题` `移动界面` `两相流` `相变建模` `自由边界问题` `界面不连续性` `数值模拟`

## 📋 核心要点

1. Stefan问题作为相变过程的经典自由边界问题，面临移动界面和非线性耦合带来的计算挑战，传统方法处理界面不连续性时存在困难。
2. 提出双神经网络框架：一个网络显式跟踪界面运动，另一个网络建模温度场，通过增强输入准确捕捉界面处的梯度跳跃。
3. 数值实验显示，该方法在动态Stefan问题上优于现有神经网络方法，能有效处理不稳定界面演化，提供高精度解决方案。

## 📝 摘要（中文）

Stefan问题是一个经典的相变过程自由边界问题，因其移动界面和非线性温度-相耦合而带来计算挑战。本文开发了一个基于物理信息的神经网络框架来解决两相Stefan问题。该方法显式跟踪界面运动，并在保持温度场全局一致性的同时，强制界面处温度梯度的不连续性。我们的方法采用两个神经网络：一个表示移动界面，另一个用于温度场。界面网络允许在空间域中快速分类热扩散率，这是为温度网络选择训练点的关键步骤。温度网络的输入通过修改的零水平集函数增强，以准确捕捉界面处法向导数的跳跃。在两相动态Stefan问题上的数值实验表明，与文献中其他神经网络方法相比，我们提出的方法具有更高的准确性和有效性。结果表明，该框架为解决受移动边界控制的相变问题提供了一个鲁棒且灵活的替代传统数值方法的选择。此外，该方法能够捕捉与Mullins-Sekerka不稳定性相关的不稳定界面演化。

## 🔬 方法详解

本文提出一个基于物理信息的神经网络框架，核心是双网络架构：一个神经网络用于显式建模移动界面，另一个神经网络用于表示温度场。关键技术创新在于，界面网络通过快速分类热扩散率来指导温度网络的训练点选择，而温度网络则利用修改的零水平集函数作为输入增强，以精确捕捉界面处的法向导数不连续性。与现有方法的主要区别在于，该方法显式处理界面运动和不连续性，避免了传统神经网络方法在界面附近精度不足的问题，同时通过物理约束确保全局一致性。

## 📊 实验亮点

数值实验表明，该方法在两相动态Stefan问题上实现了显著精度提升，优于文献中其他神经网络方法，并能成功捕捉Mullins-Sekerka不稳定性导致的不稳定界面演化，验证了框架的鲁棒性和有效性。

## 🎯 应用场景

该研究在相变过程建模中具有广泛潜在应用，如材料科学中的凝固和熔化模拟、能源领域的相变储能系统优化，以及环境工程中的冰层生长预测。其实际价值在于为移动边界问题提供高效、灵活的数值解决方案，替代传统计算密集型方法。

## 📄 摘要（原文）

> The Stefan problem is a classical free-boundary problem that models phase-change processes and poses computational challenges due to its moving interface and nonlinear temperature-phase coupling. In this work, we develop a physics-informed neural network framework for solving two-phase Stefan problems. The proposed method explicitly tracks the interface motion and enforces the discontinuity in the temperature gradient across the interface while maintaining global consistency of the temperature field. Our approach employs two neural networks: one representing the moving interface and the other for the temperature field. The interface network allows rapid categorization of thermal diffusivity in the spatial domain, which is a crucial step for selecting training points for the temperature network. The temperature network's input is augmented with a modified zero-level set function to accurately capture the jump in its normal derivative across the interface. Numerical experiments on two-phase dynamical Stefan problems demonstrate the superior accuracy and effectiveness of our proposed method compared with the ones obtained by other neural network methodology in literature. The results indicate that the proposed framework offers a robust and flexible alternative to traditional numerical methods for solving phase-change problems governed by moving boundaries. In addition, the proposed method can capture an unstable interface evolution associated with the Mullins-Sekerka instability.

