---
layout: default
title: "RoRecomp: Enhancing Reasoning Efficiency via Rollout Response Recomposition in Reinforcement Learning"
---

# RoRecomp: Enhancing Reasoning Efficiency via Rollout Response Recomposition in Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25958" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25958v1</a>
  <a href="https://arxiv.org/pdf/2509.25958.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25958v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25958v1', 'RoRecomp: Enhancing Reasoning Efficiency via Rollout Response Recomposition in Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gang Li, Yulei Qin, Xiaoyu Tan, Dingkang Yang, Yuchen Shi, Zihan Xu, Xiang Li, Xing Sun, Ke Li

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出RoRecomp，通过重组Rollout响应提升强化学习中LLM的推理效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `推理效率` `Rollout重组` `可验证奖励`

## 📋 核心要点

1. 传统RLVR训练LLM时，奖励机制缺乏对效率的激励，导致推理过程冗长，探索轨迹效率低下。
2. RoRecomp通过重组训练数据，区分优先批次和补偿批次，引导模型生成更简洁高效的推理过程。
3. 实验表明，RoRecomp在多个任务中显著减少了推理长度和不必要的工具调用，同时保持了性能。

## 📝 摘要（中文）

本文提出Rollout Response Recomposition (RoRecomp) 方法，旨在解决基于可验证奖励的强化学习（RLVR）训练大型语言模型（LLM）时，推理过程冗长和探索轨迹效率低下的问题。RoRecomp通过策略性地重组训练数据，引导模型生成简洁的推理过程。该方法将响应分为两类批次：优先批次，结合在线批次中的短-正确和长-错误响应，为简洁性提供清晰的梯度信号；补偿批次，利用回放缓冲区中的剩余响应，维持训练稳定性并防止模型崩溃。实验结果表明，RoRecomp在多个场景中显著提升了效率：在零样本强化学习中减少了27.7%的推理长度，在Agentic强化学习中减少了46.8%的不必要工具调用并提高了准确率，在思维压缩中实现了高达52.5%的长度缩减，且对性能影响极小。

## 🔬 方法详解

**问题定义**：现有基于可验证奖励的强化学习（RLVR）训练大型语言模型（LLM）时，由于奖励仅关注结果，缺乏对过程效率的激励，导致模型生成的推理过程过于冗长，探索轨迹效率低下。此外，Rollout中响应长度差异较大，导致优化信号噪声较高。

**核心思路**：RoRecomp的核心思路是通过策略性地重组Rollout响应，构建更有效的训练数据，从而引导模型学习更简洁的推理过程。具体来说，该方法区分了“优先批次”和“补偿批次”，分别用于提供简洁性梯度信号和维持训练稳定性。

**技术框架**：RoRecomp是一个即插即用的方法，可以应用于现有的RLVR训练框架。其主要流程包括：1) 从Rollout中收集响应；2) 将响应分为短-正确、长-错误和其他响应；3) 构建优先批次，包含短-正确和长-错误响应，用于优化简洁性；4) 构建补偿批次，包含剩余响应，用于维持训练稳定性；5) 使用优先批次和补偿批次更新模型。

**关键创新**：RoRecomp的关键创新在于其数据重组策略，通过区分优先批次和补偿批次，能够更有效地引导模型学习简洁的推理过程。与传统的RLVR方法相比，RoRecomp能够提供更清晰的简洁性梯度信号，并防止模型崩溃。

**关键设计**：RoRecomp的关键设计包括：1) 优先批次的构建方式，选择短-正确和长-错误响应，以提供清晰的简洁性梯度信号；2) 补偿批次的构建方式，使用剩余响应，以维持训练稳定性；3) 批次大小的设置，需要平衡简洁性优化和训练稳定性。

## 📊 实验亮点

RoRecomp在三个实验场景中均取得了显著的效率提升。在零样本强化学习中，推理长度减少了27.7%。在Agentic强化学习中，不必要的工具调用减少了46.8%，同时提高了准确率。在思维压缩任务中，长度缩减高达52.5%。所有这些提升都伴随着最小的性能影响，证明了RoRecomp的有效性和实用性。

## 🎯 应用场景

RoRecomp可应用于各种需要高效推理的大型语言模型应用场景，例如智能Agent、问答系统、代码生成等。通过减少推理长度和不必要的工具调用，RoRecomp可以显著提高这些应用的效率和用户体验，并降低计算成本。该方法还有助于提升LLM在资源受限环境下的部署能力。

## 📄 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has proven effective in eliciting complex reasoning in large language models (LLMs). However, standard RLVR training often leads to excessively verbose processes (in reasoning tasks) and inefficient exploration trajectories (in agentic settings), as outcome-only rewards provide no incentive for efficiency and the high variance in response length within relatively small rollout groups results in noisy optimization signals. To address this, we propose Rollout Response Recomposition (RoRecomp), a plug-and-play method that guides models toward concise reasoning by strategically recomposing the training data. RoRecomp separates responses into two distinct batch types: 1) priority batches, which combine short-correct and long-incorrect responses selected from online batches to provide a clear gradient signal for brevity, and 2) compensation batches, which utilize remaining responses from a replay buffer to maintain stability and prevent model collapse. To comprehensively evaluate effectiveness, we test RoRecomp across three settings where results demonstrate substantial efficiency gains: reducing reasoning length by 27.7% in zero RL training, reducing unnecessary tool calls by 46.8% while improving accuracy in agentic RL, and achieving up to 52.5% length reduction in thinking compression, all with minimal performance impact.

