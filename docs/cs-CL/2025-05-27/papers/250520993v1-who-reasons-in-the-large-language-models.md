---
layout: default
title: Who Reasons in the Large Language Models?
---

# Who Reasons in the Large Language Models?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20993" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20993v1</a>
  <a href="https://arxiv.org/pdf/2505.20993.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20993v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20993v1', 'Who Reasons in the Large Language Models?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jie Shao, Jianxin Wu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出Stethoscope for Networks以揭示大语言模型的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `输出投影模块` `多头自注意力` `模型可解释性` `诊断工具` `针对性训练`

## 📋 核心要点

1. 现有大型语言模型的推理能力来源尚不明确，是否源于整个模型、特定模块或仅为过拟合的产物仍是一个开放问题。
2. 本文提出Stethoscope for Networks（SfN）工具，旨在深入探测和分析LLMs的内部行为，验证推理能力的来源。
3. 通过实验，发现输出投影模块（oproj）在推理中起核心作用，而其他模块则主要用于提升对话流畅性，提供了新的可解释性视角。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）表现出色，但赋予它们新能力（如数学推理）的过程仍然主要依赖经验且不透明。本文假设，经过良好训练的LLMs的推理能力主要归因于变换器多头自注意力机制中的输出投影模块（oproj）。为支持这一假设，我们引入了Stethoscope for Networks（SfN），一套旨在探测和分析LLMs内部行为的诊断工具。通过SfN，我们提供了间接和实证证据，表明oproj在推理中发挥了核心作用，而其他模块则更多地促进流畅对话。这些发现为LLM的可解释性提供了新视角，并为更具针对性的训练策略开辟了新途径，可能使LLMs更高效和专业化。

## 🔬 方法详解

**问题定义**：本文旨在揭示大型语言模型的推理能力来源，现有方法对推理能力的理解多为经验性，缺乏系统性分析。

**核心思路**：我们假设推理能力主要源于输出投影模块（oproj），并通过Stethoscope for Networks（SfN）工具进行深入分析，以验证这一假设。

**技术框架**：SfN工具包含多个诊断模块，能够探测LLMs内部的行为，尤其是oproj模块的功能与其他模块的对比。

**关键创新**：引入SfN作为分析工具，系统性地探讨了LLMs推理能力的来源，强调了oproj模块的重要性，这与传统的经验性分析方法有本质区别。

**关键设计**：在实验中，我们设计了多种测试场景，通过对比不同模块的表现，量化oproj在推理任务中的贡献，同时确保其他模块在对话流畅性上的作用得到充分评估。

## 📊 实验亮点

实验结果表明，oproj模块在推理任务中表现出显著优势，相较于其他模块，其对推理能力的贡献更为突出。这一发现为LLMs的可解释性提供了新的视角，并为未来的模型设计提供了实证依据。

## 🎯 应用场景

该研究为大型语言模型的训练和优化提供了新的思路，尤其是在推理能力和对话生成的平衡方面。未来，基于oproj模块的针对性训练策略可能会提升模型在特定任务上的表现，推动智能对话系统和自动化推理工具的发展。

## 📄 摘要（原文）

> Despite the impressive performance of large language models (LLMs), the process of endowing them with new capabilities--such as mathematical reasoning--remains largely empirical and opaque. A critical open question is whether reasoning abilities stem from the entire model, specific modules, or are merely artifacts of overfitting. In this work, we hypothesize that the reasoning capabilities in well-trained LLMs are primarily attributed to the output projection module (oproj) in the Transformer's multi-head self-attention (MHSA) mechanism. To support this hypothesis, we introduce Stethoscope for Networks (SfN), a suite of diagnostic tools designed to probe and analyze the internal behaviors of LLMs. Using SfN, we provide both circumstantial and empirical evidence suggesting that oproj plays a central role in enabling reasoning, whereas other modules contribute more to fluent dialogue. These findings offer a new perspective on LLM interpretability and open avenues for more targeted training strategies, potentially enabling more efficient and specialized LLMs.

