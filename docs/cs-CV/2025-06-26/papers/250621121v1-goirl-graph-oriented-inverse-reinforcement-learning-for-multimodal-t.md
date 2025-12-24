---
layout: default
title: "GoIRL: Graph-Oriented Inverse Reinforcement Learning for Multimodal Trajectory Prediction"
---

# GoIRL: Graph-Oriented Inverse Reinforcement Learning for Multimodal Trajectory Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21121" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21121v1</a>
  <a href="https://arxiv.org/pdf/2506.21121.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21121v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21121v1', 'GoIRL: Graph-Oriented Inverse Reinforcement Learning for Multimodal Trajectory Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muleilan Pei, Shaoshuai Shi, Lu Zhang, Peiliang Li, Shaojie Shen

**分类**: cs.CV, cs.RO

**发布日期**: 2025-06-26

**备注**: Accepted by ICML 2025

---

## 💡 一句话要点

**提出GoIRL框架以解决多模态轨迹预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逆强化学习` `轨迹预测` `多模态` `图结构` `自动驾驶` `特征适配` `最大熵`

## 📋 核心要点

1. 现有的轨迹预测方法多依赖于监督学习，难以处理多模态和不确定性问题。
2. 本文提出的GoIRL框架通过逆强化学习和图结构特征表示，增强了轨迹预测的能力。
3. 实验结果表明，GoIRL在多个基准测试中表现出色，超越了现有的监督学习模型。

## 📝 摘要（中文）

在自动驾驶中，周围代理的轨迹预测是一项具有挑战性的任务，因其固有的不确定性和多模态特性。本文提出了一种新颖的图导向逆强化学习（GoIRL）框架，该框架结合了向量化的上下文表示，超越了传统的监督学习方法。我们开发了一种特征适配器，有效地将车道图特征聚合到网格空间中，能够与最大熵逆强化学习范式无缝集成，从而推断奖励分布并获得可用于生成多种合理计划的策略。此外，基于采样的计划，我们实现了一个分层参数化的轨迹生成器，并引入了精细化模块以提高预测准确性和概率融合策略以增强预测信心。大量实验结果表明，我们的方法在大规模的Argoverse和nuScenes运动预测基准上不仅达到了最先进的性能，还展现了优于现有监督模型的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶中周围代理的轨迹预测问题，现有方法往往依赖于监督学习，难以有效处理多模态和不确定性，导致预测结果的局限性。

**核心思路**：GoIRL框架通过引入逆强化学习和图导向特征表示，能够更好地捕捉轨迹的多样性和复杂性，从而生成更为合理的轨迹预测。

**技术框架**：该框架包括特征适配器、最大熵逆强化学习模块、分层参数化轨迹生成器和概率融合策略等主要模块，整体流程为特征提取、奖励推断、策略生成和轨迹优化。

**关键创新**：GoIRL的核心创新在于将图结构特征与逆强化学习相结合，能够有效推断奖励分布并生成多种合理的轨迹计划，这一方法与传统的监督学习方法有本质区别。

**关键设计**：在设计中，特征适配器负责将车道图特征聚合到网格空间，最大熵逆强化学习用于推断奖励分布，分层参数化轨迹生成器则通过精细化模块和概率融合策略提升预测的准确性和信心。

## 📊 实验亮点

在大规模的Argoverse和nuScenes运动预测基准上，GoIRL框架达到了最先进的性能，超越了现有的监督学习模型，展现出更强的泛化能力。具体而言，实验结果显示其在多个评估指标上均有显著提升，证明了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、智能交通系统和人机交互等。通过提高轨迹预测的准确性和可靠性，GoIRL框架能够为自动驾驶系统提供更好的决策支持，进而提升行车安全性和效率。未来，该方法还可能扩展到其他需要多模态预测的领域，如机器人导航和人类行为预测。

## 📄 摘要（原文）

> Trajectory prediction for surrounding agents is a challenging task in autonomous driving due to its inherent uncertainty and underlying multimodality. Unlike prevailing data-driven methods that primarily rely on supervised learning, in this paper, we introduce a novel Graph-oriented Inverse Reinforcement Learning (GoIRL) framework, which is an IRL-based predictor equipped with vectorized context representations. We develop a feature adaptor to effectively aggregate lane-graph features into grid space, enabling seamless integration with the maximum entropy IRL paradigm to infer the reward distribution and obtain the policy that can be sampled to induce multiple plausible plans. Furthermore, conditioned on the sampled plans, we implement a hierarchical parameterized trajectory generator with a refinement module to enhance prediction accuracy and a probability fusion strategy to boost prediction confidence. Extensive experimental results showcase our approach not only achieves state-of-the-art performance on the large-scale Argoverse & nuScenes motion forecasting benchmarks but also exhibits superior generalization abilities compared to existing supervised models.

