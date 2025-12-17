---
layout: default
title: PINE: Pipeline for Important Node Exploration in Attributed Networks
---

# PINE: Pipeline for Important Node Exploration in Attributed Networks

**arXiv**: [2512.07244v1](https://arxiv.org/abs/2512.07244) | [PDF](https://arxiv.org/pdf/2512.07244.pdf)

**作者**: Elizaveta Kovtun, Maksim Makarenko, Natalia Semenova, Alexey Zaytsev, Semen Budennyy

---

## 💡 一句话要点

**提出PINE管道，以无监督方式解决属性网络中关键节点识别问题。**

**关键词**: `属性网络` `无监督学习` `注意力机制` `节点重要性` `图神经网络` `企业图分析`

## 📋 核心要点

1. 核心问题：属性网络中节点重要性识别，传统方法忽略节点语义特征，现有神经网络方法需监督。
2. 方法要点：基于注意力的图模型，结合节点语义特征学习结构属性，利用注意力分布计算重要性分数。
3. 实验或效果：在多种同质和异质属性网络上验证性能优越，适用于大规模企业图的无监督关键实体识别。

## 📄 摘要（原文）

> A graph with semantically attributed nodes are a common data structure in a wide range of domains. It could be interlinked web data or citation networks of scientific publications. The essential problem for such a data type is to determine nodes that carry greater importance than all the others, a task that markedly enhances system monitoring and management. Traditional methods to identify important nodes in networks introduce centrality measures, such as node degree or more complex PageRank. However, they consider only the network structure, neglecting the rich node attributes. Recent methods adopt neural networks capable of handling node features, but they require supervision. This work addresses the identified gap--the absence of approaches that are both unsupervised and attribute-aware--by introducing a Pipeline for Important Node Exploration (PINE). At the core of the proposed framework is an attention-based graph model that incorporates node semantic features in the learning process of identifying the structural graph properties. The PINE's node importance scores leverage the obtained attention distribution. We demonstrate the superior performance of the proposed PINE method on various homogeneous and heterogeneous attributed networks. As an industry-implemented system, PINE tackles the real-world challenge of unsupervised identification of key entities within large-scale enterprise graphs.

