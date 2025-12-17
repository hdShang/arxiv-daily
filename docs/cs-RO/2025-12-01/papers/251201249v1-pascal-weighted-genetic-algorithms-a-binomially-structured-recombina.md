---
layout: default
title: Pascal-Weighted Genetic Algorithms: A Binomially-Structured Recombination Framework
---

# Pascal-Weighted Genetic Algorithms: A Binomially-Structured Recombination Framework

**arXiv**: [2512.01249v1](https://arxiv.org/abs/2512.01249) | [PDF](https://arxiv.org/pdf/2512.01249.pdf)

**作者**: Otman A. Basir

---

## 💡 一句话要点

**提出基于帕斯卡系数的多父代重组算子，以增强遗传算法的收敛性与性能。**

**关键词**: `遗传算法` `多父代重组` `帕斯卡系数` `收敛优化` `性能提升`

## 📋 核心要点

1. 核心问题：传统遗传算法中两父代交叉算子可能引入高方差，影响收敛稳定性。
2. 方法要点：使用帕斯卡系数构建多父代凸组合，强调中心继承并抑制破坏性方差。
3. 实验或效果：在PID调优、滤波器设计等基准测试中，性能提升9-22%，收敛更平滑。

## 📄 摘要（原文）

> This paper introduces a new family of multi-parent recombination operators for Genetic Algorithms (GAs), based on normalized Pascal (binomial) coefficients. Unlike classical two-parent crossover operators, Pascal-Weighted Recombination (PWR) forms offsprings as structured convex combination of multiple parents, using binomially shaped weights that emphasize central inheritance while suppressing disruptive variance. We develop a mathematical framework for PWR, derive variance-transfer properties, and analyze its effect on schema survival. The operator is extended to real-valued, binary/logit, and permutation representations.
>   We evaluate the proposed method on four representative benchmarks: (i) PID controller tuning evaluated using the ITAE metric, (ii) FIR low-pass filter design under magnitude-response constraints, (iii) wireless power-modulation optimization under SINR coupling, and (iv) the Traveling Salesman Problem (TSP). We demonstrate how, across these benchmarks, PWR consistently yields smoother convergence, reduced variance, and achieves 9-22% performance gains over standard recombination operators. The approach is simple, algorithm-agnostic, and readily integrable into diverse GA architectures.

