---
layout: default
title: Explainable time-series forecasting with sampling-free SHAP for Transformers
---

# Explainable time-series forecasting with sampling-free SHAP for Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20514" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20514v1</a>
  <a href="https://arxiv.org/pdf/2512.20514.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20514v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20514v1', 'Explainable time-series forecasting with sampling-free SHAP for Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matthias Hertel, Sebastian Pütz, Ralf Mikut, Veit Hagenmeyer, Benjamin Schäfer

**分类**: cs.LG

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出SHAPformer，一种基于Transformer的快速、无采样的可解释时间序列预测模型。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `时间序列预测` `可解释AI` `Transformer` `SHAP值` `注意力机制` `电力负荷预测` `无采样`

## 📋 核心要点

1. 现有时间序列预测方法缺乏高效的可解释性工具，SHAP等方法计算成本高，且常假设特征独立性。
2. SHAPformer利用Transformer架构和注意力机制，通过特征子集进行预测，无需采样即可快速生成解释。
3. 实验表明，SHAPformer在合成数据上解释准确，在电力负荷数据上预测性能优异，并能提供有意义的洞见。

## 📝 摘要（中文）

时间序列预测在许多领域对于规划和决策至关重要。可解释性是建立用户信任和满足透明度要求的关键。Shapley Additive Explanations (SHAP) 是一种流行的可解释AI框架，但它缺乏针对时间序列的有效实现，并且在对反事实进行采样时通常假设特征独立性。我们介绍 SHAPformer，这是一种基于 Transformer 架构的准确、快速且无采样的可解释时间序列预测模型。它利用注意力机制操作来进行基于特征子集的预测。SHAPformer 在不到一秒的时间内生成解释，比 SHAP Permutation Explainer 快几个数量级。在具有真实解释的合成数据上，SHAPformer 提供的解释与数据一致。应用于真实世界的电力负荷数据，它实现了有竞争力的预测性能，并提供了有意义的局部和全局见解，例如将过去的负荷识别为关键预测因子，并揭示了圣诞节期间独特的模型行为。

## 🔬 方法详解

**问题定义**：论文旨在解决时间序列预测模型的可解释性问题。现有的SHAP方法在时间序列数据上计算效率低，并且通常假设特征之间是相互独立的，这与时间序列数据的实际情况不符，导致解释不准确。

**核心思路**：论文的核心思路是利用Transformer模型的注意力机制，通过操纵注意力权重来模拟特征子集的影响，从而实现无采样的SHAP值计算。这种方法避免了传统SHAP方法中需要大量采样的过程，显著提高了计算效率。

**技术框架**：SHAPformer基于Transformer架构，主要包含以下模块：输入嵌入层、Transformer编码器层、注意力操纵层和预测输出层。输入嵌入层将时间序列数据转换为嵌入向量。Transformer编码器层学习时间序列的特征表示。注意力操纵层通过调整注意力权重来模拟特征子集的影响。预测输出层基于特征表示进行预测。

**关键创新**：SHAPformer最重要的创新点在于其无采样的SHAP值计算方法。通过直接操纵Transformer的注意力权重，避免了传统SHAP方法中需要大量采样来估计条件期望的问题，从而实现了快速且准确的可解释性分析。与现有方法相比，SHAPformer不需要进行昂贵的采样过程，因此计算效率更高。

**关键设计**：SHAPformer的关键设计包括：(1) 使用标准的Transformer编码器结构来学习时间序列的特征表示；(2) 设计了一种注意力操纵机制，通过屏蔽或调整注意力权重来模拟特征子集的影响；(3) 使用均方误差（MSE）作为预测损失函数，并采用Adam优化器进行模型训练。具体的注意力操纵策略和权重调整方法在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20514v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20514v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20514v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SHAPformer在合成数据上能够准确地恢复ground truth解释，证明了其解释的可靠性。在真实世界的电力负荷数据上，SHAPformer实现了与现有模型相当的预测性能，并且解释速度比SHAP Permutation Explainer快几个数量级。此外，SHAPformer还揭示了电力负荷预测中的一些有趣现象，例如过去负荷是关键预测因子，以及圣诞节期间模型行为的特殊性。

## 🎯 应用场景

SHAPformer可应用于各种需要可解释时间序列预测的领域，例如电力负荷预测、金融市场分析、供应链管理和医疗健康监测。通过提供对预测结果的解释，SHAPformer可以帮助用户理解模型的决策过程，建立信任，并做出更明智的决策。此外，SHAPformer还可以用于识别关键的影响因素，从而优化资源分配和改进业务流程。

## 📄 摘要（原文）

> Time-series forecasts are essential for planning and decision-making in many domains. Explainability is key to building user trust and meeting transparency requirements. Shapley Additive Explanations (SHAP) is a popular explainable AI framework, but it lacks efficient implementations for time series and often assumes feature independence when sampling counterfactuals. We introduce SHAPformer, an accurate, fast and sampling-free explainable time-series forecasting model based on the Transformer architecture. It leverages attention manipulation to make predictions based on feature subsets. SHAPformer generates explanations in under one second, several orders of magnitude faster than the SHAP Permutation Explainer. On synthetic data with ground truth explanations, SHAPformer provides explanations that are true to the data. Applied to real-world electrical load data, it achieves competitive predictive performance and delivers meaningful local and global insights, such as identifying the past load as the key predictor and revealing a distinct model behavior during the Christmas period.

