---
layout: default
title: Operator Learning at Machine Precision
---

# Operator Learning at Machine Precision

**arXiv**: [2511.19980v1](https://arxiv.org/abs/2511.19980) | [PDF](https://arxiv.org/pdf/2511.19980.pdf)

**作者**: Aras Bacho, Aleksei G. Sorokin, Xianjin Yang, Théo Bourdais, Edoardo Calvello, Matthieu Darcy, Alexander Hsu, Bamdad Hosseini, Houman Owhadi

---

## 💡 一句话要点

**提出CHONKNORIS方法，在非线性PDE问题中实现机器精度求解**

**关键词**: `神经算子学习` `非线性偏微分方程` `机器精度求解` `牛顿-康托罗维奇方法` `Cholesky因子回归` `基础模型`

## 📋 核心要点

1. 神经算子方法复杂度增加时精度提升有限，与简单方法相当
2. 通过回归Cholesky因子构建收缩映射，降低对算子近似精度要求
3. 在多种非线性正反问题中验证机器精度，并引入基础模型FONKNORIS

## 📄 摘要（原文）

> Neural operator learning methods have garnered significant attention in scientific computing for their ability to approximate infinite-dimensional operators. However, increasing their complexity often fails to substantially improve their accuracy, leaving them on par with much simpler approaches such as kernel methods and more traditional reduced-order models. In this article, we set out to address this shortcoming and introduce CHONKNORIS (Cholesky Newton--Kantorovich Neural Operator Residual Iterative System), an operator learning paradigm that can achieve machine precision. CHONKNORIS draws on numerical analysis: many nonlinear forward and inverse PDE problems are solvable by Newton-type methods. Rather than regressing the solution operator itself, our method regresses the Cholesky factors of the elliptic operator associated with Tikhonov-regularized Newton--Kantorovich updates. The resulting unrolled iteration yields a neural architecture whose machine-precision behavior follows from achieving a contractive map, requiring far lower accuracy than end-to-end approximation of the solution operator. We benchmark CHONKNORIS on a range of nonlinear forward and inverse problems, including a nonlinear elliptic equation, Burgers' equation, a nonlinear Darcy flow problem, the Calderón problem, an inverse wave scattering problem, and a problem from seismic imaging. We also present theoretical guarantees for the convergence of CHONKNORIS in terms of the accuracy of the emulated Cholesky factors. Additionally, we introduce a foundation model variant, FONKNORIS (Foundation Newton--Kantorovich Neural Operator Residual Iterative System), which aggregates multiple pre-trained CHONKNORIS experts for diverse PDEs to emulate the solution map of a novel nonlinear PDE. Our FONKNORIS model is able to accurately solve unseen nonlinear PDEs such as the Klein--Gordon and Sine--Gordon equations.

