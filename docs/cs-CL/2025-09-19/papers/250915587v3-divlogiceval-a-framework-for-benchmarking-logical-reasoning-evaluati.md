---
layout: default
title: "DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models"
---

# DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15587" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15587v3</a>
  <a href="https://arxiv.org/pdf/2509.15587.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15587v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15587v3', 'DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tsz Ting Chung, Lemao Liu, Mo Yu, Dit-Yan Yeung

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-19 (更新: 2025-09-26)

**备注**: Accepted by EMNLP 2025. Project Page: https://ttchungc.github.io/projects/divlogiceval/

---

## 💡 一句话要点

**DivLogicEval：用于评估大语言模型逻辑推理能力的新基准框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `逻辑推理` `基准测试` `自然语言处理` `评估指标`

## 📋 核心要点

1. 现有逻辑推理基准存在语言多样性不足和分布偏差问题，导致对大语言模型的逻辑推理能力评估不准确。
2. 提出DivLogicEval基准，包含多种陈述的自然语句，并设计新的评估指标以减轻偏差和随机性的影响。
3. 实验表明，DivLogicEval能有效评估逻辑推理能力，并比较了不同大语言模型在该基准上的性能表现。

## 📝 摘要（中文）

本文提出了一种新的经典逻辑基准DivLogicEval，用于评估大语言模型(LLMs)的逻辑推理能力。现有基准可能混淆多种推理技能，从而对逻辑推理技能的评估不准确。同时，现有的逻辑推理基准在语言多样性方面存在局限性，并且它们的分布偏离了理想逻辑推理基准的分布，这可能导致有偏差的评估结果。DivLogicEval由以违反直觉的方式组成的自然语句构成，包含多种陈述。为了确保更可靠的评估，本文还引入了一种新的评估指标，以减轻LLM中固有的偏差和随机性的影响。实验结果表明，DivLogicEval中的问题需要一定程度的逻辑推理才能回答，并比较了不同流行的LLM在进行逻辑推理方面的性能。

## 🔬 方法详解

**问题定义**：现有的大语言模型逻辑推理能力评估基准存在以下痛点：一是混杂了多种推理技能，无法单独评估逻辑推理能力；二是语言多样性不足，无法覆盖真实场景；三是数据分布存在偏差，评估结果可能不准确。因此，需要一个更纯粹、更具代表性的逻辑推理评估基准。

**核心思路**：本文的核心思路是构建一个包含多种陈述的自然语句数据集，这些语句以违反直觉的方式组合，从而更有效地考察模型的逻辑推理能力。同时，设计一种新的评估指标，以减轻模型中固有的偏差和随机性对评估结果的影响。

**技术框架**：DivLogicEval框架主要包含以下几个部分：1) 数据集构建：收集包含多种陈述的自然语句，并以违反直觉的方式组合；2) 问题生成：基于构建的数据集生成逻辑推理问题；3) 模型评估：使用大语言模型回答问题，并使用新的评估指标评估模型的逻辑推理能力。

**关键创新**：本文的关键创新在于：1) 提出了一个新的逻辑推理评估基准DivLogicEval，该基准更纯粹、更具代表性；2) 设计了一种新的评估指标，可以减轻模型偏差和随机性对评估结果的影响。与现有方法相比，DivLogicEval能够更准确地评估大语言模型的逻辑推理能力。

**关键设计**：数据集构建方面，需要仔细选择和组合语句，以确保问题的难度和区分度。评估指标方面，需要考虑如何量化模型的逻辑推理能力，并减轻偏差和随机性的影响。具体的参数设置、损失函数和网络结构等技术细节未在摘要中提及，属于未知信息。

## 📊 实验亮点

实验结果表明，DivLogicEval能够有效评估大语言模型的逻辑推理能力，并揭示了不同模型在逻辑推理方面的差异。具体的性能数据、对比基线和提升幅度等信息未在摘要中提及，属于未知信息。

## 🎯 应用场景

该研究成果可应用于大语言模型的评测与改进，帮助研究人员更准确地评估模型的逻辑推理能力，并指导模型的设计和训练。此外，该基准也可用于评估其他人工智能系统的逻辑推理能力，推动人工智能技术的发展。

## 📄 摘要（原文）

> Logic reasoning in natural language has been recognized as an important measure of human intelligence for Large Language Models (LLMs). Popular benchmarks may entangle multiple reasoning skills and thus provide unfaithful evaluations on the logic reasoning skill. Meanwhile, existing logic reasoning benchmarks are limited in language diversity and their distributions are deviated from the distribution of an ideal logic reasoning benchmark, which may lead to biased evaluation results. This paper thereby proposes a new classical logic benchmark DivLogicEval, consisting of natural sentences composed of diverse statements in a counterintuitive way. To ensure a more reliable evaluation, we also introduce a new evaluation metric that mitigates the influence of bias and randomness inherent in LLMs. Through experiments, we demonstrate the extent to which logical reasoning is required to answer the questions in DivLogicEval and compare the performance of different popular LLMs in conducting logical reasoning.

