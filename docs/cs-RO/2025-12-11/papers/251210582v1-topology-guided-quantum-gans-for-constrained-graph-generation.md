---
layout: default
title: Topology-Guided Quantum GANs for Constrained Graph Generation
---

# Topology-Guided Quantum GANs for Constrained Graph Generation

**arXiv**: [2512.10582v1](https://arxiv.org/abs/2512.10582) | [PDF](https://arxiv.org/pdf/2512.10582.pdf)

**作者**: Tobias Rohe, Markus Baumann, Michael Poppel, Gerhard Stenzel, Maximilian Zorn, Claudia Linnhoff-Popien

---

## 💡 一句话要点

**提出拓扑引导的量子生成对抗网络，用于生成几何约束的K4图**

**关键词**: `量子生成对抗网络` `电路拓扑设计` `几何约束图生成` `归纳偏置` `纠缠拓扑` `损失函数优化`

## 📋 核心要点

1. 量子计算文献缺乏针对特定领域的电路拓扑设计，依赖通用架构可能限制性能
2. 通过将几何先验作为归纳偏置融入量子电路设计，提升量子生成对抗网络在约束图生成任务中的表现
3. 评估多种纠缠拓扑和损失函数，结果显示对齐拓扑与问题结构能显著提高几何有效性和统计保真度

## 📄 摘要（原文）

> Quantum computing (QC) promises theoretical advantages, benefiting computational problems that would not be efficiently classically simulatable. However, much of this theoretical speedup depends on the quantum circuit design solving the problem. We argue that QC literature has yet to explore more domain specific ansatz-topologies, instead of relying on generic, one-size-fits-all architectures. In this work, we show that incorporating task-specific inductive biases -- specifically geometric priors -- into quantum circuit design can enhance the performance of hybrid Quantum Generative Adversarial Networks (QuGANs) on the task of generating geometrically constrained K4 graphs. We evaluate a portfolio of entanglement topologies and loss-function designs to assess their impact on both statistical fidelity and compliance with geometric constraints, including the Triangle and Ptolemaic inequalities. Our results show that aligning circuit topology with the underlying problem structure yields substantial benefits: the Triangle-topology QuGAN achieves the highest geometric validity among quantum models and matches the performance of classical Generative Adversarial Networks (GAN). Additionally, we showcase how specific architectural choices, such as entangling gate types, variance regularization and output-scaling govern the trade-off between geometric consistency and distributional accuracy, thus emphasizing the value of structured, task-aware quantum ansatz-topologies.

