---
layout: default
title: PR-CapsNet: Pseudo-Riemannian Capsule Network with Adaptive Curvature Routing for Graph Learning
---

# PR-CapsNet: Pseudo-Riemannian Capsule Network with Adaptive Curvature Routing for Graph Learning

**arXiv**: [2512.08218v1](https://arxiv.org/abs/2512.08218) | [PDF](https://arxiv.org/pdf/2512.08218.pdf)

**作者**: Ye Qin, Jingchao Wang, Yang Shi, Haiying Huang, Junxu Li, Weijian Liu, Tinghui Chen, Jinghui Qin

---

## 💡 一句话要点

**提出PR-CapsNet，通过自适应曲率伪黎曼流形改进胶囊网络，用于图表示学习。**

**关键词**: `图表示学习` `胶囊网络` `伪黎曼流形` `自适应曲率路由` `图分类`

## 📋 核心要点

1. 核心问题：胶囊网络在固定曲率空间中建模真实世界图的复杂几何结构不佳，导致性能次优。
2. 方法要点：扩展胶囊路由至伪黎曼流形，利用自适应曲率路由融合不同曲率空间特征，增强图表示能力。
3. 实验或效果：在节点和图分类基准测试中优于现有方法，验证了对复杂图结构的强表示能力。

## 📄 摘要（原文）

> Capsule Networks (CapsNets) show exceptional graph representation capacity via dynamic routing and vectorized hierarchical representations, but they model the complex geometries of real\-world graphs poorly by fixed\-curvature space due to the inherent geodesical disconnectedness issues, leading to suboptimal performance. Recent works find that non\-Euclidean pseudo\-Riemannian manifolds provide specific inductive biases for embedding graph data, but how to leverage them to improve CapsNets is still underexplored. Here, we extend the Euclidean capsule routing into geodesically disconnected pseudo\-Riemannian manifolds and derive a Pseudo\-Riemannian Capsule Network (PR\-CapsNet), which models data in pseudo\-Riemannian manifolds of adaptive curvature, for graph representation learning. Specifically, PR\-CapsNet enhances the CapsNet with Adaptive Pseudo\-Riemannian Tangent Space Routing by utilizing pseudo\-Riemannian geometry. Unlike single\-curvature or subspace\-partitioning methods, PR\-CapsNet concurrently models hierarchical and cluster or cyclic graph structures via its versatile pseudo\-Riemannian metric. It first deploys Pseudo\-Riemannian Tangent Space Routing to decompose capsule states into spherical\-temporal and Euclidean\-spatial subspaces with diffeomorphic transformations. Then, an Adaptive Curvature Routing is developed to adaptively fuse features from different curvature spaces for complex graphs via a learnable curvature tensor with geometric attention from local manifold properties. Finally, a geometric properties\-preserved Pseudo\-Riemannian Capsule Classifier is developed to project capsule embeddings to tangent spaces and use curvature\-weighted softmax for classification. Extensive experiments on node and graph classification benchmarks show PR\-CapsNet outperforms SOTA models, validating PR\-CapsNet's strong representation power for complex graph structures.

