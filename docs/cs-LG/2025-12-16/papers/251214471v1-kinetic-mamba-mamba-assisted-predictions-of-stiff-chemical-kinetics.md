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

**提出Kinetic-Mamba框架，结合Mamba架构与神经算子，以解决燃烧模拟中刚性化学动力学的高精度预测问题。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `化学动力学建模` `Mamba架构` `神经算子` `燃烧模拟` `刚性系统` `潜在空间学习` `质量守恒约束` `温度依赖区域`

## 📋 核心要点

1. 核心问题：燃烧模拟中刚性化学动力学建模面临计算成本高、传统方法难以捕捉复杂反应路径的挑战，现有方法在效率和精度上存在不足。
2. 方法要点：提出Kinetic-Mamba框架，结合Mamba架构的高效时间建模与神经算子的表达能力，通过多个互补模型和潜在空间演化提升预测能力。
3. 实验或效果：在Syngas和GRI-Mech 3.0机制上验证，仅用初始条件即可高保真预测动力学，展现出优异的准确性和外推鲁棒性。

## 📝 摘要（中文）

精确的化学动力学建模对燃烧模拟至关重要，它控制着复杂反应路径和热化学状态的演化。本文介绍了Kinetic-Mamba，这是一个基于Mamba的神经算子框架，将神经算子的表达能力与Mamba架构的高效时间建模能力相结合。该框架包含三个互补模型：（i）一个独立的Mamba模型，从给定初始条件预测热化学状态变量的时间演化；（ii）一个约束Mamba模型，在学习状态动力学的同时强制质量守恒；（iii）一个基于温度依赖区域的架构，采用两个独立的Mamba模型来捕捉跨区域的动力学。我们还开发了一个潜在Kinetic-Mamba变体，在降维潜在空间中演化动力学，并在物理流形上重建完整状态。我们使用时间分解和递归预测策略评估Kinetic-Mamba的准确性和鲁棒性。进一步评估了模型在不同分布外数据集上的外推能力。在Syngas和GRI-Mech 3.0反应机制上的计算实验表明，我们的框架仅使用状态变量的初始条件就能高保真地预测复杂的动力学行为。

## 🔬 方法详解

Kinetic-Mamba是一个基于Mamba的神经算子框架，整体框架包括三个互补模型：独立Mamba模型用于直接预测状态演化，约束Mamba模型在训练中强制质量守恒，以及基于温度依赖区域的架构使用两个Mamba模型捕捉跨区域动力学。关键技术创新点在于将Mamba架构的高效序列建模能力与神经算子的泛化能力相结合，并引入潜在空间变体以降低计算复杂度。与现有方法的主要区别在于其专注于刚性化学动力学的端到端预测，通过多模型集成和约束设计，显著提升了在复杂反应系统中的建模效率和精度。

## 📊 实验亮点

实验在Syngas和GRI-Mech 3.0反应机制上进行，Kinetic-Mamba仅使用初始条件即实现高保真动力学预测，通过时间分解和递归策略验证了其准确性和鲁棒性，并在分布外数据集上展现出良好的外推能力，显著提升了预测性能。

## 🎯 应用场景

该研究主要应用于燃烧模拟领域，如发动机设计、能源系统和环境建模，通过高精度化学动力学预测优化燃烧过程，提高模拟效率，降低计算成本，对工业设计和科学研究具有重要价值。

## 📄 摘要（原文）

> Accurate chemical kinetics modeling is essential for combustion simulations, as it governs the evolution of complex reaction pathways and thermochemical states. In this work, we introduce Kinetic-Mamba, a Mamba-based neural operator framework that integrates the expressive power of neural operators with the efficient temporal modeling capabilities of Mamba architectures. The framework comprises three complementary models: (i) a standalone Mamba model that predicts the time evolution of thermochemical state variables from given initial conditions; (ii) a constrained Mamba model that enforces mass conservation while learning the state dynamics; and (iii) a regime-informed architecture employing two standalone Mamba models to capture dynamics across temperature-dependent regimes. We additionally develop a latent Kinetic-Mamba variant that evolves dynamics in a reduced latent space and reconstructs the full state on the physical manifold. We evaluate the accuracy and robustness of Kinetic-Mamba using both time-decomposition and recursive-prediction strategies. We further assess the extrapolation capabilities of the model on varied out-of-distribution datasets. Computational experiments on Syngas and GRI-Mech 3.0 reaction mechanisms demonstrate that our framework achieves high fidelity in predicting complex kinetic behavior using only the initial conditions of the state variables.

