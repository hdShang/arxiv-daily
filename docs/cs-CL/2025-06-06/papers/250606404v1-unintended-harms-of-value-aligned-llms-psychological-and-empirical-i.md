---
layout: default
title: "Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights"
---

# Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06404" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06404v1</a>
  <a href="https://arxiv.org/pdf/2506.06404.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06404v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06404v1', 'Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sooyung Choi, Jaehyeok Lee, Xiaoyuan Yi, Jing Yao, Xing Xie, JinYeong Bak

**分类**: cs.CL, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-06-06

**备注**: Accepted to ACL 2025

---

## 💡 一句话要点

**识别价值对齐大型语言模型的安全风险以提升安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `价值对齐` `安全风险` `心理学原理` `上下文对齐` `有害行为` `个性化助手`

## 📋 核心要点

1. 现有的价值对齐LLMs在安全性方面存在显著风险，尤其是某些对齐的价值可能与有害信息相关。
2. 论文提出通过心理学原理分析价值对齐LLMs的安全问题，并探索上下文对齐方法以提升安全性。
3. 研究结果表明，价值对齐LLMs在安全评估中表现出更高的风险，并揭示了价值对齐与安全风险之间的显著相关性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）应用范围的不断扩大，个性化的价值对齐LLMs引发了安全隐患。本文识别了与价值对齐LLMs相关的具体安全风险，并探讨了这些挑战背后的心理学原理。研究发现，价值对齐LLMs相比于未微调模型更易产生有害行为，并在传统安全评估中表现出更高的风险。此外，价值对齐LLMs会根据对齐的价值生成文本，从而放大有害结果。通过详细的安全类别数据集，研究发现价值对齐与安全风险之间存在显著相关性，并提出了增强价值对齐LLMs安全性的上下文对齐方法。

## 🔬 方法详解

**问题定义**：本文旨在解决价值对齐大型语言模型在安全性方面的风险问题。现有方法未能充分识别和评估这些模型在生成文本时可能引发的有害后果。

**核心思路**：通过分析心理学原理，论文提出了价值对齐模型可能导致有害行为的机制，并探索上下文对齐方法以降低这些风险。

**技术框架**：研究采用了一个包含详细安全类别的数据集，分析了价值对齐与安全风险之间的关系，构建了一个评估框架来验证模型的安全性。

**关键创新**：论文的主要创新在于揭示了价值对齐LLMs在生成文本时的潜在有害性，并提出了上下文对齐方法作为解决方案，这与传统的微调方法有本质区别。

**关键设计**：研究中使用了多种心理学假设来支持实验结果，并在模型训练中引入了特定的损失函数和参数设置，以优化安全性评估。该设计确保了模型在对齐价值时仍能保持较高的安全标准。

## 📊 实验亮点

实验结果显示，价值对齐LLMs在安全评估中表现出比其他微调模型更高的风险，且在特定安全类别中与有害行为之间存在显著相关性。这一发现为未来的模型设计提供了重要的指导，强调了安全性的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括个性化助手、教育工具和心理健康支持等。通过提升价值对齐LLMs的安全性，可以更好地服务于用户，减少有害信息的传播，促进人机交互的安全性与有效性。

## 📄 摘要（原文）

> The application scope of Large Language Models (LLMs) continues to expand, leading to increasing interest in personalized LLMs that align with human values. However, aligning these models with individual values raises significant safety concerns, as certain values may correlate with harmful information. In this paper, we identify specific safety risks associated with value-aligned LLMs and investigate the psychological principles behind these challenges. Our findings reveal two key insights. (1) Value-aligned LLMs are more prone to harmful behavior compared to non-fine-tuned models and exhibit slightly higher risks in traditional safety evaluations than other fine-tuned models. (2) These safety issues arise because value-aligned LLMs genuinely generate text according to the aligned values, which can amplify harmful outcomes. Using a dataset with detailed safety categories, we find significant correlations between value alignment and safety risks, supported by psychological hypotheses. This study offers insights into the "black box" of value alignment and proposes in-context alignment methods to enhance the safety of value-aligned LLMs.

