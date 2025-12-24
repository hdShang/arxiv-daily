---
layout: default
title: "OmniQuality-R: Advancing Reward Models Through All-Encompassing Quality Assessment"
---

# OmniQuality-R: Advancing Reward Models Through All-Encompassing Quality Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10609" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10609v1</a>
  <a href="https://arxiv.org/pdf/2510.10609.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10609v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10609v1', 'OmniQuality-R: Advancing Reward Models Through All-Encompassing Quality Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiting Lu, Fengbin Guan, Yixin Gao, Yan Zhong, Xinge Peng, Jiakang Yuan, Yihao Liu, Bo Zhang, Xin Li, Zhibo Chen, Weisi Lin

**分类**: cs.CV

**发布日期**: 2025-10-12

---

## 💡 一句话要点

**OmniQuality-R：通过全方位质量评估提升奖励模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励模型` `质量评估` `多任务学习` `思维链` `强化学习`

## 📋 核心要点

1. 现有视觉评估方法通常仅限于单一任务，缺乏通用性和灵活性，难以适应复杂场景。
2. OmniQuality-R将多任务质量推理转化为连续可解释的奖励信号，用于策略优化，实现统一的奖励建模。
3. 通过推理增强的数据集和强化学习优化，OmniQuality-R在美学质量、技术质量和文本-图像对齐等任务上表现出色。

## 📝 摘要（中文）

现有的视觉评估方法通常局限于单一任务。为了解决这个问题，我们提出了OmniQuality-R，一个统一的奖励建模框架，它将多任务质量推理转化为连续且可解释的奖励信号，用于策略优化。受到主观实验的启发，在主观实验中，参与者在评估之前会收到特定于任务的指令，概述不同的评估原则，因此我们提出了OmniQuality-R，一个结构化的奖励建模框架，它将多维推理转化为连续且可解释的奖励信号。为了实现这一点，我们通过拒绝采样来采样信息丰富的计划-推理轨迹，从而构建了一个推理增强的奖励建模数据集，形成了一个可靠的思维链（CoT）数据集，用于监督微调（SFT）。在此基础上，我们应用Group Relative Policy Optimization (GRPO)进行后训练，使用基于高斯的奖励来支持连续分数预测。为了进一步稳定训练并提高下游泛化能力，我们在强化学习过程中加入了标准差（STD）过滤和熵门控机制。这些技术抑制了不稳定的更新，并减少了策略优化中的方差。我们在三个关键的IQA任务上评估了OmniQuality-R：美学质量评估、技术质量评估和文本-图像对齐。

## 🔬 方法详解

**问题定义**：现有视觉质量评估方法通常针对特定任务设计，缺乏通用性，难以同时处理多种质量评估标准。此外，现有方法往往输出离散的质量等级，缺乏细粒度和可解释性，不利于策略优化。因此，需要一种能够统一处理多任务质量评估，并输出连续、可解释奖励信号的框架。

**核心思路**：OmniQuality-R的核心思路是将多任务质量评估问题转化为奖励建模问题，通过学习一个能够根据不同任务指令输出连续奖励信号的模型，实现统一的质量评估。该方法借鉴了人类主观评估的模式，即根据任务指令进行评估，并利用思维链（CoT）推理来提高评估的准确性和可解释性。

**技术框架**：OmniQuality-R的整体框架包括以下几个主要阶段：1) **数据构建**：通过拒绝采样生成包含计划-推理轨迹的推理增强数据集，用于监督微调。2) **监督微调（SFT）**：利用思维链数据集对奖励模型进行微调，使其具备初步的质量评估能力。3) **Group Relative Policy Optimization (GRPO)**：使用GRPO进行后训练，利用高斯奖励函数支持连续分数预测，进一步优化奖励模型。4) **稳定训练机制**：引入标准差（STD）过滤和熵门控机制，抑制不稳定更新，减少策略优化中的方差。

**关键创新**：OmniQuality-R的关键创新在于：1) **统一的奖励建模框架**：将多任务质量评估问题转化为奖励建模问题，实现统一的质量评估。2) **推理增强的数据集**：通过拒绝采样生成包含计划-推理轨迹的数据集，提高评估的准确性和可解释性。3) **稳定训练机制**：引入标准差过滤和熵门控机制，提高训练的稳定性和泛化能力。

**关键设计**：1) **思维链（CoT）数据集**：通过人工标注或自动生成的方式，构建包含推理过程的数据集，用于监督微调。2) **高斯奖励函数**：使用高斯函数作为奖励函数，支持连续分数预测。3) **标准差（STD）过滤**：根据奖励值的标准差，过滤掉不稳定的更新。4) **熵门控机制**：通过控制策略的熵，减少策略优化中的方差。

## 📊 实验亮点

OmniQuality-R在美学质量评估、技术质量评估和文本-图像对齐三个IQA任务上进行了评估，实验结果表明，该方法能够有效提升奖励模型的性能，并取得显著的提升。具体性能数据和对比基线在论文中进行了详细展示（具体数值未知）。

## 🎯 应用场景

OmniQuality-R具有广泛的应用前景，可用于图像/视频生成模型的质量评估、图像修复/增强算法的性能优化、以及跨模态内容对齐的质量控制等领域。该研究有助于提升AI系统的感知能力和生成质量，为构建更智能、更可靠的AI应用奠定基础。

## 📄 摘要（原文）

> Current visual evaluation approaches are typically constrained to a single task. To address this, we propose OmniQuality-R, a unified reward modeling framework that transforms multi-task quality reasoning into continuous and interpretable reward signals for policy optimization. Inspired by subjective experiments, where participants are given task-specific instructions outlining distinct assessment principles prior to evaluation, we propose OmniQuality-R, a structured reward modeling framework that transforms multi-dimensional reasoning into continuous and interpretable reward signals. To enable this, we construct a reasoning-enhanced reward modeling dataset by sampling informative plan-reason trajectories via rejection sampling, forming a reliable chain-of-thought (CoT) dataset for supervised fine-tuning (SFT). Building on this, we apply Group Relative Policy Optimization (GRPO) for post-training, using a Gaussian-based reward to support continuous score prediction. To further stabilize the training and improve downstream generalization, we incorporate standard deviation (STD) filtering and entropy gating mechanisms during reinforcement learning. These techniques suppress unstable updates and reduce variance in policy optimization. We evaluate OmniQuality-R on three key IQA tasks: aesthetic quality assessment, technical quality evaluation, and text-image alignment.

