---
layout: default
title: StructEval: Benchmarking LLMs' Capabilities to Generate Structural Outputs
---

# StructEval: Benchmarking LLMs' Capabilities to Generate Structural Outputs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20139" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20139v1</a>
  <a href="https://arxiv.org/pdf/2505.20139.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20139v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20139v1', 'StructEval: Benchmarking LLMs\' Capabilities to Generate Structural Outputs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialin Yang, Dongfu Jiang, Lipeng He, Sherman Siu, Yuxuan Zhang, Disen Liao, Zhuofeng Li, Huaye Zeng, Yiming Jia, Haozhe Wang, Benjamin Schneider, Chi Ruan, Wentao Ma, Zhiheng Lyu, Yifei Wang, Yi Lu, Quy Duc Do, Ziyan Jiang, Ping Nie, Wenhu Chen

**分类**: cs.SE, cs.AI, cs.CL

**发布日期**: 2025-05-26

**备注**: 16 pages, 9 figures, 13 tables

---

## 💡 一句话要点

**提出StructEval以评估大型语言模型生成结构化输出的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `结构化输出` `评估基准` `生成任务` `转换任务` `格式遵循性` `结构正确性` `软件开发`

## 📋 核心要点

1. 现有方法在评估大型语言模型生成结构化输出的能力时缺乏系统性，导致性能差异未被充分揭示。
2. StructEval通过生成任务和转换任务两种方式，系统评估LLMs在多种结构化格式下的输出能力，填补了这一空白。
3. 实验结果表明，当前最先进的模型在生成结构化输出时仍存在显著性能差距，尤其在视觉内容生成方面更为明显。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在软件开发工作流程中的重要性日益增加，它们生成结构化输出的能力变得至关重要。本文介绍了StructEval，一个全面的基准，用于评估LLMs在生成不可渲染（如JSON、YAML、CSV）和可渲染（如HTML、React、SVG）结构化格式方面的能力。与以往的基准不同，StructEval通过生成任务和转换任务两种范式系统地评估结构的准确性。该基准涵盖18种格式和44种任务类型，并引入了格式遵循性和结构正确性的创新指标。实验结果显示，即使是最先进的模型o1-mini的平均得分也仅为75.58，开源替代方案的得分大约低10分。我们发现生成任务比转换任务更具挑战性，而生成正确的视觉内容比生成仅文本结构更困难。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成结构化输出时的评估不足，现有方法未能全面反映模型在不同格式下的性能差异。

**核心思路**：StructEval的核心思路是通过引入生成任务和转换任务，系统性地评估模型在多种结构化格式下的输出能力，确保评估的全面性和准确性。

**技术框架**：StructEval的整体架构包括两个主要模块：生成任务模块和转换任务模块。生成任务模块负责从自然语言提示生成结构化输出，而转换任务模块则负责在不同结构化格式之间进行转换。

**关键创新**：StructEval的主要创新在于引入了格式遵循性和结构正确性的评估指标，能够更全面地反映模型在生成结构化输出时的表现，与现有方法相比具有更高的评估精度。

**关键设计**：在设计中，StructEval涵盖了18种结构化格式和44种任务类型，采用了新的评估指标来衡量模型的格式遵循性和结构正确性，确保评估结果的可靠性。实验中还发现生成任务的难度普遍高于转换任务。

## 📊 实验亮点

实验结果显示，当前最先进的模型o1-mini在生成结构化输出时的平均得分为75.58，开源替代方案的得分低约10分。生成任务的挑战性明显高于转换任务，尤其在生成视觉内容时，模型表现出更大的困难。这些结果揭示了当前模型在结构化输出生成中的性能差距。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、数据处理和自动化文档生成等。通过评估大型语言模型在生成结构化输出方面的能力，StructEval能够帮助开发者选择合适的模型，提高开发效率，推动智能化软件工具的发展。未来，随着模型能力的提升，StructEval也将为更复杂的应用场景提供评估依据。

## 📄 摘要（原文）

> As Large Language Models (LLMs) become integral to software development workflows, their ability to generate structured outputs has become critically important. We introduce StructEval, a comprehensive benchmark for evaluating LLMs' capabilities in producing both non-renderable (JSON, YAML, CSV) and renderable (HTML, React, SVG) structured formats. Unlike prior benchmarks, StructEval systematically evaluates structural fidelity across diverse formats through two paradigms: 1) generation tasks, producing structured output from natural language prompts, and 2) conversion tasks, translating between structured formats. Our benchmark encompasses 18 formats and 44 types of task, with novel metrics for format adherence and structural correctness. Results reveal significant performance gaps, even state-of-the-art models like o1-mini achieve only 75.58 average score, with open-source alternatives lagging approximately 10 points behind. We find generation tasks more challenging than conversion tasks, and producing correct visual content more difficult than generating text-only structures.

