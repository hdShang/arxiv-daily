---
layout: default
title: "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning"
---

# GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16141" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16141v1</a>
  <a href="https://arxiv.org/pdf/2506.16141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16141v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16141v1', 'GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Chen, Yuying Ge, Rui Wang, Yixiao Ge, Junhao Cheng, Ying Shan, Xihui Liu

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-19

**备注**: Code released at: https://github.com/TencentARC/GRPO-CARE

---

## 💡 一句话要点

**提出GRPO-CARE以解决多模态推理中的一致性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `一致性奖励` `强化学习` `视频理解` `模型评估` `逻辑一致性` `后训练方法`

## 📋 核心要点

1. 现有的GRPO方法在多模态推理中存在逻辑一致性不足的问题，导致推理步骤与答案之间的关联性较低。
2. 本文提出GRPO-CARE框架，通过引入一致性奖励机制，优化答案的正确性和推理的一致性，避免了显式监督的需求。
3. 实验结果表明，GRPO-CARE在SEED-Bench-R1基准上表现优于标准GRPO，尤其在最具挑战性的评估上性能提升了6.7%。

## 📝 摘要（中文）

近年来，强化学习方法如结果监督的GRPO在大型语言模型的推理能力上取得了进展，但其在多模态语言模型中的适应性尚未得到探索。为了解决多模态后训练方法缺乏严格评估的问题，本文引入了SEED-Bench-R1基准，涵盖复杂的真实视频，要求平衡感知与推理。研究发现，标准GRPO在提高答案准确性的同时，逻辑一致性却降低，只有57.9%的一致性率。为此，本文提出了GRPO-CARE，一个关注一致性的强化学习框架，优化答案正确性与推理一致性，且无需显式监督。GRPO-CARE通过双重奖励机制显著提升了模型的表现，尤其在最难评估级别上提升了6.7%的性能，并在一致性上提高了24.5%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态语言模型在推理过程中逻辑一致性不足的问题。现有的GRPO方法虽然提高了答案的准确性，但却导致推理步骤与答案之间的逻辑关联性较低，表现出57.9%的低一致性率。

**核心思路**：GRPO-CARE框架的核心思路是引入一致性奖励机制，通过比较模型的推理与答案的可能性，优化推理路径的逻辑一致性，从而提升整体推理质量。

**技术框架**：GRPO-CARE的整体架构包括两个主要模块：基础奖励模块和适应性一致性奖励模块。基础奖励用于评估答案的正确性，而一致性奖励则通过与参考模型的比较来动态调整。

**关键创新**：GRPO-CARE的关键创新在于其双重奖励机制，特别是适应性一致性奖励的引入，使得模型能够在没有显式监督的情况下，优化推理过程的逻辑一致性。这与传统方法的KL惩罚机制形成了鲜明对比。

**关键设计**：在设计上，GRPO-CARE使用了一个缓慢演变的参考模型来计算一致性奖励，并替代了传统的KL惩罚。这种设计使得模型能够更好地探索推理路径，提高了逻辑一致性和整体性能。

## 📊 实验亮点

在SEED-Bench-R1基准测试中，GRPO-CARE相比标准GRPO在最难评估级别上提升了6.7%的性能，并在一致性方面提高了24.5%。此外，该方法展现出强大的迁移能力，能够在多种视频理解基准上改善模型性能。

## 🎯 应用场景

该研究的潜在应用领域包括视频理解、智能问答系统和多模态交互等。通过提升多模态语言模型的推理一致性，GRPO-CARE能够为实际应用提供更可靠的推理支持，进而推动智能系统的可解释性和鲁棒性发展。

## 📄 摘要（原文）

> Recent reinforcement learning approaches, such as outcome-supervised GRPO, have advanced Chain-of-Thought reasoning in large language models (LLMs), yet their adaptation to multimodal LLMs (MLLMs) is unexplored. To address the lack of rigorous evaluation for MLLM post-training methods, we introduce SEED-Bench-R1, a benchmark with complex real-world videos requiring balanced perception and reasoning. It offers a large training set and evaluates generalization across three escalating challenges: in-distribution, cross-environment, and cross-environment-task scenarios. Using SEED-Bench-R1, we find that standard GRPO, while improving answer accuracy, often reduces logical coherence between reasoning steps and answers, with only a 57.9% consistency rate. This stems from reward signals focusing solely on final answers, encouraging shortcuts, and strict KL penalties limiting exploration.To address this, we propose GRPO-CARE, a consistency-aware RL framework optimizing both answer correctness and reasoning coherence without explicit supervision. GRPO-CARE introduces a two-tiered reward: (1) a base reward for answer correctness, and (2) an adaptive consistency bonus, computed by comparing the model's reasoning-to-answer likelihood (via a slowly-evolving reference model) against group peers.This dual mechanism amplifies rewards for reasoning paths that are both correct and logically consistent. Replacing KL penalties with this adaptive bonus, GRPO-CARE outperforms standard GRPO on SEED-Bench-R1, achieving a 6.7% performance gain on the hardest evaluation level and a 24.5% improvement in consistency. It also shows strong transferability, improving model performance across diverse video understanding benchmarks. Our work contributes a systematically designed benchmark and a generalizable post-training framework, advancing the development of more interpretable and robust MLLMs.

