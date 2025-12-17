---
layout: default
title: Kinetic-Mamba: Mamba-Assisted Predictions of Stiff Chemical Kinetics
---

# Kinetic-Mamba: Mamba-Assisted Predictions of Stiff Chemical Kinetics

**arXiv**: [2512.14471v1](https://arxiv.org/abs/2512.14471) | [PDF](https://arxiv.org/pdf/2512.14471.pdf)

**作者**: Additi Pandey, Liang Wei, Hessam Babaee, George Em Karniadakis

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Kinetic-Mamba框架，结合Mamba架构高效预测刚性化学动力学，用于燃烧模拟。**

**关键词**: `化学动力学建模` `Mamba架构` `神经算子` `燃烧模拟` `时间序列预测` `质量守恒约束` `潜在空间学习` `刚性系统`

## 📋 核心要点

1. 核心问题：燃烧模拟中刚性化学动力学建模复杂，传统方法计算成本高，难以准确捕捉反应路径和热化学状态演化。
2. 方法要点：提出Kinetic-Mamba框架，结合神经算子的表达能力和Mamba架构的时间建模效率，通过多模型互补预测动力学演化。
3. 实验或效果：在Syngas和GRI-Mech 3.0机制上验证，仅用初始条件即实现高保真预测，并展示良好的外推能力。

## 📝 摘要（中文）

准确的化学动力学建模对燃烧模拟至关重要，它控制着复杂反应路径和热化学状态的演化。本文介绍了Kinetic-Mamba，这是一个基于Mamba的神经算子框架，将神经算子的表达能力与Mamba架构的高效时间建模能力相结合。该框架包含三个互补模型：(i) 一个独立的Mamba模型，从给定初始条件预测热化学状态变量的时间演化；(ii) 一个约束Mamba模型，在学习状态动力学时强制质量守恒；(iii) 一个基于区域的架构，采用两个独立的Mamba模型来捕捉温度依赖区域间的动力学。我们还开发了一个潜在Kinetic-Mamba变体，在降维潜在空间中演化动力学，并在物理流形上重建完整状态。我们使用时间分解和递归预测策略评估Kinetic-Mamba的准确性和鲁棒性。进一步评估模型在不同分布外数据集上的外推能力。在Syngas和GRI-Mech 3.0反应机制上的计算实验表明，我们的框架仅使用状态变量的初始条件就能高保真地预测复杂动力学行为。

## 🔬 方法详解

Kinetic-Mamba是一个基于Mamba的神经算子框架，整体框架包括三个核心模型：独立Mamba模型用于直接预测状态演化，约束Mamba模型在训练中强制质量守恒以提升物理一致性，以及区域感知架构使用两个Mamba模型分别处理不同温度区域的动力学。关键技术创新点在于将Mamba的高效序列建模能力与神经算子的泛化能力结合，并引入潜在空间变体以降低计算复杂度。与现有方法的主要区别在于其专注于刚性化学动力学的端到端预测，通过多模型集成和物理约束设计，提高了预测的准确性和效率，避免了传统数值方法的高计算成本。

## 📊 实验亮点

实验显示Kinetic-Mamba在Syngas和GRI-Mech 3.0反应机制上仅基于初始条件即实现高保真预测，准确捕捉复杂动力学行为；通过时间分解和递归预测策略验证鲁棒性，并在分布外数据集上展示良好外推能力，显著提升预测效率。

## 🎯 应用场景

该研究主要应用于燃烧模拟领域，如发动机设计、能源系统和环境建模，通过高效预测化学动力学行为，可加速复杂反应过程的仿真，降低计算资源需求，提升工业设计和优化效率。

## 📄 摘要（原文）

> Accurate chemical kinetics modeling is essential for combustion simulations, as it governs the evolution of complex reaction pathways and thermochemical states. In this work, we introduce Kinetic-Mamba, a Mamba-based neural operator framework that integrates the expressive power of neural operators with the efficient temporal modeling capabilities of Mamba architectures. The framework comprises three complementary models: (i) a standalone Mamba model that predicts the time evolution of thermochemical state variables from given initial conditions; (ii) a constrained Mamba model that enforces mass conservation while learning the state dynamics; and (iii) a regime-informed architecture employing two standalone Mamba models to capture dynamics across temperature-dependent regimes. We additionally develop a latent Kinetic-Mamba variant that evolves dynamics in a reduced latent space and reconstructs the full state on the physical manifold. We evaluate the accuracy and robustness of Kinetic-Mamba using both time-decomposition and recursive-prediction strategies. We further assess the extrapolation capabilities of the model on varied out-of-distribution datasets. Computational experiments on Syngas and GRI-Mech 3.0 reaction mechanisms demonstrate that our framework achieves high fidelity in predicting complex kinetic behavior using only the initial conditions of the state variables.

