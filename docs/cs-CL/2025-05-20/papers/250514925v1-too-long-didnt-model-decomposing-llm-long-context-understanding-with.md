---
layout: default
title: Too Long, Didn't Model: Decomposing LLM Long-Context Understanding With Novels
---

# Too Long, Didn't Model: Decomposing LLM Long-Context Understanding With Novels

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14925" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14925v1</a>
  <a href="https://arxiv.org/pdf/2505.14925.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14925v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14925v1', 'Too Long, Didn\'t Model: Decomposing LLM Long-Context Understanding With Novels')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sil Hamilton, Rebecca M. M. Hicke, Matthew Wilkens, David Mimno

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出TLDM基准以评估LLM在长上下文理解中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文理解` `大型语言模型` `小说分析` `评估基准` `叙事结构`

## 📋 核心要点

1. 现有大型语言模型在长上下文理解方面存在显著不足，尤其是在复杂的叙事结构中。
2. 本文提出TLDM基准，专注于评估模型在小说情节摘要和叙事时间理解的能力。
3. 实验结果显示，测试的七个LLM在64k标记以上无法稳定理解，提示需要新的评估标准。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）的上下文长度已增加到数百万个标记，但在复杂长上下文场景中评估其有效性仍然困难。本文认为小说是一个研究复杂结构和长距离语义依赖的案例，提出了Too Long, Didn't Model（TLDM）基准，测试模型在情节摘要、故事世界配置和叙事时间等方面的能力。研究发现，七个前沿LLM在64k个标记以上无法保持稳定理解，提示语言模型开发者在评估模型性能时需超越传统基准。为进一步发展，本文发布了TLDM基准及参考代码和数据。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长上下文理解中的有效性评估问题，现有方法往往无法处理复杂的叙事结构和长距离依赖，导致评估结果不准确。

**核心思路**：提出TLDM基准，通过小说这一复杂文本类型来测试模型的理解能力，关注情节摘要、故事世界配置和叙事时间等方面，以此评估模型在长上下文中的表现。

**技术框架**：TLDM基准包含多个模块，首先是数据集构建，选择具有复杂结构的小说文本；其次是评估指标设计，针对情节和叙事时间进行量化评估；最后是模型测试，使用七个前沿LLM进行性能对比。

**关键创新**：TLDM基准的创新在于其针对长上下文的复杂性进行专门设计，超越了传统的“迷失在中间”基准，提供了更具挑战性的评估标准。

**关键设计**：在设计中，选择了多部小说作为测试数据，设置了具体的评估指标，如情节连贯性和时间推理能力，确保评估的全面性和准确性。实验中使用的模型包括最新的LLM，确保结果的前沿性。

## 📊 实验亮点

实验结果表明，七个前沿LLM在64k标记以上无法保持稳定理解，显示出在复杂长上下文场景中的显著性能下降。这一发现强调了现有评估方法的局限性，并为未来的模型开发提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、文本生成和智能助手等。通过改进对长上下文的理解，LLM可以在更复杂的场景中提供更准确的响应，提升用户体验。未来，该基准可能推动更高效的模型设计和评估方法的发展。

## 📄 摘要（原文）

> Although the context length of large language models (LLMs) has increased to millions of tokens, evaluating their effectiveness beyond needle-in-a-haystack approaches has proven difficult. We argue that novels provide a case study of subtle, complicated structure and long-range semantic dependencies often over 128k tokens in length. Inspired by work on computational novel analysis, we release the Too Long, Didn't Model (TLDM) benchmark, which tests a model's ability to report plot summary, storyworld configuration, and elapsed narrative time. We find that none of seven tested frontier LLMs retain stable understanding beyond 64k tokens. Our results suggest language model developers must look beyond "lost in the middle" benchmarks when evaluating model performance in complex long-context scenarios. To aid in further development we release the TLDM benchmark together with reference code and data.

