---
layout: default
title: Modeling and Inverse Identification of Interfacial Heat Conduction in Finite Layer and Semi-Infinite Substrate Systems via a Physics-Guided Neural Framework
---

# Modeling and Inverse Identification of Interfacial Heat Conduction in Finite Layer and Semi-Infinite Substrate Systems via a Physics-Guided Neural Framework

**arXiv**: [2512.02618v1](https://arxiv.org/abs/2512.02618) | [PDF](https://arxiv.org/pdf/2512.02618.pdf)

**作者**: Wenhao Sha, Tienchong Chang

---

## 💡 一句话要点

**提出HeatTransFormer以解决界面主导热传导的正逆建模问题**

**关键词**: `界面热传导` `物理引导神经网络` `Transformer架构` `逆问题识别` `扩散问题` `热物性估计`

## 📋 核心要点

1. 核心问题：有限芯片层与半无限基板界面热传导梯度陡峭，传统数值方法计算量大，PINNs在界面处收敛不稳定且物理一致性差。
2. 方法要点：结合物理引导的时空采样、拉普拉斯激活函数和无掩码注意力机制，构建Transformer架构，增强梯度解析与物理一致性。
3. 实验或效果：模型在界面处生成连贯温度场，并通过物理约束逆策略可靠识别三个未知热物性，仅需外部测量数据。

## 📄 摘要（原文）

> Heat transfer in semiconductor devices is dominated by chip and substrate assemblies, where heat generated within a finite chip layer dissipates into a semi-infinite substrate with much higher thermophysical properties. This mismatch produces steep interfacial temperature gradients, making the transient thermal response highly sensitive to the interface. Conventional numerical solvers require excessive discretization to resolve these dynamics, while physics-informed neural networks (PINNs) often exhibit unstable convergence and loss of physical consistency near the material interface. To address these challenges, we introduce HeatTransFormer, a physics-guided Transformer architecture for interface-dominated diffusion problems. The framework integrates physically informed spatiotemporal sampling, a Laplace-based activation emulating analytical diffusion solutions, and a mask-free attention mechanism supporting bidirectional spatiotemporal coupling. These components enable the model to resolve steep gradients, maintain physical consistency, and remain stable where PINNs typically fail. HeatTransFormer produces coherent temperature fields across the interface when applied to a finite layer and semi-infinite substrate configuration. Coupled with a physics-constrained inverse strategy, it further enables reliable identification of three unknown thermal properties simultaneously using only external measurements. Overall, this work demonstrates that physics-guided Transformer architectures provide a unified framework for forward and inverse modeling in interface-dominated thermal systems.

