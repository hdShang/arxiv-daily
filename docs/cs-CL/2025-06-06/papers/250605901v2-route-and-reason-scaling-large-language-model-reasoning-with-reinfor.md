---
layout: default
title: "Route-and-Reason: Scaling Large Language Model Reasoning with Reinforced Model Router"
---

# Route-and-Reason: Scaling Large Language Model Reasoning with Reinforced Model Router

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05901" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05901v2</a>
  <a href="https://arxiv.org/pdf/2506.05901.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05901v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05901v2', 'Route-and-Reason: Scaling Large Language Model Reasoning with Reinforced Model Router')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyang Shao, Xinyang Liu, Yutang Lin, Fengli Xu, Yong Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-12-04)

---

## 💡 一句话要点

**提出R2-Reasoner以解决大规模语言模型推理效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理效率` `强化学习` `模型路由` `任务分解` `异构模型协作` `自然语言处理`

## 📋 核心要点

1. 现有方法在任务层面直接分配用户查询，无法实现LLMs在细粒度子任务上的有效协作，导致推理效率低下。
2. 本文提出R2-Reasoner框架，通过强化模型路由器实现多个异构模型的协作，优化复杂查询的处理过程。
3. 实验结果显示，R2-Reasoner在六个推理基准上将API成本降低了84.46%，同时保持了与最先进基线相当的推理准确性。

## 📝 摘要（中文）

链式思维被证明对增强大型语言模型（LLMs）的复杂推理能力至关重要，但也导致了高计算成本。现有方法在任务层面直接操作，无法实现混合LLMs在更细粒度子任务上的真正协作。为此，本文提出R2-Reasoner，一个围绕强化模型路由器设计的新框架，旨在高效扩展LLM推理。该路由器通过将复杂查询分解为子任务，并将每个子任务分配给最优模型，平衡性能与成本。实验表明，R2-Reasoner在六个推理基准上将API成本降低了84.46%，同时保持了竞争力的推理准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型在推理过程中的高计算成本和低效率问题。现有方法在任务层面进行操作，无法实现更细粒度的协作，导致资源浪费和性能瓶颈。

**核心思路**：R2-Reasoner通过引入强化模型路由器，首先将复杂查询分解为多个子任务，然后将每个子任务分配给最适合的模型，从而实现高效的协作和资源利用。

**技术框架**：该框架主要包括两个模块：分解器和分配器。分解器负责将复杂查询拆分为子任务，分配器则根据每个子任务的特点选择最优模型。训练过程中采用监督微调与强化学习相结合的方式，提升路由器的自我优化能力。

**关键创新**：R2-Reasoner的核心创新在于其强化模型路由器的设计，使得多个异构模型能够在推理过程中协同工作，显著提高了推理效率和降低了计算成本。与传统方法相比，该框架实现了更细粒度的任务协作。

**关键设计**：在训练过程中，采用两阶段交替训练策略，结合监督学习和强化学习，确保分解器和分配器的有效性。此外，模型参数的选择和损失函数的设计也经过精心调整，以优化整体性能。

## 📊 实验亮点

在六个推理基准上，R2-Reasoner相较于最先进的基线，API成本降低了84.46%，同时保持了竞争力的推理准确性。这一结果表明，该框架在推理效率和成本控制方面具有显著优势。

## 🎯 应用场景

R2-Reasoner框架在多个领域具有广泛的应用潜力，包括自然语言处理、智能问答系统和复杂决策支持等。其高效的推理能力能够显著降低计算成本，提升系统响应速度，未来可能推动更大规模的智能应用落地。

## 📄 摘要（原文）

> Chain-of-thought has been proven essential for enhancing the complex reasoning abilities of Large Language Models (LLMs), but it also leads to high computational costs. Recent advances have explored the method to route queries among multiple models and proved it as a promising approach. However, previous works directly operate at the task level, i.e., assigning user queries to suitable LLMs, which does not allow hybrid LLMs to truly collaborate on finer-grained sub-tasks. Collaboration at the level of intermediate reasoning steps (thoughts) could enable more efficient coordination, but it also poses significant challenges for router scheduling, placing immense demands on the quality of task decomposition and the precision of the router. To address this, we propose R2-Reasoner, a novel framework centered around a Reinforced Model Router designed to efficiently scale LLM reasoning. This router orchestrates collaboration across nine heterogeneous models, whose parameter scales range from less than 1B to hundreds of billions, by first breaking down a complex query into subtasks with a decomposer, and then assigning each subtask to the optimal model with a subtask allocator, balancing performance with cost. Training this router involves a two-stage alternating process for the decomposer and the allocator, integrating supervised fine-tuning with reinforcement learning to enable effective self-supervised refinement. Extensive experiments across six challenging reasoning benchmarks demonstrate that R2-Reasoner reduces API costs by 84.46% compared with state-of-the-art baselines while maintaining competitive reasoning accuracy. Our framework paves the way for the development of more scalable and efficient reasoning systems. Our code is open-source at https://anonymous.4open.science/r/R2_Reasoner.

