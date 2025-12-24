---
layout: default
title: Leveraging Large Language Models for Bengali Math Word Problem Solving with Chain of Thought Reasoning
---

# Leveraging Large Language Models for Bengali Math Word Problem Solving with Chain of Thought Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21354" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21354v2</a>
  <a href="https://arxiv.org/pdf/2505.21354.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21354v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21354v2', 'Leveraging Large Language Models for Bengali Math Word Problem Solving with Chain of Thought Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bidyarthi Paul, Jalisha Jashim Era, Mirazur Rahman Zim, Tahmid Sattar Aothoi, Faisal Muhammad Shah

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-27 (更新: 2025-07-30)

---

## 💡 一句话要点

**提出SOMADHAN数据集以解决孟加拉数学语言问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `孟加拉语处理` `数学语言问题` `链式思维` `低资源语言` `大型语言模型`

## 📋 核心要点

1. 孟加拉数学语言问题的解决仍面临挑战，现有模型在复杂问题上表现不佳，缺乏相应的数据集。
2. 本文提出SOMADHAN数据集，包含8792个复杂的孟加拉MWPs，支持推理评估和模型开发。
3. 实验结果显示，使用链式思维提示的模型在多步骤逻辑任务上表现优异，LLaMA-3.3 70B模型达到了88%的准确率。

## 📝 摘要（中文）

解决孟加拉数学语言问题（MWPs）在自然语言处理（NLP）领域仍然是一个重大挑战，主要由于该语言的低资源状态和多步骤推理的需求。现有模型在复杂的孟加拉MWPs上表现不佳，原因在于缺乏人类标注的数据集。为此，本文创建了SOMADHAN数据集，包含8792个复杂的孟加拉MWPs及其手动编写的逐步解决方案。通过使用该数据集，评估了多种大型语言模型（LLMs），并发现链式思维（CoT）提示显著提高了模型在多步骤逻辑任务中的表现。LLaMA-3.3 70B模型在少量示例的CoT提示下达到了88%的最高准确率。我们的研究为孟加拉NLP填补了关键空白，提供了高质量的推理数据集和可扩展的解决框架。

## 🔬 方法详解

**问题定义**：本文旨在解决孟加拉数学语言问题（MWPs）的推理挑战，现有方法因缺乏人类标注的数据集而难以处理复杂问题。

**核心思路**：通过创建SOMADHAN数据集，提供高质量的手动解决方案，支持多步骤推理的评估和模型训练。使用链式思维（CoT）提示来提升模型在复杂任务中的表现。

**技术框架**：整体架构包括数据集构建、模型选择与评估。首先构建SOMADHAN数据集，然后对多种大型语言模型进行评估，比较标准提示与CoT提示的效果。

**关键创新**：最重要的创新在于创建了一个专门针对孟加拉MWPs的高质量数据集，并通过CoT提示显著提升了模型的推理能力。与现有方法相比，提供了更具针对性的解决方案。

**关键设计**：在模型评估中，采用了零-shot和few-shot提示策略，并应用低秩适应（LoRA）技术进行高效微调，以降低计算成本。

## 📊 实验亮点

实验结果显示，使用链式思维提示的模型在多步骤逻辑任务上表现显著提升，LLaMA-3.3 70B模型在few-shot CoT提示下达到了88%的准确率，较标准提示有明显改善，展示了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、语言学习工具和智能辅导系统。通过提升孟加拉语的数学推理能力，可以帮助学生更好地理解数学问题，促进教育公平，推动低资源语言的研究与发展。

## 📄 摘要（原文）

> Solving Bengali Math Word Problems (MWPs) remains a major challenge in natural language processing (NLP) due to the language's low-resource status and the multi-step reasoning required. Existing models struggle with complex Bengali MWPs, largely because no human-annotated Bengali dataset has previously addressed this task. This gap has limited progress in Bengali mathematical reasoning. To address this, we created SOMADHAN, a dataset of 8792 complex Bengali MWPs with manually written, step-by-step solutions. We designed this dataset to support reasoning-focused evaluation and model development in a linguistically underrepresented context. Using SOMADHAN, we evaluated a range of large language models (LLMs) - including GPT-4o, GPT-3.5 Turbo, LLaMA series models, Deepseek, and Qwen - through both zero-shot and few-shot prompting with and without Chain of Thought (CoT) reasoning. CoT prompting consistently improved performance over standard prompting, especially in tasks requiring multi-step logic. LLaMA-3.3 70B achieved the highest accuracy of 88% with few-shot CoT prompting. We also applied Low-Rank Adaptation (LoRA) to fine-tune models efficiently, enabling them to adapt to Bengali MWPs with minimal computational cost. Our work fills a critical gap in Bengali NLP by providing a high-quality reasoning dataset and a scalable framework for solving complex MWPs. We aim to advance equitable research in low-resource languages and enhance reasoning capabilities in educational and language technologies.

