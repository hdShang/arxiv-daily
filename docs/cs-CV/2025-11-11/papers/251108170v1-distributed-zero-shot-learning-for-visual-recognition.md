---
layout: default
title: Distributed Zero-Shot Learning for Visual Recognition
---

# Distributed Zero-Shot Learning for Visual Recognition

**arXiv**: [2511.08170v1](https://arxiv.org/abs/2511.08170) | [PDF](https://arxiv.org/pdf/2511.08170.pdf)

**作者**: Zhi Chen, Yadan Luo, Zi Huang, Jingjing Li, Sen Wang, Xin Yu

---

## 💡 一句话要点

**提出分布式零样本学习框架以解决去中心化数据中的异构性问题**

**关键词**: `分布式学习` `零样本学习` `属性正则化` `视觉-属性映射` `数据异构性`

## 📋 核心要点

1. 核心问题：分布式节点数据异构性影响零样本学习模型对未见类的泛化能力
2. 方法要点：引入跨节点属性正则器和全局属性-视觉共识以稳定特征空间和映射
3. 实验或效果：在分布式数据学习中优于现有方法，提升零样本学习性能

## 📄 摘要（原文）

> In this paper, we propose a Distributed Zero-Shot Learning (DistZSL) framework that can fully exploit decentralized data to learn an effective model for unseen classes. Considering the data heterogeneity issues across distributed nodes, we introduce two key components to ensure the effective learning of DistZSL: a cross-node attribute regularizer and a global attribute-to-visual consensus. Our proposed cross-node attribute regularizer enforces the distances between attribute features to be similar across different nodes. In this manner, the overall attribute feature space would be stable during learning, and thus facilitate the establishment of visual-to-attribute(V2A) relationships. Then, we introduce the global attribute-tovisual consensus to mitigate biased V2A mappings learned from individual nodes. Specifically, we enforce the bilateral mapping between the attribute and visual feature distributions to be consistent across different nodes. Thus, the learned consistent V2A mapping can significantly enhance zero-shot learning across different nodes. Extensive experiments demonstrate that DistZSL achieves superior performance to the state-of-the-art in learning from distributed data.

