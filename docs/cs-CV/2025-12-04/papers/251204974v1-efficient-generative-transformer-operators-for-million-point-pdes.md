---
layout: default
title: Efficient Generative Transformer Operators For Million-Point PDEs
---

# Efficient Generative Transformer Operators For Million-Point PDEs

**arXiv**: [2512.04974v1](https://arxiv.org/abs/2512.04974) | [PDF](https://arxiv.org/pdf/2512.04974.pdf)

**作者**: Armand Kassaï Koupaï, Lise Le Boudec, Patrick Gallinari

---

## 💡 一句话要点

**提出ECHO框架以解决百万点PDE轨迹生成中的可扩展性和误差累积问题**

**关键词**: `PDE求解` `生成建模` `时空压缩` `神经算子` `高分辨率生成` `误差控制`

## 📋 核心要点

1. 现有神经算子在密集网格上可扩展性差、动态展开时误差累积，且设计任务特定。
2. 采用分层卷积编码-解码架构实现100倍时空压缩，并引入训练策略支持高分辨率生成和生成建模。
3. 在复杂几何、高频动态和长期视野的PDE系统上展示百万点模拟的先进性能。

## 📄 摘要（原文）

> We introduce ECHO, a transformer-operator framework for generating million-point PDE trajectories. While existing neural operators (NOs) have shown promise for solving partial differential equations, they remain limited in practice due to poor scalability on dense grids, error accumulation during dynamic unrolling, and task-specific design. ECHO addresses these challenges through three key innovations. (i) It employs a hierarchical convolutional encode-decode architecture that achieves a 100 $\times$ spatio-temporal compression while preserving fidelity on mesh points. (ii) It incorporates a training and adaptation strategy that enables high-resolution PDE solution generation from sparse input grids. (iii) It adopts a generative modeling paradigm that learns complete trajectory segments, mitigating long-horizon error drift. The training strategy decouples representation learning from downstream task supervision, allowing the model to tackle multiple tasks such as trajectory generation, forward and inverse problems, and interpolation. The generative model further supports both conditional and unconditional generation. We demonstrate state-of-the-art performance on million-point simulations across diverse PDE systems featuring complex geometries, high-frequency dynamics, and long-term horizons.

