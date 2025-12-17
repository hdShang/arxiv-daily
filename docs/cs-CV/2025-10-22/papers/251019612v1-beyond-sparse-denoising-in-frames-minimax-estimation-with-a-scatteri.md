---
layout: default
title: Beyond sparse denoising in frames: minimax estimation with a scattering transform
---

# Beyond sparse denoising in frames: minimax estimation with a scattering transform

**arXiv**: [2510.19612v1](https://arxiv.org/abs/2510.19612) | [PDF](https://arxiv.org/pdf/2510.19612.pdf)

**作者**: Nathanaël Cuvelle--Magar, Stéphane Mallat

---

## 💡 一句话要点

**提出基于散射变换的极小极大估计方法，用于卡通图像去噪。**

**关键词**: `散射变换` `极小极大估计` `图像去噪` `几何规律性` `谐波分析`

## 📋 核心要点

1. 核心问题：传统稀疏估计器在帧中无法适应复杂信号规律，如未知Lipschitz指数的卡通图像。
2. 方法要点：通过联合最小化和最大化散射系数子集的ℓ¹范数，捕捉几何规律性。
3. 实验或效果：数值实验显示该方法达到极小极大渐近界，支持数学猜想。

## 📄 摘要（原文）

> A considerable amount of research in harmonic analysis has been devoted to
> non-linear estimators of signals contaminated by additive Gaussian noise. They
> are implemented by thresholding coefficients in a frame, which provide a sparse
> signal representation, or by minimising their $\ell^1$ norm. However, sparse
> estimators in frames are not sufficiently rich to adapt to complex signal
> regularities. For cartoon images whose edges are piecewise $\bf C^\alpha$
> curves, wavelet, curvelet and Xlet frames are suboptimal if the Lipschitz
> exponent $\alpha \leq 2$ is an unknown parameter. Deep convolutional neural
> networks have recently obtained much better numerical results, which reach the
> minimax asymptotic bounds for all $\alpha$. Wavelet scattering coefficients
> have been introduced as simplified convolutional neural network models. They
> are computed by transforming the modulus of wavelet coefficients with a second
> wavelet transform. We introduce a denoising estimator by jointly minimising and
> maximising the $\ell^1$ norms of different subsets of scattering coefficients.
> We prove that these $\ell^1$ norms capture different types of geometric image
> regularity. Numerical experiments show that this denoising estimator reaches
> the minimax asymptotic bound for cartoon images for all Lipschitz exponents
> $\alpha \leq 2$. We state this numerical result as a mathematical conjecture.
> It provides a different harmonic analysis approach to suppress noise from
> signals, and to specify the geometric regularity of functions. It also opens a
> mathematical bridge between harmonic analysis and denoising estimators with
> deep convolutional network.

