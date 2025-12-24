---
layout: default
title: "CaPulse: Detecting Anomalies by Tuning in to the Causal Rhythms of Time Series"
---

# CaPulse: Detecting Anomalies by Tuning in to the Causal Rhythms of Time Series

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04630" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04630v1</a>
  <a href="https://arxiv.org/pdf/2508.04630.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04630v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04630v1', 'CaPulse: Detecting Anomalies by Tuning in to the Causal Rhythms of Time Series')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutong Xia, Yingying Zhang, Yuxuan Liang, Lunting Fan, Qingsong Wen, Roger Zimmermann

**分类**: cs.LG

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出CaPulse以解决时间序列异常检测中的因果机制问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `时间序列分析` `异常检测` `因果模型` `周期性归一化流` `数据不平衡` `可解释性` `机器学习`

## 📋 核心要点

1. 现有时间序列异常检测方法未能有效捕捉异常生成的因果机制，面临标签稀缺和数据不平衡等挑战。
2. 本文提出CaPulse框架，通过结构因果模型解析异常生成过程，并引入周期性归一化流以应对数据挑战。
3. 在七个真实数据集上的实验结果显示，CaPulse在AUROC指标上提升3%至17%，并且具有更好的可解释性。

## 📝 摘要（中文）

时间序列异常检测在多个领域受到广泛关注，但现有方法往往无法捕捉异常生成的潜在机制。此外，时间序列异常检测面临标签稀缺、数据不平衡和复杂多周期性等固有挑战。本文提出了一种新的基于因果关系的框架CaPulse，通过构建结构因果模型来解析异常生成过程，并提出周期性归一化流和新颖的掩码机制，创建了一种基于密度的异常检测方法。大量实验表明，CaPulse在七个真实数据集上均优于现有方法，AUROC提升幅度在3%到17%之间，且可解释性增强。

## 🔬 方法详解

**问题定义**：本文旨在解决时间序列异常检测中现有方法无法捕捉异常生成机制的问题，尤其是在标签稀缺和数据不平衡的情况下。

**核心思路**：CaPulse框架通过引入结构因果模型，解析异常生成过程，并结合周期性归一化流和掩码机制，形成一种新的异常检测方法。

**技术框架**：该方法包括三个主要模块：1) 结构因果模型构建，用于理解异常生成机制；2) 周期性归一化流，处理数据的多周期性；3) 掩码机制，增强模型对不同时间段的适应性。

**关键创新**：CaPulse的核心创新在于其因果脉冲的引入，使得模型能够更好地理解和捕捉异常生成的因果关系，这与传统方法的统计特征提取有本质区别。

**关键设计**：在设计上，采用了周期性归一化流的结构，结合了特定的损失函数以优化模型性能，同时引入了掩码机制以增强模型对时间序列中不同周期的适应能力。

## 📊 实验亮点

在七个真实数据集上的实验结果表明，CaPulse在AUROC指标上相较于现有方法提升了3%至17%，显示出显著的性能优势。此外，模型的可解释性也得到了增强，便于用户理解异常检测的原因。

## 🎯 应用场景

CaPulse框架具有广泛的应用潜力，尤其适用于金融监测、工业设备故障检测和网络安全等领域。通过有效检测异常，能够帮助企业及时识别潜在风险，优化资源配置，并提升决策效率。未来，该方法可能在更多复杂动态系统中发挥重要作用。

## 📄 摘要（原文）

> Time series anomaly detection has garnered considerable attention across diverse domains. While existing methods often fail to capture the underlying mechanisms behind anomaly generation in time series data. In addition, time series anomaly detection often faces several data-related inherent challenges, i.e., label scarcity, data imbalance, and complex multi-periodicity. In this paper, we leverage causal tools and introduce a new causality-based framework, CaPulse, which tunes in to the underlying causal pulse of time series data to effectively detect anomalies. Concretely, we begin by building a structural causal model to decipher the generation processes behind anomalies. To tackle the challenges posed by the data, we propose Periodical Normalizing Flows with a novel mask mechanism and carefully designed periodical learners, creating a periodicity-aware, density-based anomaly detection approach. Extensive experiments on seven real-world datasets demonstrate that CaPulse consistently outperforms existing methods, achieving AUROC improvements of 3% to 17%, with enhanced interpretability.

