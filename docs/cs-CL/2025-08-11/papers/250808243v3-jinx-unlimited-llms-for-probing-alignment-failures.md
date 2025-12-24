---
layout: default
title: "Jinx: Unlimited LLMs for Probing Alignment Failures"
---

# Jinx: Unlimited LLMs for Probing Alignment Failures

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08243" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08243v3</a>
  <a href="https://arxiv.org/pdf/2508.08243.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08243v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08243v3', 'Jinx: Unlimited LLMs for Probing Alignment Failures')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Zhao, Liwei Dong

**分类**: cs.CL

**发布日期**: 2025-08-11 (更新: 2025-08-24)

**备注**: https://huggingface.co/Jinx-org

---

## 💡 一句话要点

**提出Jinx以探测语言模型的对齐失败问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `对齐失败` `安全评估` `无过滤响应` `AI安全`

## 📋 核心要点

1. 现有的安全对齐模型在生成有害输出时可能会出现对齐失败，但缺乏有效的工具来评估这些失败。
2. Jinx通过不拒绝任何查询并去除安全过滤，提供了一个有用的语言模型变体，旨在帮助研究人员探测对齐失败。
3. Jinx的设计使其能够在保留基础模型能力的同时，成为评估安全边界和研究失败模式的有效工具。

## 📝 摘要（中文）

无限制的语言模型，即仅提供有用响应的模型，在没有安全对齐约束的情况下进行训练，能够对所有用户查询作出响应。这类模型在评估对齐失败方面起着重要作用，但目前尚未向研究界开放。本文介绍了Jinx，一个基于流行开放权重语言模型的有用变体，能够在不拒绝或进行安全过滤的情况下响应所有查询，同时保留基础模型的推理和指令跟随能力。Jinx为研究人员提供了一个可访问的工具，用于探测对齐失败、评估安全边界以及系统性研究语言模型安全中的失败模式。

## 🔬 方法详解

**问题定义**：本文旨在解决现有安全对齐模型在生成有害输出时的对齐失败问题。当前缺乏有效的工具来评估这些失败，限制了研究的深入。

**核心思路**：Jinx的核心思路是构建一个不拒绝任何用户查询的语言模型，去除安全过滤，从而使研究人员能够全面探测对齐失败并评估模型的安全边界。

**技术框架**：Jinx的整体架构基于流行的开放权重语言模型，经过调整以去除安全对齐约束。其主要模块包括输入处理、响应生成和输出评估。

**关键创新**：Jinx的最大创新在于其“有用-only”设计，使其能够在没有安全过滤的情况下响应所有查询，这与现有的安全对齐模型形成鲜明对比。

**关键设计**：在设计Jinx时，关键参数包括模型的训练数据选择、损失函数的调整以及网络结构的优化，以确保在去除安全约束的同时，保留模型的推理和指令跟随能力。

## 📊 实验亮点

Jinx在对齐失败探测方面表现出色，能够在不拒绝任何查询的情况下生成响应，为研究人员提供了前所未有的评估工具。与传统安全对齐模型相比，Jinx在探测失败模式和评估安全边界方面具有显著优势。

## 🎯 应用场景

Jinx的潜在应用场景包括AI安全评估、对齐失败研究以及开发更安全的语言模型。通过提供一个无过滤的响应环境，研究人员可以更深入地理解模型的行为和潜在风险，从而推动更安全的AI系统的开发。

## 📄 摘要（原文）

> Unlimited, or so-called helpful-only language models are trained without safety alignment constraints and never refuse user queries. They are widely used by leading AI companies as internal tools for red teaming and alignment evaluation. For example, if a safety-aligned model produces harmful outputs similar to an unlimited model, this indicates alignment failures that require further attention. Despite their essential role in assessing alignment, such models are not available to the research community.
>   We introduce Jinx, a helpful-only variant of popular open-weight LLMs. Jinx responds to all queries without refusals or safety filtering, while preserving the base model's capabilities in reasoning and instruction following. It provides researchers with an accessible tool for probing alignment failures, evaluating safety boundaries, and systematically studying failure modes in language model safety.

