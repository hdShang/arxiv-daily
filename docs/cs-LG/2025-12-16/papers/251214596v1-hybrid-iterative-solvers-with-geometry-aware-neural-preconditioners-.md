---
layout: default
title: Hybrid Iterative Solvers with Geometry-Aware Neural Preconditioners for Parametric PDEs
---

# Hybrid Iterative Solvers with Geometry-Aware Neural Preconditioners for Parametric PDEs

**arXiv**: [2512.14596v1](https://arxiv.org/abs/2512.14596) | [PDF](https://arxiv.org/pdf/2512.14596.pdf)

**作者**: Youngkyu Lee, Francesc Levrero Florencio, Jay Pathak, George Em Karniadakis

**分类**: cs.LG, math.NA

**发布日期**: 2025-12-16

**备注**: 19 pages, 10 figures, 3 tables

---

## 💡 一句话要点

**提出几何感知神经预条件器与混合迭代求解器，以解决参数偏微分方程在任意几何域上的求解鲁棒性问题。**

**关键词**: `参数偏微分方程` `几何感知学习` `神经预条件器` `混合迭代求解器` `深度算子网络` `非结构化网格` `有限元方法` `计算科学`

## 📋 核心要点

1. 现有混合求解器对训练几何敏感，在未见几何上性能下降，限制了泛化能力。
2. 提出Geo-DeepONet，整合有限元域信息，实现跨任意网格的几何感知算子学习。
3. 实验表明，混合求解器在多样几何上提升鲁棒性和效率，适用于实际参数PDE问题。

## 📝 摘要（中文）

参数偏微分方程（PDEs）的经典迭代求解器收敛行为通常对域和离散化高度敏感。先前，我们通过将经典求解器与神经算子结合，针对特定几何引入了混合求解器，但它们在训练未遇见的几何上表现不佳。为解决这一挑战，我们引入了Geo-DeepONet，这是一种几何感知的深度算子网络，它整合了从有限元离散化中提取的域信息。Geo-DeepONet能够在任意非结构化网格上实现精确的算子学习，无需重新训练。基于此，我们通过将Geo-DeepONet与传统方法（如松弛方案和Krylov子空间算法）耦合，开发了一类几何感知的混合预条件迭代求解器。通过在多样非结构化域上的参数PDE数值实验，我们证明了所提混合求解器在多个实际应用中的增强鲁棒性和效率。

## 🔬 方法详解

论文提出几何感知混合迭代求解器框架，核心是Geo-DeepONet模型，它基于深度算子网络（DeepONet）架构，但创新性地融入有限元离散化的几何信息作为输入，使网络能处理任意非结构化网格。关键技术创新在于几何感知设计，通过提取域特征（如网格节点和连接性）来增强神经预条件器的泛化能力。与现有方法的主要区别在于：传统混合求解器依赖特定几何训练，而Geo-DeepONet无需重新训练即可适应新几何，结合经典迭代方法（如松弛和Krylov算法）形成混合求解器，提升求解鲁棒性。

## 📊 实验亮点

数值实验在多样非结构化域上进行，结果显示，所提混合求解器相比传统方法，在收敛速度和鲁棒性上显著提升，能有效处理训练未见的几何，验证了Geo-DeepONet的泛化能力和实际应用价值。

## 🎯 应用场景

该研究适用于参数偏微分方程求解领域，如计算流体动力学、结构力学和电磁学中的多物理场模拟，能处理复杂几何域（如不规则边界或自适应网格），提高实际工程和科学计算中的求解效率和稳定性。

## 📄 摘要（原文）

> The convergence behavior of classical iterative solvers for parametric partial differential equations (PDEs) is often highly sensitive to the domain and specific discretization of PDEs. Previously, we introduced hybrid solvers by combining the classical solvers with neural operators for a specific geometry 1, but they tend to under-perform in geometries not encountered during training. To address this challenge, we introduce Geo-DeepONet, a geometry-aware deep operator network that incorporates domain information extracted from finite element discretizations. Geo-DeepONet enables accurate operator learning across arbitrary unstructured meshes without requiring retraining. Building on this, we develop a class of geometry-aware hybrid preconditioned iterative solvers by coupling Geo-DeepONet with traditional methods such as relaxation schemes and Krylov subspace algorithms. Through numerical experiments on parametric PDEs posed over diverse unstructured domains, we demonstrate the enhanced robustness and efficiency of the proposed hybrid solvers for multiple real-world applications.

