---
layout: default
title: Identifying Legal Holdings with LLMs: A Systematic Study of Performance, Scale, and Memorization
---

# Identifying Legal Holdings with LLMs: A Systematic Study of Performance, Scale, and Memorization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02172" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02172v3</a>
  <a href="https://arxiv.org/pdf/2505.02172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02172v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02172v3', 'Identifying Legal Holdings with LLMs: A Systematic Study of Performance, Scale, and Memorization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuck Arvin

**分类**: cs.CL

**发布日期**: 2025-05-04 (更新: 2025-05-24)

**备注**: Presented as a short paper at International Conference on Artificial Intelligence and Law 2025 (Chicago, IL)

---

## 💡 一句话要点

**通过LLMs识别法律判决，提升法律分析的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `法律分析` `性能评估` `引用匿名化` `宏观F1分数` `自动化法律工具` `案例识别`

## 📋 核心要点

1. 现有的法律分析方法在处理复杂法律文本时存在准确性不足和效率低下的问题。
2. 本研究提出了一种基于大型语言模型的评估方法，通过实验验证模型在法律判决识别任务中的表现。
3. 实验结果表明，模型规模与性能呈正相关，且在引用匿名化测试下仍能保持高水平的准确性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）能力的不断提升，评估其在既定基准上的表现变得至关重要。本研究通过一系列实验评估了现代LLMs（参数范围从30亿到900亿以上）在CaseHOLD法律基准数据集上的表现。实验结果显示，模型规模的增加能够显著提升任务性能，GPT4o和AmazonNovaPro等更强大的模型分别达到了0.744和0.720的宏观F1分数。这些分数与该数据集上已发布的最佳结果相当，并且不需要任何复杂的模型训练、微调或少量提示。为了确保这些强结果不是由于对训练数据中司法意见的记忆，我们开发并利用了一种新的引用匿名化测试，确保案例名称和引用是虚构的，同时保持语义意义。在这种条件下，模型仍保持强劲表现（宏观F1为0.728），表明其性能并非源于机械记忆。这些发现展示了LLMs在法律任务中的潜力与当前局限性，对自动化法律分析和法律基准的开发与测量具有重要意义。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在法律判决识别任务中的表现评估问题。现有方法往往依赖于复杂的训练过程，难以直接比较模型性能。

**核心思路**：通过设计一系列实验，评估不同规模的LLMs在法律基准数据集CaseHOLD上的表现，特别关注模型规模对性能的影响。

**技术框架**：整体架构包括数据集准备、模型选择、性能评估和引用匿名化测试四个主要模块。数据集用于训练和测试，模型则包括从30亿到900亿参数的多种LLMs。

**关键创新**：引入了引用匿名化测试，确保模型的高性能不是由于对训练数据的记忆，而是基于对法律文本的理解和推理能力。

**关键设计**：实验中使用的模型包括GPT4o和AmazonNovaPro，采用标准的宏观F1分数作为性能评估指标，确保结果的可比性和可靠性。

## 📊 实验亮点

实验结果显示，GPT4o和AmazonNovaPro在CaseHOLD数据集上的宏观F1分数分别达到0.744和0.720，表现出色。即使在引用匿名化测试下，模型仍能保持0.728的宏观F1分数，表明其性能并非源于简单的记忆，而是具备较强的理解能力。

## 🎯 应用场景

该研究的成果可广泛应用于法律领域的自动化分析工具，帮助法律从业者更高效地识别和分析判决内容。未来，随着LLMs技术的进一步发展，这些工具有望提升法律服务的质量和可及性。

## 📄 摘要（原文）

> As large language models (LLMs) continue to advance in capabilities, it is essential to assess how they perform on established benchmarks. In this study, we present a suite of experiments to assess the performance of modern LLMs (ranging from 3B to 90B+ parameters) on CaseHOLD, a legal benchmark dataset for identifying case holdings. Our experiments demonstrate scaling effects - performance on this task improves with model size, with more capable models like GPT4o and AmazonNovaPro achieving macro F1 scores of 0.744 and 0.720 respectively. These scores are competitive with the best published results on this dataset, and do not require any technically sophisticated model training, fine-tuning or few-shot prompting. To ensure that these strong results are not due to memorization of judicial opinions contained in the training data, we develop and utilize a novel citation anonymization test that preserves semantic meaning while ensuring case names and citations are fictitious. Models maintain strong performance under these conditions (macro F1 of 0.728), suggesting the performance is not due to rote memorization. These findings demonstrate both the promise and current limitations of LLMs for legal tasks with important implications for the development and measurement of automated legal analytics and legal benchmarks.

