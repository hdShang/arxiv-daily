---
layout: default
title: "Walk Before You Run! Concise LLM Reasoning via Reinforcement Learning"
---

# Walk Before You Run! Concise LLM Reasoning via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21178" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21178v1</a>
  <a href="https://arxiv.org/pdf/2505.21178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21178v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21178v1', 'Walk Before You Run! Concise LLM Reasoning via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingyang Song, Mao Zheng

**分类**: cs.CL

**发布日期**: 2025-05-27

**备注**: Ongoing Work

---

## 💡 一句话要点

**提出ConciseR以解决长链推理中的冗余问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `强化学习` `推理能力` `简洁性优化` `长链推理`

## 📋 核心要点

1. 现有推理模型在长链推理中存在过度思考，导致冗余和重复思维，影响推理效率。
2. 本文提出的ConciseR框架通过两阶段强化学习，分别优化推理能力和简洁性，解决冗余问题。
3. 实验结果显示，ConciseR在AIME 2024、MATH-500等基准测试中生成的推理响应更简洁，性能优于现有模型。

## 📝 摘要（中文）

随着大语言模型（LLMs）研究的深入，测试时扩展生成长度成为关键前沿。现有的推理模型在长链推理中存在过度思考现象，导致冗余和重复思维。为了解决这一问题，本文提出了一种简单有效的两阶段强化学习框架ConciseR，旨在实现简洁推理。第一阶段通过Group Relative Policy Optimization（GRPO++）激励模型的推理能力，第二阶段通过Length-aware Group Relative Policy Optimization（L-GRPO）明确强制简洁性。实验结果表明，ConciseR在多个基准测试中优于现有的推理模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大语言模型在长链推理中出现的冗余和重复思维问题，影响推理的效率和质量。

**核心思路**：提出ConciseR框架，通过两阶段强化学习，第一阶段专注于提升推理能力，第二阶段强调简洁性，以减少冗余。

**技术框架**：ConciseR框架分为两个阶段：第一阶段使用GRPO++进行推理能力优化，第二阶段使用L-GRPO进行简洁性优化，确保在所有样本回合正确后再优化响应长度。

**关键创新**：ConciseR的创新在于其两阶段的设计，特别是“走路再跑”的原则，确保在推理能力提升的基础上再进行简洁性优化，与现有方法形成鲜明对比。

**关键设计**：在GRPO++阶段，采用动态采样和clip-higher组件；在L-GRPO阶段，明确设置简洁性目标，优化损失函数以强化简洁性。

## 📊 实验亮点

实验结果表明，ConciseR在AIME 2024、MATH-500、AMC 2023等多个基准测试中表现优异，生成的推理响应更为简洁，且在性能上超越了现有的最先进推理模型，显示出显著的提升幅度。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动问答系统和智能助手等，能够提高大语言模型在复杂推理任务中的表现，减少冗余信息的生成，提升用户体验。未来可能在更广泛的自然语言处理任务中发挥重要作用。

## 📄 摘要（原文）

> As test-time scaling becomes a pivotal research frontier in Large Language Models (LLMs) development, contemporary and advanced post-training methodologies increasingly focus on extending the generation length of long Chain-of-Thought (CoT) responses to enhance reasoning capabilities toward DeepSeek R1-like performance. However, recent studies reveal a persistent overthinking phenomenon in state-of-the-art reasoning models, manifesting as excessive redundancy or repetitive thinking patterns in long CoT responses. To address this issue, in this paper, we propose a simple yet effective two-stage reinforcement learning framework for achieving concise reasoning in LLMs, named ConciseR. Specifically, the first stage, using more training steps, aims to incentivize the model's reasoning capabilities via Group Relative Policy Optimization with clip-higher and dynamic sampling components (GRPO++), and the second stage, using fewer training steps, explicitly enforces conciseness and improves efficiency via Length-aware Group Relative Policy Optimization (L-GRPO). Significantly, ConciseR only optimizes response length once all rollouts of a sample are correct, following the "walk before you run" principle. Extensive experimental results demonstrate that our ConciseR model, which generates more concise CoT reasoning responses, outperforms recent state-of-the-art reasoning models with zero RL paradigm across AIME 2024, MATH-500, AMC 2023, Minerva, and Olympiad benchmarks.

