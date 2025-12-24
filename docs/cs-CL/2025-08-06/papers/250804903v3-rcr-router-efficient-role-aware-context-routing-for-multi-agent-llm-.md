---
layout: default
title: "RCR-Router: Efficient Role-Aware Context Routing for Multi-Agent LLM Systems with Structured Memory"
---

# RCR-Router: Efficient Role-Aware Context Routing for Multi-Agent LLM Systems with Structured Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04903" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04903v3</a>
  <a href="https://arxiv.org/pdf/2508.04903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04903v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04903v3', 'RCR-Router: Efficient Role-Aware Context Routing for Multi-Agent LLM Systems with Structured Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Liu, Zhenglun Kong, Changdi Yang, Fan Yang, Tianqi Li, Peiyan Dong, Joannah Nanjekye, Hao Tang, Geng Yuan, Wei Niu, Wenbin Zhang, Pu Zhao, Xue Lin, Dong Huang, Yanzhi Wang

**分类**: cs.CL, cs.AI, cs.MA

**发布日期**: 2025-08-06 (更新: 2025-08-12)

---

## 💡 一句话要点

**提出RCR-Router以解决多智能体LLM系统中的上下文路由问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `上下文路由` `角色感知` `内存选择` `问答系统`

## 📋 核心要点

1. 现有的多智能体LLM系统协调方案依赖静态路由，导致资源浪费和适应性不足。
2. RCR-Router通过动态选择与智能体角色和任务阶段相关的内存子集，优化上下文路由。
3. 实验表明，RCR-Router在减少令牌使用的同时，保持或提升了答案质量，显示出其有效性。

## 📝 摘要（中文）

多智能体大型语言模型（LLM）系统在复杂推理和协作决策任务中展现出强大的潜力。然而，现有的协调方案往往依赖静态或全上下文路由策略，导致过度的令牌消耗、冗余的内存暴露以及在交互轮次中的适应性有限。为此，本文提出了RCR-Router，一个模块化且角色感知的上下文路由框架，旨在实现多智能体LLM的高效、适应性协作。该方法动态选择与每个智能体的角色和任务阶段相关的语义内存子集，同时遵循严格的令牌预算。实验结果表明，RCR-Router在三个多跳问答基准上减少了令牌使用（最高可达30%），同时改善或维持了答案质量。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体LLM系统中静态上下文路由导致的令牌消耗过高和适应性不足的问题。现有方法在交互过程中无法有效选择相关的上下文信息，导致冗余内存使用和效率低下。

**核心思路**：RCR-Router的核心思想是根据每个智能体的角色和任务阶段动态选择语义相关的内存子集，从而实现高效的上下文路由。这种设计使得每个智能体能够在严格的令牌预算内进行有效的协作。

**技术框架**：RCR-Router的整体架构包括三个主要模块：角色感知的内存选择模块、轻量级评分策略和共享内存存储。智能体的输出会被迭代整合到共享内存中，以便逐步优化上下文。

**关键创新**：该研究的主要创新在于首次提出了动态上下文路由方法，能够根据智能体的角色和任务阶段选择相关内存子集，显著提升了多智能体系统的适应性和效率。

**关键设计**：RCR-Router采用轻量级的评分策略来指导内存选择，确保在令牌预算内优化上下文信息。此外，提出的答案质量评分指标超越了传统的问答准确性评估，能够更全面地评估模型生成的解释。

## 📊 实验亮点

实验结果显示，RCR-Router在HotPotQA、MuSiQue和2WikiMultihop三个多跳问答基准上，令牌使用量减少了最高30%，同时在答案质量上保持或提升了性能。这些结果强调了结构化内存路由和输出感知评估在可扩展多智能体LLM系统中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、协作机器人和多智能体系统中的复杂决策支持。通过提高多智能体LLM的协作效率和适应性，RCR-Router能够在实际应用中显著提升系统的响应速度和决策质量，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Multi-agent large language model (LLM) systems have shown strong potential in complex reasoning and collaborative decision-making tasks. However, most existing coordination schemes rely on static or full-context routing strategies, which lead to excessive token consumption, redundant memory exposure, and limited adaptability across interaction rounds. We introduce RCR-Router, a modular and role-aware context routing framework designed to enable efficient, adaptive collaboration in multi-agent LLMs. To our knowledge, this is the first routing approach that dynamically selects semantically relevant memory subsets for each agent based on its role and task stage, while adhering to a strict token budget. A lightweight scoring policy guides memory selection, and agent outputs are iteratively integrated into a shared memory store to facilitate progressive context refinement. To better evaluate model behavior, we further propose an Answer Quality Score metric that captures LLM-generated explanations beyond standard QA accuracy. Experiments on three multi-hop QA benchmarks -- HotPotQA, MuSiQue, and 2WikiMultihop -- demonstrate that RCR-Router reduces token usage (up to 30%) while improving or maintaining answer quality. These results highlight the importance of structured memory routing and output-aware evaluation in advancing scalable multi-agent LLM systems.

