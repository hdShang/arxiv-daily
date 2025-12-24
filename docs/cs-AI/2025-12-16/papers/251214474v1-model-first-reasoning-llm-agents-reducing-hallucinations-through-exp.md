---
layout: default
title: "Model-First Reasoning LLM Agents: Reducing Hallucinations through Explicit Problem Modeling"
---

# Model-First Reasoning LLM Agents: Reducing Hallucinations through Explicit Problem Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14474" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14474v1</a>
  <a href="https://arxiv.org/pdf/2512.14474.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14474v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14474v1', 'Model-First Reasoning LLM Agents: Reducing Hallucinations through Explicit Problem Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Annu Rana, Gaurav Kumar

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Model-First Reasoning，通过显式建模减少LLM在复杂规划任务中的幻觉**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `规划任务` `显式建模` `约束满足` `推理能力`

## 📋 核心要点

1. 现有LLM在复杂规划任务中依赖隐式状态跟踪，缺乏显式问题表示，导致约束违反和结果不一致。
2. Model-First Reasoning (MFR) 范式首先让LLM构建显式问题模型，再生成解决方案，模拟经典AI规划。
3. 实验表明，MFR在多个规划领域显著减少约束违反，提升方案质量，证明显式建模的重要性。

## 📝 摘要（中文）

大型语言模型(LLMs)在复杂的多步骤规划任务中表现不佳，经常出现约束违反和不一致的解决方案。现有的策略，如Chain-of-Thought和ReAct，依赖于隐式状态跟踪，缺乏显式的问题表示。受经典AI规划的启发，我们提出了Model-First Reasoning (MFR)，这是一种两阶段范式，其中LLM首先构建问题的显式模型，定义实体、状态变量、动作和约束，然后再生成解决方案计划。在包括医疗调度、路线规划、资源分配、逻辑谜题和程序合成等多个规划领域，与Chain-of-Thought和ReAct相比，MFR减少了约束违反并提高了解决方案质量。消融研究表明，显式建模阶段对于这些收益至关重要。我们的结果表明，许多LLM规划失败源于表示缺陷，而不是推理限制，强调了显式建模是鲁棒和可解释的AI代理的关键组成部分。所有提示、评估程序和任务数据集均已记录，以方便重现。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在复杂多步骤规划任务中表现出的约束违反和不一致性问题。现有方法，如Chain-of-Thought和ReAct，主要依赖于隐式的状态跟踪，缺乏对问题的显式建模，导致LLM难以有效地进行规划和推理。这些方法在处理复杂约束和依赖关系时容易出错，产生不符合实际情况或逻辑的解决方案。

**核心思路**：论文的核心思路是借鉴经典AI规划的思想，在LLM进行规划之前，先让其构建一个显式的问题模型。这个模型明确地定义了问题中的实体、状态变量、动作以及约束条件。通过显式地表示问题，LLM可以更好地理解问题的结构和约束，从而生成更可靠和一致的解决方案。这种“先建模，后推理”的策略旨在弥补现有方法在问题表示方面的不足。

**技术框架**：Model-First Reasoning (MFR) 包含两个主要阶段：
1. **建模阶段**：LLM接收问题描述，并生成一个显式的问题模型。该模型包括：实体（Entities）、状态变量（State Variables）、动作（Actions）和约束（Constraints）。
2. **规划阶段**：LLM利用第一阶段构建的问题模型，生成解决方案计划。这个计划由一系列动作组成，旨在达到问题的目标，同时满足所有约束条件。
整个框架通过精心设计的提示（prompts）引导LLM完成这两个阶段。

**关键创新**：MFR 的最重要创新在于引入了显式建模阶段。与传统的隐式推理方法不同，MFR 强制 LLM 首先对问题进行结构化表示，然后再进行规划。这种显式建模能够显著提高 LLM 对问题理解的深度和准确性，从而减少幻觉和约束违反。MFR 的本质区别在于将问题求解过程分解为建模和规划两个阶段，使得 LLM 能够更好地利用其知识和推理能力。

**关键设计**：论文的关键设计在于建模阶段的提示工程。通过设计清晰、明确的提示，引导 LLM 准确地识别问题中的实体、状态变量、动作和约束。例如，可以使用特定的模板或格式来表示这些元素，并提供示例来帮助 LLM 理解。此外，还可以使用迭代式的建模过程，让 LLM 在生成模型后进行自我检查和修正，以确保模型的准确性和完整性。论文中没有提及具体的损失函数或网络结构，因为 MFR 主要关注的是提示工程和推理流程的设计。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14474v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Model-First Reasoning (MFR) 在多个规划领域显著优于 Chain-of-Thought 和 ReAct 等基线方法。MFR 能够显著减少约束违反，并提高解决方案的质量。消融研究进一步证实了显式建模阶段对于这些性能提升至关重要。具体性能数据在论文中进行了详细展示，证明了MFR的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要复杂规划和推理的领域，例如：医疗调度、路线规划、资源分配、物流管理、智能制造等。通过显式建模，可以提高AI系统在这些领域的决策质量和可靠性，减少错误和风险。未来，该方法有望扩展到更广泛的AI应用中，例如：智能助手、自动驾驶、机器人控制等。

## 📄 摘要（原文）

> Large Language Models (LLMs) often struggle with complex multi-step planning tasks, showing high rates of constraint violations and inconsistent solutions. Existing strategies such as Chain-of-Thought and ReAct rely on implicit state tracking and lack an explicit problem representation. Inspired by classical AI planning, we propose Model-First Reasoning (MFR), a two-phase paradigm in which the LLM first constructs an explicit model of the problem, defining entities, state variables, actions, and constraints, before generating a solution plan. Across multiple planning domains, including medical scheduling, route planning, resource allocation, logic puzzles, and procedural synthesis, MFR reduces constraint violations and improves solution quality compared to Chain-of-Thought and ReAct. Ablation studies show that the explicit modeling phase is critical for these gains. Our results suggest that many LLM planning failures stem from representational deficiencies rather than reasoning limitations, highlighting explicit modeling as a key component for robust and interpretable AI agents. All prompts, evaluation procedures, and task datasets are documented to facilitate reproducibility.

