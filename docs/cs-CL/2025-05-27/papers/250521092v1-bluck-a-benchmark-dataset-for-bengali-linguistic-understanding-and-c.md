---
layout: default
title: "BLUCK: A Benchmark Dataset for Bengali Linguistic Understanding and Cultural Knowledge"
---

# BLUCK: A Benchmark Dataset for Bengali Linguistic Understanding and Cultural Knowledge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21092" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21092v1</a>
  <a href="https://arxiv.org/pdf/2505.21092.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21092v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21092v1', 'BLUCK: A Benchmark Dataset for Bengali Linguistic Understanding and Cultural Knowledge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daeen Kabir, Minhajur Rahman Chowdhury Mahim, Sheikh Shafayat, Adnan Sadik, Arian Ahmed, Eunsu Kim, Alice Oh

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出BLUCK数据集以评估孟加拉语言理解与文化知识**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `孟加拉语言` `文化知识` `大型语言模型` `多项选择题` `数据集评估` `语言理解` `自然语言处理`

## 📋 核心要点

1. 现有大型语言模型在孟加拉语言理解和文化知识方面的表现仍显不足，尤其在孟加拉语音学领域存在明显短板。
2. BLUCK数据集通过2366道多项选择题，专注于评估LLMs在孟加拉文化和语言学方面的能力，填补了这一领域的研究空白。
3. 实验结果表明，尽管LLMs在整体表现上尚可，但在特定领域的表现仍需提升，显示出孟加拉语作为中等资源语言的潜力。

## 📝 摘要（中文）

在本研究中，我们介绍了BLUCK，一个旨在评估大型语言模型（LLMs）在孟加拉语言理解和文化知识方面表现的新数据集。该数据集包含2366道多项选择题（MCQs），这些题目经过精心策划，来源于多种大学和就业水平的考试，涵盖了孟加拉文化、历史和语言学的23个类别。我们使用6个专有和3个开源LLMs对BLUCK进行了基准测试，包括GPT-4o、Claude-3.5-Sonnet等。结果显示，尽管这些模型整体表现尚可，但在孟加拉语音学方面存在一定困难。尽管当前LLMs在孟加拉文化和语言背景下的表现仍无法与英语等主流语言相提并论，但我们的结果表明孟加拉语作为中等资源语言的地位。值得注意的是，BLUCK也是首个以本土孟加拉文化、历史和语言学为中心的多项选择题评估基准。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在孟加拉语言理解和文化知识评估中的不足，尤其是现有模型在孟加拉语音学方面的表现不佳。

**核心思路**：论文提出BLUCK数据集，包含多项选择题，专注于评估LLMs在孟加拉文化和语言学方面的能力，旨在为研究者提供一个标准化的评估工具。

**技术框架**：BLUCK数据集由2366道题目组成，涵盖23个类别，题目来源于多种考试，测试模型在不同文化和语言学知识上的表现。评估使用了6个专有和3个开源的LLMs。

**关键创新**：BLUCK是首个以本土孟加拉文化、历史和语言学为中心的多项选择题评估基准，填补了该领域的研究空白。

**关键设计**：数据集的设计考虑了多样性和代表性，确保题目涵盖广泛的文化和语言学知识，并通过严格的筛选过程确保题目的质量和有效性。实验中使用的模型包括GPT-4o、Claude-3.5-Sonnet等，提供了多样化的评估视角。

## 📊 实验亮点

实验结果表明，尽管LLMs在整体表现上表现良好，但在孟加拉语音学方面仍存在显著挑战。具体而言，当前模型在某些文化和语言学知识的准确性上与主流语言相比仍有差距，显示出进一步研究的必要性。

## 🎯 应用场景

BLUCK数据集的潜在应用领域包括教育、语言学习和人工智能研究。它可以帮助教育工作者评估学生的语言能力，也为开发更具文化适应性的语言模型提供了基础。此外，未来的研究可以基于BLUCK进一步探索孟加拉语的自然语言处理技术。

## 📄 摘要（原文）

> In this work, we introduce BLUCK, a new dataset designed to measure the performance of Large Language Models (LLMs) in Bengali linguistic understanding and cultural knowledge. Our dataset comprises 2366 multiple-choice questions (MCQs) carefully curated from compiled collections of several college and job level examinations and spans 23 categories covering knowledge on Bangladesh's culture and history and Bengali linguistics. We benchmarked BLUCK using 6 proprietary and 3 open-source LLMs - including GPT-4o, Claude-3.5-Sonnet, Gemini-1.5-Pro, Llama-3.3-70B-Instruct, and DeepSeekV3. Our results show that while these models perform reasonably well overall, they, however, struggles in some areas of Bengali phonetics. Although current LLMs' performance on Bengali cultural and linguistic contexts is still not comparable to that of mainstream languages like English, our results indicate Bengali's status as a mid-resource language. Importantly, BLUCK is also the first MCQ-based evaluation benchmark that is centered around native Bengali culture, history, and linguistics.

