---
layout: default
title: "MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework"
---

# MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00934" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00934v2</a>
  <a href="https://arxiv.org/pdf/2509.00934.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00934v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00934v2', 'MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Shahidul Salim, Lian Fu, Arav Adikesh Ramakrishnan, Zonghai Yao, Hong Yu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-31 (更新: 2025-09-19)

**备注**: To appear in Findings of the Association for Computational Linguistics: EMNLP 2025

---

## 💡 一句话要点

**提出MedCOD框架以提升医学英语到西班牙语翻译质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学翻译` `大型语言模型` `结构化知识` `UMLS` `LoRA微调` `跨语言服务` `机器翻译`

## 📋 核心要点

1. 现有医学翻译模型在处理领域特定术语和上下文时存在不足，导致翻译质量不高。
2. MedCOD框架通过整合UMLS和LLM-KB的结构化知识，优化了提示和微调过程，从而提升翻译效果。
3. 实验结果显示，使用MedCOD的Phi-4模型在BLEU、chrF++和COMET指标上均超越了强基线模型，表现出显著提升。

## 📝 摘要（中文）

我们提出了MedCOD（医学链词典），这是一个混合框架，旨在通过将领域特定的结构化知识整合到大型语言模型（LLMs）中，改善医学英语到西班牙语的翻译。MedCOD结合了来自统一医学语言系统（UMLS）和LLM作为知识库（LLM-KB）范式的领域知识，以增强结构化提示和微调。我们构建了一个包含2999篇英语-西班牙语MedlinePlus文章的平行语料库和一个带有结构化医学上下文的100句测试集。通过使用包含多语言变体、医学同义词和UMLS派生定义的结构化提示，结合基于LoRA的微调，评估了四个开源LLM（Phi-4、Qwen2.5-14B、Qwen2.5-7B和LLaMA-3.1-8B）。实验结果表明，MedCOD显著提高了所有模型的翻译质量。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有医学翻译模型在处理医学领域特定术语和上下文时的不足，导致翻译质量不高的问题。现有方法往往缺乏对结构化知识的有效利用，影响了翻译的准确性和流畅性。

**核心思路**：论文提出的MedCOD框架通过将领域特定的结构化知识整合到大型语言模型中，优化了翻译过程。通过使用结构化提示和微调，MedCOD能够更好地捕捉医学术语的语义关系，从而提高翻译质量。

**技术框架**：MedCOD的整体架构包括数据收集、结构化知识整合、模型训练和评估四个主要模块。首先，构建平行语料库并注释结构化医学上下文；其次，整合UMLS和LLM-KB知识以增强提示；最后，使用LoRA进行微调并评估模型性能。

**关键创新**：MedCOD的主要创新在于将结构化知识与大型语言模型结合，形成了一种新的翻译框架。这种方法与传统的单一模型训练方式本质上不同，能够更有效地处理医学领域的复杂性。

**关键设计**：在模型训练中，采用了基于LoRA的微调策略，结合多语言变体和医学同义词的结构化提示。关键参数设置包括BLEU、chrF++和COMET等指标的优化，以确保翻译质量的提升。通过这些设计，MedCOD实现了显著的性能改进。

## 📊 实验亮点

实验结果显示，使用MedCOD的Phi-4模型在BLEU、chrF++和COMET指标上分别达到了44.23、28.91和0.863，显著超越了基线模型如GPT-4o和GPT-4o-mini。消融研究表明，MedCOD提示和模型适应独立贡献于性能提升，两者结合则实现了最高的改进。

## 🎯 应用场景

该研究的潜在应用领域包括医学翻译、医疗信息系统和跨语言医疗服务。通过提升医学翻译的准确性和流畅性，MedCOD能够帮助医疗专业人员更好地沟通，促进不同语言背景患者的医疗服务。未来，该框架还可扩展至其他语言对的医学翻译任务，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> We present MedCOD (Medical Chain-of-Dictionary), a hybrid framework designed to improve English-to-Spanish medical translation by integrating domain-specific structured knowledge into large language models (LLMs). MedCOD integrates domain-specific knowledge from both the Unified Medical Language System (UMLS) and the LLM-as-Knowledge-Base (LLM-KB) paradigm to enhance structured prompting and fine-tuning. We constructed a parallel corpus of 2,999 English-Spanish MedlinePlus articles and a 100-sentence test set annotated with structured medical contexts. Four open-source LLMs (Phi-4, Qwen2.5-14B, Qwen2.5-7B, and LLaMA-3.1-8B) were evaluated using structured prompts that incorporated multilingual variants, medical synonyms, and UMLS-derived definitions, combined with LoRA-based fine-tuning. Experimental results demonstrate that MedCOD significantly improves translation quality across all models. For example, Phi-4 with MedCOD and fine-tuning achieved BLEU 44.23, chrF++ 28.91, and COMET 0.863, surpassing strong baseline models like GPT-4o and GPT-4o-mini. Ablation studies confirm that both MedCOD prompting and model adaptation independently contribute to performance gains, with their combination yielding the highest improvements. These findings highlight the potential of structured knowledge integration to enhance LLMs for medical translation tasks.

