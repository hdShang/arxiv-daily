---
layout: default
title: "Translate With Care: Addressing Gender Bias, Neutrality, and Reasoning in Large Language Model Translations"
---

# Translate With Care: Addressing Gender Bias, Neutrality, and Reasoning in Large Language Model Translations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00748" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00748v1</a>
  <a href="https://arxiv.org/pdf/2506.00748.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00748v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00748v1', 'Translate With Care: Addressing Gender Bias, Neutrality, and Reasoning in Large Language Model Translations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pardis Sadat Zahraei, Ali Emami

**分类**: cs.CL, cs.CY

**发布日期**: 2025-05-31

**备注**: Accepted to Findings of ACL 2025

---

## 💡 一句话要点

**提出Translate-with-Care数据集以解决机器翻译中的性别偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器翻译` `性别偏见` `逻辑一致性` `数据集构建` `模型微调` `多语言处理` `人工智能伦理`

## 📋 核心要点

1. 核心问题：现有机器翻译系统在处理性别偏见和逻辑一致性方面存在显著不足，尤其是在性别语言与无性别语言之间的翻译。
2. 方法要点：提出Translate-with-Care数据集，通过3950个场景评估翻译系统的表现，并对mBART-50进行微调以减少偏见。
3. 实验或效果：微调后的mBART-50在性别偏见和推理错误方面表现显著改善，超越了多种专有翻译模型。

## 📝 摘要（中文）

在机器翻译中，解决性别偏见和保持逻辑一致性仍然是一个挑战，尤其是在自然性别语言（如英语）与无性别语言（如波斯语、印尼语和芬兰语）之间翻译时。本文引入了Translate-with-Care（TWC）数据集，包含3950个具有挑战性的场景，旨在评估翻译系统的性能。对多种技术（包括GPT-4、mBART-50、NLLB-200和Google翻译）的分析显示，在翻译无性别内容时，普遍存在性别刻板印象和推理错误。所有模型在性别刻板印象影响选择时更倾向于使用男性代词。Google翻译和GPT-4在领导和职业成功的语境中，男性代词的使用频率是女性代词的4-6倍。对mBART-50进行TWC微调显著解决了这些偏见和错误，表现出强大的泛化能力，并超越了专有LLM，同时保持开源。该研究强调了在机器翻译中针对性别和语义一致性的必要性，尤其是对于无性别语言，从而促进更公平和准确的翻译系统。

## 🔬 方法详解

**问题定义**：本文旨在解决机器翻译中性别偏见和逻辑一致性的问题。现有方法在翻译无性别语言时，常常导致性别刻板印象和推理错误，影响翻译质量。

**核心思路**：论文提出了Translate-with-Care（TWC）数据集，包含多种具有挑战性的翻译场景，旨在评估和改进翻译系统在性别和语义一致性方面的表现。通过对mBART-50进行微调，旨在减少性别偏见和推理错误。

**技术框架**：整体架构包括数据集构建、模型选择、微调过程和性能评估。数据集涵盖六种低到中资源语言，模型选择包括GPT-4、mBART-50等，评估指标则关注性别偏见和逻辑一致性。

**关键创新**：最重要的技术创新在于引入了TWC数据集，系统性地评估了多种翻译模型在性别偏见和推理一致性方面的表现，特别是在无性别语言的翻译中。

**关键设计**：在微调过程中，采用了特定的损失函数以减少性别偏见，并通过多轮训练优化模型参数，确保在不同场景下的泛化能力。

## 📊 实验亮点

实验结果显示，微调后的mBART-50在性别偏见和推理错误方面显著改善，超越了多种专有翻译模型。具体而言，Google翻译和GPT-4在性别偏见方面的表现尤为突出，男性代词的使用频率是女性代词的4-6倍，而微调后的mBART-50则有效降低了这一比例。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译系统、跨文化交流工具和教育软件等。通过减少性别偏见和提高逻辑一致性，能够为用户提供更公平和准确的翻译体验，促进不同文化之间的理解与交流。

## 📄 摘要（原文）

> Addressing gender bias and maintaining logical coherence in machine translation remains challenging, particularly when translating between natural gender languages, like English, and genderless languages, such as Persian, Indonesian, and Finnish. We introduce the Translate-with-Care (TWC) dataset, comprising 3,950 challenging scenarios across six low- to mid-resource languages, to assess translation systems' performance. Our analysis of diverse technologies, including GPT-4, mBART-50, NLLB-200, and Google Translate, reveals a universal struggle in translating genderless content, resulting in gender stereotyping and reasoning errors. All models preferred masculine pronouns when gender stereotypes could influence choices. Google Translate and GPT-4 showed particularly strong bias, favoring male pronouns 4-6 times more than feminine ones in leadership and professional success contexts. Fine-tuning mBART-50 on TWC substantially resolved these biases and errors, led to strong generalization, and surpassed proprietary LLMs while remaining open-source. This work emphasizes the need for targeted approaches to gender and semantic coherence in machine translation, particularly for genderless languages, contributing to more equitable and accurate translation systems.

