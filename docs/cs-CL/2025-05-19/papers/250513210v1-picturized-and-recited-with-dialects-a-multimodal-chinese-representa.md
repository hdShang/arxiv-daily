---
layout: default
title: Picturized and Recited with Dialects: A Multimodal Chinese Representation Framework for Sentiment Analysis of Classical Chinese Poetry
---

# Picturized and Recited with Dialects: A Multimodal Chinese Representation Framework for Sentiment Analysis of Classical Chinese Poetry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13210" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13210v1</a>
  <a href="https://arxiv.org/pdf/2505.13210.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13210v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13210v1', 'Picturized and Recited with Dialects: A Multimodal Chinese Representation Framework for Sentiment Analysis of Classical Chinese Poetry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaocong Du, Haoyu Pei, Haipeng Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出多模态框架以提升古典诗词情感分析效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `古典诗词` `情感分析` `多模态融合` `方言音频` `视觉特征` `大语言模型` `对比学习`

## 📋 核心要点

1. 现有方法主要基于文本进行情感分析，忽视了古典诗词的韵律和视觉特征，导致分析效果不足。
2. 本文提出了一种多模态框架，结合音频、视觉和文本特征，增强古典诗词的情感分析能力。
3. 实验结果显示，框架在两个公共数据集上准确率提升至少2.51%，宏观F1提升1.63%，表现优于现有方法。

## 📝 摘要（中文）

古典汉诗是中国文学的重要组成部分，承载着深厚的情感共鸣。现有研究主要基于文本意义进行情感分析，忽视了诗词固有的韵律和视觉特征，尤其是在朗诵和配以中国画的情况下。本文提出了一种增强方言的多模态框架，用于古典汉诗的情感分析。我们从诗词中提取句子级音频特征，并结合多种方言音频，丰富了音韵表现。此外，我们生成句子级视觉特征，并通过多模态对比表示学习将这些特征与通过大语言模型翻译增强的文本特征融合。我们的框架在两个公共数据集上超越了现有最先进的方法，准确率提升至少2.51%，宏观F1提升1.63%。我们开源代码以促进该领域的研究，并为一般多模态汉语表示提供见解。

## 🔬 方法详解

**问题定义**：本研究旨在解决古典汉诗情感分析中对韵律和视觉特征的忽视，现有方法未能充分利用这些信息，导致情感识别效果不佳。

**核心思路**：我们提出的框架通过引入多模态特征，包括音频、视觉和文本，来增强情感分析的准确性，尤其是通过方言音频保留古汉语的音韵特征。

**技术框架**：整体架构包括音频特征提取、视觉特征生成和文本特征增强三个主要模块。音频模块提取句子级音频特征，视觉模块生成与诗词相关的视觉特征，文本模块通过大语言模型进行翻译和增强。

**关键创新**：本研究的创新点在于将方言音频与视觉特征结合，形成一个多模态对比表示学习框架，这一设计显著提升了情感分析的效果。

**关键设计**：在技术细节上，我们采用了特定的损失函数来优化多模态特征的融合，并设计了适应性强的网络结构，以便更好地处理不同模态之间的信息交互。

## 📊 实验亮点

实验结果表明，提出的多模态框架在两个公共数据集上均超越了现有最先进的方法，准确率提升至少2.51%，宏观F1提升1.63%。这些结果表明该框架在情感分析任务中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括古典文学的情感分析、文化遗产的数字化保护以及教育领域的诗词教学。通过多模态分析，能够更深入地理解古典诗词的情感内涵，促进文化传播与交流。未来，该框架还可扩展至其他语言和文化的情感分析研究。

## 📄 摘要（原文）

> Classical Chinese poetry is a vital and enduring part of Chinese literature, conveying profound emotional resonance. Existing studies analyze sentiment based on textual meanings, overlooking the unique rhythmic and visual features inherent in poetry,especially since it is often recited and accompanied by Chinese paintings. In this work, we propose a dialect-enhanced multimodal framework for classical Chinese poetry sentiment analysis. We extract sentence-level audio features from the poetry and incorporate audio from multiple dialects,which may retain regional ancient Chinese phonetic features, enriching the phonetic representation. Additionally, we generate sentence-level visual features, and the multimodal features are fused with textual features enhanced by LLM translation through multimodal contrastive representation learning. Our framework outperforms state-of-the-art methods on two public datasets, achieving at least 2.51% improvement in accuracy and 1.63% in macro F1. We open-source the code to facilitate research in this area and provide insights for general multimodal Chinese representation.

