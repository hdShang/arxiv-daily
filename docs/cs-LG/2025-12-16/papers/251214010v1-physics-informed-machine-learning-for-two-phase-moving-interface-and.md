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

🎯 **匹配领域**: **视觉里程计**

**关键词**: `物理信息神经网络` `Stefan问题` `移动界面` `两相流` `相变模拟` `自由边界问题` `Mullins-Sekerka不稳定性` `数值求解`

## 📋 核心要点

1. Stefan问题作为经典自由边界问题，因移动界面和温度-相非线性耦合导致传统数值方法计算复杂且精度受限。
2. 提出双神经网络框架：界面网络跟踪运动并分类热扩散率，温度网络通过增强输入捕捉梯度跳跃，实现物理约束的精确求解。
3. 数值实验显示，相比现有神经网络方法，该方法在精度和有效性上显著提升，并能模拟不稳定界面演化如Mullins-Sekerka不稳定性。

## 📝 摘要（中文）

Stefan问题是一个经典的相变过程自由边界问题，因其移动界面和非线性温度-相耦合而带来计算挑战。本研究开发了一个基于物理信息的神经网络框架来解决两相Stefan问题。该方法显式跟踪界面运动，在保持温度场全局一致性的同时，强制界面处温度梯度的不连续性。我们的方法采用两个神经网络：一个表示移动界面，另一个用于温度场。界面网络允许在空间域中快速分类热扩散率，这是为温度网络选择训练点的关键步骤。温度网络的输入通过修改的零水平集函数进行增强，以准确捕捉界面处法向导数的跳跃。在两相动态Stefan问题上的数值实验表明，与文献中其他神经网络方法相比，我们提出的方法具有更高的准确性和有效性。结果表明，该框架为解决受移动边界控制的相变问题提供了一个稳健且灵活的替代传统数值方法的选择。此外，该方法能够捕捉与Mullins-Sekerka不稳定性相关的不稳定界面演化。

## 🔬 方法详解

论文提出一个基于物理信息神经网络（PINN）的框架，用于求解两相Stefan问题。整体框架由两个神经网络组成：界面网络负责显式跟踪移动界面并快速分类空间域中的热扩散率，从而指导温度网络的训练点选择；温度网络则通过输入增强（使用修改的零水平集函数）来准确捕捉界面处温度法向导数的跳跃，同时强制物理约束如能量守恒。关键技术创新在于将界面运动与温度场解耦处理，并通过增强机制处理不连续性，与现有PINN方法相比，该方法更直接地建模界面动态并提高求解精度。

## 📊 实验亮点

数值实验表明，该方法在两相动态Stefan问题上相比文献中其他神经网络方法，展现出更高的精度和有效性，并能成功捕捉Mullins-Sekerka不稳定性相关的不稳定界面演化，验证了框架的优越性能。

## 🎯 应用场景

该研究在相变过程模拟中具有广泛潜在应用，如材料科学中的凝固与熔化、能源领域的相变储能、以及生物医学中的组织冷冻治疗。其稳健性和灵活性为传统数值方法提供了高效替代，有助于优化工业设计和科学研究中的移动边界问题求解。

## 📄 摘要（原文）

> The Stefan problem is a classical free-boundary problem that models phase-change processes and poses computational challenges due to its moving interface and nonlinear temperature-phase coupling. In this work, we develop a physics-informed neural network framework for solving two-phase Stefan problems. The proposed method explicitly tracks the interface motion and enforces the discontinuity in the temperature gradient across the interface while maintaining global consistency of the temperature field. Our approach employs two neural networks: one representing the moving interface and the other for the temperature field. The interface network allows rapid categorization of thermal diffusivity in the spatial domain, which is a crucial step for selecting training points for the temperature network. The temperature network's input is augmented with a modified zero-level set function to accurately capture the jump in its normal derivative across the interface. Numerical experiments on two-phase dynamical Stefan problems demonstrate the superior accuracy and effectiveness of our proposed method compared with the ones obtained by other neural network methodology in literature. The results indicate that the proposed framework offers a robust and flexible alternative to traditional numerical methods for solving phase-change problems governed by moving boundaries. In addition, the proposed method can capture an unstable interface evolution associated with the Mullins-Sekerka instability.

