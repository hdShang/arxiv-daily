---
layout: default
title: "HiVA: Self-organized Hierarchical Variable Agent via Goal-driven Semantic-Topological Evolution"
---

# HiVA: Self-organized Hierarchical Variable Agent via Goal-driven Semantic-Topological Evolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00189" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00189v1</a>
  <a href="https://arxiv.org/pdf/2509.00189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00189v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00189v1', 'HiVA: Self-organized Hierarchical Variable Agent via Goal-driven Semantic-Topological Evolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinzhou Tang, Jusheng Zhang, Qinhan Lv, Sidi Liu, Jing Yang, Chengpei Tang, Keze Wang

**分类**: cs.AI, cs.MA

**发布日期**: 2025-08-29

---

## 💡 一句话要点

**提出HiVA框架以解决自主智能体在动态环境中的任务执行问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主智能体` `层次可变智能体` `语义-拓扑演化` `动态环境` `任务执行` `多臂老虎机` `自组织图` `资源效率`

## 📋 核心要点

1. 现有方法在动态环境中存在固定工作流的手动配置和灵活循环的推理结构提炼不足的问题。
2. 本文提出的HiVA框架通过自组织图和STEV算法，优化智能体工作流以适应环境变化。
3. 实验结果显示，HiVA在多项基准测试中任务准确率提高5-10%，展现出更高的资源效率。

## 📝 摘要（中文）

自主智能体在推进人工通用智能方面发挥着关键作用，通过大型语言模型实现问题分解和工具协调。然而，现有方法面临着重要的权衡：固定工作流需要在环境变化时手动重新配置，而灵活的反应循环则无法将推理进展提炼为可转移的结构。本文提出了层次可变智能体（HiVA），该框架将智能体工作流建模为自组织图，并通过语义-拓扑演化（STEV）算法优化混合语义-拓扑空间，利用文本梯度作为离散域替代品进行反向传播。该迭代过程包括多臂老虎机驱动的前向路由、基于环境反馈生成的诊断梯度，以及协调更新以共同演化个体语义和拓扑，从而在未知环境中实现集体优化。实验结果表明，HiVA在对话、编码、长上下文问答、数学和智能体基准测试中，任务准确率提高了5-10%，资源效率也得到了增强。

## 🔬 方法详解

**问题定义**：本文旨在解决自主智能体在动态环境中任务执行的效率和灵活性问题。现有方法在环境变化时需要手动调整，导致效率低下。

**核心思路**：HiVA框架通过自组织图模型和语义-拓扑演化算法，能够动态适应环境变化，优化智能体的工作流。这样的设计使得智能体能够在未知环境中进行有效的任务执行。

**技术框架**：HiVA的整体架构包括三个主要模块：多臂老虎机驱动的前向路由、环境反馈生成的诊断梯度，以及个体语义和拓扑的协调更新。这些模块共同作用，实现了智能体的自适应优化。

**关键创新**：HiVA的核心创新在于将智能体工作流建模为自组织图，并通过STEV算法优化语义和拓扑空间。这一方法与传统的固定工作流和灵活反应循环有本质区别，能够更好地应对环境变化。

**关键设计**：在设计中，HiVA使用文本梯度作为离散域替代品进行反向传播，结合多臂老虎机策略进行前向路由，确保智能体能够在复杂环境中进行有效学习和任务执行。具体的参数设置和损失函数设计尚未详细披露，需进一步研究。

## 📊 实验亮点

实验结果表明，HiVA在多个基准测试中任务准确率提升了5-10%，相较于现有基线展现出更高的资源效率。这一成果验证了HiVA在自主任务执行中的有效性和优势。

## 🎯 应用场景

HiVA框架具有广泛的潜在应用场景，包括智能对话系统、自动编程、长上下文问答和复杂任务的自主执行等。其自适应能力使其在动态环境中表现出色，未来可在智能机器人、自动化系统等领域发挥重要作用。

## 📄 摘要（原文）

> Autonomous agents play a crucial role in advancing Artificial General Intelligence, enabling problem decomposition and tool orchestration through Large Language Models (LLMs). However, existing paradigms face a critical trade-off. On one hand, reusable fixed workflows require manual reconfiguration upon environmental changes; on the other hand, flexible reactive loops fail to distill reasoning progress into transferable structures. We introduce Hierarchical Variable Agent (HiVA), a novel framework modeling agentic workflows as self-organized graphs with the Semantic-Topological Evolution (STEV) algorithm, which optimizes hybrid semantic-topological spaces using textual gradients as discrete-domain surrogates for backpropagation. The iterative process comprises Multi-Armed Bandit-infused forward routing, diagnostic gradient generation from environmental feedback, and coordinated updates that co-evolve individual semantics and topology for collective optimization in unknown environments. Experiments on dialogue, coding, Long-context Q&A, mathematical, and agentic benchmarks demonstrate improvements of 5-10% in task accuracy and enhanced resource efficiency over existing baselines, establishing HiVA's effectiveness in autonomous task execution.

