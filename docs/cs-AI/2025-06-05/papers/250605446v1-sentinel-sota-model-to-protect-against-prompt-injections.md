---
layout: default
title: "Sentinel: SOTA model to protect against prompt injections"
---

# Sentinel: SOTA model to protect against prompt injections

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05446" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05446v1</a>
  <a href="https://arxiv.org/pdf/2506.05446.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05446v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05446v1', 'Sentinel: SOTA model to protect against prompt injections')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dror Ivry, Oran Nahum

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-05

**备注**: 6 pages, 2 tables

---

## 💡 一句话要点

**提出Sentinel以防御提示注入攻击**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `提示注入` `大型语言模型` `安全性` `ModernBERT` `检测模型` `数据集策划` `对抗性攻击` `自然语言处理`

## 📋 核心要点

1. 现有的大型语言模型在面对提示注入攻击时表现出明显的脆弱性，导致模型输出不符合预期。
2. Sentinel通过基于ModernBERT-large架构的检测模型，结合多样化的数据集，提供了一种有效的防御机制。
3. 在内部测试集上，Sentinel达到了0.987的准确率和0.980的F1分数，显著优于现有的基线模型。

## 📝 摘要（中文）

大型语言模型（LLMs）日益强大，但仍然容易受到提示注入攻击的影响，这种攻击会导致模型偏离其预期指令。本文介绍了Sentinel，这是一种基于ModernBERT-large架构的新型检测模型qualifire/prompt-injection-sentinel。通过利用ModernBERT的先进特性，并在一个包含多个开源和私有数据集的广泛多样化数据集上进行微调，Sentinel实现了最先进的性能。该数据集融合了多种攻击类型，从角色扮演和指令劫持到生成偏见内容的尝试，以及广泛的良性指令，私有数据集特别针对细微的错误修正和现实世界的误分类。在一个全面的、未见过的内部测试集上，Sentinel展示了0.987的平均准确率和0.980的F1分数。此外，在公共基准测试中，它始终优于强基线如protectai/deberta-v3-base-prompt-injection-v2。本文详细介绍了Sentinel的架构、数据集的精心策划、训练方法以及全面的评估，突出了其卓越的检测能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在提示注入攻击下的脆弱性，现有方法在检测和防御这些攻击时效果不佳，导致模型输出不可靠。

**核心思路**：Sentinel通过构建一个基于ModernBERT-large架构的检测模型，利用丰富的多样化数据集进行训练，以提高对各种提示注入攻击的检测能力。

**技术框架**：Sentinel的整体架构包括数据集的精心策划、模型的训练和评估三个主要阶段。数据集涵盖多种攻击类型和良性指令，确保模型的泛化能力。

**关键创新**：Sentinel的主要创新在于其数据集的多样性和针对性，特别是在细微错误修正和现实世界误分类方面的私有数据集使用，使其在检测能力上超越了现有方法。

**关键设计**：在模型设计中，Sentinel采用了ModernBERT-large的架构，结合特定的损失函数和参数设置，以优化模型在提示注入检测任务中的表现。

## 📊 实验亮点

Sentinel在内部测试集上实现了0.987的平均准确率和0.980的F1分数，显示出卓越的检测能力。此外，在公共基准测试中，Sentinel持续优于protectai/deberta-v3-base-prompt-injection-v2等强基线，证明了其在提示注入防御中的有效性。

## 🎯 应用场景

Sentinel的研究成果在多个领域具有潜在应用价值，包括自然语言处理中的安全性增强、智能助手的可靠性提升以及对抗性攻击防御等。随着大型语言模型的广泛应用，提升其安全性将对保护用户数据和维护系统稳定性产生重要影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly powerful but remain vulnerable to prompt injection attacks, where malicious inputs cause the model to deviate from its intended instructions. This paper introduces Sentinel, a novel detection model, qualifire/prompt-injection-sentinel, based on the \answerdotai/ModernBERT-large architecture. By leveraging ModernBERT's advanced features and fine-tuning on an extensive and diverse dataset comprising a few open-source and private collections, Sentinel achieves state-of-the-art performance. This dataset amalgamates varied attack types, from role-playing and instruction hijacking to attempts to generate biased content, alongside a broad spectrum of benign instructions, with private datasets specifically targeting nuanced error correction and real-world misclassifications. On a comprehensive, unseen internal test set, Sentinel demonstrates an average accuracy of 0.987 and an F1-score of 0.980. Furthermore, when evaluated on public benchmarks, it consistently outperforms strong baselines like protectai/deberta-v3-base-prompt-injection-v2. This work details Sentinel's architecture, its meticulous dataset curation, its training methodology, and a thorough evaluation, highlighting its superior detection capabilities.

