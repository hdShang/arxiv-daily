---
layout: default
title: Automated Hybrid Reward Scheduling via Large Language Models for Robotic Skill Learning
---

# Automated Hybrid Reward Scheduling via Large Language Models for Robotic Skill Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02483" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02483v1</a>
  <a href="https://arxiv.org/pdf/2505.02483.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02483v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02483v1', 'Automated Hybrid Reward Scheduling via Large Language Models for Robotic Skill Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changxin Huang, Junyang Liang, Yanbin Chang, Jingzhao Xu, Jianqiang Li

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-05

---

## 💡 一句话要点

**提出基于大语言模型的自动化混合奖励调度以提升机器人技能学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `机器人技能学习` `大语言模型` `奖励调度` `多分支网络` `动态调整` `性能提升`

## 📋 核心要点

1. 现有的强化学习方法在处理高自由度机器人技能学习时，通常对所有奖励组件进行简单相加，导致学习效率低下。
2. 本文提出的AHRS框架利用大语言模型动态调整各奖励组件的学习强度，使得机器人能够更有效地掌握复杂技能。
3. 实验结果表明，AHRS方法在多个高自由度机器人任务中实现了平均6.48%的性能提升，展示了其有效性。

## 📝 摘要（中文）

高自由度机器人学习特定技能面临复杂的动态挑战。尽管强化学习（RL）是一种有效的解决方案，但现有方法通常对所有奖励组件进行统一处理，导致学习效率低下。为此，本文提出了一种基于大语言模型（LLMs）的自动化混合奖励调度（AHRS）框架，动态调整各奖励组件的学习强度，从而使机器人以渐进和结构化的方式掌握技能。通过设计多分支价值网络，每个分支对应一个特定的奖励组件，AHRS方法在多项高自由度机器人任务中实现了平均6.48%的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决高自由度机器人在技能学习中面临的奖励函数设计复杂性问题。现有方法对所有奖励组件的统一处理导致了学习效率低下，限制了机器人的学习性能。

**核心思路**：提出的AHRS框架通过大语言模型动态调整各奖励组件的学习强度，使得机器人能够在政策优化过程中逐步掌握技能。这种方法通过多分支价值网络实现，每个分支对应一个特定的奖励组件。

**技术框架**：AHRS框架包括多个主要模块：首先，LLM根据任务描述生成一套规则；其次，在训练过程中，模型根据语言提示选择合适的权重计算规则，动态调整每个奖励组件的权重。

**关键创新**：AHRS的核心创新在于利用大语言模型生成的规则集来动态调整奖励组件的权重，这与现有方法的静态处理方式形成鲜明对比，显著提升了学习效率。

**关键设计**：在网络结构上，设计了一个多分支价值网络，每个分支对应一个奖励组件。权重计算规则由LLM生成，确保在政策优化过程中能够实时反映各奖励组件的重要性。

## 📊 实验亮点

实验结果显示，AHRS方法在多个高自由度机器人任务中实现了平均6.48%的性能提升，相较于传统方法具有显著的优势。这一结果表明，动态调整奖励组件的学习强度能够有效提升机器人技能学习的效率。

## 🎯 应用场景

该研究的潜在应用领域包括高自由度机器人在工业自动化、服务机器人以及医疗机器人等多个场景。通过提升机器人技能学习的效率，AHRS框架能够加速机器人在复杂任务中的适应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Enabling a high-degree-of-freedom robot to learn specific skills is a challenging task due to the complexity of robotic dynamics. Reinforcement learning (RL) has emerged as a promising solution; however, addressing such problems requires the design of multiple reward functions to account for various constraints in robotic motion. Existing approaches typically sum all reward components indiscriminately to optimize the RL value function and policy. We argue that this uniform inclusion of all reward components in policy optimization is inefficient and limits the robot's learning performance. To address this, we propose an Automated Hybrid Reward Scheduling (AHRS) framework based on Large Language Models (LLMs). This paradigm dynamically adjusts the learning intensity of each reward component throughout the policy optimization process, enabling robots to acquire skills in a gradual and structured manner. Specifically, we design a multi-branch value network, where each branch corresponds to a distinct reward component. During policy optimization, each branch is assigned a weight that reflects its importance, and these weights are automatically computed based on rules designed by LLMs. The LLM generates a rule set in advance, derived from the task description, and during training, it selects a weight calculation rule from the library based on language prompts that evaluate the performance of each branch. Experimental results demonstrate that the AHRS method achieves an average 6.48% performance improvement across multiple high-degree-of-freedom robotic tasks.

