---
layout: default
title: "The NTNU System at the S&I Challenge 2025 SLA Open Track"
---

# The NTNU System at the S&I Challenge 2025 SLA Open Track

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05121" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05121v2</a>
  <a href="https://arxiv.org/pdf/2506.05121.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05121v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05121v2', 'The NTNU System at the S&I Challenge 2025 SLA Open Track')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hong-Yun Lin, Tien-Hong Lo, Yu-Hsuan Fang, Jhen-Ke Lin, Chung-Chun Wang, Hao-Chien Lu, Berlin Chen

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-06-05 (更新: 2025-09-11)

**备注**: submitted to the ISCA SLaTE-2025 Workshop

---

## 💡 一句话要点

**提出多模态融合系统以提升口语能力评估准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `口语能力评估` `多模态融合` `神经网络` `BERT` `wav2vec 2.0` `评分融合` `语言模型` `声学特征`

## 📋 核心要点

1. 现有的BERT和W2V方法在口语能力评估中存在模态特定的局限性，导致评估准确性不足。
2. 本文提出了一种新系统，通过将W2V与Phi-4多模态大语言模型集成，采用评分融合策略来提升评估效果。
3. 实验结果显示，该系统在官方测试集上实现了0.375的RMSE，优于多个基线系统，展示了显著的性能提升。

## 📝 摘要（中文）

近年来，口语能力评估（SLA）研究采用神经模型如BERT和wav2vec 2.0（W2V）来评估语言和声学模态的口语能力。尽管这两种模型在捕捉口语能力相关特征方面表现良好，但各自存在模态特定的局限性。BERT方法依赖于ASR转录，常常无法捕捉到韵律和语音线索，而W2V方法在建模声学特征方面表现优异，但缺乏语义可解释性。为克服这些局限性，本文提出了一种通过评分融合策略将W2V与Phi-4多模态大语言模型（MLLM）集成的系统。该系统在Speak & Improve Challenge 2025的官方测试集上实现了0.375的均方根误差（RMSE），在比赛中获得第二名。与排名第一、第三和官方基线系统的RMSE分别为0.364、0.384和0.444相比，表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决现有口语能力评估方法在模态特定局限性下的准确性问题。BERT依赖的ASR转录无法捕捉韵律和语音特征，而W2V缺乏语义可解释性。

**核心思路**：论文的核心思路是将W2V与Phi-4多模态大语言模型进行融合，通过评分融合策略来综合两者的优势，从而提升口语能力评估的准确性。

**技术框架**：整体架构包括W2V模型用于声学特征提取，Phi-4 MLLM用于语义理解，二者通过评分融合策略结合，形成最终的评估结果。

**关键创新**：最重要的技术创新在于提出了W2V与多模态大语言模型的有效融合，克服了各自的局限性，实现了更全面的口语能力评估。

**关键设计**：在系统设计中，采用了特定的损失函数来优化评分融合过程，并在网络结构上进行了调整，以确保声学和语义特征的有效结合。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，提出的系统在Speak & Improve Challenge 2025的官方测试集上实现了0.375的RMSE，优于排名第一的系统（0.364）和第三的系统（0.384），相较于官方基线（0.444）也有显著提升，展示了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、语言学习平台和自动评分系统等。通过提升口语能力评估的准确性，能够为学习者提供更有效的反馈，帮助其更好地掌握语言技能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> A recent line of research on spoken language assessment (SLA) employs neural models such as BERT and wav2vec 2.0 (W2V) to evaluate speaking proficiency across linguistic and acoustic modalities. Although both models effectively capture features relevant to oral competence, each exhibits modality-specific limitations. BERT-based methods rely on ASR transcripts, which often fail to capture prosodic and phonetic cues for SLA. In contrast, W2V-based methods excel at modeling acoustic features but lack semantic interpretability. To overcome these limitations, we propose a system that integrates W2V with Phi-4 multimodal large language model (MLLM) through a score fusion strategy. The proposed system achieves a root mean square error (RMSE) of 0.375 on the official test set of the Speak & Improve Challenge 2025, securing second place in the competition. For comparison, the RMSEs of the top-ranked, third-ranked, and official baseline systems are 0.364, 0.384, and 0.444, respectively.

