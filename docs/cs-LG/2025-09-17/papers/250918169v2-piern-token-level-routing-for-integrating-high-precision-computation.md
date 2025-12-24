---
layout: default
title: "PiERN: Token-Level Routing for Integrating High-Precision Computation and Reasoning"
---

# PiERN: Token-Level Routing for Integrating High-Precision Computation and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18169" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18169v2</a>
  <a href="https://arxiv.org/pdf/2509.18169.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18169v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18169v2', 'PiERN: Token-Level Routing for Integrating High-Precision Computation and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengbo Xiao, Jingyuan Fan, Xin Tong, Jingzhao Zhang, Chao Lu, Guannan He

**分类**: cs.LG, cs.CE, cs.CL

**发布日期**: 2025-09-17 (更新: 2025-09-27)

---

## 💡 一句话要点

**PiERN：用于集成高精度计算与推理的Token级路由网络**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算推理` `token级路由` `专家系统` `语言模型` `科学计算`

## 📋 核心要点

1. 现有LLM难以将高精度数值计算能力内生集成，限制了其在复杂系统任务中的应用。
2. PiERN通过token级路由，将计算专家模块与推理模块集成，实现计算与推理的迭代交替。
3. 实验表明，PiERN在精度、延迟、token使用和能耗方面均优于LLM微调和多智能体方法。

## 📝 摘要（中文）

复杂系统上的任务需要高精度的数值计算来支持决策，但目前的大型语言模型（LLM）无法将这种计算作为一种内在且可解释的能力与现有架构集成。多智能体方法可以利用外部专家，但不可避免地会引入通信开销，并因有限的可扩展性而导致效率低下。为此，我们提出了一种物理隔离的专家路由网络（PiERN），这是一种用于集成计算和推理的架构。PiERN没有采用工具使用工作流程或函数调用，而是在分别训练专家、文本到计算模块和路由器后，将计算能力内生地集成到神经网络中。在推理时，路由器在token级别指导计算和推理，从而可以在单个思维链中进行迭代交替。我们针对LLM微调和多智能体系统方法，在具有代表性的线性和非线性计算推理任务上评估了PiERN。结果表明，与直接微调LLM相比，PiERN架构不仅实现了更高的准确性，而且与主流多智能体方法相比，在响应延迟、token使用和GPU能耗方面也取得了显著的改进。PiERN为语言模型与科学系统交互提供了一种高效、可解释和可扩展的范例。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理需要高精度数值计算的复杂系统任务时存在局限性。它们要么难以将计算能力集成到模型内部，要么依赖外部工具或多智能体系统，导致效率低下和可解释性差。现有方法的痛点在于无法在推理过程中灵活地进行计算和推理的迭代。

**核心思路**：PiERN的核心思路是将计算能力模块化，并利用一个路由器在token级别动态地决定何时进行计算，何时进行推理。这种设计允许模型在生成文本的过程中，根据需要灵活地调用计算模块，从而实现计算和推理的紧密结合。通过将计算模块与推理模块解耦，可以分别训练这些模块，并最终通过路由器将它们集成在一起。

**技术框架**：PiERN的整体架构包含三个主要模块：文本到计算模块（text-to-computation module）、专家模块（experts）和路由器（router）。文本到计算模块负责将文本输入转换为计算所需的数值输入。专家模块包含多个预训练的计算专家，每个专家擅长不同的计算任务。路由器根据当前token的上下文，决定将该token路由到哪个专家模块或推理模块。整个流程在推理过程中迭代进行，直到生成最终的输出。

**关键创新**：PiERN最重要的技术创新点在于token级别的路由机制。与传统的工具使用或函数调用方法不同，PiERN的路由器可以在每个token上做出决策，从而实现计算和推理的细粒度控制。这种token级别的路由机制使得模型能够更加灵活地处理复杂的计算推理任务，并避免了多智能体系统中的通信开销。

**关键设计**：PiERN的关键设计包括路由器的设计、专家模块的训练以及文本到计算模块的设计。路由器通常是一个小型神经网络，其输入是当前token的上下文向量，输出是路由决策。专家模块可以使用各种预训练的计算模型，例如数值求解器或符号计算引擎。文本到计算模块的设计需要根据具体的计算任务进行调整，以确保能够将文本输入正确地转换为数值输入。

## 📊 实验亮点

PiERN在多个计算推理任务上取得了显著的性能提升。例如，在线性计算任务中，PiERN的准确率高于直接微调的LLM。在非线性计算任务中，PiERN在响应延迟、token使用和GPU能耗方面均优于主流的多智能体方法。具体而言，PiERN在某些任务上的响应延迟降低了X%，token使用量减少了Y%，GPU能耗降低了Z%（具体数值未知）。

## 🎯 应用场景

PiERN架构具有广泛的应用前景，例如科学计算、金融建模、工程设计等领域。它可以帮助研究人员和工程师更有效地利用语言模型解决复杂的科学问题，并提高决策的准确性和效率。未来，PiERN有望成为连接语言模型与科学系统的桥梁，推动人工智能在科学领域的应用。

## 📄 摘要（原文）

> Tasks on complex systems require high-precision numerical computation to support decisions, but current large language models (LLMs) cannot integrate such computations as an intrinsic and interpretable capability with existing architectures. Multi-agent approaches can leverage external experts, but inevitably introduce communication overhead and suffer from inefficiency caused by limited scalability. To this end, we propose Physically-isolated Experts Routing Network (PiERN), an architecture for integrating computation and reasoning. Instead of the tool-use workflows or function-calling, PiERN endogenously integrates computational capabilities into neural networks after separately training experts, a text-to-computation module, and a router. At inference, the router directs computation and reasoning at the token level, thereby enabling iterative alternation within a single chain of thought. We evaluate PiERN on representative linear and nonlinear computation-reasoning tasks against LLM finetuning and the multi-agent system approaches. Results show that the PiERN architecture achieves not only higher accuracy than directly finetuning LLMs but also significant improvements in response latency, token usage, and GPU energy consumption compared with mainstream multi-agent approaches. PiERN offers an efficient, interpretable, and scalable paradigm for interfacing language models with scientific systems.

