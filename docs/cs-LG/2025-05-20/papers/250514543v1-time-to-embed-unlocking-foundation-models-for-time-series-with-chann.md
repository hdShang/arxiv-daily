---
layout: default
title: "Time to Embed: Unlocking Foundation Models for Time Series with Channel Descriptions"
---

# Time to Embed: Unlocking Foundation Models for Time Series with Channel Descriptions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14543" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14543v1</a>
  <a href="https://arxiv.org/pdf/2505.14543.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14543v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14543v1', 'Time to Embed: Unlocking Foundation Models for Time Series with Channel Descriptions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Utsav Dutta, Sina Khoshfetrat Pakazad, Henrik Ohlsson

**分类**: cs.LG

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出CHARM以解决时间序列建模的局限性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列建模` `基础模型` `多变量分析` `Transformer` `可解释性` `数据增强` `联合嵌入`

## 📋 核心要点

1. 现有的时间序列模型往往依赖于特定任务和数据集，缺乏通用性和可迁移性。
2. CHARM模型通过集成通道级文本描述，学习共享和领域感知的时间序列表示，克服了传统模型的局限。
3. CHARM在多个下游任务中表现出色，设定了时间序列表示学习的新基准，展示了700万参数模型的强大能力。

## 📝 摘要（中文）

传统的时间序列模型通常是任务特定的，依赖于数据集特定的训练和大量特征工程。尽管基于Transformer的架构提高了可扩展性，但在时间序列领域，基础模型的应用仍然较少，主要集中在预测任务上。本文提出了CHARM，一个用于多变量时间序列的基础嵌入模型，能够学习共享、可转移和领域感知的表示。CHARM通过集成通道级文本描述的架构创新，解决了时间序列基础学习的独特挑战，同时保持对通道顺序的不变性。该模型采用联合嵌入预测架构（JEPA）进行训练，结合新颖的数据增强方案和损失函数，以提高可解释性和训练稳定性。我们的700万参数模型在多种下游任务中实现了最先进的性能，为时间序列表示学习设定了新的基准。

## 🔬 方法详解

**问题定义**：本文旨在解决传统时间序列模型在任务特定性和数据集依赖性方面的局限性，现有方法往往需要大量特征工程，难以实现通用性和可迁移性。

**核心思路**：CHARM模型通过引入通道级文本描述，学习共享和领域感知的表示，旨在提高时间序列数据的表示能力，同时保持对通道顺序的不变性。

**技术框架**：CHARM采用联合嵌入预测架构（JEPA），结合新颖的数据增强方案和损失函数，整体流程包括数据预处理、模型训练和评估三个主要阶段。

**关键创新**：CHARM的主要创新在于其架构设计，能够有效整合通道级文本描述，提升模型的可解释性和训练稳定性，与传统模型相比具有显著的优势。

**关键设计**：模型包含700万参数，采用特定的损失函数以增强可解释性，网络结构设计上注重通道描述的集成，确保模型对输入顺序的鲁棒性。

## 📊 实验亮点

CHARM模型在多个下游任务中表现出色，设定了时间序列表示学习的新基准。具体而言，该模型在多项任务中超越了现有的最先进模型，展示了显著的性能提升，尤其是在数据稀缺的情况下，表现尤为突出。

## 🎯 应用场景

CHARM模型在多变量时间序列分析中具有广泛的应用潜力，适用于金融市场预测、气候变化监测、健康数据分析等领域。其通用性和可迁移性使得该模型能够在不同场景中快速适应，提升数据分析的效率和准确性。未来，CHARM有望推动时间序列分析的研究和应用发展。

## 📄 摘要（原文）

> Traditional time series models are task-specific and often depend on dataset-specific training and extensive feature engineering. While Transformer-based architectures have improved scalability, foundation models, commonplace in text, vision, and audio, remain under-explored for time series and are largely restricted to forecasting. We introduce $\textbf{CHARM}$, a foundation embedding model for multivariate time series that learns shared, transferable, and domain-aware representations. To address the unique difficulties of time series foundation learning, $\textbf{CHARM}$ incorporates architectural innovations that integrate channel-level textual descriptions while remaining invariant to channel order. The model is trained using a Joint Embedding Predictive Architecture (JEPA), with novel augmentation schemes and a loss function designed to improve interpretability and training stability. Our $7$M-parameter model achieves state-of-the-art performance across diverse downstream tasks, setting a new benchmark for time series representation learning.

