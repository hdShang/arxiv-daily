---
layout: default
title: "Chain-of-Agents: End-to-End Agent Foundation Models via Multi-Agent Distillation and Agentic RL"
---

# Chain-of-Agents: End-to-End Agent Foundation Models via Multi-Agent Distillation and Agentic RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13167" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13167v1</a>
  <a href="https://arxiv.org/pdf/2508.13167.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13167v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13167v1', 'Chain-of-Agents: End-to-End Agent Foundation Models via Multi-Agent Distillation and Agentic RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weizhen Li, Jianbo Lin, Zhuosong Jiang, Jingyi Cao, Xinpeng Liu, Jiayu Zhang, Zhenqiang Huang, Qianben Chen, Weichen Sun, Qiexiang Wang, Hongxuan Lu, Tianrui Qin, Chenghao Zhu, Yi Yao, Shuying Fan, Xiaowan Li, Tiannan Wang, Pai Liu, King Zhu, He Zhu, Dingfeng Shi, Piaohong Wang, Yeyi Guan, Xiangru Tang, Minghao Liu, Yuchen Eleanor Jiang, Jian Yang, Jiaheng Liu, Ge Zhang, Wangchunshu Zhou

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-06

**备注**: 51 pages

---

## 💡 一句话要点

**提出Chain-of-Agents以解决多代理系统效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多代理系统` `大型语言模型` `端到端学习` `强化学习` `蒸馏训练` `复杂问题解决` `智能助手`

## 📋 核心要点

1. 现有多代理系统依赖手动提示和复杂框架，导致计算效率低下和能力不足。
2. 提出Chain-of-Agents范式，通过动态激活不同工具代理和角色扮演代理，实现端到端的复杂问题解决。
3. AFM在多种基准测试中表现出色，超越了现有的最先进模型，展示了显著的性能提升。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）和多代理系统在复杂问题解决任务中展现出显著能力。然而，现有多代理系统通常依赖于手动提示和复杂的代理框架，导致计算效率低下，能力不足，无法充分利用数据驱动学习。本文提出Chain-of-Agents（CoA），一种新颖的LLM推理范式，能够在单一模型中实现原生的端到端复杂问题解决，模拟多代理协作。我们引入多代理蒸馏框架，将先进的多代理系统蒸馏为Chain-of-Agents轨迹，以进行代理监督微调，并通过代理强化学习进一步提升模型在Chain-of-Agents问题解决中的能力。实证研究表明，Agent Foundation Models（AFMs）在多个基准测试中建立了新的最先进性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多代理系统在复杂问题解决中的效率低下和能力不足问题。现有方法依赖于手动提示和复杂的工作流设计，限制了其在数据驱动学习中的应用。

**核心思路**：提出Chain-of-Agents（CoA）范式，允许在单一模型中实现多轮问题解决，动态激活不同的工具代理和角色扮演代理，模拟多代理协作。通过这种方式，模型能够更高效地处理复杂任务。

**技术框架**：整体架构包括多代理蒸馏框架和代理强化学习两个主要模块。首先，通过蒸馏将先进的多代理系统转化为Chain-of-Agents轨迹，然后在可验证的代理任务上进行强化学习，以提升模型能力。

**关键创新**：最重要的创新在于引入了多代理蒸馏和代理强化学习的结合，使得模型能够在端到端的方式下进行复杂问题解决。这一设计与传统的多代理系统有本质区别，后者通常依赖于手动设计的工作流。

**关键设计**：在模型训练中，采用了代理监督微调和强化学习相结合的策略，使用特定的损失函数来优化模型性能。模型结构上，设计了多层次的代理激活机制，以支持动态的任务处理。

## 📊 实验亮点

实验结果显示，Agent Foundation Models（AFMs）在多个基准测试中实现了新的最先进性能，特别是在网络代理和代码代理设置下，性能提升幅度显著，超越了现有的最先进模型。

## 🎯 应用场景

该研究的潜在应用领域包括自动化问题解决、智能助手、编程辅助等。通过提升多代理系统的效率和能力，Chain-of-Agents能够在复杂任务中提供更高效的解决方案，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) and multi-agent systems have demonstrated remarkable capabilities in complex problem-solving tasks such as deep research, vibe coding, and mathematical reasoning. However, most existing multi-agent systems are built upon manual prompt/workflow engineering with sophisticated agent frameworks, making them computationally inefficient, less capable, and can not benefit from data-centric learning. In this work, we introduce Chain-of-Agents (CoA), a novel paradigm of LLM reasoning that enables native end-to-end complex problem-solving in the same way as a multi-agent system (i.e., multi-turn problem solving with multiple tools and multiple agents) within one model. In chain-of-agents problem-solving, the model dynamically activates different tool agents and role-playing agents to simulate multi-agent collaboration in an end-to-end fashion. To elicit end-to-end chain-of-agents problem-solving abilities in LLMs, we introduce a multi-agent distillation framework to distill state-of-the-art multi-agent systems into chain-of-agents trajectories for agentic supervised fine-tuning. We then use agentic reinforcement learning on verifiable agentic tasks to further improve the models' capabilities on chain-of-agents problem solving. We call the resulting models Agent Foundation Models (AFMs). Our empirical studies demonstrate that AFM establishes new state-of-the-art performance across diverse benchmarks in both web agent and code agent settings. We make the entire research, including the model weights, code for training and evaluation, and the training data, fully open-sourced, which offers a solid starting point for future research on agent models and agentic RL.

