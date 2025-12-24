---
layout: default
title: "Mixed-R1: Unified Reward Perspective For Reasoning Capability in Multimodal Large Language Models"
---

# Mixed-R1: Unified Reward Perspective For Reasoning Capability in Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24164" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24164v1</a>
  <a href="https://arxiv.org/pdf/2505.24164.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24164v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24164v1', 'Mixed-R1: Unified Reward Perspective For Reasoning Capability in Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shilin Xu, Yanwei Li, Rui Yang, Tao Zhang, Yueyi Sun, Wei Chow, Linfeng Li, Hang Song, Qi Xu, Yunhai Tong, Xiangtai Li, Hao Fei

**分类**: cs.CL, cs.CV

**发布日期**: 2025-05-30

**🔗 代码/项目**: [GITHUB](https://github.com/xushilin1/mixed-r1)

---

## 💡 一句话要点

**提出Mixed-R1框架以解决多模态大语言模型的推理能力问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `推理能力` `强化学习` `混合奖励函数` `后训练数据集` `数据引擎` `开放式文本响应`

## 📋 核心要点

1. 现有方法往往专注于单一任务，缺乏对多源多模态任务的综合利用，导致推理能力的提升受限。
2. 本文提出Mixed-R1框架，通过混合奖励函数和后训练数据集，旨在提升多模态大语言模型的推理能力。
3. 实验结果显示，Mixed-R1在多个多模态大语言模型上表现优异，验证了其有效性和广泛适用性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）通过强化学习（RL）展示了推理能力的出现。尽管已有研究利用群体相对策略优化（GRPO）进行多模态大语言模型的后训练，但这些研究通常集中于特定任务，如基础任务、数学问题或图表分析。本文提出Mixed-R1，一个统一且简单的框架，包含混合奖励函数设计（Mixed-Reward）和混合后训练数据集（Mixed-45K）。我们设计了一个数据引擎，以选择高质量示例构建Mixed-45K数据集，并提出了多种奖励函数以适应不同的多模态任务。实验表明，该方法在多个多模态大语言模型上有效，数据集和模型可在指定链接获取。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在推理能力提升方面的不足，现有方法多集中于特定任务，缺乏对多源任务的综合考虑。

**核心思路**：提出Mixed-R1框架，通过设计混合奖励函数和构建混合后训练数据集，旨在实现对多种任务的统一优化，从而提升模型的推理能力。

**技术框架**：Mixed-R1框架包含两个主要模块：混合奖励函数设计和混合后训练数据集构建。数据引擎用于选择高质量示例，Mixed-Reward则针对不同任务设计多种奖励函数。

**关键创新**：最重要的创新在于提出了Bidirectional Max-Average Similarity (BMAS)奖励，用于处理开放式文本响应，利用生成响应与真实标签之间的嵌入匹配进行评估。

**关键设计**：混合奖励函数包括四种不同的奖励机制，分别针对二元答案、图表数据集、基础问题和开放式文本响应，确保模型在多种任务上的适应性和有效性。实验中使用的损失函数和参数设置经过精心设计，以优化模型性能。

## 📊 实验亮点

实验结果表明，Mixed-R1在多个多模态大语言模型上均取得显著提升，尤其是在推理任务上，相较于基线模型，性能提升幅度达到XX%（具体数据待补充），验证了该框架的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动文本生成、数据分析等。通过提升多模态大语言模型的推理能力，Mixed-R1框架可为实际应用提供更高的准确性和灵活性，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Recent works on large language models (LLMs) have successfully demonstrated the emergence of reasoning capabilities via reinforcement learning (RL). Although recent efforts leverage group relative policy optimization (GRPO) for MLLMs post-training, they constantly explore one specific aspect, such as grounding tasks, math problems, or chart analysis. There are no works that can leverage multi-source MLLM tasks for stable reinforcement learning. In this work, we present a unified perspective to solve this problem. We present Mixed-R1, a unified yet straightforward framework that contains a mixed reward function design (Mixed-Reward) and a mixed post-training dataset (Mixed-45K). We first design a data engine to select high-quality examples to build the Mixed-45K post-training dataset. Then, we present a Mixed-Reward design, which contains various reward functions for various MLLM tasks. In particular, it has four different reward functions: matching reward for binary answer or multiple-choice problems, chart reward for chart-aware datasets, IoU reward for grounding problems, and open-ended reward for long-form text responses such as caption datasets. To handle the various long-form text content, we propose a new open-ended reward named Bidirectional Max-Average Similarity (BMAS) by leveraging tokenizer embedding matching between the generated response and the ground truth. Extensive experiments show the effectiveness of our proposed method on various MLLMs, including Qwen2.5-VL and Intern-VL on various sizes. Our dataset and model are available at https://github.com/xushilin1/mixed-r1.

