---
layout: default
title: Learning Degenerate Manifolds of Frustrated Magnets with Boltzmann Machines
---

# Learning Degenerate Manifolds of Frustrated Magnets with Boltzmann Machines

**arXiv**: [2511.19879v1](https://arxiv.org/abs/2511.19879) | [PDF](https://arxiv.org/pdf/2511.19879.pdf)

**作者**: Jackson C. Glass, Gia-Wei Chern

---

## 💡 一句话要点

**提出受限玻尔兹曼机以学习受挫磁体中的简并流形**

**关键词**: `受限玻尔兹曼机` `受挫磁体` `简并流形` `自旋配置` `生成模型` `相关函数`

## 📋 核心要点

1. 核心问题：建模受挫磁体中无序强关联相的自旋配置简并流形
2. 方法要点：使用受限玻尔兹曼机作为生成模型学习局部约束和对称性破缺
3. 实验或效果：在ANNNI模型和kagome自旋冰中准确复现相关函数和冰规则

## 📄 摘要（原文）

> We show that Restricted Boltzmann Machines (RBMs) provide a flexible generative framework for modeling spin configurations in disordered yet strongly correlated phases of frustrated magnets. As a benchmark, we first demonstrate that an RBM can learn the zero-temperature ground-state manifold of the one-dimensional ANNNI model at its multiphase point, accurately reproducing its characteristic oscillatory and exponentially decaying correlations. We then apply RBMs to kagome spin ice and show that they successfully learn the local ice rules and short-range correlations of the extensively degenerate ice-I manifold. Correlation functions computed from RBM-generated configurations closely match those from direct Monte Carlo simulations. For the partially ordered ice-II phase -- featuring long-range charge order and broken time-reversal symmetry -- accurate modeling requires RBMs with uniform-sign bias fields, mirroring the underlying symmetry breaking. These results highlight the utility of RBMs as generative models for learning constrained and highly frustrated magnetic states.

