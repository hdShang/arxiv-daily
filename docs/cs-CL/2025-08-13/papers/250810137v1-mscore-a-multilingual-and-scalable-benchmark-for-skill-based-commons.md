---
layout: default
title: "mSCoRe: a $M$ultilingual and Scalable Benchmark for $S$kill-based $Co$mmonsense $Re$asoning"
---

# mSCoRe: a $M$ultilingual and Scalable Benchmark for $S$kill-based $Co$mmonsense $Re$asoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10137" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10137v1</a>
  <a href="https://arxiv.org/pdf/2508.10137.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10137v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10137v1', 'mSCoRe: a $M$ultilingual and Scalable Benchmark for $S$kill-based $Co$mmonsense $Re$asoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nghia Trung Ngo, Franck Dernoncourt, Thien Huu Nguyen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出mSCoRe以解决多语言常识推理的评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言推理` `常识推理` `大型语言模型` `推理技能` `数据合成` `复杂性评估` `跨文化交流`

## 📋 核心要点

1. 现有的推理增强模型在多语言常识推理中面临评估不足和能力局限的问题，尤其在文化和语言的细微差别上。
2. 本文提出的mSCoRe基准通过新的推理技能分类法、数据合成管道和复杂性缩放框架，系统性地评估LLM的推理能力。
3. 实验结果显示，mSCoRe对当前的LLM模型仍具有显著挑战性，尤其是在高复杂性任务中，揭示了模型的局限性。

## 📝 摘要（中文）

近年来，推理增强的大型语言模型（LLMs）在复杂推理任务中展现出显著能力。然而，关于它们如何利用不同人类推理技能的机制仍然研究不足，尤其是在涉及不同语言和文化的多语言常识推理方面。为了解决这一问题，本文提出了一个多语言和可扩展的基准测试mSCoRe。该基准包括三个关键组件，旨在系统评估LLM的推理能力：1）一种新的推理技能分类法，便于对模型推理过程进行细致分析；2）专门为常识推理评估设计的强大数据合成管道；3）允许任务难度随LLM能力的未来提升动态扩展的复杂性缩放框架。对八种不同规模和训练方法的最先进LLM进行的广泛实验表明，mSCoRe对当前模型仍然具有显著挑战性，尤其是在更高复杂性水平下。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言常识推理的评估问题，现有方法在处理不同文化和语言的细微差别时存在不足，导致推理能力的评估不够全面。

**核心思路**：论文提出的mSCoRe基准通过引入新的推理技能分类法和复杂性缩放框架，旨在系统性地评估和分析LLM的推理过程，帮助识别其在多语言环境下的局限性。

**技术框架**：mSCoRe的整体架构包括三个主要模块：1）推理技能分类法，提供细致的推理过程分析；2）数据合成管道，生成适用于常识推理的评估数据；3）复杂性缩放框架，动态调整任务难度以适应LLM能力的提升。

**关键创新**：mSCoRe的最大创新在于其推理技能的细分和复杂性动态调整机制，这与现有方法的静态评估方式形成鲜明对比，能够更全面地反映模型的推理能力。

**关键设计**：在设计中，推理技能分类法采用了多层次的分类标准，数据合成管道则利用了多样化的语料库，确保生成数据的多样性和代表性，复杂性缩放框架则通过参数设置实现任务难度的灵活调整。

## 📊 实验亮点

实验结果表明，mSCoRe对八种最先进的LLM模型进行了评估，尤其在高复杂性任务中，模型的表现显著低于预期，揭示了其在多语言和文化常识推理方面的局限性。这一发现为未来的研究指明了方向，强调了提升多语言常识推理能力的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能助手和跨文化交流等。通过提供更准确的多语言常识推理评估，mSCoRe能够帮助改进语言模型在实际应用中的表现，促进人机交互的自然性和有效性。未来，随着模型能力的提升，mSCoRe也将为进一步的研究提供基础。

## 📄 摘要（原文）

> Recent advancements in reasoning-reinforced Large Language Models (LLMs) have shown remarkable capabilities in complex reasoning tasks. However, the mechanism underlying their utilization of different human reasoning skills remains poorly investigated, especially for multilingual commonsense reasoning that involves everyday knowledge across different languages and cultures. To address this gap, we propose a \textbf{M}ultilingual and Scalable Benchmark for \textbf{S}kill-based \textbf{Co}mmonsense \textbf{Re}asoning (\textbf{mSCoRe}). Our benchmark incorporates three key components that are designed to systematically evaluate LLM's reasoning capabilities, including: (1) a novel taxonomy of reasoning skills that enables fine-grained analysis of models' reasoning processes, (2) a robust data synthesis pipeline tailored specifically for commonsense reasoning evaluation, and (3) a complexity scaling framework allowing task difficulty to scale dynamically alongside future improvements in LLM abilities. Extensive experiments on eights state-of-the-art LLMs of varying sizes and training approaches demonstrate that \textbf{mSCoRe} remains significantly challenging for current models, particularly at higher complexity levels. Our results reveal the limitations of such reasoning-reinforced models when confronted with nuanced multilingual general and cultural commonsense. We further provide detailed analysis on the models' reasoning processes, suggesting future directions for improving multilingual commonsense reasoning capabilities.

