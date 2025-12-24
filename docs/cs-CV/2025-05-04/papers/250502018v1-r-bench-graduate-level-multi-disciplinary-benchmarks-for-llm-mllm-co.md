---
layout: default
title: "R-Bench: Graduate-level Multi-disciplinary Benchmarks for LLM & MLLM Complex Reasoning Evaluation"
---

# R-Bench: Graduate-level Multi-disciplinary Benchmarks for LLM & MLLM Complex Reasoning Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02018" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02018v1</a>
  <a href="https://arxiv.org/pdf/2505.02018.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02018v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02018v1', 'R-Bench: Graduate-level Multi-disciplinary Benchmarks for LLM & MLLM Complex Reasoning Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Meng-Hao Guo, Jiajun Xu, Yi Zhang, Jiaxi Song, Haoyang Peng, Yi-Xuan Deng, Xinzhi Dong, Kiyohiro Nakayama, Zhengyang Geng, Chen Wang, Bolin Ni, Guo-Wei Yang, Yongming Rao, Houwen Peng, Han Hu, Gordon Wetzstein, Shi-min Hu

**分类**: cs.CV

**发布日期**: 2025-05-04

**备注**: 18pages

---

## 💡 一句话要点

**提出R-Bench以评估多学科复杂推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `复杂推理` `多学科评估` `多模态学习` `语言模型` `基准测试`

## 📋 核心要点

1. 现有推理基准无法有效评估复杂现实问题所需的细致推理能力，尤其是在多学科和多模态背景下。
2. 本文提出R-Bench基准，涵盖多学科问题，旨在全面评估语言和多模态模型的推理能力。
3. 实验结果显示，当前先进模型在复杂推理任务上表现不佳，尤其是多模态推理，OpenAI o1的准确率仅为53.2%。

## 📝 摘要（中文）

推理是智能的基石，使得现有知识得以综合以解决复杂问题。尽管已有显著进展，现有推理基准往往无法严格评估复杂现实问题解决所需的细致推理能力，尤其是在多学科和多模态背景下。本文提出了一种研究生级别的多学科基准R-Bench，用于评估语言和多模态模型的推理能力。R-Bench涵盖了1,094个问题，涉及108个学科用于语言模型评估，以及665个问题，涉及83个学科用于多模态模型测试，支持中英文评估。这些问题经过精心策划，以确保严格的难度校准、学科平衡和跨语言对齐，使评估成为奥林匹克级别的多学科基准。实验结果表明，先进模型在复杂推理，尤其是多模态推理方面表现不佳，甚至表现最佳的OpenAI o1在多模态评估中仅达到53.2%的准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推理基准无法有效评估复杂推理能力的问题，尤其是在多学科和多模态背景下的应用场景。现有方法在难度和学科覆盖上存在不足，无法满足真实世界的需求。

**核心思路**：论文提出的R-Bench基准通过精心策划的多学科问题，旨在全面评估语言和多模态模型的推理能力，确保评估的严谨性和有效性。

**技术框架**：R-Bench的整体架构包括问题设计、难度校准和跨语言对齐等多个模块，确保评估的全面性和科学性。问题涵盖多个学科，支持中英文评估，适用于不同类型的模型。

**关键创新**：R-Bench的主要创新在于其多学科和多模态的综合评估能力，填补了现有基准在复杂推理评估中的空白，提供了更高标准的评估框架。

**关键设计**：在设计过程中，问题的难度、学科平衡和跨语言对齐是关键参数，确保了评估的严谨性和有效性。问题的选择经过严格筛选，以保证其代表性和挑战性。

## 📊 实验亮点

实验结果显示，尽管使用了当前最先进的模型，如OpenAI o1和GPT-4o，但在多模态推理任务中，模型的表现仍然不尽如人意，OpenAI o1仅获得53.2%的准确率，表明复杂推理能力的提升仍然是一个重要挑战。

## 🎯 应用场景

R-Bench基准的潜在应用领域包括教育、人工智能模型评估和多模态学习等。通过提供一个全面的评估框架，研究者和开发者可以更好地理解和提升模型在复杂推理任务中的表现，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Reasoning stands as a cornerstone of intelligence, enabling the synthesis of existing knowledge to solve complex problems. Despite remarkable progress, existing reasoning benchmarks often fail to rigorously evaluate the nuanced reasoning capabilities required for complex, real-world problemsolving, particularly in multi-disciplinary and multimodal contexts. In this paper, we introduce a graduate-level, multi-disciplinary, EnglishChinese benchmark, dubbed as Reasoning Bench (R-Bench), for assessing the reasoning capability of both language and multimodal models. RBench spans 1,094 questions across 108 subjects for language model evaluation and 665 questions across 83 subjects for multimodal model testing in both English and Chinese. These questions are meticulously curated to ensure rigorous difficulty calibration, subject balance, and crosslinguistic alignment, enabling the assessment to be an Olympiad-level multi-disciplinary benchmark. We evaluate widely used models, including OpenAI o1, GPT-4o, DeepSeek-R1, etc. Experimental results indicate that advanced models perform poorly on complex reasoning, especially multimodal reasoning. Even the top-performing model OpenAI o1 achieves only 53.2% accuracy on our multimodal evaluation. Data and code are made publicly available at here.

