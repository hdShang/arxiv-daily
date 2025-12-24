---
layout: default
title: SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas
---

# SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14615" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14615v2</a>
  <a href="https://arxiv.org/pdf/2505.14615.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14615v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14615v2', 'SATBench: Benchmarking LLMs\' Logical Reasoning via Automated Puzzle Generation from SAT Formulas')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anjiang Wei, Yuheng Wu, Yingjia Wan, Tarun Suresh, Huanmi Tan, Zhanke Zhou, Sanmi Koyejo, Ke Wang, Alex Aiken

**分类**: cs.AI, cs.CL, cs.LG, cs.LO

**发布日期**: 2025-05-20 (更新: 2025-09-22)

**🔗 代码/项目**: [GITHUB](https://github.com/Anjiang-Wei/SATBench)

---

## 💡 一句话要点

**提出SATBench以评估大型语言模型的逻辑推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逻辑推理` `大型语言模型` `布尔可满足性` `自动生成` `基准测试` `SAT问题` `模型评估`

## 📋 核心要点

1. 现有方法主要集中在基于推理规则的推理，难以有效处理搜索型逻辑问题。
2. 论文提出SATBench，通过自动生成逻辑难题来评估LLMs的逻辑推理能力，利用SAT问题的搜索特性。
3. 实验结果表明，最强模型在困难问题上的表现仅为65.0%准确率，显示出LLMs在逻辑推理中的局限性。

## 📝 摘要（中文）

我们介绍了SATBench，这是一个通过从布尔可满足性（SAT）问题生成逻辑难题来评估大型语言模型（LLMs）逻辑推理能力的基准测试。与以往关注基于推理规则的推理方法不同，我们的方法利用SAT问题的搜索特性，目标是找到满足特定逻辑约束的解决方案。SATBench中的每个实例均由SAT公式生成，并通过LLMs转换为难题。生成过程完全自动化，并可通过调整子句数量来改变难度。所有2100个难题通过LLM和求解器的验证检查，并在部分样本上进行了人工验证。实验结果显示，即使是最强的模型o4-mini在困难的UNSAT问题上也仅达到65.0%的准确率，接近50%的随机基线。我们的错误分析揭示了系统性失败，如可满足性偏差、上下文不一致和条件遗漏，突显了当前LLMs在基于搜索的逻辑推理中的局限性。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有大型语言模型在逻辑推理能力评估中的不足，尤其是对搜索型逻辑问题的处理能力。现有方法多依赖于推理规则，缺乏对SAT问题的有效评估。

**核心思路**：论文的核心思路是通过自动生成逻辑难题来评估LLMs的逻辑推理能力，利用SAT问题的特性，寻找满足特定逻辑约束的解决方案。这种方法不仅提高了评估的自动化程度，还允许根据需求调整难度。

**技术框架**：整体架构包括三个主要模块：首先，从SAT公式生成逻辑难题；其次，利用LLMs将生成的公式转化为可解的难题；最后，通过LLM和求解器进行一致性检查，确保生成难题的有效性。

**关键创新**：最重要的技术创新在于将SAT问题的搜索特性与LLMs结合，形成了一种新的评估机制。这与以往基于推理规则的方法本质上不同，提供了更全面的逻辑推理能力评估。

**关键设计**：在生成过程中，关键参数包括子句数量的调整，以控制难度。此外，验证过程结合了LLM和求解器的双重检查，确保了生成难题的准确性和一致性。实验中还进行了人工验证，以提高结果的可靠性。

## 📊 实验亮点

实验结果显示，最强模型o4-mini在困难的UNSAT问题上仅达到65.0%的准确率，接近50%的随机基线。这一结果揭示了当前LLMs在处理复杂逻辑推理任务时的局限性，尤其是在系统性错误方面。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能问答系统和自动推理工具等。通过评估和提升LLMs的逻辑推理能力，可以促进更智能的对话系统和决策支持工具的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce SATBench, a benchmark for evaluating the logical reasoning capabilities of large language models (LLMs) through logical puzzles derived from Boolean satisfiability (SAT) problems. Unlike prior work that focuses on inference rule-based reasoning, which often involves deducing conclusions from a set of premises, our approach leverages the search-based nature of SAT problems, where the objective is to find a solution that fulfills a specified set of logical constraints. Each instance in SATBench is generated from a SAT formula, then translated into a puzzle using LLMs. The generation process is fully automated and allows for adjustable difficulty by varying the number of clauses. All 2100 puzzles are validated through both LLM-based and solver-based consistency checks, with human validation on a subset. Experimental results show that even the strongest model, o4-mini, achieves only 65.0% accuracy on hard UNSAT problems, close to the random baseline of 50%. Our error analysis reveals systematic failures such as satisfiability bias, context inconsistency, and condition omission, highlighting limitations of current LLMs in search-based logical reasoning. Our code and data are publicly available at https://github.com/Anjiang-Wei/SATBench

