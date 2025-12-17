---
layout: default
title: Novel Class Discovery for Point Cloud Segmentation via Joint Learning of Causal Representation and Reasoning
---

# Novel Class Discovery for Point Cloud Segmentation via Joint Learning of Causal Representation and Reasoning

**arXiv**: [2510.13307v1](https://arxiv.org/abs/2510.13307) | [PDF](https://arxiv.org/pdf/2510.13307.pdf)

**作者**: Yang Li, Aming Wu, Zihao Zhang, Yahong Han

---

## 💡 一句话要点

**提出联合学习因果表示与推理方法以解决点云分割中的新类发现问题**

**关键词**: `点云分割` `新类发现` `因果表示` `结构因果模型` `图推理` `语义分割`

## 📋 核心要点

1. 核心问题：点云分割中，仅基于标注基类学习未标注新类的分割模型，需精确关联点表示与类标签。
2. 方法要点：引入结构因果模型分析隐藏混杂因子，构建因果表示原型和图结构进行因果推理。
3. 实验或效果：在3D和2D新类发现语义分割实验中，方法表现出优越性能，并通过可视化验证。

## 📄 摘要（原文）

> In this paper, we focus on Novel Class Discovery for Point Cloud Segmentation
> (3D-NCD), aiming to learn a model that can segment unlabeled (novel) 3D classes
> using only the supervision from labeled (base) 3D classes. The key to this task
> is to setup the exact correlations between the point representations and their
> base class labels, as well as the representation correlations between the
> points from base and novel classes. A coarse or statistical correlation
> learning may lead to the confusion in novel class inference. lf we impose a
> causal relationship as a strong correlated constraint upon the learning
> process, the essential point cloud representations that accurately correspond
> to the classes should be uncovered. To this end, we introduce a structural
> causal model (SCM) to re-formalize the 3D-NCD problem and propose a new method,
> i.e., Joint Learning of Causal Representation and Reasoning. Specifically, we
> first analyze hidden confounders in the base class representations and the
> causal relationships between the base and novel classes through SCM. We devise
> a causal representation prototype that eliminates confounders to capture the
> causal representations of base classes. A graph structure is then used to model
> the causal relationships between the base classes' causal representation
> prototypes and the novel class prototypes, enabling causal reasoning from base
> to novel classes. Extensive experiments and visualization results on 3D and 2D
> NCD semantic segmentation demonstrate the superiorities of our method.

