---
layout: default
title: "ALIGN: Word Association Learning for Cultural Alignment in Large Language Models"
---

# ALIGN: Word Association Learning for Cultural Alignment in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13426" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13426v2</a>
  <a href="https://arxiv.org/pdf/2508.13426.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13426v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13426v2', 'ALIGN: Word Association Learning for Cultural Alignment in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chunhua Liu, Kabir Manandhar Shrestha, Sukai Huang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-19 (更新: 2025-12-15)

---

## 💡 一句话要点

**提出ALIGN方法以解决大型语言模型的文化偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文化对齐` `词汇联想` `大型语言模型` `认知心理学` `微调方法` `跨文化交流` `人工智能`

## 📋 核心要点

1. 现有大型语言模型在训练数据中存在文化偏见，且缺乏有效的文化对齐学习方法。
2. 论文提出通过母语者的词汇联想规范对LLMs进行微调，以捕捉文化知识。
3. 实验结果显示，微调后的模型在词汇对齐和文化价值对齐上均有显著提升，尤其是在与中国价值观的对齐上。

## 📝 摘要（中文）

大型语言模型（LLMs）在训练数据中表现出文化偏见，且由于文化知识的局限性，文化对齐仍然是一个挑战。本文提出了一种成本效益高且基于认知的微调方法，通过使用母语者的词汇联想规范来微调LLMs，利用认知心理学的发现，这些联想能够捕捉文化知识。我们使用来自美国（英语）和中国（普通话）的词汇联想数据集，对Llama-3.1-8B和Qwen-2.5-7B进行监督微调和偏好优化。通过涵盖词汇联想和文化价值对齐的双层评估框架，我们评估模型的文化对齐。结果显示，词汇对齐显著改善（英语提升16-20%，普通话提升43-165%），并且文化价值发生了显著变化。经过微调的Qwen在与中国价值观的响应对齐上几乎翻倍，显示出该方法的有效性和未来研究的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中的文化偏见问题，现有方法在文化对齐方面存在知识不足和学习方法不够有效的痛点。

**核心思路**：通过微调LLMs，利用母语者的词汇联想规范来捕捉文化知识，基于认知心理学的理论设计这一方法。

**技术框架**：整体流程包括数据收集、模型微调和评估三个主要阶段，首先收集来自美国和中国的词汇联想数据，然后对Llama-3.1-8B和Qwen-2.5-7B进行监督微调，最后通过双层评估框架进行效果评估。

**关键创新**：本研究的创新点在于利用文化背景的词汇联想进行模型微调，显著提升了模型的文化对齐能力，与传统方法相比，减少了对昂贵重训练的依赖。

**关键设计**：在微调过程中，采用了特定的损失函数和优化策略，以确保模型能够有效学习文化相关的词汇联想，具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，微调后的Qwen模型在与中国价值观的响应对齐上几乎翻倍，从13提升至25，且在词汇对齐上，英语提升16-20%，普通话提升43-165%。值得注意的是，经过微调的7-8B模型在性能上与70B基线模型相当或更优，显示出文化基础联想的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括跨文化交流、国际化的人工智能助手以及多语言翻译系统。通过改善模型的文化对齐能力，可以提升用户体验，减少文化误解，促进不同文化之间的理解与交流。未来，该方法可能为其他领域的AI模型提供借鉴，推动文化敏感性的发展。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit cultural bias from overrepresented viewpoints in training data, yet cultural alignment remains a challenge due to limited cultural knowledge and a lack of exploration into effective learning approaches. We introduce a cost-efficient and cognitively grounded method: fine-tuning LLMs on native speakers' word-association norms, leveraging cognitive psychology findings that such associations capture cultural knowledge. Using word association datasets from native speakers in the US (English) and China (Mandarin), we train Llama-3.1-8B and Qwen-2.5-7B via supervised fine-tuning and preference optimization. We evaluate models' cultural alignment through a two-tier evaluation framework that spans lexical associations and cultural value alignment using the World Values Survey. Results show significant improvements in lexical alignment (16-20% English, 43-165% Mandarin on Precision@5) and high-level cultural value shifts. On a subset of 50 questions where US and Chinese respondents diverge most, fine-tuned Qwen nearly doubles its response alignment with Chinese values (13 to 25). Remarkably, our trained 7-8B models match or exceed vanilla 70B baselines, demonstrating that a few million of culture-grounded associations achieve value alignment without expensive retraining. Our work highlights both the promise and the need for future research grounded in human cognition in improving cultural alignment in AI models.

