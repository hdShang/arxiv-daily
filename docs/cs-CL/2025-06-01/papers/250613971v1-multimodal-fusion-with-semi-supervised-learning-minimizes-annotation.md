---
layout: default
title: Multimodal Fusion with Semi-Supervised Learning Minimizes Annotation Quantity for Modeling Videoconference Conversation Experience
---

# Multimodal Fusion with Semi-Supervised Learning Minimizes Annotation Quantity for Modeling Videoconference Conversation Experience

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13971" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13971v1</a>
  <a href="https://arxiv.org/pdf/2506.13971.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13971v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13971v1', 'Multimodal Fusion with Semi-Supervised Learning Minimizes Annotation Quantity for Modeling Videoconference Conversation Experience')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew Chang, Chenkai Hu, Ji Qi, Zhuojian Wei, Kexin Zhang, Viswadruth Akkaraju, David Poeppel, Dustin Freeman

**分类**: eess.AS, cs.CL, cs.HC, cs.LG, cs.MM

**发布日期**: 2025-06-01

**备注**: Interspeech 2025

**DOI**: [10.21437/Interspeech.2025-2451](https://doi.org/10.21437/Interspeech.2025-2451)

---

## 💡 一句话要点

**提出半监督学习方法以减少视频会议对话体验建模的标注需求**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频会议` `半监督学习` `多模态融合` `对话体验` `深度学习`

## 📋 核心要点

1. 现有方法在建模视频会议对话体验时，面临标注数据稀缺和昂贵的挑战，尤其是负面体验的时刻。
2. 本文提出了一种半监督学习方法，结合标注和未标注数据，利用多模态特征来预测对话中的非流畅时刻。
3. 实验结果显示，半监督学习模型在相同标注数据量下，性能超越监督学习模型，且仅需8%标注数据即可接近全数据性能。

## 📝 摘要（中文）

视频会议中的群体对话是一种复杂的社会行为，但负面体验的主观时刻，如对话失去流畅性或乐趣，仍然缺乏研究。这些时刻在自然数据中较为罕见，因此训练监督学习模型需要昂贵的手动数据标注。本文应用半监督学习，利用有针对性的标注和未标注片段，训练多模态（音频、面部、文本）深度特征，以预测视频会议中的非流畅或不愉快时刻。通过模态融合的共同训练，半监督学习模型实现了0.9的ROC-AUC和0.6的F1分数，超越了相同标注数据量的监督学习模型4%。值得注意的是，最佳的半监督学习模型仅使用8%的标注数据，便达到了监督学习模型全数据性能的96%。这表明了一种高效的标注框架，用于建模视频会议体验。

## 🔬 方法详解

**问题定义**：本文旨在解决视频会议对话中负面体验时刻的建模问题。现有的监督学习方法依赖大量标注数据，而这些数据的获取成本高且稀缺。

**核心思路**：论文提出通过半监督学习方法，结合少量标注数据与大量未标注数据，利用多模态特征（音频、面部表情、文本）来提高模型的预测能力。这样的设计旨在减少对标注数据的依赖，同时提升模型的泛化能力。

**技术框架**：整体架构包括数据预处理、特征提取、模型训练和评估四个主要模块。首先，从视频中提取音频、面部和文本特征；然后，利用半监督学习框架进行模型训练，最后评估模型在未见数据上的表现。

**关键创新**：最重要的技术创新在于模态融合的共同训练策略，通过有效利用标注和未标注数据，显著提高了模型在负面体验预测上的准确性。这与传统的监督学习方法形成鲜明对比，后者通常依赖于大量标注数据。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡标注和未标注数据的影响，同时在网络结构上进行了优化，以适应多模态特征的融合。

## 📊 实验亮点

实验结果显示，模态融合的半监督学习模型在ROC-AUC上达到了0.9，F1分数为0.6，超越了相同标注数据量的监督学习模型4%。此外，最佳半监督学习模型仅使用8%的标注数据，便达到了监督学习模型全数据性能的96%，显示出显著的标注效率提升。

## 🎯 应用场景

该研究的潜在应用领域包括视频会议软件、在线教育平台和远程协作工具等。通过有效识别对话中的负面体验时刻，可以为用户提供实时反馈和改善建议，从而提升整体沟通体验。未来，该方法还可以扩展到其他社交互动场景，具有广泛的实际价值。

## 📄 摘要（原文）

> Group conversations over videoconferencing are a complex social behavior. However, the subjective moments of negative experience, where the conversation loses fluidity or enjoyment remain understudied. These moments are infrequent in naturalistic data, and thus training a supervised learning (SL) model requires costly manual data annotation. We applied semi-supervised learning (SSL) to leverage targeted labeled and unlabeled clips for training multimodal (audio, facial, text) deep features to predict non-fluid or unenjoyable moments in holdout videoconference sessions. The modality-fused co-training SSL achieved an ROC-AUC of 0.9 and an F1 score of 0.6, outperforming SL models by up to 4% with the same amount of labeled data. Remarkably, the best SSL model with just 8% labeled data matched 96% of the SL model's full-data performance. This shows an annotation-efficient framework for modeling videoconference experience.

