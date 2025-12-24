---
layout: default
title: "How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages"
---

# How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15518" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15518v1</a>
  <a href="https://arxiv.org/pdf/2509.15518.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15518v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15518v1', 'How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyang Wu, Zhewei Sun

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**系统比较人类与LLM生成俚语用法，揭示LLM在俚语理解上的偏差**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `俚语生成` `俚语理解` `偏差分析` `自然语言处理`

## 📋 核心要点

1. 现有NLP系统在处理俚语等非正式语言时面临挑战，缺乏对俚语结构知识的深入理解。
2. 该研究通过系统比较人类与LLM生成的俚语用法，评估LLM在俚语理解上的能力和偏差。
3. 实验结果表明，LLM在俚语创造性方面有所掌握，但在理解人类俚语用法方面存在显著偏差。

## 📝 摘要（中文）

俚语是一种常用的非正式语言，对自然语言处理系统构成了严峻的挑战。然而，大型语言模型（LLM）的最新进展使这个问题变得更容易解决。虽然LLM代理正被越来越广泛地应用于中间任务，如俚语检测和俚语解释，但它们的泛化性和可靠性在很大程度上取决于这些模型是否已经掌握了与人类认可的俚语用法良好对齐的俚语结构知识。为了回答这个问题，我们对人类和机器生成的俚语用法进行了系统的比较。我们的评估框架侧重于三个核心方面：1) 反映机器如何看待俚语的系统性偏差的用法特征，2) 俚语用法中使用的词汇创造和单词重用所反映的创造力，以及 3) 当用作模型蒸馏的黄金标准示例时，俚语用法的信息量。通过比较来自在线俚语词典（OSD）的人类认可的俚语用法和GPT-4o和Llama-3生成的俚语，我们发现LLM在如何看待俚语方面存在显著偏差。我们的结果表明，虽然LLM已经掌握了关于俚语创造性方面的重要知识，但这些知识与人类的知识不够一致，无法使LLM用于诸如语言分析等外推任务。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在俚语理解和生成方面存在的偏差问题。现有方法无法保证LLM生成的俚语用法与人类的认知对齐，导致其在俚语相关的NLP任务中表现不佳。现有方法的痛点在于缺乏对LLM俚语生成能力的系统性评估和分析。

**核心思路**：论文的核心思路是通过对比分析人类和LLM生成的俚语用法，揭示LLM在俚语理解上的偏差。通过评估LLM在俚语用法特征、创造性和信息量三个方面的表现，从而判断LLM是否掌握了与人类一致的俚语结构知识。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 从在线俚语词典（OSD）收集人类认可的俚语用法作为基准；2) 使用GPT-4o和Llama-3等LLM生成俚语用法；3) 设计评估框架，从用法特征、创造性和信息量三个方面对人类和LLM生成的俚语用法进行对比分析；4) 分析实验结果，揭示LLM在俚语理解上的偏差。

**关键创新**：该研究的关键创新在于提出了一个系统性的评估框架，用于对比分析人类和LLM生成的俚语用法，从而揭示LLM在俚语理解上的偏差。该框架从用法特征、创造性和信息量三个方面对俚语用法进行评估，能够全面地评估LLM在俚语理解上的能力。

**关键设计**：在用法特征方面，研究分析了LLM生成的俚语用法中词性、句法结构等特征的分布，并与人类生成的俚语用法进行对比。在创造性方面，研究评估了LLM在词汇创造和单词重用方面的能力。在信息量方面，研究评估了LLM生成的俚语用法作为模型蒸馏的黄金标准示例时的效果。

## 📊 实验亮点

实验结果表明，虽然LLM在俚语创造性方面有所掌握，但在理解人类俚语用法方面存在显著偏差。具体来说，LLM生成的俚语用法在词性分布、句法结构等方面与人类生成的俚语用法存在差异。此外，LLM生成的俚语用法作为模型蒸馏的黄金标准示例时的效果不如人类生成的俚语用法。

## 🎯 应用场景

该研究成果可应用于提升LLM在俚语理解和生成方面的能力，从而改善其在社交媒体分析、情感分析、对话系统等领域的表现。此外，该研究提出的评估框架可用于评估其他语言模型在处理非正式语言方面的能力，为语言模型的开发和评估提供参考。

## 📄 摘要（原文）

> Slang is a commonly used type of informal language that poses a daunting challenge to NLP systems. Recent advances in large language models (LLMs), however, have made the problem more approachable. While LLM agents are becoming more widely applied to intermediary tasks such as slang detection and slang interpretation, their generalizability and reliability are heavily dependent on whether these models have captured structural knowledge about slang that align well with human attested slang usages. To answer this question, we contribute a systematic comparison between human and machine-generated slang usages. Our evaluative framework focuses on three core aspects: 1) Characteristics of the usages that reflect systematic biases in how machines perceive slang, 2) Creativity reflected by both lexical coinages and word reuses employed by the slang usages, and 3) Informativeness of the slang usages when used as gold-standard examples for model distillation. By comparing human-attested slang usages from the Online Slang Dictionary (OSD) and slang generated by GPT-4o and Llama-3, we find significant biases in how LLMs perceive slang. Our results suggest that while LLMs have captured significant knowledge about the creative aspects of slang, such knowledge does not align with humans sufficiently to enable LLMs for extrapolative tasks such as linguistic analyses.

