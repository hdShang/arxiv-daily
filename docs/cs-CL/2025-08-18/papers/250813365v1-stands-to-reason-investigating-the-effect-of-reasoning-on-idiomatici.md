---
layout: default
title: "Stands to Reason: Investigating the Effect of Reasoning on Idiomaticity Detection"
---

# Stands to Reason: Investigating the Effect of Reasoning on Idiomaticity Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13365" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13365v1</a>
  <a href="https://arxiv.org/pdf/2508.13365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13365v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13365v1', 'Stands to Reason: Investigating the Effect of Reasoning on Idiomaticity Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dylan Phelps, Rodrigo Wilkens, Edward Gow-Smith, Thomas Pickard, Maggie Mi, Aline Villavicencio

**分类**: cs.CL

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**探讨推理能力对习语检测的影响**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `习语检测` `推理能力` `大型语言模型` `链式推理` `模型蒸馏` `自然语言处理` `机器学习`

## 📋 核心要点

1. 现有的习语检测方法在理解和消歧义方面存在不足，尤其是对较小模型的推理能力依赖较大。
2. 论文提出通过分析推理能力对习语检测的影响，探索不同规模模型的表现差异。
3. 实验结果显示，较小模型在链式推理下有所提升，但仍未达到较大模型的水平，且提供定义可改善小模型的表现。

## 📝 摘要（中文）

近年来，推理模型的应用提升了大型语言模型（LLMs）在许多涉及逻辑步骤的任务中的表现。习语检测作为一种语言任务，能够从这种框架中受益。本文探讨了LLMs中的推理能力如何影响习语检测的性能，并考察了模型规模的影响。研究发现，推理的效果比预期的要小且变化多端。较小模型在链式推理下性能有所提升，但未达到基础模型水平，而较大模型则表现出适度的改进。深入分析显示，较大模型对习语的理解较好，而较小模型常常无法输出实际含义。为此，本文还尝试在小模型的提示中提供定义，结果在某些情况下提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决习语检测中推理能力对模型性能的影响，现有方法在小模型上表现不佳，难以准确理解习语含义。

**核心思路**：通过分析不同规模的LLMs在习语检测任务中的推理能力，探讨如何提升小模型的表现，尤其是通过链式推理和定义提示。

**技术框架**：研究使用了一系列DeepSeek-R1蒸馏模型，参数从1.5B到70B，评估其在四个习语检测数据集上的表现，比较不同模型的推理能力和习语理解。

**关键创新**：本研究的创新在于系统性地评估推理能力对习语检测的影响，发现推理效果在不同模型间的差异，尤其是小模型在推理能力上的局限性。

**关键设计**：实验中设置了不同规模的模型，采用链式推理方法，并在小模型的提示中加入习语定义，以观察其对性能的影响。

## 📊 实验亮点

实验结果表明，较小模型在链式推理下性能有所提升，但未达到基础模型的水平。较大模型（14B、32B和70B）在习语理解上表现良好，能够准确生成表达的定义。提供定义的提示在某些情况下显著改善了小模型的表现。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的习语检测、机器翻译和对话系统等。通过提升模型对习语的理解能力，可以在实际应用中提高语言模型的准确性和流畅性，进而改善用户体验。

## 📄 摘要（原文）

> The recent trend towards utilisation of reasoning models has improved the performance of Large Language Models (LLMs) across many tasks which involve logical steps. One linguistic task that could benefit from this framing is idiomaticity detection, as a potentially idiomatic expression must first be understood before it can be disambiguated and serves as a basis for reasoning. In this paper, we explore how reasoning capabilities in LLMs affect idiomaticity detection performance and examine the effect of model size. We evaluate, as open source representative models, the suite of DeepSeek-R1 distillation models ranging from 1.5B to 70B parameters across four idiomaticity detection datasets. We find the effect of reasoning to be smaller and more varied than expected. For smaller models, producing chain-of-thought (CoT) reasoning increases performance from Math-tuned intermediate models, but not to the levels of the base models, whereas larger models (14B, 32B, and 70B) show modest improvements. Our in-depth analyses reveal that larger models demonstrate good understanding of idiomaticity, successfully producing accurate definitions of expressions, while smaller models often fail to output the actual meaning. For this reason, we also experiment with providing definitions in the prompts of smaller models, which we show can improve performance in some cases.

