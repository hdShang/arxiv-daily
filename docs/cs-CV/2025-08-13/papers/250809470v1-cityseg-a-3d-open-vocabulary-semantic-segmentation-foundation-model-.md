---
layout: default
title: "CitySeg: A 3D Open Vocabulary Semantic Segmentation Foundation Model in City-scale Scenarios"
---

# CitySeg: A 3D Open Vocabulary Semantic Segmentation Foundation Model in City-scale Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09470" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09470v1</a>
  <a href="https://arxiv.org/pdf/2508.09470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09470v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09470v1', 'CitySeg: A 3D Open Vocabulary Semantic Segmentation Foundation Model in City-scale Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialei Xu, Zizhuang Wei, Weikang You, Linyun Li, Weijian Sun

**分类**: cs.CV

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出CitySeg以解决城市规模点云语义分割问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市规模点云` `语义分割` `无人机感知` `开放词汇` `零样本推理` `交叉注意力网络` `分层分类`

## 📋 核心要点

1. 现有的城市规模点云语义分割模型受限于3D数据规模和领域差距，导致泛化能力不足。
2. 提出CitySeg模型，通过结合文本模态和局部-全局交叉注意力网络，增强点云的语义分割能力。
3. 实验结果显示，CitySeg在九个基准测试中达到了最先进的性能，并首次实现了零样本推理。

## 📝 摘要（中文）

城市规模点云的语义分割是无人机感知系统中的关键技术，能够在不依赖视觉信息的情况下实现3D点的分类，从而实现全面的3D理解。然而，现有模型常受到3D数据规模有限和数据集之间领域差距的限制，导致泛化能力下降。为了解决这些挑战，本文提出了CitySeg，一个城市规模点云语义分割的基础模型，结合文本模态实现开放词汇分割和零样本推理。通过定制数据预处理规则和提出局部-全局交叉注意力网络，增强无人机场景中的点网络感知能力。此外，引入分层分类策略以解决数据集间语义标签不一致的问题。实验结果表明，CitySeg在九个闭集基准上实现了最先进的性能，显著超越现有方法，并首次在城市规模点云场景中实现了零样本泛化。

## 🔬 方法详解

**问题定义**：本文旨在解决城市规模点云语义分割中的泛化能力不足问题，现有方法往往受限于数据规模和领域差异，导致性能下降。

**核心思路**：CitySeg通过引入文本模态实现开放词汇分割，并采用局部-全局交叉注意力网络来增强模型的感知能力，旨在提高模型在不同数据集上的适应性。

**技术框架**：CitySeg的整体架构包括数据预处理模块、局部-全局交叉注意力网络、分层分类策略和两阶段训练策略。数据预处理模块定制规则以应对非均匀数据分布，交叉注意力网络则增强特征提取能力。

**关键创新**：引入分层分类策略和图编码器来解决不同数据集间的语义标签不一致问题，这是与现有方法的本质区别。该策略通过建立分层图来整合数据标签，提升了模型的分类能力。

**关键设计**：采用了两阶段训练策略，并使用铰链损失函数来增强子类别特征的可分性。这些设计使得模型在处理复杂场景时表现更加优越。

## 📊 实验亮点

实验结果表明，CitySeg在九个闭集基准测试中实现了最先进的性能，显著超越现有方法，具体提升幅度达到XX%（具体数据未知）。此外，CitySeg首次在城市规模点云场景中实现了零样本推理，展示了其强大的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括城市规划、智能交通、环境监测等，能够为无人机在复杂城市环境中的自主导航和决策提供支持。未来，CitySeg有望推动城市规模点云分析技术的发展，提升智能城市建设的效率和精度。

## 📄 摘要（原文）

> Semantic segmentation of city-scale point clouds is a critical technology for Unmanned Aerial Vehicle (UAV) perception systems, enabling the classification of 3D points without relying on any visual information to achieve comprehensive 3D understanding. However, existing models are frequently constrained by the limited scale of 3D data and the domain gap between datasets, which lead to reduced generalization capability. To address these challenges, we propose CitySeg, a foundation model for city-scale point cloud semantic segmentation that incorporates text modality to achieve open vocabulary segmentation and zero-shot inference. Specifically, in order to mitigate the issue of non-uniform data distribution across multiple domains, we customize the data preprocessing rules, and propose a local-global cross-attention network to enhance the perception capabilities of point networks in UAV scenarios. To resolve semantic label discrepancies across datasets, we introduce a hierarchical classification strategy. A hierarchical graph established according to the data annotation rules consolidates the data labels, and the graph encoder is used to model the hierarchical relationships between categories. In addition, we propose a two-stage training strategy and employ hinge loss to increase the feature separability of subcategories. Experimental results demonstrate that the proposed CitySeg achieves state-of-the-art (SOTA) performance on nine closed-set benchmarks, significantly outperforming existing approaches. Moreover, for the first time, CitySeg enables zero-shot generalization in city-scale point cloud scenarios without relying on visual information.

