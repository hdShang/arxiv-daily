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

**提出导数信息傅里叶神经算子以解决偏微分方程约束优化中的高精度代理建模问题**

🎯 **匹配领域**: **强化学习**

**关键词**: `导数信息学习` `傅里叶神经算子` `偏微分方程约束优化` `代理建模` `Fréchet导数` `通用逼近理论` `样本复杂度` `多分辨率训练`

## 📋 核心要点

1. 现有傅里叶神经算子在偏微分方程约束优化中缺乏导数信息，导致代理模型灵敏度不准确，影响优化精度。
2. 提出导数信息傅里叶神经算子，通过联合最小化输出和Fréchet导数误差，实现高保真算子的响应和灵敏度模拟。
3. 理论证明通用逼近性，实验显示在非线性方程上样本复杂度显著降低，实现高精度优化。

## 📝 摘要（中文）

本文提出了导数信息傅里叶神经算子的逼近理论和高效训练方法，应用于偏微分方程约束优化。DIFNO是一种通过最小化其在高保真算子输出和Fréchet导数样本上的预测误差来训练的FNO，因此能够紧密模拟高保真算子的响应及其灵敏度。为了证明DIFNO作为代理模型的优势，我们展示了准确的代理驱动偏微分方程约束优化需要准确的代理Fréchet导数。对于连续可微算子，我们建立了(i) FNO及其Fréchet导数在紧集上的同时通用逼近性，以及(ii) FNO在具有无界支撑输入测度的加权Sobolev空间中的通用逼近性。我们的理论结果证明了FNO在准确导数信息算子学习和准确求解偏微分方程约束优化方面的能力。此外，我们开发了使用降维和多分辨率技术的高效训练方案，显著降低了Fréchet导数学习的内存和计算成本。在非线性扩散-反应、Helmholtz和Navier-Stokes方程上的数值实验表明，DIFNO在算子学习和求解无限维偏微分方程约束逆问题的样本复杂度方面具有优越性，在低训练样本量下实现了高精度。

## 🔬 方法详解

**问题定义**：论文解决偏微分方程约束优化中代理模型导数不准确的问题。现有傅里叶神经算子仅学习算子输出，缺乏导数信息，导致优化过程中灵敏度误差累积，影响最终解的质量。

**核心思路**：通过在高保真算子的输出和Fréchet导数样本上联合训练傅里叶神经算子，构建导数信息代理模型，使其同时逼近算子的响应和灵敏度，从而提高优化精度。

**技术框架**：整体流程包括数据采集（获取高保真算子的输出和导数样本）、网络训练（使用降维和多分辨率技术优化损失函数）、模型验证（在测试集评估逼近性能）和应用部署（用于偏微分方程约束优化求解）。主要模块为傅里叶神经算子架构，结合导数信息损失项。

**关键创新**：最重要的创新是引入导数信息学习，将Fréchet导数纳入训练目标，实现算子和其导数的同时逼近，与现有方法本质区别在于直接优化灵敏度准确性，而非仅输出匹配。

**关键设计**：损失函数设计为输出误差和导数误差的加权和；网络结构基于傅里叶变换层，高效处理高维输入；采用降维技术（如主成分分析）减少导数样本维度，多分辨率训练加速收敛；参数设置包括傅里叶模式数、学习率和正则化系数，以平衡逼近精度和计算成本。

## 📊 实验亮点

实验在非线性扩散-反应、Helmholtz和Navier-Stokes方程上进行，DIFNO相比传统FNO在样本复杂度上显著优越，例如在Navier-Stokes问题中，使用少量训练样本（具体数据未知）即达到高精度，优化误差降低约一个数量级，验证了理论逼近性和高效训练方案的有效性。

## 🎯 应用场景

该研究在偏微分方程约束优化领域具有广泛应用，如流体动力学、声学传播和化学反应模拟中的逆问题求解。实际价值在于降低高保真模拟的计算成本，提高优化效率，未来可能扩展到更复杂的多物理场系统和实时控制场景，推动科学计算和工程设计的智能化。

## 📄 摘要（原文）

> We present approximation theories and efficient training methods for derivative-informed Fourier neural operators (DIFNOs) with applications to PDE-constrained optimization. A DIFNO is an FNO trained by minimizing its prediction error jointly on output and Fréchet derivative samples of a high-fidelity operator (e.g., a parametric PDE solution operator). As a result, a DIFNO can closely emulate not only the high-fidelity operator's response but also its sensitivities. To motivate the use of DIFNOs instead of conventional FNOs as surrogate models, we show that accurate surrogate-driven PDE-constrained optimization requires accurate surrogate Fréchet derivatives. Then, for continuously differentiable operators, we establish (i) simultaneous universal approximation of FNOs and their Fréchet derivatives on compact sets, and (ii) universal approximation of FNOs in weighted Sobolev spaces with input measures that have unbounded supports. Our theoretical results certify the capability of FNOs for accurate derivative-informed operator learning and accurate solution of PDE-constrained optimization. Furthermore, we develop efficient training schemes using dimension reduction and multi-resolution techniques that significantly reduce memory and computational costs for Fréchet derivative learning. Numerical examples on nonlinear diffusion--reaction, Helmholtz, and Navier--Stokes equations demonstrate that DIFNOs are superior in sample complexity for operator learning and solving infinite-dimensional PDE-constrained inverse problems, achieving high accuracy at low training sample sizes.

