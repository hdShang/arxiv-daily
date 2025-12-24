---
layout: default
title: "Reinforcing Code Generation: Improving Text-to-SQL with Execution-Based Learning"
---

# Reinforcing Code Generation: Improving Text-to-SQL with Execution-Based Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06093" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06093v1</a>
  <a href="https://arxiv.org/pdf/2506.06093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06093v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06093v1', 'Reinforcing Code Generation: Improving Text-to-SQL with Execution-Based Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Atharv Kulkarni, Vivek Srikumar

**分类**: cs.CL

**发布日期**: 2025-06-06

**备注**: Under review at EMNLP 2025

---

## 💡 一句话要点

**通过执行反馈强化代码生成以提升文本到SQL的转换能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `文本到SQL` `强化学习` `执行反馈` `自然语言处理` `模型优化`

## 📋 核心要点

1. 现有方法主要依赖于监督微调，缺乏与实际数据库交互的能力，导致生成的SQL查询准确性不足。
2. 论文提出通过强化学习框架，利用执行反馈来调整模型，增强其生成SQL查询的能力。
3. 实验结果显示，RL调优显著提高了SQL代码的准确率和降低了错误率，接近更大模型的性能水平。

## 📝 摘要（中文）

本研究探讨了使用大型语言模型（LLM）进行代码生成的问题，重点是从自然语言问题生成SQL查询。我们提出了一种通过与数据库引擎交互来调整模型的方法，而不是依赖于文本-代码对的监督微调。我们将此问题框定为强化学习问题，模型通过环境反馈获得执行基础的反馈，反馈以标量奖励的形式呈现，惩罚执行失败并在查询返回正确答案时给予正值。通过在Group Relative Policy Optimization (GRPO)框架下使用这些奖励，我们在一个表格推理基准上测试和评估了我们的发现。结果表明，仅通过问题-答案对的弱监督，RL调优将模型生成的SQL代码的准确率从31.49提升至49.83，同时错误率从25.43%降低至14.71%。这一改进使模型的性能几乎与更大规模的SQLCoder-70B模型相当。我们的工作展示了使用执行反馈来提升LLM符号推理能力的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有文本到SQL生成方法中，依赖监督微调导致的准确性不足的问题。现有方法未能有效利用数据库执行反馈，限制了模型的学习能力。

**核心思路**：论文提出通过强化学习的方法，利用与数据库的交互来获取执行反馈，以此来优化模型的SQL生成能力。这种设计能够让模型在实际执行中学习，从而提高生成代码的准确性。

**技术框架**：整体架构包括模型与数据库引擎的交互，模型生成SQL查询后，数据库执行该查询并返回结果，模型根据结果获得奖励。使用Group Relative Policy Optimization (GRPO)框架来处理这些奖励。

**关键创新**：最重要的技术创新在于将执行反馈引入到代码生成过程中，使得模型能够在实际执行中学习，而不仅仅依赖于静态的文本-代码对。这一方法显著提升了模型的符号推理能力。

**关键设计**：在参数设置上，使用了弱监督的方式，仅依赖问题-答案对进行初步训练。损失函数设计上，结合了执行反馈的奖励机制，确保模型在生成SQL时能够最大化正确性。

## 📊 实验亮点

实验结果表明，使用RL调优后，模型生成的SQL代码准确率从31.49提升至49.83，错误率从25.43%降低至14.71%。这一改进使得模型的性能接近更大规模的SQLCoder-70B模型，展示了执行反馈的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括数据库查询生成、智能助手、自然语言处理等。通过提升模型的SQL生成能力，可以在数据分析、商业智能等领域提供更高效的解决方案，未来可能对自动化数据处理和决策支持系统产生深远影响。

## 📄 摘要（原文）

> In this work, we study the problem of code generation with a large language model (LLM), with a focus on generating SQL queries from natural language questions. We ask: Instead of using supervised fine tuning with text-code pairs, can we tune a model by having it interact with a database engine? We frame this problem as a reinforcement learning problem where the model receives execution-based feedback from the environment in the form of scalar rewards. These rewards penalize execution failures and assign positive values when a query returns a correct answer. We use the rewards within the Group Relative Policy Optimization (GRPO) framework. We use a tabular reasoning benchmark to test and evaluate our findings. We find that with only weak supervision in the form of question-answer pairs, RL-tuning improves the accuracy of model generated SQL code from 31.49 to 49.83 while reducing error percentage from 25.43% to 14.71%. This improvement allowed the model nearly match the performance performance to the larger SQLCoder-70B model. Our work demonstrates the potential of using execution-based feedback to improve symbolic reasoning capabilities of LLMs.

