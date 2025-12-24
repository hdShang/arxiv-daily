---
layout: default
title: "DrugPilot: LLM-based Parameterized Reasoning Agent for Drug Discovery"
---

# DrugPilot: LLM-based Parameterized Reasoning Agent for Drug Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13940" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13940v2</a>
  <a href="https://arxiv.org/pdf/2505.13940.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13940v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13940v2', 'DrugPilot: LLM-based Parameterized Reasoning Agent for Drug Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kun Li, Zhennan Wu, Shoupeng Wang, Jia Wu, Shirui Pan, Wenbin Hu

**分类**: cs.AI, q-bio.BM

**发布日期**: 2025-05-20 (更新: 2025-07-28)

**备注**: 29 pages, 8 figures, 2 tables

---

## 💡 一句话要点

**提出DrugPilot以解决药物发现中的多模态数据处理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `药物发现` `大型语言模型` `自主智能体` `多模态数据` `参数化推理` `科学决策` `自动化研究` `数据集成`

## 📋 核心要点

1. 现有药物发现方法在多模态数据处理、任务自动化和领域工具支持方面存在显著不足。
2. DrugPilot通过参数化推理架构和记忆池设计，集成结构化工具使用，支持多阶段研究流程。
3. 实验结果显示，DrugPilot在多种场景下的任务完成率显著高于现有智能体，展示了其强大的应用潜力。

## 📝 摘要（中文）

大型语言模型（LLMs）与自主智能体的结合在科学发现中具有重要潜力，但在药物发现领域的应用仍面临多模态数据处理、任务自动化不足及对领域特定工具支持不佳等挑战。为此，本文提出了DrugPilot，一个基于LLM的智能体系统，采用参数化推理架构，旨在实现药物发现中的端到端科学工作流程。DrugPilot通过集成结构化工具使用和新颖的参数化记忆池，支持多阶段研究过程，能够将异构数据转化为标准化表示，提升多轮对话的效率，减少数据交换中的信息损失，增强复杂科学决策能力。我们构建了涵盖八个核心药物发现任务的药物指令数据集，并在Berkeley函数调用基准下，DrugPilot在简单、多工具和多轮场景中分别达到了98.0%、93.5%和64.0%的任务完成率，显著超越了现有最先进的智能体如ReAct和LoT。

## 🔬 方法详解

**问题定义**：本文旨在解决药物发现过程中多模态数据处理效率低、任务自动化程度不足以及对领域特定工具支持不佳的问题。现有方法在这些方面存在显著的局限性，影响了科学决策的效率和准确性。

**核心思路**：DrugPilot的核心思路是通过参数化推理架构和记忆池的设计，集成多种工具和数据源，支持复杂的科学工作流程。这样的设计能够有效地处理异构数据，并提升多轮对话的效率。

**技术框架**：DrugPilot的整体架构包括数据输入模块、参数化记忆池、推理引擎和输出模块。数据输入模块负责接收来自公共源和用户定义的输入，记忆池将这些数据转化为标准化表示，推理引擎则基于这些表示进行决策，最终输出结果。

**关键创新**：DrugPilot的关键创新在于其参数化记忆池的设计，能够有效减少信息损失，并支持高效的多轮对话。这一设计与现有方法相比，显著提升了数据处理的灵活性和决策的准确性。

**关键设计**：在技术细节上，DrugPilot采用了特定的参数设置以优化记忆池的性能，并设计了适应药物发现任务的损失函数和网络结构，以确保在多种场景下的高效表现。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

在Berkeley函数调用基准测试中，DrugPilot在简单、多工具和多轮场景下的任务完成率分别达到了98.0%、93.5%和64.0%，显著超越了ReAct和LoT等现有最先进的智能体，展示了其在药物发现中的强大能力和应用潜力。

## 🎯 应用场景

DrugPilot在药物发现领域的潜在应用场景包括新药研发、药物重定位和临床试验设计等。其自动化和交互式的数据集成推理能力，能够显著提升科学研究的效率和准确性，推动药物发现的进程。未来，DrugPilot有望扩展到其他计算科学领域，促进更广泛的科学发现。

## 📄 摘要（原文）

> Large language models (LLMs) integrated with autonomous agents hold significant potential for advancing scientific discovery through automated reasoning and task execution. However, applying LLM agents to drug discovery is still constrained by challenges such as large-scale multimodal data processing, limited task automation, and poor support for domain-specific tools. To overcome these limitations, we introduce DrugPilot, a LLM-based agent system with a parameterized reasoning architecture designed for end-to-end scientific workflows in drug discovery. DrugPilot enables multi-stage research processes by integrating structured tool use with a novel parameterized memory pool. The memory pool converts heterogeneous data from both public sources and user-defined inputs into standardized representations. This design supports efficient multi-turn dialogue, reduces information loss during data exchange, and enhances complex scientific decision-making. To support training and benchmarking, we construct a drug instruction dataset covering eight core drug discovery tasks. Under the Berkeley function-calling benchmark, DrugPilot significantly outperforms state-of-the-art agents such as ReAct and LoT, achieving task completion rates of 98.0%, 93.5%, and 64.0% for simple, multi-tool, and multi-turn scenarios, respectively. These results highlight DrugPilot's potential as a versatile agent framework for computational science domains requiring automated, interactive, and data-integrated reasoning.

