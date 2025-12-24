---
layout: default
title: "WhisQ: Cross-Modal Representation Learning for Text-to-Music MOS Prediction"
---

# WhisQ: Cross-Modal Representation Learning for Text-to-Music MOS Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05899" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05899v1</a>
  <a href="https://arxiv.org/pdf/2506.05899.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05899v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05899v1', 'WhisQ: Cross-Modal Representation Learning for Text-to-Music MOS Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jakaria Islam Emon, Kazi Tamanna Alam, Md. Abu Salek

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-06-06

**备注**: 3 pages

---

## 💡 一句话要点

**提出WhisQ以解决文本到音乐的MOS预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到音乐` `平均意见评分` `多模态学习` `最优传输` `共同注意力` `音频编码` `语义对齐`

## 📋 核心要点

1. 现有文本到音乐系统在MOS预测中面临双重评估挑战，难以同时兼顾音乐质量和文本对齐性。
2. WhisQ通过引入序列级共同注意力和最优传输正则化，提出了一种新的多模态架构，以实现更精确的MOS预测。
3. 在MusicEval Track-1数据集上，WhisQ在OMQ和TA的Spearman相关性分别提高了7%和14%，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种名为WhisQ的多模态架构，旨在解决文本到音乐系统中的平均意见评分（MOS）预测问题，该问题需要同时评估音乐质量和文本提示的对齐性。WhisQ通过序列级别的共同注意力机制和最优传输正则化来应对这一挑战。该架构采用Whisper Base预训练模型进行音频编码，并使用Qwen 3小型语言模型进行文本编码，保持序列结构以实现精细的跨模态建模。在MusicEval Track-1数据集上，WhisQ在OMQ和TA的Spearman相关性上分别提高了7%和14%。消融研究表明，最优传输正则化提供了最大的性能提升（10% SRCC改进），突显了显式跨模态对齐在文本到音乐评估中的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到音乐系统中的平均意见评分（MOS）预测问题，现有方法难以同时评估音乐质量和文本提示的对齐性，导致预测准确性不足。

**核心思路**：WhisQ通过序列级别的共同注意力机制和最优传输正则化来增强音频和文本之间的对齐，确保在共享嵌入空间中实现更好的语义一致性。

**技术框架**：WhisQ的整体架构包括音频编码模块（使用Whisper Base模型）、文本编码模块（使用Qwen 3小型语言模型）以及两个专门的预测路径：OMQ和TA，分别从音频嵌入和音频文本共同注意力中进行预测。

**关键创新**：WhisQ的主要创新在于引入了最优传输正则化机制，显著提高了跨模态对齐的效果，与传统方法相比，能够更好地捕捉音频与文本之间的语义关系。

**关键设计**：WhisQ的设计包括使用序列结构保持音频和文本的时间特性，采用Sinkhorn最优传输损失函数来强化语义对齐，同时在模型训练中引入了双向序列共同注意力机制，以提升预测准确性。

## 📊 实验亮点

WhisQ在MusicEval Track-1数据集上取得了显著的实验结果，OMQ的Spearman相关性提高了7%，而TA的提升幅度更是达到了14%。消融实验表明，最优传输正则化机制带来了10%的SRCC提升，强调了跨模态对齐的重要性。

## 🎯 应用场景

WhisQ的研究成果在音乐生成、推荐系统和人机交互等领域具有广泛的应用潜力。通过提高文本与音乐之间的对齐性，该模型可以为用户提供更个性化的音乐推荐，改善用户体验。此外，该技术还可用于音乐创作辅助工具，帮助创作者更好地将文本意图转化为音乐作品。

## 📄 摘要（原文）

> Mean Opinion Score (MOS) prediction for text to music systems requires evaluating both overall musical quality and text prompt alignment. This paper introduces WhisQ, a multimodal architecture that addresses this dual-assessment challenge through sequence level co-attention and optimal transport regularization. WhisQ employs the Whisper Base pretrained model for temporal audio encoding and Qwen 3, a 0.6B Small Language Model (SLM), for text encoding, with both maintaining sequence structure for fine grained cross-modal modeling. The architecture features specialized prediction pathways: OMQ is predicted from pooled audio embeddings, while TA leverages bidirectional sequence co-attention between audio and text. Sinkhorn optimal transport loss further enforce semantic alignment in the shared embedding space. On the MusicEval Track-1 dataset, WhisQ achieves substantial improvements over the baseline: 7% improvement in Spearman correlation for OMQ and 14% for TA. Ablation studies reveal that optimal transport regularization provides the largest performance gain (10% SRCC improvement), demonstrating the importance of explicit cross-modal alignment for text-to-music evaluation.

