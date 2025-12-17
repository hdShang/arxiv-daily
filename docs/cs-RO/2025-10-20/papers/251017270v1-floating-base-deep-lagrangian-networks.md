---
layout: default
title: Floating-Base Deep Lagrangian Networks
---

# Floating-Base Deep Lagrangian Networks

**arXiv**: [2510.17270v1](https://arxiv.org/abs/2510.17270) | [PDF](https://arxiv.org/pdf/2510.17270.pdf)

**作者**: Lucas Schulze, Juliano Decico Negri, Victor Barasuol, Vivian Suzano Medeiros, Marcelo Becker, Jan Peters, Oleg Arenz

---

## 💡 一句话要点

**提出FeLaN以解决浮动基系统物理约束缺失问题**

**关键词**: `浮动基系统` `灰盒方法` `惯性矩阵参数化` `拉格朗日力学` `系统辨识` `物理约束`

## 📋 核心要点

1. 核心问题：浮动基系统如人形和四足机器人缺乏物理一致的深度学习模型
2. 方法要点：基于Deep Lagrangian Networks，参数化满足约束的惯性矩阵
3. 实验或效果：在模拟和真实机器人上实现高性能和物理可解释性

## 📄 摘要（原文）

> Grey-box methods for system identification combine deep learning with
> physics-informed constraints, capturing complex dependencies while improving
> out-of-distribution generalization. Yet, despite the growing importance of
> floating-base systems such as humanoids and quadrupeds, current grey-box models
> ignore their specific physical constraints. For instance, the inertia matrix is
> not only positive definite but also exhibits branch-induced sparsity and input
> independence. Moreover, the 6x6 composite spatial inertia of the floating base
> inherits properties of single-rigid-body inertia matrices. As we show, this
> includes the triangle inequality on the eigenvalues of the composite rotational
> inertia. To address the lack of physical consistency in deep learning models of
> floating-base systems, we introduce a parameterization of inertia matrices that
> satisfies all these constraints. Inspired by Deep Lagrangian Networks (DeLaN),
> we train neural networks to predict physically plausible inertia matrices that
> minimize inverse dynamics error under Lagrangian mechanics. For evaluation, we
> collected and released a dataset on multiple quadrupeds and humanoids. In these
> experiments, our Floating-Base Deep Lagrangian Networks (FeLaN) achieve highly
> competitive performance on both simulated and real robots, while providing
> greater physical interpretability.

