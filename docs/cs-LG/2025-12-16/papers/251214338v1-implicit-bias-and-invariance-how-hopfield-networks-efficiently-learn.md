---
layout: default
title: Implicit Bias and Invariance: How Hopfield Networks Efficiently Learn Graph Orbits
---

# Implicit Bias and Invariance: How Hopfield Networks Efficiently Learn Graph Orbits

**arXiv**: [2512.14338v1](https://arxiv.org/abs/2512.14338) | [PDF](https://arxiv.org/pdf/2512.14338.pdf)

**作者**: Michael Murray, Tenzin Chan, Kedar Karhadker, Christopher J. Hillar

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**揭示Hopfield网络通过范数效率隐式学习图同构类，实现多项式样本复杂度**

**关键词**: `Hopfield网络` `隐式偏置` `图同构` `不变子空间` `范数效率` `样本复杂度` `群结构数据` `梯度下降`

## 📋 核心要点

1. 核心问题：现有方法常显式构建不变性，但隐式学习机制在群结构数据中的效率和泛化能力尚不明确。
2. 方法要点：利用Hopfield网络，通过最小化能量流（MEF）的梯度下降，隐式偏置范数效率解，实现图同构类学习。
3. 实验或效果：网络能在三维不变子空间中表示同构类，样本复杂度为多项式，参数收敛到不变子空间。

## 📝 摘要（中文）

许多学习问题涉及对称性，虽然不变性可以内置到神经架构中，但在群结构数据上训练时也可能隐式出现。我们研究了经典Hopfield网络中的这一现象，并表明它们可以从小的随机样本中推断出图的完整同构类。我们的结果显示：(i) 图同构类可以在三维不变子空间中表示，(ii) 使用梯度下降最小化能量流（MEF）具有对范数效率解的隐式偏置，这支撑了学习同构类的多项式样本复杂度界限，以及(iii) 在多种学习规则下，参数随着样本量增长而收敛到不变子空间。这些发现共同突出了Hopfield网络中泛化的统一机制：学习中对范数效率的偏置驱动了在群结构数据下近似不变性的出现。

## 🔬 方法详解

论文采用经典Hopfield网络作为整体框架，研究其在图同构类学习中的隐式偏置。关键技术创新点在于分析梯度下降最小化能量流（MEF）的过程，揭示其对范数效率解的隐式偏置，这驱动了不变子空间的收敛。与现有方法的主要区别在于，不依赖显式的不变性设计，而是通过优化过程自然涌现近似不变性，从而更高效地处理对称性数据。

## 📊 实验亮点

最重要的实验结果显示，Hopfield网络能从少量随机样本中学习图同构类，样本复杂度为多项式界限，且参数在多种学习规则下收敛到三维不变子空间，验证了隐式偏置对泛化的关键作用。

## 🎯 应用场景

该研究可应用于图结构数据分析、模式识别和机器学习中的对称性处理，例如社交网络分析、化学分子结构分类，以及需要高效学习不变特征的领域，提升模型在群结构数据上的泛化能力。

## 📄 摘要（原文）

> Many learning problems involve symmetries, and while invariance can be built into neural architectures, it can also emerge implicitly when training on group-structured data. We study this phenomenon in classical Hopfield networks and show they can infer the full isomorphism class of a graph from a small random sample. Our results reveal that: (i) graph isomorphism classes can be represented within a three-dimensional invariant subspace, (ii) using gradient descent to minimize energy flow (MEF) has an implicit bias toward norm-efficient solutions, which underpins a polynomial sample complexity bound for learning isomorphism classes, and (iii) across multiple learning rules, parameters converge toward the invariant subspace as sample sizes grow. Together, these findings highlight a unifying mechanism for generalization in Hopfield networks: a bias toward norm efficiency in learning drives the emergence of approximate invariance under group-structured data.

