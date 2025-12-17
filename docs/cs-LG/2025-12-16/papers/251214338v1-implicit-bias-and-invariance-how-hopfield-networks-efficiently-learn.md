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

🎯 **匹配领域**: **视觉里程计**

**关键词**: `Hopfield网络` `隐式偏置` `图同构` `不变子空间` `范数效率` `样本复杂度` `群结构数据` `能量最小化`

## 📋 核心要点

1. 核心问题：现有方法常显式构建不变性，但隐式学习机制在群结构数据中的效率和泛化能力尚不明确。
2. 方法要点：利用Hopfield网络，通过最小化能量流的梯度下降，隐式偏置范数效率解，实现图同构类的高效学习。
3. 实验或效果：实验表明网络能在三维子空间表示同构类，样本复杂度为多项式级，参数收敛到不变子空间。

## 📝 摘要（中文）

许多学习问题涉及对称性，虽然不变性可以内置到神经架构中，但在群结构数据上训练时也可能隐式出现。我们研究了经典Hopfield网络中的这一现象，并表明它们可以从小的随机样本中推断出图的完整同构类。我们的结果显示：(i) 图同构类可以在三维不变子空间中表示，(ii) 使用梯度下降最小化能量流（MEF）具有对范数效率解的隐式偏置，这支撑了学习同构类的多项式样本复杂度界限，以及(iii) 在多种学习规则下，参数随着样本量增长而收敛到不变子空间。这些发现共同突出了Hopfield网络中泛化的统一机制：学习中对范数效率的偏置驱动了在群结构数据下近似不变性的出现。

## 🔬 方法详解

论文基于经典Hopfield网络框架，研究其在图同构类学习中的隐式偏置机制。整体框架涉及使用梯度下降最小化能量流（MEF）作为学习规则，以优化网络参数。关键技术创新点在于揭示了MEF具有对范数效率解的隐式偏置，这促使网络参数在训练过程中自动收敛到三维不变子空间，从而高效表示图同构类。与现有方法的主要区别在于，不依赖显式的不变性设计，而是通过隐式学习机制在群结构数据中自然涌现近似不变性，简化了架构并提升了泛化能力。

## 📊 实验亮点

最重要的实验结果显示，Hopfield网络能从少量随机样本中学习图同构类，样本复杂度为多项式界限，参数收敛到三维不变子空间，验证了隐式偏置范数效率在驱动近似不变性中的核心作用。

## 🎯 应用场景

该研究可应用于图结构数据分析、社交网络建模、化学分子识别等领域，通过隐式学习对称性，提高模型在复杂数据中的泛化效率和鲁棒性，为设计更简洁的神经网络提供理论指导。

## 📄 摘要（原文）

> Many learning problems involve symmetries, and while invariance can be built into neural architectures, it can also emerge implicitly when training on group-structured data. We study this phenomenon in classical Hopfield networks and show they can infer the full isomorphism class of a graph from a small random sample. Our results reveal that: (i) graph isomorphism classes can be represented within a three-dimensional invariant subspace, (ii) using gradient descent to minimize energy flow (MEF) has an implicit bias toward norm-efficient solutions, which underpins a polynomial sample complexity bound for learning isomorphism classes, and (iii) across multiple learning rules, parameters converge toward the invariant subspace as sample sizes grow. Together, these findings highlight a unifying mechanism for generalization in Hopfield networks: a bias toward norm efficiency in learning drives the emergence of approximate invariance under group-structured data.

