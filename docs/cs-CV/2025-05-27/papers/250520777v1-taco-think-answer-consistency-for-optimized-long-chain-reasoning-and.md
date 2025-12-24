---
layout: default
title: "TACO: Think-Answer Consistency for Optimized Long-Chain Reasoning and Efficient Data Learning via Reinforcement Learning in LVLMs"
---

# TACO: Think-Answer Consistency for Optimized Long-Chain Reasoning and Efficient Data Learning via Reinforcement Learning in LVLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20777" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20777v1</a>
  <a href="https://arxiv.org/pdf/2505.20777.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20777v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20777v1', 'TACO: Think-Answer Consistency for Optimized Long-Chain Reasoning and Efficient Data Learning via Reinforcement Learning in LVLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhehan Kan, Yanlin Liu, Kun Yin, Xinghua Jiang, Xin Li, Haoyu Cao, Yinsong Liu, Deqiang Jiang, Xing Sun, Qingmin Liao, Wenming Yang

**分类**: cs.CV

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出TACO以解决长链推理中的一致性与学习效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长链推理` `视觉推理` `强化学习` `多模态学习` `数据学习效率`

## 📋 核心要点

1. 现有方法在多模态推理中存在推理与答案不一致、模型不稳定及低效学习等问题。
2. TACO通过引入思考-答案一致性和回滚重采样策略，确保推理过程的稳定性和答案的准确性。
3. 在REC和VQA任务上，微调LVLMs后性能显著提升，验证了TACO的有效性。

## 📝 摘要（中文）

DeepSeek R1在大型语言模型的复杂推理方面取得了显著进展。然而，现有方法在多模态设置中复制R1的推理能力时面临诸多挑战，包括推理与最终答案之间的不一致性、长链探索中的模型不稳定性和崩溃，以及数据学习效率低下。为了解决这些问题，本文提出了TACO，这是一种新颖的视觉推理强化学习算法。TACO引入了思考-答案一致性，确保答案与深思熟虑的推理紧密结合。此外，采用回滚重采样策略以稳定长链探索，并引入自适应学习计划以优化数据效率。实验结果表明，微调LVLMs在REC和VQA任务上显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长链推理中的一致性问题，现有方法在推理与最终答案之间存在显著不一致，导致模型不稳定和学习效率低下。

**核心思路**：TACO的核心思想是引入思考-答案一致性，确保推理过程中的答案与思考过程紧密结合，从而提高推理的准确性和稳定性。

**技术框架**：TACO的整体架构包括三个主要模块：思考-答案一致性模块、回滚重采样策略模块和自适应学习计划模块。思考-答案一致性模块确保推理与答案的一致性，回滚重采样策略模块用于稳定长链探索，自适应学习计划模块则优化数据学习效率。

**关键创新**：TACO的主要创新在于思考-答案一致性和回滚重采样策略的结合，这与现有方法的本质区别在于更好地解决了推理过程中的不稳定性和答案不一致的问题。

**关键设计**：TACO采用自适应学习计划，重点关注中等难度样本的学习，以提高数据效率。此外，设计了测试时分辨率缩放方案，以应对推理过程中因分辨率变化导致的性能下降，同时平衡计算开销。

## 📊 实验亮点

在REC和VQA任务上，TACO通过微调LVLMs实现了显著的性能提升，具体表现为在标准基准测试中，相较于基线方法，性能提升幅度达到XX%（具体数据未知），验证了其有效性和优越性。

## 🎯 应用场景

TACO的研究成果在视觉推理、自然语言处理和多模态学习等领域具有广泛的应用潜力。其创新的方法可以提升智能助手、自动问答系统和图像理解等技术的性能，推动相关领域的进一步发展与应用。

## 📄 摘要（原文）

> DeepSeek R1 has significantly advanced complex reasoning for large language models (LLMs). While recent methods have attempted to replicate R1's reasoning capabilities in multimodal settings, they face limitations, including inconsistencies between reasoning and final answers, model instability and crashes during long-chain exploration, and low data learning efficiency. To address these challenges, we propose TACO, a novel reinforcement learning algorithm for visual reasoning. Building on Generalized Reinforcement Policy Optimization (GRPO), TACO introduces Think-Answer Consistency, which tightly couples reasoning with answer consistency to ensure answers are grounded in thoughtful reasoning. We also introduce the Rollback Resample Strategy, which adaptively removes problematic samples and reintroduces them to the sampler, enabling stable long-chain exploration and future learning opportunities. Additionally, TACO employs an adaptive learning schedule that focuses on moderate difficulty samples to optimize data efficiency. Furthermore, we propose the Test-Time-Resolution-Scaling scheme to address performance degradation due to varying resolutions during reasoning while balancing computational overhead. Extensive experiments on in-distribution and out-of-distribution benchmarks for REC and VQA tasks show that fine-tuning LVLMs leads to significant performance improvements.

