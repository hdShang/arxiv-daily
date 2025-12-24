---
layout: default
title: "FaCTR: Factorized Channel-Temporal Representation Transformers for Efficient Time Series Forecasting"
---

# FaCTR: Factorized Channel-Temporal Representation Transformers for Efficient Time Series Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05597" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05597v1</a>
  <a href="https://arxiv.org/pdf/2506.05597.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05597v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05597v1', 'FaCTR: Factorized Channel-Temporal Representation Transformers for Efficient Time Series Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yash Vijay, Harini Subramanyan

**分类**: cs.LG

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出FaCTR以解决时间序列预测中的过度参数化问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `时间序列预测` `Transformer` `低秩因子分解` `跨通道交互` `自监督学习` `模型解释性` `高效预测`

## 📋 核心要点

1. 现有Transformer在时间序列预测中面临过度参数化和复杂依赖结构的挑战，导致性能提升有限。
2. FaCTR通过引入低秩因子分解机建模动态跨通道交互，结合可学习的门控机制，优化时间序列数据的处理。
3. FaCTR在11个公共基准测试中表现优异，参数量显著减少，且支持自监督预训练，提升了模型的适用性和解释性。

## 📝 摘要（中文）

尽管Transformer在语言和视觉任务中表现优异，但其架构复杂性导致在时间序列预测中收益递减。时间序列数据的信息密度较低且通道间依赖关系复杂，需对结构化变量交互进行条件处理。为此，本文提出FaCTR，一种轻量级的时空Transformer，采用显式结构设计。FaCTR通过可学习的门控机制，将动态的对称跨通道交互注入到时间上下文的补丁嵌入中，并进一步编码静态和动态协变量以实现多变量条件化。尽管设计紧凑，FaCTR在11个公共预测基准上实现了最先进的性能，其最大变体参数仅约为40万，平均比竞争性时空Transformer基线小50倍。此外，其结构化设计通过跨通道影响评分增强了解释性，满足实际决策需求。最后，FaCTR支持自监督预训练，为下游时间序列任务提供了紧凑而多功能的基础。

## 🔬 方法详解

**问题定义**：本文旨在解决时间序列预测中Transformer模型的过度参数化和复杂依赖结构问题。现有方法在处理低信息密度和复杂通道间依赖时效果不佳，导致性能提升有限。

**核心思路**：FaCTR的核心思路是通过显式的结构设计和低秩因子分解机来建模动态的跨通道交互，从而提高模型的效率和效果。通过可学习的门控机制，FaCTR能够有效地将这些交互融入到时间上下文的补丁嵌入中。

**技术框架**：FaCTR的整体架构包括多个模块：首先是时间上下文的补丁嵌入，其次是通过低秩因子分解机实现的跨通道交互，最后是静态和动态协变量的编码。这些模块协同工作，以实现高效的时间序列预测。

**关键创新**：FaCTR的主要创新在于其轻量级设计和结构化建模方式，使其在参数量上显著低于传统时空Transformer，同时保持了优越的预测性能。这种设计使得模型不仅高效，而且易于解释。

**关键设计**：FaCTR的关键设计包括可学习的门控机制、低秩因子分解机的实现，以及对静态和动态协变量的有效编码。这些设计确保了模型在处理复杂依赖关系时的灵活性和准确性。

## 📊 实验亮点

FaCTR在11个公共预测基准上实现了最先进的性能，其最大变体仅使用约40万参数，平均比竞争性时空Transformer基线小50倍。此外，FaCTR的结构化设计提供了跨通道影响评分，增强了模型的可解释性。

## 🎯 应用场景

FaCTR在时间序列预测领域具有广泛的应用潜力，尤其适用于金融市场预测、气象数据分析和工业设备监控等场景。其高效的模型结构和良好的解释性使其在实际决策中具有重要价值，未来可能推动更多领域的智能预测技术发展。

## 📄 摘要（原文）

> While Transformers excel in language and vision-where inputs are semantically rich and exhibit univariate dependency structures-their architectural complexity leads to diminishing returns in time series forecasting. Time series data is characterized by low per-timestep information density and complex dependencies across channels and covariates, requiring conditioning on structured variable interactions. To address this mismatch and overparameterization, we propose FaCTR, a lightweight spatiotemporal Transformer with an explicitly structural design. FaCTR injects dynamic, symmetric cross-channel interactions-modeled via a low-rank Factorization Machine into temporally contextualized patch embeddings through a learnable gating mechanism. It further encodes static and dynamic covariates for multivariate conditioning. Despite its compact design, FaCTR achieves state-of-the-art performance on eleven public forecasting benchmarks spanning both short-term and long-term horizons, with its largest variant using close to only 400K parameters-on average 50x smaller than competitive spatiotemporal transformer baselines. In addition, its structured design enables interpretability through cross-channel influence scores-an essential requirement for real-world decision-making. Finally, FaCTR supports self-supervised pretraining, positioning it as a compact yet versatile foundation for downstream time series tasks.

