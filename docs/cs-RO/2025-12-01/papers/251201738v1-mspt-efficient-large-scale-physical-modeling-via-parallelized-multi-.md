---
layout: default
title: MSPT: Efficient Large-Scale Physical Modeling via Parallelized Multi-Scale Attention
---

# MSPT: Efficient Large-Scale Physical Modeling via Parallelized Multi-Scale Attention

**arXiv**: [2512.01738v1](https://arxiv.org/abs/2512.01738) | [PDF](https://arxiv.org/pdf/2512.01738.pdf)

**作者**: Pedro M. P. Curvo, Jan-Willem van de Meent, Maksim Zhdanov

---

## 💡 一句话要点

**提出MSPT架构以解决工业级物理模拟中大规模空间元素的高效建模问题**

**关键词**: `多尺度注意力` `物理建模` `神经求解器` `大规模模拟` `并行计算`

## 📋 核心要点

1. 核心问题：神经求解器在工业级物理模拟中难以高效捕获数百万空间元素的细粒度局部交互和长程全局依赖
2. 方法要点：结合局部点注意力和全局补丁级注意力，使用球树划分不规则几何输入域
3. 实验或效果：在标准PDE基准和大规模空气动力学数据集上实现最先进精度，显著降低内存占用和计算成本

## 📄 摘要（原文）

> A key scalability challenge in neural solvers for industrial-scale physics simulations is efficiently capturing both fine-grained local interactions and long-range global dependencies across millions of spatial elements. We introduce the Multi-Scale Patch Transformer (MSPT), an architecture that combines local point attention within patches with global attention to coarse patch-level representations. To partition the input domain into spatially-coherent patches, we employ ball trees, which handle irregular geometries efficiently. This dual-scale design enables MSPT to scale to millions of points on a single GPU. We validate our method on standard PDE benchmarks (elasticity, plasticity, fluid dynamics, porous flow) and large-scale aerodynamic datasets (ShapeNet-Car, Ahmed-ML), achieving state-of-the-art accuracy with substantially lower memory footprint and computational cost.

