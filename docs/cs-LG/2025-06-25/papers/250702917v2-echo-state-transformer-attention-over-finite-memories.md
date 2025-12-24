---
layout: default
title: "Echo State Transformer: Attention Over Finite Memories"
---

# Echo State Transformer: Attention Over Finite Memories

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02917" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02917v2</a>
  <a href="https://arxiv.org/pdf/2507.02917.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02917v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02917v2', 'Echo State Transformer: Attention Over Finite Memories')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yannis Bendi-Ouis, Xavier Hinaut

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-25 (更新: 2025-10-27)

---

## 💡 一句话要点

**提出回声状态变换器以解决Transformer计算复杂度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `回声状态网络` `水库计算` `Transformer` `时间序列分析` `异常检测` `分类任务` `计算复杂度` `深度学习`

## 📋 核心要点

1. 现有的Transformer模型在处理长序列时计算复杂度呈二次增长，限制了其在时间序列任务中的应用。
2. 本文提出回声状态变换器（EST），通过结合Transformer注意力机制与水库计算原理，构建高效的固定大小记忆系统。
3. EST在69个时间序列任务中表现优异，在五个类别中排名第一，尤其在分类和异常检测任务中超越了多个先进基线。

## 📝 摘要（中文）

尽管大型语言模型及其基础的Transformer架构在效率上表现出色，但它们并未反映大脑处理和学习语言及工作记忆等多样认知任务的方式。此外，Transformer在处理序列数据时面临着序列长度导致的计算复杂度呈二次增长的根本性障碍。为了解决这些问题，本文提出了回声状态变换器（EST），这是一种混合架构，能够优雅地解决计算效率问题，并在分类和检测任务中表现出色。EST将Transformer的注意力机制与水库计算的原理相结合，创建了一个固定大小的窗口分布式记忆系统。通过灵感来自回声状态网络，EST利用随机递归网络作为轻量高效的记忆单元。实验结果表明，EST在时间序列基准测试中表现优异，尤其在分类和异常检测任务中超越了多项先进基线。

## 🔬 方法详解

**问题定义**：本文旨在解决Transformer在处理长序列时计算复杂度呈二次增长的问题，这限制了其在时间序列数据处理中的应用。

**核心思路**：回声状态变换器（EST）通过结合Transformer的注意力机制与水库计算的原理，创建了一个高效的固定大小记忆系统，从而降低计算复杂度。

**技术框架**：EST架构包含多个并行工作的水库作为独立的工作记忆单元，利用随机递归网络作为轻量级记忆。整体流程包括输入序列的处理、注意力机制的应用以及通过工作记忆单元的动态调整。

**关键创新**：EST的核心创新在于训练经典水库的超参数，使得模型能够动态适应记忆与非线性之间的权衡，从而有效解决了标准Transformer的计算复杂度问题。

**关键设计**：EST的设计包括多个并行水库的构建、动态调整的超参数设置，以及在每个处理步骤中保持恒定的计算复杂度。

## 📊 实验亮点

在69个时间序列任务的基准测试中，EST在五个类别中排名第一，尤其在分类和异常检测任务中超越了多个强大的先进基线，展现出卓越的性能和竞争力。具体而言，EST在分类任务中表现优于现有最先进模型，且在短期预测任务中保持竞争力。

## 🎯 应用场景

回声状态变换器（EST）在时间序列分类和异常检测等任务中展现出优越性能，适用于金融监测、健康监测和工业故障检测等领域。其高效的计算特性使其在需要快速响应和实时处理的应用场景中具有实际价值，未来可进一步扩展到其他需要处理序列数据的领域。

## 📄 摘要（原文）

> While Large Language Models and their underlying Transformer architecture are remarkably efficient, they do not reflect how our brain processes and learns a diversity of cognitive tasks such as language and working memory. Furthermore, sequential data processing with Transformers encounters a fundamental barrier: quadratic complexity growth with sequence length. Motivated by these limitations, our ambition is to create more efficient models that are less reliant on intensive computations. We introduce Echo State Transformers (EST), a hybrid architecture that elegantly resolves this challenge while demonstrating exceptional performance in classification and detection tasks. EST integrates the Transformer attention mechanisms with principles from Reservoir Computing to create a fixed-size window distributed memory system. Drawing inspiration from Echo State Networks, the most prominent instance of the Reservoir Computing paradigm, our approach leverages reservoirs (random recurrent networks) as a lightweight and efficient memory. Our architecture integrates a new module called ''Working Memory'' based on several reservoirs working in parallel. These reservoirs work as independent working memory units with distinct internal dynamics. A novelty here is that the classical reservoir hyperparameters, controlling the dynamics, are now trained. Thus, the EST dynamically adapts the reservoir memory/non-linearity trade-off. Thanks to these working memory units, EST achieves constant computational complexity at each processing step, effectively breaking the quadratic scaling problem of standard Transformers. We evaluate ESTs on a recent challenging timeseries benchmark: the Time Series Library, which comprises 69 tasks across five categories. Results show that ESTs ranks first overall in two of five categories, outperforming strong state-of-the-art baselines on classification and anomaly detection tasks, while remaining competitive on short-term forecasting. These results position ESTs as a compelling alternative for time-series classification and anomaly detection, and a practical complement to transformer-style models in applications that prioritize robust representations and sensitive event detection.

