---
layout: default
title: Decoupled Design of Time-Varying Control Barrier Functions via Equivariances
---

# Decoupled Design of Time-Varying Control Barrier Functions via Equivariances

**arXiv**: [2512.08607v1](https://arxiv.org/abs/2512.08607) | [PDF](https://arxiv.org/pdf/2512.08607.pdf)

**作者**: Adrian Wiltz, Dimos V. Dimarogonas

---

## 💡 一句话要点

**提出基于等变性的时变控制屏障函数解耦设计方法，以处理不确定环境中的时变约束。**

**关键词**: `控制屏障函数` `时变约束` `等变性` `解耦设计` `不确定环境`

## 📋 核心要点

1. 核心问题：传统时变控制屏障函数设计计算成本高，难以处理动态系统中的时变约束。
2. 方法要点：利用系统动力学结构（如等变性），将时变部分与时不变部分解耦设计，降低计算复杂度。
3. 实验或效果：方法能处理输入约束和欠驱动系统，仅需约束时变的定性知识，适用于不确定环境。

## 📄 摘要（原文）

> This article presents a systematic method for designing time-varying Control Barrier Functions (CBF) composed of a time-invariant component and multiple time-dependent components, leveraging structural properties of the system dynamics. The method involves the construction of a specific class of time-invariant CBFs that encode the system's dynamic capabilities with respect to a given constraint, and augments them subsequently with appropriately designed time-dependent transformations. While transformations uniformly varying the time-invariant CBF can be applied to arbitrary systems, transformations exploiting structural properties in the dynamics - equivariances in particular - enable the handling of a broader and more expressive class of time-varying constraints. The article shows how to leverage such properties in the design of time-varying CBFs. The proposed method decouples the design of time variations from the computationally expensive construction of the underlying CBFs, thereby providing a computationally attractive method to the design of time-varying CBFs. The method accounts for input constraints and under-actuation, and requires only qualitative knowledge on the time-variation of the constraints making it suitable to the application in uncertain environments.

