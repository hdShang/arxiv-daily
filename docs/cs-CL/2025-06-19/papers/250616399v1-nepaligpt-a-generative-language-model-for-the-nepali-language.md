---
layout: default
title: "NepaliGPT: A Generative Language Model for the Nepali Language"
---

# NepaliGPT: A Generative Language Model for the Nepali Language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16399" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16399v1</a>
  <a href="https://arxiv.org/pdf/2506.16399.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16399v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16399v1', 'NepaliGPT: A Generative Language Model for the Nepali Language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shushanta Pudasaini, Aman Shakya, Siddhartha Shrestha, Sahil Bhatta, Sunil Thapa, Sushmita Palikhe

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-19

**备注**: 11 pages, 9 figures

---

## 💡 一句话要点

**提出NepaliGPT以解决尼泊尔语生成模型缺失问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成语言模型` `尼泊尔语` `自然语言处理` `深度学习` `文本生成` `基准数据集`

## 📋 核心要点

1. 现有的尼泊尔语自然语言处理领域缺乏有效的生成语言模型，限制了相关研究的发展。
2. 本文提出NepaliGPT，专为尼泊尔语设计的生成大型语言模型，填补了这一空白。
3. NepaliGPT在文本生成任务中表现出色，困惑度为26.32245，ROUGE-1分数为0.2604，显示出良好的生成能力。

## 📝 摘要（中文）

随着ChatGPT的发布，大型语言模型（LLMs）在最近获得了巨大的关注，然而尼泊尔语缺乏生成语言模型，导致相关下游任务未被探索。为填补这一研究空白，本文提出了NepaliGPT，一个专为尼泊尔语量身定制的生成大型语言模型。研究引入了一个名为Devanagari Corpus的先进尼泊尔语语料库，并首次构建了包含4296对尼泊尔语问答的NepaliGPT基准数据集。NepaliGPT在文本生成方面取得了26.32245的困惑度、0.2604的ROUGE-1分数、81.25%的因果连贯性和85.41%的因果一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决尼泊尔语缺乏生成语言模型的问题，现有方法未能有效支持尼泊尔语的自然语言处理任务。

**核心思路**：提出NepaliGPT，专为尼泊尔语设计的生成大型语言模型，利用丰富的语料库和创新的模型架构，提升尼泊尔语的文本生成能力。

**技术框架**：NepaliGPT的整体架构包括数据收集、模型训练和评估三个主要阶段。数据收集阶段使用Devanagari Corpus，模型训练阶段采用先进的深度学习技术，评估阶段通过多项指标进行性能测试。

**关键创新**：NepaliGPT的主要创新在于构建了专门针对尼泊尔语的生成模型，并首次引入了针对该语言的基准数据集，显著提升了模型的适用性和性能。

**关键设计**：在模型设计中，采用了适合尼泊尔语特性的参数设置和损失函数，确保生成文本的连贯性和一致性，同时优化了网络结构以提高生成效率。

## 📊 实验亮点

NepaliGPT在文本生成任务中表现优异，取得了26.32245的困惑度和0.2604的ROUGE-1分数，因果连贯性达到81.25%，因果一致性为85.41%。这些结果表明，NepaliGPT在尼泊尔语生成任务中具有显著的性能提升，填补了该领域的研究空白。

## 🎯 应用场景

NepaliGPT的潜在应用场景包括教育、内容创作、智能客服等领域。通过提供高质量的尼泊尔语文本生成能力，该模型能够促进尼泊尔语的数字化发展，提升用户体验，并推动相关研究的深入。未来，NepaliGPT有望成为尼泊尔语自然语言处理的基础工具，助力更多应用的落地。

## 📄 摘要（原文）

> After the release of ChatGPT, Large Language Models (LLMs) have gained huge popularity in recent days and thousands of variants of LLMs have been released. However, there is no generative language model for the Nepali language, due to which other downstream tasks, including fine-tuning, have not been explored yet. To fill this research gap in the Nepali NLP space, this research proposes \textit{NepaliGPT}, a generative large language model tailored specifically for the Nepali language. This research introduces an advanced corpus for the Nepali language collected from several sources, called the Devanagari Corpus. Likewise, the research introduces the first NepaliGPT benchmark dataset comprised of 4,296 question-answer pairs in the Nepali language. The proposed LLM NepaliGPT achieves the following metrics in text generation: Perplexity of 26.32245, ROUGE-1 score of 0.2604, causal coherence of 81.25\%, and causal consistency of 85.41\%.

