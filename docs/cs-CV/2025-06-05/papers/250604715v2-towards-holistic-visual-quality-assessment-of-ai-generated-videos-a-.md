---
layout: default
title: "Towards Holistic Visual Quality Assessment of AI-Generated Videos: A LLM-Based Multi-Dimensional Evaluation Model"
---

# Towards Holistic Visual Quality Assessment of AI-Generated Videos: A LLM-Based Multi-Dimensional Evaluation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04715" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04715v2</a>
  <a href="https://arxiv.org/pdf/2506.04715.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04715v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04715v2', 'Towards Holistic Visual Quality Assessment of AI-Generated Videos: A LLM-Based Multi-Dimensional Evaluation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zelu Qi, Ping Shi, Chaoyang Zhang, Shuqi Wang, Fei Zhao, Da Pan, Zefeng Ying

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-06-12)

**备注**: This paper has been accepted by CVPR Workshop 2025

**🔗 代码/项目**: [GITHUB](https://github.com/QiZelu/AIGVEval)

---

## 💡 一句话要点

**提出多维度评估模型以解决AI生成视频的视觉质量问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI生成视频` `视觉质量评估` `多维度评估` `大型语言模型` `特征编码` `LoRA微调` `视频内容生成`

## 📋 核心要点

1. AI生成视频技术虽然发展迅速，但仍存在视觉质量缺陷，影响用户体验。
2. 本文提出将视觉质量分解为技术质量、运动质量和视频语义三个维度，并利用LLM进行质量评估。
3. 在NTIRE 2025挑战赛中，所提方法获得第二名，显示出其在视觉质量评估中的有效性。

## 📝 摘要（中文）

近年来，AI生成视频（AIGV）技术发展迅速，显著改变了视频内容制作的模式。然而，AIGV仍存在明显的视觉质量缺陷，如噪声、模糊、帧抖动和动态度低，这严重影响用户的观看体验。因此，自动视觉质量评估对AIGV内容监管和生成模型改进至关重要。本文将AIGV的视觉质量分解为技术质量、运动质量和视频语义三个维度，并为每个维度设计了相应的编码器以实现有效的特征表示。此外，考虑到大型语言模型（LLMs）在各种视觉和语言任务中的出色表现，我们引入LLM作为质量回归模块，并提出了多模态提示工程框架，以帮助LLM建立多维特征与视觉质量之间的推理关联。通过在训练阶段结合LoRA微调技术，使LLM更好地适应特定任务。我们的方法在NTIRE 2025 AI生成内容质量评估挑战赛中获得第二名，证明了其有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决AI生成视频的视觉质量评估问题。现有方法往往无法全面评估视频的多维度质量，导致评估结果不够准确和可靠。

**核心思路**：通过将视觉质量分解为技术质量、运动质量和视频语义三个维度，设计相应的编码器以实现有效特征表示，并利用LLM进行质量回归。

**技术框架**：整体架构包括三个主要模块：特征编码器、LLM质量回归模块和多模态提示工程框架。特征编码器负责提取各维度特征，LLM用于质量评估，多模态提示框架帮助LLM建立特征与质量之间的关联。

**关键创新**：引入LLM作为质量回归模块，并结合多模态提示工程框架，显著提升了多维特征与视觉质量之间的推理能力，这是与现有方法的本质区别。

**关键设计**：在训练过程中，采用LoRA微调技术，使LLM能够更好地适应特定任务，提升了模型的灵活性和准确性。

## 📊 实验亮点

在NTIRE 2025 AI生成内容质量评估挑战赛中，所提方法获得第二名，显示出其在多维度视觉质量评估中的有效性。与基线方法相比，模型在各项评估指标上均有显著提升，证明了其创新设计的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括视频内容生成、内容监管和用户体验优化等。通过有效的视觉质量评估，可以为生成模型的改进提供指导，提升AI生成视频的整体质量，进而推动相关产业的发展。

## 📄 摘要（原文）

> The development of AI-Generated Video (AIGV) technology has been remarkable in recent years, significantly transforming the paradigm of video content production. However, AIGVs still suffer from noticeable visual quality defects, such as noise, blurriness, frame jitter and low dynamic degree, which severely impact the user's viewing experience. Therefore, an effective automatic visual quality assessment is of great importance for AIGV content regulation and generative model improvement. In this work, we decompose the visual quality of AIGVs into three dimensions: technical quality, motion quality, and video semantics. For each dimension, we design corresponding encoder to achieve effective feature representation. Moreover, considering the outstanding performance of large language models (LLMs) in various vision and language tasks, we introduce a LLM as the quality regression module. To better enable the LLM to establish reasoning associations between multi-dimensional features and visual quality, we propose a specially designed multi-modal prompt engineering framework. Additionally, we incorporate LoRA fine-tuning technology during the training phase, allowing the LLM to better adapt to specific tasks. Our proposed method achieved \textbf{second place} in the NTIRE 2025 Quality Assessment of AI-Generated Content Challenge: Track 2 AI Generated video, demonstrating its effectiveness. Codes can be obtained at https://github.com/QiZelu/AIGVEval.

