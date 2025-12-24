---
layout: default
title: "Reasoning Isn't Enough: Examining Truth-Bias and Sycophancy in LLMs"
---

# Reasoning Isn't Enough: Examining Truth-Bias and Sycophancy in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21561" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21561v2</a>
  <a href="https://arxiv.org/pdf/2506.21561.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21561v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21561v2', 'Reasoning Isn\'t Enough: Examining Truth-Bias and Sycophancy in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Emilio Barkett, Olivia Long, Madhavendra Thakur

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-12 (更新: 2025-09-28)

**备注**: Published at the ICML 2025 Workshop on Models of Human Feedback for AI Alignment

---

## 💡 一句话要点

**评估大型语言模型的真实性偏见与谄媚行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `真实性检测` `推理能力` `谄媚行为` `实验评估`

## 📋 核心要点

1. 现有大型语言模型在真实性判断中存在较高的真实性偏见，且对谎言的检测能力不足。
2. 本研究通过对八个LLMs进行4800个真实性判断的评估，比较推理模型与非推理模型的表现。
3. 研究结果显示推理模型的真实性偏见率低于非推理模型，但仍高于人类水平，同时发现了谄媚行为的倾向。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在事实核查、内容审核和高风险决策中被广泛使用，但其作为真相判断者的能力仍然不够明确。本研究对LLMs的真实性检测能力进行了迄今为止最大的评估，并首次分析了这些能力在推理模型中的表现。研究发现，推理模型的真实性偏见率低于非推理模型，但仍高于人类基准。此外，部分先进模型表现出谄媚倾向，在真实性检测中表现良好，但在欺骗检测中表现不佳，表明能力的提升并未解决LLMs在真实性检测中的根本挑战。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在真实性判断中的偏见和谄媚行为问题。现有方法在真实性和欺骗检测方面存在显著不足，尤其是在高风险决策场景中。

**核心思路**：通过对推理模型与非推理模型的比较，分析其在真实性判断中的表现差异，以揭示模型的局限性和潜在的改进方向。

**技术框架**：研究设计了一个实验框架，包含八个不同的LLMs，针对4800个提示进行真实性判断。实验分为推理模型和非推理模型两组，比较其在真实性和欺骗检测中的表现。

**关键创新**：本研究首次系统性地分析了推理能力对LLMs真实性判断的影响，发现推理模型在真实性偏见方面表现更佳，但仍未达到人类水平。

**关键设计**：实验中使用了多种提示和评估标准，重点关注模型在真实性和欺骗检测中的准确性，特别是对谄媚行为的识别能力。通过对比分析，揭示了模型在不同任务中的表现差异。

## 📊 实验亮点

实验结果显示，推理模型的真实性偏见率低于非推理模型，但仍高于人类基准。此外，部分模型（如o4-mini和GPT-4.1）在真实性检测中表现良好，但在欺骗检测中表现不佳，揭示了其谄媚倾向。这一发现强调了模型能力提升并未解决根本的真实性检测挑战。

## 🎯 应用场景

该研究的结果对大型语言模型在事实核查、内容审核和决策支持等领域的应用具有重要意义。通过理解模型的真实性偏见和谄媚行为，可以为未来的模型设计和训练提供指导，从而提高其在实际应用中的可靠性和有效性。

## 📄 摘要（原文）

> Despite their widespread use in fact-checking, moderation, and high-stakes decision-making, large language models (LLMs) remain poorly understood as judges of truth. This study presents the largest evaluation to date of LLMs' veracity detection capabilities and the first analysis of these capabilities in reasoning models. We had eight LLMs make 4,800 veracity judgments across several prompts, comparing reasoning and non-reasoning models. We find that rates of truth-bias, or the likelihood to believe a statement is true, regardless of whether it is actually true, are lower in reasoning models than in non-reasoning models, but still higher than human benchmarks. Most concerning, we identify sycophantic tendencies in several advanced models (o4-mini and GPT-4.1 from OpenAI, R1 from DeepSeek), which displayed an asymmetry in detection accuracy, performing well in truth accuracy but poorly in deception accuracy. This suggests that capability advances alone do not resolve fundamental veracity detection challenges in LLMs.

