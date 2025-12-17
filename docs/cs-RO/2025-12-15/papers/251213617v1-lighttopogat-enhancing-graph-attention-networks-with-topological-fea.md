---
layout: default
title: LightTopoGAT: Enhancing Graph Attention Networks with Topological Features for Efficient Graph Classification
---

# LightTopoGAT: Enhancing Graph Attention Networks with Topological Features for Efficient Graph Classification

**arXiv**: [2512.13617v1](https://arxiv.org/abs/2512.13617) | [PDF](https://arxiv.org/pdf/2512.13617.pdf)

**作者**: Ankit Sharma, Sayan Roy Gupta

---

## 💡 一句话要点

**提出LightTopoGAT，通过拓扑特征增强图注意力网络以提升图分类效率。**

**关键词**: `图神经网络` `图分类` `拓扑特征` `注意力机制` `轻量化模型`

## 📋 核心要点

1. 核心问题：图神经网络计算资源需求大且难以有效捕获全局图属性。
2. 方法要点：引入节点度和局部聚类系数进行拓扑增强，保持参数效率的注意力机制。
3. 实验或效果：在MUTAG和PROTEINS数据集上准确率分别提升6.6%和2.2%，性能增益源于拓扑特征。

## 📄 摘要（原文）

> Graph Neural Networks have demonstrated significant success in graph classification tasks, yet they often require substantial computational resources and struggle to capture global graph properties effectively. We introduce LightTopoGAT, a lightweight graph attention network that enhances node features through topological augmentation by incorporating node degree and local clustering coefficient to improve graph representation learning. The proposed approach maintains parameter efficiency through streamlined attention mechanisms while integrating structural information that is typically overlooked by local message passing schemes. Through comprehensive experiments on three benchmark datasets, MUTAG, ENZYMES, and PROTEINS, we show that LightTopoGAT achieves superior performance compared to established baselines including GCN, GraphSAGE, and standard GAT, with a 6.6 percent improvement in accuracy on MUTAG and a 2.2 percent improvement on PROTEINS. Ablation studies further confirm that these performance gains arise directly from the inclusion of topological features, demonstrating a simple yet effective strategy for enhancing graph neural network performance without increasing architectural complexity.

