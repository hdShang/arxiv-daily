---
layout: default
title: "Look to Locate: Vision-Based Multisensory Navigation with 3-D Digital Maps for GNSS-Challenged Environments"
---

# Look to Locate: Vision-Based Multisensory Navigation with 3-D Digital Maps for GNSS-Challenged Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19827" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19827v1</a>
  <a href="https://arxiv.org/pdf/2506.19827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19827v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19827v1', 'Look to Locate: Vision-Based Multisensory Navigation with 3-D Digital Maps for GNSS-Challenged Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ola Elmaghraby, Eslam Mounier, Paulo Ricardo Marques de Araujo, Aboelmagd Noureldin

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-24

---

## 💡 一句话要点

**提出基于视觉的多传感器导航系统以解决GNSS受限环境中的定位问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉导航` `多传感器融合` `单目深度估计` `三维地图` `GNSS独立定位`

## 📋 核心要点

1. 在GNSS受限环境中，现有定位方法面临准确性和鲁棒性不足的挑战。
2. 提出了一种结合单目深度估计和三维数字地图的多传感器导航系统，以提高定位精度。
3. 实验结果显示，室内外定位精度分别达到92%和80%，并显著减少了定位漂移。

## 📝 摘要（中文）

在全球导航卫星系统（GNSS）受限的环境中，如室内停车场或密集城市峡谷，准确和可靠的车辆定位仍然是一个重大挑战。本文提出了一种具有成本效益的基于视觉的多传感器导航系统，该系统结合了单目深度估计、语义过滤和视觉地图注册（VMR）与三维数字地图。通过在真实的室内和室外驾驶场景中进行广泛测试，证明了该系统的有效性，室内定位精度达到92%的亚米级，室外超过80%，水平定位和航向的均方根误差分别约为0.98米和1.25度。与所考察的基线相比，该解决方案显著减少了漂移，并在各种条件下提高了鲁棒性，平均定位精度提升约88%。这项工作突显了结合三维地图的成本效益单目视觉系统在陆地车辆中实现可扩展、独立于GNSS的导航的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决在GNSS受限环境中，车辆定位准确性和鲁棒性不足的问题。现有方法在复杂场景中容易出现漂移和定位不稳定。

**核心思路**：论文提出通过结合单目深度估计、语义过滤和视觉地图注册（VMR）与三维数字地图，来实现高效的多传感器导航。这种设计旨在利用视觉信息来补充GNSS的不足。

**技术框架**：整体架构包括三个主要模块：单目深度估计模块用于获取环境深度信息，语义过滤模块用于提取重要特征，视觉地图注册模块用于将实时数据与三维地图进行匹配。

**关键创新**：最重要的技术创新在于将单目视觉系统与三维地图结合，显著提高了在GNSS受限环境中的定位精度和鲁棒性。这与传统的多传感器融合方法有本质区别。

**关键设计**：在参数设置上，采用了优化的损失函数以提高深度估计的准确性，并设计了适应性强的网络结构，以便于在不同环境下进行有效的特征提取和匹配。

## 📊 实验亮点

实验结果显示，所提出的系统在室内环境中实现了92%的亚米级定位精度，室外环境中超过80%。与基线方法相比，平均定位精度提升约88%，并且在不同条件下表现出更强的鲁棒性，显著减少了漂移现象。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和智能交通系统等。通过提供高精度的定位解决方案，能够在GNSS信号弱或缺失的环境中实现安全可靠的导航，具有重要的实际价值和广泛的市场前景。

## 📄 摘要（原文）

> In Global Navigation Satellite System (GNSS)-denied environments such as indoor parking structures or dense urban canyons, achieving accurate and robust vehicle positioning remains a significant challenge. This paper proposes a cost-effective, vision-based multi-sensor navigation system that integrates monocular depth estimation, semantic filtering, and visual map registration (VMR) with 3-D digital maps. Extensive testing in real-world indoor and outdoor driving scenarios demonstrates the effectiveness of the proposed system, achieving sub-meter accuracy of 92% indoors and more than 80% outdoors, with consistent horizontal positioning and heading average root mean-square errors of approximately 0.98 m and 1.25 °, respectively. Compared to the baselines examined, the proposed solution significantly reduced drift and improved robustness under various conditions, achieving positioning accuracy improvements of approximately 88% on average. This work highlights the potential of cost-effective monocular vision systems combined with 3D maps for scalable, GNSS-independent navigation in land vehicles.

