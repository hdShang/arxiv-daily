---
layout: default
title: Physics-Aware Heterogeneous GNN Architecture for Real-Time BESS Optimization in Unbalanced Distribution Systems
---

# Physics-Aware Heterogeneous GNN Architecture for Real-Time BESS Optimization in Unbalanced Distribution Systems

**arXiv**: [2512.09780v1](https://arxiv.org/abs/2512.09780) | [PDF](https://arxiv.org/pdf/2512.09780.pdf)

**作者**: Aoxiang Ma, Salah Ghamizi, Jun Cao, Pedro Rodriguez

---

## 💡 一句话要点

**提出基于物理感知的异构图神经网络架构，用于三相不平衡配电网中电池储能系统的实时优化调度。**

**关键词**: `电池储能系统` `三相不平衡配电网` `异构图神经网络` `物理约束优化` `实时调度`

## 📋 核心要点

1. 现有深度学习方法缺乏明确的三相表示，难以准确建模相态动态和满足运行约束。
2. 通过将三相电网信息嵌入异构图节点，结合多种GNN架构和物理约束损失函数进行预测。
3. 在CIGRE 18节点系统上验证，实现低预测误差和近乎零的电池约束违反。

## 📄 摘要（原文）

> Battery energy storage systems (BESS) have become increasingly vital in three-phase unbalanced distribution grids for maintaining voltage stability and enabling optimal dispatch. However, existing deep learning approaches often lack explicit three-phase representation, making it difficult to accurately model phase-specific dynamics and enforce operational constraints--leading to infeasible dispatch solutions. This paper demonstrates that by embedding detailed three-phase grid information--including phase voltages, unbalanced loads, and BESS states--into heterogeneous graph nodes, diverse GNN architectures (GCN, GAT, GraphSAGE, GPS) can jointly predict network state variables with high accuracy. Moreover, a physics-informed loss function incorporates critical battery constraints--SoC and C-rate limits--via soft penalties during training. Experimental validation on the CIGRE 18-bus distribution system shows that this embedding-loss approach achieves low prediction errors, with bus voltage MSEs of 6.92e-07 (GCN), 1.21e-06 (GAT), 3.29e-05 (GPS), and 9.04e-07 (SAGE). Importantly, the physics-informed method ensures nearly zero SoC and C-rate constraint violations, confirming its effectiveness for reliable, constraint-compliant dispatch.

