---
layout: default
title: "ToxiFrench: Benchmarking and Enhancing Language Models via CoT Fine-Tuning for French Toxicity Detection"
---

# ToxiFrench: Benchmarking and Enhancing Language Models via CoT Fine-Tuning for French Toxicity Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11281" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11281v1</a>
  <a href="https://arxiv.org/pdf/2508.11281.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11281v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11281v1', 'ToxiFrench: Benchmarking and Enhancing Language Models via CoT Fine-Tuning for French Toxicity Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Axel Delaval, Shujian Yang, Haicheng Wang, Han Qiu, Jialiang Lu

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-08-15

**备注**: 14 pages, 5 figures, 8 tables. This paper introduces TOXIFRENCH, a new large-scale benchmark for French toxicity detection, and proposes a Chain-of-Thought (CoT) fine-tuning method with a dynamic weighted loss. The resulting fine-tuned 4B parameter model, ToxiFrench, achieves state-of-the-art performance, outperforming larger models like GPT-4o

---

## 💡 一句话要点

**提出ToxiFrench以解决法语毒性检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法语毒性检测` `链式思维微调` `动态加权损失` `小型语言模型` `数据集构建` `多语言能力` `模型评估`

## 📋 核心要点

1. 法语毒性检测的现有方法进展缓慢，缺乏相关的大规模数据集，导致模型性能不足。
2. 提出TOXIFRENCH基准数据集，并采用链式思维微调策略，通过动态加权损失提升模型决策的可信度。
3. 微调后的4B模型在F1分数上提高了13%，超越了多个大型语言模型，展示了强大的多语言能力。

## 📝 摘要（中文）

使用语言模型检测有毒内容至关重要，但在法语领域仍面临挑战，主要由于缺乏文化相关的大规模数据集。本文介绍了TOXIFRENCH，一个包含53,622条法语在线评论的新公共基准，采用半自动注释流程，减少了人工标注的工作量。研究发现，小型语言模型在毒性检测任务中表现出更强的鲁棒性和泛化能力。基于此，提出了一种新的链式思维（CoT）微调策略，通过动态加权损失显著提高模型的决策可信度。经过微调的4B模型在F1分数上比基线提高了13%，并超越了GPT-40和Gemini-2.5等大型语言模型。进一步的跨语言评估显示出强大的多语言能力，表明该方法可以有效扩展到其他语言和安全关键的分类任务。

## 🔬 方法详解

**问题定义**：本文旨在解决法语毒性检测中的数据稀缺和模型性能不足的问题。现有方法在法语领域的应用受限，缺乏有效的标注数据和模型评估标准。

**核心思路**：通过构建TOXIFRENCH数据集，结合半自动注释流程，减少人工标注工作，同时提出链式思维微调策略，以动态加权损失提升模型的决策能力。

**技术框架**：整体流程包括数据集构建、模型基准测试和微调。数据集通过高置信度的LLM预注释和人工验证构建，模型则在此基础上进行评估和优化。

**关键创新**：提出的链式思维微调策略是本研究的核心创新，与传统的微调方法不同，它通过动态加权损失强调模型最终决策的可信度。

**关键设计**：在微调过程中，采用动态加权损失函数，重点关注模型的最终输出。此外，模型结构经过优化，以适应毒性检测任务的特定需求。通过这些设计，模型在鲁棒性和泛化能力上取得了显著提升。

## 📊 实验亮点

实验结果显示，微调后的4B模型在F1分数上比基线提高了13%，并在毒性检测任务中超越了GPT-40和Gemini-2.5等大型语言模型。这一发现挑战了传统对大型模型性能的预期，表明小型语言模型在特定任务中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容监控、在线评论审核和自动化内容过滤等。通过提升法语毒性检测的准确性，能够有效减少有害内容的传播，增强网络环境的安全性。此外，该方法的多语言能力使其在全球范围内的应用前景广阔。

## 📄 摘要（原文）

> Detecting toxic content using language models is crucial yet challenging. While substantial progress has been made in English, toxicity detection in French remains underdeveloped, primarily due to the lack of culturally relevant, large-scale datasets. In this work, we introduce TOXIFRENCH, a new public benchmark of 53,622 French online comments, constructed via a semi-automated annotation pipeline that reduces manual labeling to only 10% through high-confidence LLM-based pre-annotation and human verification. Then, we benchmark a broad range of models and uncover a counterintuitive insight: Small Language Models (SLMs) outperform many larger models in robustness and generalization under the toxicity detection task. Motivated by this finding, we propose a novel Chain-of-Thought (CoT) fine-tuning strategy using a dynamic weighted loss that progressively emphasizes the model's final decision, significantly improving faithfulness. Our fine-tuned 4B model achieves state-of-the-art performance, improving its F1 score by 13% over its baseline and outperforming LLMs such as GPT-40 and Gemini-2.5. Further evaluation on a cross-lingual toxicity benchmark demonstrates strong multilingual ability, suggesting that our methodology can be effectively extended to other languages and safety-critical classification tasks.

