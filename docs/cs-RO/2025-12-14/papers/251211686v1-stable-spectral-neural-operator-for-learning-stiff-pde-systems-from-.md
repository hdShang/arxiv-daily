---
layout: default
title: Stable spectral neural operator for learning stiff PDE systems from limited data
---

# Stable spectral neural operator for learning stiff PDE systems from limited data

**arXiv**: [2512.11686v1](https://arxiv.org/abs/2512.11686) | [PDF](https://arxiv.org/pdf/2512.11686.pdf)

**作者**: Rui Zhang, Han Wan, Yang Liu, Hao Sun

---

## 💡 一句话要点

**提出稳定谱神经算子以从有限数据学习刚性偏微分方程系统**

**关键词**: `谱神经算子` `刚性偏微分方程` `有限数据学习` `时空动力学建模` `积分因子时间步进`

## 📋 核心要点

1. 核心问题：未知方程和稀疏数据下，系统刚性阻碍时空动力学建模。
2. 方法要点：嵌入谱结构，在频域学习空间交互，采用积分因子时间步进处理刚性。
3. 实验或效果：在2D/3D基准测试中，预测误差降低1-2个数量级，仅需2-5条轨迹实现泛化。

## 📄 摘要（原文）

> Accurate modeling of spatiotemporal dynamics is crucial to understanding complex phenomena across science and engineering. However, this task faces a fundamental challenge when the governing equations are unknown and observational data are sparse. System stiffness, the coupling of multiple time-scales, further exacerbates this problem and hinders long-term prediction. Existing methods fall short: purely data-driven methods demand massive datasets, whereas physics-aware approaches are constrained by their reliance on known equations and fine-grained time steps. To overcome these limitations, we introduce an equation-free learning framework, namely, the Stable Spectral Neural Operator (SSNO), for modeling stiff partial differential equation (PDE) systems based on limited data. Instead of encoding specific equation terms, SSNO embeds spectrally inspired structures in its architecture, yielding strong inductive biases for learning the underlying physics. It automatically learns local and global spatial interactions in the frequency domain, while handling system stiffness with a robust integrating factor time-stepping scheme. Demonstrated across multiple 2D and 3D benchmarks in Cartesian and spherical geometries, SSNO achieves prediction errors one to two orders of magnitude lower than leading models. Crucially, it shows remarkable data efficiency, requiring only very few (2--5) training trajectories for robust generalization to out-of-distribution conditions. This work offers a robust and generalizable approach to learning stiff spatiotemporal dynamics from limited data without explicit \textit{a priori} knowledge of PDE terms.

