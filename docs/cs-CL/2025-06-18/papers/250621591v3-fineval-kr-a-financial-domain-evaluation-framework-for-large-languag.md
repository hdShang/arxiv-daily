---
layout: default
title: "FinEval-KR: A Financial Domain Evaluation Framework for Large Language Models' Knowledge and Reasoning"
---

# FinEval-KR: A Financial Domain Evaluation Framework for Large Language Models' Knowledge and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21591" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21591v3</a>
  <a href="https://arxiv.org/pdf/2506.21591.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21591v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21591v3', 'FinEval-KR: A Financial Domain Evaluation Framework for Large Language Models\' Knowledge and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaoyu Dou, Yutian Shen, Mofan Chen, Zixuan Wang, Jiajie Xu, Qi Guo, Kailai Shao, Chao Chen, Haixiang Hu, Haibo Shi, Min Min, Liwen Zhang

**分类**: cs.CL

**发布日期**: 2025-06-18 (更新: 2025-11-06)

**备注**: Accepted by FinNLP@EMNLP2025

---

## 💡 一句话要点

**提出FinEval-KR框架以解决金融领域LLM评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融推理` `大型语言模型` `评估框架` `知识评分` `推理评分` `认知科学` `布鲁姆分类法` `开放数据集`

## 📋 核心要点

1. 现有评估基准未能有效解耦LLMs的知识与推理能力，且缺乏对失败原因的深入分析。
2. 提出FinEval-KR框架，通过独立的知识评分和推理评分来量化LLMs的能力，并引入认知评分以分析不同层次的推理能力。
3. 实验结果显示，推理能力和高阶认知能力是影响推理准确性的关键因素，且专门的金融LLMs在多个指标上普遍落后于顶尖的通用模型。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂金融推理任务中展现出显著潜力，但在需要领域知识和复杂推理的任务中面临挑战。现有评估基准往往未能将这些能力指标与单一任务表现解耦，并缺乏对任务失败的根本原因分析。为此，本文提出了FinEval-KR，一个新颖的评估框架，旨在独立量化LLMs的知识和推理能力，提出了知识评分和推理评分的独特指标。此外，基于布鲁姆分类法，我们进一步提出了认知评分，以分析不同认知水平的推理任务能力。我们还发布了一个涵盖22个子领域的中文金融推理数据集，以支持可重复研究和金融推理的进一步发展。实验结果表明，LLM的推理能力和高阶认知能力是影响推理准确性的核心因素。

## 🔬 方法详解

**问题定义**：本文旨在解决现有评估方法未能有效区分LLMs的知识与推理能力的问题，尤其是在复杂金融推理任务中的应用。现有方法往往无法深入分析任务失败的根本原因，导致评估结果的局限性。

**核心思路**：论文提出的FinEval-KR框架通过独立的知识评分和推理评分，旨在量化LLMs在金融领域的知识与推理能力。这种设计灵感来源于认知科学，特别是布鲁姆分类法，能够更全面地分析模型在不同认知层次上的表现。

**技术框架**：FinEval-KR框架包含多个模块，首先是知识评分模块，评估模型对金融知识的掌握；其次是推理评分模块，评估模型在复杂推理任务中的表现；最后是认知评分模块，基于布鲁姆分类法分析模型的高阶认知能力。

**关键创新**：最重要的技术创新在于将知识与推理能力独立评估，并引入认知评分的概念。这与现有方法的本质区别在于，现有方法通常只关注单一任务的表现，而忽视了能力的多维度分析。

**关键设计**：在关键设计方面，论文详细描述了知识评分和推理评分的计算方法，采用了特定的损失函数和评估标准，以确保评估结果的准确性和可靠性。

## 📊 实验亮点

实验结果表明，LLMs的推理能力和高阶认知能力是影响推理准确性的核心因素。尽管一些顶尖模型在性能上表现良好，但在知识应用方面仍面临瓶颈。此外，专门的金融LLMs在多个指标上普遍落后于顶尖的通用模型，显示出该领域的进一步研究需求。

## 🎯 应用场景

该研究的潜在应用领域包括金融科技、智能投顾和风险管理等。通过提供一个系统化的评估框架，FinEval-KR能够帮助研究人员和从业者更好地理解和提升LLMs在金融领域的应用能力，推动金融智能化的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) demonstrate significant potential but face challenges in complex financial reasoning tasks requiring both domain knowledge and sophisticated reasoning. Current evaluation benchmarks often fall short by not decoupling these capabilities indicators from single task performance and lack root cause analysis for task failure. To address this, we introduce FinEval-KR, a novel evaluation framework for decoupling and quantifying LLMs' knowledge and reasoning abilities independently, proposing distinct knowledge score and reasoning score metrics. Inspired by cognitive science, we further propose a cognitive score based on Bloom's taxonomy to analyze capabilities in reasoning tasks across different cognitive levels. We also release a new open-source Chinese financial reasoning dataset covering 22 subfields to support reproducible research and further advancements in financial reasoning. Our experimental results reveal that LLM reasoning ability and higher-order cognitive ability are the core factors influencing reasoning accuracy. We also specifically find that even top models still face a bottleneck with knowledge application. Furthermore, our analysis shows that specialized financial LLMs generally lag behind the top general large models across multiple metrics.

