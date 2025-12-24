---
layout: default
title: "Harnessing Negative Signals: Reinforcement Distillation from Teacher Data for LLM Reasoning"
---

# Harnessing Negative Signals: Reinforcement Distillation from Teacher Data for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24850" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24850v2</a>
  <a href="https://arxiv.org/pdf/2505.24850.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24850v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24850v2', 'Harnessing Negative Signals: Reinforcement Distillation from Teacher Data for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuyao Xu, Cheng Peng, Jiangxuan Long, Weidi Xu, Wei Chu, Yuan Qi

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-30 (更新: 2025-12-14)

**备注**: 22 pages, 10 figures. Code available at https://github.com/Tim-Siu/reinforcement-distillation

---

## 💡 一句话要点

**提出负信号蒸馏方法以提升大语言模型推理性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `负信号蒸馏` `大语言模型` `推理性能` `监督微调` `强化学习`

## 📋 核心要点

1. 现有的模型蒸馏方法通常忽视错误推理轨迹，导致潜在的有价值数据未被利用。
2. 本文提出了一种两阶段训练策略，首先在正轨迹上进行监督微调，然后结合正负轨迹进行精炼。
3. 实验结果表明，Qwen-REDI-1.5B模型在MATH-500上取得了83.1%的得分，显示出显著的数据效率提升。

## 📝 摘要（中文）

近年来，模型蒸馏的进展表明，来自先进推理模型的数据可以有效训练较小的学生模型。然而，标准实践往往忽视错误推理轨迹，这些数据虽有价值却未被充分利用。本文探讨如何在离线环境中有效利用正负蒸馏推理轨迹，以最大化大语言模型的推理性能。我们采用两阶段训练策略：首先在正轨迹上进行监督微调（SFT），然后在正负轨迹上进行精炼阶段。我们发现，简单的REINFORCE风格目标，即我们称之为强化蒸馏（REDI）目标，在蒸馏上下文中优于现有的偏好优化方法，如DPO和SimPO。我们的实证评估展示了该方法的有效性。值得注意的是，我们的Qwen-REDI-1.5B模型在仅使用131k轨迹的情况下，在MATH-500上取得了83.1%的得分，其性能与在800k专有数据上训练的DeepSeek-R1-Distill-Qwen-1.5B模型相当。这一结果展示了利用之前被丢弃的负轨迹的显著数据效率。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效利用正负蒸馏推理轨迹以提升大语言模型推理性能的问题。现有方法通常忽视错误推理轨迹，导致潜在信息的丢失。

**核心思路**：我们提出了一种两阶段的训练策略，首先在正轨迹上进行监督微调（SFT），然后在精炼阶段结合正负轨迹进行训练，以充分利用所有可用数据。

**技术框架**：整体架构包括两个主要阶段：第一阶段为监督微调，专注于正轨迹；第二阶段为精炼阶段，结合正负轨迹进行训练。

**关键创新**：最重要的技术创新是提出了强化蒸馏（REDI）目标，该目标在蒸馏上下文中优于传统的偏好优化方法，如DPO和SimPO。

**关键设计**：在训练过程中，我们设置了特定的损失函数以平衡正负轨迹的影响，并设计了适应性学习率以优化模型性能。

## 📊 实验亮点

实验结果显示，Qwen-REDI-1.5B模型在MATH-500上取得了83.1%的得分，表现与在800k专有数据上训练的模型相当，展示了在数据效率上的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和教育技术等。通过有效利用负信号，模型可以在更少的数据上实现更高的推理性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent advances in model distillation show that data from advanced reasoning models can effectively train smaller student models. However, standard practices discard incorrect reasoning traces -- valuable, yet underutilized data. This paper addresses the critical question: How can both positive and negative distilled reasoning traces be effectively leveraged to maximize LLM reasoning performance in an offline setting? We employ a two-stage training recipe: first, Supervised Fine-Tuning (SFT) on positive traces, followed by a refinement stage using both positive and negative traces. We find that a simple REINFORCE-style objective, which we term the Reinforcement Distillation (REDI) objective, outperforms established preference optimization methods like DPO and SimPO in this distillation context. Our empirical evaluations demonstrate the effectiveness of this approach. Notably, our Qwen-REDI-1.5B model, trained on just 131k traces from the open Open-R1 dataset, achieves an 83.1% score on MATH-500. Its performance matches that of DeepSeek-R1-Distill-Qwen-1.5B, a model trained on 800k proprietary data. This result showcases the remarkable data efficiency of utilizing previously discarded negative traces.

