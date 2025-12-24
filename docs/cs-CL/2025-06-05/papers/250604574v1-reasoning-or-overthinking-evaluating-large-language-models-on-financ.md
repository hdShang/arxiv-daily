---
layout: default
title: "Reasoning or Overthinking: Evaluating Large Language Models on Financial Sentiment Analysis"
---

# Reasoning or Overthinking: Evaluating Large Language Models on Financial Sentiment Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04574" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04574v1</a>
  <a href="https://arxiv.org/pdf/2506.04574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04574v1', 'Reasoning or Overthinking: Evaluating Large Language Models on Financial Sentiment Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dimitris Vamvourellis, Dhagash Mehta

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**评估大型语言模型在金融情感分析中的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融情感分析` `大型语言模型` `推理能力` `系统1思维` `系统2思维` `模型评估` `数据集` `机器学习`

## 📋 核心要点

1. 现有的金融情感分析方法在处理复杂语言和人类情感一致性方面存在不足，尤其是在高风险决策中。
2. 论文提出通过比较不同大型语言模型和提示策略，探索推理对金融情感分析的影响，重点在于快速直观的思维方式。
3. 实验结果显示，GPT-4o在没有推理提示的情况下表现最佳，表明推理可能导致过度思考，从而影响预测准确性。

## 📝 摘要（中文）

本研究探讨了大型语言模型（LLMs）在零-shot金融情感分析中的有效性，包括基于推理和非推理模型。通过使用由领域专家标注的Financial PhraseBank数据集，我们评估了不同LLMs和提示策略与人类标注情感的一致性。研究发现，推理并未提升模型性能，最准确的组合是GPT-4o，无需Chain-of-Thought提示。结果表明，快速直观的“系统1”思维更符合人类判断，挑战了推理总能提高决策质量的假设，尤其是在高风险金融应用中。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在金融情感分析中的有效性问题，尤其是推理能力对模型性能的影响。现有方法在复杂语言处理和人类情感一致性方面存在挑战。

**核心思路**：论文的核心思路是通过比较不同的LLMs和提示策略，评估推理在金融情感分析中的作用，特别是快速直观的“系统1”思维是否优于慢速的“系统2”推理。

**技术框架**：研究采用Financial PhraseBank数据集，比较三种大型语言模型（GPT-4o、GPT-4.1、o3-mini）与两种小型模型（FinBERT-Prosus、FinBERT-Tone），在不同提示策略下进行评估。

**关键创新**：最重要的技术创新在于发现推理并未提升模型性能，反而在某些情况下导致过度思考，影响预测准确性。这一发现挑战了推理总能提高决策质量的传统观念。

**关键设计**：在实验中，采用了不同的提示策略来模拟“系统1”和“系统2”思维，评估模型在复杂语言和标注一致性方面的表现。

## 📊 实验亮点

实验结果显示，GPT-4o在没有Chain-of-Thought提示的情况下，表现出最优的准确性和与人类标注的一致性，超越了其他模型。此结果表明，推理并不总是提升模型性能，尤其是在金融情感分析中，快速直观的思维方式更为有效。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场分析、投资决策支持和风险评估等。通过优化情感分析模型，能够提高金融决策的准确性和效率，尤其在高风险环境中具有重要价值。未来，该研究可能推动金融科技领域的进一步发展，促进智能决策系统的应用。

## 📄 摘要（原文）

> We investigate the effectiveness of large language models (LLMs), including reasoning-based and non-reasoning models, in performing zero-shot financial sentiment analysis. Using the Financial PhraseBank dataset annotated by domain experts, we evaluate how various LLMs and prompting strategies align with human-labeled sentiment in a financial context. We compare three proprietary LLMs (GPT-4o, GPT-4.1, o3-mini) under different prompting paradigms that simulate System 1 (fast and intuitive) or System 2 (slow and deliberate) thinking and benchmark them against two smaller models (FinBERT-Prosus, FinBERT-Tone) fine-tuned on financial sentiment analysis. Our findings suggest that reasoning, either through prompting or inherent model design, does not improve performance on this task. Surprisingly, the most accurate and human-aligned combination of model and method was GPT-4o without any Chain-of-Thought (CoT) prompting. We further explore how performance is impacted by linguistic complexity and annotation agreement levels, uncovering that reasoning may introduce overthinking, leading to suboptimal predictions. This suggests that for financial sentiment classification, fast, intuitive "System 1"-like thinking aligns more closely with human judgment compared to "System 2"-style slower, deliberative reasoning simulated by reasoning models or CoT prompting. Our results challenge the default assumption that more reasoning always leads to better LLM decisions, particularly in high-stakes financial applications.

