---
layout: default
title: "TUMS: Enhancing Tool-use Abilities of LLMs with Multi-structure Handlers"
---

# TUMS: Enhancing Tool-use Abilities of LLMs with Multi-structure Handlers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08402" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08402v1</a>
  <a href="https://arxiv.org/pdf/2505.08402.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08402v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08402v1', 'TUMS: Enhancing Tool-use Abilities of LLMs with Multi-structure Handlers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aiyao He, Sijia Cui, Shuai Xu, Yanna Wang, Bo Xu

**分类**: cs.CL

**发布日期**: 2025-05-13

**备注**: Accepted to ICONIP 2024

---

## 💡 一句话要点

**提出TUMS框架以提升LLMs的工具使用能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `工具使用` `自然语言处理` `任务分解` `参数生成` `智能助手` `多结构处理`

## 📋 核心要点

1. 现有方法在处理工具调用时，LLMs面临参数生成不准确和执行不当的问题，限制了其有效性。
2. TUMS框架通过意图识别、任务分解和多结构处理，提升了LLMs的工具使用能力，解决了参数生成的粗糙性。
3. 实验结果显示，TUMS在ToolQA基准上分别提高了19.6%和50.6%的性能，验证了其有效性和效率。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在解决多种自然语言处理任务中发挥了越来越重要的作用，尤其是在自然语言理解和生成方面。通过与外部工具的集成，LLMs的有效性得到了进一步增强，能够提供更精确、及时和专业的响应。然而，LLMs在执行不可执行的操作和不当操作时仍面临困难，这主要归因于参数设置不当。本文提出了TUMS，一个新颖的框架，通过将工具级处理转变为参数级处理，来增强LLMs的工具使用能力。该框架包括四个关键组件：意图识别器、任务分解器、多结构处理器和执行器。实证研究表明，TUMS框架在ToolQA的简单和困难基准上分别提高了19.6%和50.6%的性能，且通过消融实验展示了各部分的关键贡献，为未来的工具增强LLMs研究提供了更多见解。

## 🔬 方法详解

**问题定义**：本文旨在解决LLMs在工具调用中遇到的参数生成不准确和执行不当的问题，现有方法主要依赖粗粒度的工具级处理，未能考虑不同工具的复杂性。

**核心思路**：TUMS框架的核心思想是将工具级处理转变为参数级处理，通过识别用户意图和分解任务来生成更准确的参数，从而提升LLMs的工具使用能力。

**技术框架**：TUMS框架由四个主要模块组成：意图识别器（识别用户意图）、任务分解器（将复杂任务分解为简单子任务）、多结构处理器（生成准确参数）和执行器（执行工具调用）。

**关键创新**：TUMS的创新在于其多结构处理器，能够根据不同工具的复杂性生成精确参数，这一设计与现有方法的粗粒度处理方式形成鲜明对比。

**关键设计**：在设计中，意图识别器采用了先进的自然语言处理技术，任务分解器使用了层次化的分解策略，多结构处理器则结合了多种参数生成策略，以确保生成的参数适应不同工具的需求。

## 📊 实验亮点

实验结果显示，TUMS框架在ToolQA基准上分别实现了19.6%和50.6%的性能提升，显著优于现有方法。这一成果不仅验证了框架的有效性，还为未来的研究提供了重要的实验依据。

## 🎯 应用场景

TUMS框架的潜在应用领域包括智能助手、自动化工具调用和复杂任务的自动化处理等。通过提升LLMs的工具使用能力，该研究能够在实际应用中提供更高效的解决方案，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Recently, large language models(LLMs) have played an increasingly important role in solving a wide range of NLP tasks, leveraging their capabilities of natural language understanding and generating. Integration with external tools further enhances LLMs' effectiveness, providing more precise, timely, and specialized responses. However, LLMs still encounter difficulties with non-executable actions and improper actions, which are primarily attributed to incorrect parameters. The process of generating parameters by LLMs is confined to the tool level, employing the coarse-grained strategy without considering the different difficulties of various tools. To address this issue, we propose TUMS, a novel framework designed to enhance the tool-use capabilities of LLMs by transforming tool-level processing into parameter-level processing. Specifically, our framework consists of four key components: (1) an intent recognizer that identifies the user's intent to help LLMs better understand the task; (2) a task decomposer that breaks down complex tasks into simpler subtasks, each involving a tool call; (3) a subtask processor equipped with multi-structure handlers to generate accurate parameters; and (4) an executor. Our empirical studies have evidenced the effectiveness and efficiency of the TUMS framework with an average of 19.6\% and 50.6\% improvement separately on easy and hard benchmarks of ToolQA, meanwhile, we demonstrated the key contribution of each part with ablation experiments, offering more insights and stimulating future research on Tool-augmented LLMs.

