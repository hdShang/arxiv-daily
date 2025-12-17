---
layout: default
title: DAE-HardNet: A Physics Constrained Neural Network Enforcing Differential-Algebraic Hard Constraints
---

# DAE-HardNet: A Physics Constrained Neural Network Enforcing Differential-Algebraic Hard Constraints

**arXiv**: [2512.05881v1](https://arxiv.org/abs/2512.05881) | [PDF](https://arxiv.org/pdf/2512.05881.pdf)

**作者**: Rahul Golder, Bimol Nath Roy, M. M. Faruque Hasan

---

## 💡 一句话要点

**提出DAE-HardNet以严格满足微分代数约束，提升物理约束神经网络性能**

**关键词**: `物理约束神经网络` `微分代数方程` `可微分投影` `参数估计` `Lotka-Volterra系统` `热传导`

## 📋 核心要点

1. 传统PINNs难以严格满足含微分算子的物理约束，通常以软方式最小化约束违反
2. DAE-HardNet通过可微分投影层同时学习函数及其导数，强制满足代数与微分约束
3. 在多个DAE系统测试中，相比MLPs和PINNs，物理损失降低数个数量级，保持预测精度

## 📄 摘要（原文）

> Traditional physics-informed neural networks (PINNs) do not always satisfy physics based constraints, especially when the constraints include differential operators. Rather, they minimize the constraint violations in a soft way. Strict satisfaction of differential-algebraic equations (DAEs) to embed domain knowledge and first-principles in data-driven models is generally challenging. This is because data-driven models consider the original functions to be black-box whose derivatives can only be obtained after evaluating the functions. We introduce DAE-HardNet, a physics-constrained (rather than simply physics-informed) neural network that learns both the functions and their derivatives simultaneously, while enforcing algebraic as well as differential constraints. This is done by projecting model predictions onto the constraint manifold using a differentiable projection layer. We apply DAE-HardNet to several systems and test problems governed by DAEs, including the dynamic Lotka-Volterra predator-prey system and transient heat conduction. We also show the ability of DAE-HardNet to estimate unknown parameters through a parameter estimation problem. Compared to multilayer perceptrons (MLPs) and PINNs, DAE-HardNet achieves orders of magnitude reduction in the physics loss while maintaining the prediction accuracy. It has the added benefits of learning the derivatives which improves the constrained learning of the backbone neural network prior to the projection layer. For specific problems, this suggests that the projection layer can be bypassed for faster inference. The current implementation and codes are available at https://github.com/SOULS-TAMU/DAE-HardNet.

