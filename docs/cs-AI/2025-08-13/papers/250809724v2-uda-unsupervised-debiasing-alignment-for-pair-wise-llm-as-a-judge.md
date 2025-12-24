---
layout: default
title: "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge"
---

# UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09724" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09724v2</a>
  <a href="https://arxiv.org/pdf/2508.09724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09724v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09724v2', 'UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang, Guangsheng Bao, Jie Tang

**分类**: cs.AI

**发布日期**: 2025-08-13 (更新: 2025-11-16)

---

## 💡 一句话要点

**提出UDA框架以解决大语言模型评估中的偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无监督学习` `偏见去除` `大语言模型` `Elo评分系统` `模型评估` `成对比较` `一致性对齐`

## 📋 核心要点

1. 现有的成对评估方法容易受到评审偏见的影响，导致不同评审之间的结果不一致和偏斜。
2. 本文提出UDA框架，通过无监督方式动态调整Elo评分系统，减少评审之间的分歧，促进一致性。
3. 实验表明，UDA将评审评分标准差降低了63.4%，并将与人类判断的平均相关性提升了24.7%。

## 📝 摘要（中文）

对大语言模型（LLMs）的成对评估是一种常见的范式，但容易受到偏好偏见的影响，导致不同评审之间的排名不一致。为了解决这一问题，本文首先实证展示了跨模型评估中的显著且异质的偏见。接着，提出了UDA（无监督去偏对齐）框架，通过动态调整Elo评分系统，减少评审之间的分歧。UDA在完全无监督的情况下运行，目标是最小化所有评审的Elo轨迹之间的离散度，从而促使对集体共识的对齐。实验结果表明，UDA显著降低了评审评分的标准差，提升了与人类判断的相关性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型评估中的偏见问题，现有方法在跨模型评估中存在显著的偏见，导致评审之间的结果不一致。

**核心思路**：UDA框架通过无监督方式动态调整Elo评分系统，学习适应性地设置K因子和优化胜率，从而减少评审之间的分歧，促进对集体共识的对齐。

**技术框架**：UDA的整体架构包括一个紧凑的神经网络模块，该模块负责在每次成对比较中调整K因子，并计算胜率。整个过程不依赖于人工标签，完全基于评审的评分轨迹。

**关键创新**：UDA的主要创新在于其无监督的对齐机制，通过最小化Elo轨迹的离散度来实现评审之间的共识，这一方法与传统的有监督学习方法有本质区别。

**关键设计**：在设计中，UDA采用了动态调整的K因子和胜率计算，损失函数旨在最小化评审评分的离散度，网络结构为紧凑型神经网络，以提高计算效率和适应性。

## 📊 实验亮点

实验结果显示，UDA显著降低了评审评分的标准差，最高可达63.4%的降低，同时与人类判断的平均相关性提升了24.7%。此外，UDA还提升了表现较差的评审的评分水平，使其与高质量评审的表现相当，增强了评估系统的整体可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括大语言模型的评估、机器学习模型的比较以及人机交互系统的优化。通过减少评审偏见，UDA能够提升模型评估的稳定性和可重复性，进而提高模型的实际应用价值。未来，UDA可能在多种评估场景中得到广泛应用，促进更公平和可靠的评估体系的建立。

## 📄 摘要（原文）

> Pairwise evaluation of Large Language Models (LLMs) is a common paradigm, but it is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges. To address this, we first empirically demonstrate significant and heterogeneous biases in cross-model evaluations. We then propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. Crucially, UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges. This forces an alignment towards a collective consensus, which serves as an unsupervised proxy for a more stable and reproducible evaluation. In addition, we provide theoretical motivation demonstrating how alignment towards a consensus can reduce aggregate system bias. Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%. Notably, UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem. Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4.

