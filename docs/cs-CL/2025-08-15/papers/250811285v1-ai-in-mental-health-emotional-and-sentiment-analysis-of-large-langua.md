---
layout: default
title: "AI in Mental Health: Emotional and Sentiment Analysis of Large Language Models' Responses to Depression, Anxiety, and Stress Queries"
---

# AI in Mental Health: Emotional and Sentiment Analysis of Large Language Models' Responses to Depression, Anxiety, and Stress Queries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11285" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11285v1</a>
  <a href="https://arxiv.org/pdf/2508.11285.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11285v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11285v1', 'AI in Mental Health: Emotional and Sentiment Analysis of Large Language Models\' Responses to Depression, Anxiety, and Stress Queries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arya VarastehNezhad, Reza Tavasoli, Soroush Elyasi, MohammadHossein LotfiNia, Hamed Farbeh

**分类**: cs.CL

**发布日期**: 2025-08-15

---

## 💡 一句话要点

**研究大型语言模型在心理健康领域的情感分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `情感分析` `心理健康` `抑郁` `焦虑` `情绪识别` `用户体验`

## 📋 核心要点

1. 现有的心理健康支持工具在情感表达和用户体验上存在不足，尤其是对不同心理状态的响应差异较大。
2. 本研究通过分析八种大型语言模型对心理健康问题的回答，探讨了模型选择对情感表达的影响。
3. 实验结果表明，模型的选择显著影响情感表达模式，尤其在焦虑、抑郁和压力相关问题上表现出不同的情感特征。

## 📝 摘要（中文）

抑郁、焦虑和压力是普遍的心理健康问题，越来越多的人通过大型语言模型（LLMs）寻求信息。本研究调查了八种LLMs（Claude Sonnet、Copilot、Gemini Pro、GPT-4o、GPT-4o mini、Llama、Mixtral和Perplexity）对关于抑郁、焦虑和压力的二十个实际问题的回答。分析结果显示，乐观、恐惧和悲伤主导了所有输出的情感特征，而中性情感保持高值。不同模型在情感表达上存在显著差异，选择合适的LLM对心理健康应用至关重要。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在心理健康领域对抑郁、焦虑和压力问题的情感响应差异，现有方法未能充分考虑模型选择对情感表达的影响。

**核心思路**：通过对八种不同LLMs的回答进行情感和情绪分析，探讨模型选择如何影响用户体验和情感响应。

**技术框架**：研究流程包括问题设计、模型选择、数据收集和情感分析，主要模块包括用户画像、情感评分和统计分析。

**关键创新**：本研究首次系统性地比较了多种LLMs在心理健康问题上的情感表达，揭示了模型选择对情感响应的显著影响。

**关键设计**：使用先进的情感分析工具对2880个回答进行评分，关注情感的种类和强度，特别是乐观、恐惧和悲伤等情感的表现。

## 📊 实验亮点

实验结果显示，焦虑相关问题的恐惧评分高达0.974，抑郁问题的悲伤评分为0.686，且Mixtral模型表现出最高的负面情感，而Llama则展现出最乐观的反应。这些发现强调了模型选择在心理健康应用中的重要性。

## 🎯 应用场景

该研究的结果可广泛应用于心理健康支持系统的开发，帮助设计更具针对性的对话系统，以提高用户的情感支持体验。未来，基于模型选择的个性化心理健康干预将成为可能，推动心理健康领域的技术进步。

## 📄 摘要（原文）

> Depression, anxiety, and stress are widespread mental health concerns that increasingly drive individuals to seek information from Large Language Models (LLMs). This study investigates how eight LLMs (Claude Sonnet, Copilot, Gemini Pro, GPT-4o, GPT-4o mini, Llama, Mixtral, and Perplexity) reply to twenty pragmatic questions about depression, anxiety, and stress when those questions are framed for six user profiles (baseline, woman, man, young, old, and university student). The models generated 2,880 answers, which we scored for sentiment and emotions using state-of-the-art tools. Our analysis revealed that optimism, fear, and sadness dominated the emotional landscape across all outputs, with neutral sentiment maintaining consistently high values. Gratitude, joy, and trust appeared at moderate levels, while emotions such as anger, disgust, and love were rarely expressed. The choice of LLM significantly influenced emotional expression patterns. Mixtral exhibited the highest levels of negative emotions including disapproval, annoyance, and sadness, while Llama demonstrated the most optimistic and joyful responses. The type of mental health condition dramatically shaped emotional responses: anxiety prompts elicited extraordinarily high fear scores (0.974), depression prompts generated elevated sadness (0.686) and the highest negative sentiment, while stress-related queries produced the most optimistic responses (0.755) with elevated joy and trust. In contrast, demographic framing of queries produced only marginal variations in emotional tone. Statistical analyses confirmed significant model-specific and condition-specific differences, while demographic influences remained minimal. These findings highlight the critical importance of model selection in mental health applications, as each LLM exhibits a distinct emotional signature that could significantly impact user experience and outcomes.

