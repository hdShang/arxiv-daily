---
layout: default
title: Model-First Reasoning LLM Agents: Reducing Hallucinations through Explicit Problem Modeling
---

# Model-First Reasoning LLM Agents: Reducing Hallucinations through Explicit Problem Modeling

**arXiv**: [2512.14474v1](https://arxiv.org/abs/2512.14474) | [PDF](https://arxiv.org/pdf/2512.14474.pdf)

**作者**: Annu Rana, Gaurav Kumar

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出模型优先推理方法，通过显式问题建模减少大语言模型在复杂规划任务中的幻觉问题**

**关键词**: `大语言模型` `规划任务` `显式建模` `模型优先推理` `约束违反` `AI代理` `可解释性` `多步规划`

## 📋 核心要点

1. 现有方法如思维链和ReAct依赖隐式状态跟踪，缺乏显式问题表示，导致高约束违反和不一致解决方案。
2. 提出模型优先推理，两阶段范式：先构建显式问题模型，再生成解决方案计划，以增强表示能力。
3. 在多个规划领域实验中，MFR显著减少约束违反，提高解决方案质量，消融研究证实显式建模的关键作用。

## 📝 摘要（中文）

大语言模型在处理复杂多步规划任务时，常出现高约束违反率和不一致解决方案。现有策略如思维链和ReAct依赖隐式状态跟踪，缺乏显式问题表示。受经典AI规划启发，本文提出模型优先推理，这是一种两阶段范式：LLM首先构建问题的显式模型，定义实体、状态变量、动作和约束，然后生成解决方案计划。在医疗调度、路径规划、资源分配、逻辑谜题和程序合成等多个规划领域中，与思维链和ReAct相比，MFR减少了约束违反并提高了解决方案质量。消融研究表明，显式建模阶段对这些改进至关重要。结果表明，许多LLM规划失败源于表示缺陷而非推理限制，凸显显式建模作为稳健可解释AI代理的关键组成部分。所有提示、评估程序和任务数据集均已记录，以促进可重复性。

## 🔬 方法详解

模型优先推理采用两阶段框架：第一阶段，LLM构建问题的显式模型，包括定义实体、状态变量、动作和约束，形成结构化表示；第二阶段，基于此模型生成解决方案计划。关键创新在于引入显式建模步骤，将问题表示与推理分离，类似于经典AI规划方法。与现有方法如思维链和ReAct的主要区别在于，MFR不依赖隐式状态跟踪，而是通过显式模型提供清晰的问题结构，从而减少幻觉和约束违反，提高规划任务的稳健性和可解释性。

## 📊 实验亮点

在多个规划领域实验中，MFR相比思维链和ReAct，显著减少约束违反率，提高解决方案质量；消融研究显示，显式建模阶段是关键改进因素，验证了表示缺陷是LLM规划失败的主要原因。

## 🎯 应用场景

该研究适用于需要复杂多步规划的领域，如医疗调度、路径规划、资源分配、逻辑谜题和程序合成。通过显式建模，可提升AI代理在实际任务中的可靠性和效率，支持自动化决策和智能系统开发。

## 📄 摘要（原文）

> Large Language Models (LLMs) often struggle with complex multi-step planning tasks, showing high rates of constraint violations and inconsistent solutions. Existing strategies such as Chain-of-Thought and ReAct rely on implicit state tracking and lack an explicit problem representation. Inspired by classical AI planning, we propose Model-First Reasoning (MFR), a two-phase paradigm in which the LLM first constructs an explicit model of the problem, defining entities, state variables, actions, and constraints, before generating a solution plan. Across multiple planning domains, including medical scheduling, route planning, resource allocation, logic puzzles, and procedural synthesis, MFR reduces constraint violations and improves solution quality compared to Chain-of-Thought and ReAct. Ablation studies show that the explicit modeling phase is critical for these gains. Our results suggest that many LLM planning failures stem from representational deficiencies rather than reasoning limitations, highlighting explicit modeling as a key component for robust and interpretable AI agents. All prompts, evaluation procedures, and task datasets are documented to facilitate reproducibility.

