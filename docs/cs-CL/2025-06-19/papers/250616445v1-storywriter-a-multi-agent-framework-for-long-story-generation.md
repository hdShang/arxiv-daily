---
layout: default
title: "StoryWriter: A Multi-Agent Framework for Long Story Generation"
---

# StoryWriter: A Multi-Agent Framework for Long Story Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16445" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16445v1</a>
  <a href="https://arxiv.org/pdf/2506.16445.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16445v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16445v1', 'StoryWriter: A Multi-Agent Framework for Long Story Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Xia, Hao Peng, Yunjia Qi, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出StoryWriter框架以解决长篇故事生成中的连贯性与复杂性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长篇故事生成` `多代理系统` `叙述连贯性` `叙事复杂性` `自然语言处理` `大型语言模型` `故事创作` `自动化评估`

## 📋 核心要点

1. 长篇故事生成面临叙述连贯性和叙事复杂性等挑战，现有方法难以有效解决这些问题。
2. 本文提出的StoryWriter框架通过大纲代理、规划代理和写作代理三个模块，系统性地解决了故事生成中的连贯性与复杂性问题。
3. 实验结果表明，StoryWriter在故事质量和长度上显著优于现有基线，且生成的数据集包含约6000个高质量长篇故事。

## 📝 摘要（中文）

长篇故事生成对现有的大型语言模型（LLMs）仍然是一个挑战，主要由于两个因素：叙述连贯性和叙事复杂性。为了解决这些问题，本文提出了StoryWriter，一个多代理故事生成框架，包含三个主要模块：大纲代理、规划代理和写作代理。通过人类和自动化评估，StoryWriter在故事质量和长度上显著超越了现有的生成基线。此外，使用StoryWriter生成了一个包含约6000个高质量长篇故事的数据集，平均长度为8000字。我们在LongStory上对Llama3.1-8B和GLM4-9B进行了监督微调，开发了StoryWriter_GLM，展示了在长篇故事生成中的先进性能。

## 🔬 方法详解

**问题定义**：长篇故事生成需要保持叙述的连贯性和复杂性，现有方法在这两方面表现不佳，导致生成的故事缺乏逻辑性和吸引力。

**核心思路**：StoryWriter通过多代理系统，分别处理故事的大纲生成、事件规划和具体写作，以确保生成故事的结构性和连贯性。

**技术框架**：StoryWriter框架包含三个主要模块：大纲代理负责生成事件基础的大纲，规划代理细化事件并规划章节内容，写作代理则动态压缩故事历史以生成新情节。

**关键创新**：StoryWriter的创新在于其多代理设计，使得故事生成过程更加系统化和模块化，能够有效处理长篇故事的复杂性与连贯性问题。

**关键设计**：在模型训练中，使用了Llama3.1-8B和GLM4-9B进行监督微调，确保生成的故事在质量和长度上达到预期标准。

## 📊 实验亮点

实验结果显示，StoryWriter在故事质量和长度上显著优于现有基线，具体表现为生成故事的平均长度达到8000字，且质量评估结果明显提升，展示了其在长篇故事生成中的先进性能。

## 🎯 应用场景

该研究的潜在应用领域包括文学创作、游戏剧情生成和教育领域的故事教学等。通过提供高质量的长篇故事生成能力，StoryWriter能够为创作者和教育者提供强有力的工具，提升创作效率和故事质量，未来可能对内容创作行业产生深远影响。

## 📄 摘要（原文）

> Long story generation remains a challenge for existing large language models (LLMs), primarily due to two main factors: (1) discourse coherence, which requires plot consistency, logical coherence, and completeness in the long-form generation, and (2) narrative complexity, which requires an interwoven and engaging narrative. To address these challenges, we propose StoryWriter, a multi-agent story generation framework, which consists of three main modules: (1) outline agent, which generates event-based outlines containing rich event plots, character, and event-event relationships. (2) planning agent, which further details events and plans which events should be written in each chapter to maintain an interwoven and engaging story. (3) writing agent, which dynamically compresses the story history based on the current event to generate and reflect new plots, ensuring the coherence of the generated story. We conduct both human and automated evaluation, and StoryWriter significantly outperforms existing story generation baselines in both story quality and length. Furthermore, we use StoryWriter to generate a dataset, which contains about $6,000$ high-quality long stories, with an average length of $8,000$ words. We train the model Llama3.1-8B and GLM4-9B using supervised fine-tuning on LongStory and develop StoryWriter_GLM and StoryWriter_GLM, which demonstrates advanced performance in long story generation.

