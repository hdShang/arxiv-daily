---
layout: default
title: "MMTU: A Massive Multi-Task Table Understanding and Reasoning Benchmark"
---

# MMTU: A Massive Multi-Task Table Understanding and Reasoning Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05587" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05587v3</a>
  <a href="https://arxiv.org/pdf/2506.05587.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05587v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05587v3', 'MMTU: A Massive Multi-Task Table Understanding and Reasoning Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junjie Xing, Yeye He, Mengyu Zhou, Haoyu Dong, Shi Han, Lingjiao Chen, Dongmei Zhang, Surajit Chaudhuri, H. V. Jagadish

**分类**: cs.AI, cs.CL, cs.DB, cs.LG

**发布日期**: 2025-06-05 (更新: 2025-11-25)

**备注**: Accepted at NeurIPS 2025; Code and data available at https://github.com/MMTU-Benchmark/MMTU and https://huggingface.co/datasets/MMTU-benchmark/MMTU

**🔗 代码/项目**: [GITHUB](https://github.com/MMTU-Benchmark/MMTU) | [HUGGINGFACE](https://huggingface.co/datasets/MMTU-benchmark)

---

## 💡 一句话要点

**提出MMTU基准以解决表格理解与推理的评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格理解` `推理评估` `多任务基准` `数据分析` `人工智能` `机器学习` `自然语言处理`

## 📋 核心要点

1. 现有的表格相关任务评估主要集中在NL-to-SQL和表格问答，缺乏对专业用户广泛任务的全面理解。
2. 本文提出MMTU基准，涵盖28,000个问题和25个复杂表格任务，旨在评估模型的表格理解和推理能力。
3. 实验结果显示，当前前沿模型在MMTU上的得分仅为69%和57%，表明在表格理解和推理方面仍有很大改进空间。

## 📝 摘要（中文）

表格及其应用在电子表格、数据库和计算笔记本等重要现实场景中发挥着关键作用，然而现有的基准评估主要集中在NL-to-SQL和表格问答等狭窄任务，缺乏对专业用户面临的广泛实际任务的全面评估。为此，本文提出了MMTU，一个包含超过28,000个问题和25个真实世界表格任务的大规模基准，旨在全面评估模型在理解、推理和操作真实表格方面的能力。研究表明，当前前沿模型在MMTU上的表现仍有显著提升空间，期望该基准推动结构化数据处理和分析基础模型的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有表格理解与推理任务评估不足的问题，尤其是缺乏对专业用户所面临的复杂任务的全面评估。

**核心思路**：通过构建MMTU基准，提供一个包含多种真实世界表格任务的大规模评估平台，以全面测试模型在表格理解、推理和操作方面的能力。

**技术框架**：MMTU基准由28,000个问题组成，涵盖25个任务，任务设计基于计算机科学领域数十年的研究，强调复杂的表格操作。评估流程包括问题生成、模型测试和结果分析等主要模块。

**关键创新**：MMTU的创新在于其广泛的任务覆盖和综合评估能力，填补了现有基准在表格任务评估上的空白，特别是针对专业用户的需求。

**关键设计**：在设计MMTU时，关注任务的多样性和复杂性，确保问题能够有效测试模型的表格理解和推理能力，同时采用标准化的评估指标以便于不同模型间的比较。

## 📊 实验亮点

在MMTU基准的评估中，前沿模型如OpenAI GPT-5和DeepSeek R1的得分分别为69%和57%，显示出在表格理解和推理方面的显著挑战。这一结果强调了当前模型在处理复杂表格任务时的不足，指出了未来改进的方向。

## 🎯 应用场景

MMTU基准的潜在应用领域包括数据分析、数据库管理和智能助手等场景，能够帮助研究人员和开发者更好地理解和提升模型在表格数据处理方面的能力。随着对表格数据需求的增加，该基准将推动相关技术的发展，提升用户在实际应用中的效率和准确性。

## 📄 摘要（原文）

> Tables and table-based use cases play a crucial role in many important real-world applications, such as spreadsheets, databases, and computational notebooks, which traditionally require expert-level users like data engineers, data analysts, and database administrators to operate. Although LLMs have shown remarkable progress in working with tables (e.g., in spreadsheet and database copilot scenarios), comprehensive benchmarking of such capabilities remains limited. In contrast to an extensive and growing list of NLP benchmarks, evaluations of table-related tasks are scarce, and narrowly focus on tasks like NL-to-SQL and Table-QA, overlooking the broader spectrum of real-world tasks that professional users face. This gap limits our understanding and model progress in this important area.
>   In this work, we introduce MMTU, a large-scale benchmark with over 28K questions across 25 real-world table tasks, designed to comprehensively evaluate models ability to understand, reason, and manipulate real tables at the expert-level. These tasks are drawn from decades' worth of computer science research on tabular data, with a focus on complex table tasks faced by professional users. We show that MMTU require a combination of skills -- including table understanding, reasoning, and coding -- that remain challenging for today's frontier models, where even frontier reasoning models like OpenAI GPT-5 and DeepSeek R1 score only around 69\% and 57\% respectively, suggesting significant room for improvement. We highlight key findings in our evaluation using MMTU and hope that this benchmark drives further advances in understanding and developing foundation models for structured data processing and analysis.
>   Our code and data are available at https://github.com/MMTU-Benchmark/MMTU and https://huggingface.co/datasets/MMTU-benchmark/MMTU.

