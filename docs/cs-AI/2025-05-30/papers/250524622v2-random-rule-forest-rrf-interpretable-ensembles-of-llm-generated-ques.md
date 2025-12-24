---
layout: default
title: Random Rule Forest (RRF): Interpretable Ensembles of LLM-Generated Questions for Predicting Startup Success
---

# Random Rule Forest (RRF): Interpretable Ensembles of LLM-Generated Questions for Predicting Startup Success

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24622" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24622v2</a>
  <a href="https://arxiv.org/pdf/2505.24622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24622v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24622v2', 'Random Rule Forest (RRF): Interpretable Ensembles of LLM-Generated Questions for Predicting Startup Success')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ben Griffin, Diego Vidaurre, Ugur Koyluoglu, Joseph Ternasky, Fuat Alican, Yigit Ihlamur

**分类**: cs.AI, cs.LG

**发布日期**: 2025-05-30 (更新: 2025-09-15)

**备注**: 13 pages including appendix, 4 figures

---

## 💡 一句话要点

**提出随机规则森林以解决创业成功预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `创业成功预测` `随机规则森林` `大型语言模型` `可解释性` `集成学习` `风险投资` `人机协作`

## 📋 核心要点

1. 现有方法在预测创业成功等稀有结果时，往往缺乏准确性和可解释性。
2. 本文提出随机规则森林（RRF），通过生成自然语言问题作为弱学习器，结合投票机制形成强预测器。
3. 在9892名创始人的数据集上，RRF实现了6.9倍的性能提升，添加专家问题后提升至8倍，展示了人机协作的优势。

## 📝 摘要（中文）

预测创业成功等稀有结果是风险投资的核心，要求模型既准确又可解释。本文提出随机规则森林（RRF），一种轻量级集成方法，利用大型语言模型（LLM）生成简单的自然语言是/否问题。每个问题作为弱学习器，其响应通过基于阈值的投票规则组合，形成强大且可解释的预测器。在9892名创始人的数据集上，RRF在保留数据上实现了6.9倍的提升；添加专家设计的问题将这一提升提高到8倍，突显了人类与LLM协作的价值。与三种LLM架构的零样本和少样本基线相比，RRF的F0.5达到了0.121，而最佳基线为0.086（绝对提升0.035，相对提升41%）。通过结合LLM的创造力与集成学习的严谨性，RRF提供了适合高风险领域决策的可解释、高精度预测。

## 🔬 方法详解

**问题定义**：本文旨在解决创业成功预测这一稀有结果的挑战，现有方法往往缺乏准确性和可解释性，难以满足风险投资的需求。

**核心思路**：随机规则森林（RRF）通过利用大型语言模型生成简单的是/否问题，将这些问题作为弱学习器，结合其响应形成强预测器，旨在提高预测的准确性和可解释性。

**技术框架**：RRF的整体架构包括三个主要模块：首先，使用LLM生成自然语言问题；其次，将这些问题作为输入，进行响应收集；最后，采用基于阈值的投票机制整合响应，形成最终的预测结果。

**关键创新**：RRF的主要创新在于将LLM生成的自然语言问题与集成学习相结合，形成了一种新的预测框架，这与传统的机器学习方法有本质区别，后者通常依赖于固定特征和复杂模型。

**关键设计**：在设计中，RRF采用了阈值投票机制来整合多个弱学习器的输出，确保了模型的可解释性。此外，专家设计的问题进一步提升了模型的性能，展示了人类与LLM的有效协作。

## 📊 实验亮点

在实验中，RRF在9892名创始人的数据集上实现了6.9倍的性能提升，相较于随机基线，添加专家设计的问题后提升至8倍。与零样本和少样本基线相比，RRF的F0.5达到了0.121，较最佳基线提升了0.035，表现出41%的相对提升，展示了其强大的预测能力。

## 🎯 应用场景

该研究的潜在应用领域包括风险投资、创业评估和商业决策等高风险领域。通过提供可解释的高精度预测，RRF能够帮助投资者更好地评估创业项目的成功概率，从而优化投资决策，降低风险。未来，RRF的框架也可扩展至其他领域，如医疗、金融等，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> Predicting rare outcomes such as startup success is central to venture capital, demanding models that are both accurate and interpretable. We introduce Random Rule Forest (RRF), a lightweight ensemble method that uses a large language model (LLM) to generate simple YES/NO questions in natural language. Each question functions as a weak learner, and their responses are combined using a threshold-based voting rule to form a strong, interpretable predictor.
>   Applied to a dataset of 9,892 founders, RRF achieves a 6.9x improvement over a random baseline on held-out data; adding expert-crafted questions lifts this to 8x and highlights the value of human-LLM collaboration. Compared with zero- and few-shot baselines across three LLM architectures, RRF attains an F0.5 of 0.121, versus 0.086 for the best baseline (+0.035 absolute, +41% relative). By combining the creativity of LLMs with the rigor of ensemble learning, RRF delivers interpretable, high-precision predictions suitable for decision-making in high-stakes domains.

