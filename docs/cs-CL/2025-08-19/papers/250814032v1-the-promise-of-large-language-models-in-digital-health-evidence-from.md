---
layout: default
title: "The Promise of Large Language Models in Digital Health: Evidence from Sentiment Analysis in Online Health Communities"
---

# The Promise of Large Language Models in Digital Health: Evidence from Sentiment Analysis in Online Health Communities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14032" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14032v1</a>
  <a href="https://arxiv.org/pdf/2508.14032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14032v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14032v1', 'The Promise of Large Language Models in Digital Health: Evidence from Sentiment Analysis in Online Health Communities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiancheng Li, Georgios D. Karampatakis, Helen E. Wood, Chris J. Griffiths, Borislava Mihaylova, Neil S. Coulson, Alessio Pasinato, Pietro Panzarasa, Marco Viviani, Anna De Simoni

**分类**: cs.CL

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**利用大型语言模型解决数字健康领域情感分析挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `情感分析` `数字健康` `在线健康社区` `专家知识整合` `上下文学习` `机器学习` `数据隐私`

## 📋 核心要点

1. 现有方法在处理患者生成的健康内容时面临数据短缺和隐私限制，导致情感分析的准确性不足。
2. 论文提出通过大型语言模型结合上下文学习和结构化编码书，来整合专家知识以提升情感分析的效果。
3. 实验结果显示，LLM在情感分析中表现优于传统方法，且与专家标注的一致性达到专家水平，具有显著的实用价值。

## 📝 摘要（中文）

数字健康分析面临着关键挑战，尤其是在处理患者生成的健康内容时。这些内容通常包含复杂的情感和医学背景，传统机器学习方法受到数据短缺和隐私限制的制约。在线健康社区的混合情感帖子和隐含情感表达要求专业知识以进行准确的情感分析。本文探讨了大型语言模型如何通过上下文学习整合专家知识，为健康数据分析提供可扩展的解决方案。研究开发了一种结构化的编码书，系统编码专家解释指南，使大型语言模型能够通过针对性提示应用领域特定知识。实验结果表明，LLM在情感分析中表现优越，且与专家间的协议水平无显著差异，表明其知识整合超越了表面模式识别。

## 🔬 方法详解

**问题定义**：本文旨在解决数字健康领域情感分析中的专家知识短缺和数据隐私限制问题。现有的传统机器学习方法在处理复杂情感和医学术语时效果不佳，难以满足实际需求。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）通过上下文学习整合专家知识，而不是依赖于大量的训练数据。这种方法能够在不需要全面训练的情况下，快速适应特定领域的情感分析任务。

**技术框架**：整体架构包括数据收集、结构化编码书的开发、LLM的训练与评估。首先，收集来自在线健康社区的帖子，然后根据专家解释指南构建编码书，最后利用LLMs进行情感分析并与传统方法进行比较。

**关键创新**：最重要的技术创新在于通过结构化编码书实现了专家知识的有效整合，使得LLMs能够在情感分析中达到与专家相当的表现，超越了传统方法的局限。

**关键设计**：在模型设计中，采用了针对性提示的方式来引导LLMs进行情感分析，避免了大规模训练的需求。实验中使用了400个专家标注的帖子进行验证，并与BioBERT和词典方法进行了对比。

## 📊 实验亮点

实验结果显示，LLMs在情感分析中的表现显著优于BioBERT等传统方法，且与专家标注的一致性达到专家水平，表明其在数字健康分析中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括患者监测、干预评估和基于证据的健康策略制定。通过提供实时的专家级情感分析，能够帮助医疗专业人员更好地理解患者需求和情感状态，从而改善医疗服务质量和患者体验。

## 📄 摘要（原文）

> Digital health analytics face critical challenges nowadays. The sophisticated analysis of patient-generated health content, which contains complex emotional and medical contexts, requires scarce domain expertise, while traditional ML approaches are constrained by data shortage and privacy limitations in healthcare settings. Online Health Communities (OHCs) exemplify these challenges with mixed-sentiment posts, clinical terminology, and implicit emotional expressions that demand specialised knowledge for accurate Sentiment Analysis (SA). To address these challenges, this study explores how Large Language Models (LLMs) can integrate expert knowledge through in-context learning for SA, providing a scalable solution for sophisticated health data analysis. Specifically, we develop a structured codebook that systematically encodes expert interpretation guidelines, enabling LLMs to apply domain-specific knowledge through targeted prompting rather than extensive training. Six GPT models validated alongside DeepSeek and LLaMA 3.1 are compared with pre-trained language models (BioBERT variants) and lexicon-based methods, using 400 expert-annotated posts from two OHCs. LLMs achieve superior performance while demonstrating expert-level agreement. This high agreement, with no statistically significant difference from inter-expert agreement levels, suggests knowledge integration beyond surface-level pattern recognition. The consistent performance across diverse LLM models, supported by in-context learning, offers a promising solution for digital health analytics. This approach addresses the critical challenge of expert knowledge shortage in digital health research, enabling real-time, expert-quality analysis for patient monitoring, intervention assessment, and evidence-based health strategies.

