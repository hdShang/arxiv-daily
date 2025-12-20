---
layout: default
title: AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding
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

**AMUSE：用于Agentic多说话人理解的音视频基准和对齐框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多说话人理解` `音视频分析` `Agentic推理` `多模态学习` `基准测试` `奖励优化` `自评估` `大语言模型`

## 📋 核心要点

1. 现有多模态大语言模型在多说话人对话场景中，缺乏有效的Agentic推理能力，难以跟踪说话人、理解角色和事件。
2. 论文提出AMUSE基准测试和RAFT对齐框架，旨在评估和提升模型在Agentic多说话人理解方面的能力。
3. RAFT框架通过奖励优化和多模态自评估，在AMUSE基准测试中实现了高达39.52%的相对准确率提升。

## 📝 摘要（中文）

本文提出了AMUSE，一个专门用于评估Agentic多说话人理解能力的音视频基准。现有的大型多模态语言模型（MLLM），如GPT-4o和Qwen3-Omni，在感知方面表现出色，但在多说话人、以对话为中心的场景中表现不佳，这些场景需要Agentic推理来跟踪说话者、维护角色以及理解跨时间的事件。AMUSE围绕本质上是Agentic的任务设计，要求模型将复杂的音视频交互分解为规划、理解和反思步骤。它在零样本、引导和Agentic三种模式以及六个任务族（包括时空说话人定位和多模态对话摘要）中评估MLLM。研究发现，当前模型在非Agentic和Agentic评估下都表现出较弱的多说话人推理和不一致的行为。受这些任务的Agentic本质和LLM Agent最新进展的推动，本文提出RAFT，一种数据高效的Agentic对齐框架，它将奖励优化与内在多模态自我评估（作为奖励）和选择性参数适应相结合，以实现数据和参数高效的更新。使用RAFT，在AMUSE基准测试中，准确率提高了高达39.52％。AMUSE和RAFT共同为检查多模态模型中的Agentic推理和提高其能力提供了一个实用的平台。

## 🔬 方法详解

**问题定义**：现有的大型多模态语言模型（MLLM）在处理多说话人音视频对话场景时，面临Agentic推理的挑战。这些模型难以准确跟踪每个说话人的身份、角色，以及理解跨越时间轴的事件关联。现有的评估方法也缺乏对Agentic推理能力的针对性测试。

**核心思路**：论文的核心思路是构建一个专门用于评估和提升Agentic多说话人理解能力的基准测试（AMUSE）和对齐框架（RAFT）。AMUSE基准侧重于需要规划、理解和反思的任务，而RAFT框架则利用奖励优化和多模态自评估来提升模型性能。

**技术框架**：RAFT框架包含以下主要组成部分：1) 多模态输入（音视频数据）；2) Agentic任务分解（将复杂任务分解为规划、理解和反思步骤）；3) 奖励优化（使用奖励信号来指导模型学习）；4) 多模态自评估（模型自我评估性能并生成奖励信号）；5) 选择性参数适应（仅更新模型的部分参数，以提高数据效率）。整体流程是，模型接收音视频输入，执行Agentic任务，进行自我评估，并根据奖励信号更新参数。

**关键创新**：RAFT框架的关键创新在于其数据高效的Agentic对齐方法。它结合了奖励优化和内在多模态自评估，无需大量人工标注数据即可提升模型性能。此外，选择性参数适应进一步提高了数据效率，使得模型能够更快地适应新的任务。

**关键设计**：在RAFT框架中，奖励函数的设计至关重要，它需要能够准确反映模型在Agentic任务中的表现。多模态自评估模块利用LLM的推理能力来生成奖励信号。选择性参数适应则通过控制哪些参数被更新，来平衡学习速度和泛化能力。具体的参数设置和网络结构细节在论文中进行了详细描述，但此处未知。

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

实验结果表明，RAFT框架在AMUSE基准测试中取得了显著的性能提升，相对准确率提高了高达39.52%。这表明RAFT框架能够有效地提升模型在Agentic多说话人理解方面的能力，并且具有较高的数据效率。

## 🎯 应用场景

该研究成果可应用于多种场景，如智能会议助手、多模态对话系统、视频内容分析等。通过提升模型在多说话人环境下的理解能力，可以实现更自然、更智能的人机交互，并为视频内容分析提供更准确的信息。

## 📄 摘要（原文）

> Recent multimodal large language models (MLLMs) such as GPT-4o and Qwen3-Omni show strong perception but struggle in multi-speaker, dialogue-centric settings that demand agentic reasoning tracking who speaks, maintaining roles, and grounding events across time. These scenarios are central to multimodal audio-video understanding, where models must jointly reason over audio and visual streams in applications such as conversational video assistants and meeting analytics. We introduce AMUSE, a benchmark designed around tasks that are inherently agentic, requiring models to decompose complex audio-visual interactions into planning, grounding, and reflection steps. It evaluates MLLMs across three modes zero-shot, guided, and agentic and six task families, including spatio-temporal speaker grounding and multimodal dialogue summarization. Across all modes, current models exhibit weak multi-speaker reasoning and inconsistent behavior under both non-agentic and agentic evaluation. Motivated by the inherently agentic nature of these tasks and recent advances in LLM agents, we propose RAFT, a data-efficient agentic alignment framework that integrates reward optimization with intrinsic multimodal self-evaluation as reward and selective parameter adaptation for data and parameter efficient updates. Using RAFT, we achieve up to 39.52\% relative improvement in accuracy on our benchmark. Together, AMUSE and RAFT provide a practical platform for examining agentic reasoning in multimodal models and improving their capabilities.

