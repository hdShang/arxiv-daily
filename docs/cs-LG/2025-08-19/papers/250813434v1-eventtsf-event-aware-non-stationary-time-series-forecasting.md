---
layout: default
title: "EventTSF: Event-Aware Non-Stationary Time Series Forecasting"
---

# EventTSF: Event-Aware Non-Stationary Time Series Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13434" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13434v1</a>
  <a href="https://arxiv.org/pdf/2508.13434.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13434v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13434v1', 'EventTSF: Event-Aware Non-Stationary Time Series Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunfeng Ge, Ming Jin, Yiji Zhao, Hongyan Li, Bo Du, Chang Xu, Shirui Pan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-19

**备注**: 13 pages, 10 figures

---

## 💡 一句话要点

**提出EventTSF以解决多模态非平稳时间序列预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `多模态融合` `自回归模型` `事件感知` `非平稳动态` `流匹配` `扩散变换器` `预测精度`

## 📋 核心要点

1. 现有方法多依赖单一模态，未能有效整合文本事件与时间序列，导致预测性能不足。
2. 本文提出EventTSF框架，通过自回归扩散与流匹配，结合历史时间序列与文本事件进行预测。
3. 在8个数据集上，EventTSF在预测精度上提升10.7%，训练效率提高1.13倍，表现优于12个基线模型。

## 📝 摘要（中文）

时间序列预测在能源和交通等关键领域发挥着重要作用，其中非平稳动态与文本等其他模态的事件密切相关。然而，将基于自然语言的外部事件纳入非平稳预测的研究仍然较少，现有方法多依赖单一模态，导致上下文知识有限和模型性能不足。为了解决这一问题，本文提出了事件感知非平稳时间序列预测（EventTSF），该框架通过自回归生成方法将历史时间序列与文本事件结合，以进行后续预测。EventTSF在每一步中使用自回归扩散与流匹配，捕捉细微的时间-事件交互。通过适应性控制流匹配时间步，处理事件引入的不确定性。实验结果表明，EventTSF在8个合成和真实数据集上超越12个基线，预测精度提高10.7%，训练效率提升1.13倍。

## 🔬 方法详解

**问题定义**：本文旨在解决如何将文本事件与非平稳时间序列有效结合，以提高预测准确性的问题。现有方法在多模态融合方面存在不足，导致模型性能受限。

**核心思路**：EventTSF通过自回归生成框架，将历史时间序列与文本事件进行整合，利用自回归扩散与流匹配捕捉时间与事件之间的细微交互。

**技术框架**：该方法包括三个主要模块：历史时间序列输入、文本事件处理和自回归预测生成。通过流匹配技术，动态调整时间步以适应事件语义信号。

**关键创新**：EventTSF的核心创新在于引入了流匹配机制，解决了文本事件与时间序列之间的同步问题，显著提升了模型的预测能力。

**关键设计**：模型采用多模态U型扩散变换器，能够高效融合不同分辨率的时间和文本模态，损失函数设计上考虑了事件引入的不确定性。整体架构设计注重模块间的协同工作，以提高预测的准确性和效率。

## 📊 实验亮点

在实验中，EventTSF在8个合成和真实数据集上表现优异，预测精度提高了10.7%，训练效率提升了1.13倍，超越了12个基线模型，显示出其在多模态非平稳时间序列预测中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括能源管理、交通预测和金融市场分析等，能够为决策提供更准确的时间序列预测。通过整合多模态信息，EventTSF有望在实际应用中显著提升预测性能，推动相关领域的发展。

## 📄 摘要（原文）

> Time series forecasting plays a vital role in critical domains like energy and transportation, where non-stationary dynamics are deeply intertwined with events in other modalities such as texts. However, incorporating natural language-based external events to improve non-stationary forecasting remains largely unexplored, as most approaches still rely on a single modality, resulting in limited contextual knowledge and model underperformance. Enabling fine-grained multimodal interactions between temporal and textual data is challenged by three fundamental issues: (1) the difficulty of fine-grained synchronization between time-varying discrete textual events and continuous time series; (2) the inherent temporal uncertainty introduced by textual semantics; and (3) the misalignment between textual event embeddings and multi-resolution temporal patterns. In this work, we address these challenges by introducing event-aware non-stationary time series forecasting (EventTSF), an autoregressive generation framework that integrates historical time series with textual events to make subsequent forecasts. Specifically, EventTSF uses autoregressive diffusion with flow matching at each step to capture nuanced temporal-event interactions. To handle event-induced uncertainty, flow matching timesteps are adaptively controlled according to event semantic signals. The underlying denoiser employs a multimodal U-shaped diffusion transformer that efficiently fuses temporal and textual modalities across different resolutions. Extensive experiments on 8 synthetic and real-world datasets show that EventTSF outperforms 12 baselines across diverse event-aware non-stationary time series forecasting scenarios, achieving substantial improvements of 10.7% higher forecasting accuracy and $1.13\times$ faster training efficiency.

