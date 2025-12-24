---
layout: default
title: "Learning the Topic, Not the Language: How LLMs Classify Online Immigration Discourse Across Languages"
---

# Learning the Topic, Not the Language: How LLMs Classify Online Immigration Discourse Across Languages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06435" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06435v1</a>
  <a href="https://arxiv.org/pdf/2508.06435.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06435v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06435v1', 'Learning the Topic, Not the Language: How LLMs Classify Online Immigration Discourse Across Languages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrea Nasuto, Stefano Maria Iacus, Francisco Rowe, Devika Jain

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出轻量级LLM以跨语言分类移民话题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `跨语言分类` `移民话题` `微调技术` `社会科学研究` `开源模型` `推文分析`

## 📋 核心要点

1. 现有方法在跨语言话题检测中面临挑战，尤其是对未见语言的分类能力不足。
2. 论文提出通过对LLaMA模型进行轻量级微调，利用单语、双语或多语数据集进行移民话题分类。
3. 实验结果显示，微调后的模型在未见语言中表现良好，且多语言微调显著提高了分类准确性。

## 📝 摘要（中文）

大型语言模型（LLMs）正在通过实现可扩展、精准的分析，改变社会科学研究。本文探讨了通过在少数语言上微调获得的知识是否能转移到在预训练中未见过的语言。研究通过对LLaMA 3.2-3B模型进行微调，使用单语、双语或多语数据集对来自X/Twitter的移民相关推文进行分类。结果表明，微调后的LLMs能够在未见语言中可靠地分类移民内容，且多语言微调有助于更好地识别推文的移民立场。即使在微调中对代表性不足的语言进行最小暴露，也能显著提升性能。该研究挑战了跨语言掌握需要广泛多语言训练的假设，提供了开源的、可重复的LLM替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在跨语言移民话题分类中的有效性问题，现有方法在处理未见语言时表现不佳，且存在预训练偏见。

**核心思路**：通过对LLaMA模型进行轻量级微调，利用有限的语言数据实现跨语言话题检测，旨在证明少量语言覆盖足以实现主题级别的泛化。

**技术框架**：研究采用LLaMA 3.2-3B模型，进行单语、双语和多语数据集的微调，模型结构保持轻量化，便于快速推理和部署。

**关键创新**：最重要的创新在于展示了即使在微调中对代表性不足的语言进行极小的暴露，也能显著提升模型在未见语言中的分类能力，挑战了传统的多语言训练假设。

**关键设计**：在微调过程中，使用了特定的损失函数和参数设置，确保模型能够有效学习不同语言的移民话题特征，同时保持计算效率。

## 📊 实验亮点

实验结果表明，经过微调的LLMs在未见语言的移民内容分类中表现出色，尤其是在多语言微调的情况下，分类准确性显著提高。微调模型的推理速度比OpenAI的GPT-4o快35倍，且成本仅为其0.00000989%。

## 🎯 应用场景

该研究的潜在应用领域包括社会科学研究、移民政策分析和公共舆论监测。通过提供高效的跨语言分类工具，研究能够帮助政策制定者和研究人员更好地理解不同文化背景下的移民话题，从而推动更具包容性的社会对话。

## 📄 摘要（原文）

> Large language models (LLMs) are transforming social-science research by enabling scalable, precise analysis. Their adaptability raises the question of whether knowledge acquired through fine-tuning in a few languages can transfer to unseen languages that only appeared during pre-training. To examine this, we fine-tune lightweight LLaMA 3.2-3B models on monolingual, bilingual, or multilingual data sets to classify immigration-related tweets from X/Twitter across 13 languages, a domain characterised by polarised, culturally specific discourse. We evaluate whether minimal language-specific fine-tuning enables cross-lingual topic detection and whether adding targeted languages corrects pre-training biases. Results show that LLMs fine-tuned in one or two languages can reliably classify immigration-related content in unseen languages. However, identifying whether a tweet expresses a pro- or anti-immigration stance benefits from multilingual fine-tuning. Pre-training bias favours dominant languages, but even minimal exposure to under-represented languages during fine-tuning (as little as $9.62\times10^{-11}$ of the original pre-training token volume) yields significant gains. These findings challenge the assumption that cross-lingual mastery requires extensive multilingual training: limited language coverage suffices for topic-level generalisation, and structural biases can be corrected with lightweight interventions. By releasing 4-bit-quantised, LoRA fine-tuned models, we provide an open-source, reproducible alternative to proprietary LLMs that delivers 35 times faster inference at just 0.00000989% of the dollar cost of the OpenAI GPT-4o model, enabling scalable, inclusive research.

