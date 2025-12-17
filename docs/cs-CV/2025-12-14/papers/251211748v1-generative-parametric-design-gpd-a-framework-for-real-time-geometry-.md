---
layout: default
title: Generative Parametric Design (GPD): A framework for real-time geometry generation and on-the-fly multiparametric approximation
---

# Generative Parametric Design (GPD): A framework for real-time geometry generation and on-the-fly multiparametric approximation

**arXiv**: [2512.11748v1](https://arxiv.org/abs/2512.11748) | [PDF](https://arxiv.org/pdf/2512.11748.pdf)

**作者**: Mohammed El Fallaki Idrissi, Jad Mounayer, Sebastian Rodriguez, Fodil Meraghni, Francisco Chinesta

---

## 💡 一句话要点

**提出生成参数化设计框架，通过双自编码器实现实时几何生成与多参数近似。**

**关键词**: `生成参数化设计` `秩降自编码器` `稀疏PGD` `实时几何生成` `多参数近似` `数字孪生`

## 📋 核心要点

1. 核心问题：仿真工程中设计生成与参数化解决方案的高效关联问题。
2. 方法要点：使用两个秩降自编码器分别编码几何和稀疏PGD模式，通过潜空间回归链接。
3. 实验或效果：在两相微结构上演示，支持材料参数变化的多参数解。

## 📄 摘要（原文）

> This paper presents a novel paradigm in simulation-based engineering sciences by introducing a new framework called Generative Parametric Design (GPD). The GPD framework enables the generation of new designs along with their corresponding parametric solutions given as a reduced basis. To achieve this, two Rank Reduction Autoencoders (RRAEs) are employed, one for encoding and generating the design or geometry, and the other for encoding the sparse Proper Generalized Decomposition (sPGD) mode solutions. These models are linked in the latent space using regression techniques, allowing efficient transitions between design and their associated sPGD modes. By empowering design exploration and optimization, this framework also advances digital and hybrid twin development, enhancing predictive modeling and real-time decision-making in engineering applications. The developed framework is demonstrated on two-phase microstructures, in which the multiparametric solutions account for variations in two key material parameters.

