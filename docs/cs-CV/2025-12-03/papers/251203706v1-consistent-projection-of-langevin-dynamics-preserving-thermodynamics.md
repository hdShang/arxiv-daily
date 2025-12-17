---
layout: default
title: Consistent Projection of Langevin Dynamics: Preserving Thermodynamics and Kinetics in Coarse-Grained Models
---

# Consistent Projection of Langevin Dynamics: Preserving Thermodynamics and Kinetics in Coarse-Grained Models

**arXiv**: [2512.03706v1](https://arxiv.org/abs/2512.03706) | [PDF](https://arxiv.org/pdf/2512.03706.pdf)

**作者**: Vahid Nateghi, Lara Neureither, Selma Moqvist, Carsten Hartmann, Simon Olsson, Feliks Nüske

---

## 💡 一句话要点

**提出基于投影的粗粒化方法，以保持朗之万动力学的热力学和动力学性质。**

**关键词**: `粗粒化建模` `朗之万动力学` `投影方法` `热力学插值` `动力学性质评估`

## 📋 核心要点

1. 核心问题：粗粒化建模中如何准确保持全空间模型的热力学和动力学性质。
2. 方法要点：基于Zwanzig投影推导粗粒化动力学闭式表达式，结合gEDMD方法评估动力学性质。
3. 实验或效果：在二维模型系统中验证方法能准确捕获热力学和动力学性质，并扩展至不同热力学状态。

## 📄 摘要（原文）

> Coarse graining (CG) is an important task for efficient modeling and simulation of complex multi-scale systems, such as the conformational dynamics of biomolecules. This work presents a projection-based coarse-graining formalism for general underdamped Langevin dynamics. Following the Zwanzig projection approach, we derive a closed-form expression for the coarse grained dynamics. In addition, we show how the generator Extended Dynamic Mode Decomposition (gEDMD) method, which was developed in the context of Koopman operator methods, can be used to model the CG dynamics and evaluate its kinetic properties, such as transition timescales. Finally, we combine our approach with thermodynamic interpolation (TI), a generative approach to transform samples between thermodynamic conditions, to extend the scope of the approach across thermodynamic states without repeated numerical simulations. Using a two-dimensional model system, we demonstrate that the proposed method allows to accurately capture the thermodynamic and kinetic properties of the full-space model.

