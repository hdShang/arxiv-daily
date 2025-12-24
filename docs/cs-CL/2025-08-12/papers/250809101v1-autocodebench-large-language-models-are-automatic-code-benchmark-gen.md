---
layout: default
title: "AutoCodeBench: Large Language Models are Automatic Code Benchmark Generators"
---

# AutoCodeBench: Large Language Models are Automatic Code Benchmark Generators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09101" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09101v1</a>
  <a href="https://arxiv.org/pdf/2508.09101.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09101v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09101v1', 'AutoCodeBench: Large Language Models are Automatic Code Benchmark Generators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jason Chou, Ao Liu, Yuchi Deng, Zhiying Zeng, Tao Zhang, Haotian Zhu, Jianwei Cai, Yue Mao, Chenchen Zhang, Lingyun Tan, Ziyan Xu, Bohui Zhai, Hengyi Liu, Speed Zhu, Wiggin Zhou, Fengzong Lian

**分类**: cs.CL, cs.SE

**发布日期**: 2025-08-12

**备注**: Homepage: https://autocodebench.github.io/

---

## 💡 一句话要点

**提出AutoCodeBench以解决现有代码生成基准的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `大型语言模型` `自动化基准` `多语言支持` `数据集生成` `机器学习评估` `软件开发`

## 📋 核心要点

1. 现有代码生成基准依赖人工标注，难以扩展，且主要集中在Python，缺乏多语言和多样性。
2. 提出AutoCodeGen方法，通过LLMs自动生成高难度多语言数据集，确保测试用例的正确性和完整性。
3. 在AutoCodeBench上评估了30多种开源和专有LLMs，结果显示即使是最先进的模型也难以应对这些复杂任务。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个领域展现了卓越的能力，其中代码生成成为重点关注的领域。然而，现有的代码生成基准存在显著的局限性，主要依赖人工标注，难以扩展到不同编程语言和问题复杂度。此外，大多数基准主要集中在Python，缺乏多样性和难度。为了解决这些问题，本文提出了AutoCodeGen，一种自动生成高难度多语言代码生成数据集的方法，避免了人工标注的需求。基于此，我们引入了AutoCodeBench，一个包含3920个问题的大规模代码生成基准，旨在评估LLMs在具有挑战性和多样性的多语言任务上的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决现有代码生成基准的局限性，特别是人工标注的高成本和多语言支持不足的问题。

**核心思路**：提出AutoCodeGen，通过大型语言模型自动生成高难度的多语言代码生成数据集，避免了人工干预，同时确保数据的质量和多样性。

**技术框架**：整体流程包括使用LLMs生成测试输入，通过多语言沙箱获取测试输出，并通过逆序问题生成和多重过滤步骤确保数据质量。

**关键创新**：AutoCodeGen的最大创新在于其完全自动化的生成过程，显著提高了数据集的规模和多样性，克服了传统方法的局限。

**关键设计**：在数据生成过程中，采用了多重过滤机制和逆序问题生成策略，以确保生成问题的难度和多样性，同时设计了AutoCodeBench和AutoCodeBench-Lite两个版本以适应不同的评估需求。

## 📊 实验亮点

实验结果表明，超过30种LLMs在AutoCodeBench上表现不佳，尤其是在复杂性和多样性方面，显示出当前模型在处理多语言和高难度任务时的局限性。这一发现强调了AutoCodeBench在推动更具挑战性的代码生成研究中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、教育和自动化测试等。通过提供高质量的多语言代码生成基准，AutoCodeBench可以帮助研究人员和开发者更好地评估和改进代码生成模型，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities across various domains, with code generation emerging as a key area of focus. While numerous benchmarks have been proposed to evaluate their code generation abilities, these benchmarks face several critical limitations. First, they often rely on manual annotations, which are time-consuming and difficult to scale across different programming languages and problem complexities. Second, most existing benchmarks focus primarily on Python, while the few multilingual benchmarks suffer from limited difficulty and uneven language distribution. To address these challenges, we propose AutoCodeGen, an automated method for generating high-difficulty multilingual code generation datasets without manual annotations. AutoCodeGen ensures the correctness and completeness of test cases by generating test inputs with LLMs and obtaining test outputs through a multilingual sandbox, while achieving high data quality through reverse-order problem generation and multiple filtering steps. Using this novel method, we introduce AutoCodeBench, a large-scale code generation benchmark comprising 3,920 problems evenly distributed across 20 programming languages. It is specifically designed to evaluate LLMs on challenging, diverse, and practical multilingual tasks. We evaluate over 30 leading open-source and proprietary LLMs on AutoCodeBench and its simplified version AutoCodeBench-Lite. The results show that even the most advanced LLMs struggle with the complexity, diversity, and multilingual nature of these tasks. Besides, we introduce AutoCodeBench-Complete, specifically designed for base models to assess their few-shot code generation capabilities. We hope the AutoCodeBench series will serve as a valuable resource and inspire the community to focus on more challenging and practical multilingual code generation scenarios.

