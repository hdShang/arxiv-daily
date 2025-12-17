---
layout: default
title: Credal Graph Neural Networks
---

# Credal Graph Neural Networks

**arXiv**: [2512.02722v1](https://arxiv.org/abs/2512.02722) | [PDF](https://arxiv.org/pdf/2512.02722.pdf)

**作者**: Matteo Tolloso, Davide Bacciu

---

## 💡 一句话要点

**提出信度图神经网络以提升图神经网络在分布外条件下的不确定性量化可靠性**

**关键词**: `信度学习` `图神经网络` `不确定性量化` `分布外泛化` `节点分类` `异配图`

## 📋 核心要点

1. 核心问题：图神经网络在分布外条件下不确定性量化不足，现有方法主要依赖贝叶斯推断或集成学习
2. 方法要点：扩展信度学习至图域，训练图神经网络输出信度集形式的集合值预测，并利用层间信息传播的不同方面
3. 实验或效果：在异配图分布偏移下，信度图神经网络提供更可靠的认识不确定性表示，并实现最先进性能

## 📄 摘要（原文）

> Uncertainty quantification is essential for deploying reliable Graph Neural Networks (GNNs), where existing approaches primarily rely on Bayesian inference or ensembles. In this paper, we introduce the first credal graph neural networks (CGNNs), which extend credal learning to the graph domain by training GNNs to output set-valued predictions in the form of credal sets. To account for the distinctive nature of message passing in GNNs, we develop a complementary approach to credal learning that leverages different aspects of layer-wise information propagation. We assess our approach on uncertainty quantification in node classification under out-of-distribution conditions. Our analysis highlights the critical role of the graph homophily assumption in shaping the effectiveness of uncertainty estimates. Extensive experiments demonstrate that CGNNs deliver more reliable representations of epistemic uncertainty and achieve state-of-the-art performance under distributional shift on heterophilic graphs.

