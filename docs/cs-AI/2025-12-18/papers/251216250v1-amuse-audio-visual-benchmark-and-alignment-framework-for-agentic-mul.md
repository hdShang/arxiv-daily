---
layout: default
title: "AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding"
---

# AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16250" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16250v1</a>
  <a href="https://arxiv.org/pdf/2512.16250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16250v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16250v1', 'AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sanjoy Chowdhury, Karren D. Yang, Xudong Liu, Fartash Faghri, Pavan Kumar Anasosalu Vasu, Oncel Tuzel, Dinesh Manocha, Chun-Liang Li, Raviteja Vemulapalli

**分类**: cs.AI, cs.MA

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**AMUSE：用于Agentic多说话人理解的视听基准和对齐框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `Agentic推理` `多说话人理解` `视听融合` `基准测试` `奖励学习` `大型语言模型`

## 📋 核心要点

1. 现有MLLM在多说话人对话场景中，缺乏有效的agentic推理能力，难以跟踪说话人、理解角色和事件。
2. 提出RAFT框架，通过奖励优化和多模态自评估，实现数据高效的agentic对齐，提升模型性能。
3. 在AMUSE基准测试中，RAFT框架实现了高达39.52%的相对精度提升，验证了其有效性。

## 📝 摘要（中文）

本文提出了AMUSE，一个旨在评估多模态大型语言模型（MLLM）在多说话人、以对话为中心的场景下agentic推理能力的基准。现有MLLM如GPT-4o和Qwen3-Omni在感知方面表现出色，但在需要跟踪说话者、维护角色以及理解跨时间事件的此类场景中表现不佳。AMUSE围绕本质上是agentic的任务设计，要求模型将复杂的视听交互分解为规划、理解和反思步骤。它在零样本、引导和agentic三种模式以及六个任务族（包括时空说话人定位和多模态对话摘要）中评估MLLM。结果表明，当前模型在非agentic和agentic评估下都表现出较弱的多说话人推理和不一致的行为。受任务的agentic本质和LLM agent最新进展的启发，本文提出RAFT，一种数据高效的agentic对齐框架，它将奖励优化与内在多模态自我评估（作为奖励）和选择性参数适应相结合，以实现数据和参数高效的更新。使用RAFT，在基准测试中实现了高达39.52％的相对精度提升。AMUSE和RAFT共同为检查多模态模型中的agentic推理并提高其能力提供了一个实用的平台。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）在处理多说话人、以对话为中心的视听场景时，缺乏有效的agentic推理能力的问题。现有方法难以准确跟踪说话人身份、维护角色一致性，以及理解跨时间发生的事件，导致在会话视频助手和会议分析等应用中表现不佳。

**核心思路**：论文的核心思路是利用agentic框架来提升MLLM在多说话人视听场景中的推理能力。通过将复杂的视听交互分解为规划、理解和反思等步骤，并结合奖励优化和多模态自评估，使模型能够更好地理解和处理多说话人对话中的上下文信息。

**技术框架**：整体框架包含两个主要部分：AMUSE基准测试和RAFT对齐框架。AMUSE基准用于评估MLLM在不同agentic模式下的性能，包括零样本、引导和agentic模式。RAFT框架则用于提升MLLM的agentic推理能力，它通过将奖励优化与内在多模态自评估相结合，并采用选择性参数适应策略，实现数据和参数高效的更新。

**关键创新**：论文的关键创新在于提出了RAFT（Reward-Aware Fine-Tuning）框架，该框架将奖励优化与内在多模态自评估相结合，以提升MLLM的agentic推理能力。与传统的微调方法相比，RAFT能够更有效地利用数据，并根据模型的自身评估结果进行参数调整，从而实现更好的性能。

**关键设计**：RAFT框架的关键设计包括：1) 使用多模态自评估作为奖励信号，引导模型学习更有效的agentic策略；2) 采用选择性参数适应策略，只更新与agentic推理相关的参数，从而提高训练效率；3) 设计了AMUSE基准测试，用于全面评估MLLM在多说话人视听场景下的agentic推理能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16250v1/figures/teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16250v1/figures/eval-modes-short.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16250v1/figures/raft-revised.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，使用RAFT框架后，模型在AMUSE基准测试中实现了高达39.52%的相对精度提升。这一显著的性能提升验证了RAFT框架的有效性，表明其能够显著提高MLLM在多说话人视听场景下的agentic推理能力。此外，实验还表明，RAFT框架具有数据高效性，能够在少量数据上实现显著的性能提升。

## 🎯 应用场景

该研究成果可应用于会话视频助手、会议分析、智能客服等领域。通过提升模型在多说话人场景下的理解和推理能力，可以实现更自然、更智能的人机交互，提高工作效率和用户体验。未来，该技术有望在教育、医疗等领域发挥重要作用。

## 📄 摘要（原文）

> Recent multimodal large language models (MLLMs) such as GPT-4o and Qwen3-Omni show strong perception but struggle in multi-speaker, dialogue-centric settings that demand agentic reasoning tracking who speaks, maintaining roles, and grounding events across time. These scenarios are central to multimodal audio-video understanding, where models must jointly reason over audio and visual streams in applications such as conversational video assistants and meeting analytics. We introduce AMUSE, a benchmark designed around tasks that are inherently agentic, requiring models to decompose complex audio-visual interactions into planning, grounding, and reflection steps. It evaluates MLLMs across three modes zero-shot, guided, and agentic and six task families, including spatio-temporal speaker grounding and multimodal dialogue summarization. Across all modes, current models exhibit weak multi-speaker reasoning and inconsistent behavior under both non-agentic and agentic evaluation. Motivated by the inherently agentic nature of these tasks and recent advances in LLM agents, we propose RAFT, a data-efficient agentic alignment framework that integrates reward optimization with intrinsic multimodal self-evaluation as reward and selective parameter adaptation for data and parameter efficient updates. Using RAFT, we achieve up to 39.52\% relative improvement in accuracy on our benchmark. Together, AMUSE and RAFT provide a practical platform for examining agentic reasoning in multimodal models and improving their capabilities.

