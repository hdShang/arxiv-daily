---
layout: default
title: Rates and architectures for learning geometrically non-trivial operators
---

# Rates and architectures for learning geometrically non-trivial operators

**arXiv**: [2512.09376v1](https://arxiv.org/abs/2512.09376) | [PDF](https://arxiv.org/pdf/2512.09376.pdf)

**作者**: T. Mitchell Roddenberry, Leo Tzou, Ivan Dokmanić, Maarten V. de Hoop, Richard G. Baraniuk

---

## 💡 一句话要点

**提出学习几何非平凡算子的理论与架构，实现超代数误差衰减与数据高效性。**

**关键词**: `算子学习` `几何积分算子` `双纤维变换` `科学机器学习` `数据高效性` `交叉注意力架构`

## 📋 核心要点

1. 扩展学习理论至双纤维变换，涵盖广义Radon和测地线射线变换等几何积分算子。
2. 证明该类算子无维度诅咒，误差随训练样本数倒数衰减快于任意固定幂次。
3. 设计基于水平集方法的交叉注意力架构，实现通用、稳定且数据高效的学习。

## 📄 摘要（原文）

> Deep learning methods have proven capable of recovering operators between high-dimensional spaces, such as solution maps of PDEs and similar objects in mathematical physics, from very few training samples. This phenomenon of data-efficiency has been proven for certain classes of elliptic operators with simple geometry, i.e., operators that do not change the domain of the function or propagate singularities. However, scientific machine learning is commonly used for problems that do involve the propagation of singularities in a priori unknown ways, such as waves, advection, and fluid dynamics. In light of this, we expand the learning theory to include double fibration transforms--geometric integral operators that include generalized Radon and geodesic ray transforms. We prove that this class of operators does not suffer from the curse of dimensionality: the error decays superalgebraically, that is, faster than any fixed power of the reciprocal of the number of training samples. Furthermore, we investigate architectures that explicitly encode the geometry of these transforms, demonstrating that an architecture reminiscent of cross-attention based on levelset methods yields a parameterization that is universal, stable, and learns double fibration transforms from very few training examples. Our results contribute to a rapidly-growing line of theoretical work on learning operators for scientific machine learning.

