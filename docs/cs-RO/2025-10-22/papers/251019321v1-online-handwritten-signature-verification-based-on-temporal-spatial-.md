---
layout: default
title: Online Handwritten Signature Verification Based on Temporal-Spatial Graph Attention Transformer
---

# Online Handwritten Signature Verification Based on Temporal-Spatial Graph Attention Transformer

**arXiv**: [2510.19321v1](https://arxiv.org/abs/2510.19321) | [PDF](https://arxiv.org/pdf/2510.19321.pdf)

**作者**: Hai-jie Yuan, Heng Zhang, Fei Yin

---

## 💡 一句话要点

**提出时空图注意力Transformer以提升在线手写签名验证准确性**

**关键词**: `手写签名验证` `图注意力网络` `门控循环单元` `时空建模` `动态特征` `身份认证`

## 📋 核心要点

1. 核心问题：手写签名验证因用户内变异性与伪造风险而准确率低
2. 方法要点：结合图注意力网络与门控循环单元建模时空依赖关系
3. 实验或效果：在MSDS和DeepSignDB数据集上EER低于现有方法

## 📄 摘要（原文）

> Handwritten signature verification is a crucial aspect of identity
> authentication, with applications in various domains such as finance and
> e-commerce. However, achieving high accuracy in signature verification remains
> challenging due to intra-user variability and the risk of forgery. This paper
> introduces a novel approach for dynamic signature verification: the
> Temporal-Spatial Graph Attention Transformer (TS-GATR). TS-GATR combines the
> Graph Attention Network (GAT) and the Gated Recurrent Unit (GRU) to model both
> spatial and temporal dependencies in signature data. TS-GATR enhances
> verification performance by representing signatures as graphs, where each node
> captures dynamic features (e.g. position, velocity, pressure), and by using
> attention mechanisms to model their complex relationships. The proposed method
> further employs a Dual-Graph Attention Transformer (DGATR) module, which
> utilizes k-step and k-nearest neighbor adjacency graphs to model local and
> global spatial features, respectively. To capture long-term temporal
> dependencies, the model integrates GRU, thereby enhancing its ability to learn
> dynamic features during signature verification. Comprehensive experiments
> conducted on benchmark datasets such as MSDS and DeepSignDB show that TS-GATR
> surpasses current state-of-the-art approaches, consistently achieving lower
> Equal Error Rates (EER) across various scenarios.

