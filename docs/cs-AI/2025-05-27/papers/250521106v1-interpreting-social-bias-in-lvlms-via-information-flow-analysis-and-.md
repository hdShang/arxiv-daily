---
layout: default
title: Interpreting Social Bias in LVLMs via Information Flow Analysis and Multi-Round Dialogue Evaluation
---

# Interpreting Social Bias in LVLMs via Information Flow Analysis and Multi-Round Dialogue Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21106" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21106v1</a>
  <a href="https://arxiv.org/pdf/2505.21106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21106v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21106v1', 'Interpreting Social Bias in LVLMs via Information Flow Analysis and Multi-Round Dialogue Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyang Ji, Yifan Jia, Shang Gao, Yutao Yue

**分类**: cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**通过信息流分析与多轮对话评估揭示LVLM中的社会偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `社会偏见` `信息流分析` `多轮对话` `多模态学习` `模型解释性` `人工智能伦理`

## 📋 核心要点

1. 现有方法主要集中于检测和量化社会偏见，但对其内部机制的理解不足。
2. 本文提出结合信息流分析与多轮对话评估的框架，旨在揭示社会偏见的起源。
3. 实验结果表明，LVLM在处理不同人口群体的图像时，信息使用存在显著差异，揭示了偏见的内在机制。

## 📝 摘要（中文）

大型视觉语言模型（LVLM）在多模态任务中取得了显著进展，但也表现出明显的社会偏见。这些偏见通常表现为中性概念与敏感人类属性之间的意外关联，导致模型在不同人口群体中的行为差异。现有研究主要集中在检测和量化这些偏见上，但对模型内部机制的理解有限。为此，本文提出了一种结合信息流分析与多轮对话评估的解释框架，旨在从不平衡的内部信息利用角度理解社会偏见的起源。通过实验发现，LVLM在处理不同人口群体的图像时，信息使用存在系统性差异，表明社会偏见深植于模型的内部推理动态中。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型（LVLM）中存在的社会偏见问题，现有方法在理解模型内部机制方面存在不足。

**核心思路**：通过信息流分析识别模型推理过程中高贡献的图像标记，并设计多轮对话机制评估这些标记编码敏感信息的程度。

**技术框架**：整体架构包括信息流分析模块和多轮对话评估模块，前者用于识别关键图像标记，后者用于评估这些标记的敏感信息编码。

**关键创新**：提出的信息流分析与多轮对话评估的结合，为理解社会偏见的形成提供了新的视角，区别于传统的检测和量化方法。

**关键设计**：在信息流分析中，重点识别高贡献图像标记；在多轮对话中，设计了特定的对话机制以评估标记的敏感性，确保实验的有效性和准确性。

## 📊 实验亮点

实验结果显示，LVLM在处理不同人口群体的图像时，信息使用存在系统性差异，表明社会偏见深植于模型的内部推理动态中。具体而言，模型在处理某些群体时，信息流的利用效率显著低于其他群体，揭示了偏见的内在机制。

## 🎯 应用场景

该研究的潜在应用领域包括社会科学研究、人工智能伦理以及多模态系统的设计与优化。通过理解和减少模型中的社会偏见，可以提升AI系统在实际应用中的公平性和可靠性，促进更广泛的社会接受度。

## 📄 摘要（原文）

> Large Vision Language Models (LVLMs) have achieved remarkable progress in multimodal tasks, yet they also exhibit notable social biases. These biases often manifest as unintended associations between neutral concepts and sensitive human attributes, leading to disparate model behaviors across demographic groups. While existing studies primarily focus on detecting and quantifying such biases, they offer limited insight into the underlying mechanisms within the models. To address this gap, we propose an explanatory framework that combines information flow analysis with multi-round dialogue evaluation, aiming to understand the origin of social bias from the perspective of imbalanced internal information utilization. Specifically, we first identify high-contribution image tokens involved in the model's reasoning process for neutral questions via information flow analysis. Then, we design a multi-turn dialogue mechanism to evaluate the extent to which these key tokens encode sensitive information. Extensive experiments reveal that LVLMs exhibit systematic disparities in information usage when processing images of different demographic groups, suggesting that social bias is deeply rooted in the model's internal reasoning dynamics. Furthermore, we complement our findings from a textual modality perspective, showing that the model's semantic representations already display biased proximity patterns, thereby offering a cross-modal explanation of bias formation.

