---
layout: default
title: RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation
---

# RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01709" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01709v3</a>
  <a href="https://arxiv.org/pdf/2505.01709.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01709v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01709v3', 'RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaidong Zhang, Rongtao Xu, Pengzhen Ren, Junfan Lin, Hefeng Wu, Liang Lin, Xiaodan Liang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-05-03 (更新: 2025-07-23)

**备注**: project page: https://abliao.github.io/RoBridge/

---

## 💡 一句话要点

**提出RoBridge以解决机器人操作中的认知与执行问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `认知与执行` `多模态模型` `强化学习` `智能架构` `开放环境` `任务泛化`

## 📋 核心要点

1. 现有方法在开放环境中面临程序技能和声明技能的困境，无法有效整合认知与执行能力。
2. 本文提出RoBridge架构，通过高层认知规划器、符号桥梁和通用体现代理，解决认知与执行之间的鸿沟。
3. RoBridge在新任务上取得75%的成功率，在模拟到现实的泛化中平均成功率达到83%，显示出显著的性能提升。

## 📝 摘要（中文）

在开放场景中操作机器人以完成多样化任务是机器人研究与应用的重要方向。尽管自然语言处理和大型多模态模型的进展提升了机器人理解复杂指令的能力，但在开放环境中，机器人操作仍面临程序技能和声明技能的困境。现有方法往往在认知与执行能力之间妥协。为此，本文提出了RoBridge，一个用于通用机器人操作的分层智能架构。该架构包括基于大规模预训练视觉-语言模型的高层认知规划器（HCP）、作为符号桥梁的不可变可操作表示（IOR）以及通用体现代理（GEA）。RoBridge有效地连接了认知与执行，展示了显著的性能提升，新的任务成功率达到75%，在模拟到现实的泛化中平均成功率为83%，仅使用每个任务五个真实世界数据样本。这项工作为机器人系统中认知推理与物理执行的整合迈出了重要一步。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在开放环境中执行多样化任务时的认知与执行能力不足的问题。现有方法往往在这两者之间妥协，导致操作效率低下。

**核心思路**：RoBridge通过分层架构设计，将高层认知规划与低层执行能力有效结合，利用大规模预训练的视觉-语言模型提升认知能力，同时通过强化学习增强执行能力。

**技术框架**：RoBridge的整体架构包括三个主要模块：高层认知规划器（HCP）、不可变可操作表示（IOR）和通用体现代理（GEA）。HCP负责理解复杂指令，IOR作为符号桥梁连接认知与执行，GEA则执行具体操作。

**关键创新**：RoBridge的创新在于其分层架构设计，能够同时保持视觉-语言模型的声明技能和强化学习的程序技能，显著提升了机器人在复杂任务中的表现。

**关键设计**：在设计中，HCP采用了大规模预训练的视觉-语言模型，IOR通过符号表示确保操作的一致性，GEA则通过强化学习优化执行策略，确保在多样化任务中的适应性。

## 📊 实验亮点

RoBridge在新任务上实现了75%的成功率，并在模拟到现实的泛化中达到了83%的平均成功率，显示出相较于现有基线的显著性能提升，且仅需每个任务五个真实世界数据样本。

## 🎯 应用场景

RoBridge的研究成果可广泛应用于服务机器人、工业自动化、智能家居等领域，提升机器人在复杂环境中的操作能力。未来，随着技术的进一步发展，RoBridge有望在更多开放场景中实现自主操作，推动智能机器人向更高水平发展。

## 📄 摘要（原文）

> Operating robots in open-ended scenarios with diverse tasks is a crucial research and application direction in robotics. While recent progress in natural language processing and large multimodal models has enhanced robots' ability to understand complex instructions, robot manipulation still faces the procedural skill dilemma and the declarative skill dilemma in open environments. Existing methods often compromise cognitive and executive capabilities. To address these challenges, in this paper, we propose RoBridge, a hierarchical intelligent architecture for general robotic manipulation. It consists of a high-level cognitive planner (HCP) based on a large-scale pre-trained vision-language model (VLM), an invariant operable representation (IOR) serving as a symbolic bridge, and a generalist embodied agent (GEA). RoBridge maintains the declarative skill of VLM and unleashes the procedural skill of reinforcement learning, effectively bridging the gap between cognition and execution. RoBridge demonstrates significant performance improvements over existing baselines, achieving a 75% success rate on new tasks and an 83% average success rate in sim-to-real generalization using only five real-world data samples per task. This work represents a significant step towards integrating cognitive reasoning with physical execution in robotic systems, offering a new paradigm for general robotic manipulation.

