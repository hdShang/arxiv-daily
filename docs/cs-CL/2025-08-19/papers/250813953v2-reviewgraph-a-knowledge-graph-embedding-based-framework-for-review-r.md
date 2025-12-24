---
layout: default
title: "ReviewGraph: A Knowledge Graph Embedding Based Framework for Review Rating Prediction with Sentiment Features"
---

# ReviewGraph: A Knowledge Graph Embedding Based Framework for Review Rating Prediction with Sentiment Features

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13953" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13953v2</a>
  <a href="https://arxiv.org/pdf/2508.13953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13953v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13953v2', 'ReviewGraph: A Knowledge Graph Embedding Based Framework for Review Rating Prediction with Sentiment Features')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: A. J. W. de Vink, Natalia Amat-Lefort, Lifeng Han

**分类**: cs.CL

**发布日期**: 2025-08-19 (更新: 2025-11-15)

**备注**: Peer-reviewed and published version is in ICKG-2025 (The 16th IEEE International Conference on Knowledge Graphs, November 13-14, 2025, Limassol, Cyprus)

**🔗 代码/项目**: [GITHUB](https://github.com/aaronlifenghan/ReviewGraph)

---

## 💡 一句话要点

**提出ReviewGraph框架以解决酒店客户评价评分预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `情感分析` `评分预测` `机器学习` `图嵌入` `酒店管理` `客户满意度`

## 📋 核心要点

1. 现有方法在客户评价评分预测中缺乏有效的情感分析和知识表示，导致模型性能受限。
2. 论文提出的ReviewGraph框架通过知识图谱嵌入和情感特征相结合，提升了评分预测的准确性和可解释性。
3. 实验结果显示，ReviewGraph在与传统基线和大型语言模型的比较中表现优异，且计算成本更低。

## 📝 摘要（中文）

在酒店行业，理解影响客户评价评分的因素对于提升客户满意度和商业绩效至关重要。本研究提出了ReviewGraph框架，通过提取（主语、谓语、宾语）三元组并关联情感分数，将文本客户评价转化为知识图谱。该框架利用图嵌入（Node2Vec）和情感特征，通过机器学习分类器预测评价评分。我们在HotelRec数据集上将ReviewGraph的性能与传统NLP基线（如词袋模型、TF-IDF和Word2Vec）及大型语言模型（LLMs）进行了比较。结果表明，ReviewGraph在预测性能上与LLMs相当，并在一致性指标（如Cohen's Kappa）上超越了基线，同时在可解释性、可视化探索和与检索增强生成（RAG）系统的潜在集成方面具有额外优势。

## 🔬 方法详解

**问题定义**：本论文旨在解决酒店客户评价评分预测中的情感分析不足和知识表示不充分的问题。现有方法往往依赖于简单的文本特征，导致模型在复杂情感表达上的性能不足。

**核心思路**：论文提出的ReviewGraph框架通过将客户评价转化为知识图谱，提取（主语、谓语、宾语）三元组并关联情感分数，从而实现更丰富的特征表示，提升评分预测的准确性。

**技术框架**：ReviewGraph的整体架构包括三个主要模块：首先，文本预处理和三元组提取；其次，利用Node2Vec进行图嵌入；最后，通过机器学习分类器进行评分预测。

**关键创新**：ReviewGraph的主要创新在于将知识图谱嵌入与情感特征结合，提供了比传统方法更高的可解释性和准确性，同时降低了计算成本。

**关键设计**：在模型设计中，使用Node2Vec进行图嵌入，情感分数通过情感分析工具提取，损失函数采用交叉熵损失，确保模型在评分预测中的有效性。整体架构设计注重模块化，便于后续的扩展和集成。

## 📊 实验亮点

实验结果表明，ReviewGraph在与传统基线（如词袋模型、TF-IDF和Word2Vec）及大型语言模型的比较中，表现出色，尤其在一致性指标Cohen's Kappa上超越了基线，且计算成本显著降低，展示了其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括酒店管理、客户服务和在线评论分析等。通过提升客户评价评分预测的准确性，酒店可以更好地理解客户需求，从而优化服务和提升客户满意度。此外，ReviewGraph的可解释性和可视化能力为决策支持提供了有力工具，未来可与其他智能系统集成，推动行业发展。

## 📄 摘要（原文）

> In the hospitality industry, understanding the factors that drive customer review ratings is critical for improving guest satisfaction and business performance. This work proposes ReviewGraph for Review Rating Prediction (RRP), a novel framework that transforms textual customer reviews into knowledge graphs by extracting (subject, predicate, object) triples and associating sentiment scores. Using graph embeddings (Node2Vec) and sentiment features, the framework predicts review rating scores through machine learning classifiers. We compare ReviewGraph performance with traditional NLP baselines (such as Bag of Words, TF-IDF, and Word2Vec) and large language models (LLMs), evaluating them in the HotelRec dataset. In comparison to the state of the art literature, our proposed model performs similar to their best performing model but with lower computational cost (without ensemble).
>   While ReviewGraph achieves comparable predictive performance to LLMs and outperforms baselines on agreement-based metrics such as Cohen's Kappa, it offers additional advantages in interpretability, visual exploration, and potential integration into Retrieval-Augmented Generation (RAG) systems. This work highlights the potential of graph-based representations for enhancing review analytics and lays the groundwork for future research integrating advanced graph neural networks and fine-tuned LLM-based extraction methods. We will share ReviewGraph output and platform open-sourced on our GitHub page https://github.com/aaronlifenghan/ReviewGraph

