---
layout: default
title: FABLE: A Novel Data-Flow Analysis Benchmark on Procedural Text for Large Language Model Evaluation
---

# FABLE: A Novel Data-Flow Analysis Benchmark on Procedural Text for Large Language Model Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24258" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24258v1</a>
  <a href="https://arxiv.org/pdf/2505.24258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24258v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24258v1', 'FABLE: A Novel Data-Flow Analysis Benchmark on Procedural Text for Large Language Model Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vishal Pallagani, Nitin Gupta, John Aydin, Biplav Srivastava

**分类**: cs.AI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出FABLE基准以评估大语言模型的数据流推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据流分析` `大型语言模型` `程序性任务` `基准评估` `推理能力` `软件工程` `人工智能`

## 📋 核心要点

1. 现有的大语言模型在程序性任务的数据流推理能力上缺乏系统性的评估，导致其应用效果不佳。
2. FABLE基准通过适配经典的数据流分析方法，提供了一个结构化的评估框架，专注于程序性文本的理解。
3. 实验表明，推理专注的模型在准确性上表现优异，但推理速度显著低于其他模型，后者表现接近随机水平。

## 📝 摘要（中文）

理解数据如何移动、转化和持久化，即数据流，是进行程序性任务推理的基础。尽管大型语言模型（LLMs）在自然语言和编程语言中表现出流利性，但它们在程序性任务的数据流推理能力方面尚未得到系统评估。本文提出了FABLE，一个可扩展的基准，旨在通过结构化的程序性文本评估LLMs对数据流的理解。FABLE适配了八种经典的数据流分析方法，并在烹饪食谱、旅行路线和自动化计划三个真实领域中实例化。基准包含2400个问答对，评估了三种类型的LLMs。实验结果表明，推理模型的准确性更高，但推理速度比其他模型慢20倍以上，而通用模型和代码特定模型的表现接近随机猜测。FABLE为系统评估数据流推理提供了首个诊断基准，并为开发更强的程序理解模型提供了见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在程序性任务中对数据流推理能力的评估不足，现有方法未能有效衡量这一能力的表现。

**核心思路**：FABLE基准通过引入八种经典的数据流分析方法，结合真实世界的程序性文本，系统地评估LLMs对数据流的理解能力。

**技术框架**：FABLE的整体架构包括数据流分析模块和问答生成模块，涵盖烹饪、旅行和自动化计划三个领域，每个领域包含100个示例，形成2400个问答对。

**关键创新**：FABLE是首个专注于数据流推理的基准，提供了系统化的评估方法，填补了现有LLMs评估的空白。

**关键设计**：在实验中，使用了三种不同类型的LLMs，采用五次采样的多数投票机制进行评估，确保结果的可靠性和准确性。

## 📊 实验亮点

实验结果显示，推理专注的模型在数据流推理任务中准确率显著高于其他模型，尽管其推理速度慢于20倍。通用模型和代码特定模型的表现接近随机水平，表明FABLE基准在评估LLMs的有效性方面具有重要意义。

## 🎯 应用场景

FABLE基准的潜在应用领域包括软件工程、教育和自动化决策等。通过系统评估LLMs的数据流推理能力，可以为相关领域的模型开发提供指导，提升模型在复杂程序性任务中的表现，进而推动智能系统的实际应用和发展。

## 📄 摘要（原文）

> Understanding how data moves, transforms, and persists, known as data flow, is fundamental to reasoning in procedural tasks. Despite their fluency in natural and programming languages, large language models (LLMs), although increasingly being applied to decisions with procedural tasks, have not been systematically evaluated for their ability to perform data-flow reasoning. We introduce FABLE, an extensible benchmark designed to assess LLMs' understanding of data flow using structured, procedural text. FABLE adapts eight classical data-flow analyses from software engineering: reaching definitions, very busy expressions, available expressions, live variable analysis, interval analysis, type-state analysis, taint analysis, and concurrency analysis. These analyses are instantiated across three real-world domains: cooking recipes, travel routes, and automated plans. The benchmark includes 2,400 question-answer pairs, with 100 examples for each domain-analysis combination. We evaluate three types of LLMs: a reasoning-focused model (DeepSeek-R1 8B), a general-purpose model (LLaMA 3.1 8B), and a code-specific model (Granite Code 8B). Each model is tested using majority voting over five sampled completions per prompt. Results show that the reasoning model achieves higher accuracy, but at the cost of over 20 times slower inference compared to the other models. In contrast, the general-purpose and code-specific models perform close to random chance. FABLE provides the first diagnostic benchmark to systematically evaluate data-flow reasoning and offers insights for developing models with stronger procedural understanding.

