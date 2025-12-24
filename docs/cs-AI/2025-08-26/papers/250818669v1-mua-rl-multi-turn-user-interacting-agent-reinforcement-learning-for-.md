---
layout: default
title: "MUA-RL: Multi-turn User-interacting Agent Reinforcement Learning for agentic tool use"
---

# MUA-RL: Multi-turn User-interacting Agent Reinforcement Learning for agentic tool use

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18669" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18669v1</a>
  <a href="https://arxiv.org/pdf/2508.18669.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18669v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18669v1', 'MUA-RL: Multi-turn User-interacting Agent Reinforcement Learning for agentic tool use')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weikang Zhao, Xili Wang, Chengdi Ma, Lingbin Kong, Zhaohua Yang, Mingxiang Tuo, Xiaowei Shi, Yitao Zhai, Xunliang Cai

**分类**: cs.AI

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出MUA-RL以解决多轮用户交互中的工具使用问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `代理智能` `强化学习` `多轮交互` `工具使用` `用户模拟` `动态环境` `模型优化`

## 📋 核心要点

1. 现有的强化学习方法在工具使用中未能有效整合动态用户，导致代理在多轮交互中难以满足用户需求。
2. MUA-RL框架通过将LLM模拟用户纳入强化学习循环，旨在实现模型的自主学习与高效沟通。
3. MUA-RL-32B在多个多轮工具使用基准测试中表现出色，超越或匹配了如DeepSeek-V3-0324等更大模型的性能。

## 📝 摘要（中文）

随着代理智能的快速发展，LLM中的代理工具使用变得愈加重要。在多轮交互中，用户需求的动态性和不确定性对代理的工具调用能力提出了重大挑战。现有的强化学习方法未能在训练过程中有效整合动态用户。为此，本文提出了MUA-RL框架，首次将LLM模拟用户纳入强化学习循环，旨在使模型能够高效地与用户沟通并使用各种工具解决实际问题。实验结果表明，MUA-RL-32B在多个基准测试中表现优异，超越或匹配了更大开源模型的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决在多轮用户交互中，代理工具使用的动态性和不确定性问题。现有方法未能有效整合动态用户，导致代理无法准确理解和满足用户需求。

**核心思路**：MUA-RL通过将LLM模拟用户引入强化学习循环，使代理能够在与用户的交互中不断迭代和优化理解，从而提高工具调用的准确性和效率。

**技术框架**：MUA-RL的整体架构包括用户模拟模块、强化学习训练模块和工具调用模块。用户模拟模块生成动态用户需求，强化学习模块通过与用户的交互不断优化策略，工具调用模块则执行具体的工具操作。

**关键创新**：MUA-RL的核心创新在于首次将LLM模拟用户集成到强化学习过程中，使得代理能够在动态环境中进行有效学习。这一设计与传统方法的静态用户模型形成鲜明对比。

**关键设计**：在技术细节上，MUA-RL采用了特定的损失函数来优化用户交互的效果，并设计了适应动态用户需求的网络结构，以提高模型的灵活性和响应速度。具体参数设置和网络结构设计在实验部分进行了详细描述。

## 📊 实验亮点

MUA-RL-32B在多个基准测试中表现优异，具体结果为：在TAU2 Retail上得分67.3，TAU2 Airline上得分45.4，TAU2 Telecom上得分28.3，BFCL-V3 Multi Turn上得分28.4，以及ACEBench Agent上得分82.5。这些结果超越或匹配了如DeepSeek-V3-0324和Qwen3-235B-A22B等更大模型的性能，显示了MUA-RL的有效性。

## 🎯 应用场景

MUA-RL的研究成果在多个领域具有广泛的应用潜力，包括智能客服、在线教育和人机交互等场景。通过提高代理在多轮交互中的工具使用能力，该框架能够显著提升用户体验和问题解决效率，未来可能推动更智能的交互系统的发展。

## 📄 摘要（原文）

> With the recent rapid advancement of Agentic Intelligence, agentic tool use in LLMs has become increasingly important. During multi-turn interactions between agents and users, the dynamic, uncertain, and stochastic nature of user demands poses significant challenges to the agent's tool invocation capabilities. Agents are no longer expected to simply call tools to deliver a result; rather, they must iteratively refine their understanding of user needs through communication while simultaneously invoking tools to resolve user queries. Existing reinforcement learning (RL) approaches for tool use lack the integration of genuinely dynamic users during the RL training process. To bridge this gap, we introduce MUA-RL (Multi-turn User-interacting Agent Reinforcement Learning for agentic tool use), a novel reinforcement learning framework that, for the first time in the field of agentic tool use, integrates LLM-simulated users into the reinforcement learning loop. MUA-RL aims to enable autonomous learning of models to communicate with users efficiently and use various tools to solve practical problems in dynamic multi-turn interactions. Evaluations are done on several multi-turn tool-using benchmarks (see Figure 1). Specifically, MUA-RL-32B achieves 67.3 on TAU2 Retail, 45.4 on TAU2 Airline, 28.3 on TAU2 Telecom, 28.4 on BFCL-V3 Multi Turn, and 82.5 on ACEBench Agent -- outperforming or matching the performance of larger open-source models such as DeepSeek-V3-0324 and Qwen3-235B-A22B in non-thinking settings.

