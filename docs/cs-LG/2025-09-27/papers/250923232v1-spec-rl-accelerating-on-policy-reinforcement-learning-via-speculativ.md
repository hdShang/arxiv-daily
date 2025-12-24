---
layout: default
title: "SPEC-RL: Accelerating On-Policy Reinforcement Learning via Speculative Rollouts"
---

# SPEC-RL: Accelerating On-Policy Reinforcement Learning via Speculative Rollouts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23232" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23232v1</a>
  <a href="https://arxiv.org/pdf/2509.23232.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23232v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23232v1', 'SPEC-RL: Accelerating On-Policy Reinforcement Learning via Speculative Rollouts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingshuai Liu, Ante Wang, Zijun Min, Liang Yao, Haibo Zhang, Yang Liu, Anxiang Zeng, Jinsong Su

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/ShopeeLLM/Spec-RL)

---

## 💡 一句话要点

**SPEC-RL：通过推测性Rollout加速On-Policy强化学习，提升LLM推理效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `推测性解码` `Rollout加速` `思维链推理`

## 📋 核心要点

1. 现有RLVR方法在LLM推理中面临rollout阶段计算成本高的挑战，限制了训练效率。
2. SPEC-RL通过重用先前轨迹片段作为推测性前缀，结合draft-and-verify机制，避免冗余计算。
3. 实验表明，SPEC-RL在多个数学推理基准测试中，将rollout时间减少2-3倍，且不影响策略质量。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地依赖于具有可验证奖励的强化学习（RLVR）来获得可靠的思维链推理。然而，训练过程仍然受到计算成本高昂的rollout阶段的限制。现有的加速方法，如并行化、目标和数据驱动的修改以及回放缓冲区，要么收益递减，要么引入偏差，要么忽略了迭代之间的冗余。我们发现，连续训练epoch的rollout经常共享大部分重叠片段，浪费了计算资源。为了解决这个问题，我们提出了SPEC-RL，这是一个将推测性解码与RL rollout过程相结合的新框架。SPEC-RL重用先前的轨迹片段作为推测性前缀，并通过draft-and-verify机制扩展它们，避免了冗余生成，同时确保了策略一致性。在包括GSM8K、MATH-500、OlympiadBench、MMLU-STEM等在内的各种数学推理和泛化基准上的实验表明，SPEC-RL在不影响策略质量的前提下，将rollout时间减少了2-3倍。作为一个纯粹的rollout阶段增强，SPEC-RL可以与主流算法（例如，PPO、GRPO、DAPO）无缝集成，为扩展大型推理模型的RLVR提供了一条通用且实用的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决在基于强化学习的大型语言模型训练中，rollout阶段计算开销过大的问题。现有方法，如并行化、修改目标函数或使用replay buffer，要么效果有限，要么引入偏差，并且忽略了连续迭代之间rollout轨迹的冗余性。

**核心思路**：SPEC-RL的核心思路是利用连续训练epoch之间rollout轨迹的相似性，通过推测性解码重用先前轨迹片段作为前缀，从而减少重复计算。类似于推测执行，该方法首先快速生成一个“草稿”（draft），然后通过验证机制确保策略的一致性。

**技术框架**：SPEC-RL框架主要包含以下几个阶段：1) 轨迹片段存储：存储先前epoch的rollout轨迹片段；2) 推测性前缀生成：从存储的片段中选择合适的片段作为当前rollout的推测性前缀；3) 草稿生成：基于推测性前缀，快速生成完整的rollout轨迹草稿；4) 验证：使用验证机制评估草稿轨迹的质量，并根据评估结果进行调整或重新生成。

**关键创新**：SPEC-RL的关键创新在于将推测性解码的思想引入到强化学习的rollout过程中。与传统方法相比，SPEC-RL避免了从头开始生成完整的rollout轨迹，而是通过重用和扩展先前的信息来加速rollout过程。这种方法在保证策略质量的同时，显著降低了计算成本。

**关键设计**：SPEC-RL的关键设计包括：1) 如何选择合适的推测性前缀：可能涉及到相似度度量和选择策略；2) 如何设计有效的验证机制：确保推测性rollout的策略一致性，避免引入偏差；3) 如何平衡推测的准确性和计算效率：需要权衡草稿生成的速度和验证的开销。

## 📊 实验亮点

实验结果表明，SPEC-RL在GSM8K、MATH-500、OlympiadBench和MMLU-STEM等多个数学推理和泛化基准测试中，能够将rollout时间减少2-3倍，同时保持与现有算法（如PPO、GRPO、DAPO）相当的策略性能。这表明SPEC-RL是一种高效且通用的rollout加速方法。

## 🎯 应用场景

SPEC-RL可广泛应用于需要大规模强化学习训练的大型语言模型，尤其是在需要复杂推理和决策的任务中，例如数学问题求解、代码生成和对话系统。该方法能够显著降低训练成本，加速模型迭代，并推动更强大、更高效的AI系统的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) increasingly rely on reinforcement learning with verifiable rewards (RLVR) to elicit reliable chain-of-thought reasoning. However, the training process remains bottlenecked by the computationally expensive rollout stage. Existing acceleration methods-such as parallelization, objective- and data-driven modifications, and replay buffers-either incur diminishing returns, introduce bias, or overlook redundancy across iterations. We identify that rollouts from consecutive training epochs frequently share a large portion of overlapping segments, wasting computation. To address this, we propose SPEC-RL, a novel framework that integrates SPECulative decoding with the RL rollout process. SPEC-RL reuses prior trajectory segments as speculative prefixes and extends them via a draft-and-verify mechanism, avoiding redundant generation while ensuring policy consistency. Experiments on diverse math reasoning and generalization benchmarks, including GSM8K, MATH-500, OlympiadBench, MMLU-STEM, and others, demonstrate that SPEC-RL reduces rollout time by 2-3x without compromising policy quality. As a purely rollout-stage enhancement, SPEC-RL integrates seamlessly with mainstream algorithms (e.g., PPO, GRPO, DAPO), offering a general and practical path to scale RLVR for large reasoning models. Our code is available at https://github.com/ShopeeLLM/Spec-RL

