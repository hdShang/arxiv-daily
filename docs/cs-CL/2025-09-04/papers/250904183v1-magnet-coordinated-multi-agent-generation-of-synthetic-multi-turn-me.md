---
layout: default
title: "MAGneT: Coordinated Multi-Agent Generation of Synthetic Multi-Turn Mental Health Counseling Sessions"
---

# MAGneT: Coordinated Multi-Agent Generation of Synthetic Multi-Turn Mental Health Counseling Sessions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04183" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04183v1</a>
  <a href="https://arxiv.org/pdf/2509.04183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04183v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04183v1', 'MAGneT: Coordinated Multi-Agent Generation of Synthetic Multi-Turn Mental Health Counseling Sessions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aishik Mandal, Tanmoy Chakraborty, Iryna Gurevych

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04

**备注**: 25 pages, 29 figures

---

## 💡 一句话要点

**MAGneT：协同多智能体生成合成多轮心理健康咨询对话，解决高质量数据稀缺问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `心理咨询` `对话生成` `大型语言模型` `数据增强`

## 📋 核心要点

1. 高质量、符合隐私要求的心理咨询数据稀缺，限制了开源大语言模型（LLM）在该领域的应用。
2. MAGneT通过多智能体框架，将咨询师回应生成分解为多个子任务，由专门的LLM智能体模拟心理学技巧协同完成。
3. 实验表明，MAGneT生成的对话在质量、多样性和治疗一致性方面优于现有方法，且微调后的模型性能显著提升。

## 📝 摘要（中文）

针对可扩展心理咨询日益增长的需求，本文提出了MAGneT，一种新颖的多智能体框架，用于生成合成心理咨询对话。该框架将咨询师的回应生成分解为由专门的LLM智能体处理的协同子任务，每个智能体模拟一种关键的心理学技巧。与以往的单智能体方法不同，MAGneT更好地捕捉了真实咨询的结构和细微差别。此外，本文提出了一个统一的评估框架，整合了多种自动和专家指标，解决了先前评估协议中的不一致性。专家评估从先前工作的四个咨询方面扩展到九个方面，从而能够更彻底、更稳健地评估数据质量。实验结果表明，MAGneT在生成咨询对话的质量、多样性和治疗一致性方面显著优于现有方法，在认知疗法评定量表（CTRS）上，一般咨询技巧平均提高3.2%，CBT特定技巧平均提高4.3%。关键的是，专家在所有方面平均77.2%的情况下更喜欢MAGneT生成的对话。此外，在MAGneT生成的对话上微调开源模型显示出更好的性能，在CTRS上，一般咨询技巧平均提高6.3%，CBT特定技巧平均提高7.3%，优于使用基线方法生成的对话进行微调的模型。代码和数据已公开。

## 🔬 方法详解

**问题定义**：现有心理咨询领域缺乏高质量、符合隐私要求的训练数据，限制了大型语言模型在该领域的应用。以往的单智能体方法难以捕捉真实咨询的复杂结构和细微差别，且评估标准不统一，难以全面评估数据质量。

**核心思路**：MAGneT的核心思路是将咨询师的回应生成过程分解为多个子任务，每个子任务由一个专门的LLM智能体负责，这些智能体模拟不同的心理学技巧，通过协同工作生成高质量的咨询对话。这种多智能体协同的方式能够更好地捕捉真实咨询的复杂性和多样性。

**技术框架**：MAGneT框架包含多个智能体，每个智能体负责一个特定的心理学技巧，例如共情、提问、认知重构等。这些智能体通过一个协调机制进行通信和协作，共同生成咨询师的回应。框架还包含一个统一的评估模块，整合了多种自动和专家指标，用于全面评估生成对话的质量。

**关键创新**：MAGneT的关键创新在于其多智能体协同生成机制，以及更全面的评估框架。与以往的单智能体方法相比，MAGneT能够更好地模拟真实咨询的复杂性，生成更高质量的对话。同时，统一的评估框架能够更准确地评估生成对话的各个方面。

**关键设计**：MAGneT框架中，每个智能体都使用一个预训练的LLM进行微调，以掌握特定的心理学技巧。协调机制采用了一种基于规则的方法，根据当前对话状态选择合适的智能体进行回应生成。评估框架包含多种自动指标，例如BLEU、ROUGE等，以及专家评估指标，例如咨询技巧、治疗一致性等。

## 📊 实验亮点

实验结果表明，MAGneT在生成咨询对话的质量、多样性和治疗一致性方面显著优于现有方法。在认知疗法评定量表（CTRS）上，一般咨询技巧平均提高3.2%，CBT特定技巧平均提高4.3%。专家在所有方面平均77.2%的情况下更喜欢MAGneT生成的对话。使用MAGneT生成的数据微调开源模型，在CTRS上，一般咨询技巧平均提高6.3%，CBT特定技巧平均提高7.3%，优于使用基线方法生成的数据进行微调的模型。

## 🎯 应用场景

MAGneT可用于生成大规模的合成心理咨询对话数据，用于训练和微调LLM，从而提升LLM在心理健康领域的应用能力。该技术可应用于在线心理咨询平台、心理健康教育、以及心理咨询师的培训等领域，具有重要的社会价值和应用前景。

## 📄 摘要（原文）

> The growing demand for scalable psychological counseling highlights the need for fine-tuning open-source Large Language Models (LLMs) with high-quality, privacy-compliant data, yet such data remains scarce. Here we introduce MAGneT, a novel multi-agent framework for synthetic psychological counseling session generation that decomposes counselor response generation into coordinated sub-tasks handled by specialized LLM agents, each modeling a key psychological technique. Unlike prior single-agent approaches, MAGneT better captures the structure and nuance of real counseling. In addition, we address inconsistencies in prior evaluation protocols by proposing a unified evaluation framework integrating diverse automatic and expert metrics. Furthermore, we expand the expert evaluations from four aspects of counseling in previous works to nine aspects, enabling a more thorough and robust assessment of data quality. Empirical results show that MAGneT significantly outperforms existing methods in quality, diversity, and therapeutic alignment of the generated counseling sessions, improving general counseling skills by 3.2% and CBT-specific skills by 4.3% on average on cognitive therapy rating scale (CTRS). Crucially, experts prefer MAGneT-generated sessions in 77.2% of cases on average across all aspects. Moreover, fine-tuning an open-source model on MAGneT-generated sessions shows better performance, with improvements of 6.3% on general counseling skills and 7.3% on CBT-specific skills on average on CTRS over those fine-tuned with sessions generated by baseline methods. We also make our code and data public.

