---
layout: default
title: LLMPR: A Novel LLM-Driven Transfer Learning based Petition Ranking Model
---

# LLMPR: A Novel LLM-Driven Transfer Learning based Petition Ranking Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21689" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21689v1</a>
  <a href="https://arxiv.org/pdf/2505.21689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21689v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21689v1', 'LLMPR: A Novel LLM-Driven Transfer Learning based Petition Ranking Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Avijit Gayen, Somyajit Chakraborty, Mainak Sen, Soham Paul, Angshuman Jana

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-27

**备注**: 28 pages, 5 figures, journal paper, submitted to AI and Law

---

## 💡 一句话要点

**提出LLMPR以解决印度司法案件积压问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律申请排序` `迁移学习` `机器学习` `大型语言模型` `司法效率` `自动化系统` `特征提取`

## 📋 核心要点

1. 现有的手动申请优先级排序方法效率低下，容易受到主观偏见影响，导致司法延误。
2. 本文提出LLMPR框架，结合迁移学习和机器学习，自动化地为法律申请分配优先级。
3. 实验结果显示，随机森林和决策树模型的准确率超过99%，显著提升了法律申请的排序效率。

## 📝 摘要（中文）

随着未解决法律案件的持续增加，尤其是在印度司法系统中，及时交付正义的能力受到严重影响。手动优先级排序方法往往效率低下且容易受到主观偏见的影响，从而加剧了延误。为了解决这一问题，本文提出了LLMPR（基于大型语言模型的申请排序），这是一个自动化框架，利用迁移学习和机器学习根据法律申请的上下文紧迫性分配优先级。通过处理包含7593个标注申请的ILDC数据集，提取非结构化法律文本的特征，结合定量指标训练多种机器学习模型。实验结果表明，随机森林和决策树模型的表现优越，准确率超过99%。

## 🔬 方法详解

**问题定义**：本文旨在解决印度司法系统中未解决法律案件的积压问题。现有的手动排序方法效率低下，且容易受到主观因素的影响，导致案件处理延误。

**核心思路**：提出LLMPR框架，利用大型语言模型和迁移学习技术，自动化处理法律申请的优先级排序，以提高效率和公平性。

**技术框架**：整体架构包括数据预处理、特征提取、模型训练和评估四个主要模块。首先，处理ILDC数据集中的非结构化法律文本，然后提取特征并结合定量指标，最后训练多种机器学习模型进行排序。

**关键创新**：最重要的创新在于将大型语言模型与传统的机器学习方法结合，利用文本嵌入和数值特征共同提升排序效果。这一方法与现有的手动排序方法有本质区别。

**关键设计**：在模型训练中，采用了DistilBERT、LegalBERT和MiniLM等嵌入技术，并结合了间隔天数、排名分数和字数等定量指标，训练了随机森林、决策树、XGBoost等多种模型。

## 📊 实验亮点

实验结果表明，随机森林和决策树模型的准确率超过99%，Spearman等级相关性达到0.99。仅使用数值特征的模型也取得了接近最优的排序结果（R2 = 0.988），而LLM嵌入的增益相对较小，显示出数值特征在排序中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括法律事务管理、司法系统优化和智能法律服务。通过自动化申请排序，能够有效减少案件积压，提高司法效率，进而提升公众对法律系统的信任和满意度。未来，该技术还可扩展至其他国家的法律系统，推动全球司法改革。

## 📄 摘要（原文）

> The persistent accumulation of unresolved legal cases, especially within the Indian judiciary, significantly hampers the timely delivery of justice. Manual methods of prioritizing petitions are often prone to inefficiencies and subjective biases further exacerbating delays. To address this issue, we propose LLMPR (Large Language Model-based Petition Ranking), an automated framework that utilizes transfer learning and machine learning to assign priority rankings to legal petitions based on their contextual urgency. Leveraging the ILDC dataset comprising 7,593 annotated petitions, we process unstructured legal text and extract features through various embedding techniques, including DistilBERT, LegalBERT, and MiniLM. These textual embeddings are combined with quantitative indicators such as gap days, rank scores, and word counts to train multiple machine learning models, including Random Forest, Decision Tree, XGBoost, LightGBM, and CatBoost. Our experiments demonstrate that Random Forest and Decision Tree models yield superior performance, with accuracy exceeding 99% and a Spearman rank correlation of 0.99. Notably, models using only numerical features achieve nearly optimal ranking results (R2 = 0.988, \r{ho} = 0.998), while LLM-based embeddings offer only marginal gains. These findings suggest that automated petition ranking can effectively streamline judicial workflows, reduce case backlog, and improve fairness in legal prioritization.

