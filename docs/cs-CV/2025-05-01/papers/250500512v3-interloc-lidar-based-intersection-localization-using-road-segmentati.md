---
layout: default
title: InterLoc: LiDAR-based Intersection Localization using Road Segmentation with Automated Evaluation Method
---

# InterLoc: LiDAR-based Intersection Localization using Road Segmentation with Automated Evaluation Method

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00512" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00512v3</a>
  <a href="https://arxiv.org/pdf/2505.00512.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00512v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00512v3', 'InterLoc: LiDAR-based Intersection Localization using Road Segmentation with Automated Evaluation Method')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nguyen Hoang Khoi Tran, Julie Stephany Berrio, Mao Shan, Zhenxing Ming, Stewart Worrall

**分类**: cs.CV, cs.RO

**发布日期**: 2025-05-01 (更新: 2025-07-16)

---

## 💡 一句话要点

**提出一种基于LiDAR的交叉口定位方法以解决自动驾驶中的定位挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `交叉口定位` `LiDAR` `自动驾驶` `语义分割` `在线定位` `鲁棒性` `自动化评估`

## 📋 核心要点

1. 现有交叉口定位方法往往忽视了车载传感器获取的丰富语义信息，且依赖于稀缺的手工标注数据集，导致定位精度不足。
2. 本文提出了一种基于LiDAR的在线交叉口定位方法，通过鸟瞰图表示检测交叉口候选点，并优化交叉口中心点。
3. 在SemanticKITTI数据集上的实验表明，该方法在准确性和可靠性上超越了最新的学习基线，展示了良好的鲁棒性。

## 📝 摘要（中文）

在线定位道路交叉口对自动驾驶车辆的定位、地图构建和运动规划具有重要意义。交叉口作为强有力的地标，有助于修正车辆姿态估计、将新传感器数据锚定到最新地图中，并指导车辆在道路网络图中的路径规划。尽管交叉口定位的重要性不言而喻，但现有方法往往忽视了车载计算的丰富语义信息，或依赖稀缺的手工标注交叉口数据集。为此，本文提出了一种新颖的基于LiDAR的在线车辆中心交叉口定位方法，通过鸟瞰图表示检测交叉口候选点，并通过分析交叉道路分支来优化交叉口中心点。我们还引入了一种自动化评估流程，将定位的交叉口点与OpenStreetMap交叉口节点配对。实验结果表明，该方法在准确性和可靠性上优于最新的学习基线。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶车辆在复杂环境中准确定位交叉口的问题。现有方法通常忽视了车载传感器所提供的语义信息，且依赖于有限的手工标注数据，导致定位效果不佳。

**核心思路**：论文提出的核心思路是利用LiDAR传感器获取的语义信息，通过鸟瞰图表示来检测交叉口候选点，并通过分析交叉道路的分支来优化交叉口的中心点位置。这样的设计能够充分利用已有的语义信息，提高定位的准确性。

**技术框架**：整体方法包括几个主要模块：首先，通过LiDAR传感器获取道路的语义扫描数据，并生成鸟瞰图表示；其次，检测交叉口候选点；最后，通过最小二乘法调整交叉口中心点。该流程确保了从数据获取到定位结果的高效性和准确性。

**关键创新**：本文的关键创新在于提出了一种结合语义信息和几何分析的交叉口定位方法，显著提高了定位的准确性和鲁棒性。这与传统方法依赖于手工标注数据的方式形成了鲜明对比。

**关键设计**：在方法设计中，采用了最小二乘法来优化交叉口中心点的位置，并通过自动化评估流程将定位结果与OpenStreetMap交叉口节点进行配对，确保了评估的准确性和高效性。

## 📊 实验亮点

实验结果显示，本文方法在准确性和可靠性方面超越了最新的学习基线，具体性能提升幅度达到XX%（具体数据未知）。此外，敏感性测试表明该方法对复杂的分割错误具有良好的鲁棒性，适用于实际应用场景。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶车辆的导航系统、智能交通管理以及城市规划等。通过提高交叉口定位的准确性，能够有效提升自动驾驶系统的安全性和可靠性，推动智能交通的发展。

## 📄 摘要（原文）

> Online localization of road intersections is beneficial for autonomous vehicle localization, mapping and motion planning. Intersections offer strong landmarks for correcting vehicle pose estimation, anchoring new sensor data in up-to-date maps, and guiding vehicle routing in road network graphs. Despite this importance, intersection localization has not been widely studied, with existing methods either ignoring the rich semantic information already computed onboard or relying on scarce, hand-labeled intersection datasets. To close this gap, we present a novel LiDAR-based method for online vehicle-centric intersection localization. We detect the intersection candidates in a bird's eye view (BEV) representation formed by concatenating a sequence of semantic road scans. We then refine these candidates by analyzing the intersecting road branches and adjusting the intersection center point in a least-squares formulation. For evaluation, we introduce an automated pipeline that pairs localized intersection points with OpenStreetMap (OSM) intersection nodes using precise GNSS/INS ground-truth poses. Experiments on the SemanticKITTI dataset show that our method outperforms the latest learning-based baseline in accuracy and reliability. Sensitivity tests demonstrate the method's robustness to challenging segmentation errors, highlighting its applicability in the real world.

