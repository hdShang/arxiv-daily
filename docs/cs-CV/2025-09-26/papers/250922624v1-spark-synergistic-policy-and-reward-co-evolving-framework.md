---
layout: default
title: "SPARK: Synergistic Policy And Reward Co-Evolving Framework"
---

# SPARK: Synergistic Policy And Reward Co-Evolving Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22624" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22624v1</a>
  <a href="https://arxiv.org/pdf/2509.22624.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22624v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22624v1', 'SPARK: Synergistic Policy And Reward Co-Evolving Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyu Liu, Yuhang Zang, Shengyuan Ding, Yuhang Cao, Xiaoyi Dong, Haodong Duan, Dahua Lin, Jiaqi Wang

**分类**: cs.CV, cs.LG

**发布日期**: 2025-09-26

**备注**: Project:https://github.com/InternLM/Spark

---

## 💡 一句话要点

**提出SPARK框架以解决RLHF与RLVR的效率与准确性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `奖励模型` `协同演化` `生成模型` `多任务学习`

## 📋 核心要点

1. 现有的RLHF方法成本高且可能导致奖励与策略之间的不匹配，而RLVR则浪费了重要的监督信息。
2. SPARK框架通过回收回滚和正确性数据，构建生成奖励模型，实现奖励与策略的协同演化。
3. SPARK在多个基准测试中表现出色，例如在7个推理基准上平均提升9.7%，在2个奖励基准上提升12.1%。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）和大型视觉语言模型（LVLMs）在后期训练中越来越多地使用强化学习（RL），如可验证奖励的RL（RLVR）和基于人类反馈的RL（RLHF）。然而，RLHF存在高成本和潜在的奖励-策略不匹配问题，而RLVR则在每次更新后丢弃了重要的回滚和正确性信号。为了解决这些挑战，本文提出了一种高效、稳定的协同策略与奖励共同演化框架（SPARK），该框架通过回收回滚和正确性数据，利用混合目标同时训练生成奖励模型，从而消除了对单独奖励模型和人类偏好数据的需求。实验表明，SPARK在多个LLM和LVLM模型上取得了显著的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法中RLHF的高成本和RLVR的监督信息浪费问题。现有方法在更新过程中丢弃了重要的回滚和正确性信号，导致效率低下。

**核心思路**：SPARK框架的核心思路是回收和利用这些丢弃的信息，通过同时训练生成奖励模型来提高奖励的准确性，从而优化策略。这样的设计旨在消除对外部奖励模型和人类偏好数据的依赖。

**技术框架**：SPARK的整体架构包括数据回收模块、生成奖励模型训练模块和策略优化模块。数据回收模块负责收集回滚和正确性信号，生成奖励模型训练模块使用混合目标进行训练，策略优化模块则基于改进的奖励进行策略更新。

**关键创新**：SPARK的最大创新在于构建了一个正向反馈循环，通过提高奖励的准确性来优化策略梯度，从而生成更高质量的回滚，进一步提升奖励模型的性能。这种协同演化机制与传统方法截然不同。

**关键设计**：在设计上，SPARK采用了多种目标函数，包括点对点奖励评分、成对比较和基于进一步反思的评估，以指导模型评估和改进自身的响应。

## 📊 实验亮点

SPARK在多个基准测试中展现出显著的性能提升，例如SPARK-VL-7B在7个推理基准上平均提升9.7%，在2个奖励基准上提升12.1%，在8个通用基准上提升1.5%。这些结果表明SPARK在多种任务中具有良好的鲁棒性和广泛的泛化能力。

## 🎯 应用场景

SPARK框架在多个领域具有广泛的应用潜力，尤其是在需要高效和准确的决策支持系统中，如自动化客服、智能推荐系统和复杂任务的自动化处理。通过减少对人类反馈的依赖，SPARK能够降低成本并提高系统的自适应能力，未来可能在更多实际应用中发挥重要作用。

## 📄 摘要（原文）

> Recent Large Language Models (LLMs) and Large Vision-Language Models (LVLMs) increasingly use Reinforcement Learning (RL) for post-pretraining, such as RL with Verifiable Rewards (RLVR) for objective tasks and RL from Human Feedback (RLHF) for subjective tasks. However, RLHF incurs high costs and potential reward-policy mismatch due to reliance on human preferences, while RLVR still wastes supervision by discarding rollouts and correctness signals after each update. To address these challenges, we introduce the Synergistic Policy And Reward Co-Evolving Framework (SPARK), an efficient, on-policy, and stable method that builds on RLVR. Instead of discarding rollouts and correctness data, SPARK recycles this valuable information to simultaneously train the model itself as a generative reward model. This auxiliary training uses a mix of objectives, such as pointwise reward score, pairwise comparison, and evaluation conditioned on further-reflection responses, to teach the model to evaluate and improve its own responses. Our process eliminates the need for a separate reward model and costly human preference data. SPARK creates a positive co-evolving feedback loop: improved reward accuracy yields better policy gradients, which in turn produce higher-quality rollouts that further refine the reward model. Our unified framework supports test-time scaling via self-reflection without external reward models and their associated costs. We show that SPARK achieves significant performance gains on multiple LLM and LVLM models and multiple reasoning, reward models, and general benchmarks. For example, SPARK-VL-7B achieves an average 9.7% gain on 7 reasoning benchmarks, 12.1% on 2 reward benchmarks, and 1.5% on 8 general benchmarks over the baselines, demonstrating robustness and broad generalization.

