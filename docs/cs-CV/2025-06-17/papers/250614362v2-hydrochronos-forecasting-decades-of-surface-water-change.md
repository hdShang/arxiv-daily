---
layout: default
title: "HydroChronos: Forecasting Decades of Surface Water Change"
---

# HydroChronos: Forecasting Decades of Surface Water Change

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14362" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14362v2</a>
  <a href="https://arxiv.org/pdf/2506.14362.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14362v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14362v2', 'HydroChronos: Forecasting Decades of Surface Water Change')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniele Rege Cambrin, Eleonora Poeta, Eliana Pastor, Isaac Corley, Tania Cerquitelli, Elena Baralis, Paolo Garza

**分类**: cs.CV

**发布日期**: 2025-06-17 (更新: 2025-08-07)

**备注**: Accepted to SIGSPATIAL 2025

**DOI**: [10.1145/3748636.3762732](https://doi.org/10.1145/3748636.3762732)

---

## 💡 一句话要点

**提出HydroChronos以解决水体动态预测数据不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `水体动态预测` `多模态数据集` `气候变化适应` `深度学习` `可解释人工智能`

## 📋 核心要点

1. 现有水体动态预测方法缺乏全面的数据集和标准化基准，限制了研究的深入和应用。
2. HydroChronos数据集结合了多种数据源，并提出了AquaClimaTempo UNet模型，专注于气候数据的整合与分析。
3. 实验结果显示，提出的模型在多个预测任务中均显著优于传统基线，提升了预测的准确性和可靠性。

## 📝 摘要（中文）

预测水体动态对于水资源管理和气候变化适应至关重要。然而，该领域缺乏全面的数据集和标准化的基准。本文介绍了HydroChronos，这是一个大规模的多模态时空数据集，旨在填补这一空白。该数据集包含超过三十年的Landsat 5和Sentinel-2影像、气候数据和数字高程模型，覆盖欧洲、北美和南美的多种湖泊和河流。我们还提出了AquaClimaTempo UNet，这是一种具有专门气候数据分支的新型时空架构，作为强基准模型。我们的模型在未来水动态预测方面显著优于持久性基线，变化检测和变化方向分类任务的F1提升分别为14%和11%，变化幅度回归的MAE提升为0.1。最后，我们进行了可解释人工智能分析，以识别影响水体变化的关键气候变量和输入通道，为未来建模工作提供了指导。

## 🔬 方法详解

**问题定义**：本文旨在解决水体动态预测中数据不足和缺乏标准化基准的问题。现有方法通常依赖于有限的数据集，导致预测结果的可靠性不足。

**核心思路**：通过构建HydroChronos数据集，整合多种时空数据，结合AquaClimaTempo UNet模型，专注于气候数据的影响，从而提升水体动态预测的准确性。

**技术框架**：该方法包括数据收集、数据预处理、模型构建和预测评估四个主要阶段。数据收集阶段整合了Landsat 5、Sentinel-2影像、气候数据和数字高程模型，模型构建阶段采用了具有气候数据分支的UNet架构。

**关键创新**：HydroChronos数据集的构建和AquaClimaTempo UNet模型的提出是本研究的核心创新，特别是模型中对气候数据的专门处理，使其在预测任务中表现优异。

**关键设计**：模型采用了多模态输入，损失函数设计考虑了不同任务的特性，网络结构上引入了气候数据分支，以增强模型对气候变化的敏感性。具体参数设置和超参数调优在实验中进行了详细验证。

## 📊 实验亮点

实验结果表明，AquaClimaTempo UNet模型在变化检测和变化方向分类任务中，F1值分别提升了14%和11%，在变化幅度回归任务中，MAE提升了0.1，显著优于持久性基线，展示了模型的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括水资源管理、气候变化适应策略制定及生态环境监测等。通过提供准确的水体动态预测，HydroChronos可以帮助决策者制定更有效的水资源管理政策，提升应对气候变化的能力，促进可持续发展。

## 📄 摘要（原文）

> Forecasting surface water dynamics is crucial for water resource management and climate change adaptation. However, the field lacks comprehensive datasets and standardized benchmarks. In this paper, we introduce HydroChronos, a large-scale, multi-modal spatiotemporal dataset for surface water dynamics forecasting designed to address this gap. We couple the dataset with three forecasting tasks. The dataset includes over three decades of aligned Landsat 5 and Sentinel-2 imagery, climate data, and Digital Elevation Models for diverse lakes and rivers across Europe, North America, and South America. We also propose AquaClimaTempo UNet, a novel spatiotemporal architecture with a dedicated climate data branch, as a strong benchmark baseline. Our model significantly outperforms a Persistence baseline for forecasting future water dynamics by +14% and +11% F1 across change detection and direction of change classification tasks, and by +0.1 MAE on the magnitude of change regression. Finally, we conduct an Explainable AI analysis to identify the key climate variables and input channels that influence surface water change, providing insights to inform and guide future modeling efforts.

