---
layout: default
title: "RHYTHM: Reasoning with Hierarchical Temporal Tokenization for Human Mobility"
---

# RHYTHM: Reasoning with Hierarchical Temporal Tokenization for Human Mobility

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23115" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23115v2</a>
  <a href="https://arxiv.org/pdf/2509.23115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23115v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23115v2', 'RHYTHM: Reasoning with Hierarchical Temporal Tokenization for Human Mobility')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu He, Haozheng Luo, Yan Chen, Qi R. Wang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-27 (更新: 2025-10-20)

**备注**: Advances in Neural Information Processing Systems 39 (NeurIPS) 2025

**🔗 代码/项目**: [GITHUB](https://github.com/he-h/rhythm)

---

## 💡 一句话要点

**提出RHYTHM框架以解决人类移动预测中的复杂依赖问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人类移动预测` `分层时间标记` `大型语言模型` `时空预测` `轨迹推理` `周期性行为` `机器学习`

## 📋 核心要点

1. 人类移动预测面临复杂的长程依赖和周期性行为，现有方法难以有效捕捉这些特征。
2. RHYTHM框架通过分层时间标记和大型语言模型，优化了轨迹的表示和推理过程。
3. 在真实数据集上，RHYTHM显著提高了预测准确率，并减少了训练时间，展现了优越的性能。

## 📝 摘要（中文）

预测人类移动具有内在挑战，主要由于复杂的长程依赖和多尺度周期性行为。为此，我们提出了RHYTHM（基于分层时间标记的人类移动推理），这是一个统一框架，利用大型语言模型（LLMs）作为通用的时空预测器和轨迹推理器。RHYTHM通过时间标记将每条轨迹划分为每日段，并将其编码为离散标记，采用分层注意力机制捕捉日常和每周依赖，从而在保留周期性信息的同时，显著减少序列长度。此外，我们通过冻结的LLM为轨迹段和预测目标添加预计算的提示嵌入，进一步丰富标记表示。RHYTHM在三个真实世界数据集上评估，整体准确率提高了2.4%，周末准确率提升了5.0%，训练时间减少了24.6%。

## 🔬 方法详解

**问题定义**：本论文旨在解决人类移动预测中的复杂长程依赖和多尺度周期性行为问题。现有方法在捕捉这些特征时存在不足，导致预测准确性低下。

**核心思路**：RHYTHM框架通过时间标记将轨迹划分为日常段，并利用分层注意力机制来捕捉日常和每周的依赖关系，从而有效减少序列长度并保留周期性信息。

**技术框架**：RHYTHM的整体架构包括轨迹的时间标记、离散标记的编码、分层注意力机制以及通过冻结的LLM进行的推理。主要模块包括轨迹分段、标记表示和预测目标的提示嵌入。

**关键创新**：RHYTHM的主要创新在于引入分层时间标记和利用大型语言模型进行轨迹推理，这与传统方法在处理长序列时的局限性形成鲜明对比。

**关键设计**：在模型设计中，RHYTHM保持预训练的LLM骨干网络冻结，优化了训练速度和内存使用。同时，通过添加预计算的提示嵌入，增强了标记的表示能力。

## 📊 实验亮点

RHYTHM在三个真实世界数据集上进行评估，取得了整体准确率提高2.4%的显著成果，周末的准确率提升达到5.0%，同时训练时间减少了24.6%。这些结果表明RHYTHM在处理复杂人类移动预测任务中的有效性和高效性。

## 🎯 应用场景

RHYTHM框架在智能交通、城市规划和人群行为分析等领域具有广泛的应用潜力。通过提高人类移动预测的准确性，该研究可以为交通管理和资源分配提供更有效的决策支持，进而提升城市运营效率和居民生活质量。

## 📄 摘要（原文）

> Predicting human mobility is inherently challenging due to complex long-range dependencies and multi-scale periodic behaviors. To address this, we introduce RHYTHM (Reasoning with Hierarchical Temporal Tokenization for Human Mobility), a unified framework that leverages large language models (LLMs) as general-purpose spatio-temporal predictors and trajectory reasoners. Methodologically, RHYTHM employs temporal tokenization to partition each trajectory into daily segments and encode them as discrete tokens with hierarchical attention that captures both daily and weekly dependencies, thereby quadratically reducing the sequence length while preserving cyclical information. Additionally, we enrich token representations by adding pre-computed prompt embeddings for trajectory segments and prediction targets via a frozen LLM, and feeding these combined embeddings back into the LLM backbone to capture complex interdependencies. Computationally, RHYTHM keeps the pretrained LLM backbone frozen, yielding faster training and lower memory usage. We evaluate our model against state-of-the-art methods using three real-world datasets. Notably, RHYTHM achieves a 2.4% improvement in overall accuracy, a 5.0% increase on weekends, and a 24.6% reduction in training time. Code is publicly available at https://github.com/he-h/rhythm.

