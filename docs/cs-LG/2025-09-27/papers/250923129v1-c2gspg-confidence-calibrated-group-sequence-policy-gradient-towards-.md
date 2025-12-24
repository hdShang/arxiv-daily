---
layout: default
title: "C$^2$GSPG: Confidence-calibrated Group Sequence Policy Gradient towards Self-aware Reasoning"
---

# C$^2$GSPG: Confidence-calibrated Group Sequence Policy Gradient towards Self-aware Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23129" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23129v1</a>
  <a href="https://arxiv.org/pdf/2509.23129.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23129v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23129v1', 'C$^2$GSPG: Confidence-calibrated Group Sequence Policy Gradient towards Self-aware Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Liu, Shuo Wang, Hongteng Xu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/HaotianLiu123/CCGSPG)

---

## 💡 一句话要点

**提出C$^2$GSPG，解决强化学习推理模型中的过度自信问题，提升自知推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `推理模型` `置信度校准` `策略梯度` `自知推理`

## 📋 核心要点

1. 现有基于强化学习的推理模型，如GRPO，存在过度自信问题，阻碍了模型实现自知推理。
2. C$^2$GSPG通过组序列策略梯度框架消除token级别偏差，并引入置信度校准正则化器，将模型置信度与序列奖励对齐。
3. 实验表明，C$^2$GSPG在逻辑和数学推理任务中，显著提升了推理准确性，并有效校准了模型置信度。

## 📝 摘要（中文）

本文提出了一种置信度校准的组序列策略梯度方法C$^2$GSPG，旨在提升推理性能并抑制过度自信，从而实现自知推理模型。该方法基于组序列策略梯度(GSPG)框架，消除了GRPO及其变体中常见的token级别偏差。通过使用归一化的序列级别概率定义模型置信度，并应用交叉熵正则化器将模型置信度校准到序列奖励。研究表明，置信度校准正则化器和GSPG在二元奖励下协同工作。对于非二元奖励，采用非线性奖励归一化和自适应正则化器裁剪，以减轻两个目标之间的潜在冲突。在逻辑和数学推理任务中对大型语言模型进行后训练，实验结果表明C$^2$GSPG在推理准确性和置信度校准方面均优于现有方法。代码已开源。

## 🔬 方法详解

**问题定义**：现有基于强化学习的推理模型，特别是Group Relative Policy Optimization (GRPO)及其变体，在训练过程中容易产生过度自信的问题。这种过度自信会导致模型在推理时做出错误的判断，并且无法准确评估自身推理结果的可靠性，从而阻碍了自知推理能力的提升。现有方法通常在token级别进行策略优化，容易引入偏差，影响整体推理效果。

**核心思路**：C$^2$GSPG的核心思路是通过置信度校准来解决过度自信问题。具体来说，该方法首先使用序列级别的概率来定义模型对于每个推理问题的置信度，然后通过一个交叉熵正则化器，将这个置信度校准到序列的奖励。这样做的目的是让模型在获得高奖励的序列上更加自信，而在获得低奖励的序列上更加谨慎，从而提升模型的自知能力。

**技术框架**：C$^2$GSPG包含以下几个主要组成部分：1) Group Sequence Policy Gradient (GSPG)框架：用于学习推理模型，消除token级别的偏差。2) 置信度定义：使用归一化的序列级别概率来定义模型对于每个推理问题的置信度。3) 置信度校准正则化器：使用交叉熵损失函数，将模型置信度校准到序列的奖励。4) 非线性奖励归一化和自适应正则化器裁剪：用于处理非二元奖励的情况，减轻置信度校准和策略优化目标之间的冲突。

**关键创新**：C$^2$GSPG的关键创新在于提出了置信度校准正则化器，并将其与GSPG框架相结合。与现有方法不同，C$^2$GSPG直接在序列级别进行置信度校准，避免了token级别偏差的影响。此外，C$^2$GSPG还针对非二元奖励的情况，提出了非线性奖励归一化和自适应正则化器裁剪等技术，进一步提升了方法的鲁棒性和适用性。

**关键设计**：在二元奖励情况下，置信度校准正则化器和GSPG的目标函数梯度方向一致，可以协同优化。对于非二元奖励，采用非线性奖励归一化（具体形式未知）来调整奖励分布，并使用自适应正则化器裁剪（具体裁剪策略未知）来限制正则化器的影响，避免与策略优化目标产生冲突。交叉熵损失函数的具体形式为标准形式，用于衡量模型置信度与目标奖励之间的差异。

## 📊 实验亮点

实验结果表明，C$^2$GSPG在逻辑和数学推理任务中，显著优于现有方法。具体来说，在某些任务上，C$^2$GSPG的推理准确率提升了X%（具体数据未知），并且在置信度校准方面也取得了显著的改进。这些结果表明，C$^2$GSPG能够有效地提升模型的推理能力和自知能力。

## 🎯 应用场景

C$^2$GSPG可应用于各种需要逻辑推理和数学推理的场景，例如智能问答、知识图谱推理、代码生成等。通过提升模型的推理准确性和置信度校准能力，可以提高这些应用系统的可靠性和可解释性，并为未来的自知推理模型研究奠定基础。

## 📄 摘要（原文）

> Reinforcement Learning (RL) methods, exemplified by Group Relative Policy Optimization (GRPO) and its variants, play a central role in developing reasoning models. However, these methods often suffer from a critical overconfidence issue, which prevents them from achieving self-aware reasoning models. In this study, we propose a simple yet effective confidence-calibration group sequence policy gradient method, called C$^2$GSPG, which simultaneously enhances reasoning performance while suppressing overconfidence. In principle, we propose a Group Sequence Policy Gradient (GSPG) framework for learning reasoning models, which eliminates the token-level bias commonly appearing in GRPO and its variants. In this framework, we define the model confidence for each reasoning problem using the normalized sequence-level probability, and then apply a cross-entropy regularizer to calibrate the model confidence to the sequence's reward. We demonstrate that the confidence calibration regularizer and GSPG are collaborative for binary rewards, as their objectives always share the same gradient direction. For non-binary rewards, we apply nonlinear reward normalization and adaptive regularizer clipping, mitigating the potential conflict between the two objectives. Applying C$^2$GSPG to post-train large language models in logical and mathematical reasoning tasks, we show its superiority over state-of-the-art methods in both reasoning accuracy and confidence calibration. The code of C$^2$GSPG is available at https://github.com/HaotianLiu123/CCGSPG.

