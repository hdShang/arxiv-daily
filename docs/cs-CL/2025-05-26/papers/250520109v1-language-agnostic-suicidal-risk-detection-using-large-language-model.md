---
layout: default
title: Language-Agnostic Suicidal Risk Detection Using Large Language Models
---

# Language-Agnostic Suicidal Risk Detection Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20109" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20109v1</a>
  <a href="https://arxiv.org/pdf/2505.20109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20109v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20109v1', 'Language-Agnostic Suicidal Risk Detection Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: June-Woo Kim, Wonkyo Oh, Haram Yoon, Sung-Hoon Yoon, Dae-Jin Kim, Dong-Ho Lee, Sang-Yeol Lee, Chan-Mo Yang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26

**备注**: Accepted to InterSpeech 2025

---

## 💡 一句话要点

**提出语言无关的自杀风险检测框架以解决现有方法局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自杀风险检测` `语言无关` `大型语言模型` `自动语音识别` `心理健康评估` `特征提取` `跨语言分析`

## 📋 核心要点

1. 现有自杀风险检测方法依赖于特定语言模型，导致可扩展性差和泛化能力不足。
2. 本研究提出了一种语言无关的框架，通过大型语言模型提取自杀风险特征，支持跨语言分析。
3. 实验结果显示，该方法在性能上与传统方法相当，展示了其在自杀风险评估中的应用潜力。

## 📝 摘要（中文）

青少年自杀风险检测是一个重要的挑战，但现有方法依赖于特定语言模型，限制了其可扩展性和泛化能力。本研究提出了一种新颖的语言无关框架，利用大型语言模型（LLMs）进行自杀风险评估。我们通过自动语音识别（ASR）模型生成中文转录文本，并使用基于提示的查询从这些转录文本中提取与自杀风险相关的特征。这些特征以中文和英文保留，以便进行跨语言分析，并用于独立微调相应的预训练语言模型。实验结果表明，我们的方法在性能上与直接微调ASR结果或仅基于中文自杀风险特征训练的模型相当，展示了其克服语言限制和提高自杀风险评估鲁棒性的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决青少年自杀风险检测中现有方法的语言依赖性问题，导致其在不同语言环境中的应用受限。

**核心思路**：提出一种语言无关的框架，通过自动语音识别生成转录文本，并利用大型语言模型提取自杀风险特征，从而实现跨语言分析。

**技术框架**：整体流程包括使用ASR模型生成中文转录文本，随后通过LLMs进行特征提取，并将提取的特征用于微调预训练语言模型。

**关键创新**：本研究的主要创新在于实现了语言无关的自杀风险检测，突破了传统方法的语言限制，提升了模型的适用性和鲁棒性。

**关键设计**：在特征提取过程中，采用基于提示的查询方式，确保提取的特征在中文和英文中均有效，并独立微调相应的预训练模型以优化性能。

## 📊 实验亮点

实验结果表明，该方法在自杀风险检测中表现出与直接微调ASR结果或仅基于中文特征训练的模型相当的性能，展示了其在不同语言环境中的有效性和鲁棒性。具体性能数据未提供，但结果表明该方法具有显著的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康监测、社交媒体内容分析和危机干预等。通过提供一种语言无关的自杀风险检测工具，可以在多语言环境中更有效地识别和干预自杀风险，从而提高青少年的心理健康支持水平。未来，该框架有望扩展到其他心理健康领域的风险评估。

## 📄 摘要（原文）

> Suicidal risk detection in adolescents is a critical challenge, yet existing methods rely on language-specific models, limiting scalability and generalization. This study introduces a novel language-agnostic framework for suicidal risk assessment with large language models (LLMs). We generate Chinese transcripts from speech using an ASR model and then employ LLMs with prompt-based queries to extract suicidal risk-related features from these transcripts. The extracted features are retained in both Chinese and English to enable cross-linguistic analysis and then used to fine-tune corresponding pretrained language models independently. Experimental results show that our method achieves performance comparable to direct fine-tuning with ASR results or to models trained solely on Chinese suicidal risk-related features, demonstrating its potential to overcome language constraints and improve the robustness of suicidal risk assessment.

