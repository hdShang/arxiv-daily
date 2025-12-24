---
layout: default
title: "CoreThink: A Symbolic Reasoning Layer to reason over Long Horizon Tasks with LLMs"
---

# CoreThink: A Symbolic Reasoning Layer to reason over Long Horizon Tasks with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00971" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00971v2</a>
  <a href="https://arxiv.org/pdf/2509.00971.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00971v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00971v2', 'CoreThink: A Symbolic Reasoning Layer to reason over Long Horizon Tasks with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jay Vaghasiya, Omkar Ghugarkar, Vishvesh Bhat, Vipul Dholaria, Julian McAuley

**分类**: cs.AI

**发布日期**: 2025-08-31 (更新: 2025-09-03)

---

## 💡 一句话要点

**提出CoreThink以解决长时间任务推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间任务推理` `符号推理` `工具调用` `代码生成` `规划`

## 📋 核心要点

1. 现有方法在长时间任务推理中面临性能瓶颈，导致准确性和效率的下降。
2. CoreThink通过引入General Symbolics推理方法，提供了一种新的推理层，专注于工具调用、代码生成和规划。
3. 在多个基准测试中，CoreThink展示了显著的性能提升，尤其是在Livecodebench和指令跟随评估中取得了领先的准确率。

## 📝 摘要（中文）

我们介绍了CoreThink，一个基于新颖推理方法General Symbolics的最先进推理层。该方法与现有的推理范式如测试时扩展、监督微调和可验证奖励的强化学习有所不同。CoreThink的通用符号推理器（GSR）专门围绕工具调用、代码生成和规划三个关键用例构建，在七个基准测试中表现出色。我们在Livecodebench v6上取得了66.66%的SOTA分数，在指令跟随评估中达到了89%，在ARC-AGI-2上则为24.4%。此外，我们还开发了一个基于General Symbolics原则的智能编码IDE，在SWE-Bench Lite上达到了62.3%的SOTA准确率。我们在没有任何微调或训练成本的情况下实现了这些改进，确保模型在推理任务上的准确性不会受到负面影响。

## 🔬 方法详解

**问题定义**：本论文旨在解决长时间任务推理中的性能瓶颈，现有方法如测试时扩展和强化学习在准确性和效率上存在不足。

**核心思路**：CoreThink的核心思想是通过General Symbolics推理方法，构建一个高效的推理层，专注于特定的应用场景，如工具调用和代码生成，以提升推理性能。

**技术框架**：整体架构包括三个主要模块：工具调用模块、代码生成模块和规划模块。每个模块针对特定任务进行优化，确保推理过程的高效性和准确性。

**关键创新**：最重要的技术创新点在于引入General Symbolics推理方法，区别于传统的微调和强化学习方法，提供了一种无需训练成本的推理提升方案。

**关键设计**：在设计中，CoreThink采用了特定的参数设置和损失函数，以确保推理层的性能提升，同时保持模型在推理任务上的准确性不受影响。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

在实验中，CoreThink在Livecodebench v6上取得了66.66%的SOTA分数，在指令跟随评估中达到了89%的准确率，ARC-AGI-2上为24.4%。此外，智能编码IDE在SWE-Bench Lite上达到了62.3%的准确率，显示出显著的性能提升。

## 🎯 应用场景

CoreThink的研究成果在多个领域具有潜在应用价值，包括自动化编程、智能助手和复杂任务规划等。其高效的推理能力可以显著提升这些应用的智能水平和用户体验，未来可能会在更多智能系统中得到广泛应用。

## 📄 摘要（原文）

> We introduce CoreThink, a state-of-the-art Reasoning Layer built upon a novel reasoning method called General Symbolics. This approach diverges from reasoning paradigms such as test-time scaling, Supervised Fine-Tuning (SFT), and Reinforcement Learning with Verifiable Rewards (RLVR). CoreThink General Symbolic Reasoner (GSR) is specifically structured around three key use cases: tool-calling, code generation, and planning, demonstrating exemplary performance across a total of seven benchmarks in their respective areas. Notably, we are achieving SOTA scores of 66.66% on Livecodebench v6, 89% on Instruction-Following Evals, and 24.4% on ARC-AGI-2. We also present an agentic coding IDE, developed using the principles of General Symbolics, which achieves a state-of-the-art accuracy of 62.3% on SWE-Bench Lite. We are able to achieve these improvements without any fine-tuning or training costs. Our Reasoning Layer is designed to provide a pure performance uplift, ensuring that a model's accuracy on reasoning tasks is never negatively impacted. We argue that incumbent methods will eventually lead to diminishing returns in LLM performance, necessitating the development of new reasoning techniques. This technical report details our approach at a high level and the availability of the CoreThink models for reasoning-intensive use cases.

