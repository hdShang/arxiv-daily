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

**提出导数信息傅里叶神经算子(DIFNO)，用于求解PDE约束优化问题。**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)** **动作生成与物理动画 (Animation & Physics)**

**关键词**: `傅里叶神经算子` `导数信息` `PDE约束优化` `算子学习` `反问题求解`

## 📋 核心要点

1. 传统FNO在PDE约束优化中作为替代模型时，其Fréchet导数的精度不足，影响优化效果。
2. DIFNO通过联合最小化输出和Fréchet导数样本的预测误差进行训练，从而精确模拟算子的响应和灵敏度。
3. 数值实验表明，DIFNO在算子学习和求解PDE约束反问题上，样本复杂度更低，精度更高。

## 📝 摘要（中文）

本文提出了一种导数信息傅里叶神经算子(DIFNO)，并研究了其逼近理论和高效训练方法，应用于PDE约束优化问题。DIFNO是一种通过最小化其在输出和高保真算子（例如，参数化PDE解算子）的Fréchet导数样本上的预测误差来训练的FNO。因此，DIFNO不仅可以精确地模拟高保真算子的响应，还可以精确地模拟其灵敏度。为了证明使用DIFNO代替传统FNO作为替代模型的合理性，我们证明了精确的替代驱动PDE约束优化需要精确的替代Fréchet导数。然后，对于连续可微算子，我们建立了(i) FNO及其Fréchet导数在紧集上的同时通用逼近，以及(ii) FNO在具有无界支撑的输入测度的加权Sobolev空间中的通用逼近。我们的理论结果证明了FNO在精确的导数信息算子学习和精确求解PDE约束优化方面的能力。此外，我们开发了使用降维和多分辨率技术的高效训练方案，这些技术显著降低了Fréchet导数学习的内存和计算成本。非线性扩散-反应、亥姆霍兹和Navier-Stokes方程的数值例子表明，DIFNO在算子学习和求解无限维PDE约束反问题方面具有优越的样本复杂度，在低训练样本量下实现了高精度。

## 🔬 方法详解

**问题定义**：论文旨在解决PDE约束优化问题，现有方法如传统FNO作为替代模型时，其Fréchet导数的精度不足，导致优化效果不佳。准确的Fréchet导数对于PDE约束优化至关重要，而传统FNO在这方面存在局限性。

**核心思路**：论文的核心思路是训练一个能够同时精确预测算子输出及其Fréchet导数的神经算子。通过在训练过程中引入导数信息，使得神经算子能够更好地捕捉算子的灵敏度，从而提高PDE约束优化的效果。

**技术框架**：DIFNO的整体框架是基于傅里叶神经算子(FNO)，但其训练方式有所不同。具体流程如下：1) 收集高保真算子的输出和Fréchet导数样本；2) 构建FNO模型；3) 定义损失函数，该损失函数同时考虑输出预测误差和Fréchet导数预测误差；4) 使用优化算法最小化损失函数，训练DIFNO模型。

**关键创新**：最重要的技术创新点在于将导数信息融入到FNO的训练过程中。传统FNO只关注输出的预测精度，而DIFNO同时关注输出和Fréchet导数的预测精度。这种导数信息的引入使得DIFNO能够更好地捕捉算子的灵敏度，从而提高PDE约束优化的效果。与现有方法的本质区别在于，DIFNO是一种导数感知的算子学习方法，而传统FNO则不是。

**关键设计**：论文采用联合损失函数，同时考虑输出预测误差和Fréchet导数预测误差。为了降低计算成本，论文还采用了降维和多分辨率技术。具体的网络结构和参数设置取决于具体的PDE问题，但核心思想是利用导数信息来提高算子学习的精度。

## 📊 实验亮点

论文通过非线性扩散-反应、亥姆霍兹和Navier-Stokes方程的数值实验验证了DIFNO的有效性。实验结果表明，DIFNO在算子学习和求解无限维PDE约束反问题方面具有优越的样本复杂度，即在较低的训练样本量下即可实现较高的精度。相比于传统FNO，DIFNO在PDE约束优化问题上表现出更强的性能。

## 🎯 应用场景

DIFNO可广泛应用于涉及PDE约束优化的领域，例如反问题求解、控制问题、参数估计、不确定性量化等。通过构建高精度、低成本的替代模型，DIFNO能够加速优化过程，降低计算成本，并提高优化结果的可靠性。该研究对科学计算和工程设计具有重要的实际价值和潜在影响。

## 📄 摘要（原文）

> We present approximation theories and efficient training methods for derivative-informed Fourier neural operators (DIFNOs) with applications to PDE-constrained optimization. A DIFNO is an FNO trained by minimizing its prediction error jointly on output and Fréchet derivative samples of a high-fidelity operator (e.g., a parametric PDE solution operator). As a result, a DIFNO can closely emulate not only the high-fidelity operator's response but also its sensitivities. To motivate the use of DIFNOs instead of conventional FNOs as surrogate models, we show that accurate surrogate-driven PDE-constrained optimization requires accurate surrogate Fréchet derivatives. Then, for continuously differentiable operators, we establish (i) simultaneous universal approximation of FNOs and their Fréchet derivatives on compact sets, and (ii) universal approximation of FNOs in weighted Sobolev spaces with input measures that have unbounded supports. Our theoretical results certify the capability of FNOs for accurate derivative-informed operator learning and accurate solution of PDE-constrained optimization. Furthermore, we develop efficient training schemes using dimension reduction and multi-resolution techniques that significantly reduce memory and computational costs for Fréchet derivative learning. Numerical examples on nonlinear diffusion--reaction, Helmholtz, and Navier--Stokes equations demonstrate that DIFNOs are superior in sample complexity for operator learning and solving infinite-dimensional PDE-constrained inverse problems, achieving high accuracy at low training sample sizes.

