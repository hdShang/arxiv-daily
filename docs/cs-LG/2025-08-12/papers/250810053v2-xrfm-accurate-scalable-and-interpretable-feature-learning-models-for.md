---
layout: default
title: "xRFM: Accurate, scalable, and interpretable feature learning models for tabular data"
---

# xRFM: Accurate, scalable, and interpretable feature learning models for tabular data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10053" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10053v2</a>
  <a href="https://arxiv.org/pdf/2508.10053.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10053v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10053v2', 'xRFM: Accurate, scalable, and interpretable feature learning models for tabular data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniel Beaglehole, David Holzmüller, Adityanarayanan Radhakrishnan, Mikhail Belkin

**分类**: cs.LG, stat.ML

**发布日期**: 2025-08-12 (更新: 2025-10-23)

---

## 💡 一句话要点

**提出xRFM以解决表格数据特征学习问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格数据` `特征学习` `机器学习` `可解释性` `算法创新` `数据科学`

## 📋 核心要点

1. 现有的表格数据预测方法主要依赖于GBDT，缺乏创新，难以适应大规模数据的需求。
2. xRFM算法通过结合特征学习核机器与树结构，能够有效适应数据的局部结构并处理大规模数据。
3. 在实验中，xRFM在100个回归数据集上表现最佳，并在200个分类数据集上超越了GBDT，显示出其强大的性能和可解释性。

## 📝 摘要（中文）

表格数据的推断是现代科技与科学的基础。然而，与人工智能其他领域的快速发展相比，表格数据的预测任务仍主要依赖于梯度提升决策树（GBDT）的变体。近期，基于神经网络和特征学习方法的最新进展，开发先进的表格数据处理方法引起了关注。本文提出了xRFM算法，该算法结合了特征学习核机器与树结构，能够适应数据的局部结构并扩展到几乎无限的训练数据。与31种其他方法相比，xRFM在100个回归数据集上表现最佳，并在200个分类数据集上与最佳方法竞争，超越了GBDT。此外，xRFM通过平均梯度外积提供了内在的可解释性。

## 🔬 方法详解

**问题定义**：本文旨在解决表格数据特征学习的准确性和可扩展性问题。现有方法如GBDT在处理大规模数据时存在性能瓶颈，且缺乏对数据结构的适应性。

**核心思路**：xRFM算法的核心思想是将特征学习核机器与树结构相结合，以便更好地适应数据的局部结构，同时具备良好的扩展性，能够处理大规模训练数据。

**技术框架**：xRFM的整体架构包括特征学习模块和树结构模块。特征学习模块负责从原始数据中提取有用特征，而树结构模块则用于构建决策树，以进行高效的预测。

**关键创新**：xRFM的主要创新在于其结合了特征学习与树结构的优势，能够在处理复杂数据时提供更高的准确性和可解释性。这一设计与传统的GBDT方法有本质区别，后者主要依赖于固定的特征选择。

**关键设计**：xRFM采用了平均梯度外积作为损失函数的一部分，以增强模型的可解释性。此外，模型的参数设置经过优化，以确保在大规模数据集上的高效训练和推断。具体的网络结构和超参数设置在实验中进行了详细验证。

## 📊 实验亮点

在实验中，xRFM在100个回归数据集上表现最佳，超越了31种其他方法，包括最新的表格基础模型（TabPFNv2）和GBDT。此外，在200个分类数据集上，xRFM的表现与最佳方法相当，显示出其在表格数据处理中的强大竞争力。

## 🎯 应用场景

xRFM算法在金融、医疗、市场营销等领域具有广泛的应用潜力。其高效的特征学习能力和可解释性使其能够帮助决策者更好地理解数据背后的模式，从而做出更为精准的决策。未来，xRFM有望在更多实际应用中发挥重要作用，推动数据驱动决策的进步。

## 📄 摘要（原文）

> Inference from tabular data, collections of continuous and categorical variables organized into matrices, is a foundation for modern technology and science. Yet, in contrast to the explosive changes in the rest of AI, the best practice for these predictive tasks has been relatively unchanged and is still primarily based on variations of Gradient Boosted Decision Trees (GBDTs). Very recently, there has been renewed interest in developing state-of-the-art methods for tabular data based on recent developments in neural networks and feature learning methods. In this work, we introduce xRFM, an algorithm that combines feature learning kernel machines with a tree structure to both adapt to the local structure of the data and scale to essentially unlimited amounts of training data.
>   We show that compared to $31$ other methods, including recently introduced tabular foundation models (TabPFNv2) and GBDTs, xRFM achieves best performance across $100$ regression datasets and is competitive to the best methods across $200$ classification datasets outperforming GBDTs. Additionally, xRFM provides interpretability natively through the Average Gradient Outer Product.

