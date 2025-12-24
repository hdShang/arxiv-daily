---
layout: default
title: "Deciphering Emotions in Children Storybooks: A Comparative Analysis of Multimodal LLMs in Educational Applications"
---

# Deciphering Emotions in Children Storybooks: A Comparative Analysis of Multimodal LLMs in Educational Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18201" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18201v1</a>
  <a href="https://arxiv.org/pdf/2506.18201.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18201v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18201v1', 'Deciphering Emotions in Children Storybooks: A Comparative Analysis of Multimodal LLMs in Educational Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bushra Asseri, Estabraq Abdelaziz, Maha Al Mogren, Tayef Alhefdhi, Areej Al-Wabil

**分类**: cs.CL, cs.CV, cs.HC

**发布日期**: 2025-06-22

**DOI**: [10.3390/ai6090211](https://doi.org/10.3390/ai6090211)

---

## 💡 一句话要点

**评估多模态大语言模型在儿童故事书情感识别中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感识别` `多模态学习` `大语言模型` `教育技术` `阿拉伯语` `文化适应性` `儿童故事书`

## 📋 核心要点

1. 现有多模态AI系统在阿拉伯语环境中的情感识别能力不足，缺乏文化适应性学习工具。
2. 本文通过评估GPT-4o和Gemini 1.5 Pro在儿童故事书插图中的表现，提出了多种提示策略以提升情感识别效果。
3. 实验结果显示，GPT-4o在所有条件下表现优于Gemini，尤其在链式思维提示下，宏观F1分数提升显著。

## 📝 摘要（中文）

情感识别能力在多模态人工智能系统中至关重要，尤其是在阿拉伯语环境中，文化适应性学习工具的需求迫切。本文评估了两种先进的多模态大语言模型GPT-4o和Gemini 1.5 Pro在处理阿拉伯儿童故事书插图时的情感识别性能。通过对75幅来自七本阿拉伯故事书的图像进行零-shot、few-shot和链式思维三种提示策略的评估，结果显示GPT-4o在所有条件下均优于Gemini，链式思维提示下的宏观F1分数达到59%，而Gemini的最佳表现为43%。错误分析揭示了系统性的误分类模式，情感价值反转占错误的60.7%，而两个模型在处理文化细腻情感和模糊叙事上下文时均表现不佳。这些发现突显了当前模型在文化理解方面的基本局限性，并强调了开发针对阿拉伯语学习者的情感感知教育技术所需的文化敏感训练方法。

## 🔬 方法详解

**问题定义**：本研究旨在解决阿拉伯语儿童故事书插图中的情感识别问题，现有方法在文化适应性和情感细腻度上存在不足。

**核心思路**：通过比较两种多模态大语言模型在不同提示策略下的表现，探索如何提升情感识别的准确性和文化适应性。

**技术框架**：研究采用了GPT-4o和Gemini 1.5 Pro模型，使用零-shot、few-shot和链式思维三种提示策略对75幅插图进行评估，结合人类注释进行对比分析。

**关键创新**：本研究的创新点在于系统性地评估了多模态大语言模型在特定文化背景下的情感识别能力，揭示了模型在处理文化细腻情感时的局限性。

**关键设计**：实验中采用了Plutchik的情感框架进行人类注释，设置了不同的提示策略以观察模型表现，分析了误分类的原因，特别关注情感价值反转和文化细腻情感的处理。

## 📊 实验亮点

实验结果显示，GPT-4o在链式思维提示下的宏观F1分数达到59%，显著高于Gemini的最佳表现43%。错误分析表明，情感价值反转是主要误分类原因，占错误的60.7%。这突显了当前模型在文化情感理解上的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、儿童心理发展和文化适应性学习工具的开发。通过提升情感识别能力，能够为阿拉伯语学习者提供更有效的学习体验，促进情感理解与文化认同。未来，这一研究方向可能推动多模态AI在教育领域的广泛应用。

## 📄 摘要（原文）

> Emotion recognition capabilities in multimodal AI systems are crucial for developing culturally responsive educational technologies, yet remain underexplored for Arabic language contexts where culturally appropriate learning tools are critically needed. This study evaluates the emotion recognition performance of two advanced multimodal large language models, GPT-4o and Gemini 1.5 Pro, when processing Arabic children's storybook illustrations. We assessed both models across three prompting strategies (zero-shot, few-shot, and chain-of-thought) using 75 images from seven Arabic storybooks, comparing model predictions with human annotations based on Plutchik's emotional framework. GPT-4o consistently outperformed Gemini across all conditions, achieving the highest macro F1-score of 59% with chain-of-thought prompting compared to Gemini's best performance of 43%. Error analysis revealed systematic misclassification patterns, with valence inversions accounting for 60.7% of errors, while both models struggled with culturally nuanced emotions and ambiguous narrative contexts. These findings highlight fundamental limitations in current models' cultural understanding and emphasize the need for culturally sensitive training approaches to develop effective emotion-aware educational technologies for Arabic-speaking learners.

