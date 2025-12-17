---
layout: default
title: Dynamic Stratified Contrastive Learning with Upstream Augmentation for MILP Branching
---

# Dynamic Stratified Contrastive Learning with Upstream Augmentation for MILP Branching

**arXiv**: [2511.21107v1](https://arxiv.org/abs/2511.21107) | [PDF](https://arxiv.org/pdf/2511.21107.pdf)

**作者**: Tongkai Lu, Shuai Ma, Chongyang Tao

---

## 💡 一句话要点

**提出动态分层对比学习框架，结合上游增强解决MILP分支问题**

**关键词**: `混合整数线性规划` `分支定界` `图卷积神经网络` `对比学习` `数据增强` `求解效率`

## 📋 核心要点

1. 核心问题：MILP分支中语义变化、上游节点稀缺和强分支样本收集成本高
2. 方法要点：基于特征分布分组节点，使用GCNN模型逐步分离，并引入上游增强生成实例
3. 实验或效果：在标准基准上提升分支准确率、减少求解时间，并有效泛化到未见实例

## 📄 摘要（原文）

> Mixed Integer Linear Programming (MILP) is a fundamental class of NP-hard problems that has garnered significant attention from both academia and industry. The Branch-and-Bound (B\&B) method is the dominant approach for solving MILPs and the branching plays an important role in B\&B methods. Neural-based learning frameworks have recently been developed to enhance branching policies and the efficiency of solving MILPs. However, these methods still struggle with semantic variation across depths, the scarcity of upstream nodes, and the costly collection of strong branching samples. To address these issues, we propose \ours, a Dynamic \underline{\textbf{S}}tratified \underline{\textbf{C}}ontrastive Training Framework for \underline{\textbf{MILP}} Branching. It groups branch-and-bound nodes based on their feature distributions and trains a GCNN-based discriminative model to progressively separate nodes across groups, learning finer-grained node representations throughout the tree. To address data scarcity and imbalance at upstream nodes, we introduce an upstream-augmented MILP derivation procedure that generates both theoretically equivalent and perturbed instances. \ours~effectively models subtle semantic differences between nodes, significantly enhancing branching accuracy and solving efficiency, particularly for upstream nodes. Extensive experiments on standard MILP benchmarks demonstrate that our method enhances branching accuracy, reduces solving time, and generalizes effectively to unseen instances.

