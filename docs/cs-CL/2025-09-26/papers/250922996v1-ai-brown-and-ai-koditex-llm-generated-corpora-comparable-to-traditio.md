---
layout: default
title: "AI Brown and AI Koditex: LLM-Generated Corpora Comparable to Traditional Corpora of English and Czech Texts"
---

# AI Brown and AI Koditex: LLM-Generated Corpora Comparable to Traditional Corpora of English and Czech Texts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22996" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22996v1</a>
  <a href="https://arxiv.org/pdf/2509.22996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22996v1', 'AI Brown and AI Koditex: LLM-Generated Corpora Comparable to Traditional Corpora of English and Czech Texts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiří Milička, Anna Marklová, Václav Cvrček

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出AI Brown和AI Koditex，用于对比人类文本与LLM生成文本的英语和捷克语语料库。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `LLM生成文本` `语料库构建` `对比分析` `自然语言处理` `计算语言学` `通用依存关系`

## 📋 核心要点

1. 现有方法缺乏专门用于对比人类文本与LLM生成文本的语言学资源，阻碍了对LLM生成文本特性的深入研究。
2. 论文通过生成AI Brown和AI Koditex语料库，旨在提供可与现有的人工语料库进行比较的资源，促进对LLM生成文本的语言学分析。
3. 该语料库涵盖多种主题和文本类型，并使用多种LLM生成，经过通用依存关系标准标注，方便研究人员使用。

## 📝 摘要（中文）

本文介绍了两个使用大型语言模型（LLM）生成的英语和捷克语文本语料库：AI Brown和AI Koditex。其动机是创建一个资源，用于从语言学角度比较人类书写的文本与LLM生成的文本。重点在于确保这些资源是多领域、多主题、多作者和多文本类型的，同时保持与现有人工创建的语料库的可比性。这些生成的语料库复制了参考人类语料库：Paul Baker的BE21（原始Brown语料库的现代版本）和Koditex语料库（同样遵循Brown语料库的传统，但使用捷克语）。新语料库使用OpenAI、Anthropic、Alphabet、Meta和DeepSeek的模型生成，范围从GPT-3 (davinci-002)到GPT-4.5，并根据通用依存关系标准进行标记（即，它们被分词、词形还原，并进行形态和句法注释）。子语料库的大小因使用的模型而异（英语部分平均每个模型包含864k个token，总共27M个token，捷克语部分平均每个模型包含768k个token，总共21.5M个token）。这些语料库在CC BY 4.0许可下可免费下载（注释数据在CC BY-NC-SA 4.0许可下），并且可以通过捷克国家语料库的搜索界面访问。

## 🔬 方法详解

**问题定义**：论文旨在解决缺乏专门用于对比人类文本与LLM生成文本的语言学资源的问题。现有的人工语料库无法直接用于评估LLM生成文本的特性，而专门构建的对比语料库能够帮助研究人员更好地理解LLM的语言生成模式和潜在偏差。

**核心思路**：核心思路是模仿现有的人工语料库（BE21和Koditex）的结构和内容，使用多种LLM生成与之对应的语料库。通过控制生成过程中的主题、文本类型和作者等因素，确保生成的语料库与人工语料库具有可比性，从而能够进行有效的对比分析。

**技术框架**：整体框架包括以下几个阶段：1) 选择参考的人工语料库（BE21和Koditex）；2) 使用多种LLM（GPT-3到GPT-4.5）生成文本；3) 对生成的文本进行通用依存关系标准标注（分词、词形还原、形态和句法分析）；4) 构建可供下载和搜索的语料库。

**关键创新**：关键创新在于构建了可与现有的人工语料库直接对比的LLM生成语料库。通过控制生成过程，确保了语料库的多样性和可比性，为研究LLM的语言生成特性提供了新的资源。

**关键设计**：关键设计包括：1) 使用多种LLM以增加生成文本的多样性；2) 模仿人工语料库的结构和内容，确保可比性；3) 使用通用依存关系标准进行标注，方便研究人员使用现有的NLP工具进行分析；4) 子语料库大小根据模型进行调整，英语部分平均每个模型包含864k个token，捷克语部分平均每个模型包含768k个token。

## 📊 实验亮点

论文构建了大规模的英语和捷克语LLM生成语料库，总计分别包含27M和21.5M个token。该语料库使用多种LLM生成，并经过通用依存关系标准标注，可与现有的人工语料库进行对比分析，为研究LLM的语言生成特性提供了宝贵资源。

## 🎯 应用场景

该研究成果可应用于自然语言处理、计算语言学等领域，用于评估和改进LLM的语言生成能力，识别LLM生成文本中的潜在偏差，并深入理解LLM的语言模型。该语料库可促进对LLM生成文本的语言学分析，并为开发更可靠、更自然的LLM提供数据支持。

## 📄 摘要（原文）

> This article presents two corpora of English and Czech texts generated with large language models (LLMs). The motivation is to create a resource for comparing human-written texts with LLM-generated text linguistically. Emphasis was placed on ensuring these resources are multi-genre and rich in terms of topics, authors, and text types, while maintaining comparability with existing human-created corpora. These generated corpora replicate reference human corpora: BE21 by Paul Baker, which is a modern version of the original Brown Corpus, and Koditex corpus that also follows the Brown Corpus tradition but in Czech. The new corpora were generated using models from OpenAI, Anthropic, Alphabet, Meta, and DeepSeek, ranging from GPT-3 (davinci-002) to GPT-4.5, and are tagged according to the Universal Dependencies standard (i.e., they are tokenized, lemmatized, and morphologically and syntactically annotated). The subcorpus size varies according to the model used (the English part contains on average 864k tokens per model, 27M tokens altogether, the Czech partcontains on average 768k tokens per model, 21.5M tokens altogether). The corpora are freely available for download under the CC BY 4.0 license (the annotated data are under CC BY-NC-SA 4.0 licence) and are also accessible through the search interface of the Czech National Corpus.

