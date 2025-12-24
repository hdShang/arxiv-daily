---
layout: default
title: "CC-LEARN: Cohort-based Consistency Learning"
---

# CC-LEARN: Cohort-based Consistency Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15662" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15662v1</a>
  <a href="https://arxiv.org/pdf/2506.15662.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15662v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15662v1', 'CC-LEARN: Cohort-based Consistency Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Ye, Shaswat Shrivastava, Zhaonan Li, Jacob Dineen, Shijie Lu, Avneet Ahuja, Ming Shen, Zhikun Xu, Ben Zhou

**分类**: cs.CL

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出CC-Learn以提升大语言模型推理一致性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `一致性学习` `强化学习` `推理稳定性` `问题分解`

## 📋 核心要点

1. 现有的大语言模型在推理一致性和稳健性方面表现不佳，导致其在复杂任务中的可靠性不足。
2. 本文提出的CC-Learn框架通过强化学习，利用相似问题的队列来提升模型的推理一致性，优化了模型的推理模式。
3. 在多个推理基准测试中，CC-Learn显著提高了模型的准确性和推理稳定性，相较于预训练和监督微调基线均有提升。

## 📝 摘要（中文）

大语言模型在许多任务中表现出色，但在一致性和稳健推理方面仍存在挑战。本文提出了基于队列的一致性学习（CC-Learn）框架，通过对来自共享程序抽象的相似问题队列进行训练，提升了大语言模型的推理可靠性。为强制执行队列级一致性，定义了一个复合目标，结合了队列准确性、有效问题分解的检索奖励和对琐碎或无效查找的拒绝惩罚，这些都可以通过强化学习直接优化。实验结果表明，CC-Learn在多个推理基准（如ARC-Challenge和StrategyQA）上显著提高了准确性和推理稳定性，证明了队列级强化学习有效增强了大语言模型的推理一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理过程中存在的一致性和稳健性不足的问题。现有方法往往无法有效处理复杂问题，导致推理结果不稳定。

**核心思路**：CC-Learn通过强化学习框架，利用相似问题的队列进行训练，强制模型在队列内保持一致的推理模式，从而提升推理的可靠性。

**技术框架**：该方法的整体架构包括三个主要模块：队列准确性评估、检索奖励机制和拒绝惩罚机制。通过优化这些模块的复合目标，模型能够在推理过程中保持一致性。

**关键创新**：CC-Learn的主要创新在于引入了队列级别的一致性学习，通过强化学习直接优化复合目标，而非依赖传统的监督微调方法，这使得模型能够更好地处理复杂推理任务。

**关键设计**：在损失函数设计上，结合了队列准确性和检索奖励，同时引入了对无效查找的惩罚机制，以引导模型学习有效的推理策略。

## 📊 实验亮点

实验结果显示，CC-Learn在ARC-Challenge和StrategyQA等推理基准上，相较于预训练和监督微调基线，准确性和推理稳定性均有显著提升，具体提升幅度达到XX%（具体数据需根据实验结果填写）。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动问答系统和智能助手等，能够提升这些系统在复杂推理任务中的表现。通过增强推理一致性，CC-Learn有助于提高用户体验和系统的可靠性，未来可能在更多实际应用中发挥重要作用。

## 📄 摘要（原文）

> Large language models excel at many tasks but still struggle with consistent, robust reasoning. We introduce Cohort-based Consistency Learning (CC-Learn), a reinforcement learning framework that improves the reliability of LLM reasoning by training on cohorts of similar questions derived from shared programmatic abstractions. To enforce cohort-level consistency, we define a composite objective combining cohort accuracy, a retrieval bonus for effective problem decomposition, and a rejection penalty for trivial or invalid lookups that reinforcement learning can directly optimize, unlike supervised fine-tuning. Optimizing this reward guides the model to adopt uniform reasoning patterns across all cohort members. Experiments on challenging reasoning benchmarks (including ARC-Challenge and StrategyQA) show that CC-Learn boosts both accuracy and reasoning stability over pretrained and SFT baselines. These results demonstrate that cohort-level RL effectively enhances reasoning consistency in LLMs.

