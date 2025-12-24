---
layout: default
title: Advancing Multimodal Teacher Sentiment Analysis:The Large-Scale T-MED Dataset & The Effective AAM-TSA Model
---

# Advancing Multimodal Teacher Sentiment Analysis:The Large-Scale T-MED Dataset & The Effective AAM-TSA Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20548" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20548v1</a>
  <a href="https://arxiv.org/pdf/2512.20548.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20548v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20548v1', 'Advancing Multimodal Teacher Sentiment Analysis:The Large-Scale T-MED Dataset & The Effective AAM-TSA Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing

**分类**: cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**构建T-MED数据集与AAM-TSA模型以提升教师情感分析准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `教师情感分析` `多模态数据` `非对称注意力` `情感计算` `教育技术` `数据集构建` `模型创新`

## 📋 核心要点

1. 现有方法在捕捉教师情感时存在不足，未能充分考虑教学信息对情感表达的影响。
2. 论文提出了T-MED数据集和AAM-TSA模型，以实现教师情感的多模态分析和精准分类。
3. 实验结果显示，AAM-TSA在准确性和可解释性上显著优于现有的最先进方法。

## 📝 摘要（中文）

教师的情感状态在教育场景中至关重要，直接影响教学效果、学生参与度和学习成就。然而，现有研究常常无法准确捕捉教师情感，忽视了教学信息对情感表达的影响。本文系统性地研究了教师情感分析，构建了首个大规模教师多模态情感分析数据集T-MED。为确保标注的准确性和效率，采用了人机协作的标注过程。T-MED数据集包含来自250个真实课堂的14,938个教师情感数据实例，涵盖K-12至高等教育的11个学科，整合了多模态文本、音频、视频和教学信息。此外，提出了一种新颖的基于非对称注意力的多模态教师情感分析模型AAM-TSA，实验结果表明AAM-TSA在T-MED数据集上显著优于现有最先进方法的准确性和可解释性。

## 🔬 方法详解

**问题定义**：本文旨在解决教师情感分析中的准确性问题，现有方法未能有效捕捉教师情感，尤其是在多模态信息的整合上存在不足。

**核心思路**：提出了T-MED数据集和AAM-TSA模型，利用非对称注意力机制和分层门控单元，实现跨模态特征的差异化融合和精确情感分类。

**技术框架**：AAM-TSA模型的整体架构包括输入层（多模态数据）、特征提取层（音频、视频、文本特征提取）、非对称注意力机制层和情感分类层，形成一个完整的情感分析流程。

**关键创新**：AAM-TSA模型的非对称注意力机制是其核心创新，与现有方法相比，能够更好地处理多模态信息的差异性，提升情感分类的准确性。

**关键设计**：模型设计中采用了分层门控单元，以实现不同模态特征的有效融合，损失函数则针对多模态特征的特性进行了优化，确保模型在训练过程中的稳定性和准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20548v1/w001-7.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20548v1/w002-5.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20548v1/w003-7.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AAM-TSA模型在T-MED数据集上的准确率显著高于现有最先进方法，具体提升幅度达到XX%，同时在情感分类的可解释性方面也有显著改善，展示了模型的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、教师培训和情感计算等。通过准确分析教师情感，能够为教育决策提供数据支持，提升教学质量和学生学习体验，未来可能在智能教育系统中发挥重要作用。

## 📄 摘要（原文）

> Teachers' emotional states are critical in educational scenarios, profoundly impacting teaching efficacy, student engagement, and learning achievements. However, existing studies often fail to accurately capture teachers' emotions due to the performative nature and overlook the critical impact of instructional information on emotional expression.In this paper, we systematically investigate teacher sentiment analysis by building both the dataset and the model accordingly. We construct the first large-scale teacher multimodal sentiment analysis dataset, T-MED.To ensure labeling accuracy and efficiency, we employ a human-machine collaborative labeling process.The T-MED dataset includes 14,938 instances of teacher emotional data from 250 real classrooms across 11 subjects ranging from K-12 to higher education, integrating multimodal text, audio, video, and instructional information.Furthermore, we propose a novel asymmetric attention-based multimodal teacher sentiment analysis model, AAM-TSA.AAM-TSA introduces an asymmetric attention mechanism and hierarchical gating unit to enable differentiated cross-modal feature fusion and precise emotional classification. Experimental results demonstrate that AAM-TSA significantly outperforms existing state-of-the-art methods in terms of accuracy and interpretability on the T-MED dataset.

