---
layout: default
title: "GeoMAE: Masking Representation Learning for Spatio-Temporal Graph Forecasting with Missing Values"
---

# GeoMAE: Masking Representation Learning for Spatio-Temporal Graph Forecasting with Missing Values

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14083" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14083v2</a>
  <a href="https://arxiv.org/pdf/2508.14083.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14083v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14083v2', 'GeoMAE: Masking Representation Learning for Spatio-Temporal Graph Forecasting with Missing Values')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Songyu Ke, Chenyu Wu, Yuxuan Liang, Huiling Qin, Junbo Zhang, Yu Zheng

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-13 (更新: 2025-12-02)

**备注**: 34 pages

---

## 💡 一句话要点

**提出GeoMAE以解决城市智能系统中的缺失数据问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `时空图预测` `缺失数据` `自监督学习` `掩码自编码器` `交通预测` `能源消耗预测`

## 📋 核心要点

1. 现有时空图预测方法对缺失数据的处理仍存在不足，尤其是忽视了动态空间相关性和缺失模式的复杂性。
2. GeoMAE模型通过自监督学习和掩码自编码器的灵感，设计了一个强大的时空表示学习框架，能够有效处理缺失数据。
3. 实验结果表明，GeoMAE在多个真实数据集上显著优于现有基线，提升幅度最高可达13.20%。

## 📝 摘要（中文）

城市智能系统中缺失数据的普遍存在，主要由于不良环境条件和设备故障，给交通预测和能源消耗预测等下游应用的有效性带来了重大挑战。因此，开发一种能够从不完整数据集中提取有意义见解的强大时空学习方法显得尤为重要。尽管已有针对缺失值的时空图预测方法，但仍存在未解决的问题，尤其是现有研究大多基于时间序列分析，忽视了传感器网络中固有的动态空间相关性。为应对这些挑战，本文提出了GeoMAE，一个自监督的时空表示学习模型，通过引入基于掩码自编码器的辅助学习任务，增强时空表示学习的鲁棒性。实证评估表明，GeoMAE在真实世界数据集上的表现显著优于现有基准，最佳基线模型的相对提升达到13.20%。

## 🔬 方法详解

**问题定义**：本文旨在解决城市智能系统中缺失数据对时空图预测的影响。现有方法多基于时间序列分析，未能有效考虑传感器网络的动态空间相关性，且缺失数据模式复杂，影响模型的泛化能力。

**核心思路**：GeoMAE通过自监督学习框架，结合掩码自编码器的思想，增强了时空表示学习的鲁棒性，能够从不完整数据中提取有效信息。

**技术框架**：GeoMAE模型主要由三个模块组成：输入预处理模块、基于注意力机制的时空预测网络（STAFN）和辅助学习任务。输入预处理模块负责数据的清洗和格式化，STAFN则通过注意力机制捕捉时空特征，辅助学习任务则通过掩码策略提升模型的学习能力。

**关键创新**：GeoMAE的核心创新在于引入了自监督学习机制和掩码自编码器的设计，显著提高了模型在处理缺失数据时的表现，与传统方法相比，能够更好地捕捉动态空间关系。

**关键设计**：模型的损失函数设计考虑了缺失值的影响，采用了加权损失策略，以确保模型在训练过程中对缺失数据的鲁棒性。同时，网络结构中引入了多层注意力机制，以增强时空特征的提取能力。

## 📊 实验亮点

GeoMAE在多个真实世界数据集上的实验结果显示，相较于最佳基线模型，其性能提升达13.20%。这一显著的提升表明，GeoMAE在处理缺失数据方面的有效性和鲁棒性，超越了现有的时空图预测方法。

## 🎯 应用场景

GeoMAE模型在城市交通预测、能源消耗预测等领域具有广泛的应用潜力。通过有效处理缺失数据，该模型能够为城市智能系统提供更准确的预测结果，从而优化资源配置和提高管理效率。未来，GeoMAE还可以扩展到其他领域，如环境监测和公共安全等，具有重要的实际价值和影响力。

## 📄 摘要（原文）

> The ubiquity of missing data in urban intelligence systems, attributable to adverse environmental conditions and equipment failures, poses a significant challenge to the efficacy of downstream applications, notably in the realms of traffic forecasting and energy consumption prediction.
>   Therefore, it is imperative to develop a robust spatio-temporal learning methodology capable of extracting meaningful insights from incomplete datasets. Despite the existence of methodologies for spatio-temporal graph forecasting in the presence of missing values, unresolved issues persist.
>   Primarily, the majority of extant research is predicated on time-series analysis, thereby neglecting the dynamic spatial correlations inherent in sensor networks.
>   Additionally, the complexity of missing data patterns compounds the intricacy of the problem.
>   Furthermore, the variability in maintenance conditions results in a significant fluctuation in the ratio and pattern of missing values, thereby challenging the generalizability of predictive models.
>   In response to these challenges, this study introduces GeoMAE, a self-supervised spatio-temporal representation learning model.
>   The model is comprised of three principal components: an input preprocessing module, an attention-based spatio-temporal forecasting network (STAFN), and an auxiliary learning task, which draws inspiration from Masking AutoEncoders to enhance the robustness of spatio-temporal representation learning.
>   Empirical evaluations on real-world datasets demonstrate that GeoMAE significantly outperforms existing benchmarks, achieving up to 13.20\% relative improvement over the best baseline models.

