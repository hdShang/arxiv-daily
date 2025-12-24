---
layout: default
title: "Robix: A Unified Model for Robot Interaction, Reasoning and Planning"
---

# Robix: A Unified Model for Robot Interaction, Reasoning and Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01106" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01106v2</a>
  <a href="https://arxiv.org/pdf/2509.01106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01106v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01106v2', 'Robix: A Unified Model for Robot Interaction, Reasoning and Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huang Fang, Mengxi Zhang, Heng Dong, Wei Li, Zixuan Wang, Qifeng Zhang, Xueyun Tian, Yucheng Hu, Hang Li

**分类**: cs.AI, cs.CV, cs.RO

**发布日期**: 2025-09-01 (更新: 2025-09-11)

**备注**: Tech report. Project page: https://robix-seed.github.io/robix/

---

## 💡 一句话要点

**提出Robix以解决机器人交互与任务规划问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人交互` `任务规划` `自然语言处理` `多模态学习` `链式思维推理` `强化学习` `上下文感知` `智能系统`

## 📋 核心要点

1. 现有方法在机器人交互和任务规划中存在分离的问题，难以实现自然的多模态交互。
2. Robix通过统一的视觉-语言架构，整合推理、任务规划和自然语言交互，提升机器人的智能化水平。
3. 实验结果显示，Robix在多种任务执行中优于现有基线，展现出强大的泛化能力和任务执行效率。

## 📝 摘要（中文）

我们介绍了Robix，这是一种统一模型，将机器人推理、任务规划和自然语言交互整合在一个视觉-语言架构中。作为分层机器人系统中的高层认知层，Robix动态生成原子命令和人机交互的语言响应，使机器人能够遵循复杂指令、规划长时间任务，并与人类自然互动。Robix还引入了主动对话、实时中断处理和上下文感知的常识推理等新能力。核心上，Robix利用链式思维推理，并采用三阶段训练策略：继续预训练以增强基础的具身推理能力，监督微调以将人机交互和任务规划建模为统一的推理-行动序列，以及强化学习以提高推理-行动一致性和长时间任务的连贯性。大量实验表明，Robix在交互任务执行中超越了开源和商业基线（如GPT-4o和Gemini 2.5 Pro），在多种指令类型和用户参与任务中表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人在交互和任务规划中存在的分离问题，现有方法往往难以实现自然的多模态交互，导致机器人无法有效理解和执行复杂指令。

**核心思路**：Robix的核心思路是通过一个统一的视觉-语言架构，将机器人推理、任务规划和自然语言交互整合在一起，从而提升机器人的智能化和交互能力。这样的设计使得机器人能够在执行任务时，实时响应人类的指令和需求。

**技术框架**：Robix的整体架构包括三个主要模块：1) 继续预训练阶段，增强基础的具身推理能力；2) 监督微调阶段，将人机交互和任务规划建模为统一的推理-行动序列；3) 强化学习阶段，提升推理与行动的一致性和长时间任务的连贯性。

**关键创新**：Robix的关键创新在于引入了主动对话、实时中断处理和上下文感知的常识推理能力，这些能力使得机器人能够在复杂环境中更自然地与人类互动，显著提升了任务执行的灵活性和准确性。

**关键设计**：在技术细节上，Robix采用了链式思维推理方法，并在训练过程中使用了特定的损失函数和网络结构，以确保推理和行动之间的高度一致性。

## 📊 实验亮点

实验结果表明，Robix在交互任务执行中超越了多个开源和商业基线，如GPT-4o和Gemini 2.5 Pro，展现出在多种指令类型下的强大泛化能力，尤其在开放式、多阶段和中断任务中表现优异，提升幅度显著。

## 🎯 应用场景

Robix的研究成果在多个领域具有广泛的应用潜力，包括智能家居、服务机器人、医疗辅助和教育等。通过提升机器人与人类的交互能力，Robix能够在实际场景中更好地理解和执行复杂任务，进而提高工作效率和用户体验。

## 📄 摘要（原文）

> We introduce Robix, a unified model that integrates robot reasoning, task planning, and natural language interaction within a single vision-language architecture. Acting as the high-level cognitive layer in a hierarchical robot system, Robix dynamically generates atomic commands for the low-level controller and verbal responses for human interaction, enabling robots to follow complex instructions, plan long-horizon tasks, and interact naturally with human within an end-to-end framework. Robix further introduces novel capabilities such as proactive dialogue, real-time interruption handling, and context-aware commonsense reasoning during task execution. At its core, Robix leverages chain-of-thought reasoning and adopts a three-stage training strategy: (1) continued pretraining to enhance foundational embodied reasoning abilities including 3D spatial understanding, visual grounding, and task-centric reasoning; (2) supervised finetuning to model human-robot interaction and task planning as a unified reasoning-action sequence; and (3) reinforcement learning to improve reasoning-action consistency and long-horizon task coherence. Extensive experiments demonstrate that Robix outperforms both open-source and commercial baselines (e.g., GPT-4o and Gemini 2.5 Pro) in interactive task execution, demonstrating strong generalization across diverse instruction types (e.g., open-ended, multi-stage, constrained, invalid, and interrupted) and various user-involved tasks such as table bussing, grocery shopping, and dietary filtering.

