---
layout: default
title: "EICAP: Deep Dive in Assessment and Enhancement of Large Language Models in Emotional Intelligence through Multi-Turn Conversations"
---

# EICAP: Deep Dive in Assessment and Enhancement of Large Language Models in Emotional Intelligence through Multi-Turn Conversations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06196" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06196v1</a>
  <a href="https://arxiv.org/pdf/2508.06196.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06196v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06196v1', 'EICAP: Deep Dive in Assessment and Enhancement of Large Language Models in Emotional Intelligence through Multi-Turn Conversations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nizi Nazar, Ehsaneddin Asgari

**分类**: cs.CL, cs.HC

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出EICAP以提升大语言模型的情感智能能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感智能` `大语言模型` `多轮对话` `评估基准` `微调技术` `心理学分类法` `人机交互`

## 📋 核心要点

1. 现有的大语言模型在情感智能方面的能力不足，缺乏深层情感推理。
2. 本文提出了一种四层情感智能分类法，并设计了EICAP-Bench基准来评估LLMs的情感智能能力。
3. 实验结果表明，Qwen2.5-Instruct在评估中表现最佳，且通过微调仅在评估层上取得显著提升。

## 📝 摘要（中文）

情感智能（EI）是人类对齐大语言模型（LLMs）发展的一个关键但未被充分探索的维度。为了解决这一问题，本文提出了一种统一的、基于心理学的四层EI分类法，涵盖情感追踪、因果推断、评估和情感适当的响应生成。基于此框架，我们推出了EICAP-Bench，一个新颖的多轮选择题基准，旨在评估开源LLMs在多样语言和文化背景下的EI能力。我们对六种LLMs进行了评估，发现Qwen2.5-Instruct是最强基线。通过在UltraChat数据集上对Qwen2.5-Base和Qwen2.5-Instruct进行LoRA适配器微调，我们的统计分析显示，只有评估层在微调中显著改善。这些发现突显了现有预训练和指令微调范式在赋予LLMs更深层情感推理方面的局限性，并强调了针对性数据和建模策略的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决当前大语言模型在情感智能方面的不足，尤其是在深层情感推理能力上的缺失。现有方法未能有效评估和提升LLMs的情感智能能力。

**核心思路**：论文提出了一种基于心理学的四层情感智能分类法，涵盖情感追踪、因果推断、评估和情感适当的响应生成，以此为基础设计EICAP-Bench基准，评估LLMs的情感智能能力。

**技术框架**：整体架构包括情感智能的四个层次，分别是情感追踪、因果推断、评估和响应生成。EICAP-Bench作为评估工具，采用多轮选择题形式，涵盖多种语言和文化背景。

**关键创新**：最重要的创新在于提出了统一的情感智能分类法，并通过EICAP-Bench提供了一种新的评估框架，填补了现有LLMs在情感智能评估方面的空白。

**关键设计**：在微调过程中，使用LoRA适配器对Qwen2.5-Base和Qwen2.5-Instruct进行优化，特别是在UltraChat数据集上进行训练，关注评估层的提升。

## 📊 实验亮点

实验结果显示，Qwen2.5-Instruct在EICAP-Bench基准中表现最佳，成为最强基线。通过在UltraChat数据集上的微调，评估层的性能显著提升，强调了针对性微调的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、情感分析和智能客服等。通过提升大语言模型的情感智能能力，可以改善用户体验，增强模型在复杂对话场景中的表现，未来可能在教育、心理咨询等领域产生深远影响。

## 📄 摘要（原文）

> Emotional Intelligence (EI) is a critical yet underexplored dimension in the development of human-aligned LLMs. To address this gap, we introduce a unified, psychologically grounded four-layer taxonomy of EI tailored for large language models (LLMs), encompassing emotional tracking, cause inference, appraisal, and emotionally appropriate response generation. Building on this framework, we present EICAP-Bench, a novel MCQ style multi-turn benchmark designed to evaluate EI capabilities in open-source LLMs across diverse linguistic and cultural contexts. We evaluate six LLMs: LLaMA3 (8B), LLaMA3-Instruct, Gemma (9B), Gemma-Instruct, Qwen2.5 (7B), and Qwen2.5-Instruct on EmoCap-Bench, identifying Qwen2.5-Instruct as the strongest baseline. To assess the potential for enhancing EI capabilities, we fine-tune both Qwen2.5-Base and Qwen2.5-Instruct using LoRA adapters on UltraChat (UC), a large-scale, instruction-tuned dialogue dataset, in both English and Arabic. Our statistical analysis reveals that among the five EI layers, only the Appraisal layer shows significant improvement through UC-based fine-tuning. These findings highlight the limitations of existing pretraining and instruction-tuning paradigms in equipping LLMs with deeper emotional reasoning and underscore the need for targeted data and modeling strategies for comprehensive EI alignment.

