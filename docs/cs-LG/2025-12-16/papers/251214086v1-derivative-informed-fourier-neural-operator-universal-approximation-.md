---
layout: default
title: Derivative-Informed Fourier Neural Operator: Universal Approximation and Applications to PDE-Constrained Optimization
---

# Derivative-Informed Fourier Neural Operator: Universal Approximation and Applications to PDE-Constrained Optimization

**arXiv**: [2512.14086v1](https://arxiv.org/abs/2512.14086) | [PDF](https://arxiv.org/pdf/2512.14086.pdf)

**作者**: Boyuan Yao, Dingcheng Luo, Lianghao Cao, Nikola Kovachki, Thomas O'Leary-Roseberry, Omar Ghattas

**分类**: cs.LG, math.NA

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出导数信息傅里叶神经算子，通过联合优化输出和导数样本实现高效PDE约束优化**

**关键词**: `傅里叶神经算子` `导数信息学习` `PDE约束优化` `通用近似理论` `Fréchet导数` `降维训练` `多分辨率技术` `逆问题求解`

## 📋 核心要点

1. 现有FNO作为代理模型在PDE约束优化中导数精度不足，影响优化效果
2. 提出DIFNO，通过联合训练输出和Fréchet导数样本提升导数模拟能力
3. 理论证明通用近似性，实验显示在低样本量下实现高精度，显著降低计算成本

## 📝 摘要（中文）

本文提出了导数信息傅里叶神经算子的近似理论和高效训练方法，应用于偏微分方程约束优化。DIFNO是一种通过最小化高保真算子输出和Fréchet导数样本预测误差联合训练的FNO，能够紧密模拟算子的响应和灵敏度。研究表明，准确的代理驱动PDE约束优化需要准确的代理Fréchet导数。对于连续可微算子，我们建立了FNO及其Fréchet导数在紧集上的同时通用近似性，以及在具有无界支撑的输入测度加权Sobolev空间中FNO的通用近似性。理论结果验证了FNO在准确导数信息算子学习和PDE约束优化求解中的能力。此外，我们开发了使用降维和多分辨率技术的高效训练方案，显著降低了Fréchet导数学习的内存和计算成本。非线性扩散-反应、Helmholtz和Navier-Stokes方程的数值实验表明，DIFNO在算子学习和求解无限维PDE约束逆问题的样本复杂度方面具有优越性，在低训练样本量下实现高精度。

## 🔬 方法详解

DIFNO基于傅里叶神经算子框架，核心创新在于训练过程中同时最小化高保真算子的输出误差和Fréchet导数误差。整体框架采用FNO作为基础架构，通过联合损失函数优化，使网络不仅能准确预测算子响应，还能精确模拟其灵敏度。关键技术创新包括：1）同时通用近似理论证明FNO及其导数在紧集上的逼近能力；2）开发高效的降维和多分辨率训练技术，减少导数学习的内存和计算开销。与现有FNO的主要区别在于训练目标包含导数信息，从而在PDE约束优化中提供更准确的梯度信息，提升优化效率和精度。

## 📊 实验亮点

数值实验在非线性扩散-反应、Helmholtz和Navier-Stokes方程上验证DIFNO的优越性：在低训练样本量下实现高精度，样本复杂度显著优于传统FNO，高效解决无限维PDE约束逆问题，计算成本大幅降低。

## 🎯 应用场景

该研究主要应用于偏微分方程约束的优化问题，如逆问题求解、参数估计和最优控制，在工程、物理和计算科学中具有广泛价值，能高效处理高维、非线性PDE系统，降低计算成本。

## 📄 摘要（原文）

> We present approximation theories and efficient training methods for derivative-informed Fourier neural operators (DIFNOs) with applications to PDE-constrained optimization. A DIFNO is an FNO trained by minimizing its prediction error jointly on output and Fréchet derivative samples of a high-fidelity operator (e.g., a parametric PDE solution operator). As a result, a DIFNO can closely emulate not only the high-fidelity operator's response but also its sensitivities. To motivate the use of DIFNOs instead of conventional FNOs as surrogate models, we show that accurate surrogate-driven PDE-constrained optimization requires accurate surrogate Fréchet derivatives. Then, for continuously differentiable operators, we establish (i) simultaneous universal approximation of FNOs and their Fréchet derivatives on compact sets, and (ii) universal approximation of FNOs in weighted Sobolev spaces with input measures that have unbounded supports. Our theoretical results certify the capability of FNOs for accurate derivative-informed operator learning and accurate solution of PDE-constrained optimization. Furthermore, we develop efficient training schemes using dimension reduction and multi-resolution techniques that significantly reduce memory and computational costs for Fréchet derivative learning. Numerical examples on nonlinear diffusion--reaction, Helmholtz, and Navier--Stokes equations demonstrate that DIFNOs are superior in sample complexity for operator learning and solving infinite-dimensional PDE-constrained inverse problems, achieving high accuracy at low training sample sizes.

