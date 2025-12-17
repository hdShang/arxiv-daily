---
layout: default
title: Prismatic World Model: Learning Compositional Dynamics for Planning in Hybrid Systems
---

# Prismatic World Model: Learning Compositional Dynamics for Planning in Hybrid Systems

**arXiv**: [2512.08411v1](https://arxiv.org/abs/2512.08411) | [PDF](https://arxiv.org/pdf/2512.08411.pdf)

**作者**: Mingwei Li, Xiaoyuan Zhang, Chengwei Yang, Zilong Zheng, Yaodong Yang

---

## 💡 一句话要点

**提出棱镜世界模型以解决混合系统中基于模型的规划问题**

**关键词**: `混合系统` `世界模型` `专家混合` `轨迹优化` `模型规划`

## 📋 核心要点

1. 核心问题：混合动态（连续运动与离散事件）导致传统世界模型过度平滑，规划时产生累积误差。
2. 方法要点：采用上下文感知的专家混合框架，分解动态为可组合基元，引入潜在正交化目标防止模式崩溃。
3. 实验或效果：在连续控制基准测试中显著减少滚动漂移，提升轨迹优化算法性能。

## 📄 摘要（原文）

> Model-based planning in robotic domains is fundamentally challenged by the hybrid nature of physical dynamics, where continuous motion is punctuated by discrete events such as contacts and impacts. Conventional latent world models typically employ monolithic neural networks that enforce global continuity, inevitably over-smoothing the distinct dynamic modes (e.g., sticking vs. sliding, flight vs. stance). For a planner, this smoothing results in catastrophic compounding errors during long-horizon lookaheads, rendering the search process unreliable at physical boundaries. To address this, we introduce the Prismatic World Model (PRISM-WM), a structured architecture designed to decompose complex hybrid dynamics into composable primitives. PRISM-WM leverages a context-aware Mixture-of-Experts (MoE) framework where a gating mechanism implicitly identifies the current physical mode, and specialized experts predict the associated transition dynamics. We further introduce a latent orthogonalization objective to ensure expert diversity, effectively preventing mode collapse. By accurately modeling the sharp mode transitions in system dynamics, PRISM-WM significantly reduces rollout drift. Extensive experiments on challenging continuous control benchmarks, including high-dimensional humanoids and diverse multi-task settings, demonstrate that PRISM-WM provides a superior high-fidelity substrate for trajectory optimization algorithms (e.g., TD-MPC), proving its potential as a powerful foundational model for next-generation model-based agents.

