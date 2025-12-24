---
layout: default
title: "Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning"
---

# Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19828" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19828v4</a>
  <a href="https://arxiv.org/pdf/2508.19828.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19828v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19828v4', 'Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Kristian Kersting, Jeff Z. Pan, Hinrich Schütze, Volker Tresp, Yunpu Ma

**分类**: cs.CL, cs.MA

**发布日期**: 2025-08-27 (更新: 2025-10-08)

---

## 💡 一句话要点

**提出Memory-R1以增强大语言模型的记忆管理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `强化学习` `记忆管理` `自然语言处理` `信息检索`

## 📋 核心要点

1. 现有的大语言模型在处理长时间推理时受限于上下文窗口，缺乏有效的记忆管理机制。
2. Memory-R1通过强化学习框架，赋予大语言模型主动管理外部记忆的能力，包含记忆管理器和答案代理。
3. 在仅使用152个训练问答对的情况下，Memory-R1在多个基准测试中超越了强基线，展现出良好的泛化能力。

## 📝 摘要（中文）

大语言模型（LLMs）在多种自然语言处理任务中展现了卓越的能力，但其本质上是无状态的，受限于有限的上下文窗口，难以进行长时间的推理。为了解决这一问题，Memory-R1提出了一种强化学习框架，使LLMs能够主动管理和利用外部记忆。该框架通过两个专门的代理：记忆管理器和答案代理，来学习结构化操作，如添加、更新、删除和无操作。经过结果驱动的强化学习微调，Memory-R1在仅使用152个训练问答对的情况下，超越了强基线，并在多种问题类型、三个基准（LoCoMo、MSC、LongMemEval）和多个模型规模（3B-14B）上实现了良好的泛化能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型在长时间推理中的无状态性问题，现有方法多为静态和启发式驱动，缺乏学习机制来决定存储、更新或检索内容。

**核心思路**：Memory-R1通过引入强化学习框架，使得大语言模型能够主动管理外部记忆，设计了记忆管理器和答案代理，以实现动态的记忆操作和信息检索。

**技术框架**：整体架构包括两个主要模块：记忆管理器负责学习如何添加、更新、删除和无操作，答案代理则预选并推理相关条目。两者通过结果驱动的强化学习（PPO和GRPO）进行微调。

**关键创新**：最重要的技术创新在于引入了学习机制来动态管理外部记忆，而不是依赖静态的启发式方法，这使得模型在处理复杂问题时更具灵活性和适应性。

**关键设计**：在训练过程中，使用了152个问答对进行微调，采用了适应性较强的损失函数和强化学习策略，确保了模型在多种问题类型和基准测试中的优越表现。

## 📊 实验亮点

Memory-R1在仅使用152个训练问答对的情况下，超越了多个强基线，在LoCoMo、MSC和LongMemEval等基准测试中表现出色，展现出良好的泛化能力，尤其在处理多种问题类型时，提升幅度显著。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、对话代理和信息检索等。通过增强大语言模型的记忆管理能力，能够提升其在复杂任务中的表现，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated impressive capabilities across a wide range of NLP tasks, but they remain fundamentally stateless, constrained by limited context windows that hinder long-horizon reasoning. Recent efforts to address this limitation often augment LLMs with an external memory bank, yet most existing pipelines are static and heuristic-driven, lacking a learned mechanism for deciding what to store, update, or retrieve. We present Memory-R1, a reinforcement learning (RL) framework that equips LLMs with the ability to actively manage and utilize external memory through two specialized agents: a Memory Manager that learns structured operations, including ADD, UPDATE, DELETE, and NOOP; and an Answer Agent that pre-selects and reasons over relevant entries. Both agents are fine-tuned with outcome-driven RL (PPO and GRPO), enabling adaptive memory management with minimal supervision. With only 152 training QA pairs, Memory-R1 outperforms strong baselines and generalizes across diverse question types, three benchmarks (LoCoMo, MSC, LongMemEval), and multiple model scales (3B-14B).

