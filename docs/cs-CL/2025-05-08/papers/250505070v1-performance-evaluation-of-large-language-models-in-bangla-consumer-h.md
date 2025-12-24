---
layout: default
title: Performance Evaluation of Large Language Models in Bangla Consumer Health Query Summarization
---

# Performance Evaluation of Large Language Models in Bangla Consumer Health Query Summarization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05070" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05070v1</a>
  <a href="https://arxiv.org/pdf/2505.05070.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05070v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05070v1', 'Performance Evaluation of Large Language Models in Bangla Consumer Health Query Summarization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ajwad Abrar, Farzana Tabassum, Sabbir Ahmed

**分类**: cs.CL

**发布日期**: 2025-05-08

**DOI**: [10.1109/ICCIT64611.2024.11022034](https://doi.org/10.1109/ICCIT64611.2024.11022034)

---

## 💡 一句话要点

**评估大型语言模型在孟加拉消费者健康查询摘要中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `消费者健康查询` `摘要生成` `低资源语言` `ROUGE指标` `零-shot学习` `医疗信息处理`

## 📋 核心要点

1. 孟加拉语的消费者健康查询常常包含冗余信息，导致医疗响应效率低下。
2. 本研究评估了九种大型语言模型在零-shot条件下对孟加拉CHQs的摘要能力，探索其潜力。
3. 实验结果表明，零-shot LLMs在摘要质量上可与经过微调的模型相媲美，特别是在ROUGE指标上表现优异。

## 📝 摘要（中文）

孟加拉语的消费者健康查询（CHQs）常包含冗余信息，影响医疗响应的效率。本研究探讨了九种先进大型语言模型（LLMs）在总结孟加拉CHQs时的零-shot表现，使用包含2350对注释查询-摘要对的BanglaCHQ-Summ数据集进行基准测试。结果显示，Mixtral-8x22b-Instruct在ROUGE-1和ROUGE-L指标上表现最佳，而Bangla T5在ROUGE-2上表现突出。这项工作强调了LLMs在低资源语言中应对挑战的潜力，为医疗查询摘要提供了可扩展的解决方案。

## 🔬 方法详解

**问题定义**：本研究旨在解决孟加拉消费者健康查询中冗余信息导致的摘要效率低下问题。现有方法在处理低资源语言时面临挑战，尤其是在缺乏任务特定训练的情况下。

**核心思路**：本研究通过评估九种大型语言模型在零-shot条件下的表现，探索其在生成高质量摘要方面的潜力，旨在证明这些模型能够在没有专门训练的情况下提供有效的解决方案。

**技术框架**：研究使用BanglaCHQ-Summ数据集进行基准测试，包含2350对注释的查询和摘要。通过ROUGE指标评估模型性能，比较不同模型的摘要质量。

**关键创新**：本研究的主要创新在于展示了零-shot LLMs在低资源语言摘要生成中的有效性，尤其是Mixtral-8x22b-Instruct模型在ROUGE-1和ROUGE-L指标上的优异表现。

**关键设计**：在实验中，采用了ROUGE-1、ROUGE-2和ROUGE-L作为性能评估指标，确保了对模型摘要质量的全面评估。

## 📊 实验亮点

实验结果显示，Mixtral-8x22b-Instruct在ROUGE-1和ROUGE-L指标上表现最佳，分别取得了显著的性能提升。同时，Bangla T5在ROUGE-2上也展现了强劲的能力，表明零-shot LLMs在低资源语言处理中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康信息系统、在线健康咨询平台以及任何需要处理低资源语言的自动摘要生成任务。通过提升摘要质量，能够更有效地满足用户的健康查询需求，改善医疗服务的可及性和效率。

## 📄 摘要（原文）

> Consumer Health Queries (CHQs) in Bengali (Bangla), a low-resource language, often contain extraneous details, complicating efficient medical responses. This study investigates the zero-shot performance of nine advanced large language models (LLMs): GPT-3.5-Turbo, GPT-4, Claude-3.5-Sonnet, Llama3-70b-Instruct, Mixtral-8x22b-Instruct, Gemini-1.5-Pro, Qwen2-72b-Instruct, Gemma-2-27b, and Athene-70B, in summarizing Bangla CHQs. Using the BanglaCHQ-Summ dataset comprising 2,350 annotated query-summary pairs, we benchmarked these LLMs using ROUGE metrics against Bangla T5, a fine-tuned state-of-the-art model. Mixtral-8x22b-Instruct emerged as the top performing model in ROUGE-1 and ROUGE-L, while Bangla T5 excelled in ROUGE-2. The results demonstrate that zero-shot LLMs can rival fine-tuned models, achieving high-quality summaries even without task-specific training. This work underscores the potential of LLMs in addressing challenges in low-resource languages, providing scalable solutions for healthcare query summarization.

