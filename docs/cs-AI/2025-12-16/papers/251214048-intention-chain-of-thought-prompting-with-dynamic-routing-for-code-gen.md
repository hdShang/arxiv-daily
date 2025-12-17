---
layout: default
title: Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation
---

# Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14048" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14048</a>
  <a href="https://arxiv.org/pdf/2512.14048.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14048" onclick="toggleFavorite(this, '2512.14048', 'Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shen Li, Li Huang, Shaoxiong Zhan, Weifeng Sun, Tao Yin, Zhongxin Liu, Meng Yan

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出RoutingGen框架，通过动态路由和意图链式思考提升代码生成效果。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `大型语言模型` `思维链` `动态路由` `意图建模` `提示学习` `认知经济` `算法设计`

## 📋 核心要点

1. 现有CoT方法在代码生成中存在过度思考和缺乏意图抽象的问题，导致效率降低和性能瓶颈。
2. RoutingGen框架通过难度感知路由，动态选择少样本提示或意图链式思考(ICoT)策略，优化资源利用。
3. 实验结果表明，RoutingGen在多个代码生成基准上达到SOTA，并显著降低了token使用量。

## 📝 摘要（中文）

大型语言模型(LLMs)在代码生成方面展现出强大的生成能力和巨大的潜力。现有的思维链(CoT)提示方法通过引发中间步骤来增强模型推理，但存在两个主要限制：首先，它们的统一应用容易导致简单任务的过度思考。其次，它们在代码生成中缺乏意图抽象，例如显式地建模核心算法设计和效率，导致模型专注于表面结构而忽略了全局问题目标。受到认知经济原则的启发，即仅在必要时才进行结构化推理以节省认知资源，我们提出RoutingGen，一种新颖的难度感知路由框架，可以动态地调整代码生成的提示策略。对于简单的任务，它采用少样本提示；对于更复杂的任务，它调用一种结构化的推理策略，称为意图链式思考(ICoT)，我们引入该策略来指导模型捕获任务意图，例如核心算法逻辑及其时间复杂度。在三个模型和六个标准代码生成基准上的实验表明，RoutingGen在大多数设置中实现了最先进的性能，同时在各种设置中平均减少了46.37%的总token使用量。此外，ICoT在具有挑战性的基准测试中优于六个现有的提示基线。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在代码生成任务中，现有思维链(CoT)提示方法存在的两个主要问题：一是对于简单任务的过度推理，导致计算资源浪费；二是缺乏对代码意图的抽象，使得模型难以把握算法的核心逻辑和效率，从而影响代码质量。现有方法未能根据任务难度动态调整推理策略，导致效率和性能受限。

**核心思路**：论文的核心思路是引入难度感知的动态路由机制，根据任务的复杂程度，选择合适的提示策略。对于简单任务，采用更高效的少样本提示；对于复杂任务，则采用结构化的意图链式思考(ICoT)方法，引导模型理解任务意图，从而生成更优质的代码。这种动态调整策略旨在平衡推理成本和代码质量。

**技术框架**：RoutingGen框架包含两个主要模块：难度评估模块和提示策略选择模块。难度评估模块用于判断输入代码生成任务的复杂程度。提示策略选择模块根据难度评估结果，动态选择合适的提示策略。如果任务难度较低，则采用少样本提示；如果任务难度较高，则采用ICoT提示。ICoT提示包括明确建模核心算法逻辑和时间复杂度等步骤，以引导模型捕获任务意图。

**关键创新**：论文的关键创新在于提出了难度感知的动态路由机制和意图链式思考(ICoT)方法。动态路由机制能够根据任务难度自适应地选择提示策略，避免了过度推理和资源浪费。ICoT方法则通过显式地建模任务意图，引导模型生成更符合要求的代码，提升了代码质量。

**关键设计**：难度评估模块的具体实现方式未知，可能采用了基于规则或机器学习的方法。ICoT提示的具体步骤包括：首先，明确任务的目标和约束；其次，设计核心算法逻辑；然后，分析算法的时间复杂度；最后，生成代码。论文中没有详细说明少样本提示的具体实现方式，但可以推测是采用了常见的示例学习方法。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14048/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14048/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14048/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RoutingGen框架在六个标准代码生成基准测试中，在大多数设置下实现了最先进的性能。与现有方法相比，RoutingGen平均减少了46.37%的token使用量，显著提高了效率。此外，ICoT方法在具有挑战性的基准测试中优于六个现有的提示基线，证明了其有效性。

## 🎯 应用场景

该研究成果可应用于各种代码生成场景，例如软件开发、自动化测试、数据分析等。通过动态调整推理策略和引导模型理解任务意图，可以提高代码生成的效率和质量，降低开发成本，并加速软件开发流程。未来，该方法有望扩展到其他自然语言处理任务中，例如文本摘要、机器翻译等。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit strong generative capabilities and have shown great potential in code generation. Existing chain-of-thought (CoT) prompting methods enhance model reasoning by eliciting intermediate steps, but suffer from two major limitations: First, their uniform application tends to induce overthinking on simple tasks. Second, they lack intention abstraction in code generation, such as explicitly modeling core algorithmic design and efficiency, leading models to focus on surface-level structures while neglecting the global problem objective. Inspired by the cognitive economy principle of engaging structured reasoning only when necessary to conserve cognitive resources, we propose RoutingGen, a novel difficulty-aware routing framework that dynamically adapts prompting strategies for code generation. For simple tasks, it adopts few-shot prompting; for more complex ones, it invokes a structured reasoning strategy, termed Intention Chain-of-Thought (ICoT), which we introduce to guide the model in capturing task intention, such as the core algorithmic logic and its time complexity. Experiments across three models and six standard code generation benchmarks show that RoutingGen achieves state-of-the-art performance in most settings, while reducing total token usage by 46.37% on average across settings. Furthermore, ICoT outperforms six existing prompting baselines on challenging benchmarks.

