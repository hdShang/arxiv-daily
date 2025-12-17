---
layout: default
title: Solving Heterogeneous Agent Models with Physics-informed Neural Networks
---

# Solving Heterogeneous Agent Models with Physics-informed Neural Networks

**arXiv**: [2511.20283v1](https://arxiv.org/abs/2511.20283) | [PDF](https://arxiv.org/pdf/2511.20283.pdf)

**作者**: Marta Grzeskiewicz

---

## 💡 一句话要点

**提出ABH-PINN求解器以解决异质代理模型的计算挑战**

**关键词**: `异质代理模型` `物理信息神经网络` `偏微分方程求解` `计算经济学` `无网格方法`

## 📋 核心要点

1. 异质代理模型在连续时间下计算复杂，传统网格求解器存在维数灾难和高成本问题
2. 基于物理信息神经网络，将HJB和Kolmogorov方程嵌入训练目标，实现无网格学习
3. 初步结果显示，PINN方法可获经济有效结果，与有限差分求解器匹配

## 📄 摘要（原文）

> Understanding household behaviour is essential for modelling macroeconomic dynamics and designing effective policy. While heterogeneous agent models offer a more realistic alternative to representative agent frameworks, their implementation poses significant computational challenges, particularly in continuous time. The Aiyagari-Bewley-Huggett (ABH) framework, recast as a system of partial differential equations, typically relies on grid-based solvers that suffer from the curse of dimensionality, high computational cost, and numerical inaccuracies. This paper introduces the ABH-PINN solver, an approach based on Physics-Informed Neural Networks (PINNs), which embeds the Hamilton-Jacobi-Bellman and Kolmogorov Forward equations directly into the neural network training objective. By replacing grid-based approximation with mesh-free, differentiable function learning, the ABH-PINN solver benefits from the advantages of PINNs of improved scalability, smoother solutions, and computational efficiency. Preliminary results show that the PINN-based approach is able to obtain economically valid results matching the established finite-difference solvers.

