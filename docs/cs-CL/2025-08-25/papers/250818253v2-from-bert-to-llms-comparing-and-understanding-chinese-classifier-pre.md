---
layout: default
title: "From BERT to LLMs: Comparing and Understanding Chinese Classifier Prediction in Language Models"
---

# From BERT to LLMs: Comparing and Understanding Chinese Classifier Prediction in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18253" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18253v2</a>
  <a href="https://arxiv.org/pdf/2508.18253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18253v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18253v2', 'From BERT to LLMs: Comparing and Understanding Chinese Classifier Prediction in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziqi Zhang, Jianfei Ma, Emmanuele Chersoni, Jieshun You, Zhaoxin Feng

**分类**: cs.CL

**发布日期**: 2025-08-25 (更新: 2025-11-02)

---

## 💡 一句话要点

**比较BERT与LLMs在中文分类器预测中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `中文分类器` `大型语言模型` `BERT` `自然语言处理` `微调技术` `注意力机制` `教育应用`

## 📋 核心要点

1. 核心问题：现有研究未充分探讨大型语言模型在中文分类器预测中的能力，导致教育应用中的潜在问题。
2. 方法要点：通过多种掩蔽策略评估LLMs的预测能力，并探索微调以提升其分类器性能。
3. 实验或效果：研究发现LLMs的表现不如BERT，且预测效果依赖于后续名词的信息。

## 📝 摘要（中文）

分类器是中文语言的重要特征，其正确预测对教育应用至关重要。然而，现有文献中对流行的大型语言模型（LLMs）在中文分类器知识方面的能力探讨较少。为此，本文采用多种掩蔽策略评估LLMs的内在能力、不同句子元素的贡献以及注意力机制在预测中的作用。此外，本文还探索了对LLMs进行微调以提升分类器性能。研究发现，LLMs的表现不如BERT，即使经过微调，预测效果仍然受限于后续名词的信息，这也解释了具有双向注意力机制的模型（如BERT）的优势。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在中文分类器预测中的能力不足问题。现有方法未能充分评估LLMs在这一领域的表现，导致教育应用中的潜在挑战。

**核心思路**：通过多种掩蔽策略，评估LLMs的内在能力及其注意力机制的工作原理，同时探索微调方法以提升分类器性能。这种设计旨在揭示不同句子元素对预测的贡献。

**技术框架**：研究采用了多种掩蔽策略，分为评估LLMs的基本能力、分析句子元素的贡献和微调模型三个主要阶段。每个阶段都通过实验验证模型的表现。

**关键创新**：本文的创新在于系统性地比较了BERT与LLMs在中文分类器预测中的表现，揭示了后续名词信息对预测的重要性，强调了双向注意力机制的优势。

**关键设计**：在实验中，采用了多种掩蔽策略和微调技术，关注不同句子元素的贡献，确保模型在训练和评估阶段的有效性。

## 📊 实验亮点

实验结果显示，LLMs在中文分类器预测中的表现不如BERT，且即使经过微调，性能提升仍有限。具体而言，后续名词的信息对预测效果有显著影响，强调了双向注意力机制的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、语言学习工具和智能问答系统。通过提升LLMs在中文分类器预测中的表现，可以为教育应用提供更准确的语言理解和生成能力，从而改善学习效果和用户体验。

## 📄 摘要（原文）

> Classifiers are an important and defining feature of the Chinese language, and their correct prediction is key to numerous educational applications. Yet, whether the most popular Large Language Models (LLMs) possess proper knowledge the Chinese classifiers is an issue that has largely remain unexplored in the Natural Language Processing (NLP) literature.
>   To address such a question, we employ various masking strategies to evaluate the LLMs' intrinsic ability, the contribution of different sentence elements, and the working of the attention mechanisms during prediction. Besides, we explore fine-tuning for LLMs to enhance the classifier performance.
>   Our findings reveal that LLMs perform worse than BERT, even with fine-tuning. The prediction, as expected, greatly benefits from the information about the following noun, which also explains the advantage of models with a bidirectional attention mechanism such as BERT.

