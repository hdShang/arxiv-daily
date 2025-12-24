---
layout: default
title: "Measuring (a Sufficient) World Model in LLMs: A Variance Decomposition Framework"
---

# Measuring (a Sufficient) World Model in LLMs: A Variance Decomposition Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16584" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16584v1</a>
  <a href="https://arxiv.org/pdf/2506.16584.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16584v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16584v1', 'Measuring (a Sufficient) World Model in LLMs: A Variance Decomposition Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nadav Kunievsky, James A. Evans

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出方差分解框架以评估大型语言模型的世界模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `世界模型` `方差分解` `模型评估` `自然语言处理` `语义理解`

## 📋 核心要点

1. 核心问题：现有方法未能有效评估大型语言模型的世界模型，尤其是在高风险应用中的可靠性。
2. 方法要点：提出方差分解框架，通过分析模型响应的变异性来评估其世界模型的稳健性。
3. 实验或效果：实验结果显示，较大模型在输出变异性中更依赖于用户目的，表明其世界模型更为稳健。

## 📝 摘要（中文）

理解大型语言模型（LLMs）是否具备世界模型，即对世界的结构化理解，对于评估其在高风险应用中的可靠性至关重要。本文提出了一种正式框架，用于评估LLM是否展现出足够稳健的世界模型，定义为在语义等价的提示下产生一致的输出，同时区分表达不同意图的提示。我们引入了一种新的评估方法，将模型响应的变异性分解为三个组成部分：用户目的、用户表达和模型不稳定性。结果表明，较大的模型在输出变异性中更大程度地归因于用户目的的变化，表明其世界模型更为稳健。这一改进并不均匀，较大的模型在所有领域并不总是优于较小的模型，且其稳健性优势往往有限。

## 🔬 方法详解

**问题定义**：本文旨在解决如何评估大型语言模型是否具备稳健的世界模型的问题。现有方法往往侧重于准确性，未能深入分析模型的内部理解结构和稳定性。

**核心思路**：论文提出了一种方差分解框架，旨在通过将模型响应的变异性分解为用户目的、用户表达和模型不稳定性三个部分，来量化模型的世界模型的稳健性。这样的设计使得我们能够更清晰地理解模型行为的根源。

**技术框架**：整体架构包括三个主要模块：1) 用户目的的定义与识别；2) 用户表达的变化分析；3) 模型不稳定性的评估。通过这些模块的协同工作，能够全面评估模型的世界模型。

**关键创新**：最重要的技术创新在于引入了方差分解的方法，使得我们能够量化模型响应的变异性来源。这与现有方法的本质区别在于，后者通常只关注输出的准确性，而忽视了模型内部理解的结构。

**关键设计**：在设计中，关键参数包括用户目的的分类标准、表达变化的度量方式，以及模型不稳定性的评估指标。这些设计确保了评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，较大的语言模型在输出变异性中，约有更高比例归因于用户目的的变化，表明其世界模型更为稳健。尽管如此，较大模型在所有领域的表现并不一致，且其优势往往有限，提示我们需要更深入的研究。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和自动化内容生成等。通过更好地理解和评估大型语言模型的世界模型，可以提高其在复杂任务中的可靠性和适应性，进而推动高风险应用的安全性和有效性。

## 📄 摘要（原文）

> Understanding whether large language models (LLMs) possess a world model-a structured understanding of the world that supports generalization beyond surface-level patterns-is central to assessing their reliability, especially in high-stakes applications. We propose a formal framework for evaluating whether an LLM exhibits a sufficiently robust world model, defined as producing consistent outputs across semantically equivalent prompts while distinguishing between prompts that express different intents. We introduce a new evaluation approach to measure this that decomposes model response variability into three components: variability due to user purpose, user articulation, and model instability. An LLM with a strong world model should attribute most of the variability in its responses to changes in foundational purpose rather than superficial changes in articulation. This approach allows us to quantify how much of a model's behavior is semantically grounded rather than driven by model instability or alternative wording. We apply this framework to evaluate LLMs across diverse domains. Our results show how larger models attribute a greater share of output variability to changes in user purpose, indicating a more robust world model. This improvement is not uniform, however: larger models do not consistently outperform smaller ones across all domains, and their advantage in robustness is often modest. These findings highlight the importance of moving beyond accuracy-based benchmarks toward semantic diagnostics that more directly assess the structure and stability of a model's internal understanding of the world.

