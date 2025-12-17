---
layout: default
title: KD-PINN: Knowledge-Distilled PINNs for ultra-low-latency real-time neural PDE solvers
---

# KD-PINN: Knowledge-Distilled PINNs for ultra-low-latency real-time neural PDE solvers

**arXiv**: [2512.13336v1](https://arxiv.org/abs/2512.13336) | [PDF](https://arxiv.org/pdf/2512.13336.pdf)

**作者**: Karim Bounja, Lahcen Laayouni, Abdeljalil Sakat

---

## 💡 一句话要点

**提出知识蒸馏物理信息神经网络框架，用于实现超低延迟实时神经偏微分方程求解器。**

**关键词**: `知识蒸馏` `物理信息神经网络` `偏微分方程求解` `超低延迟` `实时计算` `模型压缩`

## 📋 核心要点

1. 核心问题：物理信息神经网络推理延迟高，难以满足实时求解需求。
2. 方法要点：通过连续适应KL散度，将高容量教师模型预测精度迁移至紧凑学生模型。
3. 实验或效果：在多种偏微分方程上验证，学生模型保持物理精度，推理速度提升4.8-6.9倍，平均延迟5.3毫秒。

## 📄 摘要（原文）

> This work introduces Knowledge-Distilled Physics-Informed Neural Networks (KD-PINN), a framework that transfers the predictive accuracy of a high-capacity teacher model to a compact student through a continuous adaptation of the Kullback-Leibler divergence. To confirm its generality for various dynamics and dimensionalities, the framework is evaluated on a representative set of partial differential equations (PDEs). In all tested cases, the student model preserved the teacher's physical accuracy, with a mean RMSE increase below 0.64%, and achieved inference speedups ranging from 4.8x (Navier-Stokes) to 6.9x (Burgers). The distillation process also revealed a regularizing effect. With an average inference latency of 5.3 ms on CPU, the distilled models enter the ultra-low-latency real-time regime defined by sub-10 ms performance. Finally, this study examines how knowledge distillation reduces inference latency in PINNs to contribute to the development of accurate ultra-low-latency neural PDE solvers.

