---
layout: default
title: "CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis"
---

# CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10886" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10886v1</a>
  <a href="https://arxiv.org/pdf/2509.10886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10886v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10886v1', 'CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyu Zhang, Pei Zhang, Shuang Luo, Jialong Tang, Yu Wan, Baosong Yang, Fei Huang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-13

**备注**: Accepted as a Findings paper at EMNLP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Eyr3/CultureSynth)

---

## 💡 一句话要点

**CultureSynth：提出层级分类引导和检索增强的文化问答合成框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文化能力` `大型语言模型` `检索增强生成` `层级分类体系` `多语言评估` `知识库` `问答合成`

## 📋 核心要点

1. 现有文化评估基准存在分类体系分散、领域特定性强和过度依赖人工标注的问题。
2. CultureSynth利用层级文化分类体系和检索增强生成，自动合成大规模文化相关的问答对。
3. 实验表明，模型规模、架构和地理位置都会影响LLMs的文化能力，并构建了包含多种语言的评测基准。

## 📝 摘要（中文）

为了提升大型语言模型(LLMs)在全球环境下的文化能力，本文提出了CultureSynth框架。该框架包含：(1)一个全面的多语言层级文化分类体系，涵盖12个一级主题和130个二级主题；(2)一种基于检索增强生成(RAG)的方法，利用事实知识合成文化相关的问答对。CultureSynth-7合成基准包含19,360个条目，其中4,149个经过人工验证，覆盖7种语言。对14个不同规模的LLMs的评估表明，ChatGPT-4o-Latest和Qwen2.5-72B-Instruct表现领先。结果表明，达到基本的文化能力需要30亿参数的模型，模型在知识处理中表现出不同的架构偏差，并且模型之间存在显著的地域差异。CultureSynth提供了一个可扩展的框架，用于开发具有文化意识的AI系统，同时减少对人工标注的依赖。

## 🔬 方法详解

**问题定义**：当前大型语言模型在全球化应用中，文化能力至关重要。然而，现有的文化评估基准存在诸多问题，例如分类体系不完整，缺乏统一的标准；领域特定性强，难以泛化到不同场景；以及严重依赖人工标注，成本高昂且难以扩展。这些问题阻碍了文化意识AI系统的发展。

**核心思路**：CultureSynth的核心思路是利用结构化的文化知识体系和检索增强生成技术，自动化地合成大规模、高质量的文化相关问答对。通过构建一个全面的文化分类体系，并结合外部知识库，模型可以生成更具文化背景和上下文的问答，从而更有效地评估和提升LLMs的文化能力。

**技术框架**：CultureSynth框架主要包含两个核心模块：一是层级文化分类体系，二是检索增强生成(RAG)模块。层级文化分类体系定义了12个一级主题和130个二级主题，用于组织和管理文化知识。RAG模块首先根据给定的文化主题，从外部知识库中检索相关的事实知识，然后利用这些知识生成相应的问答对。整个流程无需大量人工标注，可以实现高效的文化问答对合成。

**关键创新**：CultureSynth的关键创新在于其综合利用了层级分类体系和检索增强生成技术。传统的文化评估方法往往依赖于人工标注的数据，而CultureSynth通过自动化合成数据的方式，大大降低了成本和提高了效率。此外，层级分类体系的引入使得模型可以更好地理解文化知识的结构和关系，从而生成更具文化深度的问答。

**关键设计**：在RAG模块中，使用了预训练语言模型作为生成器，并采用了一种基于相似度匹配的检索策略，从外部知识库中选择最相关的知识片段。具体而言，使用了余弦相似度来衡量查询和知识片段之间的语义相似度，并选择相似度最高的Top-K个片段作为生成器的输入。此外，还使用了数据过滤策略，对生成的数据进行质量控制，以确保数据的准确性和一致性。

## 📊 实验亮点

在CultureSynth-7基准测试中，ChatGPT-4o-Latest和Qwen2.5-72B-Instruct表现领先，验证了该基准的有效性。实验结果还表明，模型规模是影响文化能力的关键因素，至少需要30亿参数的模型才能达到基本的文化能力。此外，不同架构的模型在知识处理方面存在差异，且模型在不同地理区域的表现也存在显著差异。

## 🎯 应用场景

CultureSynth框架可应用于开发更具文化意识的AI系统，例如多语言聊天机器人、跨文化交流工具和全球化教育平台。通过提升LLMs的文化理解能力，可以减少文化误解和偏见，促进不同文化之间的交流与合作。该研究还有助于构建更公平、包容和负责任的AI系统。

## 📄 摘要（原文）

> Cultural competence, defined as the ability to understand and adapt to multicultural contexts, is increasingly vital for large language models (LLMs) in global environments. While several cultural benchmarks exist to assess LLMs' cultural competence, current evaluations suffer from fragmented taxonomies, domain specificity, and heavy reliance on manual data annotation. To address these limitations, we introduce CultureSynth, a novel framework comprising (1) a comprehensive hierarchical multilingual cultural taxonomy covering 12 primary and 130 secondary topics, and (2) a Retrieval-Augmented Generation (RAG)-based methodology leveraging factual knowledge to synthesize culturally relevant question-answer pairs. The CultureSynth-7 synthetic benchmark contains 19,360 entries and 4,149 manually verified entries across 7 languages. Evaluation of 14 prevalent LLMs of different sizes reveals clear performance stratification led by ChatGPT-4o-Latest and Qwen2.5-72B-Instruct. The results demonstrate that a 3B-parameter threshold is necessary for achieving basic cultural competence, models display varying architectural biases in knowledge processing, and significant geographic disparities exist across models. We believe that CultureSynth offers a scalable framework for developing culturally aware AI systems while reducing reliance on manual annotation\footnote{Benchmark is available at https://github.com/Eyr3/CultureSynth.}.

