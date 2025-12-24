---
layout: default
title: Evaluating Reasoning LLMs for Suicide Screening with the Columbia-Suicide Severity Rating Scale
---

# Evaluating Reasoning LLMs for Suicide Screening with the Columbia-Suicide Severity Rating Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13480" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13480v1</a>
  <a href="https://arxiv.org/pdf/2505.13480.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13480v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13480v1', 'Evaluating Reasoning LLMs for Suicide Screening with the Columbia-Suicide Severity Rating Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Avinash Patil, Siru Tao, Amardeep Gedhu

**分类**: cs.CL, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-05-11

**备注**: 8 Pages, 6 Figures, 1 Table

**🔗 代码/项目**: [GITHUB](https://github.com/av9ash/llm_cssrs_code)

---

## 💡 一句话要点

**评估大型语言模型在自杀筛查中的应用潜力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自杀风险评估` `大型语言模型` `自动化筛查` `心理健康` `哥伦比亚自杀严重性评分量表`

## 📋 核心要点

1. 自杀风险评估的现有方法面临准确性和及时性不足的挑战，尤其是在在线平台上。
2. 本研究通过评估多种大型语言模型在自杀风险评估中的表现，提出了一种新的自动化筛查方法。
3. 实验结果显示，Claude和GPT模型的表现与人类标注高度一致，Mistral模型的序数预测误差最低，展示了模型的有效性。

## 📝 摘要（中文）

自杀预防是一个重要的公共卫生挑战。随着大型语言模型（LLMs）的出现，个体可能开始向AI系统而非人类披露自杀意念。本研究评估了LLMs在使用哥伦比亚自杀严重性评分量表（C-SSRS）进行自动化自杀风险评估的能力。我们评估了包括Claude、GPT、Mistral和LLaMA在内的六个模型在7级严重性评分（0-6级）上的零-shot性能。结果表明，Claude和GPT与人类标注高度一致，而Mistral的序数预测误差最低。大多数模型表现出序数敏感性，误分类通常发生在相邻的严重性级别之间。我们进一步分析了混淆模式、误分类来源和伦理考虑，强调了人类监督、透明性和谨慎部署的重要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决自杀风险评估中人工标注的局限性，现有方法在准确性和效率上存在不足，尤其是在处理大量在线数据时。

**核心思路**：通过评估大型语言模型在自杀风险评估中的零-shot性能，探索其在自动化筛查中的应用潜力，以提高评估的效率和准确性。

**技术框架**：研究使用哥伦比亚自杀严重性评分量表（C-SSRS）作为评估标准，测试六个不同的语言模型，包括Claude、GPT、Mistral和LLaMA，分析其在7级严重性评分上的表现。

**关键创新**：本研究的创新点在于将大型语言模型应用于自杀风险评估，提供了一种新的自动化方法，与传统人工标注相比，能够更快速地处理大量信息。

**关键设计**：在实验中，模型的参数设置和损失函数经过精心设计，以确保在不同严重性级别之间的分类准确性，特别关注序数敏感性和误分类模式的分析。

## 📊 实验亮点

实验结果显示，Claude和GPT模型在自杀风险评估中与人类标注高度一致，而Mistral模型的序数预测误差最低，表明其在处理相邻严重性级别时的准确性更高。这些结果为大型语言模型在心理健康领域的应用提供了有力支持。

## 🎯 应用场景

该研究的潜在应用领域包括在线社交平台、心理健康支持系统和危机干预服务。通过自动化自杀风险评估，能够更及时地识别高风险个体，从而提供必要的支持和干预，具有重要的社会价值和实际意义。

## 📄 摘要（原文）

> Suicide prevention remains a critical public health challenge. While online platforms such as Reddit's r/SuicideWatch have historically provided spaces for individuals to express suicidal thoughts and seek community support, the advent of large language models (LLMs) introduces a new paradigm-where individuals may begin disclosing ideation to AI systems instead of humans. This study evaluates the capability of LLMs to perform automated suicide risk assessment using the Columbia-Suicide Severity Rating Scale (C-SSRS). We assess the zero-shot performance of six models-including Claude, GPT, Mistral, and LLaMA-in classifying posts across a 7-point severity scale (Levels 0-6). Results indicate that Claude and GPT closely align with human annotations, while Mistral achieves the lowest ordinal prediction error. Most models exhibit ordinal sensitivity, with misclassifications typically occurring between adjacent severity levels. We further analyze confusion patterns, misclassification sources, and ethical considerations, underscoring the importance of human oversight, transparency, and cautious deployment. Full code and supplementary materials are available at https://github.com/av9ash/llm_cssrs_code.

