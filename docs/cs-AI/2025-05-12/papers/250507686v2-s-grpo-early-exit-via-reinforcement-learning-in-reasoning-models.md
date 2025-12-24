---
layout: default
title: S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models
---

# S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07686" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07686v2</a>
  <a href="https://arxiv.org/pdf/2505.07686.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07686v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07686v2', 'S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muzhi Dai, Chenxu Yang, Qingyi Si

**分类**: cs.AI, cs.LG

**发布日期**: 2025-05-12 (更新: 2025-05-17)

---

## 💡 一句话要点

**提出S-GRPO以解决推理模型中的过度思考问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理模型` `强化学习` `链式思维` `过度思考` `序列长度减少` `准确性提升` `奖励机制` `智能问答`

## 📋 核心要点

1. 现有推理模型在链式思维生成中存在过度思考的冗余问题，导致推理效率低下。
2. 本文提出S-GRPO，通过串行选择推理路径中的时间位置，促进早期思考退出，减少冗余。
3. 实验结果显示，S-GRPO在多个基准测试中显著减少了序列长度，并提高了模型的准确性。

## 📝 摘要（中文）

随着测试时扩展成为大型语言模型社区的研究热点，先进的后训练方法越来越强调延长链式思维（CoT）生成长度，从而增强推理能力。然而，近期研究表明，推理模型（甚至Qwen3）在CoT生成中普遍存在过度思考的冗余问题。本文提出了一种新颖的强化学习范式——串行组衰减奖励策略优化（S-GRPO），使模型能够隐式评估中间推理步骤的充分性，从而促进CoT生成中的早期退出。与并行组的GRPO不同，S-GRPO仅采样一条推理路径，并串行选择路径中的多个时间位置进行思考退出和直接生成答案。实证评估表明，S-GRPO与Qwen3和Deepseek-distill等最先进的推理模型兼容，在GSM8K、AIME 2024、AMC 2023、MATH-500和GPQA Diamond等多项基准测试中，S-GRPO实现了序列长度的显著减少（35.4%-61.1%），同时提高了准确性（绝对提升0.72%-6.08%）。

## 🔬 方法详解

**问题定义**：本文旨在解决推理模型在链式思维生成中存在的过度思考问题，现有的强化学习方法未能有效调节中间推理过程，导致冗余思考。

**核心思路**：S-GRPO通过串行选择推理路径中的多个时间位置，允许模型在适当时机提前退出思考，从而提高生成的准确性和简洁性。

**技术框架**：S-GRPO的整体架构包括一个推理路径采样模块和一个奖励机制模块。模型首先选择一条推理路径，然后在该路径上选择多个时间位置进行思考退出。

**关键创新**：S-GRPO的核心创新在于其串行组的设计，与传统的并行组方法相比，能够更有效地评估中间推理步骤的充分性，减少冗余思考。

**关键设计**：在奖励机制中，对于正确答案，奖励会根据推理路径的退出位置逐渐减少，从而鼓励模型在适当时机终止思考。

## 📊 实验亮点

实验结果显示，S-GRPO在多个基准测试中实现了35.4%-61.1%的序列长度减少，同时准确性提升了0.72%-6.08%。这些结果表明，S-GRPO在推理模型的性能上具有显著的改进，尤其是在处理复杂推理任务时。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、对话生成和教育辅助工具等。通过提高推理模型的效率和准确性，S-GRPO能够在实际应用中提供更快速和可靠的响应，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> As Test-Time Scaling emerges as an active research focus in the large language model community, advanced post-training methods increasingly emphasize extending chain-of-thought (CoT) generation length, thereby enhancing reasoning capabilities to approach Deepseek R1-like reasoning models. However, recent studies reveal that reasoning models (even Qwen3) consistently exhibit excessive thought redundancy in CoT generation. This overthinking issue arises from the inherent limitations of conventional outcome-reward reinforcement learning, which systematically overlooks the regulation of intermediate reasoning processes. This paper introduces Serial-Group Decaying-Reward Policy Optimization (S-GRPO), a novel reinforcement learning paradigm that enables models to implicitly evaluate the sufficiency of intermediate reasoning steps, thereby facilitating early exit in CoT generation. Unlike GRPO, which samples multiple possible reasoning paths in parallel (parallel group), S-GRPO only samples one reasoning path and serially selects multiple temporal positions from the path to exit thinking and directly generate answers (serial group). For correct answers within a serial group, rewards gradually decrease based on the exit positions along the reasoning path from front to back. This design encourages the model to produce more accurate and concise thoughts, while also incentivizing early thinking termination when appropriate. Empirical evaluations demonstrate that S-GRPO is compatible with state-of-the-art reasoning models, including Qwen3 and Deepseek-distill. Across diverse benchmarks such as GSM8K, AIME 2024, AMC 2023, MATH-500, and GPQA Diamond, S-GRPO achieves a substantial reduction in sequence length (35.4% - 61.1%) while simultaneously improving accuracy (absolute 0.72% - 6.08%).

