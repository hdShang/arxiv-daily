---
layout: default
title: Tracking large chemical reaction networks and rare events by neural networks
---

# Tracking large chemical reaction networks and rare events by neural networks

**arXiv**: [2512.10309v1](https://arxiv.org/abs/2512.10309) | [PDF](https://arxiv.org/pdf/2512.10309.pdf)

**作者**: Jiayu Weng, Xinyi Zhu, Jing Liu, Linyuan Lü, Pan Zhang, Ying Tang

---

## 💡 一句话要点

**提出基于神经网络的优化方法，以高效求解大规模化学反应网络和稀有事件问题。**

**关键词**: `化学反应网络` `神经网络优化` `稀有事件采样` `化学主方程求解` `反应-扩散系统`

## 📋 核心要点

1. 核心问题：化学反应网络的状态空间随系统规模指数增长，求解化学主方程计算成本高，尤其在稀有事件场景下。
2. 方法要点：利用自然梯度下降和时间依赖变分原理加速优化，结合增强采样策略捕捉稀有事件，提升神经网络方法效率。
3. 实验或效果：在MAPK级联网络等挑战性系统中，计算成本降低、精度提高，并扩展至二维反应-扩散系统，超越现有方法。

## 📄 摘要（原文）

> Chemical reaction networks are widely used to model stochastic dynamics in chemical kinetics, systems biology and epidemiology. Solving the chemical master equation that governs these systems poses a significant challenge due to the large state space exponentially growing with system sizes. The development of autoregressive neural networks offers a flexible framework for this problem; however, its efficiency is limited especially for high-dimensional systems and in scenarios with rare events. Here, we push the frontier of neural-network approach by exploiting faster optimizations such as natural gradient descent and time-dependent variational principle, achieving a 5- to 22-fold speedup, and by leveraging enhanced-sampling strategies to capture rare events. We demonstrate reduced computational cost and higher accuracy over the previous neural-network method in challenging reaction networks, including the mitogen-activated protein kinase (MAPK) cascade network, the hitherto largest biological network handled by the previous approaches of solving the chemical master equation. We further apply the approach to spatially extended reaction-diffusion systems, the Schlögl model with rare events, on two-dimensional lattices, beyond the recent tensor-network approach that handles one-dimensional lattices. The present approach thus enables efficient modeling of chemical reaction networks in general.

