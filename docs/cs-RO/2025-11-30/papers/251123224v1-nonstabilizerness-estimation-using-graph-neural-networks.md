---
layout: default
title: Nonstabilizerness Estimation using Graph Neural Networks
---

# Nonstabilizerness Estimation using Graph Neural Networks

**arXiv**: [2511.23224v1](https://arxiv.org/abs/2511.23224) | [PDF](https://arxiv.org/pdf/2511.23224.pdf)

**作者**: Vincenzo Lipardi, Domenica Dibenedetto, Georgios Stamoulis, Evert van Nieuwenburg, Mark H. M. Winands

---

## 💡 一句话要点

**提出图神经网络方法以估计量子电路中的非稳定子性，提升稳定子Rényi熵的评估效率。**

**关键词**: `量子计算` `图神经网络` `非稳定子性估计` `稳定子Rényi熵` `量子电路` `监督学习`

## 📋 核心要点

1. 核心问题：非稳定子性是量子优势的关键资源，其高效估计在应用中至关重要。
2. 方法要点：基于图表示，通过分类到回归的监督学习框架，捕获电路特征。
3. 实验效果：在分类和回归任务中，模型在多种场景下展现出鲁棒的泛化性能。

## 📄 摘要（原文）

> This article proposes a Graph Neural Network (GNN) approach to estimate nonstabilizerness in quantum circuits, measured by the stabilizer Rényi entropy (SRE). Nonstabilizerness is a fundamental resource for quantum advantage, and efficient SRE estimations are highly beneficial in practical applications. We address the nonstabilizerness estimation problem through three supervised learning formulations starting from easier classification tasks to the more challenging regression task. Experimental results show that the proposed GNN manages to capture meaningful features from the graph-based circuit representation, resulting in robust generalization performances achieved across diverse scenarios. In classification tasks, the GNN is trained on product states and generalizes on circuits evolved under Clifford operations, entangled states, and circuits with higher number of qubits. In the regression task, the GNN significantly improves the SRE estimation on out-of-distribution circuits with higher number of qubits and gate counts compared to previous work, for both random quantum circuits and structured circuits derived from the transverse-field Ising model. Moreover, the graph representation of quantum circuits naturally integrates hardware-specific information. Simulations on noisy quantum hardware highlight the potential of the proposed GNN to predict the SRE measured on quantum devices.

