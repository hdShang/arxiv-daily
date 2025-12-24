---
layout: default
title: "Estimating Quality in Therapeutic Conversations: A Multi-Dimensional Natural Language Processing Framework"
---

# Estimating Quality in Therapeutic Conversations: A Multi-Dimensional Natural Language Processing Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06151" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06151v1</a>
  <a href="https://arxiv.org/pdf/2505.06151.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06151v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06151v1', 'Estimating Quality in Therapeutic Conversations: A Multi-Dimensional Natural Language Processing Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alice Rueda, Argyrios Perivolaris, Niloy Roy, Dylan Weston, Sarmed Shaya, Zachary Cote, Martin Ivanov, Bazen G. Teferra, Yuqi Wu, Sirisha Rambhatla, Divya Sharma, Andrew Greenshaw, Rakesh Jetly, Yanbo Zhang, Bo Cao, Reza Samavi, Sridhar Krishnan, Venkat Bhat

**分类**: cs.CL

**发布日期**: 2025-05-09

**备注**: 12 pages, 4 figures, 7 tables

---

## 💡 一句话要点

**提出多维自然语言处理框架以评估治疗对话质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言处理` `治疗对话` `参与质量评估` `多维特征提取` `机器学习` `心理健康` `数据增强`

## 📋 核心要点

1. 现有方法在评估治疗对话质量时缺乏客观性和多维度分析，难以提供实时反馈。
2. 论文提出了一种基于文本分析的多维NLP框架，通过提取对话动态、语义相似性等特征来评估参与质量。
3. 实验结果显示，经过数据增强后，随机森林的准确率提升至88.9%，表明该框架在实际应用中的有效性和可扩展性。

## 📝 摘要（中文）

客户与治疗师之间的互动是治疗成功的关键因素。本文提出了一种多维自然语言处理（NLP）框架，基于文本转录客观分类咨询会话中的参与质量。通过分析253个动机访谈的转录文本，提取了四个领域的42个特征，包括对话动态、语义相似性、情感分类和问题检测。使用随机森林、Cat-Boost和支持向量机等分类器进行超参数调优，结果显示随机森林在未增强数据上达到了76.7%的分类准确率，而在经过SMOTE-Tomek增强后，准确率提升至88.9%。该框架为未来大规模应用提供了潜力，并支持多模态扩展，以实现更全面的评估。

## 🔬 方法详解

**问题定义**：本文旨在解决治疗对话质量评估的客观性不足问题，现有方法往往依赖主观判断，缺乏系统性分析。

**核心思路**：提出的框架通过提取多维特征（如对话动态和语义相似性），实现对咨询会话参与质量的量化评估，旨在提供实时反馈以改善治疗效果。

**技术框架**：整体架构包括数据收集、特征提取、分类器训练与评估四个主要阶段。首先收集动机访谈的文本数据，然后提取相关特征，最后使用多种分类器进行训练和评估。

**关键创新**：该框架的创新点在于多维度特征提取和分类方法的结合，尤其是对话动态和语义相似性分析的引入，使得评估更加全面和客观。

**关键设计**：在分类器方面，使用随机森林、Cat-Boost和支持向量机，并通过超参数调优和5折交叉验证优化模型性能。特征提取过程中，重点关注客户发言的词汇使用情况。

## 📊 实验亮点

实验结果显示，随机森林在未增强数据上的分类准确率为76.7%，而经过SMOTE-Tomek增强后，准确率提升至88.9%，F1-score达到90.0%，AUC值为94.6%。支持向量机在增强数据上也表现出色，AUC值达93.6%。

## 🎯 应用场景

该研究的潜在应用领域包括心理治疗、咨询服务和教育等，能够为临床工作者提供实时反馈，帮助提升治疗质量。未来，该框架还可扩展至多模态数据分析，如结合语音语调和面部表情，进一步增强评估的全面性。

## 📄 摘要（原文）

> Engagement between client and therapist is a critical determinant of therapeutic success. We propose a multi-dimensional natural language processing (NLP) framework that objectively classifies engagement quality in counseling sessions based on textual transcripts. Using 253 motivational interviewing transcripts (150 high-quality, 103 low-quality), we extracted 42 features across four domains: conversational dynamics, semantic similarity as topic alignment, sentiment classification, and question detection. Classifiers, including Random Forest (RF), Cat-Boost, and Support Vector Machines (SVM), were hyperparameter tuned and trained using a stratified 5-fold cross-validation and evaluated on a holdout test set. On balanced (non-augmented) data, RF achieved the highest classification accuracy (76.7%), and SVM achieved the highest AUC (85.4%). After SMOTE-Tomek augmentation, performance improved significantly: RF achieved up to 88.9% accuracy, 90.0% F1-score, and 94.6% AUC, while SVM reached 81.1% accuracy, 83.1% F1-score, and 93.6% AUC. The augmented data results reflect the potential of the framework in future larger-scale applications. Feature contribution revealed conversational dynamics and semantic similarity between clients and therapists were among the top contributors, led by words uttered by the client (mean and standard deviation). The framework was robust across the original and augmented datasets and demonstrated consistent improvements in F1 scores and recall. While currently text-based, the framework supports future multimodal extensions (e.g., vocal tone, facial affect) for more holistic assessments. This work introduces a scalable, data-driven method for evaluating engagement quality of the therapy session, offering clinicians real-time feedback to enhance the quality of both virtual and in-person therapeutic interactions.

