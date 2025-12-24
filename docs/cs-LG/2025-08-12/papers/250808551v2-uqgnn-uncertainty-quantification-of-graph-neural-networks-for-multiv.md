---
layout: default
title: "UQGNN: Uncertainty Quantification of Graph Neural Networks for Multivariate Spatiotemporal Prediction"
---

# UQGNN: Uncertainty Quantification of Graph Neural Networks for Multivariate Spatiotemporal Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08551" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08551v2</a>
  <a href="https://arxiv.org/pdf/2508.08551.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08551v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08551v2', 'UQGNN: Uncertainty Quantification of Graph Neural Networks for Multivariate Spatiotemporal Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dahai Yu, Dingyi Zhuang, Lin Jiang, Rongchao Xu, Xinyue Ye, Yuheng Bu, Shenhao Wang, Guang Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-12 (更新: 2025-08-31)

**备注**: 10 pages, 7 figures, SIGSPATIAL 2025

---

## 💡 一句话要点

**提出UQGNN以解决多变量时空预测中的不确定性量化问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `图神经网络` `时空预测` `不确定性量化` `多变量分析` `深度学习`

## 📋 核心要点

1. 现有的时空预测模型大多为确定性模型，无法有效量化预测的不确定性，导致结果不可靠。
2. 本文提出的UQGNN通过交互感知时空嵌入模块和多变量概率预测模块，能够同时捕捉复杂的时空交互模式和量化不确定性。
3. 在多个真实数据集上，UQGNN在预测准确性和不确定性量化方面均表现出显著提升，例如在深圳数据集上提升了5%。

## 📝 摘要（中文）

时空预测在城市规划、交通优化、灾害响应和疫情控制等多个实际应用中扮演着重要角色。尽管近年来深度学习模型在此领域取得了显著进展，但大多数现有模型是确定性的，仅预测期望均值而未量化不确定性，导致结果可能不可靠。为填补这一研究空白，本文提出了一种新型图神经网络UQGNN，专注于多变量时空预测。UQGNN引入了两个关键创新：一是交互感知时空嵌入模块，二是多变量概率预测模块。通过在深圳、纽约和芝加哥的四个真实数据集上进行广泛实验，UQGNN在预测准确性和不确定性量化方面均优于现有最先进的基线。

## 🔬 方法详解

**问题定义**：本文旨在解决多变量时空预测中不确定性量化的问题。现有方法通常只提供期望均值预测，忽视了不同城市现象之间的内在关联，导致结果的可靠性不足。

**核心思路**：UQGNN通过引入交互感知时空嵌入模块和多变量概率预测模块，旨在同时捕捉复杂的时空交互模式并量化预测的不确定性，从而提升预测的准确性和可靠性。

**技术框架**：UQGNN的整体架构包括两个主要模块：交互感知时空嵌入模块，结合了多变量扩散图卷积网络和交互感知时间卷积网络；多变量概率预测模块，负责估计期望均值和相关的不确定性。

**关键创新**：UQGNN的核心创新在于其能够同时处理多种城市现象的时空数据，并通过概率模型量化不确定性，这与传统的单一现象预测方法有本质区别。

**关键设计**：在网络结构上，UQGNN采用了多层图卷积和时间卷积的组合，损失函数设计上考虑了预测误差和不确定性量化的平衡，以确保模型的稳定性和准确性。

## 📊 实验亮点

在实验中，UQGNN在深圳、纽约和芝加哥的四个真实多变量时空数据集上表现出色，尤其是在深圳数据集上，UQGNN在预测准确性和不确定性量化方面均提升了5%，超越了现有的最先进基线，证明了其有效性和优越性。

## 🎯 应用场景

UQGNN的研究成果在城市规划、交通管理、灾害应对和公共卫生等领域具有广泛的应用潜力。通过量化不确定性，决策者可以更好地评估风险并制定更有效的应对策略，从而提升城市管理的智能化水平和应对突发事件的能力。

## 📄 摘要（原文）

> Spatiotemporal prediction plays a critical role in numerous real-world applications such as urban planning, transportation optimization, disaster response, and pandemic control. In recent years, researchers have made significant progress by developing advanced deep learning models for spatiotemporal prediction. However, most existing models are deterministic, i.e., predicting only the expected mean values without quantifying uncertainty, leading to potentially unreliable and inaccurate outcomes. While recent studies have introduced probabilistic models to quantify uncertainty, they typically focus on a single phenomenon (e.g., taxi, bike, crime, or traffic crashes), thereby neglecting the inherent correlations among heterogeneous urban phenomena. To address the research gap, we propose a novel Graph Neural Network with Uncertainty Quantification, termed UQGNN for multivariate spatiotemporal prediction. UQGNN introduces two key innovations: (i) an Interaction-aware Spatiotemporal Embedding Module that integrates a multivariate diffusion graph convolutional network and an interaction-aware temporal convolutional network to effectively capture complex spatial and temporal interaction patterns, and (ii) a multivariate probabilistic prediction module designed to estimate both expected mean values and associated uncertainties. Extensive experiments on four real-world multivariate spatiotemporal datasets from Shenzhen, New York City, and Chicago demonstrate that UQGNN consistently outperforms state-of-the-art baselines in both prediction accuracy and uncertainty quantification. For example, on the Shenzhen dataset, UQGNN achieves a 5% improvement in both prediction accuracy and uncertainty quantification.

