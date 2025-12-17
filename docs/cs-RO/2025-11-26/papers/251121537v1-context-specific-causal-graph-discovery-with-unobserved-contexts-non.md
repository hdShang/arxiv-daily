---
layout: default
title: Context-Specific Causal Graph Discovery with Unobserved Contexts: Non-Stationarity, Regimes and Spatio-Temporal Patterns
---

# Context-Specific Causal Graph Discovery with Unobserved Contexts: Non-Stationarity, Regimes and Spatio-Temporal Patterns

**arXiv**: [2511.21537v1](https://arxiv.org/abs/2511.21537) | [PDF](https://arxiv.org/pdf/2511.21537.pdf)

**作者**: Martin Rabel, Jakob Runge

---

## 💡 一句话要点

**提出框架以在非平稳时空数据中发现上下文特定因果图，提升因果发现稳定性。**

**关键词**: `因果图发现` `非平稳数据` `时空模式` `约束因果发现` `独立性测试`

## 📋 核心要点

1. 核心问题：非平稳时空数据中因果图变化影响算法稳定性和结果可靠性。
2. 方法要点：基于约束因果发现，修改独立性测试，实现模块化可扩展框架。
3. 实验或效果：兼容多种因果发现算法，未知实际应用效果。

## 📄 摘要（原文）

> Real-world data, for example in climate applications, often consists of spatially gridded time series data or data with comparable structure. While the underlying system is often believed to behave similar at different points in space and time, those variations that do exist are twofold relevant: They often encode important information in and of themselves. And they may negatively affect the stability / convergence and reliability\Slash{}validity of results of algorithms assuming stationarity or space-translation invariance. We study the information encoded in changes of the causal graph, with stability in mind. An analysis of this general task identifies two core challenges. We develop guiding principles to overcome these challenges, and provide a framework realizing these principles by modifying constraint-based causal discovery approaches on the level of independence testing. This leads to an extremely modular, easily extensible and widely applicable framework. It can leverage existing constraint-based causal discovery methods (demonstrated on IID-algorithms PC, PC-stable, FCI and time series algorithms PCMCI, PCMCI+, LPCMCI) with little to no modification. The built-in modularity allows to systematically understand and improve upon an entire array of subproblems. By design, it can be extended by leveraging insights from change-point-detection, clustering, independence-testing and other well-studied related problems. The division into more accessible sub-problems also simplifies the understanding of fundamental limitations, hyperparameters controlling trade-offs and the statistical interpretation of results. An open-source implementation will be available soon.

