---
layout: default
title: "The Physical Basis of Prediction: World Model Formation in Neural Organoids via an LLM-Generated Curriculum"
---

# The Physical Basis of Prediction: World Model Formation in Neural Organoids via an LLM-Generated Curriculum

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04633" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04633v3</a>
  <a href="https://arxiv.org/pdf/2509.04633.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04633v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04633v3', 'The Physical Basis of Prediction: World Model Formation in Neural Organoids via an LLM-Generated Curriculum')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Brennen Hill

**分类**: cs.NE, cs.AI, cs.LG, q-bio.NC

**发布日期**: 2025-09-04 (更新: 2025-11-04)

**备注**: Published in the proceedings of the 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Scaling Environments for Agents (SEA). Additionally accepted for presentation in NeurIPS 2025 Workshop: Embodied World Models for Decision Making

---

## 💡 一句话要点

**利用LLM生成课程，在神经类器官中构建世界模型的物理基础研究**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经类器官` `世界模型` `大型语言模型` `具身智能` `突触可塑性` `元学习` `生物计算` `强化学习`

## 📋 核心要点

1. 现有具身智能体缺乏在生物基质中构建和适应世界模型的研究，难以理解智能的物理基础。
2. 利用人类神经类器官作为生物智能体，通过精心设计的虚拟环境和LLM驱动的课程进行训练。
3. 通过多模态评估策略，直接测量突触可塑性，从而量化学习到的世界模型的物理相关性。

## 📝 摘要（中文）

本文介绍了一种新颖的框架，用于研究生物基质（人类神经类器官）中世界模型的形成和适应。我们提出了一个由三个可扩展的闭环虚拟环境组成的课程，旨在训练这些生物智能体，并探究学习的潜在突触机制，如长期增强（LTP）和长期抑制（LTD）。我们详细设计了三个不同的任务环境，这些环境需要逐步完善的世界模型才能成功进行决策：（1）用于学习静态状态-动作条件的条件回避任务；（2）用于目标导向交互的一维捕食者-猎物场景；（3）用于建模动态、连续时间系统的经典Pong游戏复现。对于每个环境，我们形式化了状态和动作空间、感觉编码和运动解码机制，以及基于可预测（奖励）和不可预测（惩罚）刺激的反馈协议，这些协议用于驱动模型改进。作为一项重要的方法学进展，我们提出了一种元学习方法，其中大型语言模型自动执行实验协议的生成设计和优化，从而扩展了环境和课程设计的过程。最后，我们概述了一种多模态评估策略，该策略超越了任务性能，通过量化电生理、细胞和分子水平的突触可塑性，直接测量学习到的世界模型的物理相关性。这项工作弥合了基于模型的强化学习和计算神经科学之间的差距，为研究具身认知、决策制定和智能的物理基础提供了一个独特的平台。

## 🔬 方法详解

**问题定义**：现有方法难以在生物系统中研究世界模型的形成和适应，缺乏有效的训练和评估框架。传统方法在设计实验环境和课程时耗时且难以扩展，无法充分探索生物智能体的学习能力。此外，缺乏直接测量世界模型物理基础的手段。

**核心思路**：利用人类神经类器官作为生物智能体，通过闭环虚拟环境进行训练，并使用大型语言模型（LLM）自动生成和优化训练课程。通过奖励和惩罚机制驱动类器官学习，并采用多模态评估策略，直接测量突触可塑性等物理指标，从而理解世界模型的生物学基础。

**技术框架**：该框架包含三个主要模块：1) 虚拟环境设计：设计三个难度递增的虚拟环境，包括条件回避任务、一维捕食者-猎物场景和Pong游戏。2) LLM驱动的课程生成：使用LLM自动生成和优化实验协议，包括状态和动作空间、感觉编码和运动解码机制、以及反馈协议。3) 多模态评估：通过电生理、细胞和分子水平的测量，量化突触可塑性，评估学习到的世界模型的物理相关性。

**关键创新**：1) 将LLM引入生物智能体的训练流程，实现实验设计和优化的自动化和可扩展性。2) 提出了一种多模态评估策略，可以直接测量世界模型的物理基础，而不仅仅是任务性能。3) 利用神经类器官作为生物智能体，为研究具身认知和智能的生物学机制提供了一个独特的平台。

**关键设计**：1) 虚拟环境的状态和动作空间被精心设计，以适应神经类器官的生物学特性。2) 奖励和惩罚机制基于可预测和不可预测的刺激，以驱动模型改进。3) LLM被用于生成和优化实验协议，包括感觉编码和运动解码机制、以及反馈协议。4) 多模态评估策略包括电生理记录、细胞成像和分子生物学分析，以全面评估突触可塑性。

## 📊 实验亮点

该研究提出了一种新颖的框架，通过LLM驱动的课程在神经类器官中构建世界模型。实验设计了三个难度递增的虚拟环境，并采用多模态评估策略，直接测量突触可塑性等物理指标。通过LLM自动生成和优化实验协议，显著提高了实验效率和可扩展性。该研究为理解具身认知和智能的生物学基础提供了新的视角。

## 🎯 应用场景

该研究成果可应用于开发新型生物计算设备、理解神经系统疾病的病理机制，以及探索人工智能的生物学基础。通过研究神经类器官的学习和适应能力，可以为开发更智能、更具适应性的AI系统提供新的思路和方法。此外，该框架还可以用于药物筛选和毒性测试，加速新药研发过程。

## 📄 摘要（原文）

> The capacity of an embodied agent to understand, predict, and interact with its environment is fundamentally contingent on an internal world model. This paper introduces a novel framework for investigating the formation and adaptation of such world models within a biological substrate: human neural organoids. We present a curriculum of three scalable, closed-loop virtual environments designed to train these biological agents and probe the underlying synaptic mechanisms of learning, such as long-term potentiation (LTP) and long-term depression (LTD). We detail the design of three distinct task environments that demand progressively more sophisticated world models for successful decision-making: (1) a conditional avoidance task for learning static state-action contingencies, (2) a one-dimensional predator-prey scenario for goal-directed interaction, and (3) a replication of the classic Pong game for modeling dynamic, continuous-time systems. For each environment, we formalize the state and action spaces, the sensory encoding and motor decoding mechanisms, and the feedback protocols based on predictable (reward) and unpredictable (punishment) stimulation, which serve to drive model refinement. In a significant methodological advance, we propose a meta-learning approach where a Large Language Model automates the generative design and optimization of experimental protocols, thereby scaling the process of environment and curriculum design. Finally, we outline a multi-modal evaluation strategy that moves beyond task performance to directly measure the physical correlates of the learned world model by quantifying synaptic plasticity at electrophysiological, cellular, and molecular levels. This work bridges the gap between model-based reinforcement learning and computational neuroscience, offering a unique platform for studying embodiment, decision-making, and the physical basis of intelligence.

