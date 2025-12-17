---
layout: default
title: Residual subspace evolution strategies for nonlinear inverse problems
---

# Residual subspace evolution strategies for nonlinear inverse problems

**arXiv**: [2512.10325v1](https://arxiv.org/abs/2512.10325) | [PDF](https://arxiv.org/pdf/2512.10325.pdf)

**作者**: Francesco Alemanno

---

## 💡 一句话要点

**提出残差子空间进化策略以解决非线性逆问题中噪声、不可微或昂贵残差评估的挑战。**

**关键词**: `非线性逆问题` `无导数优化` `进化策略` `残差代理` `最小二乘求解` `计算效率`

## 📋 核心要点

1. 核心问题：非线性逆问题常涉及噪声、不可微或计算昂贵的残差评估，导致基于雅可比矩阵的求解器不可靠。
2. 方法要点：RSES通过采样高斯探针构建残差代理，利用最小二乘求解更新，避免雅可比矩阵或协方差计算，每次迭代成本低。
3. 实验或效果：在标定、回归和去卷积问题中，RSES在确定性和随机设置下均能持续降低失配，性能优于或匹配xNES和NEWUOA，与EKI竞争。

## 📄 摘要（原文）

> Nonlinear inverse problems often feature noisy, non-differentiable, or expensive residual evaluations that make Jacobian-based solvers unreliable. Popular derivative-free optimizers such as natural evolution strategies (NES) or Powell's NEWUOA still assume smoothness or expend many evaluations to maintain stability. Ensemble Kalman inversion (EKI) relies on empirical covariances that require preconditioning and scale poorly with residual dimension.
>   We introduce residual subspace evolution strategies (RSES), a derivative-free solver that samples Gaussian probes around the current iterate, builds a residual-only surrogate from their differences, and recombines the probes through a least-squares solve yielding an optimal update without forming Jacobians or covariances. Each iteration costs $k+1$ residual evaluations, where $k \ll n$ for $n$-dimensional problems, with $O(k^3)$ linear algebra overhead.
>   Benchmarks on calibration, regression, and deconvolution problems demonstrate consistent misfit reduction in both deterministic and stochastic settings. RSES matches or surpasses xNES and NEWUOA while staying competitive with EKI under matched evaluation budgets, particularly when smoothness or covariance assumptions fail.

