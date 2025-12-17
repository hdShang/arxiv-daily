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

**提出导数信息傅里叶神经算子，通过联合优化输出和导数样本，提升PDE约束优化的精度和效率。**

🎯 **匹配领域**: **强化学习**

**关键词**: `傅里叶神经算子` `导数信息学习` `PDE约束优化` `通用近似理论` `Fréchet导数` `样本复杂度` `多分辨率训练` `无限维逆问题`

## 📋 核心要点

1. 现有傅里叶神经算子在PDE约束优化中，由于缺乏精确导数信息，导致代理模型驱动优化时精度不足。
2. 提出导数信息傅里叶神经算子，通过联合训练输出和Fréchet导数样本，实现算子和导数的同时高精度近似。
3. 实验显示DIFNO在低样本量下显著提升优化精度，并降低计算成本，验证了其高效性和通用近似能力。

## 📝 摘要（中文）

本文介绍了导数信息傅里叶神经算子的近似理论和高效训练方法，应用于偏微分方程约束优化。DIFNO是一种傅里叶神经算子，通过最小化其在高保真算子输出和Fréchet导数样本上的预测误差进行训练，从而不仅能紧密模拟高保真算子的响应，还能模拟其敏感性。为证明DIFNO优于传统FNO作为代理模型，我们指出精确的代理驱动PDE约束优化需要精确的代理Fréchet导数。对于连续可微算子，我们建立了（i）FNO及其Fréchet导数在紧集上的同时通用近似性，以及（ii）FNO在具有无界支持的输入测度的加权Sobolev空间中的通用近似性。这些理论结果验证了FNO在精确导数信息算子学习和精确求解PDE约束优化方面的能力。此外，我们开发了使用降维和多分辨率技术的高效训练方案，显著降低了Fréchet导数学习的内存和计算成本。在非线性扩散-反应、Helmholtz和Navier-Stokes方程上的数值实验表明，DIFNO在算子学习和求解无限维PDE约束逆问题的样本复杂度方面表现优越，能在低训练样本量下实现高精度。

## 🔬 方法详解

DIFNO基于傅里叶神经算子框架，通过最小化高保真算子的输出和Fréchet导数样本的联合损失函数进行训练。关键创新在于引入导数信息学习，利用降维和多分辨率技术优化训练过程，减少内存和计算开销。与现有FNO的主要区别在于，DIFNO不仅学习算子映射，还学习其导数，从而在PDE约束优化中提供更精确的敏感性信息。

## 📊 实验亮点

数值实验表明，DIFNO在非线性扩散-反应、Helmholtz和Navier-Stokes方程上，相比传统FNO，样本复杂度显著降低，能在少量训练样本下实现高精度优化，验证了其高效性和理论优势。

## 🎯 应用场景

该研究主要应用于偏微分方程约束优化问题，如非线性扩散-反应、Helmholtz和Navier-Stokes方程的逆问题求解，在工程和科学计算中具有广泛价值，可提升优化效率和精度。

## 📄 摘要（原文）

> We present approximation theories and efficient training methods for derivative-informed Fourier neural operators (DIFNOs) with applications to PDE-constrained optimization. A DIFNO is an FNO trained by minimizing its prediction error jointly on output and Fréchet derivative samples of a high-fidelity operator (e.g., a parametric PDE solution operator). As a result, a DIFNO can closely emulate not only the high-fidelity operator's response but also its sensitivities. To motivate the use of DIFNOs instead of conventional FNOs as surrogate models, we show that accurate surrogate-driven PDE-constrained optimization requires accurate surrogate Fréchet derivatives. Then, for continuously differentiable operators, we establish (i) simultaneous universal approximation of FNOs and their Fréchet derivatives on compact sets, and (ii) universal approximation of FNOs in weighted Sobolev spaces with input measures that have unbounded supports. Our theoretical results certify the capability of FNOs for accurate derivative-informed operator learning and accurate solution of PDE-constrained optimization. Furthermore, we develop efficient training schemes using dimension reduction and multi-resolution techniques that significantly reduce memory and computational costs for Fréchet derivative learning. Numerical examples on nonlinear diffusion--reaction, Helmholtz, and Navier--Stokes equations demonstrate that DIFNOs are superior in sample complexity for operator learning and solving infinite-dimensional PDE-constrained inverse problems, achieving high accuracy at low training sample sizes.

