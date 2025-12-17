---
layout: default
title: A Stochastic Approach to Terrain Maps for Safe Lunar Landing
---

# A Stochastic Approach to Terrain Maps for Safe Lunar Landing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.12058" class="toolbar-btn" target="_blank">📄 arXiv: 2512.12058v1</a>
  <a href="https://arxiv.org/pdf/2512.12058.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12058v1" onclick="toggleFavorite(this, '2512.12058v1', 'A Stochastic Approach to Terrain Maps for Safe Lunar Landing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anja Sheppard, Chris Reale, Katherine A. Skinner

**分类**: cs.RO

**发布日期**: 2025-12-12

**备注**: Accepted to IEEE Aerospace 2026

---

## 💡 一句话要点

**提出一种基于高斯过程的两阶段随机地形图方法，用于月球安全着陆。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `月球着陆` `地形建模` `高斯过程` `不确定性估计` `数字高程模型` `异方差噪声` `随机变分推断`

## 📋 核心要点

1. 传统月球着陆依赖视觉的危险检测方法在光照不足的南极区域失效，且激光雷达在月球环境中的可靠性未知，因此需要更稳健的地形建模方法。
2. 该论文提出一种两阶段高斯过程模型，利用LRO的DEM置信度数据学习空间变化的噪声特征，并将其用于指导地形建模，从而更准确地估计地形不确定性。
3. 通过利用高斯过程，该方法能够更准确地模拟异方差传感器噪声对高程图的影响，从而产生更具信息性的地形不确定性估计，可用于危险检测和安全着陆点选择。

## 📝 摘要（中文）

在月球表面安全着陆极具挑战性，尤其是在阴影密布的南极区域，传统的基于视觉的危险检测方法并不可靠。月球南极可能存在有价值的资源，使得在该区域着陆成为许多航天机构和商业公司的高度优先事项。然而，在下降过程中依赖激光雷达进行危险检测存在风险，因为该技术在月球环境中尚未经过充分测试。月球勘测轨道飞行器（LRO）积累了丰富的月球表面数据，可用于在下降之前创建信息丰富的先验地图。本文提出了一种利用高斯过程（GP）从LRO数据生成随机高程图的方法。高斯过程是一种强大的贝叶斯非参数建模框架，可生成伴随的不确定性估计。在诸如自主航天等高风险环境中，对地形不确定性的可解释估计至关重要。然而，以往的随机高程图方法均未考虑LRO数字高程模型（DEM）置信度图，尽管该数据包含有关不同区域DEM质量的关键信息。为了解决这一差距，我们引入了一种两阶段GP模型，其中辅助GP从DEM置信度数据中学习空间变化的噪声特征。然后，该异方差信息用于告知主GP的噪声参数，该主GP对月球地形进行建模。此外，我们使用随机变分GP来实现可扩展的训练。通过利用GP，我们能够更准确地模拟异方差传感器噪声对最终高程图的影响。因此，我们的方法产生更具信息性的地形不确定性，可用于下游任务，例如危险检测和安全着陆点选择。

## 🔬 方法详解

**问题定义**：论文旨在解决月球南极地区安全着陆的问题，该区域光照条件差，传统视觉方法失效，且激光雷达的可靠性存疑。现有的随机高程图方法忽略了LRO数字高程模型（DEM）置信度图中的关键信息，导致地形不确定性估计不准确。

**核心思路**：核心思路是利用高斯过程（GP）对月球地形进行建模，并引入一个两阶段的GP模型来考虑DEM置信度数据。通过学习DEM置信度数据中的空间变化的噪声特征，可以更准确地估计地形的不确定性。这样设计的目的是为了提高地形建模的精度和可靠性，从而为安全着陆提供更好的保障。

**技术框架**：整体框架包含两个主要阶段：第一阶段，使用一个辅助GP从DEM置信度数据中学习空间变化的噪声特征。第二阶段，将这些噪声特征作为先验信息，用于指导主GP对月球地形进行建模。为了实现可扩展的训练，使用了随机变分GP。整个流程旨在利用DEM置信度信息来提高地形建模的准确性。

**关键创新**：最重要的技术创新点在于引入了两阶段GP模型，该模型能够有效地利用DEM置信度数据来建模空间变化的噪声特征。与现有方法相比，该方法能够更准确地估计地形的不确定性，从而为危险检测和安全着陆点选择提供更可靠的信息。这是现有随机高程图方法所忽略的。

**关键设计**：关键设计包括：1) 使用高斯过程进行地形建模，利用其贝叶斯特性提供不确定性估计；2) 设计两阶段GP模型，其中辅助GP学习DEM置信度数据中的噪声特征；3) 使用随机变分GP实现可扩展的训练。具体参数设置和损失函数等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

摘要中未提供具体的实验结果或性能数据。但该方法的核心优势在于能够利用DEM置信度数据来提高地形不确定性估计的准确性，从而为下游任务（如危险检测和安全着陆点选择）提供更可靠的信息。具体的性能提升幅度未知。

## 🎯 应用场景

该研究成果可应用于未来的月球探测任务，尤其是在光照条件恶劣的月球南极地区。通过提供更准确的地形不确定性估计，可以提高着陆的安全性，并为选择合适的着陆点提供依据。此外，该方法还可以推广到其他行星或卫星的探测任务中，具有广泛的应用前景。

## 📄 摘要（原文）

> Safely landing on the lunar surface is a challenging task, especially in the heavily-shadowed South Pole region where traditional vision-based hazard detection methods are not reliable. The potential existence of valuable resources at the lunar South Pole has made landing in that region a high priority for many space agencies and commercial companies. However, relying on a LiDAR for hazard detection during descent is risky, as this technology is fairly untested in the lunar environment.
>   There exists a rich log of lunar surface data from the Lunar Reconnaissance Orbiter (LRO), which could be used to create informative prior maps of the surface before descent. In this work, we propose a method for generating stochastic elevation maps from LRO data using Gaussian processes (GPs), which are a powerful Bayesian framework for non-parametric modeling that produce accompanying uncertainty estimates. In high-risk environments such as autonomous spaceflight, interpretable estimates of terrain uncertainty are critical. However, no previous approaches to stochastic elevation mapping have taken LRO Digital Elevation Model (DEM) confidence maps into account, despite this data containing key information about the quality of the DEM in different areas.
>   To address this gap, we introduce a two-stage GP model in which a secondary GP learns spatially varying noise characteristics from DEM confidence data. This heteroscedastic information is then used to inform the noise parameters for the primary GP, which models the lunar terrain. Additionally, we use stochastic variational GPs to enable scalable training. By leveraging GPs, we are able to more accurately model the impact of heteroscedastic sensor noise on the resulting elevation map. As a result, our method produces more informative terrain uncertainty, which can be used for downstream tasks such as hazard detection and safe landing site selection.

