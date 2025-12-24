---
layout: default
title: "Prediction is not Explanation: Revisiting the Explanatory Capacity of Mapping Embeddings"
---

# Prediction is not Explanation: Revisiting the Explanatory Capacity of Mapping Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13729" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13729v1</a>
  <a href="https://arxiv.org/pdf/2508.13729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13729v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13729v1', 'Prediction is not Explanation: Revisiting the Explanatory Capacity of Mapping Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanna Herasimchyk, Alhassan Abdelhalim, Sören Laue, Michaela Regneri

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-19

**备注**: 10 pages, 6 Figures. Published at ECAI 2025 in a version without the Appendix

---

## 💡 一句话要点

**挑战传统假设，揭示词嵌入的解释能力局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `词嵌入` `可解释性` `深度学习` `语义特征` `人工智能`

## 📋 核心要点

1. 现有方法假设词嵌入能够准确预测语义特征，但这一假设存在局限性。
2. 本文通过实验证明，预测准确性并不等同于真正的特征可解释性，提出了新的分析视角。
3. 研究结果显示，词嵌入的映射主要反映几何相似性，而非真实的语义知识，挑战了传统理解。

## 📝 摘要（中文）

理解深度学习模型中隐含的知识对于提升人工智能系统的可解释性至关重要。本文探讨了用于解释词嵌入知识的常用方法，这些方法通常将嵌入映射到人类可解释的语义特征集合上。以往研究假设，从词嵌入准确预测这些语义特征意味着嵌入中包含相应知识。我们质疑这一假设，表明仅凭预测准确性并不能可靠地指示真正的特征可解释性。我们的研究表明，这些方法甚至可以成功预测随机信息，结果主要由算法上限决定，而非词嵌入中的有意义语义表示。因此，仅基于预测性能的比较并不能可靠地指示哪个数据集更好地被词嵌入捕捉。我们的分析表明，这种映射主要反映了向量空间中的几何相似性，而非语义属性的真实出现。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在解释词嵌入知识时的局限性，尤其是预测准确性与真正可解释性之间的假设关系。现有方法往往依赖于预测性能来评估嵌入的知识内容，但缺乏对其有效性的深入分析。

**核心思路**：论文的核心思路是通过实验证明，预测准确性并不能可靠地指示词嵌入的特征可解释性。通过对比随机信息的预测结果，揭示了现有方法的不足。

**技术框架**：整体架构包括数据集的选择、特征映射方法的实施以及预测性能的评估。主要模块包括词嵌入生成、特征映射算法和性能评估机制。

**关键创新**：最重要的技术创新在于挑战了传统的假设，强调预测准确性与真正语义知识之间的区别，提出了新的评估标准。与现有方法的本质区别在于不再单纯依赖预测性能作为可解释性的指标。

**关键设计**：在实验中，采用了多种数据集和特征映射方法，设计了相应的损失函数和评估指标，以确保对比的公平性和结果的可靠性。

## 📊 实验亮点

实验结果表明，现有的特征映射方法在预测随机信息时也能取得高准确性，显示出这些方法的局限性。通过对比不同数据集的预测性能，发现仅依赖预测结果无法有效评估词嵌入的语义捕捉能力，强调了几何相似性在结果中的主导作用。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和信息检索等。通过提升对词嵌入的理解，可以改善模型的可解释性，进而增强用户对AI系统的信任和接受度。未来，研究成果可能推动更透明的AI系统设计，促进人机协作的有效性。

## 📄 摘要（原文）

> Understanding what knowledge is implicitly encoded in deep learning models is essential for improving the interpretability of AI systems. This paper examines common methods to explain the knowledge encoded in word embeddings, which are core elements of large language models (LLMs). These methods typically involve mapping embeddings onto collections of human-interpretable semantic features, known as feature norms. Prior work assumes that accurately predicting these semantic features from the word embeddings implies that the embeddings contain the corresponding knowledge. We challenge this assumption by demonstrating that prediction accuracy alone does not reliably indicate genuine feature-based interpretability.
>   We show that these methods can successfully predict even random information, concluding that the results are predominantly determined by an algorithmic upper bound rather than meaningful semantic representation in the word embeddings. Consequently, comparisons between datasets based solely on prediction performance do not reliably indicate which dataset is better captured by the word embeddings. Our analysis illustrates that such mappings primarily reflect geometric similarity within vector spaces rather than indicating the genuine emergence of semantic properties.

