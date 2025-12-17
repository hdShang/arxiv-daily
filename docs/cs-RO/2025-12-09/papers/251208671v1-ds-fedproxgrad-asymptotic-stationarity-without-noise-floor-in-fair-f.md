---
layout: default
title: DS FedProxGrad: Asymptotic Stationarity Without Noise Floor in Fair Federated Learning
---

# DS FedProxGrad: Asymptotic Stationarity Without Noise Floor in Fair Federated Learning

**arXiv**: [2512.08671v1](https://arxiv.org/abs/2512.08671) | [PDF](https://arxiv.org/pdf/2512.08671.pdf)

**作者**: Huzaifa Arif

---

## 💡 一句话要点

**提出DS FedProxGrad以在公平联邦学习中实现无噪声底限的渐近平稳性**

**关键词**: `公平联邦学习` `非凸优化` `渐近收敛` `衰减步长` `近端梯度方法`

## 📋 核心要点

1. 原FedProxGrad在公平联邦学习中收敛至噪声主导邻域，存在方差诱导的噪声底限问题
2. 扩展为DS FedProxGrad框架，结合衰减步长和不精确局部解，证明渐近平稳性
3. 在Robbins-Monro步长调度下，实现梯度范数平方期望的极限为零，消除噪声底限依赖

## 📄 摘要（原文）

> Recent work \cite{arifgroup} introduced Federated Proximal Gradient \textbf{(\texttt{FedProxGrad})} for solving non-convex composite optimization problems in group fair federated learning. However, the original analysis established convergence only to a \textit{noise-dominated neighborhood of stationarity}, with explicit dependence on a variance-induced noise floor. In this work, we provide an improved asymptotic convergence analysis for a generalized \texttt{FedProxGrad}-type analytical framework with inexact local proximal solutions and explicit fairness regularization. We call this extended analytical framework \textbf{DS \texttt{FedProxGrad}} (Decay Step Size \texttt{FedProxGrad}). Under a Robbins-Monro step-size schedule \cite{robbins1951stochastic} and a mild decay condition on local inexactness, we prove that $\liminf_{r\to\infty} \mathbb{E}[\\|\nabla F(\mathbf{x}^r)\\|^2] = 0$, i.e., the algorithm is asymptotically stationary and the convergence rate does not depend on a variance-induced noise floor.

