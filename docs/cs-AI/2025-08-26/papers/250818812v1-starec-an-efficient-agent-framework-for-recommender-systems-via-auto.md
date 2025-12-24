---
layout: default
title: "STARec: An Efficient Agent Framework for Recommender Systems via Autonomous Deliberate Reasoning"
---

# STARec: An Efficient Agent Framework for Recommender Systems via Autonomous Deliberate Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18812" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18812v1</a>
  <a href="https://arxiv.org/pdf/2508.18812.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18812v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18812v1', 'STARec: An Efficient Agent Framework for Recommender Systems via Autonomous Deliberate Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenghao Wu, Ruiyang Ren, Junjie Zhang, Ruirui Wang, Zhongrui Ma, Qi Ye, Wayne Xin Zhao

**分类**: cs.AI

**发布日期**: 2025-08-26

**期刊**: Proceedings of the 34th ACM International Conference on Information and Knowledge Management (CIKM 2025)

**DOI**: [10.1145/3746252.3760995](https://doi.org/10.1145/3746252.3760995)

---

## 💡 一句话要点

**提出STARec以解决推荐系统中的静态用户建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推荐系统` `自主推理` `强化学习` `知识蒸馏` `用户建模` `慢思考` `个性化推荐`

## 📋 核心要点

1. 现有推荐系统依赖静态用户建模和反应式决策，导致推荐结果的相关性和因果推理能力不足。
2. STARec通过将用户建模为具有快速响应和慢速推理的代理，增强了推荐系统的自主推理能力。
3. 在MovieLens 1M和Amazon CDs数据集上，STARec显著提升了推荐性能，使用的数据量仅为0.4%。

## 📝 摘要（中文）

现代推荐系统在信息丰富的环境中发挥着重要作用，但仍然受到静态用户建模和反应式决策范式的限制。当前基于大型语言模型的代理继承了这些缺陷，过度依赖启发式模式匹配，导致推荐结果容易受到表面相关性偏见、因果推理有限以及在稀疏数据场景中的脆弱性影响。为此，本文提出STARec，一个慢思考增强代理框架，使推荐系统具备自主的深思熟虑推理能力。每个用户被建模为一个具有并行认知的代理，快速响应即时交互和慢速推理以进行思维链推理。通过锚定强化训练，我们开发了一种两阶段范式，结合了来自先进推理模型的结构化知识蒸馏与偏好对齐的奖励塑造。实验结果表明，STARec在MovieLens 1M和Amazon CDs基准测试中相比于最先进的基线取得了显著的性能提升，尽管仅使用了0.4%的完整训练数据。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推荐系统在用户建模和决策过程中存在的静态性和反应性问题，导致推荐结果的相关性和因果推理能力不足。

**核心思路**：STARec通过将用户视为具有并行认知的代理，结合快速响应与慢速推理，增强了推荐系统的推理能力，从而克服了传统方法的局限性。

**技术框架**：STARec的整体架构包括两个主要模块：快速响应模块和慢速推理模块。快速响应模块处理即时交互，而慢速推理模块则进行链式思维推理。整个过程通过锚定强化训练进行优化。

**关键创新**：STARec的核心创新在于引入了慢思考的概念，并通过锚定强化训练实现了结构化知识蒸馏与偏好对齐的奖励塑造，这与现有方法的单一模式匹配策略有本质区别。

**关键设计**：在关键设计方面，STARec采用了两阶段的训练流程，结合了先进推理模型的知识蒸馏和动态策略适应，确保代理能够在复杂环境中有效学习和适应。

## 📊 实验亮点

在实验中，STARec在MovieLens 1M和Amazon CDs基准测试中表现出显著的性能提升，相比于最先进的基线，推荐效果有显著改善，且仅使用了0.4%的完整训练数据，展示了其高效性和实用性。

## 🎯 应用场景

STARec的研究成果在多个领域具有潜在应用价值，尤其是在个性化推荐、智能客服和信息过滤等场景中。通过提升推荐系统的推理能力，STARec能够更好地满足用户需求，提供更精准的推荐服务，未来可能推动推荐技术的进一步发展与应用。

## 📄 摘要（原文）

> While modern recommender systems are instrumental in navigating information abundance, they remain fundamentally limited by static user modeling and reactive decision-making paradigms. Current large language model (LLM)-based agents inherit these shortcomings through their overreliance on heuristic pattern matching, yielding recommendations prone to shallow correlation bias, limited causal inference, and brittleness in sparse-data scenarios. We introduce STARec, a slow-thinking augmented agent framework that endows recommender systems with autonomous deliberative reasoning capabilities. Each user is modeled as an agent with parallel cognitions: fast response for immediate interactions and slow reasoning that performs chain-of-thought rationales. To cultivate intrinsic slow thinking, we develop anchored reinforcement training - a two-stage paradigm combining structured knowledge distillation from advanced reasoning models with preference-aligned reward shaping. This hybrid approach scaffolds agents in acquiring foundational capabilities (preference summarization, rationale generation) while enabling dynamic policy adaptation through simulated feedback loops. Experiments on MovieLens 1M and Amazon CDs benchmarks demonstrate that STARec achieves substantial performance gains compared with state-of-the-art baselines, despite using only 0.4% of the full training data.

