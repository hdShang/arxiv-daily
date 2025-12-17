---
layout: default
title: ARM-Explainer -- Explaining and improving graph neural network predictions for the maximum clique problem using node features and association rule mining
---

# ARM-Explainer -- Explaining and improving graph neural network predictions for the maximum clique problem using node features and association rule mining

**arXiv**: [2511.22866v1](https://arxiv.org/abs/2511.22866) | [PDF](https://arxiv.org/pdf/2511.22866.pdf)

**作者**: Bharat Sharman, Elkafi Hassini

---

## 💡 一句话要点

**提出ARM-Explainer，基于关联规则挖掘解释并改进图神经网络在最大团问题上的预测。**

**关键词**: `图神经网络解释` `关联规则挖掘` `最大团问题` `组合优化` `后处理解释器`

## 📋 核心要点

1. 核心问题：图神经网络在组合优化问题中预测解释方法不足。
2. 方法要点：采用后处理模型级解释器，通过关联规则挖掘识别关键节点特征。
3. 实验或效果：在基准数据集上提升GNN性能，最大团大小中位数增加22%。

## 📄 摘要（原文）

> Numerous graph neural network (GNN)-based algorithms have been proposed to solve graph-based combinatorial optimization problems (COPs), but methods to explain their predictions remain largely undeveloped. We introduce ARM-Explainer, a post-hoc, model-level explainer based on association rule mining, and demonstrate it on the predictions of the hybrid geometric scattering (HGS) GNN for the maximum clique problem (MCP), a canonical NP-hard graph-based COP. The eight most explanatory association rules discovered by ARM-Explainer achieve high median lift and confidence values of 2.42 and 0.49, respectively, on test instances from the TWITTER and BHOSLIB-DIMACS benchmark datasets. ARM-Explainer identifies the most important node features, together with their value ranges, that influence the GNN's predictions on these datasets. Furthermore, augmenting the GNN with informative node features substantially improves its performance on the MCP, increasing the median largest-found clique size by 22% (from 29.5 to 36) on large graphs from the BHOSLIB-DIMACS dataset.

