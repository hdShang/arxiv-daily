---
layout: default
title: "Fisher Random Walk: Automatic Debiasing Contextual Preference Inference for Large Language Model Evaluation"
---

# Fisher Random Walk: Automatic Debiasing Contextual Preference Inference for Large Language Model Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05852" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05852v1</a>
  <a href="https://arxiv.org/pdf/2509.05852.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05852v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05852v1', 'Fisher Random Walk: Automatic Debiasing Contextual Preference Inference for Large Language Model Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yichi Zhang, Alexander Belloni, Ethan X. Fang, Junwei Lu, Xiaoan Xu

**分类**: stat.ML, cs.LG, math.ST

**发布日期**: 2025-09-06

---

## 💡 一句话要点

**提出Fisher随机游走方法，用于大规模语言模型评估中的自动去偏上下文偏好推断。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大规模语言模型评估` `上下文偏好推断` `去偏估计` `Fisher随机游走` `半参数估计` `Bradley-Terry-Luce模型` `多重假设检验` `分布偏移`

## 📋 核心要点

1. 现有大规模语言模型评估方法缺乏严格性和可扩展性，难以有效处理上下文相关的偏好推断。
2. 提出Fisher随机游走策略，通过加权残差平衡项聚合，实现上下文偏好推断的自动去偏估计。
3. 实验结果表明，该方法在语言模型评估中具有准确性、效率和实用性，并能有效处理分布偏移。

## 📝 摘要（中文）

本文针对大规模语言模型评估中严格且可扩展的需求，研究了跨领域的上下文相关偏好评分函数的成对比较泛函的上下文偏好推断问题。聚焦于上下文Bradley-Terry-Luce模型，我们开发了一种半参数有效估计器，通过聚合比较图上的加权残差平衡项来自动实现去偏估计。我们证明了当权重来源于一种名为Fisher随机游走的新策略时，可以实现效率。我们还提出了一种计算上可行的方法，通过 nuisance 权重函数的势表示来计算权重。我们证明了我们的推断程序对于通用评分函数估计器是有效的，满足了从业者实现灵活的深度学习方法的需求。我们将该程序扩展到使用高斯乘数bootstrap进行多重假设检验，以控制familywise error，并通过交叉拟合的重要性抽样调整来处理目标域推断中的分布偏移。包括在不同上下文中进行的语言模型评估在内的数值研究证实了我们方法的准确性、效率和实用性。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模语言模型评估中，由于上下文因素导致的偏好推断偏差问题。现有方法难以有效处理上下文相关性，导致评估结果不准确，且缺乏可扩展性，难以应用于大规模语言模型的评估。

**核心思路**：论文的核心思路是利用Fisher随机游走策略，为每个比较样本赋予合适的权重，通过聚合加权残差平衡项，从而实现对上下文偏好推断的自动去偏。这种方法旨在消除由于上下文因素引起的偏差，提高评估的准确性和可靠性。

**技术框架**：整体框架基于上下文Bradley-Terry-Luce模型，主要包含以下几个阶段：1) 构建上下文相关的成对比较图；2) 利用Fisher随机游走策略计算每个比较样本的权重；3) 聚合加权残差平衡项，估计偏好评分函数；4) 使用高斯乘数bootstrap进行多重假设检验，控制familywise error；5) 通过交叉拟合的重要性抽样调整处理分布偏移。

**关键创新**：最重要的技术创新点在于提出了Fisher随机游走策略，用于计算比较样本的权重。与现有方法不同，该策略能够自适应地调整权重，从而更有效地消除上下文偏差。此外，论文还提出了一种计算上可行的方法，通过 nuisance 权重函数的势表示来计算权重，降低了计算复杂度。

**关键设计**：论文的关键设计包括：1) 使用上下文Bradley-Terry-Luce模型来建模上下文相关的偏好；2) 利用Fisher信息矩阵的逆来指导随机游走，从而确定最优权重；3) 采用半参数有效估计器，保证估计的效率和准确性；4) 使用高斯乘数bootstrap进行多重假设检验，控制familywise error。

## 📊 实验亮点

论文通过数值实验验证了所提出方法的有效性。实验结果表明，该方法在语言模型评估中具有更高的准确性和效率，能够有效消除上下文偏差，并能处理分布偏移问题。具体的性能数据和对比基线在论文中进行了详细的展示，证实了该方法的实用价值。

## 🎯 应用场景

该研究成果可广泛应用于大规模语言模型的评估和选择，尤其是在需要考虑上下文因素的场景下。例如，可以用于评估不同语言模型在特定领域的表现，或者用于比较不同语言模型在处理不同类型用户查询时的偏好。该方法还可以扩展到其他需要进行偏好推断的领域，如推荐系统、信息检索等。

## 📄 摘要（原文）

> Motivated by the need for rigorous and scalable evaluation of large language models, we study contextual preference inference for pairwise comparison functionals of context-dependent preference score functions across domains. Focusing on the contextual Bradley-Terry-Luce model, we develop a semiparametric efficient estimator that automates the debiased estimation through aggregating weighted residual balancing terms across the comparison graph. We show that the efficiency is achieved when the weights are derived from a novel strategy called Fisher random walk. We also propose a computationally feasible method to compute the weights by a potential representation of nuisance weight functions. We show our inference procedure is valid for general score function estimators accommodating the practitioners' need to implement flexible deep learning methods. We extend the procedure to multiple hypothesis testing using a Gaussian multiplier bootstrap that controls familywise error and to distributional shift via a cross-fitted importance-sampling adjustment for target-domain inference. Numerical studies, including language model evaluations under diverse contexts, corroborate the accuracy, efficiency, and practical utility of our method.

