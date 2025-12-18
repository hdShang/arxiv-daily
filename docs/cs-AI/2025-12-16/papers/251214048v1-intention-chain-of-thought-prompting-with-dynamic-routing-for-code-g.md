---
layout: default
title: Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation
---

# Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14048" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14048v1</a>
  <a href="https://arxiv.org/pdf/2512.14048.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14048v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14048v1', 'Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shen Li, Li Huang, Shaoxiong Zhan, Weifeng Sun, Tao Yin, Zhongxin Liu, Meng Yan

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Accepted at AAAI-2026

---

## 💡 一句话要点

**提出RoutingGen框架，通过动态路由和意图链式思考提升代码生成性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `大语言模型` `思维链` `动态路由` `意图建模` `提示学习` `算法设计` `认知经济`

## 📋 核心要点

1. 现有CoT方法在代码生成中存在过度推理和缺乏意图抽象的问题，导致效率低下且忽略全局目标。
2. RoutingGen框架通过难度感知路由动态调整提示策略，对简单任务采用少样本提示，复杂任务采用意图链式思考（ICoT）。
3. 实验结果表明，RoutingGen在多个代码生成基准上取得了SOTA性能，并显著降低了token使用量。

## 📝 摘要（中文）

大型语言模型（LLMs）展现出强大的生成能力，并在代码生成方面显示出巨大潜力。现有的思维链（CoT）提示方法通过引出中间步骤来增强模型推理，但存在两个主要限制：首先，它们的统一应用容易导致简单任务的过度思考；其次，它们在代码生成中缺乏意图抽象，例如显式地建模核心算法设计和效率，导致模型专注于表面结构而忽略了全局问题目标。受到认知经济原则的启发，即仅在必要时才进行结构化推理以节省认知资源，我们提出了RoutingGen，这是一种新颖的难度感知路由框架，可以动态地调整代码生成的提示策略。对于简单的任务，它采用少样本提示；对于更复杂的任务，它调用一种结构化的推理策略，称为意图链式思考（ICoT），我们引入该策略来指导模型捕获任务意图，例如核心算法逻辑及其时间复杂度。在三个模型和六个标准代码生成基准上的实验表明，RoutingGen在大多数设置中实现了最先进的性能，同时在各种设置中平均减少了46.37%的总token使用量。此外，ICoT在具有挑战性的基准测试中优于六个现有的提示基线。

## 🔬 方法详解

**问题定义**：现有基于思维链（CoT）的代码生成方法存在两个主要问题。一是对于简单的代码生成任务，CoT方法会引入不必要的中间步骤，导致“过度思考”，浪费计算资源。二是现有方法缺乏对代码意图的抽象，例如算法的核心逻辑和时间复杂度，使得模型容易关注代码的表面结构，而忽略了问题的本质。

**核心思路**：论文的核心思路是模仿人类解决问题的认知过程，即根据问题的难度动态调整推理策略。对于简单问题，直接给出答案；对于复杂问题，则进行深入思考。具体来说，论文提出了一个难度感知的路由框架，根据任务的难度选择不同的提示策略。

**技术框架**：RoutingGen框架包含两个主要模块：难度评估模块和提示策略选择模块。难度评估模块用于评估代码生成任务的难度，可以基于任务描述的长度、关键词的数量等特征进行评估。提示策略选择模块根据难度评估的结果选择合适的提示策略。对于简单任务，选择少样本提示（few-shot prompting）；对于复杂任务，选择意图链式思考（ICoT）提示。ICoT提示首先引导模型识别代码的意图，例如算法的核心逻辑和时间复杂度，然后基于意图生成代码。

**关键创新**：该论文的关键创新在于提出了难度感知的动态路由框架RoutingGen和意图链式思考（ICoT）提示。RoutingGen能够根据任务的难度动态调整提示策略，避免了过度思考的问题。ICoT提示能够引导模型关注代码的意图，从而生成更高效、更符合问题本质的代码。与现有方法相比，RoutingGen更加灵活和高效。

**关键设计**：难度评估模块可以使用多种方法实现，例如基于规则的方法、基于机器学习的方法等。ICoT提示的关键在于如何有效地引导模型识别代码的意图。论文中没有详细说明ICoT的具体实现细节，例如如何定义代码意图、如何将意图融入到提示中等，这些细节可能需要根据具体的代码生成任务进行调整。论文中也没有提及具体的损失函数或网络结构的设计。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14048v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14048v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14048v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

RoutingGen在六个标准代码生成基准测试中取得了最先进的性能。与现有方法相比，RoutingGen在保持或提高性能的同时，平均减少了46.37%的token使用量。ICoT提示在具有挑战性的基准测试中优于六个现有的提示基线，证明了其有效性。

## 🎯 应用场景

该研究成果可应用于各种代码生成场景，例如软件开发、自动化测试、代码修复等。通过动态调整提示策略，可以提高代码生成的效率和质量，降低开发成本。未来，该方法可以进一步扩展到其他自然语言生成任务中，例如文本摘要、机器翻译等。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit strong generative capabilities and have shown great potential in code generation. Existing chain-of-thought (CoT) prompting methods enhance model reasoning by eliciting intermediate steps, but suffer from two major limitations: First, their uniform application tends to induce overthinking on simple tasks. Second, they lack intention abstraction in code generation, such as explicitly modeling core algorithmic design and efficiency, leading models to focus on surface-level structures while neglecting the global problem objective. Inspired by the cognitive economy principle of engaging structured reasoning only when necessary to conserve cognitive resources, we propose RoutingGen, a novel difficulty-aware routing framework that dynamically adapts prompting strategies for code generation. For simple tasks, it adopts few-shot prompting; for more complex ones, it invokes a structured reasoning strategy, termed Intention Chain-of-Thought (ICoT), which we introduce to guide the model in capturing task intention, such as the core algorithmic logic and its time complexity. Experiments across three models and six standard code generation benchmarks show that RoutingGen achieves state-of-the-art performance in most settings, while reducing total token usage by 46.37% on average across settings. Furthermore, ICoT outperforms six existing prompting baselines on challenging benchmarks.

