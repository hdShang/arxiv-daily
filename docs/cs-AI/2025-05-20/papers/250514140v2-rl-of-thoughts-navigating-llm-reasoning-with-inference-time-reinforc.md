---
layout: default
title: RL of Thoughts: Navigating LLM Reasoning with Inference-time Reinforcement Learning
---

# RL of Thoughts: Navigating LLM Reasoning with Inference-time Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14140" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14140v2</a>
  <a href="https://arxiv.org/pdf/2505.14140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14140v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14140v2', 'RL of Thoughts: Navigating LLM Reasoning with Inference-time Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianyue Hao, Sibo Li, Jian Yuan, Yong Li

**分类**: cs.AI

**发布日期**: 2025-05-20 (更新: 2025-09-25)

---

## 💡 一句话要点

**提出RL-of-Thoughts以增强大语言模型推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理能力` `强化学习` `逻辑模块` `动态选择` `任务适应性` `迁移学习`

## 📋 核心要点

1. 现有推理技术如Chain/Tree/Graph-of-Thought(s)缺乏适应性，无法针对不同任务进行优化。
2. 提出RL-of-Thoughts（RLoT），通过强化学习训练导航模型，动态选择和组合逻辑模块以增强推理能力。
3. 实验结果显示，RLoT在多个基准上超越现有技术，提升幅度可达13.4%，且具有良好的迁移能力。

## 📝 摘要（中文）

尽管大语言模型（LLMs）迅速发展，但其基于token的自回归特性限制了复杂推理能力。为提升LLM推理，推理时技术如Chain/Tree/Graph-of-Thought(s)通过复杂逻辑结构引导推理，表现出良好的性价比。然而，这些手动预定义的框架缺乏适应性。为此，本文提出RL-of-Thoughts（RLoT），通过强化学习训练轻量级导航模型，动态选择适合的逻辑模块，结合成任务特定的逻辑结构。实验表明，RLoT在多个推理基准上超越现有技术，且其导航模型在参数少于3K的情况下，使得小于10B的LLM可与100B规模的模型相媲美。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理过程中由于自回归特性导致的复杂推理能力不足的问题。现有的推理技术虽然有效，但缺乏针对特定任务的适应性，导致性能受限。

**核心思路**：论文提出RL-of-Thoughts（RLoT），通过强化学习训练一个轻量级的导航模型，使其能够根据问题特征动态选择和组合逻辑模块，从而提升LLM的推理能力。

**技术框架**：RLoT的整体架构包括一个RL导航模型和五个基本逻辑模块。导航模型在推理过程中根据输入特征选择合适的逻辑模块，并将其组合成任务特定的逻辑结构。

**关键创新**：RLoT的主要创新在于通过强化学习实现了逻辑模块的动态选择与组合，显著提高了推理的灵活性和适应性。这与传统的手动预定义框架形成鲜明对比。

**关键设计**：导航模型的参数设置少于3K，采用轻量级设计，确保在不增加计算负担的情况下提升推理能力。损失函数和训练策略经过精心设计，以优化模型在不同任务上的表现。

## 📊 实验亮点

实验结果显示，RLoT在多个推理基准（如AIME、MATH、GPQA等）上超越了现有的推理技术，性能提升幅度可达13.4%。此外，RLoT的轻量级导航模型使得小于10B的LLM在推理能力上可与100B规模的模型相媲美，展现出强大的迁移能力。

## 🎯 应用场景

该研究的潜在应用领域包括教育、医疗、金融等需要复杂推理的场景。通过提升LLM的推理能力，RLoT能够在这些领域提供更准确的决策支持和智能服务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Despite rapid advancements in large language models (LLMs), the token-level autoregressive nature constrains their complex reasoning capabilities. To enhance LLM reasoning, inference-time techniques, including Chain/Tree/Graph-of-Thought(s), successfully improve the performance, as they are fairly cost-effective by guiding reasoning through sophisticated logical structures without modifying LLMs' parameters. However, these manually predefined, task-agnostic frameworks are applied uniformly across diverse tasks, lacking adaptability. To improve this, we propose RL-of-Thoughts (RLoT), where we train a lightweight navigator model with reinforcement learning (RL) to adaptively enhance LLM reasoning at inference time. Specifically, we design five basic logic blocks from the perspective of human cognition. During the reasoning process, the trained RL navigator dynamically selects the suitable logic blocks and combines them into task-specific logical structures according to problem characteristics. Experiments across multiple reasoning benchmarks (AIME, MATH, GPQA, etc.) with multiple LLMs (GPT, Llama, Qwen, and DeepSeek) illustrate that RLoT outperforms established inference-time techniques by up to 13.4%. Remarkably, with less than 3K parameters, our RL navigator is able to make sub-10B LLMs comparable to 100B-scale counterparts. Moreover, the RL navigator demonstrates strong transferability: a model trained on one specific LLM-task pair can effectively generalize to unseen LLMs and tasks. Our code is open-source at https://anonymous.4open.science/r/RL-LLM-Reasoning-1A30 for reproducibility.

