---
layout: default
title: Hard-Constrained Neural Networks with Physics-Embedded Architecture for Residual Dynamics Learning and Invariant Enforcement in Cyber-Physical Systems
---

# Hard-Constrained Neural Networks with Physics-Embedded Architecture for Residual Dynamics Learning and Invariant Enforcement in Cyber-Physical Systems

**arXiv**: [2511.23307v1](https://arxiv.org/abs/2511.23307) | [PDF](https://arxiv.org/pdf/2511.23307.pdf)

**作者**: Enzo Nicolás Spotorno, Josafat Leal Filho, Antônio Augusto Fröhlich

---

## 💡 一句话要点

**提出硬约束神经网络框架，通过物理嵌入架构学习残差动力学并强制代数不变量，应用于复杂网络物理系统。**

**关键词**: `物理信息学习` `残差动力学学习` `代数不变量强制` `网络物理系统` `硬约束神经网络` `预测-投影机制`

## 📋 核心要点

1. 针对微分方程中未知动力学和代数不变量问题，提出HRPINN嵌入已知物理作为硬约束。
2. 扩展PHRPINN引入预测-投影机制，设计上严格强制代数不变量。
3. 在电池预测和标准基准测试中验证高精度和数据效率，分析物理一致性、计算成本和数值稳定性权衡。

## 📄 摘要（原文）

> This paper presents a framework for physics-informed learning in complex cyber-physical systems governed by differential equations with both unknown dynamics and algebraic invariants. First, we formalize the Hybrid Recurrent Physics-Informed Neural Network (HRPINN), a general-purpose architecture that embeds known physics as a hard structural constraint within a recurrent integrator to learn only residual dynamics. Second, we introduce the Projected HRPINN (PHRPINN), a novel extension that integrates a predict-project mechanism to strictly enforce algebraic invariants by design. The framework is supported by a theoretical analysis of its representational capacity. We validate HRPINN on a real-world battery prognostics DAE and evaluate PHRPINN on a suite of standard constrained benchmarks. The results demonstrate the framework's potential for achieving high accuracy and data efficiency, while also highlighting critical trade-offs between physical consistency, computational cost, and numerical stability, providing practical guidance for its deployment.

