---
layout: default
title: "Teaching LLMs to Plan: Logical Chain-of-Thought Instruction Tuning for Symbolic Planning"
---

# Teaching LLMs to Plan: Logical Chain-of-Thought Instruction Tuning for Symbolic Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13351" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13351v1</a>
  <a href="https://arxiv.org/pdf/2509.13351.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13351v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13351v1', 'Teaching LLMs to Plan: Logical Chain-of-Thought Instruction Tuning for Symbolic Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pulkit Verma, Ngoc La, Anthony Favier, Swaroop Mishra, Julie A. Shah

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-14

---

## 💡 一句话要点

**提出PDDL-Instruct框架，通过逻辑链式思维指令调优提升LLM的符号规划能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `符号规划` `大型语言模型` `指令调优` `链式思维` `PDDL`

## 📋 核心要点

1. 现有LLM在符号规划任务中表现不足，尤其是在需要PDDL等形式化表示的领域，缺乏精确的逻辑推理能力。
2. PDDL-Instruct框架通过指令调优，引导LLM进行逻辑链式思维，显式推理动作适用性、状态转换和计划有效性。
3. 实验结果表明，该方法显著提升了LLM的规划准确率，在标准基准测试中达到94%，相比基线模型提升了66%。

## 📝 摘要（中文）

大型语言模型(LLMs)在各种任务中表现出令人印象深刻的能力，但它们执行结构化符号规划的能力仍然有限，尤其是在需要形式化表示的领域，如规划领域定义语言(PDDL)。本文提出了一种新颖的指令调优框架PDDL-Instruct，旨在通过逻辑链式思维推理来增强LLMs的符号规划能力。我们的方法侧重于教导模型使用显式的逻辑推理步骤来严格推理动作适用性、状态转换和计划有效性。通过开发指令提示，引导模型完成精确的逻辑推理，以确定何时可以在给定状态下应用动作，我们使LLMs能够通过结构化的反思来自我纠正其规划过程。该框架通过将规划过程分解为关于前提条件满足、效果应用和不变性保持的显式推理链，系统地构建验证技能。在多个规划领域进行的实验结果表明，我们基于链式思维推理的指令调优模型在规划方面明显更好，在标准基准测试中实现了高达94%的规划准确率，比基线模型提高了66%。这项工作弥合了LLMs的通用推理能力与自动化规划所需的逻辑精度之间的差距，为开发更好的AI规划系统提供了一个有希望的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在符号规划任务中表现不足的问题，特别是当需要使用Planning Domain Definition Language (PDDL) 进行形式化表示时。现有方法无法使LLM进行精确的逻辑推理，导致规划结果不准确。LLM难以理解动作的前提条件、状态转移以及计划的有效性，从而无法生成有效的规划方案。

**核心思路**：论文的核心思路是通过指令调优（Instruction Tuning）的方式，教导LLM进行逻辑链式思维（Logical Chain-of-Thought Reasoning）。具体来说，就是设计一系列指令，引导LLM逐步推理动作的适用性、状态的转移以及计划的有效性。通过显式的逻辑推理步骤，使LLM能够理解规划过程中的约束条件，并生成满足这些约束条件的规划方案。这种方法的核心在于将复杂的规划问题分解为一系列简单的逻辑推理步骤，从而降低了LLM的学习难度。

**技术框架**：PDDL-Instruct框架主要包含以下几个关键模块：1) 指令提示（Instruction Prompts）的设计：设计能够引导LLM进行逻辑推理的指令，包括前提条件检查、效果应用以及不变性保持等。2) 链式思维推理（Chain-of-Thought Reasoning）：将规划过程分解为一系列逻辑推理步骤，LLM需要逐步执行这些步骤，才能得到最终的规划方案。3) 自我纠正（Self-Correction）：通过结构化的反思，LLM可以检查规划过程中的错误，并进行自我纠正。整体流程是，首先将规划问题转化为PDDL格式，然后使用设计的指令提示引导LLM进行链式思维推理，最后得到规划方案。

**关键创新**：该论文最重要的技术创新点在于提出了基于逻辑链式思维的指令调优框架PDDL-Instruct。与现有方法相比，PDDL-Instruct不是直接让LLM生成规划方案，而是引导LLM进行逻辑推理，从而保证了规划方案的正确性。这种方法弥合了LLM的通用推理能力与自动化规划所需的逻辑精度之间的差距。此外，该框架还引入了自我纠正机制，使LLM能够检查规划过程中的错误，并进行自我纠正。

**关键设计**：指令提示的设计是该方法的一个关键环节。指令提示需要清晰地描述每个逻辑推理步骤，并提供足够的上下文信息，以便LLM能够理解这些步骤的含义。例如，对于前提条件检查，指令提示需要明确指出需要检查哪些前提条件，以及如何检查这些前提条件。此外，该论文还使用了数据增强技术，生成了大量的训练数据，以提高LLM的泛化能力。损失函数方面，使用了标准的交叉熵损失函数，以优化LLM的参数。

## 📊 实验亮点

实验结果表明，PDDL-Instruct框架显著提升了LLM的规划准确率。在标准基准测试中，基于链式思维推理的指令调优模型达到了94%的规划准确率，相比基线模型提升了66%。这一结果表明，该方法能够有效地提高LLM的符号规划能力，使其能够更好地解决复杂问题。

## 🎯 应用场景

该研究成果可应用于机器人导航、任务调度、游戏AI等领域。通过提升LLM的符号规划能力，可以使AI系统更好地理解和解决复杂问题，从而实现更智能的自动化。未来，该技术有望应用于智能制造、智能交通等领域，提高生产效率和资源利用率。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated impressive capabilities across diverse tasks, yet their ability to perform structured symbolic planning remains limited, particularly in domains requiring formal representations like the Planning Domain Definition Language (PDDL). In this paper, we present a novel instruction tuning framework, PDDL-Instruct, designed to enhance LLMs' symbolic planning capabilities through logical chain-of-thought reasoning. Our approach focuses on teaching models to rigorously reason about action applicability, state transitions, and plan validity using explicit logical inference steps. By developing instruction prompts that guide models through the precise logical reasoning required to determine when actions can be applied in a given state, we enable LLMs to self-correct their planning processes through structured reflection. The framework systematically builds verification skills by decomposing the planning process into explicit reasoning chains about precondition satisfaction, effect application, and invariant preservation. Experimental results on multiple planning domains show that our chain-of-thought reasoning based instruction-tuned models are significantly better at planning, achieving planning accuracy of up to 94% on standard benchmarks, representing a 66% absolute improvement over baseline models. This work bridges the gap between the general reasoning capabilities of LLMs and the logical precision required for automated planning, offering a promising direction for developing better AI planning systems.

