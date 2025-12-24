---
layout: default
title: "TRUST: Transparent, Robust and Ultra-Sparse Trees"
---

# TRUST: Transparent, Robust and Ultra-Sparse Trees

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15791" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15791v1</a>
  <a href="https://arxiv.org/pdf/2506.15791.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15791v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15791v1', 'TRUST: Transparent, Robust and Ultra-Sparse Trees')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Albert Dorador

**分类**: stat.ME, cs.AI, cs.LG, stat.ML

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出TRUST以解决回归树模型的准确性与可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `回归树` `可解释性` `随机森林` `机器学习` `大型语言模型` `模型透明度` `数据分析`

## 📋 核心要点

1. 现有的回归树模型在可解释性上表现良好，但在预测准确性上往往不及随机森林等复杂模型。
2. TRUST模型通过结合随机森林的准确性与浅层决策树的可解释性，提供了一种新的回归树解决方案。
3. 实验结果表明，TRUST在多个基准数据集上超越了传统可解释模型，并在准确性和可解释性上优于M5'模型。

## 📝 摘要（中文）

分段常数回归树因其可解释性而受到广泛欢迎，但在预测准确性上常常落后于随机森林等黑箱模型。本文提出了一种新颖的回归树模型TRUST（透明、稳健和超稀疏树），它结合了随机森林的准确性与浅层决策树和稀疏线性模型的可解释性。TRUST通过利用大型语言模型生成量身定制的用户友好解释，进一步增强了透明度。在对合成和真实世界基准数据集的广泛验证中，TRUST在预测准确性上始终优于其他可解释模型，包括CART、Lasso和Node Harvest，同时与随机森林的准确性相匹配，并在准确性和可解释性上显著超越了概念上相关的成熟模型M5'。

## 🔬 方法详解

**问题定义**：本文旨在解决现有回归树模型在预测准确性上不及黑箱模型的问题，尤其是如何在保持可解释性的同时提升模型性能。

**核心思路**：TRUST通过结合随机森林的高准确性与浅层决策树的可解释性，设计了一种新型回归树模型，并利用大型语言模型生成用户友好的解释，以增强模型的透明度。

**技术框架**：TRUST的整体架构包括数据预处理、模型训练和解释生成三个主要模块。首先，对输入数据进行预处理，然后训练回归树模型，最后利用大型语言模型生成解释。

**关键创新**：TRUST的主要创新在于其结合了高效的回归树结构与大型语言模型生成的解释，使得模型在保持高准确性的同时，具备良好的可解释性。这与传统的回归树模型有本质区别。

**关键设计**：在模型设计中，TRUST采用了稀疏线性模型的思想，优化了树的结构，并在损失函数中引入了可解释性相关的约束，以确保模型在准确性与可解释性之间的平衡。

## 📊 实验亮点

实验结果显示，TRUST在多个基准数据集上均优于CART、Lasso和Node Harvest等可解释模型，同时在准确性上与随机森林持平。与成熟模型M5'相比，TRUST在准确性和可解释性上均有显著提升，展示了其在实际应用中的优势。

## 🎯 应用场景

TRUST模型在金融、医疗和市场分析等领域具有广泛的应用潜力。其高准确性和良好的可解释性使得决策者能够更好地理解模型的预测结果，从而在实际应用中做出更为合理的决策。未来，该模型可能会推动可解释人工智能的发展，促进各行业对透明模型的需求。

## 📄 摘要（原文）

> Piecewise-constant regression trees remain popular for their interpretability, yet often lag behind black-box models like Random Forest in predictive accuracy. In this work, we introduce TRUST (Transparent, Robust, and Ultra-Sparse Trees), a novel regression tree model that combines the accuracy of Random Forests with the interpretability of shallow decision trees and sparse linear models. TRUST further enhances transparency by leveraging Large Language Models to generate tailored, user-friendly explanations. Extensive validation on synthetic and real-world benchmark datasets demonstrates that TRUST consistently outperforms other interpretable models -- including CART, Lasso, and Node Harvest -- in predictive accuracy, while matching the accuracy of Random Forest and offering substantial gains in both accuracy and interpretability over M5', a well-established model that is conceptually related.

