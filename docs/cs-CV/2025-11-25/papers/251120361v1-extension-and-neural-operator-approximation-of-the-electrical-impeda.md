---
layout: default
title: Extension and neural operator approximation of the electrical impedance tomography inverse map
---

# Extension and neural operator approximation of the electrical impedance tomography inverse map

**arXiv**: [2511.20361v1](https://arxiv.org/abs/2511.20361) | [PDF](https://arxiv.org/pdf/2511.20361.pdf)

**作者**: Maarten V. de Hoop, Nikola B. Kovachki, Matti Lassas, Nicholas H. Nelsen

---

## 💡 一句话要点

**提出噪声鲁棒神经算子方法以解决电导率成像逆问题**

**关键词**: `电导率成像逆问题` `神经算子近似` `噪声鲁棒性` `Fourier神经算子` `无限维重建`

## 📋 核心要点

1. 核心问题：Calderón逆电导率问题中边界测量的噪声鲁棒求解
2. 方法要点：扩展逆算子域至核函数空间，实现神经算子近似
3. 实验或效果：Fourier神经算子有效重建无限维电导率，噪声下表现优异

## 📄 摘要（原文）

> This paper considers the problem of noise-robust neural operator approximation for the solution map of Calderón's inverse conductivity problem. In this continuum model of electrical impedance tomography (EIT), the boundary measurements are realized as a noisy perturbation of the Neumann-to-Dirichlet map's integral kernel. The theoretical analysis proceeds by extending the domain of the inversion operator to a Hilbert space of kernel functions. The resulting extension shares the same stability properties as the original inverse map from kernels to conductivities, but is now amenable to neural operator approximation. Numerical experiments demonstrate that Fourier neural operators excel at reconstructing infinite-dimensional piecewise constant and lognormal conductivities in noisy setups both within and beyond the theory's assumptions. The methodology developed in this paper for EIT exemplifies a broader strategy for addressing nonlinear inverse problems with a noise-aware operator learning framework.

