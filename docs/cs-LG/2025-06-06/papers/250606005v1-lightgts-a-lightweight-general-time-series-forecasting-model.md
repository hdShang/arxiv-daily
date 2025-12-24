---
layout: default
title: "LightGTS: A Lightweight General Time Series Forecasting Model"
---

# LightGTS: A Lightweight General Time Series Forecasting Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06005" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06005v1</a>
  <a href="https://arxiv.org/pdf/2506.06005.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06005v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06005v1', 'LightGTS: A Lightweight General Time Series Forecasting Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihang Wang, Yuying Qiu, Peng Chen, Yang Shu, Zhongwen Rao, Lujia Pan, Bin Yang, Chenjuan Guo

**分类**: cs.LG

**发布日期**: 2025-06-06

**备注**: Accepted by the 42th International Conference on Machine Learning (ICML 2025)

---

## 💡 一句话要点

**提出LightGTS以解决时间序列预测中的计算负担问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `轻量级模型` `周期性建模` `多源预训练` `高效解码`

## 📋 核心要点

1. 现有时间序列预测模型通常参数庞大，计算负担重，难以在资源受限的环境中应用。
2. LightGTS通过周期性标记化和周期性并行解码技术，旨在实现轻量级且高效的时间序列预测。
3. 在9个真实世界基准测试中，LightGTS在零样本和全样本设置下均表现出色，效率显著提升。

## 📝 摘要（中文）

现有的时间序列预测模型通常依赖于大规模的多源预训练，导致模型参数庞大，计算负担重，尤其在资源受限的场景中表现不佳。本文提出LightGTS，一个轻量级的通用时间序列预测模型，旨在通过一致的周期建模来解决这一问题。为处理多源预训练中的多样化尺度和内在周期，本文引入了周期性标记化技术，以提取不同数据集中的一致周期模式。同时，采用周期性并行解码技术，利用历史标记来提升预测效果。LightGTS在9个真实世界基准测试中表现出色，且在零样本和全样本设置下均展现出优越的效率。

## 🔬 方法详解

**问题定义**：现有的时间序列预测模型通常依赖于大规模的多源预训练，导致模型参数庞大，计算负担重，尤其在资源受限的场景中表现不佳。

**核心思路**：本文提出LightGTS，通过周期性标记化和周期性并行解码技术，旨在提取一致的周期模式并利用历史信息，从而实现轻量级的高效预测。

**技术框架**：LightGTS的整体架构包括周期性标记化模块和周期性并行解码模块。周期性标记化负责提取不同数据集中的周期模式，而周期性并行解码则利用历史标记进行预测。

**关键创新**：最重要的技术创新点在于引入了周期性标记化和周期性并行解码，这两者充分利用了时间序列中固有的周期性偏置，显著提升了模型的预测能力。

**关键设计**：在模型设计中，LightGTS采用了轻量级的网络结构，优化了参数设置，并设计了适应周期性特征的损失函数，以提高预测的准确性和效率。

## 📊 实验亮点

在9个真实世界基准测试中，LightGTS在零样本和全样本设置下均实现了最先进的预测性能，相比现有时间序列基础模型，其效率显著提升，具体性能数据尚未公开。

## 🎯 应用场景

LightGTS在时间序列预测领域具有广泛的应用潜力，尤其适用于金融市场预测、气象数据分析和工业设备监控等场景。其轻量级特性使其能够在资源受限的环境中高效运行，具有实际应用价值。未来，该模型可能推动更多领域的智能预测技术发展。

## 📄 摘要（原文）

> Existing works on general time series forecasting build foundation models with heavy model parameters through large-scale multi-source pre-training. These models achieve superior generalization ability across various datasets at the cost of significant computational burdens and limitations in resource-constrained scenarios. This paper introduces LightGTS, a lightweight general time series forecasting model designed from the perspective of consistent periodical modeling. To handle diverse scales and intrinsic periods in multi-source pre-training, we introduce Periodical Tokenization, which extracts consistent periodic patterns across different datasets with varying scales. To better utilize the periodicity in the decoding process, we further introduce Periodical Parallel Decoding, which leverages historical tokens to improve forecasting. Based on the two techniques above which fully leverage the inductive bias of periods inherent in time series, LightGTS uses a lightweight model to achieve outstanding performance on general time series forecasting. It achieves state-of-the-art forecasting performance on 9 real-world benchmarks in both zero-shot and full-shot settings with much better efficiency compared with existing time series foundation models.

