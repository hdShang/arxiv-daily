---
layout: default
title: "HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models"
---

# HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00820" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00820v1</a>
  <a href="https://arxiv.org/pdf/2505.00820.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00820v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00820v1', 'HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoxing Li, Wenbo Wu, Yue Wang, Yanran Xu, William Hunt, Sebastian Stein

**分类**: cs.RO

**发布日期**: 2025-05-01

---

## 💡 一句话要点

**提出人机协作的多机器人框架以解决任务分配问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多机器人系统` `人机协作` `大型语言模型` `任务分配` `零-shot 泛化` `安全性` `适应性` `仿真测试`

## 📋 核心要点

1. 现有多机器人系统在泛化能力和异构性管理上存在显著不足，难以适应新任务和场景。
2. 本文提出的HMCF框架结合大型语言模型与人类监督，优化多机器人任务分配与执行。
3. 实验结果显示，HMCF在任务成功率上提升4.76%，并具备良好的零-shot 泛化能力，适应多样化任务。

## 📝 摘要（中文）

随着人工智能的快速发展，机器人能够越来越精确地自主执行复杂任务。然而，多机器人系统在推广到大规模应用（如灾难响应）时面临泛化、异构性和安全性等挑战。传统方法往往缺乏泛化能力，需要大量工程投入以适应新任务，并且难以管理多样化的机器人。为此，本文提出了一种基于大型语言模型的人机协作多机器人框架（HMCF），通过人类监督和LLM的推理能力，优化任务分配与执行。每个机器人配备LLM代理，能够理解自身能力，将任务转化为可执行指令，并通过任务验证和人类监督减少幻觉。仿真结果表明，该框架在任务成功率上超越了现有最先进的任务规划方法，提升幅度达到4.76%。

## 🔬 方法详解

**问题定义**：本文旨在解决多机器人系统在大规模应用中面临的泛化、异构性和安全性挑战。现有方法往往需要大量工程投入，难以适应新任务和场景，且对多样化机器人的管理能力不足。

**核心思路**：HMCF框架通过结合大型语言模型（LLM）与人类监督，提升多机器人系统的适应性和安全性。LLM能够推理不同任务和机器人能力，而人类监督则在必要时进行干预，确保系统的可靠性。

**技术框架**：HMCF框架包括三个主要模块：人类监督、LLM代理和异构机器人。每个机器人配备LLM代理，负责理解自身能力、将任务转化为可执行指令，并通过人类监督进行任务验证。

**关键创新**：HMCF的主要创新在于将大型语言模型与人机协作相结合，显著提升了多机器人系统的任务分配和执行效率。这一设计与传统方法的根本区别在于引入了LLM的推理能力和人类的实时监督。

**关键设计**：在框架中，LLM代理的设计确保了对机器人能力的准确理解，并通过任务验证机制减少了幻觉现象。此外，框架的参数设置和损失函数设计旨在优化任务执行的准确性和效率。

## 📊 实验亮点

实验结果表明，HMCF框架在任务成功率上较现有最先进的任务规划方法提升了4.76%。此外，实地测试展示了其强大的零-shot 泛化能力，能够在多样化任务和环境中以最小的人类干预进行有效操作。

## 🎯 应用场景

该研究的潜在应用领域包括灾难响应、物流管理和智能制造等场景。在这些领域中，HMCF框架能够有效协调多种类机器人，提升任务执行的效率和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Rapid advancements in artificial intelligence (AI) have enabled robots to performcomplex tasks autonomously with increasing precision. However, multi-robot systems (MRSs) face challenges in generalization, heterogeneity, and safety, especially when scaling to large-scale deployments like disaster response. Traditional approaches often lack generalization, requiring extensive engineering for new tasks and scenarios, and struggle with managing diverse robots. To overcome these limitations, we propose a Human-in-the-loop Multi-Robot Collaboration Framework (HMCF) powered by large language models (LLMs). LLMs enhance adaptability by reasoning over diverse tasks and robot capabilities, while human oversight ensures safety and reliability, intervening only when necessary. Our framework seamlessly integrates human oversight, LLM agents, and heterogeneous robots to optimize task allocation and execution. Each robot is equipped with an LLM agent capable of understanding its capabilities, converting tasks into executable instructions, and reducing hallucinations through task verification and human supervision. Simulation results show that our framework outperforms state-of-the-art task planning methods, achieving higher task success rates with an improvement of 4.76%. Real-world tests demonstrate its robust zero-shot generalization feature and ability to handle diverse tasks and environments with minimal human intervention.

