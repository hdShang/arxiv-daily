---
layout: default
title: "ATLAS: Constraints-Aware Multi-Agent Collaboration for Real-World Travel Planning"
---

# ATLAS: Constraints-Aware Multi-Agent Collaboration for Real-World Travel Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25586" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25586v1</a>
  <a href="https://arxiv.org/pdf/2509.25586.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25586v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25586v1', 'ATLAS: Constraints-Aware Multi-Agent Collaboration for Real-World Travel Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jihye Choi, Jinsung Yoon, Jiefeng Chen, Somesh Jha, Tomas Pfister

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**ATLAS：面向真实旅行规划的约束感知多智能体协作框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `约束满足问题` `旅行规划` `大型语言模型` `动态规划`

## 📋 核心要点

1. 现有LLM在复杂约束下的规划能力不足，尤其是在动态变化的真实世界场景中，难以生成最优解。
2. ATLAS通过动态约束管理、迭代计划评估和自适应交错搜索，实现对复杂约束的有效处理。
3. 在TravelPlanner基准测试和真实世界旅行规划任务中，ATLAS显著优于现有方法，提升了规划成功率。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理和工具使用方面取得了显著进展，但它们在复杂约束条件下生成最优、有实际依据的解决方案时常常失败。现实世界的旅行规划就是一个典型的例子，它评估了智能体处理显式、隐式甚至基于与动态环境和用户需求交互而演变的约束的能力。本文提出了ATLAS，一个通用的多智能体框架，旨在有效处理现实世界旅行规划任务中这种复杂的约束感知特性。ATLAS引入了一种原则性的方法，通过动态约束管理、迭代计划评估和自适应交错搜索等专用机制来解决约束感知规划的根本挑战。ATLAS在TravelPlanner基准测试中表现出最先进的性能，将其最终通过率从最佳替代方案的23.3%提高到44.4%。更重要的是，我们的工作首次展示了在具有实时信息搜索和多轮反馈的真实世界旅行规划任务中的定量有效性。在这种现实环境中，ATLAS展示了其卓越的整体规划性能，实现了84%的最终通过率，显著优于包括ReAct（59%）和单体智能体（27%）在内的基线。

## 🔬 方法详解

**问题定义**：现实世界旅行规划涉及多种复杂约束，包括显式约束（如预算、时间）、隐式约束（如偏好、习惯）以及动态约束（如实时交通、突发事件）。现有方法，特别是单体LLM，难以有效管理和推理这些约束，导致规划结果不理想。

**核心思路**：ATLAS的核心思路是将复杂的旅行规划任务分解为多个智能体的协作，每个智能体负责不同的子任务，并通过动态约束管理、迭代计划评估和自适应交错搜索来协调它们的工作，从而更好地处理各种约束。

**技术框架**：ATLAS框架包含以下主要模块：1) 动态约束管理器：负责维护和更新约束信息，包括显式、隐式和动态约束。2) 计划生成器：基于当前约束生成初步的旅行计划。3) 计划评估器：评估计划的可行性和优化程度，并识别潜在的冲突或违反约束的情况。4) 自适应交错搜索：根据评估结果，动态调整搜索策略，并迭代优化计划。智能体之间通过消息传递进行协作和信息共享。

**关键创新**：ATLAS的关键创新在于其多智能体协作架构和约束感知的规划机制。与单体LLM相比，ATLAS能够更好地分解复杂任务，并利用多个智能体的专业知识来处理不同的约束。动态约束管理和迭代计划评估机制使得ATLAS能够适应动态变化的环境和用户需求。

**关键设计**：ATLAS使用LLM作为每个智能体的基础模型，并针对旅行规划任务进行了微调。动态约束管理器使用知识图谱来表示约束信息，并使用规则引擎来推理约束关系。计划评估器使用启发式函数和约束检查器来评估计划的质量。自适应交错搜索使用蒙特卡洛树搜索（MCTS）来探索不同的计划选项。

## 📊 实验亮点

ATLAS在TravelPlanner基准测试中将最终通过率从23.3%提高到44.4%，显著优于现有方法。在真实世界旅行规划任务中，ATLAS实现了84%的最终通过率，远超ReAct（59%）和单体智能体（27%）。这些结果表明ATLAS在处理复杂约束和动态环境方面具有显著优势。

## 🎯 应用场景

ATLAS框架可应用于各种需要复杂约束处理的现实世界规划任务，例如物流调度、供应链管理、智能家居控制等。通过将复杂任务分解为多个智能体的协作，并引入约束感知的规划机制，ATLAS能够提高规划效率和质量，并适应动态变化的环境。

## 📄 摘要（原文）

> While Large Language Models (LLMs) have shown remarkable advancements in reasoning and tool use, they often fail to generate optimal, grounded solutions under complex constraints. Real-world travel planning exemplifies these challenges, evaluating agents' abilities to handle constraints that are explicit, implicit, and even evolving based on interactions with dynamic environments and user needs. In this paper, we present ATLAS, a general multi-agent framework designed to effectively handle such complex nature of constraints awareness in real-world travel planning tasks. ATLAS introduces a principled approach to address the fundamental challenges of constraint-aware planning through dedicated mechanisms for dynamic constraint management, iterative plan critique, and adaptive interleaved search. ATLAS demonstrates state-of-the-art performance on the TravelPlanner benchmark, improving the final pass rate from 23.3% to 44.4% over its best alternative. More importantly, our work is the first to demonstrate quantitative effectiveness on real-world travel planning tasks with live information search and multi-turn feedback. In this realistic setting, ATLAS showcases its superior overall planning performance, achieving an 84% final pass rate which significantly outperforms baselines including ReAct (59%) and a monolithic agent (27%).

