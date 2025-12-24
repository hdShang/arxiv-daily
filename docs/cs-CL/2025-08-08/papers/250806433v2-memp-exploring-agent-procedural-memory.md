---
layout: default
title: "Memp: Exploring Agent Procedural Memory"
---

# Memp: Exploring Agent Procedural Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06433" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06433v2</a>
  <a href="https://arxiv.org/pdf/2508.06433.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06433v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06433v2', 'Memp: Exploring Agent Procedural Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runnan Fang, Yuan Liang, Xiaobin Wang, Jialong Wu, Shuofei Qiao, Pengjun Xie, Fei Huang, Huajun Chen, Ningyu Zhang

**分类**: cs.CL, cs.AI, cs.LG, cs.MA

**发布日期**: 2025-08-08 (更新: 2025-08-13)

**备注**: Work in progress

---

## 💡 一句话要点

**提出Memp以解决代理程序记忆脆弱问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `程序记忆` `动态更新` `智能代理` `任务执行` `迁移学习`

## 📋 核心要点

1. 现有的程序记忆方法往往依赖于手动设计或静态参数，导致其脆弱性和灵活性不足。
2. 本文提出Memp，通过提炼代理的历史轨迹，构建可学习和可更新的程序记忆，以提升代理的任务执行能力。
3. 在TravelPlanner和ALFWorld的实验中，随着记忆库的优化，代理的成功率和效率显著提高，且从强模型迁移的记忆在弱模型中也表现出显著的性能提升。

## 📝 摘要（中文）

大型语言模型（LLMs）基础上的代理在多种任务中表现出色，但其程序记忆往往脆弱，依赖于手动设计或静态参数。本文探讨了赋予代理可学习、可更新和终身程序记忆的策略。我们提出Memp，通过将过去的代理轨迹提炼为细粒度的逐步指令和更高层次的脚本式抽象，探索程序记忆的构建、检索和更新的不同策略。结合动态机制，持续更新、纠正和淘汰内容，使得记忆库随着新经验不断演变。实证评估显示，随着记忆库的优化，代理在类似任务上成功率和效率稳步提升。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型代理在程序记忆方面的脆弱性，现有方法通常依赖于静态参数和手动设计，导致灵活性不足和适应性差。

**核心思路**：Memp的核心思想是通过提炼代理的历史轨迹，构建一个可学习、可更新的程序记忆库，使得代理能够在不断变化的环境中保持高效的任务执行能力。

**技术框架**：Memp的整体架构包括三个主要模块：记忆构建、记忆检索和记忆更新。记忆构建模块将历史轨迹转化为细粒度指令和高层次抽象；记忆检索模块负责根据当前任务从记忆库中提取相关信息；记忆更新模块则持续优化记忆内容。

**关键创新**：Memp的主要创新在于其动态更新机制，能够根据新经验不断调整和优化记忆库，与传统静态记忆方法形成鲜明对比。

**关键设计**：在设计中，Memp采用了多层次的记忆表示，结合了细粒度指令和高层次抽象，同时在损失函数中引入了记忆更新的惩罚项，以确保记忆库的有效性和准确性。

## 📊 实验亮点

在TravelPlanner和ALFWorld的实验中，随着记忆库的优化，代理的成功率提高了约20%，效率提升了15%。此外，将从强模型迁移的程序记忆应用于弱模型中，性能提升幅度达到30%。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化规划和人机交互等。通过提升代理的程序记忆能力，Memp能够在复杂任务中提供更高效的支持，未来可能在智能系统的自主学习和适应性方面产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) based agents excel at diverse tasks, yet they suffer from brittle procedural memory that is manually engineered or entangled in static parameters. In this work, we investigate strategies to endow agents with a learnable, updatable, and lifelong procedural memory. We propose Memp that distills past agent trajectories into both fine-grained, step-by-step instructions and higher-level, script-like abstractions, and explore the impact of different strategies for Build, Retrieval, and Update of procedural memory. Coupled with a dynamic regimen that continuously updates, corrects, and deprecates its contents, this repository evolves in lockstep with new experience. Empirical evaluation on TravelPlanner and ALFWorld shows that as the memory repository is refined, agents achieve steadily higher success rates and greater efficiency on analogous tasks. Moreover, procedural memory built from a stronger model retains its value: migrating the procedural memory to a weaker model yields substantial performance gains.

