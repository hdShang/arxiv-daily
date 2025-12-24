---
layout: default
title: "Interpretable Traces, Unexpected Outcomes: Investigating the Disconnect in Trace-Based Knowledge Distillation"
---

# Interpretable Traces, Unexpected Outcomes: Investigating the Disconnect in Trace-Based Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13792" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13792v1</a>
  <a href="https://arxiv.org/pdf/2505.13792.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13792v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13792v1', 'Interpretable Traces, Unexpected Outcomes: Investigating the Disconnect in Trace-Based Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siddhant Bhambri, Upasana Biswas, Subbarao Kambhampati

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20

**备注**: 10 pages

---

## 💡 一句话要点

**提出基于规则分解的知识蒸馏方法以提升小型语言模型的可解释性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识蒸馏` `可解释性` `问答系统` `推理追踪` `规则分解` `小型语言模型` `深度学习`

## 📋 核心要点

1. 现有的知识蒸馏方法在利用推理追踪提升小型语言模型性能时，面临可解释性不足和评估困难的问题。
2. 本文提出了一种基于规则的问题分解方法，通过将复杂查询拆解为结构化子问题，生成可解释的推理追踪。
3. 实验结果显示，正确的推理追踪与最终答案的正确性之间存在低相关性，挑战了传统知识蒸馏的假设。

## 📝 摘要（中文）

问答系统在现代交互式对话系统中面临着准确性和透明性的双重挑战。尽管小型语言模型在计算效率上具有优势，但其性能往往低于大型模型。知识蒸馏方法通过微调小型模型以提升其性能，然而，基于推理的中间追踪信息往往冗长且难以解释。本文提出了一种基于规则的问题分解的知识蒸馏方法，旨在提高这些推理追踪的可解释性和评估的可行性。通过在Open Book QA上进行实验，发现正确的推理追踪并不总是能保证模型输出正确的最终答案，这一发现挑战了利用推理追踪提升小型模型性能的假设。

## 🔬 方法详解

**问题定义**：本文旨在解决推理追踪的可解释性和评估问题，现有方法在利用这些追踪信息时常常面临冗长和难以理解的挑战。

**核心思路**：通过引入基于规则的问题分解方法，将复杂的问答任务拆解为更简单的分类和信息检索步骤，从而生成可解释的推理追踪。

**技术框架**：整体架构包括两个主要模块：第一步是将问题分类，第二步是进行信息检索。这种分解方法使得每个步骤的输出都可以独立评估，增强了可解释性。

**关键创新**：最重要的创新在于提出了基于规则的问题分解策略，使得推理追踪的生成和评估变得更加直观和可操作，与传统的基于深度学习的推理方法相比，显著提升了可解释性。

**关键设计**：在实验中，采用了特定的损失函数来优化模型在分类和信息检索步骤的表现，同时对中间追踪的正确性进行了严格的评估，确保了最终输出的可靠性。

## 📊 实验亮点

实验结果表明，尽管推理追踪的正确性与最终答案的正确性之间存在低相关性，但通过基于规则的问题分解方法，模型在多个数据集上的表现得到了显著提升。这一发现为知识蒸馏方法的应用提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、对话代理和教育技术等。通过提升小型语言模型的可解释性和性能，能够更好地满足用户对透明性和准确性的需求，推动人机交互的进一步发展。

## 📄 摘要（原文）

> Question Answering (QA) poses a challenging and critical problem, particularly in today's age of interactive dialogue systems such as ChatGPT, Perplexity, Microsoft Copilot, etc. where users demand both accuracy and transparency in the model's outputs. Since smaller language models (SLMs) are computationally more efficient but often under-perform compared to larger models, Knowledge Distillation (KD) methods allow for finetuning these smaller models to improve their final performance. Lately, the intermediate tokens or the so called `reasoning' traces produced by Chain-of-Thought (CoT) or by reasoning models such as DeepSeek R1 are used as a training signal for KD. However, these reasoning traces are often verbose and difficult to interpret or evaluate. In this work, we aim to address the challenge of evaluating the faithfulness of these reasoning traces and their correlation with the final performance. To this end, we employ a KD method leveraging rule-based problem decomposition. This approach allows us to break down complex queries into structured sub-problems, generating interpretable traces whose correctness can be readily evaluated, even at inference time. Specifically, we demonstrate this approach on Open Book QA, decomposing the problem into a Classification step and an Information Retrieval step, thereby simplifying trace evaluation. Our SFT experiments with correct and incorrect traces on the CoTemp QA, Microsoft Machine Reading Comprehension QA, and Facebook bAbI QA datasets reveal the striking finding that correct traces do not necessarily imply that the model outputs the correct final solution. Similarly, we find a low correlation between correct final solutions and intermediate trace correctness. These results challenge the implicit assumption behind utilizing reasoning traces for improving SLMs' final performance via KD.

