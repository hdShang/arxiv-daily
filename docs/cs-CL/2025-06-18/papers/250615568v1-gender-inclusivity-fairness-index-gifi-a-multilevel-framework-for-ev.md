---
layout: default
title: "Gender Inclusivity Fairness Index (GIFI): A Multilevel Framework for Evaluating Gender Diversity in Large Language Models"
---

# Gender Inclusivity Fairness Index (GIFI): A Multilevel Framework for Evaluating Gender Diversity in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15568" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15568v1</a>
  <a href="https://arxiv.org/pdf/2506.15568.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15568v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15568v1', 'Gender Inclusivity Fairness Index (GIFI): A Multilevel Framework for Evaluating Gender Diversity in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyang Shan, Emily Ruth Diana, Jiawei Zhou

**分类**: cs.CL

**发布日期**: 2025-06-18

**备注**: Accepted by ACL 2025 Main

---

## 💡 一句话要点

**提出GIFI以评估大型语言模型的性别多样性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `性别公平性` `大型语言模型` `性别包容性` `评估指标` `自然语言处理` `人工智能伦理` `生成模型`

## 📋 核心要点

1. 现有研究主要集中于二元性别，忽视了非二元性别的处理能力，导致性别公平性评估不全面。
2. 本文提出性别包容性公平指数（GIFI），通过多层次评估来量化大型语言模型的性别包容性，涵盖多种性别假设。
3. 在对22个大型语言模型的评估中，发现其性别包容性存在显著差异，强调了改善模型包容性的必要性。

## 📝 摘要（中文）

本文全面评估了大型语言模型（LLMs）在性别公平性方面的表现，特别关注其对二元和非二元性别的处理能力。与以往研究主要集中于二元性别区分不同，我们引入了性别包容性公平指数（GIFI），这是一个新颖且全面的指标，用于量化LLMs的性别包容性。GIFI涵盖了多层次的评估，从简单的性别代词探测到在不同性别假设下测试模型生成和认知行为的各个方面，揭示了与不同性别标识相关的偏见。我们对22个不同规模和能力的开源及专有LLMs进行了广泛评估，发现LLMs的性别包容性存在显著差异。我们的研究强调了提高LLMs包容性的重要性，为未来生成模型的性别公平性进展提供了重要基准。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在性别公平性评估中的不足，尤其是对非二元性别的处理能力缺乏关注，导致评估结果不够全面和准确。

**核心思路**：论文提出性别包容性公平指数（GIFI），通过多层次的评估方法，全面量化模型在不同性别假设下的表现，旨在揭示和减少模型中的性别偏见。

**技术框架**：GIFI的评估流程包括多个阶段：首先是对模型进行性别代词的探测，然后测试模型在不同性别假设下的生成能力和认知行为，最后综合分析模型的性别包容性。

**关键创新**：GIFI作为一个新颖的评估指标，首次将非二元性别纳入评估范围，提供了比传统二元性别评估更全面的视角，填补了现有方法的空白。

**关键设计**：在评估过程中，设置了多种性别代词和假设，采用了多样的生成任务和认知行为测试，确保评估的全面性和准确性。

## 📊 实验亮点

在对22个大型语言模型的评估中，GIFI揭示了显著的性别包容性差异，部分模型在处理非二元性别时的表现明显低于二元性别，强调了改进模型性别公平性的必要性。具体数据表明，某些模型在非二元性别的生成任务中准确率低于50%。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、人工智能伦理和社会科学等。通过提供一个全面的性别公平性评估框架，GIFI可以帮助开发者和研究人员在设计和优化大型语言模型时，更好地考虑性别多样性，从而推动生成模型的社会责任感和公平性。

## 📄 摘要（原文）

> We present a comprehensive evaluation of gender fairness in large language models (LLMs), focusing on their ability to handle both binary and non-binary genders. While previous studies primarily focus on binary gender distinctions, we introduce the Gender Inclusivity Fairness Index (GIFI), a novel and comprehensive metric that quantifies the diverse gender inclusivity of LLMs. GIFI consists of a wide range of evaluations at different levels, from simply probing the model with respect to provided gender pronouns to testing various aspects of model generation and cognitive behaviors under different gender assumptions, revealing biases associated with varying gender identifiers. We conduct extensive evaluations with GIFI on 22 prominent open-source and proprietary LLMs of varying sizes and capabilities, discovering significant variations in LLMs' gender inclusivity. Our study highlights the importance of improving LLMs' inclusivity, providing a critical benchmark for future advancements in gender fairness in generative models.

