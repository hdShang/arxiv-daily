---
layout: default
title: RM-R1: Reward Modeling as Reasoning
---

# RM-R1: Reward Modeling as Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02387" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02387v3</a>
  <a href="https://arxiv.org/pdf/2505.02387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02387v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02387v3', 'RM-R1: Reward Modeling as Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiusi Chen, Gaotang Li, Ziqi Wang, Bowen Jin, Cheng Qian, Yu Wang, Hongru Wang, Yu Zhang, Denghui Zhang, Tong Zhang, Hanghang Tong, Heng Ji

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-05 (更新: 2025-05-18)

**备注**: 25 pages, 8 figures

**🔗 代码/项目**: [GITHUB](https://github.com/RM-R1-UIUC/RM-R1)

---

## 💡 一句话要点

**提出基于推理的奖励建模方法以提升模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励建模` `推理能力` `强化学习` `可解释性` `自然语言处理` `模型对齐`

## 📋 核心要点

1. 现有的奖励建模方法在提供准确的奖励信号和可解释性方面存在不足，难以有效对齐模型与人类偏好。
2. 本文提出了推理奖励模型（ReasRMs），将奖励建模视为推理任务，设计了链式评分机制以增强模型的可解释性和性能。
3. RM-R1在多个奖励模型基准上表现出色，平均性能超越了更大规模的模型，提升幅度达到4.9%。

## 📝 摘要（中文）

奖励建模对于通过人类反馈的强化学习来对齐大型语言模型与人类偏好至关重要。为了提供准确的奖励信号，奖励模型应在赋分之前进行深度思考和可解释推理。本文提出了一种新的生成奖励模型——推理奖励模型（ReasRMs），将奖励建模视为推理任务。我们设计了一个面向推理的训练流程，并训练了一系列ReasRMs，RM-R1。RM-R1采用了链式评分机制，通过自生成样本级别的评分标准来评估候选响应。实验表明，我们的模型在三个奖励模型基准上实现了最先进的性能，超越了更大规模的开放权重模型和专有模型，提升幅度可达4.9%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有奖励建模方法在可解释性和准确性方面的不足，现有方法往往无法有效对齐大型语言模型与人类偏好。

**核心思路**：我们提出将奖励建模视为推理任务，通过引入推理能力来增强奖励模型的可解释性和性能，设计了链式评分机制以自生成评分标准。

**技术框架**：RM-R1的训练流程分为两个主要阶段：第一阶段为高质量推理链的蒸馏，第二阶段为使用可验证奖励的强化学习。整体架构包括推理链生成和候选响应评估两个模块。

**关键创新**：最重要的创新在于将奖励建模与推理结合，形成了新的推理奖励模型（ReasRMs），与传统方法相比，显著提升了模型的可解释性和性能。

**关键设计**：在训练过程中，我们采用了链式评分机制，允许模型自生成样本级别的评分标准，并通过强化学习优化模型参数，确保奖励信号的准确性和可验证性。

## 📊 实验亮点

实验结果显示，RM-R1在三个奖励模型基准上实现了最先进的性能，平均超越了更大规模的开放权重模型（如INF-ORM-Llama3.1-70B）和专有模型（如GPT-4o）达4.9%。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和人机交互等。通过提升奖励建模的准确性和可解释性，能够更好地对齐大型语言模型与人类偏好，进而提高模型在实际应用中的表现和用户满意度。

## 📄 摘要（原文）

> Reward modeling is essential for aligning large language models with human preferences through reinforcement learning from human feedback. To provide accurate reward signals, a reward model (RM) should stimulate deep thinking and conduct interpretable reasoning before assigning a score or a judgment. Inspired by recent advances of long chain-of-thought on reasoning-intensive tasks, we hypothesize and validate that integrating reasoning capabilities into reward modeling significantly enhances RMs interpretability and performance. To this end, we introduce a new class of generative reward models - Reasoning Reward Models (ReasRMs) - which formulate reward modeling as a reasoning task. We propose a reasoning-oriented training pipeline and train a family of ReasRMs, RM-R1. RM-R1 features a chain-of-rubrics (CoR) mechanism - self-generating sample-level chat rubrics or math/code solutions, and evaluating candidate responses against them. The training of RM-R1 consists of two key stages: (1) distillation of high-quality reasoning chains and (2) reinforcement learning with verifiable rewards. Empirically, our models achieve state-of-the-art performance across three reward model benchmarks on average, outperforming much larger open-weight models (e.g., INF-ORM-Llama3.1-70B) and proprietary ones (e.g., GPT-4o) by up to 4.9%. Beyond final performance, we perform thorough empirical analyses to understand the key ingredients of successful ReasRM training. To facilitate future research, we release six REASRM models along with code and data at https://github.com/RM-R1-UIUC/RM-R1.

