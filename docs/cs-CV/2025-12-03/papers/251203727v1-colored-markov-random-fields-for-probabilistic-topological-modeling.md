---
layout: default
title: Colored Markov Random Fields for Probabilistic Topological Modeling
---

# Colored Markov Random Fields for Probabilistic Topological Modeling

**arXiv**: [2512.03727v1](https://arxiv.org/abs/2512.03727) | [PDF](https://arxiv.org/pdf/2512.03727.pdf)

**作者**: Lorenzo Marinucci, Leonardo Di Nino, Gabriele D'Acunto, Mario Edoardo Pandolfo, Paolo Di Lorenzo, Sergio Barbarossa

---

## 💡 一句话要点

**提出彩色马尔可夫随机场以在拓扑空间中建模高斯边缘变量的条件与边际依赖关系。**

**关键词**: `概率图模型` `拓扑信号处理` `马尔可夫随机场` `Hodge理论` `分布式估计`

## 📋 核心要点

1. 核心问题：拓扑空间变量依赖关系受拓扑结构限制，传统概率图模型表达能力不足。
2. 方法要点：基于Hodge理论，引入链接着色扩展高斯马尔可夫随机场，编码条件与边际独立性。
3. 实验或效果：通过物理网络分布式估计案例量化优势，对比不同拓扑先验基线。

## 📄 摘要（原文）

> Probabilistic Graphical Models (PGMs) encode conditional dependencies among random variables using a graph -nodes for variables, links for dependencies- and factorize the joint distribution into lower-dimensional components. This makes PGMs well-suited for analyzing complex systems and supporting decision-making. Recent advances in topological signal processing highlight the importance of variables defined on topological spaces in several application domains. In such cases, the underlying topology shapes statistical relationships, limiting the expressiveness of canonical PGMs. To overcome this limitation, we introduce Colored Markov Random Fields (CMRFs), which model both conditional and marginal dependencies among Gaussian edge variables on topological spaces, with a theoretical foundation in Hodge theory. CMRFs extend classical Gaussian Markov Random Fields by including link coloring: connectivity encodes conditional independence, while color encodes marginal independence. We quantify the benefits of CMRFs through a distributed estimation case study over a physical network, comparing it with baselines with different levels of topological prior.

