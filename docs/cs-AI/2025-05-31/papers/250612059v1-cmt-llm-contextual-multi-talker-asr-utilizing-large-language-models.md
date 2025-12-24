---
layout: default
title: "CMT-LLM: Contextual Multi-Talker ASR Utilizing Large Language Models"
---

# CMT-LLM: Contextual Multi-Talker ASR Utilizing Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12059" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12059v1</a>
  <a href="https://arxiv.org/pdf/2506.12059.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12059v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12059v1', 'CMT-LLM: Contextual Multi-Talker ASR Utilizing Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiajun He, Naoki Sawada, Koichi Miyazaki, Tomoki Toda

**分类**: eess.AS, cs.AI, cs.CL, cs.SD

**发布日期**: 2025-05-31

**备注**: Accepted by INTERSPEECH 2025

---

## 💡 一句话要点

**提出CMT-LLM框架以解决多说话者ASR与上下文偏置问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动语音识别` `多说话者识别` `上下文偏置` `大型语言模型` `稀有词汇识别`

## 📋 核心要点

1. 现有的多说话者ASR和上下文偏置方法分别处理，导致在复杂场景中的性能不足。
2. 提出的统一框架将多说话者重叠语音识别与上下文偏置结合，利用预训练的语音编码器和大型语言模型。
3. 实验结果显示，该方法在LibriMix和AMI SDM数据集上显著优于传统方法，字错误率分别为7.9%和32.9%。

## 📝 摘要（中文）

在实际应用中，自动语音识别（ASR）系统必须处理多说话者的重叠语音并识别稀有词汇，如技术术语。传统方法将多说话者ASR和上下文偏置分别处理，限制了在复杂场景中的性能。本文提出了一个统一框架，将多说话者重叠语音识别和上下文偏置整合为单一任务。我们的ASR方法结合了预训练的语音编码器和大型语言模型（LLMs），并采用优化的微调策略。此外，我们还引入了一种两阶段过滤算法，以高效识别来自大型偏置列表的相关稀有词汇，并将其纳入LLM的提示输入中，从而增强稀有词汇的识别能力。实验结果表明，我们的方法在LibriMix上达到了7.9%的字错误率（WER），在AMI SDM上达到了32.9%，展示了其在复杂语音场景中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决多说话者ASR系统在处理重叠语音和稀有词汇时的性能不足。现有方法将这两者分开处理，导致在复杂场景中的识别效果不佳。

**核心思路**：提出的CMT-LLM框架将多说话者重叠语音识别与上下文偏置整合为一个统一任务，通过结合预训练的语音编码器和大型语言模型来提升识别精度。

**技术框架**：该框架包括两个主要模块：首先是多说话者重叠语音识别模块，利用预训练的语音编码器进行特征提取；其次是上下文偏置模块，通过大型语言模型优化输入提示，增强稀有词汇的识别能力。

**关键创新**：最重要的创新在于将多说话者ASR与上下文偏置整合为一个任务，利用两阶段过滤算法高效识别相关稀有词汇，显著提升了识别性能。

**关键设计**：在模型设计中，采用了优化的微调策略，确保预训练模型能够适应特定任务需求。同时，设计了两阶段过滤算法，以减少偏置列表的规模，提高稀有词汇的识别效率。

## 📊 实验亮点

实验结果表明，CMT-LLM框架在LibriMix数据集上实现了7.9%的字错误率（WER），在AMI SDM数据集上达到了32.9%。与传统上下文偏置方法相比，显著提升了识别性能，展示了其在复杂语音场景中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括会议记录、客服系统和多媒体内容的自动转录等。通过提升多说话者环境下的语音识别能力，能够显著提高信息获取的效率和准确性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> In real-world applications, automatic speech recognition (ASR) systems must handle overlapping speech from multiple speakers and recognize rare words like technical terms. Traditional methods address multi-talker ASR and contextual biasing separately, limiting performance in complex scenarios. We propose a unified framework that combines multi-talker overlapping speech recognition and contextual biasing into a single task. Our ASR method integrates pretrained speech encoders and large language models (LLMs), using optimized finetuning strategies. We also introduce a two-stage filtering algorithm to efficiently identify relevant rare words from large biasing lists and incorporate them into the LLM's prompt input, enhancing rare word recognition. Experiments show that our approach outperforms traditional contextual biasing methods, achieving a WER of 7.9% on LibriMix and 32.9% on AMI SDM when the biasing size is 1,000, demonstrating its effectiveness in complex speech scenarios.

