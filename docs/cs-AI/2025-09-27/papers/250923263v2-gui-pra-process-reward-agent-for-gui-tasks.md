---
layout: default
title: "GUI-PRA: Process Reward Agent for GUI Tasks"
---

# GUI-PRA: Process Reward Agent for GUI Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23263" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23263v2</a>
  <a href="https://arxiv.org/pdf/2509.23263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23263v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23263v2', 'GUI-PRA: Process Reward Agent for GUI Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Xiong, Xavier Hu, Yurun Chen, Yuhang Liu, Changqiao Wu, Pengzhi Gao, Wei Liu, Jian Luan, Shengyu Zhang

**分类**: cs.AI

**发布日期**: 2025-09-27 (更新: 2025-10-03)

---

## 💡 一句话要点

**提出GUI-PRA，通过动态记忆和UI感知提升GUI任务中进程奖励模型的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI自动化` `进程奖励模型` `多模态大语言模型` `动态记忆` `UI感知`

## 📋 核心要点

1. 多模态大语言模型驱动的GUI Agent在长程任务中表现不佳，主要原因是难以有效利用历史信息。
2. GUI-PRA通过动态记忆机制和自适应UI感知机制，使Agent能够关注相关上下文并感知UI状态变化。
3. 实验结果（具体数据未知）表明，GUI-PRA能够比标准PRM提供更好的进程奖励，提升GUI任务的成功率。

## 📝 摘要（中文）

本文提出GUI-PRA，一个用于GUI任务的进程奖励Agent，旨在解决多模态大语言模型在自动化GUI任务中长程任务失败的问题。现有的进程奖励模型(PRM)在处理GUI领域密集的人工输入和长历史数据时，面临“中间丢失”现象，历史信息过载影响当前步骤的评估。此外，标准PRM缺乏GUI变化感知能力，无法根据动作的动态结果进行评估。GUI-PRA通过动态记忆机制（包括基于相关性的检索模块和渐进式摘要模块）智能地处理历史上下文，并通过自适应UI感知机制来推理UI状态变化，动态选择合适的工具来收集视觉证据，从而提供更好的进程奖励。

## 🔬 方法详解

**问题定义**：现有的基于多模态大语言模型的GUI Agent在处理长程任务时，由于历史交互数据过长，导致进程奖励模型(PRM)出现“中间丢失”现象，即模型难以从长历史中提取关键信息来评估当前步骤的优劣。此外，标准PRM缺乏对GUI界面变化的感知能力，无法根据执行动作后的UI状态变化进行动态评估，这与GUI任务的动态特性不符。

**核心思路**：GUI-PRA的核心思路是通过引入动态记忆机制和自适应UI感知机制，使Agent能够更有效地处理历史信息，并根据UI状态的变化进行动态评估。动态记忆机制用于从长历史中检索相关信息并进行摘要，从而缓解“中间丢失”问题。自适应UI感知机制则使Agent能够感知UI状态变化，并选择合适的工具来获取视觉证据，从而进行更准确的评估。

**技术框架**：GUI-PRA的整体框架包含两个主要模块：动态记忆机制和自适应UI感知机制。动态记忆机制包括一个基于相关性的检索模块和一个渐进式摘要模块。检索模块用于从历史交互数据中检索与当前步骤相关的信息，摘要模块用于将历史信息进行压缩和总结。自适应UI感知机制则允许Agent根据UI状态的变化选择合适的工具（例如，OCR、图像识别等）来获取视觉证据。

**关键创新**：GUI-PRA的关键创新在于其动态记忆机制和自适应UI感知机制。动态记忆机制能够有效地缓解“中间丢失”问题，使Agent能够更好地利用历史信息。自适应UI感知机制则使Agent能够根据UI状态的变化进行动态评估，从而更准确地判断当前步骤的优劣。与现有方法相比，GUI-PRA能够更好地处理长程GUI任务，并提供更准确的进程奖励。

**关键设计**：关于动态记忆机制，相关性检索模块的具体实现方式（例如，使用何种相似度度量方法）以及渐进式摘要模块的具体结构（例如，使用循环神经网络或Transformer）未知。关于自适应UI感知机制，如何动态选择合适的工具（例如，基于规则或学习的方法）以及如何将视觉证据融入评估过程的具体细节未知。损失函数和网络结构等细节也未知。

## 📊 实验亮点

论文的主要实验结果集中在验证GUI-PRA在提供进程奖励方面的有效性。通过与标准PRM进行对比，GUI-PRA在长程GUI任务中表现出更好的性能，能够更准确地评估当前步骤的优劣，从而引导Agent更好地完成任务。具体的性能数据（例如，任务成功率、奖励准确率等）以及提升幅度未知，但整体结果表明GUI-PRA能够有效提升GUI Agent的性能。

## 🎯 应用场景

GUI-PRA具有广泛的应用前景，可用于自动化软件测试、RPA（机器人流程自动化）、智能助手等领域。通过提升GUI Agent在长程任务中的性能，GUI-PRA可以显著提高自动化任务的效率和可靠性，降低人工成本，并为用户提供更智能、更便捷的服务。未来，GUI-PRA有望应用于更复杂的GUI任务，例如跨平台应用自动化、移动应用自动化等。

## 📄 摘要（原文）

> Graphical User Interface (GUI) Agents powered by Multimodal Large Language Models (MLLMs) show significant potential for automating tasks. However, they often struggle with long-horizon tasks, leading to frequent failures. Process Reward Models (PRMs) are a promising solution, as they can guide these agents with crucial process signals during inference. Nevertheless, their application to the GUI domain presents unique challenges. When processing dense artificial inputs with long history data, PRMs suffer from a "lost in the middle" phenomenon, where the overwhelming historical context compromises the evaluation of the current step. Furthermore, standard PRMs lacks GUI changing awareness, providing static evaluations that are disconnected from the dynamic consequences of actions, a critical mismatch with the inherently dynamic nature of GUI tasks. In response to these challenges, we introduce GUI-PRA (Process Reward Agent for GUI Tasks), a judge agent designed to better provide process reward than standard PRM by intelligently processing historical context and actively perceiving UI state changes. Specifically, to directly combat the ``lost in the middle'' phenomenon, we introduce a dynamic memory mechanism consisting of two core components: a Relevance-based Retrieval Module to actively fetch pertinent information from long histories and a Progressive Summarization Module to dynamically condense growing interaction data, ensuring the model focuses on relevant context. Moreover, to address the lack of UI changing awareness, we introduce an Aadaptive UI Perception mechanism. This mechanism enables the agent to reason about UI state changes and dynamically select the most appropriate tool to gather grounded visual evidence, ensuring its evaluation is always informed by the current UI context.

