---
layout: default
title: DeepCritic: Deliberate Critique with Large Language Models
---

# DeepCritic: Deliberate Critique with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00662" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00662v1</a>
  <a href="https://arxiv.org/pdf/2505.00662.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00662v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00662v1', 'DeepCritic: Deliberate Critique with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenkai Yang, Jingwen Chen, Yankai Lin, Ji-Rong Wen

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-01

**备注**: Work in progress. Data and models are available at https://github.com/RUCBM/DeepCritic

---

## 💡 一句话要点

**提出DeepCritic以解决LLM输出反馈不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `批评能力` `数学解题` `强化学习` `自动化监督` `深度学习` `教育技术`

## 📋 核心要点

1. 现有的LLM批评者在数学解题过程中提供的反馈往往过于肤浅，导致生成模型难以获得有效的纠错信息。
2. 本文提出了一种两阶段的框架，通过生成长形式的批评和强化学习来提升LLMs的批判能力。
3. 实验结果表明，所提出的批评模型在错误识别基准上显著优于现有的LLM批评者，能够提供更详细的反馈。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，提供准确的反馈和可扩展的监督变得愈发重要。本文提出了一种新颖的两阶段框架，旨在增强LLMs在数学解题中的批判能力。现有的LLM批评者往往提供的反馈过于肤浅，导致判断准确性低，无法为生成模型提供足够的纠错信息。通过利用Qwen2.5-72B-Instruct生成长达4.5K的批评作为监督微调的种子数据，并结合强化学习，本文开发的批评模型在多项错误识别基准上显著优于现有的LLM批评者，能够更有效地帮助生成模型修正错误步骤。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM批评者在数学解题中反馈不足的问题，现有方法往往提供的批评过于表面，无法有效指导生成模型进行纠错。

**核心思路**：提出一种两阶段的框架，首先生成长形式的批评作为种子数据进行微调，然后通过强化学习进一步提升批评能力，以实现更深入的逐步批评。

**技术框架**：整体流程分为两个主要阶段：第一阶段使用Qwen2.5-72B-Instruct生成4.5K的长形式批评作为监督微调的种子数据；第二阶段则对微调后的模型进行强化学习，使用人类标注数据或通过蒙特卡罗采样获得的自动标注数据进行训练。

**关键创新**：最重要的创新在于通过两阶段框架实现了对每个推理步骤的深度批评，显著提升了批评的准确性和有效性，与现有方法相比，能够提供更为详细和多角度的反馈。

**关键设计**：在模型设计中，采用了Qwen2.5-7B-Instruct作为基础模型，结合多种损失函数和参数设置，以确保批评的多样性和深度，同时利用强化学习策略来激励模型的批评能力。

## 📊 实验亮点

实验结果显示，所提出的DeepCritic模型在多项错误识别基准上显著优于现有的LLM批评者，包括同规模的DeepSeek-R1-distill模型和GPT-4o，提升幅度达到XX%（具体数据待补充），并且能够更有效地帮助生成模型修正错误步骤。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、自动化评估系统和智能辅导工具。通过提升LLMs的批评能力，可以为学生提供更有效的学习反馈，帮助他们更好地理解和纠正错误，从而提高学习效率和效果。未来，该技术有望在更广泛的领域中应用，如智能问答系统和自动化内容生成。

## 📄 摘要（原文）

> As Large Language Models (LLMs) are rapidly evolving, providing accurate feedback and scalable oversight on their outputs becomes an urgent and critical problem. Leveraging LLMs as critique models to achieve automated supervision is a promising solution. In this work, we focus on studying and enhancing the math critique ability of LLMs. Current LLM critics provide critiques that are too shallow and superficial on each step, leading to low judgment accuracy and struggling to offer sufficient feedback for the LLM generator to correct mistakes. To tackle this issue, we propose a novel and effective two-stage framework to develop LLM critics that are capable of deliberately critiquing on each reasoning step of math solutions. In the first stage, we utilize Qwen2.5-72B-Instruct to generate 4.5K long-form critiques as seed data for supervised fine-tuning. Each seed critique consists of deliberate step-wise critiques that includes multi-perspective verifications as well as in-depth critiques of initial critiques for each reasoning step. Then, we perform reinforcement learning on the fine-tuned model with either existing human-labeled data from PRM800K or our automatically annotated data obtained via Monte Carlo sampling-based correctness estimation, to further incentivize its critique ability. Our developed critique model built on Qwen2.5-7B-Instruct not only significantly outperforms existing LLM critics (including the same-sized DeepSeek-R1-distill models and GPT-4o) on various error identification benchmarks, but also more effectively helps the LLM generator refine erroneous steps through more detailed feedback.

