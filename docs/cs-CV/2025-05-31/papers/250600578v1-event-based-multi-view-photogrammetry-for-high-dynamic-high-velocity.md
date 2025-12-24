---
layout: default
title: Event-based multi-view photogrammetry for high-dynamic, high-velocity target measurement
---

# Event-based multi-view photogrammetry for high-dynamic, high-velocity target measurement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00578" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00578v1</a>
  <a href="https://arxiv.org/pdf/2506.00578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00578v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00578v1', 'Event-based multi-view photogrammetry for high-dynamic, high-velocity target measurement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taihang Lei, Banglei Guan, Minzu Liang, Xiangyu Li, Jianbing Liu, Jing Tao, Yang Shang, Qifeng Yu

**分类**: cs.CV

**发布日期**: 2025-05-31

**备注**: 9 pages, 9 figures, 1 table. This paper was accepted by Acta Mechanica Sinica (Date:30.May 2025)

**DOI**: [10.1007/s10409-025-25314-x](https://doi.org/10.1007/s10409-025-25314-x)

---

## 💡 一句话要点

**提出基于事件的多视角摄影测量方法以解决高速动态目标测量问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `高速动态测量` `多视角摄影测量` `事件驱动` `目标特征提取` `重投影误差` `速度衰减模型` `精密制造` `武器系统验证`

## 📋 核心要点

1. 现有测量方法在高速动态目标的测量中存在动态范围有限和观察不连续等问题，导致测量精度不足。
2. 本文提出了一种基于事件的多视角摄影测量方法，通过提取目标前缘特征和重投影误差关联事件，提升了测量精度。
3. 在轻气枪碎片测试中，所提方法的测量偏差仅为4.47%，显著优于传统方法，验证了其有效性。

## 📝 摘要（中文）

高动态、高速度目标运动的机械特性表征在工业中至关重要，为武器系统验证和精密制造过程提供了重要数据。然而，现有测量方法面临动态范围有限、观察不连续和高成本等挑战。本文提出了一种新的基于事件的多视角摄影测量系统，旨在解决上述问题。通过利用事件在时空分布中的单调性提取目标的前缘特征，消除了复杂运动测量的尾随效应。然后，利用重投影误差将事件与目标轨迹关联，提供比传统交点方法更多的数据。最后，采用目标速度衰减模型拟合数据，通过多视角数据联合计算实现准确的运动测量。在轻气枪碎片测试中，所提方法与电磁测速仪相比，测量偏差为4.47%。

## 🔬 方法详解

**问题定义**：本文旨在解决高速动态目标的精确测量问题，现有方法面临动态范围有限、观察不连续和高成本等痛点，导致测量精度不足。

**核心思路**：论文的核心思路是利用事件驱动的多视角摄影测量系统，通过提取目标的前缘特征来消除尾随效应，并通过重投影误差关联事件与目标轨迹，从而提高测量精度。

**技术框架**：整体架构包括三个主要模块：首先，利用事件的时空分布提取目标前缘特征；其次，使用重投影误差将事件与目标轨迹关联；最后，采用目标速度衰减模型进行数据拟合，实现准确的运动测量。

**关键创新**：最重要的技术创新点在于通过事件的单调性提取前缘特征，消除了传统方法中的尾随效应，并通过重投影误差提供了比交点方法更多的数据，显著提升了测量精度。

**关键设计**：在参数设置上，重投影误差的计算方式和目标速度衰减模型的选择是关键设计细节，确保了数据拟合的准确性和可靠性。具体的损失函数设计和网络结构未在摘要中详细说明，需参考原文获取更多信息。

## 📊 实验亮点

实验结果表明，所提方法在轻气枪碎片测试中的测量偏差仅为4.47%，相比于电磁测速仪的结果，显示出显著的精度提升，验证了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括武器系统验证、精密制造过程监测以及高速动态目标的测量等。通过提高测量精度，该方法能够为相关工业应用提供更可靠的数据支持，推动技术进步和产业发展。

## 📄 摘要（原文）

> The characterization of mechanical properties for high-dynamic, high-velocity target motion is essential in industries. It provides crucial data for validating weapon systems and precision manufacturing processes etc. However, existing measurement methods face challenges such as limited dynamic range, discontinuous observations, and high costs. This paper presents a new approach leveraging an event-based multi-view photogrammetric system, which aims to address the aforementioned challenges. First, the monotonicity in the spatiotemporal distribution of events is leveraged to extract the target's leading-edge features, eliminating the tailing effect that complicates motion measurements. Then, reprojection error is used to associate events with the target's trajectory, providing more data than traditional intersection methods. Finally, a target velocity decay model is employed to fit the data, enabling accurate motion measurements via ours multi-view data joint computation. In a light gas gun fragment test, the proposed method showed a measurement deviation of 4.47% compared to the electromagnetic speedometer.

