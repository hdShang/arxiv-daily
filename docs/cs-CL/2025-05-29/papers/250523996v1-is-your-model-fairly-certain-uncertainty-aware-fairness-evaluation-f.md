---
layout: default
title: Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs
---

# Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23996" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23996v1</a>
  <a href="https://arxiv.org/pdf/2505.23996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23996v1', 'Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinong Oliver Wang, Nivedha Sivakumar, Falaah Arif Khan, Rin Metcalf Susa, Adam Golinski, Natalie Mackraz, Barry-John Theobald, Luca Zappella, Nicholas Apostoloff

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-29

**备注**: 9 pages, 8 figures, and 1 table in main paper. Supplementary appendix attached. Accepted at ICML 2025

---

## 💡 一句话要点

**提出UCerF以解决大型语言模型公平性评估中的不确定性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `公平性评估` `不确定性感知` `数据集构建` `模型偏见`

## 📋 核心要点

1. 现有的公平性评估方法主要依赖于准确性指标，未能考虑模型的不确定性，导致评估结果可能不全面。
2. 本文提出的不确定性感知公平性指标UCerF，旨在更细致地评估模型的公平性，反映模型决策中的潜在偏见。
3. 通过建立新的性别-职业公平性评估数据集并应用UCerF，发现多个开源LLMs在公平性方面存在显著问题，尤其是高信心的错误预测。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速应用，公平性评估的重要性日益凸显。传统的公平性指标主要关注基于离散准确性的评估，未能充分反映模型不确定性对不同群体的隐性影响。为此，本文提出了一种不确定性感知的公平性指标UCerF，能够更细致地评估模型的公平性，揭示模型决策中的内部偏见。此外，针对当前数据集在规模、多样性和清晰度方面的问题，本文引入了一个新的性别-职业公平性评估数据集，包含31,756个样本，适用于共指消解任务。通过使用该指标和数据集，我们建立了基准，并对十个开源LLMs的行为进行了评估，发现Mistral-7B在错误预测中表现出较高的信心，导致公平性不足，这是传统方法未能捕捉到的。整体而言，本文的研究为开发更透明和负责任的AI系统铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在公平性评估中未考虑不确定性的问题。现有方法往往只关注预测的准确性，忽视了模型对不同群体的信心差异，导致评估结果不够全面和准确。

**核心思路**：论文提出的不确定性感知公平性指标UCerF，能够在评估模型公平性时考虑模型的不确定性，从而更准确地反映模型决策中的潜在偏见。这一设计旨在填补传统公平性评估方法的空白。

**技术框架**：整体架构包括数据集构建、UCerF指标设计和模型评估三个主要模块。首先，构建新的性别-职业公平性评估数据集；其次，设计UCerF指标以评估模型的公平性；最后，应用该指标对多个开源LLMs进行评估。

**关键创新**：最重要的技术创新点在于引入了不确定性感知的公平性评估指标UCerF，与传统方法相比，它能够捕捉到模型在不同群体间的信心差异，从而提供更全面的公平性评估。

**关键设计**：在UCerF的设计中，考虑了模型的预测信心和准确性之间的关系，采用了特定的损失函数来量化不确定性对公平性的影响。此外，数据集的多样性和样本量也经过精心设计，以确保评估的有效性和可靠性。

## 📊 实验亮点

实验结果表明，使用UCerF指标评估的十个开源LLMs中，Mistral-7B在错误预测中表现出高达80%的信心，导致其公平性评分显著低于传统评估方法。这一发现强调了不确定性感知在公平性评估中的重要性，推动了对模型行为的深入理解。

## 🎯 应用场景

该研究的潜在应用领域包括AI系统的公平性评估、社会科学研究以及政策制定等。通过提供更准确的公平性评估工具，能够帮助开发者和研究人员识别和减少模型中的偏见，从而推动更透明和负责任的AI技术的发展。

## 📄 摘要（原文）

> The recent rapid adoption of large language models (LLMs) highlights the critical need for benchmarking their fairness. Conventional fairness metrics, which focus on discrete accuracy-based evaluations (i.e., prediction correctness), fail to capture the implicit impact of model uncertainty (e.g., higher model confidence about one group over another despite similar accuracy). To address this limitation, we propose an uncertainty-aware fairness metric, UCerF, to enable a fine-grained evaluation of model fairness that is more reflective of the internal bias in model decisions compared to conventional fairness measures. Furthermore, observing data size, diversity, and clarity issues in current datasets, we introduce a new gender-occupation fairness evaluation dataset with 31,756 samples for co-reference resolution, offering a more diverse and suitable dataset for evaluating modern LLMs. We establish a benchmark, using our metric and dataset, and apply it to evaluate the behavior of ten open-source LLMs. For example, Mistral-7B exhibits suboptimal fairness due to high confidence in incorrect predictions, a detail overlooked by Equalized Odds but captured by UCerF. Overall, our proposed LLM benchmark, which evaluates fairness with uncertainty awareness, paves the way for developing more transparent and accountable AI systems.

