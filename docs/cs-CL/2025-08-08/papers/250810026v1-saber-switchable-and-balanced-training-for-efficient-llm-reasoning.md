---
layout: default
title: "SABER: Switchable and Balanced Training for Efficient LLM Reasoning"
---

# SABER: Switchable and Balanced Training for Efficient LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10026" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10026v1</a>
  <a href="https://arxiv.org/pdf/2508.10026.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10026v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10026v1', 'SABER: Switchable and Balanced Training for Efficient LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Zhao, Yanjun Zhao, Jiaming Song, Shien He, Lusheng Zhang, Qiang Zhang, Tianjiao Li

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出SABER以解决大语言模型推理效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理效率` `强化学习` `可切换推理` `令牌预算` `跨领域泛化` `无思考示例` `系统提示`

## 📋 核心要点

1. 现有的大语言模型在处理复杂任务时，推理成本和延迟过高，难以高效应用于各种问题。
2. SABER通过引入用户可控的令牌预算和多种推理模式，优化了模型的推理效率和灵活性。
3. 实验结果显示，SABER在MATH基准上实现了65.4%的推理长度缩减和3.6%的准确性提升。

## 📝 摘要（中文）

大型语言模型（LLMs）通过链式推理在复杂任务上取得了显著的准确性，但在统一应用于所有问题时，面临过高的推理成本和延迟。本文提出了SABER（可切换和均衡训练框架），这是一个强化学习框架，使LLMs具备用户可控的、基于令牌预算的推理能力。SABER首先分析每个训练示例的基础模型思维令牌使用情况，并将其分配到预定义的预算层级。在微调过程中，模型通过系统提示和长度感知奖励来遵循其分配的预算。同时，我们引入无思考示例，以确保模型在关闭显式推理时仍然可靠。SABER支持四种离散推理模式——NoThink、FastThink、CoreThink和DeepThink，灵活权衡延迟与推理深度。大量评估表明，SABER在数学推理、代码生成和逻辑推理任务中，在严格预算下实现了高准确性和有效的跨尺度、跨领域泛化。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理过程中面临的高成本和延迟问题。现有方法在处理不同复杂度任务时，未能有效调整推理资源，导致效率低下。

**核心思路**：SABER通过建立用户可控的令牌预算和多种推理模式，使模型能够根据任务需求灵活调整推理深度，从而提高效率。该设计允许模型在不同任务间进行有效的资源分配。

**技术框架**：SABER的整体架构包括训练示例的预算分配、系统提示引导的微调过程以及无思考示例的引入。模型在训练过程中根据每个示例的复杂性分配预算，并在推理时选择适当的模式。

**关键创新**：SABER的主要创新在于其可切换的推理模式（NoThink、FastThink、CoreThink、DeepThink），使得模型能够在推理深度和延迟之间进行灵活的权衡。这一设计与现有方法的固定推理方式形成鲜明对比。

**关键设计**：在模型训练中，采用长度感知奖励机制来引导模型遵循预算，同时引入无思考示例以增强模型的可靠性。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多信息。

## 📊 实验亮点

在MATH基准测试中，SABER-FastThink模式将推理长度缩短了65.4%，同时实现了3.6%的准确性提升，显示出在严格预算下的高效性能。实验结果表明，SABER在数学推理、代码生成和逻辑推理等任务中均表现出色，具有良好的跨领域泛化能力。

## 🎯 应用场景

SABER的研究成果在多个领域具有广泛的应用潜力，包括教育、编程辅助和逻辑推理等。通过提高大语言模型的推理效率，SABER可以帮助用户在更短的时间内获得更准确的结果，提升工作效率。此外，该框架的灵活性使其能够适应不同任务的需求，具有良好的扩展性和适应性。

## 📄 摘要（原文）

> Large language models (LLMs) empowered by chain-of-thought reasoning have achieved impressive accuracy on complex tasks but suffer from excessive inference costs and latency when applied uniformly to all problems. We propose SABER (Switchable and Balanced Training for Efficient LLM Reasoning), a reinforcement learning framework that endows LLMs with user-controllable, token-budgeted reasoning. SABER first profiles each training example's base-model thinking token usage and assigns it to one of the predefined budget tiers. During fine-tuning, the model is guided by system prompts and length-aware rewards to respect its assigned budget. In parallel, we incorporate no-think examples to ensure the model remains reliable even when explicit reasoning is turned off. SABER further supports four discrete inference modes - NoThink, FastThink, CoreThink, and DeepThink, enabling flexible trade-offs between latency and reasoning depth. Extensive evaluations on math reasoning (MATH, GSM8K), code generation (MBPP), and logical reasoning (LiveBench-Reasoning) demonstrate that SABER achieves high accuracy under tight budgets, graceful degradation, and effective cross-scale and cross-domain generalization. In particular, SABER-FastThink cuts reasoning length by 65.4% and yields a 3.6% accuracy gain compared with the base model on the MATH benchmark.

