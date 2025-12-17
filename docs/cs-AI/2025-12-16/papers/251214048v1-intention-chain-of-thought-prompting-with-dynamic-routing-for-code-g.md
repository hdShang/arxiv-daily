---
layout: default
title: Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation
---

# Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation

**arXiv**: [2512.14048v1](https://arxiv.org/abs/2512.14048) | [PDF](https://arxiv.org/pdf/2512.14048.pdf)

**作者**: Shen Li, Li Huang, Shaoxiong Zhan, Weifeng Sun, Tao Yin, Zhongxin Liu, Meng Yan

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Accepted at AAAI-2026

---

## 💡 一句话要点

**提出RoutingGen框架，通过动态路由和意图链式思考解决代码生成中过度推理和意图抽象不足的问题。**

**关键词**: `代码生成` `大型语言模型` `链式思考提示` `动态路由` `意图抽象` `难度感知` `算法设计` `令牌效率`

## 📋 核心要点

1. 现有链式思考提示方法在代码生成中存在过度推理和意图抽象不足的问题，导致模型效率低下且忽视全局目标。
2. 论文提出RoutingGen框架，结合动态路由和意图链式思考，根据任务难度自适应选择提示策略，提升推理效率。
3. 实验显示RoutingGen在多个基准上达到最优性能，平均减少46.37%令牌使用，意图链式思考优于现有基线。

## 📝 摘要（中文）

大型语言模型在代码生成方面展现出强大的生成能力和巨大潜力。现有的链式思考提示方法通过引出中间步骤来增强模型推理，但存在两个主要局限：首先，其统一应用倾向于在简单任务上引发过度思考；其次，它们在代码生成中缺乏意图抽象，例如明确建模核心算法设计和效率，导致模型关注表面结构而忽视全局问题目标。受认知经济原则启发——仅在必要时进行结构化推理以节省认知资源，我们提出了RoutingGen，一种新颖的难度感知路由框架，动态调整代码生成的提示策略。对于简单任务，它采用少样本提示；对于更复杂的任务，它调用结构化推理策略，称为意图链式思考，我们引入该策略来指导模型捕捉任务意图，如核心算法逻辑及其时间复杂度。在三个模型和六个标准代码生成基准上的实验表明，RoutingGen在大多数设置中实现了最先进的性能，同时在所有设置中平均减少了46.37%的总令牌使用量。此外，意图链式思考在具有挑战性的基准上优于六个现有的提示基线。

## 🔬 方法详解

RoutingGen是一个难度感知的动态路由框架，整体框架包括任务难度评估模块和策略选择模块。关键技术创新点在于引入意图链式思考，它通过结构化推理指导模型捕捉任务意图，如核心算法逻辑和时间复杂度，与现有方法的主要区别在于动态路由机制：对于简单任务采用少样本提示以避免过度推理，对于复杂任务则调用意图链式思考进行深度推理，从而优化资源分配和性能。

## 📊 实验亮点

RoutingGen在三个模型和六个标准代码生成基准上实现最先进性能，平均减少46.37%总令牌使用量；意图链式思考在挑战性基准上优于六个现有提示基线，显著提升推理效率和任务完成度。

## 🎯 应用场景

该研究可应用于自动化代码生成、智能编程助手和软件工程工具开发，通过提升代码生成效率和准确性，支持复杂算法设计和优化任务，具有实际价值于减少开发时间和提高代码质量。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit strong generative capabilities and have shown great potential in code generation. Existing chain-of-thought (CoT) prompting methods enhance model reasoning by eliciting intermediate steps, but suffer from two major limitations: First, their uniform application tends to induce overthinking on simple tasks. Second, they lack intention abstraction in code generation, such as explicitly modeling core algorithmic design and efficiency, leading models to focus on surface-level structures while neglecting the global problem objective. Inspired by the cognitive economy principle of engaging structured reasoning only when necessary to conserve cognitive resources, we propose RoutingGen, a novel difficulty-aware routing framework that dynamically adapts prompting strategies for code generation. For simple tasks, it adopts few-shot prompting; for more complex ones, it invokes a structured reasoning strategy, termed Intention Chain-of-Thought (ICoT), which we introduce to guide the model in capturing task intention, such as the core algorithmic logic and its time complexity. Experiments across three models and six standard code generation benchmarks show that RoutingGen achieves state-of-the-art performance in most settings, while reducing total token usage by 46.37% on average across settings. Furthermore, ICoT outperforms six existing prompting baselines on challenging benchmarks.

