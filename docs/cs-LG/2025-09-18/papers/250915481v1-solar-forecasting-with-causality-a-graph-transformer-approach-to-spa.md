---
layout: default
title: "Solar Forecasting with Causality: A Graph-Transformer Approach to Spatiotemporal Dependencies"
---

# Solar Forecasting with Causality: A Graph-Transformer Approach to Spatiotemporal Dependencies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15481" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15481v1</a>
  <a href="https://arxiv.org/pdf/2509.15481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15481v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15481v1', 'Solar Forecasting with Causality: A Graph-Transformer Approach to Spatiotemporal Dependencies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanan Niu, Demetri Psaltis, Christophe Moser, Luisa Lambertini

**分类**: cs.LG, cs.SI

**发布日期**: 2025-09-18

**备注**: Accepted to CIKM 2025

**期刊**: Proceedings of the 34th ACM International Conference on Information and Knowledge Management (CIKM '25), November 10--14, 2025, Seoul, Republic of Korea

**DOI**: [10.1145/3746252.3760905](https://doi.org/10.1145/3746252.3760905)

---

## 💡 一句话要点

**SolarCAST：利用因果图Transformer预测太阳辐射，无需专用硬件。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `太阳能预测` `因果推理` `图神经网络` `Transformer` `时空建模`

## 📋 核心要点

1. 现有太阳能预测方法依赖专用硬件（如天空相机或卫星图像），成本高昂且预处理复杂。
2. SolarCAST利用因果关系，通过图神经网络和Transformer建模时空依赖，仅需公开的GHI数据。
3. 实验表明，SolarCAST在不同地理条件下均优于现有方法，且比商业预测器Solcast误差降低25.9%。

## 📝 摘要（中文）

本文提出了一种名为SolarCAST的因果驱动模型，用于预测目标地点的未来全球水平辐照度(GHI)。与依赖天空相机或卫星图像的现有方法不同，SolarCAST仅使用目标地点X和附近站点S的历史GHI数据，无需专用硬件和大量预处理。为了仅使用公共传感器数据实现高精度，SolarCAST使用可扩展的神经组件对X-S相关性背后的三类混淆因素进行建模：(i)可观察的同步变量(例如，时间、站点身份)，通过嵌入模块处理；(ii)潜在的同步因素(例如，区域天气模式)，由时空图神经网络捕获；(iii)时滞影响(例如，跨站点的云移动)，使用门控Transformer建模，学习时间偏移。在不同的地理条件下，SolarCAST优于领先的时间序列和多模态基线，并且比顶级商业预测器Solcast的误差降低了25.9%。SolarCAST为局部太阳能预测提供了一种轻量级、实用且通用的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决太阳能预测问题，特别是如何仅利用公开可用的历史全球水平辐照度(GHI)数据，在无需昂贵设备和复杂预处理的情况下，实现高精度的局部太阳能预测。现有方法通常依赖天空相机或卫星图像，这些方法成本高昂，且数据预处理复杂，限制了其广泛应用。

**核心思路**：SolarCAST的核心思路是利用因果关系建模站点之间的时空依赖性。它假设站点之间的GHI相关性受到多种混淆因素的影响，包括可观测的同步变量（如时间）、潜在的同步因素（如区域天气模式）和时滞影响（如云移动）。通过显式地建模这些混淆因素，SolarCAST能够更准确地预测目标站点的GHI。

**技术框架**：SolarCAST的整体框架包括三个主要模块：(1)嵌入模块，用于处理可观测的同步变量，如时间和站点身份；(2)时空图神经网络，用于捕获潜在的同步因素，如区域天气模式；(3)门控Transformer，用于建模时滞影响，如云移动。这三个模块协同工作，共同预测目标站点的未来GHI。

**关键创新**：SolarCAST的关键创新在于其因果驱动的时空建模方法。与传统的黑盒时间序列模型不同，SolarCAST显式地建模了站点之间的因果关系，并考虑了多种混淆因素的影响。此外，SolarCAST还采用了图神经网络和Transformer等先进的深度学习技术，以有效地捕获复杂的时空依赖性。

**关键设计**：SolarCAST的关键设计包括：(1)使用图神经网络建模站点之间的空间关系，其中节点表示站点，边表示站点之间的相关性；(2)使用门控Transformer建模时间序列数据，其中门控机制用于控制信息的流动；(3)使用因果推理技术来识别和消除混淆因素的影响；(4)损失函数采用均方误差(MSE)，优化器采用Adam。

## 📊 实验亮点

SolarCAST在多个真实世界的太阳能数据集上进行了评估，结果表明其性能优于领先的时间序列和多模态基线。最显著的成果是，SolarCAST比顶级商业预测器Solcast的误差降低了25.9%，证明了其在实际应用中的巨大潜力。该模型在不同地理条件下均表现出良好的泛化能力。

## 🎯 应用场景

SolarCAST可应用于各种太阳能相关的场景，例如太阳能电站的发电预测、电网调度优化、能源交易决策等。通过提供准确的太阳能预测，SolarCAST可以帮助提高太阳能的利用效率，降低能源成本，并促进可再生能源的普及。该模型轻量级且易于部署，尤其适用于资源有限的地区。

## 📄 摘要（原文）

> Accurate solar forecasting underpins effective renewable energy management. We present SolarCAST, a causally informed model predicting future global horizontal irradiance (GHI) at a target site using only historical GHI from site X and nearby stations S - unlike prior work that relies on sky-camera or satellite imagery requiring specialized hardware and heavy preprocessing. To deliver high accuracy with only public sensor data, SolarCAST models three classes of confounding factors behind X-S correlations using scalable neural components: (i) observable synchronous variables (e.g., time of day, station identity), handled via an embedding module; (ii) latent synchronous factors (e.g., regional weather patterns), captured by a spatio-temporal graph neural network; and (iii) time-lagged influences (e.g., cloud movement across stations), modeled with a gated transformer that learns temporal shifts. It outperforms leading time-series and multimodal baselines across diverse geographical conditions, and achieves a 25.9% error reduction over the top commercial forecaster, Solcast. SolarCAST offers a lightweight, practical, and generalizable solution for localized solar forecasting.

