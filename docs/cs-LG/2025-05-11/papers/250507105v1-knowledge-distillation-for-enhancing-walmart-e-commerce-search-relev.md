---
layout: default
title: Knowledge Distillation for Enhancing Walmart E-commerce Search Relevance Using Large Language Models
---

# Knowledge Distillation for Enhancing Walmart E-commerce Search Relevance Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07105" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07105v1</a>
  <a href="https://arxiv.org/pdf/2505.07105.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07105v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07105v1', 'Knowledge Distillation for Enhancing Walmart E-commerce Search Relevance Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongwei Shang, Nguyen Vo, Nitin Yadav, Tian Zhang, Ajit Puthenputhussery, Xunfan Cai, Shuyi Chen, Prijith Chandran, Changsung Kang

**分类**: cs.IR, cs.LG

**发布日期**: 2025-05-11

**备注**: 9 pages, published at WWWW'25

**期刊**: The Web Conference 2025

**DOI**: [10.1145/3701716.3715242](https://doi.org/10.1145/3701716.3715242)

---

## 💡 一句话要点

**提出知识蒸馏方法以提升沃尔玛电商搜索相关性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识蒸馏` `电商搜索` `大型语言模型` `深度学习` `模型优化` `用户体验` `相关性匹配`

## 📋 核心要点

1. 现有方法在电商搜索中难以实时部署大型语言模型，导致搜索结果相关性不足。
2. 论文提出通过知识蒸馏将高性能的LLM转化为低延迟的学生模型，以满足生产系统的需求。
3. 实验表明，学生模型在增强数据集上训练后，性能持续提升，最终在某些情况下超越教师模型。

## 📝 摘要（中文）

确保电商搜索结果与用户查询相关性至关重要。深度学习模型在搜索任务中的相关性匹配中得到了广泛应用。尽管大型语言模型（LLMs）具有优越的排名能力，但由于高延迟要求，实时系统中部署LLMs面临挑战。为此，本文提出了一种新颖的框架，将高性能的LLM蒸馏为更高效、低延迟的学生模型。通过生成未标记数据并用教师模型预测进行标注，显著扩展学生模型的数据集。实验结果表明，随着增强训练数据的增加，学生模型的性能持续提升，甚至在足够的数据下超越教师模型。该学生模型已成功在Walmart.com的生产环境中部署，取得了显著的正向指标。

## 🔬 方法详解

**问题定义**：本文旨在解决电商搜索中大型语言模型（LLMs）高延迟的问题，现有方法难以在实时系统中有效部署，影响搜索结果的相关性。

**核心思路**：通过知识蒸馏，将高性能的LLM转化为一个更高效的学生模型，使其在保持较低延迟的同时，仍能利用教师模型的强大排名能力。

**技术框架**：整体框架包括两个主要阶段：首先训练教师模型作为分类模型，使用软目标进行训练；然后训练学生模型，利用均方误差损失捕捉产品对之间的相关性边际。此外，通过生成未标记数据并用教师模型的预测进行标注，显著扩展学生模型的数据集。

**关键创新**：最重要的创新在于通过生成未标记数据并进行标注，显著扩展了学生模型的训练数据集，使其在性能上超越教师模型，这是与现有方法的本质区别。

**关键设计**：在损失函数上，学生模型使用均方误差损失来优化相关性边际；网络结构方面，学生模型设计为更轻量级，以适应低延迟的需求。

## 📊 实验亮点

实验结果显示，随着增强训练数据的增加，学生模型的性能持续提升，最终在某些情况下超越了教师模型。具体而言，学生模型在生产环境中部署后，相关性指标显著改善，提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

该研究的潜在应用领域包括电商平台的搜索引擎优化、推荐系统等。通过提升搜索结果的相关性，能够显著改善用户体验，增加用户粘性和购买转化率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Ensuring the products displayed in e-commerce search results are relevant to users queries is crucial for improving the user experience. With their advanced semantic understanding, deep learning models have been widely used for relevance matching in search tasks. While large language models (LLMs) offer superior ranking capabilities, it is challenging to deploy LLMs in real-time systems due to the high-latency requirements. To leverage the ranking power of LLMs while meeting the low-latency demands of production systems, we propose a novel framework that distills a high performing LLM into a more efficient, low-latency student model. To help the student model learn more effectively from the teacher model, we first train the teacher LLM as a classification model with soft targets. Then, we train the student model to capture the relevance margin between pairs of products for a given query using mean squared error loss. Instead of using the same training data as the teacher model, we significantly expand the student model dataset by generating unlabeled data and labeling it with the teacher model predictions. Experimental results show that the student model performance continues to improve as the size of the augmented training data increases. In fact, with enough augmented data, the student model can outperform the teacher model. The student model has been successfully deployed in production at Walmart.com with significantly positive metrics.

