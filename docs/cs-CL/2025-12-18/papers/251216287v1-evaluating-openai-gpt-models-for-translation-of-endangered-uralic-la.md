---
layout: default
title: "Evaluating OpenAI GPT Models for Translation of Endangered Uralic Languages: A Comparison of Reasoning and Non-Reasoning Architectures"
---

# Evaluating OpenAI GPT Models for Translation of Endangered Uralic Languages: A Comparison of Reasoning and Non-Reasoning Architectures

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16287" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16287v1</a>
  <a href="https://arxiv.org/pdf/2512.16287.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16287v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16287v1', 'Evaluating OpenAI GPT Models for Translation of Endangered Uralic Languages: A Comparison of Reasoning and Non-Reasoning Architectures')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yehor Tereshchenko, Mika Hämäläinen, Svitlana Myroniuk

**分类**: cs.CL

**发布日期**: 2025-12-18

**备注**: IWCLUL 2025

---

## 💡 一句话要点

**评估OpenAI GPT模型在濒危乌拉尔语翻译中的表现，对比推理与非推理架构。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低资源语言翻译` `濒危语言保护` `大型语言模型` `推理能力` `乌拉尔语`

## 📋 核心要点

1. 现有LLM翻译评估主要集中于高资源语言，忽略了低资源和濒危语言的性能。
2. 研究对比OpenAI的GPT模型，考察推理和非推理架构在乌拉尔语翻译中的差异。
3. 实验表明，推理模型在低资源乌拉尔语翻译中表现更佳，拒绝率显著降低。

## 📝 摘要（中文）

本研究旨在评估大型语言模型（LLMs）在翻译任务中的表现，特别关注低资源和濒危语言，弥补了现有研究主要集中于高资源语言的不足。本文对比了OpenAI的GPT模型，着重考察了推理和非推理架构在芬兰语与四种低资源乌拉尔语（科米-兹梁语、莫克沙语、埃尔齐亚语和乌德穆尔特语）之间翻译的差异。我们使用文学文本的平行语料库，通过拒绝率分析评估模型尝试翻译的意愿。研究结果表明，推理模型和非推理模型之间存在显著的性能差异，推理模型的拒绝率降低了16个百分点。这些发现为研究乌拉尔语的研究人员和从业者提供了有价值的见解，并有助于更广泛地理解推理模型在濒危语言保护方面的能力。

## 🔬 方法详解

**问题定义**：论文旨在解决低资源和濒危乌拉尔语的机器翻译问题。现有的大型语言模型（LLMs）在这些语言上的表现缺乏充分评估，并且现有方法在高资源语言上训练的模型可能无法很好地泛化到低资源语言，导致翻译质量差或模型直接拒绝翻译请求。

**核心思路**：论文的核心思路是对比具有推理能力的LLM（如GPT模型）和不具备推理能力的LLM在低资源乌拉尔语翻译任务上的表现差异。通过分析模型的拒绝率和翻译质量，评估推理能力对低资源语言翻译的贡献。

**技术框架**：研究采用平行语料库，包含芬兰语和四种低资源乌拉尔语（科米-兹梁语、莫克沙语、埃尔齐亚语和乌德穆尔特语）的文学文本。研究流程包括：1) 构建平行语料库；2) 使用不同的OpenAI GPT模型（包括推理和非推理架构）进行翻译；3) 分析模型的拒绝率，即模型拒绝尝试翻译的比例；4) 对翻译结果进行人工评估或使用自动评估指标（如BLEU）评估翻译质量。

**关键创新**：论文的关键创新在于首次系统性地评估了具有推理能力的LLM在低资源乌拉尔语翻译中的表现，并对比了推理和非推理架构的差异。通过拒绝率分析，揭示了推理能力对模型处理低资源语言翻译请求的重要性。

**关键设计**：论文的关键设计包括：1) 选择具有代表性的低资源乌拉尔语，以确保研究结果的泛化性；2) 使用文学文本的平行语料库，以保证翻译任务的复杂性和挑战性；3) 采用拒绝率作为评估指标，以衡量模型处理低资源语言翻译请求的意愿；4) 对比不同规模和架构的GPT模型，以分析模型性能与模型复杂度的关系。

## 📊 实验亮点

实验结果表明，具有推理能力的GPT模型在低资源乌拉尔语翻译中表现优于非推理模型，拒绝率降低了16个百分点。这表明推理能力对于处理低资源语言的翻译请求至关重要。该研究为进一步优化LLM在低资源语言上的翻译性能提供了重要依据。

## 🎯 应用场景

该研究成果可应用于濒危语言的保护和传承，例如辅助语言学习、自动生成语言资源、促进跨文化交流等。通过优化LLM在低资源语言上的翻译能力，可以帮助更多人接触和了解这些语言，从而促进其复兴和发展。此外，该研究也为其他低资源语言的机器翻译研究提供了借鉴。

## 📄 摘要（原文）

> The evaluation of Large Language Models (LLMs) for translation tasks has primarily focused on high-resource languages, leaving a significant gap in understanding their performance on low-resource and endangered languages. This study presents a comprehensive comparison of OpenAI's GPT models, specifically examining the differences between reasoning and non-reasoning architectures for translating between Finnish and four low-resource Uralic languages: Komi-Zyrian, Moksha, Erzya, and Udmurt. Using a parallel corpus of literary texts, we evaluate model willingness to attempt translation through refusal rate analysis across different model architectures. Our findings reveal significant performance variations between reasoning and non-reasoning models, with reasoning models showing 16 percentage points lower refusal rates. The results provide valuable insights for researchers and practitioners working with Uralic languages and contribute to the broader understanding of reasoning model capabilities for endangered language preservation.

