---
layout: default
title: DSADF: Thinking Fast and Slow for Decision Making
---

# DSADF: Thinking Fast and Slow for Decision Making

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08189" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08189v2</a>
  <a href="https://arxiv.org/pdf/2505.08189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08189v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08189v2', 'DSADF: Thinking Fast and Slow for Decision Making')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Dou, Dongfei Cui, Jun Yan, Weida Wang, Benteng Chen, Haoming Wang, Zeke Xie, Shufei Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-13 (更新: 2025-08-25)

---

## 💡 一句话要点

**提出双系统自适应决策框架以提升RL智能体的决策能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `决策框架` `视觉语言模型` `动态环境` `智能体` `深度推理` `快速决策`

## 📋 核心要点

1. 现有的强化学习方法在动态环境中的泛化能力不足，导致决策效率低下。
2. 本文提出的双系统自适应决策框架（DSADF）结合了RL智能体和视觉语言模型，实现快速与深度推理的协同。
3. 在Crafter和Housekeep等视频游戏环境中，DSADF显著提升了智能体在已知和未知任务中的决策能力。

## 📝 摘要（中文）

尽管强化学习（RL）智能体在明确环境中表现出色，但在动态环境中由于依赖试错交互而难以推广其学习策略。近期研究尝试通过大型语言模型（LLM）或视觉语言模型（VLM）来增强RL智能体的泛化能力，但这些方法往往缺乏与基础模型的无缝协调，导致在不熟悉环境中的决策不合理且效率低下。为了解决这一问题，本文提出了一种双系统自适应决策框架（DSADF），结合了RL智能体和VLM的优势，实现快速直觉与深度推理的平衡。实验证明，该方法在视频游戏环境中显著提升了决策能力。

## 🔬 方法详解

**问题定义**：本文旨在解决强化学习智能体在动态环境中决策能力不足的问题，现有方法往往缺乏与基础模型的有效协调，导致决策不合理和效率瓶颈。

**核心思路**：提出双系统自适应决策框架（DSADF），通过结合快速直觉的RL智能体和深度推理的视觉语言模型（VLM），实现高效的决策过程。这样的设计旨在充分利用两者的优势，提升智能体在复杂环境中的适应能力。

**技术框架**：DSADF框架包含两个主要模块：系统1（RL智能体及其记忆空间）用于快速直觉决策，系统2（VLM）用于深度分析推理。两者通过有效的交互形成一个双系统决策机制。

**关键创新**：DSADF的创新点在于将RL智能体与VLM的推理能力结合，形成一个动态适应的决策系统。这一方法与传统的RL方法相比，能够更好地处理复杂和动态的环境。

**关键设计**：在DSADF中，RL智能体的记忆空间用于存储历史决策信息，VLM则通过分析环境信息提供决策支持。具体的参数设置和损失函数设计尚未详细披露，未来研究可进一步优化这些技术细节。

## 📊 实验亮点

实验结果表明，DSADF在Crafter和Housekeep环境中显著提升了智能体的决策能力，相较于基线方法，决策效率提高了XX%（具体数据待补充），在已知和未知任务中均表现出色。

## 🎯 应用场景

该研究的潜在应用领域包括智能游戏、机器人控制和自动驾驶等动态环境中的决策系统。通过提升智能体的决策能力，DSADF有望在复杂场景中实现更高效的自动化决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Although Reinforcement Learning (RL) agents are effective in well-defined environments, they often struggle to generalize their learned policies to dynamic settings due to their reliance on trial-and-error interactions. Recent work has explored applying Large Language Models (LLMs) or Vision Language Models (VLMs) to boost the generalization of RL agents through policy optimization guidance or prior knowledge. However, these approaches often lack seamless coordination between the RL agent and the foundation model, leading to unreasonable decision-making in unfamiliar environments and efficiency bottlenecks. Making full use of the inferential capabilities of foundation models and the rapid response capabilities of RL agents and enhancing the interaction between the two to form a dual system is still a lingering scientific question. To address this problem, we draw inspiration from Kahneman's theory of fast thinking (System 1) and slow thinking (System 2), demonstrating that balancing intuition and deep reasoning can achieve nimble decision-making in a complex world. In this study, we propose a Dual-System Adaptive Decision Framework (DSADF), integrating two complementary modules: System 1, comprising an RL agent and a memory space for fast and intuitive decision making, and System 2, driven by a VLM for deep and analytical reasoning. DSADF facilitates efficient and adaptive decision-making by combining the strengths of both systems. The empirical study in the video game environment: Crafter and Housekeep demonstrates the effectiveness of our proposed method, showing significant improvements in decision abilities for both unseen and known tasks.

