---
layout: default
title: EuroMineNet: A Multitemporal Sentinel-2 Benchmark for Spatiotemporal Mining Footprint Analysis in the European Union (2015-2024)
---

# EuroMineNet: A Multitemporal Sentinel-2 Benchmark for Spatiotemporal Mining Footprint Analysis in the European Union (2015-2024)

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14661" target="_blank" class="toolbar-btn">arXiv: 2510.14661v1</a>
    <a href="https://arxiv.org/pdf/2510.14661.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14661v1" 
            onclick="toggleFavorite(this, '2510.14661v1', 'EuroMineNet: A Multitemporal Sentinel-2 Benchmark for Spatiotemporal Mining Footprint Analysis in the European Union (2015-2024)')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Weikang Yu, Vincent Nwazelibe, Xianping Ma, Xiaokang Zhang, Richard Gloaguen, Xiao Xiang Zhu, Pedram Ghamisi

**分类**: cs.CV

**发布日期**: 2025-10-16

**🔗 代码/项目**: [GITHUB](https://github.com/EricYu97/EuroMineNet)

---

## 💡 一句话要点

**EuroMineNet：欧盟多时相Sentinel-2矿区时空足迹分析基准数据集**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `矿区监测` `多时相遥感` `土地利用变化` `深度学习` `环境可持续性` `GeoAI` `Sentinel-2` `时空数据挖掘`

## 📋 核心要点

1. 现有矿区监测数据集在时间跨度和地理覆盖范围上存在局限性，难以支持对环境动态的长期分析。
2. EuroMineNet提供了一个多时相、大规模的矿区足迹基准数据集，包含欧盟133个矿区2015-2024年的年度观测数据。
3. 通过基准测试20个深度学习模型，揭示了GeoAI在识别长期环境变化方面的有效性，以及在检测短期动态方面的挑战。

## 📝 摘要（中文）

采矿活动对工业和经济发展至关重要，但也是环境退化的主要来源，导致森林砍伐、土壤侵蚀和水污染。可持续资源管理和环境治理需要对采矿引起的地表变化进行长期监测，但现有数据集通常在时间深度或地理范围上受到限制。为了解决这一差距，我们提出了EuroMineNet，这是第一个基于Sentinel-2多光谱图像的综合性多时相基准，用于矿区足迹mapping和监测。EuroMineNet覆盖欧盟的133个矿区，提供2015年至2024年的年度观测数据和专家验证的注释，使基于GeoAI的模型能够在欧洲大陆范围内分析环境动态。它支持两个可持续性驱动的任务：（1）多时相矿区足迹mapping，用于一致的年度土地利用划分，使用一种新的Change-Aware Temporal IoU（CA-TIoU）指标进行评估，以及（2）跨时相变化检测，以捕获渐进和突发的地表转换。对20个最先进的深度学习模型进行基准测试表明，虽然GeoAI方法有效地识别了长期环境变化，但在检测对及时缓解至关重要的短期动态方面仍然存在挑战。通过推进时间上一致且可解释的采矿监测，EuroMineNet有助于可持续土地利用管理、环境复原力以及将GeoAI应用于社会和环境利益的更广泛目标。我们通过与FAIR和开放科学范式对齐，在https://github.com/EricYu97/EuroMineNet 上发布代码和数据集。

## 🔬 方法详解

**问题定义**：论文旨在解决欧盟范围内矿区环境影响监测的问题。现有数据集的时间跨度和地理范围有限，难以支持对矿区长期环境变化的有效分析。此外，现有方法在检测短期环境动态方面存在不足，无法及时进行环境风险预警和干预。

**核心思路**：论文的核心思路是构建一个高质量、多时相的矿区遥感数据集，并利用GeoAI模型进行矿区足迹mapping和变化检测。通过提供长期、连续的观测数据，促进对矿区环境动态的深入理解，并为可持续土地利用管理提供支持。

**技术框架**：EuroMineNet数据集包含欧盟133个矿区2015-2024年的Sentinel-2多光谱图像，以及专家验证的年度矿区足迹注释。该数据集支持两个主要任务：多时相矿区足迹mapping和跨时相变化检测。研究人员使用该数据集对20个深度学习模型进行了基准测试，并使用Change-Aware Temporal IoU (CA-TIoU)指标评估了模型性能。

**关键创新**：该论文的关键创新在于构建了EuroMineNet数据集，这是第一个综合性的多时相矿区足迹基准数据集，覆盖了欧盟范围内的多个矿区，并提供了长达十年的年度观测数据。此外，论文还提出了Change-Aware Temporal IoU (CA-TIoU)指标，用于评估多时相矿区足迹mapping的性能。

**关键设计**：数据集的构建遵循FAIR原则，保证了数据的可查找性、可访问性、互操作性和可重用性。在模型评估方面，论文选择了20个具有代表性的深度学习模型，并使用CA-TIoU指标对模型的时序一致性进行了评估。数据集和代码已开源，方便研究人员使用和扩展。

## 📊 实验亮点

论文通过对20个深度学习模型进行基准测试，发现GeoAI方法在识别长期环境变化方面表现良好，但在检测短期动态方面仍存在挑战。实验结果表明，需要进一步研究更有效的时序建模方法，以提高矿区环境变化的检测精度和及时性。CA-TIoU指标能够有效评估模型在多时相mapping中的时序一致性。

## 🎯 应用场景

EuroMineNet数据集可用于矿区环境监测、土地利用规划、环境风险评估和可持续资源管理等领域。该数据集能够帮助政府部门和企业更好地了解矿区环境变化趋势，制定更有效的环境保护政策和措施，促进矿业的可持续发展。

## 📄 摘要（原文）

> Mining activities are essential for industrial and economic development, but remain a leading source of environmental degradation, contributing to deforestation, soil erosion, and water contamination. Sustainable resource management and environmental governance require consistent, long-term monitoring of mining-induced land surface changes, yet existing datasets are often limited in temporal depth or geographic scope. To address this gap, we present EuroMineNet, the first comprehensive multitemporal benchmark for mining footprint mapping and monitoring based on Sentinel-2 multispectral imagery. Spanning 133 mining sites across the European Union, EuroMineNet provides annual observations and expert-verified annotations from 2015 to 2024, enabling GeoAI-based models to analyze environmental dynamics at a continental scale. It supports two sustainability-driven tasks: (1) multitemporal mining footprint mapping for consistent annual land-use delineation, evaluated with a novel Change-Aware Temporal IoU (CA-TIoU) metric, and (2) cross-temporal change detection to capture both gradual and abrupt surface transformations. Benchmarking 20 state-of-the-art deep learning models reveals that while GeoAI methods effectively identify long-term environmental changes, challenges remain in detecting short-term dynamics critical for timely mitigation. By advancing temporally consistent and explainable mining monitoring, EuroMineNet contributes to sustainable land-use management, environmental resilience, and the broader goal of applying GeoAI for social and environmental good. We release the codes and datasets by aligning with FAIR and the open science paradigm at https://github.com/EricYu97/EuroMineNet.

